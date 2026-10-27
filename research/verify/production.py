"""15.7.2 ARM64の通常生産と生成入口を局所実行する。GUIは操作しない。"""
import argparse
import json
from pathlib import Path
import sqlite3
import struct
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs', type=Path, required=True)
parser.add_argument('--publish', action='store_true')
args = parser.parse_args()
sys.path.insert(0, str(args.python_libs.resolve()))
from stages import Native, ROOT, SHA, digest


class ProductionNative(Native):
    def hook(self, cpu, address, size, data):
        if any(a <= address < self.ends[a] for a in getattr(self, 'actual', [])):
            return
        super().hook(cpu, address, size, data)


n = ProductionNative()
game = 0x40000000
n.cpu.mem_map(game, 0x500000)
with sqlite3.connect((n.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
    for address, size in db.execute("SELECT address,size FROM functions WHERE address IN ('009f4a74','005c2d18','005c2d60','005c2dd0','009f1e64','00a9400c','00a9478c','00a9486c','00a94e34','0058c05c','00aa08f8')"):
        n.ends[int(address, 16)] = int(address, 16) + size


def reg(index):
    return n.cpu.reg_read(getattr(n.reg, 'UC_ARM64_REG_X' + str(index))) & 0xffffffff


def signed(value):
    return value - 0x100000000 if value & 0x80000000 else value


def execute(case):
    n.actual = [0x5c2d60]
    n.cpu.mem_write(game, bytes(0x400000))
    slot = 2
    economy = game + 0x2678
    n.cpu.mem_write(economy + 0x108 + slot * 4, struct.pack('<i', case.get('produced', 0)))
    n.cpu.mem_write(economy + 0x14 + slot * 4, struct.pack('<i', case.get('wait', 0)))
    n.cpu.mem_write(economy + 0x40 + slot * 4, struct.pack('<i', 17))
    money = case.get('money', 100000)
    generated, calls = [], []

    def create():
        generated.append([reg(i) for i in range(1, 8)])
        return case.get('result', 1)

    def deduct():
        nonlocal money
        money += signed(reg(1))
        calls.append('money')
        return 0

    n.helpers = {
        0x5bc910: case.get('allowed', 1), 0x5bcdec: case.get('present', 1),
        0x5be130: case.get('cost', 7500), 0x5bf81c: 0,
        0x5c2d18: case.get('wait', 0), 0x5c2720: lambda: money,
        0x9e583c: case.get('blocked', 0), 0x5bbbf0: 2, 0x6505d0: 1,
        0xacf894: 29, 0xacf804: 7, 0x44abfc: lambda: min(reg(0), reg(1)),
        0x44abe4: lambda: max(signed(reg(0)), signed(reg(1))),
        0x8cfcf0: 0, 0x5bce08: 40, 0x5bc280: 42, 0x5bce20: 2,
        0x9f1e64: create, 0x7cf950: 0, 0x644304: 0, 0xa9e594: 0,
        0xa0b03c: 0, 0xaa3f20: -1, 0x5c2990: deduct,
        0x58c05c: case.get('recharge', 181),
        0x5c2f88: int(case.get('reduction', -1) >= 0),
        0x6440f0: 0, 0xa99234: max(0, case.get('reduction', -1)),
        0x5c2f30: 0, 0x457e1c: 0,
        0x459efc: lambda: calls.append(['sound', reg(1)]) or 0, 0xa60594: 0,
    }
    n.call(0x9f4a74, game, 0, slot, case.get('notifyFailure', 1))
    wait = struct.unpack('<i', n.cpu.mem_read(economy + 0x14 + slot * 4, 4))[0]
    wait_max = struct.unpack('<i', n.cpu.mem_read(economy + 0x40 + slot * 4, 4))[0]
    produced = struct.unpack('<i', n.cpu.mem_read(economy + 0x108 + slot * 4, 4))[0]
    last_cost = struct.unpack('<i', n.cpu.mem_read(economy + 0x130 + slot * 4, 4))[0]
    return {'money': money, 'wait': wait, 'maximum': wait_max, 'produced': produced,
            'lastCost': last_cost, 'generated': generated, 'calls': calls}


cases = [
    {'name': 'ordinary'}, {'name': 'money-boundary', 'money': 7500},
    {'name': 'money-short', 'money': 7499}, {'name': 'recharging', 'wait': 1},
    {'name': 'restriction', 'allowed': 0}, {'name': 'blocked', 'blocked': 1},
    {'name': 'empty', 'present': 0}, {'name': 'pool-full', 'result': -1},
    {'name': 'automatic-pool-full', 'result': -1, 'notifyFailure': 0},
    {'name': 'automatic-short-money', 'money': 7499, 'notifyFailure': 0},
    {'name': 'invalid-raw', 'result': -2}, {'name': 'slot50', 'result': 50, 'produced': 7},
    {'name': 'reduction-rounding', 'reduction': 13, 'recharge': 181},
    {'name': 'reduction-minimum', 'reduction': 99, 'recharge': 181},
    {'name': 'reduction-short-base', 'reduction': 50, 'recharge': 30},
]
vectors = [{'input': case, 'output': execute(case)} for case in cases]

# 個体能力getterより前の、実枠探索・座標設定・実RNGを使う生成入口。
placements = []
for side, raw, free, low, high, castle in [
        (0, 42, 1, 0, 9, -1), (1, 2, 50, 3, 9, -1),
        (1, 2, 1, 9, 3, -1), (1, 2, 1, 0, 0, 1),
        (0, 42, 0, 0, 9, -1), (1, -1, 1, 0, 9, -1)]:
    n.cpu.mem_write(game, bytes(0x400000))
    n.cpu.mem_write(game + 0x9ee48, struct.pack('<i', 24000))
    n.cpu.mem_write(0xc24d18, struct.pack('<I', 0x12345678))
    n.actual = [0xa9400c, 0xa9478c, 0xa9486c, 0xa94e34]
    n.helpers = {0x81f580: game, 0xa93f08: lambda: int(reg(1) != free), 0x5bbc10: castle,
                 **{a: 0 for a in [0xa94ec0, 0xa9bb38, 0xa9d498, 0xa94f4c, 0xa94fe0, 0xa95220]}}
    # RNG入口は実命令を通す。
    n.actual += [0x44a8d8, 0x44a8e8]
    n.ends[0x44a8d8] = 0x44a8e8
    n.ends[0x44a8e8] = 0x44aa50
    n.terminals = {0xaa0aa4}
    n.entry = 0x9f1e64
    for i, value in enumerate([game, side, raw, 36, low, high, 2, 0]):
        n.cpu.reg_write(getattr(n.reg, 'UC_ARM64_REG_X' + str(i)), value & 0xffffffffffffffff)
    n.cpu.reg_write(n.reg.UC_ARM64_REG_SP, n.stack + 0x8000)
    n.cpu.reg_write(n.reg.UC_ARM64_REG_LR, n.stop)
    n.cpu.emu_start(n.entry, n.stop + 4, count=20000)
    allocated = n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) == 0xaa0aa4
    slot = free if allocated else signed(reg(0))
    position = game + 0x84080 + side * 0xc804 + free * 0x3ec
    placement = list(struct.unpack('<4i', n.cpu.mem_read(position + 0xc, 16))) if allocated else None
    placements.append({'side': side, 'raw': raw, 'free': free, 'low': low, 'high': high,
                       'castle': castle, 'slot': slot, 'placement': placement,
                       'state': struct.unpack('<I', n.cpu.mem_read(0xc24d18, 4))[0]})

# ボス位置は後段の0x9f3ee0..0x9f3fb4を実行する。城設定getterのみ制御。
boss = []
for offset, scale in [(0, 127), (13, 90), (-13, 90), (0, 0)]:
    def setting():
        n.cpu.reg_write(n.reg.UC_ARM64_REG_W1, scale)
        return offset
    n.actual = []
    n.helpers = {0xa92ea0: 3200, 0x5bbfb0: 0, 0x656de0: setting}
    n.terminals = {0xa9486c}
    n.entry = 0x9f3ee0
    n.cpu.mem_write(n.stack + 0x8038, struct.pack('<Q', game))
    n.cpu.reg_write(n.reg.UC_ARM64_REG_SP, n.stack + 0x8000)
    n.cpu.emu_start(n.entry, n.stop + 4, count=1000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) == 0xa9486c
    boss.append({'castleX': 3200, 'offset': offset, 'scale': scale, 'x': signed(reg(2))})

clocks = []
for wait, recharge in [(0, 181), (1, 181), (181, 181), (182, 181), (1, 0)]:
    n.cpu.mem_write(game + 0x2678, bytes(0x200))
    n.cpu.mem_write(game + 0x2678 + 0x1c, struct.pack('<i', wait))
    n.cpu.mem_write(game + 0x2678 + 0x48, struct.pack('<i', 17))
    sounds = []
    n.actual = [0x5c2d18, 0x5c2d60, 0x5c2dd0]
    n.helpers = {0x58c05c: recharge, 0x457e1c: 0,
                 0x459efc: lambda: sounds.append(reg(1)) or 0}
    n.terminals = {0x6db700}
    n.entry = 0x6db668
    for register, value in [(19, 1), (21, 0), (23, 0x2678), (25, game), (26, 2)]:
        n.cpu.reg_write(getattr(n.reg, 'UC_ARM64_REG_X' + str(register)), value)
    n.cpu.emu_start(n.entry, n.stop + 4, count=1000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) == 0x6db700
    clocks.append({'wait': wait, 'recharge': recharge,
                   'next': struct.unpack('<i', n.cpu.mem_read(game + 0x2678 + 0x1c, 4))[0],
                   'maximum': struct.unpack('<i', n.cpu.mem_read(game + 0x2678 + 0x48, 4))[0],
                   'ready': 27 in sounds})

recharges = []
for base, talent, level, treasure, combo, rate, override in [
        (1001, 13, 29, 150, 20, 100, -1), (1001, 13, 29, 150, 13, 37, -1),
        (30, 0, 0, 0, 0, 50, -1), (30, 100, 29, 150, 100, 100, -1),
        (0, 0, 0, 0, 0, 0, -1), (1001, 13, 29, 150, 20, 100, 0),
        (1001, 13, 29, 150, 20, 100, 17)]:
    n.cpu.mem_write(game + 40 * 0x770 + 2 * 0x1dc + 0x9fd84, struct.pack('<i', base))
    for table, value in [(n.memory + 0x6000, override), (n.memory + 0x6200, rate)]:
        n.cpu.mem_write(table, struct.pack('<QQ', table + 0x100, table + 0x104))
        n.cpu.mem_write(table + 0x100, struct.pack('<i', value))
    n.actual = [0xaa08f8]
    n.terminals = set()
    n.helpers = {0x81f580: game, 0x7cf950: 0,
                 0x644304: lambda: (n.memory + 0x6000 if override >= 0 else 0) if reg(2) == 1 else n.memory + 0x6200 if reg(2) == 6 else 0,
                 0x5bce08: 40, 0x5bce20: 2, 0x5c2710: 1, 0xa9f0e0: talent,
                 0x44abe4: lambda: max(signed(reg(0)), signed(reg(1))),
                 0x58b674: level, 0xa5b084: treasure, 0x88f9e4: combo, 0x63e4a8: 0}
    value = n.call(0x58c05c, 0, 2)
    recharges.append({'input': {'base': base, 'talent': talent, 'research_level': level,
                     'treasure': treasure, 'combo': combo, 'stage_percent': rate, 'override_frames': override}, 'value': value})

report = {'version': '15.7.2', 'architecture': 'arm64-v8a', 'sha256': SHA,
          'scope': '009f4a74 regular production full control flow; getters, constructor, audio, money obfuscation controlled; actual cooldown writes. 009f1e64 allocation through first stat getter and boss coordinate slice; actual RNG/setters. 006db668..006db700 recharge slice. No spirit/multi-production/stage overrides/full actor initialization.',
          'evidence': {a: digest((n.cache / 'code' / (a + '.c')).read_bytes())
                       for a in ['009f4a74', '009f1e64', '0058c05c', '00aa08f8',
                                 '006d6d04', '005c2d18', '005c2d60', '005c2dd0',
                                 '0044a8d8', '0044a8e8', '005c3468']},
          'vectors': vectors, 'placements': placements, 'boss': boss, 'clocks': clocks, 'recharges': recharges}
(ROOT / 'research/.local/production-1572.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8-sig')
if args.publish:
    (ROOT / 'native/kbcs-core/tests/production-vectors.json').write_text(json.dumps(report, separators=(',', ':')) + '\n', encoding='utf-8')
print(json.dumps({'cases': len(vectors), 'placements': len(placements), 'boss': len(boss), 'clocks': len(clocks), 'recharges': recharges}, ensure_ascii=True))
