"""保存済み15.7.2 ARM64と同版原本で、番台と0番台の読込を照合する。"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import struct
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
SHA = '6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def digest(data):
    return hashlib.sha256(data).hexdigest()


class Assets:
    def __init__(self, root):
        self.root = root.resolve()
        self.current = read_json(self.root / 'metadata/jp/current.json')
        assert self.current['status'] == 'verified' and self.current['versionCode'] == 1507021
        generated = self.root / self.current['generatedPath']
        generated.resolve().relative_to(self.root)
        data = (generated / 'manifest.json').read_bytes()
        assert digest(data) == self.current['manifestSha256']
        manifest = json.loads(data)
        entry = manifest['artifacts']['indexes/assets.json']
        data = (generated / 'indexes/assets.json').read_bytes()
        assert len(data) == entry['size'] and digest(data) == entry['sha256']
        index = json.loads(data)
        for header in [manifest['header'], index['header']]:
            assert all(header[key] == self.current[key] for key in
                       ['schemaVersion', 'datasetId', 'buildId', 'sourceRegion', 'versionCode', 'versionName'])
        self.files = index['files']
        self.sources = {}

    def text(self, name):
        entry = self.files[name]
        path = (self.root / entry['path']).resolve()
        path.relative_to(self.root)
        data = path.read_bytes()
        assert len(data) == entry['size'] and digest(data) == entry['sha256'], name
        self.sources[name] = entry
        return data.decode('utf-8-sig')

    def numeric(self, name, columns=None):
        result = []
        for position, line in enumerate(self.text(name).splitlines(), 1):
            value = line.split('//', 1)[0].strip()
            if not value:
                continue
            cells = next(csv.reader([value]))
            # 末尾の説明と数値CSVを区別し、空欄・欠測列は保持する。
            if not re.fullmatch(r'-?\d+', cells[0].strip()):
                continue
            result.append({'line': position, 'cells': [int(cell) if cell.strip() else None for cell in cells[:columns]]})
        return result


class Native:
    def __init__(self):
        from unicorn import Uc, UC_ARCH_ARM64, UC_MODE_ARM, UC_HOOK_CODE
        from unicorn import arm64_const as registers
        from elftools.elf.elffile import ELFFile
        self.reg = registers
        reference = read_json(ROOT / 'research/.local/reference.json')
        self.cache = Path(reference['cache'])
        identity = read_json(self.cache / 'identity.json')
        with sqlite3.connect((self.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
            self.ends = {int(address, 16): int(address, 16) + size for address, size in
                         db.execute("SELECT address,size FROM functions WHERE address IN ('009e505c','006ef2b0')")}
        assert identity['version'] == '15.7.2' and identity['architecture'] == 'arm64-v8a'
        assert identity['sha256'] == reference['sha256'] == SHA
        binary = Path(identity['binary'])
        assert digest(binary.read_bytes()) == SHA
        with binary.open('rb') as stream:
            elf = ELFFile(stream)
            assert elf['e_machine'] == 'EM_AARCH64'
            segments = [(segment['p_vaddr'] + 0x100000, segment.data(), segment['p_memsz'])
                        for segment in elf.iter_segments() if segment['p_type'] == 'PT_LOAD']
        self.cpu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
        self.cpu.mem_map(0, (max(address + size for address, _, size in segments) + 4095) // 4096 * 4096)
        for address, data, _ in segments:
            self.cpu.mem_write(address, data)
        self.memory, self.stack, self.stop = 0x20000000, 0x30000000, 0x60000000
        for address in [self.memory, self.stack, self.stop]:
            self.cpu.mem_map(address, 0x10000)
        self.cpu.mem_write(self.memory, struct.pack('<Q', self.memory + 0x100))
        self.cpu.mem_write(self.memory + 0x128, struct.pack('<Q', self.stop + 0x100))
        self.row = []
        self.helpers = {}
        self.terminals = set()
        self.entry = 0
        self.cpu.hook_add(UC_HOOK_CODE, self.hook)

    def hook(self, cpu, address, size, data):
        if address == self.stop or address in self.terminals:
            cpu.emu_stop()
        elif self.entry == 0xa06ae4 and address in [self.stop + 0x100, 0x464a64]:
            # CSVのセル取得だけを制御する。14列の転送とF換算は実命令を使う。
            index = cpu.reg_read(self.reg.UC_ARM64_REG_X1)
            value = len(self.row) if address == self.stop + 0x100 else self.row[index]
            cpu.reg_write(self.reg.UC_ARM64_REG_X0, value & 0xffffffff)
            cpu.reg_write(self.reg.UC_ARM64_REG_PC, cpu.reg_read(self.reg.UC_ARM64_REG_LR))
        elif address in self.helpers:
            value = self.helpers[address]
            if callable(value):
                value = value()
            cpu.reg_write(self.reg.UC_ARM64_REG_X0, value & 0xffffffffffffffff)
            cpu.reg_write(self.reg.UC_ARM64_REG_PC, cpu.reg_read(self.reg.UC_ARM64_REG_LR))
        elif self.entry == 0x6ef2b0 and 0xa06c30 <= address < 0xa06ce4:
            return
        elif not (self.entry <= address < self.ends.get(self.entry, self.entry + 0x400)):
            raise RuntimeError(f'Uncontrolled call {address:08x} from {self.entry:08x}')

    def call(self, entry, *args):
        self.entry = entry
        for name in ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']:
            self.cpu.reg_write(getattr(self.reg, 'UC_ARM64_REG_' + name), 0)
        for index, value in enumerate(args):
            self.cpu.reg_write(getattr(self.reg, 'UC_ARM64_REG_X' + str(index)), value & 0xffffffffffffffff)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_SP, self.stack + 0x8000)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_LR, self.stop)
        self.cpu.emu_start(entry, self.stop + 4, count=10000)
        assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC) == self.stop, 'Instruction budget exhausted'
        value = self.cpu.reg_read(self.reg.UC_ARM64_REG_X0) & 0xffffffff
        return value - 0x100000000 if value & 0x80000000 else value

    def spawn(self, cells):
        self.row = [value or 0 for value in cells]
        self.call(0xa06ae4, self.memory + 0x200, self.memory)
        actual = list(struct.unpack('<14i', self.cpu.mem_read(self.memory + 0x200, 56)))
        expected = (self.row + [0] * 14)[:14]
        for index in [2, 3, 4]:
            expected[index] *= 2
        assert actual == expected
        return actual

    def crowns(self, map_id, rates):
        manager, node, values = self.memory + 0x1000, self.memory + 0x2000, self.memory + 0x3000
        self.cpu.mem_write(manager, bytes(0x80))
        self.cpu.mem_write(manager + 0x38, struct.pack('<Q', node))
        self.cpu.mem_write(node, bytes(0x40))
        self.cpu.mem_write(node + 0x20, struct.pack('<i', map_id))
        self.cpu.mem_write(node + 0x28, struct.pack('<Q', values))
        self.cpu.mem_write(values, struct.pack('<4i', *rates))
        actual = [self.call(0x7cebc8, manager, map_id, crown) for crown in range(4)]
        assert actual == rates
        fallback = [self.call(0x7cebc8, manager, 999, crown) for crown in range(4)]
        assert fallback == [100, 150, 200, 250]
        return actual

    def schedule(self, case):
        game, rows, states = 0x40000000, self.memory + 0x5000, self.memory + 0x4000
        self.cpu.mem_write(game, bytes(0xa0000))
        count = len(case['rows'])
        self.cpu.mem_write(rows, b''.join(struct.pack('<14i', *row) for row in case['rows']))
        self.cpu.mem_write(states, b''.join(struct.pack('<3i', *row) for row in case['states']))
        for offset, value in [(0x1120, case.get('kills', 0)), (0x84048, case.get('globalWait', 0)),
                              (0x908a0, 100), (0x9ee5c, case.get('maximum', 50)),
                              (0x9ee50, 3), (0x9ee54, 7)]:
            self.cpu.mem_write(game + offset, struct.pack('<i', value))
        for offset, value in [(0x9ee70, rows), (0x9ee78, rows + count * 56), (0x84050, states)]:
            self.cpu.mem_write(game + offset, struct.pack('<Q', value))
        for index in range(case.get('active', 0)):
            self.cpu.mem_write(game + 0x90c70 + index * 0x3ec, struct.pack('<i', 1))
        self.cpu.mem_write(game + 0x239e6c, struct.pack('<i', int(case.get('damageCondition', False))))
        spawned, random_bounds = [], []
        def spawn():
            spawned.append(self.cpu.reg_read(self.reg.UC_ARM64_REG_X7))
            return case.get('spawnResult', 0)
        def random():
            bound = self.cpu.reg_read(self.reg.UC_ARM64_REG_X0) & 0xffffffff
            assert bound > 0
            random_bounds.append(bound)
            return bound - 1 if case.get('randomMaximum') else 0
        self.helpers = {0x5bc058: int(case.get('paused', False)), 0x5c2710: 0,
                        0x5bbbc8: int(case.get('castlePresent', case.get('damageCondition', False))), 0x5bbbf0: 0, 0x5bbc10: 1,
                        0xa951e0: case.get('castleDamage', 0),
                        0xa958b0: case.get('castleHp', 100), 0x9f1e64: spawn, 0x44a8d8: random}
        self.call(0x6ef2b0, game)
        return {'states': [list(struct.unpack('<3i', self.cpu.mem_read(states + index * 12, 12))) for index in range(count)],
                'globalWait': struct.unpack('<i', self.cpu.mem_read(game + 0x84048, 4))[0],
                'killsCleared': struct.unpack('<i', self.cpu.mem_read(game + 0x1120, 4))[0],
                'spawnedRows': spawned, 'randomBounds': random_bounds}

    def restriction(self, rarity):
        game, manager, node = 0x40000000, self.memory + 0x7000, self.memory + 0x8000
        self.cpu.mem_write(game + 0x32ff0c, struct.pack('<i', 3))
        self.cpu.mem_write(game + 0x39781c, struct.pack('<i', 0))
        self.cpu.mem_write(game + 0xc400, struct.pack('<i', 2))
        self.cpu.mem_write(game + 0xc428, bytes(4))
        self.cpu.mem_write(manager, bytes(0x60)); self.cpu.mem_write(node, bytes(0x60))
        self.cpu.mem_write(manager + 8, struct.pack('<Q', node))
        self.cpu.mem_write(node + 0x24, struct.pack('<i', 6))
        self.helpers = {0x81f580:game, 0x9e4ef8:0, 0x63eaf8:0, 0x63e4a8:rarity,
                        0x5c2710:0, 0x644304:0}
        return self.call(0x9e505c, manager, 0, 1)

    def reward_comparison(self, chances, rolls, radar=False):
        # 取得済み状態の分岐へ入る前の、順次比較ループだけを実行する。
        stage, state, mode, stack = self.memory + 0x9000, self.memory + 0xa000, self.memory + 0xb000, self.stack + 0x8000
        self.cpu.mem_write(stage, bytes(0xc0)); self.cpu.mem_write(state, bytes(0x800))
        mask = 0x01020304
        self.cpu.mem_write(stage + 0xb8, struct.pack('<I', mask))
        for offset, chance in zip([0x14, 0x24, 0x30], chances):
            self.cpu.mem_write(stage + offset, struct.pack('<I', chance ^ mask))
        self.cpu.mem_write(mode, struct.pack('<i', 3))
        for offset, pointer in [(0xf0,state), (0xd8,state+0x3cc), (0xd0,mode), (0x50,stage+0x16)]:
            self.cpu.mem_write(stack + offset, struct.pack('<Q', pointer))
        self.cpu.mem_write(stack + 0x60, struct.pack('<i', len(chances)))
        for name, value in [('SP',stack), ('X19',state), ('X21',stage+0x14), ('X23',stage+0x15), ('X25',stage), ('X28',stage+0x17)]:
            self.cpu.reg_write(getattr(self.reg, 'UC_ARM64_REG_' + name), value)
        consumed = []
        def random():
            bound = self.cpu.reg_read(self.reg.UC_ARM64_REG_X0)
            value = rolls[len(consumed)]
            assert bound == 100 and 0 <= value < bound
            consumed.append(value)
            return value
        self.entry = 0x5dbfd4
        self.helpers = {0x44a8d8:random, 0x5c022c:int(radar)}
        self.terminals = {0x5dc128, 0x5dd52c}
        self.cpu.emu_start(self.entry, self.stop, count=10000)
        pc = self.cpu.reg_read(self.reg.UC_ARM64_REG_PC)
        assert pc in self.terminals
        winner = self.cpu.reg_read(self.reg.UC_ARM64_REG_X27) if pc == 0x5dc128 else None
        self.terminals = set()
        return {'winnerBeforeAcquisition':winner, 'rolls':consumed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', type=Path, required=True)
    parser.add_argument('--python-libs', type=Path, required=True)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    sys.path.insert(0, str(args.python_libs.resolve()))
    native, assets = Native(), Assets(args.assets)
    # 読込口のない番台も省略せず、境界を現版の分類関数へ通す。
    bands = []
    for band in range(40):
        start, end = band * 1000, band * 1000 + 999
        kind = native.call(0x7cd2ac, start)
        bands.append({'band': band, 'start': start, 'end': end, 'kind': kind,
                      'endKind': native.call(0x7cd2ac, end)})
    mappings = []
    for kind in range(-26, 5):
        map_id = native.call(0x7cd120, kind, 0)
        if map_id < 0:
            continue
        assert native.call(0x7cd2ac, map_id) == kind
        mappings.append({'kind': kind, 'firstMap': map_id})
    boundaries = [{'id': value, 'kind': native.call(0x7cd2ac, value),
                   'index': native.call(0x7cd560, value)}
                  for value in [-1000, -999, -1, 2999, *range(3000, 3010), 32999, 39000, 39999, 40000]]
    names = {int(row[0]): row[1] for row in csv.reader(io.StringIO(assets.text('res/Map_Name.csv'))) if row}
    stage_names = list(csv.reader(io.StringIO(assets.text('res/StageName_RN_ja.csv'))))
    map_options = assets.numeric('Data/Map_option.csv', 19)
    stage_options = assets.numeric('Data/Stage_option.csv', 9)
    definitions, metadata = {}, {}
    prefixes = {}
    for name in sorted(assets.files):
        match = re.fullmatch(r'Data/stage([A-Z]+)\d+_\d+\.csv', name)
        if match:
            prefixes[match[1]] = prefixes.get(match[1], 0) + 1
        match = re.fullmatch(r'Data/stageRN(\d+)_(\d+)\.csv', name)
        if match:
            definitions[(int(match[1]), int(match[2]))] = name
        match = re.fullmatch(r'Data/MapStageDataN_(\d+)\.csv', name)
        if match:
            metadata[int(match[1])] = name
    maps, stages, row_count = [], [], 0
    for map_id, name in sorted(metadata.items()):
        assert 0 <= map_id < 1000 and native.call(0x7cd120, 0, map_id) == map_id
        rows = assets.numeric(name)
        assert len(rows) >= 2
        entries = rows[2:]
        options = [row for row in map_options if row['cells'][0] == map_id]
        assert len(options) == 1
        crowns = native.crowns(map_id, options[0]['cells'][3:7])
        maps.append({'id': map_id, 'name': names.get(map_id), 'path': name,
                     'header': rows[:2], 'stages': len(entries),
                     'options': options, 'nativeCrowns': crowns,
                     'restrictions': [row for row in stage_options if row['cells'][0] == map_id]})
        for stage_id, rewards in enumerate(entries):
            path = definitions.pop((map_id, stage_id))
            rows = assets.numeric(path)
            assert len(rows[0]['cells']) >= 6 and len(rows[1]['cells']) >= 6
            spawns = []
            for row in rows[2:]:
                loaded = native.spawn(row['cells'])
                row_count += 1
                if not native.call(0xa06c30, native.memory + 0x200):
                    break
                assert native.call(0xa06c48, native.memory + 0x200) == loaded[0] - 2
                assert native.call(0xa06cb8, native.memory + 0x200) == (loaded[11] or loaded[9])
                spawns.append({**row, 'loaded': loaded})
            stages.append({'map': map_id, 'stage': stage_id, 'name': stage_names[map_id][stage_id],
                           'path': path, 'settings': rows[0], 'header': rows[1], 'rewards': rewards, 'spawns': spawns})
    assert not definitions, f'Unpaired definitions: {definitions}'
    special = [row for row in stages if row['map'] == 17 and row['stage'] == 5][0]
    assert special['header']['cells'][:6] == [5800, 500000, 1, 1, 10, 8]
    assert special['rewards']['cells'][:8] == [160, 3040, 31, 90, 4, 30, 1113, 1]
    # 合成条件で、負の待機・空欄・追加列・攻撃倍率の非0選択も確認する。
    for cells in [[2, 0, -7, 3, 9], [2, 1, 0, 1, 1, 100, 0, 9, 2, 0, 0, -17, 1, 3, 999]]:
        native.spawn(cells)
        assert native.call(0xa06cb8, native.memory + 0x200) == (cells[11] if len(cells) > 11 else 0)
    native.cpu.mem_map(0x40000000, 0x400000)
    row = [2, 0, 0, 10, 20, 100, 0, 9, 0, 100, 0, 0, 0, 0]
    gated = row.copy(); gated[5] = 90
    after_castle = gated.copy(); after_castle[12] = 1
    high_castle = row.copy(); high_castle[5] = 300
    finite = row.copy(); finite[1] = 1
    kills = row.copy(); kills[13] = 3
    cases = [
        {'name': 'reverse-order', 'rows': [row, row], 'states': [[0, 0, 0], [0, 0, 0]], 'expectedRows': [1]},
        {'name': 'global-wait', 'rows': [row], 'states': [[2, 0, 0]], 'globalWait': 2, 'expectedRows': []},
        {'name': 'enemy-cap', 'rows': [row], 'states': [[0, 0, 0]], 'maximum': 1, 'active': 1, 'expectedRows': []},
        {'name': 'castle-not-ready', 'rows': [gated], 'states': [[0, 0, 0]], 'castleHp': 100, 'expectedRows': []},
        {'name': 'castle-equal', 'rows': [gated], 'states': [[0, 0, 0]], 'castleHp': 90, 'expectedRows': [0]},
        {'name': 'castle-300', 'rows': [high_castle], 'states': [[0, 0, 0]], 'expectedRows': [0]},
        {'name': 'after-castle-hold', 'rows': [after_castle], 'states': [[7, 0, 0]], 'expectedRows': []},
        {'name': 'finite-exhausted', 'rows': [finite], 'states': [[10, 1, 0]], 'expectedRows': []},
        {'name': 'kill-gate', 'rows': [kills], 'states': [[0, 0, 0]], 'kills': 2, 'expectedRows': []},
        {'name': 'kill-equal', 'rows': [kills], 'states': [[0, 0, 0]], 'kills': 3, 'expectedRows': [0]},
        {'name': 'spawn-failure', 'rows': [row], 'states': [[0, 0, 0]], 'spawnResult': -1, 'expectedRows': [0]},
        {'name': 'inclusive-random-max', 'rows': [row], 'states': [[0, 0, 0]], 'randomMaximum': True, 'expectedRows': [0]},
        {'name': 'castle-damage-below', 'rows': [gated], 'states': [[0, 0, 0]], 'damageCondition': True, 'castleDamage': 89, 'castleHp': 1, 'expectedRows': []},
        {'name': 'castle-damage-equal', 'rows': [gated], 'states': [[0, 0, 0]], 'damageCondition': True, 'castleDamage': 90, 'expectedRows': [0]},
        {'name': 'paused-kills-consumed', 'rows': [row], 'states': [[2, 0, 0]], 'globalWait': 2, 'paused': True, 'kills': 3, 'expectedRows': []},
        {'name': 'castle-present-without-damage-flag', 'rows': [gated], 'states': [[0, 0, 0]], 'castlePresent':True, 'castleDamage':999, 'expectedRows': []},
    ]
    expected_states = [[[-1, 0, 0], [10, 1, 0]], [[1, 0, 0]], [[-1, 0, 0]], [[1, 0, 0]],
                       [[10, 1, 0]], [[10, 1, 0]], [[7, 0, 0]], [[10, 1, 0]], [[1, 0, 2]],
                       [[10, 1, 3]], [[-1, 0, 0]], [[20, 1, 0]], [[1, 0, 0]], [[10, 1, 0]], [[2, 0, 0]], [[1, 0, 0]]]
    expected_waits = [3, 1, -1, -1, 3, 3, -1, -1, -1, 3, -1, 7, -1, 3, 2, -1]
    scheduler = []
    for case, states, wait in zip(cases, expected_states, expected_waits, strict=True):
        actual = native.schedule(case)
        assert actual['spawnedRows'] == case['expectedRows'], (case['name'], actual)
        assert actual['states'] == states and actual['globalWait'] == wait, (case['name'], actual)
        assert actual['killsCleared'] == 0
        assert actual['randomBounds'] == ([5, 11] if case['expectedRows'] and case.get('spawnResult', 0) >= 0 else [])
        scheduler.append({'input': case, 'result': actual})
    restrictions = []
    for rarity in range(6):
        actual = native.restriction(rarity)
        assert actual == int(rarity in [1, 2]), (rarity, actual)
        restrictions.append({'mask':6, 'rarity':rarity, 'allowed':bool(actual)})
    enemy_rows = assets.numeric('Data/t_unit.csv')
    castle_rows = [{'map':stage['map'], 'stage':stage['stage'], 'rawEnemy':stage['header']['cells'][6],
                    'rawFlag49':enemy_rows[stage['header']['cells'][6]]['cells'][49]}
                   for stage in stages if stage['header']['cells'][6] > 1]
    assert len(castle_rows) == 4 and all(row['rawEnemy'] == 317 and row['rawFlag49'] == 0 for row in castle_rows)
    bosses = []
    native.helpers = {0x81f580:0x40000000, 0x5c2710:0}
    for flag in range(3):
        native.call(0xa95094, 1, 1, flag)
        raw, active = native.call(0xa9502c, 1, 1), native.call(0xa94bf0, 1, 1)
        assert raw == flag and active == int(flag != 0)
        bosses.append({'raw':raw, 'active':bool(active)})
    reward_cases = [([30],[29],False,0), ([30],[30],False,None),
                    ([30,85,9],[30,84],False,1), ([30,85,9],[30,85,8],False,2),
                    ([30,85,9],[30,85,9],False,None), ([0],[0],False,None),
                    ([100],[99],False,0), ([30,85,9],[99],True,0)]
    rewards = []
    for chances, rolls, radar, expected in reward_cases:
        actual = native.reward_comparison(chances, rolls, radar)
        assert actual['winnerBeforeAcquisition'] == expected
        rewards.append({'chances':chances, 'radar':radar, 'result':actual})
    addresses = ['007cd120', '007cd2ac', '007cd560', '0099fe4c', '009a3a30', '00a06ae4',
                 '00a06c30', '00a06c48', '00a06cb8', '006ef2b0', '007cebc8', '009e505c',
                 '00a95094', '00a9502c', '00a94bf0', '006d6d04', '005d996c', '005bbbf0', '00a951e0']
    report = {'version': '15.7.2', 'versionCode': 1507021, 'architecture': 'arm64-v8a', 'sha256': SHA,
              'build': assets.current, 'scope': 'ID conversion, spawn-row reader, crown lookup and controlled normal-castle scheduling; not full battle simulation',
              'evidence': {address: digest((native.cache / 'code' / (address + '.c')).read_bytes()) for address in addresses},
              'bands': bands, 'mappings': mappings, 'boundaries': boundaries, 'definitionPrefixes': prefixes,
              'maps': maps, 'stages': stages, 'nativeRows': row_count, 'sources': assets.sources}
    report['scheduler'] = scheduler
    report['restrictions'] = restrictions
    report['bossFlags'] = bosses
    report['castleRows'] = castle_rows
    report['rewardComparisons'] = rewards
    if args.publish:
        fixture = {'version': report['version'], 'architecture': report['architecture'], 'sha256': SHA,
                   'entry': '006ef2b0', 'scope': 'Native ARM64 scheduler; controlled flags, castle values, RNG and spawn helper; not full battle simulation', 'vectors': scheduler}
        (ROOT / 'native/kbcs-core/tests/stage-vectors.json').write_text(json.dumps(fixture, separators=(',', ':')) + '\n', encoding='utf-8')
    destination = ROOT / 'research/.local/stages-1572-band0.json'
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8-sig')
    print(json.dumps({'report': str(destination), 'maps': len(maps), 'stages': len(stages),
                      'nativeRows': row_count, 'sources': len(assets.sources), 'bandBoundaries': len(bands) * 2,
                      'internalKinds': len(mappings), 'schedulerCases': len(scheduler),
                      'restrictionCases':len(restrictions), 'rewardComparisons':len(rewards)}, separators=(',', ':')))


if __name__ == '__main__':
    main()
