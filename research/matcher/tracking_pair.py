import json
import time
from collections import Counter, defaultdict
from functools import lru_cache

from matcher import logic
from matcher.report import peak_memory
from matcher.structure import load_metadata, load_row, operations, pack, reader


def ordered(addresses):
    return sorted((a for a in addresses if not a.startswith('EXTERNAL:')), key=lambda a: int(a, 16))


def catalogs(db):
    shapes, outgoing, incoming = {}, defaultdict(set), defaultdict(set)
    for address, state, shape, count, machine, graph, raw in db.execute(
            "SELECT address,state,shape,operations,bytes_sha256,cfg,json_extract(metadata,'$.refs') FROM functions ORDER BY address"):
        shapes[address] = (state, shape, count, machine, graph)
        for _, _, kind, _, callee, _, _ in json.loads(raw):
            if callee and callee != address and ('CALL' in kind or 'JUMP' in kind):
                outgoing[address].add(callee)
                incoming[callee].add(address)
    return shapes, outgoing, incoming


def refine(accepted, structure, graphs, get, rejected, max_rounds=5):
    anchors = {a: b for a, (b, _, _) in accepted.items()}
    initial = set(anchors)
    left, right = structure
    taken = set(anchors.values())
    groups = []
    for source in structure:
        by_shape = defaultdict(list)
        for address, (state, shape, count, _, _) in source.items():
            if state == 'available' and count >= 24:
                by_shape[shape].append(address)
        groups.append(by_shape)
    hits, proposals, candidates, collisions = {}, {}, {}, Counter()
    old_out, old_in, new_out, new_in = graphs
    for key, old in groups[0].items():
        new = groups[1].get(key, ())
        if not new:
            continue
        if len(old) != 1 or len(new) != 1:
            free_left = [a for a in old if a not in initial]
            free_right = [b for b in new if b not in taken]
            collisions['old'] += len(free_left) if free_right else 0
            collisions['new'] += len(free_right) if free_left else 0
            for a in free_left:
                for b in free_right[:8]:
                    if (a, b) not in rejected:
                        proposals[a, b] = ('shape_collision', {'shape': key, 'group_sizes': [len(old), len(new)]})
            continue
        a, b = old[0], new[0]
        if a in accepted or b in taken or (a, b) in rejected:
            continue
        candidates[a] = (b, key)
    reverse = {b: a for a, (b, _) in candidates.items()}
    pending, rounds = set(candidates), []
    for number in range(1, max_rounds + 1):
        if not pending:
            break
        current = {}
        new_targets = {value: value for value in anchors.values()}
        for a in sorted(pending):
            b, shape = candidates[a]
            support = {}
            for kind, before, after in (('callee', old_out[a], new_out[b]), ('caller', old_in[a], new_in[b])):
                for other in before:
                    if other in anchors and anchors[other] in after:
                        support.setdefault(other, []).append(kind)
            strict = False
            if len(support) >= 2 and initial.intersection(support):
                a_ops = [op for _, op in operations(get(0, a), anchors)]
                b_ops = [op for _, op in operations(get(1, b), new_targets)]
                strict = a_ops == b_ops and left[a][4] == right[b][4]
            evidence = {'unique_cfg_pcode_shape': shape, 'round': number,
                        'anchors': [{'old': other, 'new': anchors[other], 'relation': support[other],
                                     'origin': 'initial_matcher' if other in initial else 'strict_structure'}
                                    for other in sorted(support)],
                        'sources': ['ghidra_cfg', 'strict_raw_pcode', 'recorded_call_edges'],
                        'strict_pcode_and_cfg_equal': strict}
            if strict:
                current[a] = (b, 'unique_structure_with_call_anchors', evidence)
                proposals.pop((a, b), None)
            else:
                proposals[a, b] = ('structural_candidate', evidence)
        rounds.append({'round': number, 'candidates': len(pending), 'accepted': len(current),
                       'held': len(pending) - len(current), 'collisions': dict(collisions) if number == 1 else {}})
        if not current:
            break
        hits.update(current)
        anchors.update((a, item[0]) for a, item in current.items())
        # 次のラウンドは、新しい基準と呼出で接続する未対応候補だけを見直す。
        pending = set()
        for a, (b, _, _) in current.items():
            pending.update(old_out[a] | old_in[a])
            pending.update(reverse[target] for target in new_out[b] | new_in[b] if target in reverse)
        pending = (pending & candidates.keys()) - hits.keys()
    return hits, [(a, b, kind, 'review', evidence) for (a, b), (kind, evidence) in proposals.items()], {
        'rounds': rounds, 'shape_collisions': dict(collisions)}


