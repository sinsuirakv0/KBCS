"""命中本体を同版ARM64へ比較する。外部プロフィールとOS/コンテナだけを制御する。"""
import argparse
import ctypes as c
import hashlib
import itertools
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


class Actor(c.Structure):
    _fields_ = [('words', c.c_int32 * 251)]


Pool = (Actor * 51) * 2


class Environment(c.Structure):
    _fields_ = [('unit_modes', c.c_int32 * 2), *[(name, c.c_int32) for name in ['stage_width', 'castle_slot', 'castle_x', 'castle_scale', 'castle_offset', 'stage_kind', 'zombie', 'chapter_rate', 'crown', 'hp_percent', 'attack_percent']], ('crystal_max', c.c_int32 * 5), ('crystal', c.c_int32 * 5), ('treasures', c.c_int32 * 32), ('combos', c.c_int32 * 32), ('orb_stage', c.c_int32), ('talents_disabled', c.c_int32), ('parameters', c.c_int32 * 2), ('spawned', c.c_int32 * 2), ('spawn_row', c.c_int32 * 14), ('special_castle', c.c_int32)]


class Effects(c.Structure):
    _fields_ = [('fruit', c.c_int32), ('base_reductions', c.c_int32 * 4), ('sage', c.c_int32 * 11), ('notifications', c.c_int32), ('target_count', c.c_int32), ('scenario_level', c.c_int32)]


class HitContext(c.Structure):
    _fields_ = [('effects', Effects), ('form', c.c_int32), ('raw_attack', c.c_int32 * 3), ('targeted_orbs', (c.c_int32 * 2) * 5), ('fruit_rates', c.c_int32 * 32), ('orbs', (c.c_int32*4)*32), ('orb_present', c.c_int32*32), ('parameters', c.c_int32 * 5), ('base_reductions', c.c_int32 * 12), ('decoration_reductions', c.c_int32 * 3)]


class Clock(c.Structure):
    _fields_ = [('encoded', c.c_int32 * 4), ('plain', c.c_int32 * 4), ('forms', (c.c_int32 * 51) * 2), ('kill_orb', c.c_int32 * 51), ('kill_threshold', c.c_int32)]


class Damage(c.Structure):
    _fields_ = [('guard_enabled', c.c_int32), ('notice', c.c_int32 * 2), ('rows', c.c_void_p), ('states', c.c_void_p), ('count', c.c_int32)]


class DirectHit(c.Structure):
    _fields_ = [(name, c.c_int32) for name in ['side', 'slot', 'target', 'hit', 'kind', 'parameter', 'rate']] + [('flags', c.c_int32 * 12)]


class Hit(c.Structure):
    _fields_ = [('hit', DirectHit), ('attack_type', c.c_int32)]


class Events(c.Structure):
    _fields_ = [('count', c.c_int32), ('events', (c.c_int32 * 2) * 16)]


class HitNative(Native):
    def hook(self, cpu, address, size, data):
        if address in self.helpers or address in self.terminals:
            return super().hook(cpu, address, size, data)
        if address in self.allowed:
            return
        return super().hook(cpu, address, size, data)

    def value(self, index):
        return self.cpu.reg_read(getattr(self.reg, 'UC_ARM64_REG_X' + str(index)))


