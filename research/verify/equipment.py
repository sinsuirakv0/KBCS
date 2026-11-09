"""本能玉310件・複数枠・属性木をJP15.7.2 ARM64の取得関数へ渡す。"""
import argparse
import ctypes as c
import json
import os
from pathlib import Path
import sqlite3
import struct
import sys

from stages import Assets, Native, ROOT, SHA, digest


class EquipmentNative(Native):
    def hook(self, cpu, address, size, data):
        if address not in self.helpers and any(start <= address < end for start, end in self.functions):
            return
        super().hook(cpu, address, size, data)


class Orb(c.Structure):
    _fields_ = [('effect', c.c_int32), ('mask', c.c_int32), ('values', c.c_int32 * 4)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python-libs', type=Path, required=True)
    parser.add_argument('--library', type=Path, required=True)
    parser.add_argument('--assets', type=Path, required=True)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    sys.path.insert(0, str(args.python_libs.resolve()))
    assets = Assets(args.assets)
    raw = assets.text('Data/equipmentlist.json')
    attribute_csv = assets.text('Data/equipment_attribute.csv')
    items = json.loads(raw)['ID']
    masks = [sum(bit << index for index, bit in enumerate(row['cells'][:12]))
             for row in assets.numeric('Data/equipment_attribute.csv')]
    assert len(items) == 310 and {item['content'] for item in items} == set(range(26))
    assert len({(item['content'], item.get('attribute'), item['gradeID']) for item in items}) == 310
    highest = {5, 9, 10, 11, 13, 16, 17, 18, 19, 22, 24}
    runtime = os.add_dll_directory('D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin') if os.name == 'nt' else None
    lib = c.CDLL(str(args.library.resolve()))
    lib.kbcs_audit_equipment.argtypes = [c.POINTER(Orb), c.POINTER(c.c_int32), c.c_int32, c.c_uint32,
                                        c.POINTER(c.c_int32 * 4), c.POINTER(c.c_int32)]
    n = EquipmentNative()
    getter = {0: 0x663c44, 1: 0x66398c, 2: 0x663af4}
    target_getters = [0xaa30a8, 0xaa3168, 0xaa3228, 0xaa32e8, 0xaa33a8, 0xa9f838,
                      0xaa3468, 0xaa3528, 0xaa35e8, 0xaa4b70, 0xaa4c30, 0xaa3bec]
    addresses = [*getter.values(), 0x66367c, 0x661498, 0x66141c, 0x661a60, 0x661b30, 0x63e8b4,
                 0x65f258, 0xaa1a68, 0xaa1c24, 0xaa1afc, 0xaa3aa8, 0xaa5f84, *target_getters]
    with sqlite3.connect((n.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
        for address in addresses:
            n.ends[address] = address + db.execute('SELECT size FROM functions WHERE address=?',
                                                  (f'{address:08x}',)).fetchone()[0]
    n.functions = [(address, n.ends[address]) for address in addresses]
    m = n.memory
    table, records, attributes, capacity, conditions = [m + offset for offset in [0x200, 0x1000, 0x6000, 0x6100, 0x6180]]
    game = 0x40000000
    n.cpu.mem_map(game, 0x500000)
    unit = 83

    def put(address, fmt, *values):
        n.cpu.mem_write(address, struct.pack('<' + fmt, *values))

    def register(index):
        return n.cpu.reg_read(getattr(n.reg, 'UC_ARM64_REG_X' + str(index)))

    def record(index, item):
        address = records + index * 64
        values = item['value']
        put(table + index * 8, 'Q', address)
        put(address + 4, 'iiiQQQ', item['gradeID'], item.get('attribute', -1), item['content'],
            address + 40, address + 40 + len(values) * 4, address + 40 + len(values) * 4)
        put(address + 40, f'{len(values)}i', *values)

    for index, item in enumerate(items):
        record(index, item)
    put(m, '3Q', table, table + len(items) * 8, table + len(items) * 8)
    put(m + 48, '3Q', attributes, attributes + len(masks) * 4, attributes + len(masks) * 4)
    put(attributes, f'{len(masks)}I', *masks)
    put(m + 0x80, 'Q', capacity)
    put(capacity + 32, 'i4xI4xQQQ', unit, 2, conditions, conditions + 8, conditions + 8)
    _, slot_count, *codes = next(row['cells'] for row in assets.numeric('Data/equipmentslot.csv') if row['cells'][0] == unit)
    assert slot_count == 2
    put(conditions, 'ii', *codes)
    selected = []
    disabled = 0

    def slot_map():
        # 00661ce4のstd::mapコピーのみ制御し、00661498の探索はARM64で実行する。
        result = register(8)
        nodes = m + 0x6300
        put(result, 'QQQ', nodes if selected else result + 8, nodes if selected else 0, len(selected))
        for slot, index in enumerate(selected):
            put(nodes + slot * 48, 'QQQ4xii', 0, nodes + (slot + 1) * 48 if slot + 1 < len(selected) else 0,
                nodes + (slot - 1) * 48 if slot else result + 8, slot, index)
        return 0

    n.helpers = {0x81f580: game, 0x8cfcf0: lambda: disabled, 0x661ce4: slot_map, 0x59d12c: 0}
    assert n.call(0x66141c, m, unit) == 2
    for level, plus in [(59, 0), (59, 1), (60, 0), (57, 2)]:
        n.helpers.update({0xacf894: level - 1, 0xacf804: plus})
        for slot in range(2):
            assert n.call(0x661b30, m, unit, slot) == int(slot == 0 or level + plus >= 60)

    def compare(indices, trait_bits):
        selected[:] = indices
        put(capacity + 40, 'i', len(indices))
        tree, nodes = m + 0x6500, m + 0x6520
        put(tree, 'QQQ', nodes if trait_bits else tree + 8, nodes if trait_bits else 0, len(trait_bits))
        for index, (mask, enabled) in enumerate(trait_bits):
            put(nodes + index * 48, 'QQQ4xIB', 0,
                nodes + (index + 1) * 48 if index + 1 < len(trait_bits) else 0,
                nodes + (index - 1) * 48 if index else tree + 8, mask, enabled)
        native_values = []
        effects = {items[index]['content'] for index in indices}
        mask = 0
        for flag, enabled in trait_bits:
            if enabled:
                mask |= flag
        for effect in sorted(effects):
            mode = 0 if effect < 5 else 1 if effect in highest else 2
            values = []
            for parameter in range(len(next(item['value'] for item in items if item['content'] == effect))):
                arguments = (m, unit, effect, parameter, tree, 0) if mode == 0 else (m, unit, effect, parameter, 0)
                values.append(c.c_int32(n.call(getter[mode], *arguments)).value)
            present = n.call(0x66367c, m, unit, effect)
            native_values.append([effect, values, present])
        assert n.call(0x66367c, m, unit, 31) == 0
        rows = [items[index] for index in indices]
        orbs = (Orb * len(rows))(*(Orb(item['content'], masks[item['attribute']] if 'attribute' in item else 0,
                                       (c.c_int32 * 4)(*item['value'])) for item in rows))
        grades = (c.c_int32 * len(rows))(*(item['gradeID'] for item in rows))
        values, present = ((c.c_int32 * 4) * 26)(), (c.c_int32 * 26)()
        assert lib.kbcs_audit_equipment(orbs, grades, len(rows), mask, values, present) == 0
        for effect, expected, exists in native_values:
            assert list(values[effect])[:len(expected)] == expected and present[effect] == exists, (indices, mask, effect, expected)
        return {'ids': [30000 + index for index in indices], 'mask': mask, 'results': native_values}

    witnesses = []
    for index, item in enumerate(items):
        trait = masks[item['attribute']] if 'attribute' in item else 0
        compare([index], [(trait, True)] if trait else [])
    for effect in range(26):
        grades = {item['gradeID']: i for i, item in enumerate(items)
                  if item['content'] == effect and item.get('attribute', 0) == 0}
        s, a = grades[4], grades[3]
        for pair in [[s, a], [a, s], [s, s], [grades[0], grades[1]]]:
            witnesses.append(compare(pair, [(1, True), (2, True)]))
    for pair, flags in [
        ([4, 14], [(1, True), (2, True)]), ([4, 14], [(1, True), (2, False)]),
        ([4, 14], [(4, True)]), ([4, 9], [(1, True)]),
        ([234, 279], [(1, True)]), ([], []),
    ]:
        witnesses.append(compare(pair, flags))
    # 同じ等級でも異なる配列なら、先に走査した玉が残る。
    original = items[233]
    items[233] = {**original, 'gradeID': 4}
    record(233, items[233])
    compare([233, 234], [])
    compare([234, 233], [])
    items[233] = original
    record(233, original)
    selected[:] = [234, 209]
    put(capacity + 40, 'i', 2)
    assert n.call(0x66398c, m, unit, 10, 0, 123) == 160
    assert n.call(0x66398c, m, unit, 11, 0, 123) == 123
    disabled = 1
    assert n.call(0x66398c, m, unit, 10, 0, 123) == 123
    assert n.call(0x66367c, m, unit, 10) == 1

    def trait_tree():
        # std::mapの確保だけを代替する。能力・素の属性・一致判定は原本を実行する。
        result, pairs, nodes = register(0), register(1), m + 0x6500
        put(result, 'QQQ', nodes, nodes, 12)
        for index in range(12):
            mask, enabled = struct.unpack('<IB3x', n.cpu.mem_read(pairs + index * 8, 8))
            put(nodes + index * 48, 'QQQ4xIB', 0, nodes + (index + 1) * 48 if index < 11 else 0,
                nodes + (index - 1) * 48 if index else result + 8, mask, enabled)
        return 0

    selected_form, added_targets, skill, skill_level = 2, 0, 0, 0
    n.helpers.update({0x63eaf8: lambda: selected_form, 0x5c2710: 1, 0x65f698: trait_tree, 0x66ba4c: 0,
                      0xaa4fb0: lambda: int(bool(register(3) & added_targets)),
                      0xaa2c2c: lambda: int(register(3) == skill and skill_level > 0),
                      0xa9f0e0: lambda: skill_level if register(3) == skill else 0})
    put(game + 0x1590, 'QQ', attributes, attributes + len(masks) * 4)
    put(game + 0x3b1d70 + unit * 4, 'i', 2)
    form2 = game + (unit + 2) * 0x770 + 2 * 0x1dc + 0x9ee88
    candidate = m + 0x6800

    def acceptance(effect, attribute):
        put(candidate + 8, 'ii', attribute, effect)
        return n.call(0x65f258, candidate, unit)

    eligibility_checks = 0
    for effect, column, skill in [(2, 23, 5), (3, 30, 7), (4, 29, 6)]:
        for attribute, target in enumerate([10,16,17,18,20,21,22,78,19,54,76,96]):
            n.cpu.mem_write(form2, bytes(0x1dc))
            put(form2 + column * 4, 'i', 1)
            put(form2 + target * 4, 'i', 1)
            assert acceptance(effect, attribute) == 3 and acceptance(effect, (attribute + 1) % 12) == 1
            eligibility_checks += 2
        n.cpu.mem_write(form2, bytes(0x1dc));added_targets = 1
        assert acceptance(effect, 0) == 1
        skill_level = 1
        assert acceptance(effect, 0) == 3
        selected_form = 3
        assert acceptance(effect, 0) == 3
        skill_level, added_targets = 0, 0
        put(form2 + column * 4, 'i', 1);put(form2 + 10 * 4, 'i', 1)
        assert acceptance(effect, 0) == 2
        selected_form = 2;eligibility_checks += 4
    for effect, column in [(17,91),(19,118)]:
        assert acceptance(effect, 12) == 0
        put(form2 + column * 4, 'i', 1)
        assert acceptance(effect, 12) == 4
        eligibility_checks += 2
    print(f'{len(items)} single, {len(witnesses)} paired/mixed, 2 tie, 8 slot and {eligibility_checks} eligibility checks equal to ARM64')
    if args.publish:
        fixture = {'version': '15.7.2', 'versionCode': 1507021, 'nativeSha256': SHA,
                   'sources': assets.sources, 'list': json.loads(raw), 'attributes': attribute_csv,
                   'cases': witnesses}
        (ROOT / 'native/kbcs-core/tests/equipment-vectors.json').write_text(
            json.dumps(fixture, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8-sig')
    (ROOT / 'research/.local/equipment-1572.json').write_text(json.dumps({
        'nativeSha256': SHA, 'librarySha256': digest(args.library.read_bytes()),
        'sources': assets.sources, 'singles': len(items), 'multi': len(witnesses), 'eligibility': eligibility_checks,
        'result': 'equal',
    }, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
