"""フレーム印・敵城行・再生産遅延をJP15.7.2実命令へ比較する。全mainの比較ではない。"""
import argparse
import ctypes as c
import itertools
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs', type=Path, required=True)
parser.add_argument('--assets', type=Path, required=True)
parser.add_argument('--library', type=Path, required=True)
parser.add_argument('--publish', action='store_true')
args = parser.parse_args()
sys.path[:0] = [str(args.python_libs.resolve())]
from stages import Native, Assets, ROOT, SHA


class Actor(c.Structure):
    _fields_ = [('words', c.c_int32 * 251)]


Pool = (Actor * 51) * 2
class TraitsNative(Native):
    allowed = set()

    def hook(self, cpu, address, size, data):
        if address in self.allowed:
            return
        return super().hook(cpu, address, size, data)


n = TraitsNative()
game = 0x40000000
n.cpu.mem_map(game, 0x500000)
with sqlite3.connect((n.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
    for address, size in db.execute("SELECT address,size FROM functions WHERE address IN ('006d6d04','00a9dce8','00a9bd84','00a9cf6c','00a06db4','0044abe4')"):
        n.ends[int(address, 16)] = int(address, 16) + size
runtime = os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name == 'nt' else None
lib = c.CDLL(str(args.library.resolve()))
lib.kbcs_audit_frame_marks.argtypes = [c.POINTER(Actor * 51), c.POINTER(c.c_int32)]
lib.kbcs_core_production_delay.argtypes = [c.c_int32] * 3 + [c.POINTER(c.c_int32)] * 3
sp = n.stack + 0x8000


def reg(i):
    return n.cpu.reg_read(getattr(n.reg, 'UC_ARM64_REG_X' + str(i)))


def setreg(name, value):
    n.cpu.reg_write(getattr(n.reg, 'UC_ARM64_REG_' + name), value)


def fragment(start, stop):
    # 通過を許すのはこの区間と指定したsetter/maxだけ。未知の外部呼出しは停止する。
    n.entry = start
    n.ends[start] = 0x6db46c if start == 0x6db348 else stop
    n.terminals = {stop}
    n.cpu.emu_start(start, n.stop + 4, count=200000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) == stop


pool = Pool()
for side in range(2):
    for slot in range(51):
        for word in range(251):
            pool[side][slot].words[word] = (side * 100003 + slot * 251 + word) % 30001
for frame in range(3):
    for side in range(2):
        for slot in range(51):
            for word in [107, 131, 191]:
                pool[side][slot].words[word] = frame + 1
    n.cpu.mem_write(game + 0x84080, bytes(pool))
    setreg('SP', sp)
    n.cpu.mem_write(sp + 0x1b0, struct.pack('<Q', game))
    modes = (c.c_int32 * 2)(1, frame % 2)
    n.helpers = {0x81f580: game, 0x5c2710: lambda: modes[(reg(0) - game - 0x2678) // 0x1f0]}
    # 実setterの本体を実行するため、フックの許可入口を登録する。
    n.allowed = {pc for a in [0xa9dce8, 0xa9bd84, 0xa9cf6c] for pc in range(a, n.ends[a], 4)}
    fragment(0x6d7dc4, 0x6d7e48)
    n.allowed = set()
    assert lib.kbcs_audit_frame_marks(pool, modes) == 0
    assert bytes(pool) == bytes(n.cpu.mem_read(game + 0x84080, c.sizeof(pool))), ('frame marks', frame)

assets = Assets(args.assets)
raw_row = next(row['cells'] for row in assets.numeric('Data/stageRA081_00.csv') if row['cells'][0] == 787)
loaded = (c.c_int32 * 14)()
lib.kbcs_core_stage_row_decode((c.c_int32 * len(raw_row))(*raw_row), len(raw_row), loaded)
n.cpu.mem_write(n.memory, bytes(loaded))
n.helpers = {}
n.call(0xa06db4, n.memory)
normalized = list(struct.unpack('<14i', n.cpu.mem_read(n.memory, 56)))
assert normalized[1:6] == [1, 0, 1, 1, 0]

delays = []
for recharge, wait, maximum, red, rate in itertools.product([60, 601], [1, 30, 60], [30, 60], [0, 15], [0, 1, 50, 100, 200]):
    values = [wait, maximum, red]
    n.cpu.mem_write(sp, bytes(0x500))
    n.cpu.mem_write(sp + 0x1e8, struct.pack('<Q', game + 0x2678))
    n.cpu.mem_write(sp + 0x1a0, struct.pack('<Q', n.memory + 0x1000))
    n.cpu.mem_write(sp + 0x360, struct.pack('<10i', rate, *([0] * 9)))
    n.cpu.mem_write(game + 0x2820, struct.pack('<i', red))

    def maximum_set():
        values[1] = c.c_int32(reg(2)).value
        return 0

    def wait_set():
        values[0] = c.c_int32(reg(2)).value
        assert reg(3) == 0
        return 0

    n.helpers = {0x58c05c: recharge, 0x5c2d18: lambda: values[0], 0x5c2e40: lambda: values[1],
                 0x5c2e88: maximum_set, 0x5c2d60: wait_set, 0x44abe4: lambda: max(c.c_int32(reg(0)).value, c.c_int32(reg(1)).value),
                 0x9019f4: 15}
    setreg('SP', sp)
    setreg('X27', game)
    fragment(0x6db348, 0x6da03c)
    values[2] = struct.unpack('<i', n.cpu.mem_read(game + 0x2820, 4))[0]
    actual = [c.c_int32(value) for value in [wait, maximum, red]]
    assert lib.kbcs_core_production_delay(recharge, rate, 15, *[c.byref(v) for v in actual]) == 0
    assert [v.value for v in actual] == values, ('delay', recharge, wait, maximum, red, rate, values)
    delays.append({'input': [recharge, rate, wait, maximum, red], 'output': values})

enemy_rows = assets.numeric('Data/t_unit.csv')
report = {'version': '15.7.2', 'nativeSha256': SHA, 'frameResets': 3, 'resetActors': 102,
          'castleRow': list(loaded), 'normalizedCastleRow': normalized,
          'castleRaw': 787, 'castleEnemy': [v or 0 for v in enemy_rows[785 + 2]['cells']],
          'breakerEnemy': [v or 0 for v in enemy_rows[35 + 2]['cells']], 'delays': delays, 'sources': assets.sources,
          'limits': ['フレーム初期化・敵城行補正・遅延区間の実命令比較。全main/GPU画素ではない', '外部の再生産getter・setter・パラメータ取得を制御']}
(ROOT / 'research/.local/battle-traits-1572.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8-sig')
if args.publish:
    (ROOT / 'native/kbcs-core/tests/battle-traits-vectors.json').write_text(json.dumps(report, ensure_ascii=False, separators=(',', ':')), encoding='utf-8-sig')
print(json.dumps({'frameResets': 3, 'delayCases': len(delays), 'castleNormalization': 'equal'}))
