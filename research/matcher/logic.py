from bisect import bisect_right
from collections import Counter
from difflib import SequenceMatcher
from itertools import groupby, islice

from matcher.structure import cfg, indexed_refs, operations


CALLS = {'CALL', 'CALLIND'}
BRANCHES = {'BRANCH', 'BRANCHIND', 'CBRANCH', 'RETURN'}
COMPARE = {'INT_EQUAL', 'INT_NOTEQUAL', 'INT_LESS', 'INT_LESSEQUAL', 'INT_SLESS', 'INT_SLESSEQUAL',
           'FLOAT_EQUAL', 'FLOAT_NOTEQUAL', 'FLOAT_LESS', 'FLOAT_LESSEQUAL'}
MAX_DETAIL = 24


def args_of(op):
    return (op[1], *op[2])


def refs_signature(row, targets):
    # 実データの同一性が未確認の参照先は、値を残して別途報告する。
    result = []
    for _, target, kind, _, callee, name, datatype in row['refs']:
        if 'CALL' in kind or 'JUMP' in kind:
            if callee and callee != row['address']:
                result.append((kind, targets.get(callee, callee)))
        elif kind in ('READ', 'WRITE', 'READ_WRITE', 'DATA', 'PARAM'):
            result.append((kind, (name, datatype) if name and datatype else target))
    return result


def explain_ops(before, after):
    counts = [Counter(op[0] for op in seq) for seq in (before, after)]
    tags = set()
    if before != after and Counter(before) == Counter(after):
        tags.add('operation_order')
    for label, names in (('control_flow', BRANCHES), ('call', CALLS), ('memory_write', {'STORE'}),
                         ('memory_read', {'LOAD'}), ('comparison', COMPARE)):
        old, new = ([op for op in seq if op[0] in names] for seq in (before, after))
        if old != new:
            tags.add(label)
        if any(counts[0][name] != counts[1][name] for name in names):
            tags.add(label + '_count')
    constants = [Counter(value for op in seq for value in op[2] if value and value.startswith('const:'))
                 for seq in (before, after)]
    if constants[0] != constants[1]:
        tags.add('constant')
    if [op[0] for op in before] != [op[0] for op in after]:
        tags.add('operation_sequence')
    if [args_of(op) for op in before] != [args_of(op) for op in after]:
        tags.add('operands_and_dependencies')
    return tags


def relaxed_registers(ops):
    return [(name, tuple('register:' + value.rsplit(':', 1)[1] if value and value.startswith('register:') else value
                         for value in args_of(op))) for op in ops for name in (op[0],)]


def conditions(sequence):
    result = []
    for _, rows in groupby(sequence, key=lambda item: item[0]):
        operations_at_site = tuple(op for _, op in rows)
        if any(op[0] == 'CBRANCH' for op in operations_at_site):
            result.append(operations_at_site)
    return result


def local_dependencies(row, sequence):
    # 基本ブロック内の同一記憶域だけを追い、別ブロックや別サイズの別名は推測しない。
    spans = sorted((int(a, 16), int(b, 16), block) for block, ranges, _ in row['blocks'] for a, b in ranges)
    starts = [span[0] for span in spans]
    definitions, result = {}, []
    last_block = None
    for index, (site, (_, output, inputs)) in enumerate(sequence):
        position = int(site, 16)
        slot = bisect_right(starts, position) - 1
        block = spans[slot][2] if slot >= 0 and position <= spans[slot][1] else site
        if block != last_block:
            definitions.clear()
            last_block = block

        def key(value):
            return (site, value) if value.startswith('tmp:') else value

        result.append(tuple(index - definitions[key(value)] if key(value) in definitions else None
                            for value in inputs if value and value.startswith(('tmp:', 'register:'))))
        if output and output.startswith(('tmp:', 'register:')):
            definitions[key(output)] = index
    return result


def relocation_shape(row, targets):
    # アドレス生成命令と、Ghidraの参照先と一致した直後のオフセットを区別する。
    # この投影は差分の分類専用。実際のオペランドを置き換えて等価とは判定しない。
    projected = iter(operations(row, targets, search=True))
    refs = indexed_refs(row)
    result = []
    previous = {}
    block_starts = {block[0] for block in row['blocks']}
    for site, mnemonic, flow, raw in row['instructions']:
        state = {} if site in block_starts else previous.copy()
        for opcode, output, inputs in raw:
            _, (name, target, args) = next(projected)
            values = list(args)
            pointer = None
            if mnemonic.lower() in ('adr', 'adrp') and opcode == 'COPY' and inputs[0].startswith('const:'):
                _, offset, width = inputs[0].split(':')
                pointer = int(offset, 16)
                values[0] = f'pc_relative_address:{width}'
            elif (mnemonic.lower() in ('bl', 'blr') and 'CALL' in flow and opcode == 'INT_ADD'
                  and inputs[0] == f'const:{int(site, 16):x}:8' and inputs[1] == 'const:4:8'):
                values[0] = 'call_return_pc:8'
            elif opcode == 'INT_ADD' and len(inputs) == 2 and inputs[0] in state and inputs[1].startswith('const:'):
                _, offset, width = inputs[1].split(':')
                pointer = state[inputs[0]] + int(offset, 16)
                if pointer in refs.get(site, {}):
                    values[1] = f'verified_pc_relative_offset:{width}'
            if output:
                state.pop(output, None)
                if pointer is not None:
                    state[output] = pointer
            result.append((name, target, tuple(values)))
        # 一命令分だけレジスタを引き継ぎ、間接的なデータ推測を広げない。
        previous = {output: state[output] for _, output, _ in raw if output in state and output.startswith('register:')}
    return result


