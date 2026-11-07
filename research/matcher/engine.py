import collections
import hashlib

from matcher.relations import context_pairs, data_pairs


def unique_pairs(old, new, key):
    def groups(functions):
        result = collections.defaultdict(list)
        for address, row in functions.items():
            for value in key(row):
                if value:
                    result[value].append(address)
        return result
    left, right = groups(old), groups(new)
    choices, reverse = collections.defaultdict(set), collections.defaultdict(set)
    for value, addresses in left.items():
        if len(addresses) == len(right.get(value, ())) == 1:
            a, b = addresses[0], right[value][0]
            choices[a].add(b)
            reverse[b].add(a)
    return {a: next(iter(bs)) for a, bs in choices.items()
            if len(bs) == 1 and len(reverse[next(iter(bs))]) == 1}


def symbol_pairs(old, new):
    return unique_pairs(old, new, lambda row: row['symbols'])


def holdout_pairs(old, pairs):
    return {a: b for a, b in pairs.items() if not old[a]['external'] and
            hashlib.sha256(old[a]['symbols'][0].encode()).digest()[0] < 86}


def order_candidates(old, new, anchors):
    left = sorted((a for a in old if not old[a]['external']), key=lambda a: int(a, 16))
    right = sorted((a for a in new if not new[a]['external']), key=lambda a: int(a, 16))
    right_addresses = {int(a, 16): a for a in right}
    left_index, right_index = ({a: i for i, a in enumerate(items)} for items in (left, right))
    seeds = sorted((a for a in anchors if a in left_index and anchors[a] in right_index), key=lambda a: int(a, 16))
    right_seed_rank = {b: i for i, b in enumerate(sorted((anchors[a] for a in seeds), key=lambda a: int(a, 16)))}
    result = collections.defaultdict(dict)
    gaps = []
    for start, end in zip(seeds, seeds[1:]):
        first, last = anchors[start], anchors[end]
        if right_seed_rank[last] - right_seed_rank[first] != 1:
            gaps.append((start, end, first, last, 'crossing'))
            continue
        i, j, k, l = left_index[start], left_index[end], right_index[first], right_index[last]
        equal = j - i == l - k
        delta = int(first, 16) - int(start, 16)
        same_delta = delta == int(last, 16) - int(end, 16)
        small_interval = equal and 0 < j - i - 1 <= 4
        local_counts = {}
        if small_interval:
            for key in ('shape', 'leaf_bytes'):
                local_counts[key] = (collections.Counter(old[a].get(key) for a in left[i + 1:j]),
                                     collections.Counter(new[b].get(key) for b in right[k + 1:l]))
        gaps.append((start, end, first, last, 'equal' if equal else 'changed_count'))
        for rank in range(i + 1, j):
            a = left[rank]
            expected = k + rank - i if equal else k + (rank - i) * (l - k) // (j - i)
            for position in range(max(k + 1, expected - 3), min(l, expected + 4)):
                b = right[position]
                result[a][b] = {'order': equal and position == expected, 'delta': False,
                                'bounds': [start, end, first, last], 'interval_count': j - i - 1 if equal else None}
                for key in ('shape', 'leaf_bytes'):
                    value = old[a].get(key)
                    result[a][b]['local_unique_' + key] = bool(small_interval and value and value == new[b].get(key)
                                                              and local_counts[key][0][value] == local_counts[key][1][value] == 1)
            if same_delta:
                b = right_addresses.get(int(a, 16) + delta)
                if b in right_index and k < right_index[b] < l:
                    result[a].setdefault(b, {'order': False, 'bounds': [start, end, first, last]})['delta'] = True
    return result, gaps


def similarity(first, second):
    return len(first & second) / len(first | second) if first and second else 0.0


