from bisect import bisect_right
from collections import defaultdict
from itertools import zip_longest


# Ghidra AARCH64 LEのGPR記憶域。raw CALLからは実際の引数数を確定できない。
ABI_SLOTS = tuple((f'register:{0x4000+i*8:x}:8', f'register:{0x4000+i*8:x}:4') for i in range(8))
CALLS = {'CALL', 'CALLIND'}
MAX_EFFECTS = 32


def register(value):
    if value and value.startswith('register:'):
        _, address, width = value.split(':')
        offset = int(address, 16)
        return offset, offset + int(width)
    return None


def write_register(definitions, name, slot, value):
    if name not in definitions:
        a, b = slot
        for old, ((c, d), _) in list(definitions.items()):
            if a < d and c < b:
                del definitions[old]
    definitions[name] = slot, value


def block_lookup(row):
    spans = sorted((int(a, 16), int(b, 16), block) for block, ranges, _ in row['blocks'] for a, b in ranges)
    if not spans and len(row['blocks']) == 1:
        spans = [(int(a, 16), int(b, 16), row['blocks'][0][0]) for a, b in row['ranges']]
    starts = [span[0] for span in spans]

    def find(site):
        position = int(site, 16)
        index = bisect_right(starts, position) - 1
        return spans[index][2] if index >= 0 and position <= spans[index][1] else None
    return find


def collect(row, sequence, intern, abi):
    find_block = block_lookup(row)
    # 定義をブロックと命令で分離する。レジスタの別サイズ書込は重複する古い定義を無効にする。
    definitions, temporaries = {}, {}
    events, predicates = defaultdict(list), {}
    last_block, last_site, local_branch = None, None, False

    def read(value):
        if value is None:
            return (intern(('leaf', None)), None, True)
        space = value.split(':', 1)[0]
        if space == 'tmp':
            item = temporaries.get(value)
        elif space == 'register':
            item = definitions.get(value, (None, None))[1]
        else:
            return (intern(('leaf', value)), None, space in ('ram', 'stack'))
        return item or (intern(('live', value)), None, True)

    def slots(count):
        return tuple(next((definitions[variant][1] for variant in variants if variant in definitions), None)
                     for variants in ABI_SLOTS[:count])

    for site, (opcode, output, inputs) in sequence:
        block = find_block(site)
        if block != last_block or (block is None and last_site != site):
            definitions.clear()
        if last_site != site:
            temporaries.clear()
            if local_branch:
                definitions.clear()
            local_branch = False
        last_block, last_site = block, site
        values = tuple(read(value) for value in inputs)
        if opcode == 'STORE' and len(values) == 3:
            events['store'].append((site, block, values))
        elif opcode == 'CBRANCH' and len(values) >= 2:
            events['branch'].append((site, block, (values[1],)))
            local_branch = inputs[0].startswith('const:')
            if block is not None and not local_branch:
                predicates[block] = (site, values[1])
        elif opcode == 'BRANCH' and inputs and inputs[0].startswith('const:'):
            local_branch = True
        elif opcode in CALLS and values:
            events['call'].append((site, block, (values[0], *(values[1:] or (slots(8) if abi else ())))))
            definitions.clear()
            temporaries.clear()
        elif opcode == 'RETURN' and (len(values) > 1 or abi):
            events['return'].append((site, block, values[1:] or slots(1)))
        if not output:
            continue
        slot = register(output)
        if slot is None and not output.startswith('tmp:'):
            continue
        if opcode == 'COPY' and len(values) == 1 and inputs[0] and output.rsplit(':', 1)[1] == inputs[0].rsplit(':', 1)[1]:
            number, _, unknown = values[0]
        else:
            number = intern((opcode, output.rsplit(':', 1)[1], tuple(item[0] for item in values)))
            # LOADとCALLOTHERの値はメモリ状態・ユーザー定義演算に依存する。
            unknown = opcode in ('LOAD', 'CALLOTHER', 'INDIRECT', 'MULTIEQUAL') or any(item[2] for item in values)
        item = number, site, unknown or local_branch
        if slot is None:
            temporaries[output] = item
        else:
            write_register(definitions, output, slot, item)

    # 合流・循環を越えず、唯一の前任経路が条件分岐へ戻る場合だけ書込のガードを記録する。
    incoming, outgoing = defaultdict(set), defaultdict(set)
    blocks = {block[0] for block in row['blocks']}
    for block, _, edges in row['blocks']:
        for kind, _, target in edges:
            outgoing[block].add((kind, target))
            if target in blocks:
                incoming[target].add((kind, block))
    entry = row['address']
    for site, block, _ in events['store']:
        seen = set()
        while block is not None and block != entry and block not in seen and len(incoming[block]) == 1:
            seen.add(block)
            kind, parent = next(iter(incoming[block]))
            if parent in predicates and len({target for _, target in outgoing[parent]}) == 2:
                condition_site, value = predicates[parent]
                events['guard'].append((site, kind, (value,), condition_site))
                break
            block = parent
        else:
            events['guard'].append((site, None, (None,), None))
    return events


def changes(old, new, left, right, abi, *, include_evidence=True):
    nodes, numbers = [], {}

    def intern(key):
        if key not in numbers:
            numbers[key] = len(nodes)
            nodes.append(key)
        return numbers[key]

    def describe(number, depth=2):
        node = nodes[number]
        if node[0] in ('leaf', 'live'):
            return list(node)
        return [node[0], node[1], [describe(child, depth-1) for child in node[2][:5]]] if depth else node[0]

    def fact(item, event):
        return {'site': event[0], 'definition_site': item[1], 'value': describe(item[0]),
                'incomplete_value': item[2]} if item else None

    a, b = collect(old, left, intern, abi), collect(new, right, intern, abi)
    records, counts = [], defaultdict(int)
    fields = {'store': ('store_space', 'store_destination', 'store_value'),
              'branch': ('branch_value',), 'call': ('call_target',), 'return': (), 'guard': ('store_condition',)}
    for sink, labels in fields.items():
        for index, (first, second) in enumerate(zip_longest(a[sink], b[sink])):
            if first is None or second is None:
                kind = sink + '_count'
                counts[kind] += int(sink != 'guard')
                continue
            for slot, (before, after) in enumerate(zip_longest(first[2], second[2])):
                guard = sink == 'guard'
                if (before and before[0], first[1] if guard else None) == (after and after[0], second[1] if guard else None):
                    continue
                kind = labels[slot] if slot < len(labels) else ('call_argument_candidate' if sink == 'call' else 'return_value_candidate')
                counts[kind] += 1
                if include_evidence and len(records) < MAX_EFFECTS:
                    evidence = {'kind': kind, 'ordinal': index, 'slot': slot,
                                'old': fact(before, first), 'new': fact(after, second),
                                'confidence': 'limited' if not before or not after or before[2] or after[2] or
                                kind in ('call_argument_candidate', 'return_value_candidate') else 'bounded'}
                    if guard:
                        evidence['guard'] = [[first[1], first[3]], [second[1], second[3]]]
                    records.append(evidence)
    return dict(counts), records