n = HitNative()
game, heap = 0x40000000, 0x50000000
n.cpu.mem_map(game, 0x800000)
n.cpu.mem_map(heap, 0x100000)
manifest = json.loads((ROOT / 'research/.local/actor-bindings.json').read_text(encoding='utf-8-sig'))
with sqlite3.connect((n.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
    sizes = {int(a, 16): size for a, size in db.execute("SELECT address,size FROM functions WHERE address NOT LIKE 'EXTERNAL:%'")}
n.allowed = {pc for a in [*[int(v, 16) for v in manifest['functions']], 0xa94678, 0xa956f8, 0x44abfc, 0x44abe4, 0x44a8d8, 0x44a8e8] if a in sizes for pc in range(a, a + sizes[a], 4)}
runtime = os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name == 'nt' else None
lib = c.CDLL(str(args.library.resolve()))
lib.kbcs_core_actor_last_error.restype = c.c_int64
lib.kbcs_core_actor_hit.argtypes = [c.c_void_p, c.POINTER(Actor * 51), c.POINTER(Environment), c.POINTER(HitContext), c.POINTER(Clock), c.POINTER(Damage), c.POINTER(Hit), c.POINTER(c.c_uint32), c.POINTER(c.c_int32), c.POINTER(Events)]
lib.kbcs_core_actor_hits_destroy.argtypes = [c.c_void_p]
lib.kbcs_core_actor_hits_values.argtypes = [c.c_void_p, c.c_int32, c.c_int32, c.POINTER(c.c_int32), c.c_int32, c.POINTER(c.c_int32)]


def sparse(pool):
    return [[i, v] for i, v in enumerate(struct.unpack('<25602i', bytes(pool))) if v]


def pod(value):
    if isinstance(value, c.Structure):
        return {k: pod(getattr(value, k)) for k, *_ in value._fields_}
    if isinstance(value, c.Array):
        return [pod(v) for v in value]
    return value


conditions = ['plain', 'strong', 'massive', 'extreme', 'resistant', 'super-resistant', 'witch', 'eva', 'colossus', 'behemoth', 'sage', 'villain', 'metal', 'poison', 'immunity', 'resistance', 'evasion', 'invincible', 'behemoth-evasion', 'extra-evasion', 'strengthen', 'kill-strengthen', 'weaken', 'barrier', 'shield', 'all-effects', 'curse', 'target-only', 'decoration', 'base', 'orbs', 'compound', 'castlebreaker', 'savage', 'poison-immune', 'negative', 'wrap']
records, count = [], 0
cases=[(*value,None) for value in itertools.product([0,1],conditions,[0,1],range(4),[0,1])]
cases.extend((side,condition,1,0,flags,combo) for side,condition,flags,combo in itertools.product([0,1],['massive','resistant','super-resistant','witch','eva'],[0,1],[0,99,100]))
cases.append((0,'castle-compound',0,0,1,None))
for side, condition, target, attack_type, flags_on, combo_override in cases:
    pool, environment, context, clock, damage = Pool(), Environment(), HitContext(), Clock(), Damage()
    environment.unit_modes[:] = [1, 0]
    environment.castle_slot = -1
    environment.treasures[:] = [17 + i * 2 for i in range(32)]
    environment.combos[:] = [7 + i for i in range(32)] if combo_override is None else [combo_override]*32
    context.effects.target_count = 3
    context.effects.scenario_level = 1
    context.effects.sage[:] = [50, 51, 52, 53, 54, 55, 56, 57, 70, 58, 59]
    context.effects.notifications = 1
    context.form = 2
    context.raw_attack[:] = [197, 311, 401]
    context.fruit_rates[:] = [i * 7 for i in range(32)]
    context.parameters[:] = [30, 2500, 1600, 600, 700]
    clock.forms[0][1] = 2
    clock.kill_threshold = 15
    unit, enemy = pool[0][1].words, pool[1][1].words
    for s in [0, 1]:
        for j in [0, 1]:
            w = pool[s][j].words
            for k, v in {0: 2 if j else 1, 7: 10001, 8: 10001, 11: 997, 119: 313, 120: 419, 240: 42 + s * 10 + j, 126: -1}.items():
                w[k] = v
    unit[16] = enemy[17] = 1
    trait_words = {'strong': [48], 'massive': [55], 'extreme': [161], 'resistant': [54], 'super-resistant': [160], 'witch': [110], 'eva': [145], 'colossus': [197], 'behemoth': [207], 'sage': [216]}
    for word in trait_words.get(condition, []):
        unit[word] = 1
    if condition == 'compound':
        for k in [110, 145, 197, 207, 216]:
            unit[k] = 1
        for k in [109, 144, 196, 206, 215, 244]:
            enemy[k] = 1
        unit[229] = 170
        unit[230] = 40
    if condition in ['witch','eva','colossus','behemoth','sage','villain']:
        enemy[{'witch':109,'eva':144,'colossus':196,'behemoth':206,'sage':215,'villain':244}[condition]]=1
        if condition=='colossus':unit[229],unit[230]=170,40
    defender, attacker = pool[1-side][target].words, pool[side][1].words
    if condition == 'metal':
        defender[74 if side else 43] = 1
    if condition == 'poison':
        attacker[172] = 37
    if condition in ['immunity', 'all-effects']:
        for k in [86, 179, 227]:
            defender[k] = 1
    if condition == 'resistance':
        for k in [157, 92, 245, 180]:
            defender[k] = 57
    if condition == 'evasion':
        defender[165], defender[168] = 100, 73
    if condition == 'invincible':
        defender[234] = 17
    if condition == 'behemoth-evasion':
        enemy[206], unit[207], unit[208], unit[209] = 1, 1, 100, 47
    if condition == 'extra-evasion':
        unit[235], unit[236] = 100, 71
    if condition == 'strengthen':
        attacker[8], attacker[71], attacker[72] = 1234, 50, 71
    if condition == 'kill-strengthen':
        unit[241] = 15
        clock.kill_orb[1] = 1
        context.orbs[18][0] = 37
        context.orb_present[18] = 1
    if condition == 'weaken':
        attacker[75], attacker[76], attacker[79] = 71, 10, 37
    if condition == 'barrier':
        defender[130] = 997
    if condition == 'shield':
        defender[184] = defender[190] = 997
    if condition == 'curse':
        attacker[150] = attacker[151] = 31
    if condition == 'target-only':
        unit[57], unit[16] = 1, 0
    if condition in ['base', 'compound']:
        context.base_reductions[:] = [113 + i * 17 for i in range(12)]
    if condition in ['decoration', 'compound']:
        context.decoration_reductions[:] = [1191, 2357, 3491]
        context.effects.base_reductions[:] = [117, 231, 397, 431]
    if condition in ['orbs', 'compound', 'kill-strengthen']:
        for orb in context.targeted_orbs:
            orb[:] = [17, 23]
    if condition in ['all-effects', 'compound']:
        for word, value in [(51,101),(53,103),(69,107),(70,20),(136,47),(137,21),(138,101),(148,109),(247,113)]:
            attacker[word] = value
    if condition == 'castle-compound':
        attacker[59],attacker[164]=1,211
    if condition == 'castlebreaker':
        attacker[59] = 1
    if condition == 'savage':
        attacker[164] = 211
    if condition == 'poison-immune':
        attacker[172], defender[178] = 37, 1
    if condition in ['negative', 'wrap']:
        for word in [11, 119, 120]:
            attacker[word] = -1 if condition == 'negative' else 2147483647
    call = Hit()
    call.attack_type = attack_type
    call.hit = DirectHit(side=side, slot=1, target=target, hit=count % 3, kind=count % 3, parameter=17, rate=[100, 37, 233][count % 3])
    call.hit.flags[:] = [flags_on] * 12
    if condition=='castle-compound':call.hit.kind=0;call.hit.rate=100;call.hit.hit=0
    if combo_override is not None:context.parameters[:]=[20,2500,1200,600,500]
    before = sparse(pool)
    n.cpu.mem_write(game, bytes(0x400000))
    n.cpu.mem_write(game + 0x84080, bytes(pool))
    n.cpu.mem_write(game + 0x4dc, struct.pack('<i', -1))
    n.cpu.mem_write(game + 0x9ee70, struct.pack('<QQ', n.memory, n.memory))
    n.cpu.mem_write(0xc24d18, struct.pack('<I', 0x12345678))
    for off in [0x84068, 0x2a40]:
        n.cpu.mem_write(game + off, struct.pack('<QQQ', game + off + 8, 0, 0))
    next_heap, native_events = heap, []

    def allocate():
        global next_heap
        address = next_heap
        next_heap += (n.value(0) + 15) & ~15
        assert next_heap < heap + 0x100000
        n.cpu.mem_write(address, bytes(next_heap - address))
        return address

    def notify():
        native_events.append([n.value(1), n.value(2)])
        return len(native_events)

    def parameter():
        address = n.value(1)
        head = n.cpu.mem_read(address, 24)
        data = struct.unpack_from('<Q', head, 16)[0] if head[0] & 1 else address + 1
        key = bytes(n.cpu.mem_read(data, 100)).split(b'\0')[0].decode('ascii')
        if key in manifest['effectParameters']:
            return context.effects.sage[manifest['effectParameters'].index(key)]
        if key == 'battle_powerup_kill_enemy':
            return clock.kill_threshold
        keys = ['battle_wave_s_st', 'battle_super_beast_hunter', 'battle_super_sage_hunter_damage1', 'battle_super_beast_hunter_df', 'battle_super_sage_hunter_damage2']
        assert key in keys, key
        return context.parameters[keys.index(key)]

    def reductions():
        effect = n.value(1)
        if 100 <= effect < 112:
            return context.base_reductions[effect - 100]
        if effect in [201, 203, 205]:
            return context.decoration_reductions[(effect - 201) // 2]
        return context.effects.base_reductions[(effect - 200) // 2]

    def copy_memory():
        n.cpu.mem_write(n.value(0), bytes(n.cpu.mem_read(n.value(1), n.value(2))))
        return n.value(0)

    def find_word():
        address, value, length = n.value(0), n.value(1) & 0xffffffff, n.value(2)
        for k in range(length):
            if struct.unpack('<I', n.cpu.mem_read(address + k * 4, 4))[0] == value:
                return address + k * 4
        return 0

    def make_string():
        address, source = n.value(0), n.value(1)
        data = bytes(n.cpu.mem_read(source, 100)).split(b'\0')[0]
        if len(data) < 23:
            n.cpu.mem_write(address, bytes([len(data)*2])+data+b'\0'+bytes(22-len(data)))
        else:
            global next_heap
            n.cpu.mem_write(next_heap, data+b'\0')
            n.cpu.mem_write(address, struct.pack('<QQQ', 1, len(data), next_heap))
            next_heap += (len(data)+16)&~15
        return address

    n.helpers = {0x81f580: game, 0x5c2710: lambda: environment.unit_modes[(n.value(0)-game-0x2678)//0x1f0], 0x5bc1dc: lambda: n.value(1), 0x5bce20: context.form, 0x5bbc10: 0xffffffffffffffff, 0x5bbbc8: 0,
                 0x65f698: 0, 0x66ba4c: 0, 0x419064: 0, 0xbdaf40: allocate, 0xbdaf60: 0, 0xbdb0b0: copy_memory,
                 0x63c178: 0, 0x63c21c: 0, 0x63c3a0: 0, 0x63c480: 0, 0x68c30c: 0, 0x68c330: 0, 0x8cfcf0: 0, 0x63a050: reductions,
                 0x663c44: lambda: context.targeted_orbs[n.value(2)][n.value(3)], 0x66398c: lambda: context.orbs[n.value(2)][n.value(3)], 0x66367c: lambda: clock.kill_orb[1],
                 0xa5b084: lambda: environment.treasures[n.value(1)], 0xa5b1b4: lambda: context.fruit_rates[n.value(1)], 0x88f9e4: lambda: environment.combos[n.value(1)],
                 0xa9fb88: lambda: context.raw_attack[n.value(5)], 0x5bc198: 1, 0x9d49e4: 1, 0xa960ac: 3, 0x9d4e1c: notify, 0x9019f4: parameter,
                 0x41b298: make_string}
    # wmemchrは実シンボルを呼出先検出で特定して固定する。
    n.helpers[0xbdb500] = find_word
    n.entry = 0x6e79bc if side else 0x6e4aec
    n.ends[n.entry] = n.entry + sizes[n.entry]
    sp = n.stack + 0x8000
    n.cpu.mem_write(n.stack, bytes(0x10000))
    h, f = call.hit, list(call.hit.flags)
    values = [game, attack_type, 1, target, h.hit, h.kind, f[0], f[5], f[1], f[2], f[3], f[4], f[6], f[8], f[7], f[9] if side else 0, f[10], f[11] if side else h.parameter, h.rate]
    for i, value in enumerate(values[:8]):
        n.cpu.reg_write(getattr(n.reg, 'UC_ARM64_REG_X' + str(i)), value)
    n.cpu.mem_write(sp, struct.pack('<11Q', *values[8:]))
    n.cpu.reg_write(n.reg.UC_ARM64_REG_SP, sp)
    n.cpu.reg_write(n.reg.UC_ARM64_REG_LR, n.stop)
    try:
        n.cpu.emu_start(n.entry, n.stop + 4, count=200000)
    except Exception as error:
        raise RuntimeError((count, side, condition, target, attack_type, flags_on, hex(n.cpu.reg_read(n.reg.UC_ARM64_REG_PC)))) from error
    assert n.cpu.reg_read(n.reg.UC_ARM64_REG_PC) == n.stop, 'hit budget'
    expected = bytes(n.cpu.mem_read(game + 0x84080, c.sizeof(pool)))
    expected_applied = n.value(0) & 0xffffffff
    expected_seed = struct.unpack('<I', n.cpu.mem_read(0xc24d18, 4))[0]
    owner = c.c_void_p()
    assert lib.kbcs_core_actor_hits_create(c.byref(owner)) == 0
    seed, applied, events = c.c_uint32(0x12345678), c.c_int32(-1), Events()
    code = lib.kbcs_core_actor_hit(owner, pool, c.byref(environment), c.byref(context), c.byref(clock), c.byref(damage), c.byref(call), c.byref(seed), c.byref(applied), c.byref(events))
    diff = [(i, a, b) for i, (a, b) in enumerate(zip(struct.unpack('<25602i', expected), struct.unpack('<25602i', bytes(pool)))) if a != b]
    assert not code and not diff and expected_applied == applied.value and seed.value == expected_seed, (count, side, condition, target, attack_type, flags_on, code, hex(lib.kbcs_core_actor_last_error()), diff[:20], expected_applied, applied.value, expected_seed, seed.value)
    assert [list(v) for v in events.events[:events.count]] == native_events
    def native_values(offset, key):
        node = struct.unpack('<Q', n.cpu.mem_read(game+offset+8, 8))[0]
        while node:
            found = struct.unpack('<i', n.cpu.mem_read(node+32, 4))[0]
            if found == key:
                start, end = struct.unpack('<QQ', n.cpu.mem_read(node+40, 16))
                return list(struct.unpack('<'+'i'*((end-start)//4), n.cpu.mem_read(start, end-start)))
            node = struct.unpack('<Q', n.cpu.mem_read(node+(0 if key<found else 8), 8))[0]
        return []
    reservations = []
    for kind, offset, key in [(0, 0x84068, target), (1, 0x2a40, pool[1][target].words[240])]:
        values, length = (c.c_int32*1024)(), c.c_int32()
        assert lib.kbcs_core_actor_hits_values(owner, kind, key, values, 1024, c.byref(length)) == 0
        actual = list(values[:length.value])
        assert actual == native_values(offset, key), ('bookkeeping', count, kind, actual, native_values(offset, key))
        reservations.append(actual)
    lib.kbcs_core_actor_hits_destroy(owner)
    if count % 83 == 0 or condition in ['compound', 'evasion', 'poison'] and target and attack_type == 0 or combo_override is not None and condition in ['witch','eva'] and flags_on or condition=='castle-compound':
        records.append({'side': side, 'condition': condition, 'before': before, 'after': sparse(pool), 'environment': pod(environment), 'context': pod(context), 'clock': pod(clock), 'call': pod(call), 'applied': applied.value, 'seed': seed.value, 'events': native_events, 'reservations': reservations})
    count += 1
print(json.dumps({'hitCases': count, 'published': len(records)}))
report = {'version': '15.7.2', 'sha256': SHA, 'librarySha256': hashlib.sha256(args.library.read_bytes()).hexdigest(), 'cases': count, 'records': records,
          'controlled': ['profile/form/orb/treasure/combo/parameter inputs', 'attribute map construction and destruction', 'allocation and tree rebalance', 'debug strings', 'notifications'], 'entries': ['006e4aec', '006e79bc']}
(ROOT / 'research/.local/actor-hit-1572.json').write_text(json.dumps(report, indent=2), encoding='utf-8-sig')
if args.publish:
    (ROOT / 'native/kbcs-core/tests/actor-hit-vectors.json').write_text(json.dumps(report, separators=(',', ':')), encoding='utf-8-sig')
