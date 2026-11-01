"""ゾンビキラーの同F/後続Fを、各段階の全個体/RNG/死亡通知までARM64へ比較する。"""
import argparse
import ast
import ctypes as c
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs', type=Path, required=True)
parser.add_argument('--library', type=Path, required=True)
parser.add_argument('--publish', action='store_true')
args = parser.parse_args()
sys.path.insert(0, str(args.python_libs.resolve()))
from stages import Native, ROOT, SHA

# 既存の命中照合と同じPOD/実命令フック。既存試験のループは実行しない。
tree = ast.parse((ROOT / 'research/verify/actor_hit.py').read_text(encoding='utf-8-sig'))
exec(compile(ast.Module(body=[node for node in tree.body if isinstance(node, ast.ClassDef)], type_ignores=[]), 'actor_hit.py', 'exec'))
Pool = (Actor * 51) * 2
class Cannon(c.Structure): _fields_ = [('segments', ((c.c_int32 * 3) * 15) * 2)]
class Rules(c.Structure): _fields_ = [('encoded', c.c_int32 * 4), ('attack_rate', c.c_int32)]
class Health(c.Structure): _fields_ = [(k, c.c_int32) for k in ['deployment_slot', 'cooldown', 'preserve_enemy_castle']]
class HealthResult(c.Structure): _fields_ = [(k, c.c_int32) for k in ['previous_hp', 'delay_slot', 'delay_frames', 'delay_x', 'delay_y', 'sound']]
class Reaction(c.Structure): _fields_ = [('previous_hp', c.c_int32), ('death_visual_available', c.c_int32)]
class ReactionResult(c.Structure): _fields_ = [('sound_count', c.c_int32), ('sounds', c.c_int32 * 2), ('death_visual', c.c_int32), ('death_x', c.c_int32), ('death_y', c.c_int32)]
class Protection(c.Structure): _fields_ = [('shield_hit', c.c_int32), ('sound_count', c.c_int32), ('sounds', c.c_int32 * 2), ('visual_count', c.c_int32), ('visuals', (c.c_int32 * 4) * 2)]