def intervals(functions, accepted):
    left, right = (ordered(items) for items in functions)
    positions = ({a: i for i, a in enumerate(left)}, {b: i for i, b in enumerate(right)})
    anchors = [(a, accepted[a][0]) for a in left if a in accepted and accepted[a][0] in positions[1]]
    rank = {b: i for i, b in enumerate(ordered(b for _, b in anchors))}
    layouts, neighborhoods = [], ({}, {})
    for (a, b), (c, d) in zip(anchors, anchors[1:]):
        i, j = positions[0][a], positions[0][c]
        k, l = positions[1][b], positions[1][d]
        left_gap, right_gap = left[i + 1:j], right[k + 1:l]
        crossing = rank[d] - rank[b] != 1
        state = 'reordered' if crossing else 'different_count' if len(left_gap) != len(right_gap) else 'equal_count'
        if crossing or left_gap or right_gap:
            layouts.append((a, c, b, d, state, len(left_gap), len(right_gap)))
        if crossing and len(left_gap) <= 20:
            pool = sorted(set(right[max(0, k-4):k+5] + right[max(0, l-4):l+5]))
            for address in left_gap:
                neighborhoods[0][address] = (pool, ())
        elif max(len(left_gap), len(right_gap)) <= 20:
            for address in left_gap:
                neighborhoods[0][address] = (right_gap, (a, c, b, d))
            for address in right_gap:
                neighborhoods[1][address] = (left_gap, (b, d, a, c))
    moved = {edge for a, c, b, d, state, _, _ in layouts if state == 'reordered' for edge in ((a, b), (c, d))}
    return layouts, neighborhoods, moved


def residuals(side, address, alternatives, neighbors, map_to_other, taken, callers, pieces, *, strong=(), callees=None):
    chunk, bounds = neighbors.get(address, ((), ()))
    pool = sorted((set(chunk) | alternatives.get(address, set())) - taken)[:24]
    own = pieces(side, address)
    output = []
    if len(own) >= 12:
        overlaps = []
        for target in pool:
            other = pieces(1 - side, target)
            shared = own & other
            if len(shared) >= 6 and len(shared) >= 0.55 * len(other):
                overlaps.append((target, shared))
        for i, (first, one) in enumerate(overlaps):
            for second, two in overlaps[i + 1:]:
                if len(one - two) >= 5 and len(two - one) >= 5 and len(one | two) >= 0.65 * len(own):
                    output.append(('split_candidate' if side == 0 else 'merge_candidate', [first, second],
                                   {'shared_fragments': len(one | two), 'source_fragments': len(own), 'bounds': bounds}))
        mapped_context = set(callers[address]) | set((callees or {}).get(address, ())) | set(bounds[:2])
        for neighbor in sorted(mapped_context)[:16]:
            target = map_to_other.get(neighbor)
            if target:
                shared = own & (pieces(1 - side, target) - pieces(side, neighbor))
                if len(shared) >= max(8, 0.6 * len(own)):
                    relation = 'caller' if neighbor in callers[address] else 'callee_or_interval'
                    kind = (('inline_candidate' if side == 0 else 'outline_candidate') if relation == 'caller'
                            else 'embedded_fragment_candidate')
                    output.append((kind, [target], {'source_neighbor': neighbor, 'relation': relation,
                                                    'shared_fragments': len(shared), 'source_fragments': len(own)}))
    hypotheses = output[:12]
    if alternatives.get(address):
        hypotheses.append(('competing_candidates', sorted(alternatives[address])[:16], {'bounds': bounds}))
    if bounds and own and not strong:
        hypotheses.append(('deletion_candidate' if side == 0 else 'addition_candidate', [],
                           {'bounds': bounds, 'other_functions_in_interval': len(chunk),
                            'competing_weak_candidates': len(alternatives.get(address, ())),
                            'evidence': 'bounded_interval_without_strong_correspondence'}))
    return hypotheses or [('unresolved', [], {'reason': 'insufficient_structural_or_interval_evidence'})]