def match(old, new, decisions=(), withheld=(), max_rounds=12, progress=None):
    named = symbol_pairs(old, new)
    rejected = set()
    accepted = {}
    def accept(a, b, reason, evidence, round_number):
        accepted[a] = {'new': b, 'reason': reason, 'evidence': evidence, 'round': round_number}
    for item in decisions:
        a, b = item['old'], item['new']
        if a not in old or b not in new or bool(old[a]['external']) != bool(new[b]['external']):
            raise ValueError('Review decision refers to incompatible or missing functions')
        if item['action'] not in ('accept', 'reject') or not item.get('note'):
            raise ValueError('Review decisions require accept/reject and a note')
        if item['action'] == 'reject':
            rejected.add((a, b))
        else:
            if a in accepted or b in {r['new'] for r in accepted.values()}:
                raise ValueError('Review decisions must be one-to-one')
            accept(a, b, 'manual', {'note': item['note']}, 0)
    for a, item in accepted.items():
        if (a, item['new']) in rejected:
            raise ValueError('Conflicting review decisions')
    used = {r['new'] for r in accepted.values()}
    for a, b in named.items():
        if a in withheld or (a, b) in rejected:
            continue
        if a in accepted or b in used:
            if a not in accepted or accepted[a]['new'] != b:
                raise ValueError('Review acceptance conflicts with a unique symbol')
            continue
        accept(a, b, 'symbol', {'symbols': sorted(set(old[a]['symbols']) & set(new[b]['symbols']))}, 0)
        used.add(b)
    strict = unique_pairs(old, new, lambda r: [r['shape']] if not r['external'] and r['confidence'] != 'low' else [])
    raw = unique_pairs(old, new, lambda r: [r['raw']] if r['raw_size'] >= 32 else [])
    leaves = unique_pairs(old, new, lambda r: [r.get('leaf_bytes', '')])
    indexes = {}
    for key in ('shape', 'relaxed'):
        index = collections.defaultdict(list)
        for b, row in new.items():
            if row[key] and not row['external']:
                index[row[key]].append(b)
        indexes[key] = index
    string_index = collections.defaultdict(set)
    for b, row in new.items():
        for value in row['strings']:
            string_index[value].add(b)
    old_string_counts = collections.Counter(s for row in old.values() for s in row['strings'])
    data_index = collections.defaultdict(set)
    for address, row in new.items():
        for reference in row.get('data_refs', ()):
            data_index[reference].add(address)
    history = []
    for round_number in range(1, max_rounds + 2):
        # 局所的な並びに依存した対応は、別の対応を作る基準へ昇格させない。
        anchors = {a: r['new'] for a, r in accepted.items() if r['reason'] != 'leaf_bytes_and_local_order'}
        used = {r['new'] for r in accepted.values()}
        data_anchors, data_owners = data_pairs(old, new, anchors)
        neighborhoods = context_pairs(old, new, anchors)
        layout, gaps = order_candidates(old, new, anchors)
        pool = {}
        reverse = collections.defaultdict(list)
        for a, first in old.items():
            if a in accepted or first['external']:
                continue
            candidates = set(layout.get(a, ()))
            for key in ('shape', 'relaxed'):
                matches = indexes[key].get(first[key], ())
                if len(matches) <= 32:
                    candidates.update(matches)
            if a in raw:
                candidates.add(raw[a])
            if a in leaves:
                candidates.add(leaves[a])
            expected_edges = {(direction, anchors[other]) for direction, other in first['calls'] if other in anchors}
            data_origins = {(kind, data_anchors[target]): target for kind, target in first.get('data_refs', ()) if target in data_anchors}
            expected_data = set(data_origins)
            votes = collections.Counter()
            for direction, other in expected_edges:
                opposite = 'in' if direction == 'out' else 'out'
                votes.update(target for kind, target in new[other]['calls'] if kind == opposite)
            candidates.update(b for b, _ in sorted(votes.items(), key=lambda item: (-item[1], item[0]))[:32])
            data_votes = collections.Counter(b for reference in expected_data for b in data_index[reference])
            candidates.update(b for b, _ in sorted(data_votes.items(), key=lambda item: (-item[1], item[0]))[:32])
            if a in neighborhoods:
                candidates.add(neighborhoods[a])
            for value in first['strings']:
                if old_string_counts[value] <= 5 and len(string_index[value]) <= 5:
                    candidates.update(string_index[value])
            ranked = []
            for b in sorted(candidates - used):
                second = new[b]
                if second['external'] or (a, b) in rejected:
                    continue
                position = layout.get(a, {}).get(b, {})
                shape = bool(first['shape']) and first['shape'] == second['shape']
                relaxed = bool(first['relaxed']) and first['relaxed'] == second['relaxed']
                common_edges = expected_edges & second['calls']
                context = len(common_edges)
                common_data = expected_data & second.get('data_refs', set())
                data_count = len(common_data)
                neighborhood = neighborhoods.get(a) == b
                rare_values = sorted(s for s in first['strings'] & second['strings']
                                     if old_string_counts[s] <= 5 and len(string_index[s]) <= 5)
                rare = len(rare_values)
                ratio = min(first['size'], second['size']) / max(first['size'], second['size'], 1)
                sketch = similarity(first['sketch'], second['sketch'])
                byte_match = raw.get(a) == b
                leaf_match = bool(first.get('leaf_bytes')) and first.get('leaf_bytes') == second.get('leaf_bytes')
                score = (50 * shape + 12 * (relaxed and not shape) + 15 * sketch + 10 * bool(position.get('order'))
                         + 5 * bool(position.get('delta')) + min(context, 4) * 4 + min(rare, 2) * 5 + 4 * ratio
                         + 15 * byte_match + min(data_count, 3) * 5 + 15 * neighborhood + 15 * leaf_match)
                evidence = dict(position, shape=shape, unique_shape=strict.get(a) == b, relaxed=relaxed,
                                code_sketch=round(sketch, 4), matched_edges=context, rare_strings=rare,
                                size_ratio=round(ratio, 4), exported_bytes=byte_match,
                                call_examples=sorted(common_edges)[:4], string_examples=rare_values[:3],
                                unique_neighborhood=neighborhood, matched_data=data_count,
                                leaf_bytes=leaf_match, unique_leaf=leaves.get(a) == b,
                                data_examples=[{'old': target, 'new': data_anchors[target], 'kind': kind,
                                                'anchor_owners_new': data_owners[target]}
                                               for kind, target in sorted((kind, data_origins[(kind, target)])
                                                                          for kind, target in common_data)[:3]],
                                tail_call_examples=sorted(common_edges & second.get('tail_calls', set()))[:3])
                sufficient = ''
                clean = first['confidence'] != 'low' and second['confidence'] != 'low'
                large = min(first['tokens'], second['tokens']) >= 64
                if clean and strict.get(a) == b and large and (position.get('order') or position.get('delta') or context or rare or data_count):
                    sufficient = 'unique_code_and_context'
                elif clean and shape and position.get('order') and position.get('delta') and (context >= 1 or data_count >= 1):
                    sufficient = 'code_order_and_references'
                elif clean and shape and neighborhood:
                    sufficient = 'code_and_unique_call_neighborhood'
                elif (clean and shape and leaf_match and (strict.get(a) == b or leaves.get(a) == b)
                      and position.get('order') and position.get('delta')):
                    sufficient = 'leaf_bytes_and_unique_code_order'
                elif (clean and shape and leaf_match and position.get('local_unique_shape')
                      and position.get('local_unique_leaf_bytes') and position.get('order') and position.get('delta')):
                    sufficient = 'leaf_bytes_and_local_order'
                elif clean and byte_match and (shape or context >= 1):
                    sufficient = 'exported_bytes_and_context'
                elif clean and relaxed and large and position.get('order') and context >= 2:
                    sufficient = 'relaxed_code_order_and_calls'
                elif (clean and large and sketch >= 0.85 and ratio >= 0.75 and position.get('order')
                      and position.get('delta') and context >= 3):
                    sufficient = 'similar_code_order_and_calls'
                elif clean and large and sketch >= 0.92 and ratio >= 0.75 and context >= 5 and rare:
                    sufficient = 'similar_code_calls_and_string'
                ranked.append({'new': b, 'score': round(score, 4), 'evidence': evidence, 'eligible': sufficient})
            ranked.sort(key=lambda row: (-row['score'], row['new']))
            pool[a] = ranked[:8]
            for item in ranked:
                reverse[item['new']].append((item['score'], a))
        for entries in reverse.values():
            entries.sort(key=lambda item: (-item[0], item[1]))
        promoted = 0
        for a, ranked in pool.items():
            if not ranked:
                continue
            best = ranked[0]
            alternatives = reverse[best['new']]
            margin = best['score'] - (ranked[1]['score'] if len(ranked) > 1 else 0)
            reverse_margin = best['score'] - (alternatives[1][0] if len(alternatives) > 1 else 0)
            best['evidence'].update(margin=round(margin, 4), reverse_margin=round(reverse_margin, 4),
                                    reciprocal_best=alternatives[0][1] == a)
            if round_number <= max_rounds and best['eligible'] and alternatives[0][1] == a and min(margin, reverse_margin) >= 8:
                accept(a, best['new'], best['eligible'], best['evidence'], round_number)
                promoted += 1
        history.append({'round': round_number, 'promoted': promoted, 'accepted': len(accepted), 'anchors': len(anchors)})
        if progress:
            progress(history[-1])
        if not promoted:
            return {'accepted': accepted, 'candidates': pool, 'history': history, 'gaps': gaps, 'named': named}
    raise RuntimeError('Matching did not reach a bounded stopping point')
