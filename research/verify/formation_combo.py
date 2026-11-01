"""15.7.2 ARM64の自動セットを同じ編成・コンボ一覧で局所照合する。"""
import argparse
import ctypes
import json
from pathlib import Path
import random
import sqlite3
import struct
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--python-libs', type=Path, required=True)
parser.add_argument('--library', type=Path, required=True)
parser.add_argument('--publish', action='store_true')
args = parser.parse_args()
sys.path.insert(0, str(args.python_libs))
from stages import Native, ROOT, SHA


class Probe(Native):
    def __init__(self):
        super().__init__()
        entries = ['00893ea0', '0089c2ec', '00419064', '00650740', '0047b5ec', '00895118']
        with sqlite3.connect((self.cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True) as db:
            self.ranges = [(int(a, 16), int(a, 16) + size) for a, size in
                           db.execute('SELECT address,size FROM functions WHERE address IN (' + ','.join('?' for _ in entries) + ')', entries)]
        self.cpu.mem_map(0x40000000, 0x500000)
        self.cpu.mem_map(0x50000000, 0x1000000)
        self.cursor = 0x50000000
        self.helpers.update({0x81f580: 0x40000000, 0xbdaf40: self.allocate, 0xbdaf60: 0,
                             0xbdb0b0: self.copy, 0xbdaff0: self.copy, 0x59be80: self.locked})
        self.locks = set()
        self.helpers.update({0xbdb500:self.find,0xaa9778:0,0x8906a8:0})

    def hook(self, cpu, address, size, data):
        if address not in self.helpers and any(start <= address < end for start, end in self.ranges):
            return
        super().hook(cpu, address, size, data)

    def register(self, index):
        return self.cpu.reg_read(getattr(self.reg, 'UC_ARM64_REG_X' + str(index)))

    def allocate(self):
        length = self.register(0)
        pointer = self.cursor
        self.cursor += (length + 15) & -16
        assert self.cursor < 0x51000000
        self.cpu.mem_write(pointer, bytes(length))
        return pointer

    def copy(self):
        dest, source, length = [self.register(i) for i in range(3)]
        if length:
            self.cpu.mem_write(dest, bytes(self.cpu.mem_read(source, length)))
        return dest

    def find(self):
        pointer,value,count=[self.register(i) for i in range(3)]
        values=struct.unpack('<'+'I'*count,self.cpu.mem_read(pointer,count*4))
        return pointer+values.index(value&0xffffffff)*4 if value&0xffffffff in values else 0

    def locked(self):
        value = ctypes.c_int32(self.register(2)).value
        return int(value in self.locks)

    def plan(self, definitions, team, forms, selected):
        self.cursor = 0x50000000
        context, pointers, records, output = 0x20001000, 0x20002000, 0x20004000, 0x2000e000
        self.cpu.mem_write(context, bytes(0x500))
        self.cpu.mem_write(output, bytes(24))
        ptrs = b''.join(struct.pack('<QQ', records + i * 0x80, 0) for i in range(len(definitions)))
        self.cpu.mem_write(pointers, ptrs)
        self.cpu.mem_write(context, struct.pack('<6Q', pointers, pointers + len(ptrs), pointers + len(ptrs), pointers, pointers + len(ptrs), pointers + len(ptrs)))
        for i, combo in enumerate(definitions):
            record = bytearray(0x80)
            struct.pack_into('<5i', record, 0x3c, *combo['units'])
            struct.pack_into('<5i', record, 0x50, *combo['forms'])
            record[0x65] = int(all(unit < 0 or any(team[j] == unit and forms[j] >= combo['forms'][k] for j in range(5)) for k, unit in enumerate(combo['units'])))
            self.cpu.mem_write(records + i * 0x80, bytes(record))
        self.cpu.mem_write(0x4000c400, struct.pack('<10i', *(unit + 2 if unit >= 0 else -1 for unit in team)))
        self.cpu.mem_write(0x4000c428, bytes(4))
        self.cpu.mem_write(0x4039781c, bytes(4))
        self.entry = 0x893ea0
        for i, value in enumerate([context, selected, 0, 0, 0, 0, 0, 0, output]):
            self.cpu.reg_write(getattr(self.reg, 'UC_ARM64_REG_X' + str(i)), value)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_SP, self.stack + 0x8000)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_LR, self.stop)
        self.cpu.emu_start(self.entry, self.stop + 4, count=500000)
        assert self.register(30) == self.stop or self.cpu.reg_read(self.reg.UC_ARM64_REG_PC) == self.stop
        begin, end, _ = struct.unpack('<3Q', self.cpu.mem_read(output, 24))
        values = list(struct.unpack('<' + 'i' * ((end - begin) // 4), self.cpu.mem_read(begin, end - begin))) if end > begin else []
        first=[value if value >= 0 else -1 for value in values]
        for unit,form in zip(team,forms):
            if unit>=0:self.cpu.mem_write(0x40049734+unit*4,struct.pack('<i',form))
        self.entry=0x895118
        for i,value in enumerate([context,selected]):self.cpu.reg_write(getattr(self.reg,'UC_ARM64_REG_X'+str(i)),value)
        self.cpu.reg_write(self.reg.UC_ARM64_REG_SP,self.stack+0x8000);self.cpu.reg_write(self.reg.UC_ARM64_REG_LR,self.stop)
        self.cpu.emu_start(self.entry,self.stop+4,count=500000)
        assert self.cpu.reg_read(self.reg.UC_ARM64_REG_PC)==self.stop
        slots=[max(-1,value-2) for value in struct.unpack('<10i',self.cpu.mem_read(0x4000c400,40))]
        return first,slots


class Definition(ctypes.Structure):
    _fields_ = [('units', ctypes.c_int32 * 5), ('forms', ctypes.c_int32 * 5)]


class Selection(ctypes.Structure):
    _fields_ = [('team', ctypes.c_int32 * 10), ('forms', ctypes.c_int32 * 10), ('locked', ctypes.c_int32 * 10), ('selected', ctypes.c_int32)]


class Plan(ctypes.Structure):
    _fields_ = [('first', ctypes.c_int32 * 5), ('slots', ctypes.c_int32 * 10)]


native = Probe()
library = ctypes.CDLL(str(args.library.resolve()))
library.kbcs_core_combo_plan.argtypes = [ctypes.POINTER(Definition), ctypes.c_int32, ctypes.POINTER(Selection), ctypes.POINTER(Plan)]
randomizer = random.Random(20261101)
cases = []
for index in range(120):
    team = randomizer.sample(range(15), randomizer.randrange(0, 11))
    team += [-1] * (10 - len(team))
    forms = [randomizer.randrange(4) for _ in team]
    combos = []
    for _ in range(randomizer.randrange(1, 16)):
        members = randomizer.sample(range(15), randomizer.randrange(1, 6))
        combos.append({'units': members + [-1] * (5 - len(members)), 'forms': [randomizer.randrange(4) for _ in range(5)]})
    # 既存の複合コンボを含む条件を意図的に増やす。
    if index % 2 == 0 and team[0] >= 0:
        members = [unit for unit in team[:5] if unit >= 0]
        combos.append({'units': members + [-1] * (5 - len(members)), 'forms': [0] * 5})
    selected = randomizer.randrange(len(combos))
    expected,slots = native.plan(combos, team, forms, selected)
    definitions = (Definition * len(combos))(*(Definition((ctypes.c_int32 * 5)(*v['units']), (ctypes.c_int32 * 5)(*v['forms'])) for v in combos))
    selection = Selection((ctypes.c_int32 * 10)(*team), (ctypes.c_int32 * 10)(*forms), (ctypes.c_int32 * 10)(*([0] * 10)), selected)
    result = Plan()
    code = library.kbcs_core_combo_plan(definitions, len(combos), ctypes.byref(selection), ctypes.byref(result))
    assert code == 0 and list(result.first) == expected + [-1] * (5 - len(expected)), (index, combos, team, forms, selected, expected, code, list(result.first))
    assert list(result.slots)==slots,(index,team,expected,slots,list(result.slots))
    cases.append({'combos': combos, 'selection': {'team': team, 'forms': forms, 'locked': [0] * 10, 'selected': selected}, 'first': list(result.first), 'slots': list(result.slots)})
print(json.dumps({'native': SHA, 'cases': len(cases), 'result': '一致'}, ensure_ascii=True))
if args.publish:
    (ROOT / 'native/kbcs-core/tests/formation-combo-vectors.json').write_text(json.dumps({'nativeSha256': SHA, 'cases': cases[:12]}, ensure_ascii=False, indent=2), encoding='utf-8-sig')