def audit(initial, old_db, new_db, target, pair, emit=print, force_detail=()):
    started, metrics = time.monotonic(), {}

    def stage(name):
        nonlocal started
        end = time.monotonic()
        metrics[name] = {'seconds': end - started, 'process_peak_rss_bytes': peak_memory()}
        started = end

    with reader(initial) as source:
        metadata = {key: json.loads(value) for key, value in source.execute('SELECT key,value FROM metadata')}
        if metadata['quality_gate'] != 'passed_named_holdout':
            raise ValueError('PASS 1 did not pass the named holdout')
        accepted = {a: (b, reason, json.loads(evidence) | {'pseudocode_state': change})
                    for a, b, reason, change, evidence in source.execute('SELECT old,new,reason,change,evidence FROM matches')}
        rejected = {(item['old'], item['new']) for item in metadata['decisions'] if item['action'] == 'reject'}
        functions = tuple(dict(source.execute('SELECT address,review_reason FROM functions WHERE side=?', (side,)))
                          for side in ('old', 'new'))
        candidates = source.execute('SELECT old,new,rank,score,eligible,evidence FROM candidates ORDER BY old,rank').fetchall()
        target.executemany('INSERT INTO candidates VALUES(?,?,?,?,?,?,?)', ((pair, *row) for row in candidates))
    initial_count = len(accepted)
    emit(f'{pair} PASS 1: {initial_count} relations; ledger {len(functions[0])}/{len(functions[1])}')
    stage('pass1_load')
    with reader(old_db) as first, reader(new_db) as second:
        sources = (first, second)
        abi = all(json.loads(db.execute("SELECT value FROM meta WHERE key='program'").fetchone()[0])[
            'language'].startswith('AARCH64:LE:64:') for db in sources)
        (old, old_out, old_in), (new, new_out, new_in) = map(catalogs, sources)

        @lru_cache(maxsize=48)
        def get(side, address):
            return load_row(sources[side], address)

        @lru_cache(maxsize=128)
        def pieces(side, address):
            row = get(side, address)
            return logic.fragments(row) if row else set()

        # 未対応だけでなく、変更疑いと未対応の一段の呼出近傍を詳細調査する。
        hits, proposed, refinement = refine(accepted, (old, new), (old_out, old_in, new_out, new_in), get, rejected)
        accepted.update(hits)
        maps = ({a: row[0] for a, row in accepted.items()}, {row[0]: a for a, row in accepted.items()})
        new_targets = {b: b for b in maps[1]}
        alternatives = (defaultdict(set), defaultdict(set))
        strong = (defaultdict(set), defaultdict(set))
        for a, b, *_ in [*candidates, *proposed]:
            if (a, b) not in rejected:
                alternatives[0][a].add(b)
                alternatives[1][b].add(a)
        for a, b, _, _, eligible, _ in candidates:
            if eligible and (a, b) not in rejected and a not in maps[0] and b not in maps[1]:
                strong[0][a].add(b)
                strong[1][b].add(a)
        layouts, nearby, moved = intervals(functions, accepted)
        target.executemany('INSERT INTO layout VALUES(?,?,?,?,?,?,?,?)', ((pair, *row) for row in layouts))
        target.executemany('INSERT INTO relations VALUES(?,?,?,?,?,?)',
                           ((pair, a, b, kind, verdict, pack(evidence)) for a, b, kind, verdict, evidence in proposed))
        target.executemany('INSERT INTO relations VALUES(?,?,?,?,?,?)',
                           ((pair, a, b, reason, 'accepted', pack(evidence)) for a, (b, reason, evidence) in accepted.items()))
        emit(f'{pair} PASS 2: {len(hits)} added; {len(proposed)} structural candidates')
        stage('pass2_structure')
        detailed = set(force_detail)
        for side, (shapes, outgoing, incoming) in enumerate(((old, old_out, old_in), (new, new_out, new_in))):
            seeds = shapes.keys() - maps[side].keys()
            detailed.update(address if side == 0 else maps[1].get(address)
                            for seed in seeds for address in incoming[seed] | outgoing[seed])
        detailed.update(a for a, (_, _, evidence) in accepted.items()
                        if evidence.get('pseudocode_state') in ('different', 'unavailable'))
        for a in tuple(detailed):
            if a in old:
                detailed.update(old_in[a] | old_out[a])
        counts, importance, inspection, impacts, ref_states = (Counter() for _ in range(5))
        for a, (b, reason, evidence) in accepted.items():
            if a not in old or b not in new or old[a][0] != 'available' or new[b][0] != 'available':
                record = {'status': 'unavailable', 'scope': [old.get(a, ['external_or_missing'])[0],
                                                           new.get(b, ['external_or_missing'])[0]],
                          'importance': 'review', 'confidence': 'limited', 'reference_state': 'not_tested',
                          'equivalence': 'unproven', 'unchecked': ['structure', 'references', 'raw_pcode_operands']}
                inspection['unavailable'] += 1
            else:
                reference_check = None
                if a not in detailed and old[a][1:5] == new[b][1:5]:
                    reference_check = logic.reference_comparison(load_metadata(first, a), load_metadata(second, b),
                                                                maps[0], new_targets)
                if reference_check and reference_check['state'] == 'equal':
                    record = logic.skipped((old[a], new[b]), reference_check)
                    inspection['skipped'] += 1
                else:
                    record = logic.compare(get(0, a), get(1, b), maps[0], new_targets, references=reference_check, abi=abi)
                    inspection['detailed'] += 1
                    if reference_check:
                        inspection['forced_by_references'] += 1
            record['order_changed'] = (a, b) in moved
            if a in old and b in new:
                record['address_delta'] = int(b, 16) - int(a, 16)
            if record.get('cfg_changed'):
                record['structural_candidate'] = ('boundary_candidate'
                    if len(get(0, a)['ranges']) != len(get(1, b)['ranges'])
                    else 'compiler_shape_candidate' if record['status'] in ('register_sensitive', 'structure_or_reference_change')
                    else 'cfg_change')
            counts[record['status']] += 1
            importance[record['importance']] += 1
            ref_states[record['reference_state']] += 1
            impacts.update(record.get('impact', {}).keys())
            target.execute('INSERT INTO logic VALUES(?,?,?,?,?)', (pair, a, b, record['status'], pack(record)))
        emit(f'{pair} PASS 3: {dict(counts)}')
        stage('pass3_logic')
        residual_counts = Counter()
        unresolved = []
        for side, (incoming, outgoing) in enumerate(((old_in, old_out), (new_in, new_out))):
            unresolved.append(len(functions[side].keys() - maps[side].keys()))
            for address in sorted(functions[side].keys() - maps[side].keys()):
                state = (old, new)[side].get(address, ('not_indexed',))[0]
                if state == 'boundary_mismatch':
                    results = [('boundary_candidate', [], {'reason': 'backfill disagrees with original function boundary'})]
                else:
                    results = residuals(side, address, alternatives[side], nearby[side], maps[side],
                                        maps[1 - side].keys(), incoming, pieces,
                                        strong=strong[side].get(address, ()), callees=outgoing)
                for kind, candidates_for_function, proof in results:
                    residual_counts[kind] += 1
                    target.execute('INSERT INTO review VALUES(?,?,?,?,?,?)', (pair, side, address, kind,
                        pack(candidates_for_function), pack(proof | {'initial_reason': functions[side][address]})))
        emit(f'{pair} PASS 4: {dict(residual_counts)}')
        stage('pass4_hypotheses')
    validation = metadata['validation']
    answered = validation['correct'] + validation['wrong']
    held_out = answered + validation['abstained']
    rates = {'correct_among_answered': validation['correct'] / answered if answered else None,
             'abstention_rate': validation['abstained'] / held_out if held_out else None}
    return maps[0], {'initial_accepted': initial_count, 'refined_accepted': len(hits),
                    'logic': dict(counts), 'review': dict(residual_counts), 'validation': metadata['validation'],
                    'importance': dict(importance), 'inspection': dict(inspection), 'impacts': dict(impacts),
                    'reference_states': dict(ref_states), 'refinement': refinement, 'unmatched': unresolved, 'passes': metrics,
                    'named_holdout_rates': rates,
                    'baseline_coverage': metadata['coverage'], 'layout': dict(Counter(row[4] for row in layouts))}