n = HitNative()
game, heap = 0x40000000, 0x50000000
n.cpu.mem_map(game, 0x800000)
n.cpu.mem_map(heap, 0x100000)
manifest = json.loads((ROOT / 'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
    sizes = {int(a, 16): size for a, size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.ends.update({a: a + size for a, size in sizes.items()})
n.allowed = {pc for a in [*[int(v, 16) for v in manifest['functions']], 0xa94678, 0xa956f8, 0x44abfc, 0x44abe4, 0x44a8d8, 0x44a8e8, 0x5bb5a0] if a in sizes for pc in range(a, a + sizes[a], 4)}
runtime = os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name == 'nt' else None
lib = c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_hits_destroy.argtypes = [c.c_void_p]
ptr = c.POINTER(Actor * 51)
lib.kbcs_core_actor_frame_marks.argtypes = [ptr, c.POINTER(Environment)]
lib.kbcs_core_actor_begin.argtypes = [ptr, c.POINTER(Environment), c.c_int32, c.c_int32]
lib.kbcs_core_actor_hit.argtypes = [c.c_void_p, ptr, c.POINTER(Environment), c.POINTER(HitContext), c.POINTER(Clock), c.POINTER(Damage), c.POINTER(Hit), c.POINTER(c.c_uint32), c.POINTER(c.c_int32), c.POINTER(Events)]
lib.kbcs_core_actor_cannon_hit.argtypes = [c.POINTER(Cannon), ptr, c.POINTER(Environment), c.POINTER(HitContext), c.POINTER(Clock), c.POINTER(Damage), c.POINTER(Rules), c.c_int32, c.c_int32, c.c_int32, c.POINTER(c.c_uint32), c.POINTER(Events)]
lib.kbcs_core_actor_health.argtypes = [ptr, c.c_int32, c.c_int32, c.POINTER(Health), c.POINTER(c.c_uint32), c.POINTER(HealthResult)]
lib.kbcs_core_actor_react.argtypes = [ptr, c.POINTER(Environment), c.c_int32, c.c_int32, c.POINTER(Reaction), c.POINTER(c.c_uint32), c.POINTER(ReactionResult)]
lib.kbcs_core_actor_protect.argtypes = [ptr, c.c_int32, c.c_int32, c.POINTER(Protection)]

def sparse(pool): return [[i, v] for i, v in enumerate(struct.unpack('<25602i', bytes(pool))) if v]
def put(offset, value): n.cpu.mem_write(game + offset, struct.pack('<i', value))
def allocate():
    global next_heap
    address = next_heap
    next_heap += (n.value(0) + 15) & ~15
    assert next_heap < heap + 0x100000
    n.cpu.mem_write(address, bytes(next_heap - address))
    return address
def find_word():
    address, value, length = n.value(0), n.value(1) & 0xffffffff, n.value(2)
    for i in range(length):
        if struct.unpack('<I', n.cpu.mem_read(address + i * 4, 4))[0] == value: return address + i * 4
    return 0
def fragment(start, stop, *other_stops):
    n.entry, n.terminals = start, {stop, *other_stops}
    if stop != n.stop: n.ends[start] = max(n.terminals)
    n.cpu.emu_start(start, n.stop + 4, count=200000)
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) in n.terminals
    n.terminals = set()
def setreg(name, value): n.cpu.reg_write(getattr(n.reg, 'UC_ARM64_REG_' + name), value)

records = []
for source, gap, lethal in [('angel', 0, True), ('unit', 0, True), ('angel', 1, True), ('unit', 3, True), ('unit', 0, False)]:
    pool, env, context, clock, damage, cannon = Pool(), Environment(), HitContext(), Clock(), Damage(), Cannon()
    env.unit_modes[:] = [1, 0]
    env.castle_slot = -1
    context.effects.target_count = context.effects.scenario_level = 1
    rules = Rules((c.c_int32 * 4)(27, 31, 22, 13), 100)
    for side, slot in [(0, 1), (0, 2), (1, 1)]:
        for word, value in {0: 2, 7: 10000, 8: 10000, 9: 1, 11: 100 if slot == 1 else 10000, 126: -1, 240: side * 10 + slot}.items(): pool[side][slot].words[word] = value
    pool[0][1].words[108] = pool[1][1].words[47] = 1
    for word, value in {0: 1, 7: 236000, 8: 236000, 17: 5, 21: 1000, 30: 150, 31: 200}.items(): pool[0][0].words[word] = value
    initial = sparse(pool)
    n.cpu.mem_write(game, bytes(0x800000))
    n.cpu.mem_write(game + 0x84080, bytes(pool))
    n.cpu.mem_write(0xc24d18, struct.pack('<I', 0x12345678))
    put(0x4dc, -1)
    for offset in [0x84068, 0x2a40]: n.cpu.mem_write(game + offset, struct.pack('<QQQ', game + offset + 8, 0, 0))
    next_heap = heap
    sounds = []
    def sound(): sounds.append(n.value(1)); return 0
    n.helpers = {0x81f580: game, 0x5c2710: lambda: env.unit_modes[(n.value(0) - game - 0x2678) // 0x1f0],
                 0x457e1c: 0, 0x459efc: sound, 0x459f04: sound, 0x5bbc10: -1, 0x5bbbc8: 0,
                 0x5bce20: 0, 0x5bc1dc: 0, 0x5c2d18: 0, 0xa9fb88: 100, 0xa5b084: 0, 0xa5b1b4: 0, 0x88f9e4: 0,
                 0x5bc198: 1, 0x9d49e4: 1, 0xa960ac: 1, 0x9d4e1c: 0, 0x9019f4: 0,
                 0x63c178: 0, 0x63c480: 0, 0x68c330: 0, 0x8cfcf0: 0, 0x63a050: 0,
                 0x419064: 0, 0xbdaf40: allocate, 0xbdaf60: 0, 0x65f698: 0, 0x66ba4c: 0,
                 0xbdb500: find_word, 0xbdb0b0: lambda: n.cpu.mem_write(n.value(0), bytes(n.cpu.mem_read(n.value(1), n.value(2)))) or n.value(0),
                 0x663c44: 0, 0x66398c: 0, 0x66367c: 0, 0x63c21c: 0, 0x63c3a0: 0, 0x68c30c: 0,
                 0xbdb160: lambda: n.cpu.mem_write(n.value(8), bytes(24)) or 0,
                 0xa94074: lambda: n.cpu.mem_write(n.value(8), bytes(24)) or 0,
                 0x41b298: lambda: n.cpu.mem_write(n.value(0), bytes(24)) or 0}
    owner, seed, steps = c.c_void_p(), c.c_uint32(0x12345678), []
    assert lib.kbcs_core_actor_hits_create(c.byref(owner)) == 0
    def check(kind, slot=1):
        expected = bytes(n.cpu.mem_read(game + 0x84080, c.sizeof(pool)))
        assert bytes(pool) == expected, (source, gap, lethal, kind, [(i // 12801, i % 12801 // 251, i % 251, a, b) for i, (a, b) in enumerate(zip(struct.unpack('<25602i', expected), struct.unpack('<25602i', bytes(pool)))) if a != b][:8])
        assert seed.value == struct.unpack('<I', n.cpu.mem_read(0xc24d18, 4))[0], (kind, 'RNG')
        steps.append({'kind': kind, 'slot': slot, 'after': sparse(pool), 'seed': seed.value})
    def begin():
        sp = n.stack + 0x8000
        setreg('SP', sp)
        n.cpu.mem_write(sp + 0x1b0, struct.pack('<Q', game))
        fragment(0x6d7dc4, 0x6d7e48)
        assert lib.kbcs_core_actor_frame_marks(pool, c.byref(env)) == 0
        check('marks')
        n.cpu.mem_write(sp + 0xb8, struct.pack('<QQ', game + 0x84080, 1))
        setreg('W19', 1); setreg('X26', 1)
        fragment(0x6ece50, 0x6ecf90)
        assert lib.kbcs_core_actor_begin(pool, c.byref(env), 1, 1) == 0
        check('begin')
    def hit(slot):
        values = [game, 0, slot, 1, 0, 0, 0, 0, *([0] * 10), 100]
        sp = n.stack + 0x8000
        n.cpu.mem_write(sp, struct.pack('<11Q', *values[8:]))
        for i, value in enumerate(values[:8]): setreg('X' + str(i), value)
        setreg('SP', sp); setreg('LR', n.stop)
        fragment(0x6e4aec, n.stop)
        call = Hit(DirectHit(0, slot, 1, 0, 0, 0, 100), 0)
        applied, events = c.c_int32(), Events()
        assert lib.kbcs_core_actor_hit(owner, pool, c.byref(env), c.byref(context), c.byref(clock), c.byref(damage), c.byref(call), c.byref(seed), c.byref(applied), c.byref(events)) == 0
        assert applied.value == 1
        check('hit', slot)
    def settle():
        # 無保護対象でも原本の区間を実行し、次のhealthへ状態を引き継ぐ。
        sp, tree = n.stack + 0x8000, n.memory + 0x4000
        n.cpu.mem_write(tree, struct.pack('<QQQ', tree + 8, 0, 0))
        n.cpu.mem_write(sp, bytes(0x500))
        for offset, value in [(0x1e8, tree + 8), (0x140, game + 0x9e750), (0x1e0, game + 0x9ea98), (0x1f0, game + 0x84080), (0x1d8, game + 0x90884)]: n.cpu.mem_write(sp + offset, struct.pack('<Q', value))
        for name, value in [('SP', sp), ('X23', tree), ('W27', 1), ('W28', 1)]: setreg(name, value)
        fragment(0x6d97dc, 0x6d9da0, 0x6d9510)
        protection = Protection()
        assert lib.kbcs_core_actor_protect(pool, 1, 1, c.byref(protection)) == 0
        assert protection.sound_count == protection.visual_count == protection.shield_hit == 0
        check('protect')
        sp = n.stack + 0x8000
        n.cpu.mem_write(sp, bytes(0x500))
        for offset, value in [(0x1f0, game + 0x84080), (0x1d8, game + 0x90884)]: n.cpu.mem_write(sp + offset, struct.pack('<Q', value))
        for name, value in [('SP', sp), ('X19', game + 0x90c70), ('X27', game), ('W26', 1), ('W28', 1), ('W24', 0)]: setreg(name, value)
        fragment(0x6da994, 0x6dac68)
        out = HealthResult()
        assert lib.kbcs_core_actor_health(pool, 1, 1, c.byref(Health(-1, 0, 0)), c.byref(seed), c.byref(out)) == 0
        check('health')
        before = out.previous_hp
        if pool[1][1].words[8] < 1:
            pool[1][1].words[8] = 0
            n.cpu.mem_write(game + 0x90c70 + 8 * 4, struct.pack('<i', 0))
        n.cpu.mem_write(sp + 0x80, struct.pack('<Q', game + 0x9e570))
        for name, value in [('SP', sp), ('X19', game + 0x90c70), ('W21', before), ('W26', 1), ('W28', 1), ('W24', 0)]: setreg(name, value)
        fragment(0x6dac8c, 0x6db1ac)
        result = ReactionResult()
        assert lib.kbcs_core_actor_react(pool, c.byref(env), 1, 1, c.byref(Reaction(before, 1)), c.byref(seed), c.byref(result)) == 0
        assert list(result.sounds)[:result.sound_count] == sounds
        assert bool(result.death_visual) == bool(n.cpu.mem_read(game + 0x9e570, 1)[0] & 1)
        if result.death_visual: assert [result.death_x, result.death_y] == list(struct.unpack('<ii', n.cpu.mem_read(game + 0x9e574, 8)))
        sounds.clear()
        check('react')
        steps[-1].update({'sounds': list(result.sounds)[:result.sound_count], 'deathVisual': result.death_visual, 'deathX': result.death_x, 'deathY': result.death_y})
    begin()
    if source == 'angel':
        n.call(0x5d6c3c, game, 0, 1, 7)
        events = Events()
        assert lib.kbcs_core_actor_cannon_hit(c.byref(cannon), pool, c.byref(env), c.byref(context), c.byref(clock), c.byref(damage), c.byref(rules), 0, 1, 7, c.byref(seed), c.byref(events)) == 0
        check('angel')
    else: hit(1)
    assert pool[1][1].words[107] == 1
    if gap:
        settle()
        for _ in range(gap): begin()
    if lethal: hit(2)
    settle()
    assert pool[1][1].words[114] == int(lethal and gap == 0), (source, gap, lethal, pool[1][1].words[114])
    records.append({'source': source, 'gap': gap, 'lethal': lethal, 'initial': initial, 'steps': steps})
    lib.kbcs_core_actor_hits_destroy(owner)

report = {'version': '15.7.2', 'sha256': SHA, 'sequences': records, 'limits': ['制御した直接命中/砲撃/被弾/死亡の連続区間。全mainの自動行動やGPU画素を比較したものではない', '無保護対象。保護は既存の独立したARM照合を使用']}
(ROOT / 'research/.local/battle-trait-sequence-1572.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8-sig')
if args.publish:
    path = ROOT / 'native/kbcs-core/tests/battle-traits-vectors.json'
    fixture = json.loads(path.read_text(encoding='utf-8-sig'))
    fixture['sequences'] = records
    path.write_text(json.dumps(fixture, ensure_ascii=False, separators=(',', ':')), encoding='utf-8-sig')
print(json.dumps({'sequences': len(records), 'phases': sum(len(case['steps']) for case in records)}))
