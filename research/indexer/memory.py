import argparse
import ctypes
import json
import os
import time
from ctypes import wintypes
from pathlib import Path

from indexer.store import configure_output, write_json


class ProcessEntry(ctypes.Structure):
    _fields_ = [('size', wintypes.DWORD), ('usage', wintypes.DWORD), ('pid', wintypes.DWORD),
                ('heap', ctypes.c_size_t), ('module', wintypes.DWORD), ('threads', wintypes.DWORD),
                ('parent', wintypes.DWORD), ('priority', wintypes.LONG), ('flags', wintypes.DWORD),
                ('name', wintypes.WCHAR * 260)]


class MemoryCounters(ctypes.Structure):
    _fields_ = [('size', wintypes.DWORD), ('faults', wintypes.DWORD)] + [
        (name, ctypes.c_size_t) for name in ('peak_working', 'working', 'paged_peak', 'paged',
                                           'nonpaged_peak', 'nonpaged', 'pagefile', 'pagefile_peak', 'private')]


def processes():
    kernel = ctypes.windll.kernel32
    kernel.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    snapshot = kernel.CreateToolhelp32Snapshot(2, 0)
    if snapshot == wintypes.HANDLE(-1).value:
        return []
    entry = ProcessEntry()
    entry.size = ctypes.sizeof(entry)
    rows = []
    try:
        kernel.Process32FirstW.argtypes = [wintypes.HANDLE, ctypes.c_void_p]
        kernel.Process32NextW.argtypes = [wintypes.HANDLE, ctypes.c_void_p]
        found = kernel.Process32FirstW(snapshot, ctypes.byref(entry))
        while found:
            rows.append((entry.pid, entry.parent, entry.name))
            found = kernel.Process32NextW(snapshot, ctypes.byref(entry))
    finally:
        kernel.CloseHandle(snapshot)
    return rows


def enforce_memory(java_pid, root, limit_mb=1536):
    # 自分が起動したJVM直下のデコンパイラだけを対象にし、時間では停止しない。
    if os.name != 'nt':
        return 0, True
    rows = processes()
    alive = any(pid == java_pid and name.lower() == 'java.exe' for pid, _, name in rows)
    peak = 0
    kernel = ctypes.windll.kernel32
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
    query = ctypes.windll.psapi.GetProcessMemoryInfo
    query.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD]
    for pid, parent, name in rows:
        if parent != java_pid or name.lower() != 'decompile.exe':
            continue
        handle = kernel.OpenProcess(0x0411, False, pid)
        if not handle:
            continue
        try:
            counters = MemoryCounters()
            counters.size = ctypes.sizeof(counters)
            if not query(handle, ctypes.byref(counters), counters.size):
                continue
            peak = max(peak, counters.private)
            if limit_mb and counters.private > limit_mb * 1024**2:
                event = {'unix': time.time(), 'pid': pid, 'private_bytes': counters.private,
                         'limit_mb': limit_mb, 'reason': 'native decompiler memory budget exceeded'}
                if kernel.TerminateProcess(handle, 1):
                    with (root / 'memory-events.jsonl').open('a', encoding='utf-8') as stream:
                        stream.write(json.dumps(event) + '\n')
        finally:
            kernel.CloseHandle(handle)
    return peak, alive


def main():
    configure_output()
    parser = argparse.ArgumentParser()
    parser.add_argument('--java-pid', required=True, type=int)
    parser.add_argument('--cache', required=True, type=Path)
    parser.add_argument('--limit-mb', type=int, default=1536)
    args = parser.parse_args()
    peak = 0
    while True:
        current, alive = enforce_memory(args.java_pid, args.cache, args.limit_mb)
        peak = max(peak, current)
        write_json(args.cache / 'native-memory-metrics.json', {'observed_peak_private_bytes': peak, 'limit_mb': args.limit_mb})
        if not alive:
            break
        time.sleep(2)


if __name__ == '__main__':
    main()