def compare(old, new, old_targets, new_targets):
    old_cfg, new_cfg = cfg(old), cfg(new)
    graph = old_cfg != new_cfg
    left, right = operations(old, old_targets), operations(new, new_targets)
    a, b = [op for _, op in left], [op for _, op in right]
    old_refs, new_refs = refs_signature(old, old_targets), refs_signature(new, new_targets)
    ref_changed = old_refs != new_refs
    machine = old['bytes_sha256'] != new['bytes_sha256']
    warnings = []
    if old['unresolved'] or new['unresolved']:
        warnings.append('unresolved_indirect_flow')
    if old['instruction_bytes'] != old['body_bytes'] or new['instruction_bytes'] != new['body_bytes']:
        warnings.append('incomplete_instruction_coverage')
    result = {'scope': 'raw_instruction_pcode', 'operations': [len(a), len(b)], 'cfg_changed': graph,
              'machine_changed': machine, 'reference_changed': ref_changed, 'warnings': warnings,
              'changes': [], 'details': [], 'detail_truncated': False}
    if graph:
        result['cfg'] = {'blocks': [len(old_cfg), len(new_cfg)], 'ranges': [old['ranges'], new['ranges']],
                         'changed_blocks': [[index, left, right] for index, (left, right) in
                             islice(((index, pair) for index, pair in enumerate(zip(old_cfg, new_cfg)) if pair[0] != pair[1]), 16)]}
    if ref_changed:
        old_counts, new_counts = Counter(old_refs), Counter(new_refs)
        result['references'] = {'removed': list(islice((old_counts-new_counts).elements(), 16)),
                                'added': list(islice((new_counts-old_counts).elements(), 16)),
                                'order_only': old_counts == new_counts}
    if a == b:
        result['status'] = 'structure_or_reference_change' if graph or ref_changed else (
            'machine_only_observed' if machine else 'no_difference_in_scope')
        return result
    tags = explain_ops(a, b)
    if conditions(left) != conditions(right):
        tags.add('branch_condition_or_target')
    if local_dependencies(old, left) != local_dependencies(new, right):
        tags.add('local_def_use')
    known_calls = [[op[2][0] for op in ops if op[0] == 'CALL' and op[2][0].startswith('callee:')]
                   for ops in (a, b)]
    if relaxed_registers(a) == relaxed_registers(b):
        result['status'] = 'register_sensitive'
    elif known_calls[0] == known_calls[1] and not graph and (
            relocation_shape(old, old_targets) == relocation_shape(new, new_targets)):
        result['status'] = 'reference_sensitive'
    else:
        result['status'] = 'logic_change_candidate'
    if max(len(a), len(b)) <= 3500:
        changes = ((i, j, k, l) for op, i, j, k, l in SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
                   if op != 'equal')
    else:
        prefix = next((i for i, pair in enumerate(zip(a, b)) if pair[0] != pair[1]), min(len(a), len(b)))
        changes = iter([(prefix, len(a), prefix, len(b))])
        result['detail_truncated'] = True
    for i, j, k, l in islice(changes, MAX_DETAIL + 1):
        if len(result['details']) == MAX_DETAIL:
            result['detail_truncated'] = True
            break
        local = explain_ops(a[i:j], b[k:l])
        tags.update(local)
        result['details'].append({'old': left[i:min(i + 6, j)], 'new': right[k:min(k + 6, l)],
                                  'counts': [j - i, l - k], 'types': sorted(local)})
        result['detail_truncated'] |= max(j - i, l - k) > 6
    result['changes'] = sorted(tags)
    return result


def fragments(row):
    # 断片検索でのみ割当レジスタと参照先の移動を許容する。
    ops = [op for _, op in operations(row, search=True)]
    tokens = relaxed_registers(ops)
    return {tuple(tokens[i:i + 6]) for i in range(len(tokens) - 5)
            if len({token[0] for token in tokens[i:i + 6]}) >= 4}
