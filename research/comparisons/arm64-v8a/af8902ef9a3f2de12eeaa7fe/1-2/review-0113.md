# v15.7.4 → v16.0.0 · 追加調査 (113)

[一覧の目次](README.md)

<a id="review-d7efe43361371b0aa49f6fc0e1140628"></a>

### v16.0.0 [`0061d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d874.md) FUN_0061d874

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eb8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7edc.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.142857 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": 0.0
      },
      "new": "005f7eb8",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f7edc",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.142857,
        "reverse_margin": 0.0
      },
      "new": "005f8024",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f4287da9fa83e1183141bdf19d77678b"></a>

### v16.0.0 [`0061d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d890.md) FUN_0061d890

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8040.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`005f7edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7edc.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f7eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eb8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f7eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eec.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f7ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 66.0
      },
      "new": "005f8040",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f7edc",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8024",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-97138fd51af5b1ad76f6818a52fb1182"></a>

### v16.0.0 [`0061d89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d89c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f7ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f804c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f7eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7eec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f7edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7edc.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8040.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f7ef0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f804c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f7eec",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-20c8b42f78e272f2853cc2428214d833"></a>

### v16.0.0 [`0061d8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8a0.md) FUN_0061d8a0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 26.666667 · 採用条件未達 · 順位差 -10.476189999999999 / 26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a91ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91ccc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.1111111111111111
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.476189999999999,
        "reverse_margin": 26.666667
      },
      "new": "005f8024",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -26.666667
      },
      "new": "005f8050",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.0,
        "reverse_margin": -26.666667
      },
      "new": "00a91ccc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1cf3bf9af2194a1c24818121125f0290"></a>

### v16.0.0 [`0061d8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8c4.md) FUN_0061d8c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 37.142857 · 採用条件未達 · 順位差 10.476189999999999 / 37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.476189999999999,
        "reverse_margin": 37.142857
      },
      "new": "005f8024",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -37.142857
      },
      "new": "005f8050",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -37.142857
      },
      "new": "005f8074",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a9a310d4d18baf136b354bb53a530819"></a>

### v16.0.0 [`0061d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8d4.md) FUN_0061d8d4

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8084.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f804c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8040.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f8084",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f804c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8040",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-093bc07700d3c7e7e7a9b3530731a699"></a>

### v16.0.0 [`0061d8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8d8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f804c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8084.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8040.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8024.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f804c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8084",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8074",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-76b5f40c0f95f2f00fd96ae122034634"></a>

### v16.0.0 [`0061d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8dc.md) FUN_0061d8dc

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f7464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7464.md) · スコア 40.070175 · 採用条件未達 · 順位差 -8.614035999999999 / 2.368420999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75fc.md) · スコア 37.701754 · 採用条件未達 · 順位差 -3.1686909999999955 / -2.368420999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f7794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7794.md) · スコア 35.903272 · 採用条件未達 · 順位差 3.4495020000000025 / -4.166902999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d5c.md) · スコア 35.45614 · 採用条件未達 · 順位差 -12.318980000000003 / -4.614035000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00601410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601410.md) · スコア 35.333333 · 採用条件未達 · 順位差 -3.9784079999999946 / -4.736841999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 34.368421 · 採用条件未達 · 順位差 -15.515790000000003 / -5.701754000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f808c.md) · スコア 31.087719 · 採用条件未達 · 順位差 -4.296895999999997 / -8.982455999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f888c.md) · スコア 31.08453 · 採用条件未達 · 順位差 -5.893141 / -8.985644999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5789473684210527,
          0.5789473684210527
        ],
        "cfg_coverage": [
          0.3076923076923077,
          0.26666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.614035999999999,
        "reverse_margin": 2.368420999999998
      },
      "new": "005f7464",
      "score": 40.070175
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5394736842105263,
          0.5394736842105263
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.26666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.1686909999999955,
        "reverse_margin": -2.368420999999998
      },
      "new": "005f75fc",
      "score": 37.701754
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5263157894736842,
          0.5263157894736842
        ],
        "cfg_coverage": [
          0.21621621621621623,
          0.26666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.4495020000000025,
        "reverse_margin": -4.166902999999998
      },
      "new": "005f7794",
      "score": 35.903272
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6c1c4f95db38144c9a170f69967ef7d3"></a>

### v16.0.0 [`0061da0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da0c.md) FUN_0061da0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 17.142857 · 採用条件未達 · 順位差 17.142857 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.2857142857142857
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.142857,
        "reverse_margin": 17.142857
      },
      "new": "005f81bc",
      "score": 17.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -17.142857
      },
      "new": "005f8050",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -17.142857
      },
      "new": "005f8074",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-185e70f1430d044dea64570b488e9bab"></a>

### v16.0.0 [`0061da28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da28.md) FUN_0061da28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8050.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8084.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8088.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8074",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f81bc",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8050",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-36749e72d7a368e103af1488a05669fe"></a>

### v16.0.0 [`0061da34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da34.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8088.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9474 · 
- 2. [`005f8084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8084.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8074.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9474
      },
      "new": "005f8088",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8084",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8074",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-35fc0c25c4b15fad35dfc5db16b04ef4"></a>

### v16.0.0 [`0061da38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da38.md) FUN_0061da38

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00a91d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91d74.md) · スコア 73.333333 · 採用条件未達 · 順位差 0.0 / 73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -17.142857 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 73.333333
      },
      "new": "00a91d74",
      "score": 73.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.142857,
        "reverse_margin": -73.333333
      },
      "new": "005f81bc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5ada4c2c82c7b95894156c2b68d24ad3"></a>

### v16.0.0 [`0061da5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da5c.md) FUN_0061da5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -17.142857 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -26.666667 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.142857,
        "reverse_margin": 0.0
      },
      "new": "005f81bc",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.666667,
        "reverse_margin": 0.0
      },
      "new": "005f81e8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d405fb252c0403d0a91c32490badabc1"></a>

### v16.0.0 [`0061da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da6c.md) FUN_0061da6c

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8088.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f81e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8088",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f81e4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f81d8",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0e1180487f6bc4856a7e708be4f5729b"></a>

### v16.0.0 [`0061da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da70.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f81e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e4.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9474 · 
- 2. [`005f821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f821c.md) · スコア 4.0 · 採用条件未達 · 順位差 0.0 / -0.0526 · 
- 3. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f81bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9474
      },
      "new": "005f81e4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": -0.0526
      },
      "new": "005f821c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f820c",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e553d10e5664f198f1d89d2dc2272e78"></a>

### v16.0.0 [`0061da74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da74.md) FUN_0061da74

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f86f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f4.md) · スコア 41.500975 · 採用条件未達 · 順位差 -0.13870100000000463 / 1.5302149999999983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d5c.md) · スコア 39.97076 · 採用条件未達 · 順位差 -7.804360000000003 / -1.5302149999999983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8224.md) · スコア 39.181287 · 採用条件未達 · 順位差 -3.2883490000000037 / -2.3196879999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 37.521368 · 採用条件未達 · 順位差 -2.4786319999999975 / -3.9796069999999943 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 36.959064 · 採用条件未達 · 順位差 -12.925147000000003 / -4.541910999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f855c.md) · スコア 34.444444 · 採用条件未達 · 順位差 -10.671345000000002 / -7.056531 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75fc.md) · スコア 33.80117 · 採用条件未達 · 順位差 -7.0692749999999975 / -7.699804999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f888c.md) · スコア 32.240829 · 採用条件未達 · 順位差 -4.736842000000003 / -9.260145999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6052631578947368,
          0.6052631578947368
        ],
        "cfg_coverage": [
          0.30434782608695654,
          0.25925925925925924
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -0.13870100000000463,
        "reverse_margin": 1.5302149999999983
      },
      "new": "005f86f4",
      "score": 41.500975
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5921052631578947,
          0.5921052631578947
        ],
        "cfg_coverage": [
          0.2857142857142857,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.804360000000003,
        "reverse_margin": -1.5302149999999983
      },
      "new": "005f7d5c",
      "score": 39.97076
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5789473684210527,
          0.5789473684210527
        ],
        "cfg_coverage": [
          0.25,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.2883490000000037,
        "reverse_margin": -2.3196879999999993
      },
      "new": "005f8224",
      "score": 39.181287
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aa64b00de21a892152ddb12ae38a7faf"></a>

### v16.0.0 [`0061dba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dba4.md) FUN_0061dba4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -26.666667 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.142857,
        "reverse_margin": 17.142857
      },
      "new": "005f8354",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.2857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -17.142857
      },
      "new": "005f820c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.666667,
        "reverse_margin": -54.285714
      },
      "new": "005f81e8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-212676247027918492e97a68dc62c947"></a>

### v16.0.0 [`0061dbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dbc0.md) FUN_0061dbc0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f81e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f821c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8220.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f820c",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8354",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f81e4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9a31d6d93f2139eda3f0e7594f77d274"></a>

### v16.0.0 [`0061dbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dbcc.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8220.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9474 · 
- 2. [`005f821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f821c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8370.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f81e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81e8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9474
      },
      "new": "005f8220",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f821c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f820c",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b27f89e7a97b462a957d5f24725c736a"></a>

### v16.0.0 [`0061dbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dbd0.md) FUN_0061dbd0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f820c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f820c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00874684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874684.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a91e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e1c.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f820c",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -54.285714,
        "reverse_margin": 0.0
      },
      "new": "005f8354",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00874684",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7baa437d4a986b8f67b77fc6d2bbd266"></a>

### v16.0.0 [`0061dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dbf4.md) FUN_0061dbf4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008746a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008746a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00a91e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e40.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008746a8",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00a91e40",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.142857,
        "reverse_margin": -42.857143
      },
      "new": "005f8354",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-22a425232720468f48c90dad722f539d"></a>

### v16.0.0 [`0061dc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc04.md) FUN_0061dc04

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8220.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f837c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f837c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8370.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8220",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f837c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8370",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7a6c9c6647ce402a4487b65f00aea5f6"></a>

### v16.0.0 [`0061dc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc08.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f837c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f837c.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9474 · 
- 2. [`005f83b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b4.md) · スコア 4.0 · 採用条件未達 · 順位差 0.0 / -0.0526 · 
- 3. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8370.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8354.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9474
      },
      "new": "005f837c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": -0.0526
      },
      "new": "005f83b4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f83a4",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b3c0b5c5e7a6aeec50f7d6623c72d2c"></a>

### v16.0.0 [`0061dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc0c.md) FUN_0061dc0c

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 25.948718 · 採用条件未達 · 順位差 -14.051282 / 0.5641029999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7794.md) · スコア 25.384615 · 採用条件未達 · 順位差 -10.518657000000001 / -0.5641029999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f808c.md) · スコア 24.410256 · 採用条件未達 · 順位差 -10.974358999999996 / -1.538461999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f888c.md) · スコア 23.846154 · 採用条件未達 · 順位差 -13.131517000000002 / -2.102564000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f72cc.md) · スコア 22.769231 · 採用条件未達 · 順位差 -8.508963999999999 / -3.179486999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f792c.md) · スコア 22.769231 · 採用条件未達 · 順位差 -8.663518 / -3.179486999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f7ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ac4.md) · スコア 11.498599 · 採用条件未達 · 順位差 -9.697829999999998 / -14.450118999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006700bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md) · スコア 8.461538 · 採用条件未達 · 順位差 -15.990075 / -17.487180000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.41025641025641024,
          0.41025641025641024
        ],
        "cfg_coverage": [
          0.08,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.051282,
        "reverse_margin": 0.5641029999999994
      },
      "new": "005f83bc",
      "score": 25.948718
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4342105263157895,
          0.4230769230769231
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.518657000000001,
        "reverse_margin": -0.5641029999999994
      },
      "new": "005f7794",
      "score": 25.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.39473684210526316,
          0.38461538461538464
        ],
        "cfg_coverage": [
          0.07692307692307693,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.974358999999996,
        "reverse_margin": -1.538461999999999
      },
      "new": "005f808c",
      "score": 24.410256
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c502e75441badcaeee086ec377765b85"></a>

### v16.0.0 [`0061dd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd44.md) FUN_0061dd44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 54.285714,
        "reverse_margin": 54.285714
      },
      "new": "005f84f4",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -54.285714
      },
      "new": "005f8380",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -54.285714
      },
      "new": "005f83a4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a49f8bdc97893d97a38b7d0ea5d7fa1f"></a>

### v16.0.0 [`0061dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd60.md) FUN_0061dd60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f837c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f837c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f83b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f83b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f83a4",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f84f4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f837c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-120f287ed1ba74788f05798066b29b19"></a>

### v16.0.0 [`0061dd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd6c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f83b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b8.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9487 · 
- 2. [`005f83b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8510.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8380.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9487
      },
      "new": "005f83b8",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f83b4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f83a4",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5f4b85d303c1712f38a9dae6f790eb0f"></a>

### v16.0.0 [`0061dd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd70.md) FUN_0061dd70

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f83a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f83a4",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -54.285714,
        "reverse_margin": 0.0
      },
      "new": "005f84f4",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.0,
        "reverse_margin": 0.0
      },
      "new": "005f86b8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9a3387b92badc9b5a38b4b3b251ba4a1"></a>

### v16.0.0 [`0061dd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd94.md) FUN_0061dd94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00758360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758360.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00874940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874940.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00a91f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91f98.md) · スコア 80.0 · 採用条件未達 · 順位差 42.857143 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 80.0,
        "reverse_margin": 0.0
      },
      "new": "00758360",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 0.0
      },
      "new": "00874940",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 42.857143,
        "reverse_margin": 0.0
      },
      "new": "00a91f98",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3be37740a77efaab9cf7bddb679380b3"></a>

### v16.0.0 [`0061dda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dda4.md) FUN_0061dda4

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f83b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83b8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f851c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f851c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8510.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f83b8",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f851c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8510",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-20c14240ffbc79c75c742d4bc5575e69"></a>

### v16.0.0 [`0061dda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dda8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f851c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f851c.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 68.9487 · 
- 2. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8510.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f84f4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 68.9487
      },
      "new": "005f851c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8544",
      "score": 1.9375
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8510",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-61d78bba8bae689f311b294e09bca34f"></a>

### v16.0.0 [`0061ddac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061ddac.md) FUN_0061ddac

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d5c.md) · スコア 42.715789 · 採用条件未達 · 順位差 -5.059331 / 1.5789469999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 41.136842 · 採用条件未達 · 順位差 -8.747368999999999 / -1.5789469999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75fc.md) · スコア 37.147368 · 採用条件未達 · 順位差 -3.7230769999999964 / -5.568421000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f86f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f4.md) · スコア 35.578947 · 採用条件未達 · 順位差 -6.060729000000002 / -7.1368420000000015 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00601410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601410.md) · スコア 34.778947 · 採用条件未達 · 順位差 -4.5327939999999955 / -7.936841999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f7464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7464.md) · スコア 34.635628 · 採用条件未達 · 順位差 -14.048583 / -8.080161000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 34.0 · 採用条件未達 · 順位差 -6.0 / -8.715789000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f855c.md) · スコア 34.0 · 採用条件未達 · 順位差 -11.115789 / -8.715789000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6052631578947368,
          0.6052631578947368
        ],
        "cfg_coverage": [
          0.38095238095238093,
          0.32
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.059331,
        "reverse_margin": 1.5789469999999994
      },
      "new": "005f7d5c",
      "score": 42.715789
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5789473684210527,
          0.5789473684210527
        ],
        "cfg_coverage": [
          0.32,
          0.32
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.747368999999999,
        "reverse_margin": -1.5789469999999994
      },
      "new": "005f7ef4",
      "score": 41.136842
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5657894736842105,
          0.5657894736842105
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.16
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.7230769999999964,
        "reverse_margin": -5.568421000000001
      },
      "new": "005f75fc",
      "score": 37.147368
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-884fe6a876fec9235d1e4972f8f11e89"></a>

### v16.0.0 [`0061dedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dedc.md) FUN_0061dedc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 37.142857 · 採用条件未達 · 順位差 2.8571430000000007 / 10.476189999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -10.476189999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.2857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.8571430000000007,
        "reverse_margin": 10.476189999999999
      },
      "new": "005f868c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.14285714285714285
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.333332999999996,
        "reverse_margin": -10.476189999999999
      },
      "new": "005f8520",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -37.142857
      },
      "new": "005f8544",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2d2ebf49afd42bd95bb18942438f1429"></a>

### v16.0.0 [`0061def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061def8.md) FUN_0061def8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f851c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f851c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8554.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8558.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8544",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f851c",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8520",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1a97e0646add097473aad551a312bcb7"></a>

### v16.0.0 [`0061df04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df04.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8558.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 68.9474 · 
- 2. [`005f8554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8554.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 68.9474
      },
      "new": "005f8558",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8554",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8544",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ce861d47817ff0d48ab4e014d222486f"></a>

### v16.0.0 [`0061df08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df08.md) FUN_0061df08

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8520.md) · スコア 60.0 · 採用条件未達 · 順位差 33.333332999999996 / 26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0043d1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md) · スコア 33.333333 · 採用条件未達 · 順位差 33.333333 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0087796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/0087796c.md) · スコア 33.333333 · 採用条件未達 · 順位差 33.333333 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 20.0 · 採用条件未達 · 順位差 -17.142857 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.333332999999996,
        "reverse_margin": 26.666666999999997
      },
      "new": "005f8520",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 33.333333,
        "reverse_margin": -26.666666999999997
      },
      "new": "0043d1f8",
      "score": 33.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 33.333333,
        "reverse_margin": -26.666666999999997
      },
      "new": "0087796c",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-16356c42107b0ba10ee7f0dbea0b3bed"></a>

### v16.0.0 [`0061df2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df2c.md) FUN_0061df2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0043d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d21c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00877990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877990.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005f8544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8544.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.142857 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0043d21c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00877990",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "005f8544",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0b4bdb4486208be1906cd13c86d2412b"></a>

### v16.0.0 [`0061df3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df3c.md) FUN_0061df3c

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8554.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f8558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8558.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f86b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f86a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86a8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f8554",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8558",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86b4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-66225664c825d13be1324ede1818a92c"></a>

### v16.0.0 [`0061df40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df40.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8558.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f86b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f86a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86a8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8558",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f86b4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86dc",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b6a558f2dff2e624570720e2719872c7"></a>

### v16.0.0 [`0061df44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df44.md) FUN_0061df44

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f855c.md) · スコア 37.712551 · 採用条件未達 · 順位差 -7.403238000000002 / 1.578947999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d5c.md) · スコア 36.133603 · 採用条件未達 · 順位差 -11.641517 / -1.578947999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8224.md) · スコア 33.785425 · 採用条件未達 · 順位差 -8.684211000000005 / -3.9271260000000012 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f888c.md) · スコア 33.452951 · 採用条件未達 · 順位差 -3.524720000000002 / -4.259599999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f86f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f4.md) · スコア 30.62753 · 採用条件未達 · 順位差 -11.012146000000001 / -7.085020999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 30.0 · 採用条件未達 · 順位差 -10.0 / -7.712550999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 26.781377 · 採用条件未達 · 順位差 -23.102834 / -10.931173999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f7794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7794.md) · スコア 26.13798 · 採用条件未達 · 順位差 -9.765292000000002 / -11.574570999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5131578947368421,
          0.5131578947368421
        ],
        "cfg_coverage": [
          0.375,
          0.34615384615384615
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.403238000000002,
        "reverse_margin": 1.578947999999997
      },
      "new": "005f855c",
      "score": 37.712551
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4868421052631579,
          0.4868421052631579
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.34615384615384615
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.641517,
        "reverse_margin": -1.578947999999997
      },
      "new": "005f7d5c",
      "score": 36.133603
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4605263157894737,
          0.4605263157894737
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.3076923076923077
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.684211000000005,
        "reverse_margin": -3.9271260000000012
      },
      "new": "005f8224",
      "score": 33.785425
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0afd4372431b1830a5356afb4835634b"></a>

### v16.0.0 [`0061e074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e074.md) FUN_0061e074

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f868c.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.142857 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.714286,
        "reverse_margin": 17.142857
      },
      "new": "005f8824",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.2857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -17.142857
      },
      "new": "005f86dc",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.142857,
        "reverse_margin": -54.285714
      },
      "new": "005f868c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ae72e4220b7a032e2d33b4ea50d3c494"></a>

### v16.0.0 [`0061e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e090.md) FUN_0061e090

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f86a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86a8.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f86b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f86ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86ec.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f86f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 66.0
      },
      "new": "005f86a8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86dc",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86b4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5e2b169562ddec189695b101c6c701e1"></a>

### v16.0.0 [`0061e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e09c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f86b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f86f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f0.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f86ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86ec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86b4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f86f0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86ec",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a28012fbf01d50fe60bd18068078773f"></a>

### v16.0.0 [`0061e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0a0.md) FUN_0061e0a0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f86b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86b8.md) · スコア 53.333333 · 採用条件未達 · 順位差 -6.666666999999997 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a926a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a926a4.md) · スコア 33.333333 · 採用条件未達 · 順位差 6.666666000000003 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -53.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -53.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.666666999999997,
        "reverse_margin": 20.0
      },
      "new": "005f86b8",
      "score": 53.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.666666000000003,
        "reverse_margin": -20.0
      },
      "new": "00a926a4",
      "score": 33.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -53.333333
      },
      "new": "005f86dc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f92b2ddc5a481ea7efcc009e237295e3"></a>

### v16.0.0 [`0061e0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0c4.md) FUN_0061e0c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a926c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a92/00a926c8.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005f86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86dc.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "00a926c8",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "005f86dc",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -42.857143
      },
      "new": "005f8824",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-82119786ca9532ad3259be498e69f5fa"></a>

### v16.0.0 [`0061e0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0d4.md) FUN_0061e0d4

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f86ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86ec.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f86f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f884c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8840.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f86ec",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86f0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f884c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-222896c10b7f6702253280fe70af416e"></a>

### v16.0.0 [`0061e0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0d8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f86f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f884c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8840.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f86f0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f884c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8874",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c31552f2ffc2d1aca08c94bc38290232"></a>

### v16.0.0 [`0061e0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0dc.md) FUN_0061e0dc

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 47.505263 · 採用条件未達 · 順位差 -2.378948000000001 / 2.5739129999999975 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d5c.md) · スコア 44.93135 · 採用条件未達 · 順位差 -2.8437699999999992 / -2.5739129999999975 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f86f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86f4.md) · スコア 36.796339 · 採用条件未達 · 順位差 -4.843336999999998 / -10.708923999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f855c.md) · スコア 35.0 · 採用条件未達 · 順位差 -10.115789 / -12.505263 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75fc.md) · スコア 34.912281 · 採用条件未達 · 順位差 -5.9581639999999965 / -12.592982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f8224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8224.md) · スコア 34.912281 · 採用条件未達 · 順位差 -7.557355000000001 / -12.592982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 34.8 · 採用条件未達 · 順位差 -5.200000000000003 / -12.705263000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00601410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601410.md) · スコア 32.54386 · 採用条件未達 · 順位差 -6.767880999999996 / -14.961402999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.618421052631579,
          0.618421052631579
        ],
        "cfg_coverage": [
          0.52,
          0.5652173913043478
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.378948000000001,
        "reverse_margin": 2.5739129999999975
      },
      "new": "005f7ef4",
      "score": 47.505263
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.618421052631579,
          0.618421052631579
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.391304347826087
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.8437699999999992,
        "reverse_margin": -2.5739129999999975
      },
      "new": "005f7d5c",
      "score": 44.93135
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5263157894736842,
          0.5263157894736842
        ],
        "cfg_coverage": [
          0.2608695652173913,
          0.2608695652173913
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.843336999999998,
        "reverse_margin": -10.708923999999996
      },
      "new": "005f86f4",
      "score": 36.796339
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-eb825339d66f82decdac6f930762da69"></a>

### v16.0.0 [`0061e20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e20c.md) FUN_0061e20c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8824.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -27.619047 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.714286,
        "reverse_margin": 0.0
      },
      "new": "005f8824",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.714286,
        "reverse_margin": 0.0
      },
      "new": "005f89bc",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.2857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -17.142857
      },
      "new": "005f8874",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2311c70391b887c48a60030400ec2c1a"></a>

### v16.0.0 [`0061e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e228.md) FUN_0061e228

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8840.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f884c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8884.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8888.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 66.0
      },
      "new": "005f8840",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8874",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f884c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-91a6fbcd1df38cbc216ca5f69c0e05f9"></a>

### v16.0.0 [`0061e234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e234.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f884c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8888.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8884.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f884c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8888",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8884",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e66f6e1f6246150f5e5ca4a6ee75fbbb"></a>

### v16.0.0 [`0061e238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e238.md) FUN_0061e238

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f8850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8850.md) · スコア 60.0 · 採用条件未達 · 順位差 -13.333332999999996 / 33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.333332999999996,
        "reverse_margin": 33.333332999999996
      },
      "new": "005f8850",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.1111111111111111
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.333332999999996,
        "reverse_margin": -33.333332999999996
      },
      "new": "005f8874",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.1111111111111111
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.333332999999996,
        "reverse_margin": -33.333332999999996
      },
      "new": "005f89bc",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-340a7d55e6d7e3b79072a6d9ac20b444"></a>

### v16.0.0 [`0061e25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e25c.md) FUN_0061e25c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8874.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.0,
        "reverse_margin": 12.857143
      },
      "new": "005f8874",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -12.857143
      },
      "new": "005f89bc",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-67a5157631e5e009f25cfcdc3e391572"></a>

### v16.0.0 [`0061e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e26c.md) FUN_0061e26c

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8884.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f8888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8888.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f89e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f8884",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8888",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f89e4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eaab43f3a375a114d96863a7280da364"></a>

### v16.0.0 [`0061e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e270.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8888.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f89e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8888",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f89e4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f89d8",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9207d773ed2c6349e392fb4788918593"></a>

### v16.0.0 [`0061e274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e274.md) FUN_0061e274

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)

- 1. [`005f72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f72cc.md) · スコア 29.24498 · 採用条件未達 · 順位差 -2.0332149999999984 / 1.277109000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 27.967871 · 採用条件未達 · 順位差 -12.032129000000001 / -1.277109000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f7464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7464.md) · スコア 25.911647 · 採用条件未達 · 順位差 -22.772564 / -3.333333000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f7794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7794.md) · スコア 25.659394 · 採用条件未達 · 順位差 -10.243878000000002 / -3.585586000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75fc.md) · スコア 24.409639 · 採用条件未達 · 順位差 -16.460805999999998 / -4.835341000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f792c.md) · スコア 23.742972 · 採用条件未達 · 順位差 -7.689776999999999 / -5.502008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ef4.md) · スコア 23.742972 · 採用条件未達 · 順位差 -26.141239 / -5.502008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f888c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f888c.md) · スコア 23.015699 · 採用条件未達 · 順位差 -13.961972 / -6.229281 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4473684210526316,
          0.40963855421686746
        ],
        "cfg_coverage": [
          0.25,
          0.23333333333333334
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.0332149999999984,
        "reverse_margin": 1.277109000000003
      },
      "new": "005f72cc",
      "score": 29.24498
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.44871794871794873,
          0.42168674698795183
        ],
        "cfg_coverage": [
          0.16,
          0.13333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.032129000000001,
        "reverse_margin": -1.277109000000003
      },
      "new": "005f83bc",
      "score": 27.967871
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4473684210526316,
          0.40963855421686746
        ],
        "cfg_coverage": [
          0.07692307692307693,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.772564,
        "reverse_margin": -3.333333000000003
      },
      "new": "005f7464",
      "score": 25.911647
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd08142b43a12a93a63a58edb2042282"></a>

### v16.0.0 [`0061e3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3c0.md) FUN_0061e3c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f89bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f89bc",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": 0.0
      },
      "new": "005f89e8",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f8a0c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-319b81c4146d621ea5fddc4a150d562f"></a>

### v16.0.0 [`0061e3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3dc.md) FUN_0061e3dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89d8.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f89e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a1c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a20.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 66.0
      },
      "new": "005f89d8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8a0c",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f89e4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d15cebde10a77e5410f5d3c4b83ef93c"></a>

### v16.0.0 [`0061e3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3e8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f89e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a20.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a1c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f89e4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8a20",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8a1c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab87cc3e40e9bdf7e5ae544cedad45f9"></a>

### v16.0.0 [`0061e3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3ec.md) FUN_0061e3ec

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`0062fd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fd20.md) · スコア 60.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0087a4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4d4.md) · スコア 60.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0089b75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b75c.md) · スコア 60.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007c6e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e78.md) · スコア 0.0 · 採用条件未達 · 順位差 -46.666667 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00879ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ac8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0062fd20",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0087a4d4",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0089b75c",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-01e8576853092889a075c951897e31a2"></a>

### v16.0.0 [`0061e410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e410.md) FUN_0061e410

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008789c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/008789c8.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 2. [`005f89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "008789c8",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -60.0
      },
      "new": "005f89e8",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -60.0
      },
      "new": "005f8a0c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8c92d18c01af9c1e7b5db78b632188cd"></a>

### v16.0.0 [`0061e420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e420.md) FUN_0061e420

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a1c.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f8a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a20.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b00.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8af4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a0c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f8a1c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8a20",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b00",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1247eb0aea3a7ef83597cf35a99dc4d8"></a>

### v16.0.0 [`0061e424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e424.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a20.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b00.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a1c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8af4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8a20",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8b00",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8a1c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-683c2faa849c74178d780c240d2c9499"></a>

### v16.0.0 [`0061e428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e428.md) FUN_0061e428

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00820074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

- 1. [`005f8a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8a24.md) · スコア 24.444444 · 採用条件未達 · 順位差 11.111111000000001 / 15.111111000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0062f8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f8f0.md) · スコア 9.333333 · 採用条件未達 · 順位差 -25.111110999999998 / -15.111111000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00947c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/00947c3c.md) · スコア 8.235294 · 採用条件未達 · 順位差 -18.562092 / -16.20915 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ffa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa34.md) · スコア 6.0 · 採用条件未達 · 順位差 -21.7 / -18.444444 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005b6368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6368.md) · スコア 5.333333 · 採用条件未達 · 順位差 -64.666667 / -19.111111 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f16dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f16dc.md) · スコア 5.333333 · 採用条件未達 · 順位差 -57.435897999999995 / -19.111111 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f7188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7188.md) · スコア 5.333333 · 採用条件未達 · 順位差 -64.666667 / -19.111111 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00600e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600e48.md) · スコア 5.333333 · 採用条件未達 · 順位差 -64.666667 / -19.111111 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.3333333333333333
        ],
        "cfg_coverage": [
          0.2857142857142857,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.111111000000001,
        "reverse_margin": 15.111111000000001
      },
      "new": "005f8a24",
      "score": 24.444444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.15555555555555556
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.111110999999998,
        "reverse_margin": -15.111111000000001
      },
      "new": "0062f8f0",
      "score": 9.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13725490196078433,
          0.15555555555555556
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.562092,
        "reverse_margin": -16.20915
      },
      "new": "00947c3c",
      "score": 8.235294
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c13e1ce1547359e4d1272b2cad9153da"></a>

### v16.0.0 [`0061e4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e4dc.md) FUN_0061e4dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 54.285714 · 採用条件未達 · 順位差 49.670328999999995 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 0.0 · 採用条件未達 · 順位差 -55.384615 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.670328999999995,
        "reverse_margin": 54.285714
      },
      "new": "005f8bf8",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -54.285714
      },
      "new": "005f8ad8",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -55.384615,
        "reverse_margin": -54.285714
      },
      "new": "005f8b04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c0aabef5b3d795b8a123e79e31363961"></a>

### v16.0.0 [`0061e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e4f8.md) FUN_0061e4f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8af4.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.6 · 
- 2. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8ad8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b00.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b4c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b50.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 66.6
      },
      "new": "005f8af4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b38",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8ad8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ee2b9f5d7394746c32c6a3f14e1f8409"></a>

### v16.0.0 [`0061e504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e504.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b00.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b50.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b4c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8af4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b00",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8b50",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b4c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5b7125e5ae72eda89c16353d550f48b6"></a>

### v16.0.0 [`0061e508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e508.md) FUN_0061e508

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`0067c940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c940.md) · スコア 50.769231 · 採用条件未達 · 順位差 50.769231 / 27.692307999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 23.076923 · 採用条件未達 · 順位差 -32.307691999999996 / -27.692307999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 4.615385 · 採用条件未達 · 順位差 -49.670328999999995 / -46.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -50.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8461538461538461,
          0.8461538461538461
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 50.769231,
        "reverse_margin": 27.692307999999997
      },
      "new": "0067c940",
      "score": 50.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38461538461538464,
          0.38461538461538464
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.307691999999996,
        "reverse_margin": -27.692307999999997
      },
      "new": "005f8b04",
      "score": 23.076923
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -49.670328999999995,
        "reverse_margin": -46.153846
      },
      "new": "005f8bf8",
      "score": 4.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1ed94026486d0f7b9609b0b29ed2bd9d"></a>

### v16.0.0 [`0061e53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e53c.md) FUN_0061e53c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0067c974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c974.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 24.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 56.0 · 採用条件未達 · 順位差 -24.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005f8b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b04.md) · スコア 24.615385 · 採用条件未達 · 順位差 -30.769229999999997 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 80.0,
        "reverse_margin": 24.0
      },
      "new": "0067c974",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.6
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.0,
        "reverse_margin": -24.0
      },
      "new": "005f8b38",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.2
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.769229999999997,
        "reverse_margin": -55.384615
      },
      "new": "005f8b04",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-788d99eb31c9169ade7f5769178d7688"></a>

### v16.0.0 [`0061e550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e550.md) FUN_0061e550

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b4c.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 0.0 · 
- 2. [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) · スコア 54.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b50.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c14.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b38.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 0.0
      },
      "new": "005f8b4c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8c20",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b50",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d5c637510dc3372a52d2a2a6eb651617"></a>

### v16.0.0 [`0061e554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e554.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b50.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c24.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b4c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c14.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b50",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8c24",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8b4c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-78639aec992c02d7102ca9e0987d9aa7"></a>

### v16.0.0 [`0061e558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md) FUN_0061e558

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00747390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747390.md) [`00747398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747398.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

- 1. [`005f8b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b54.md) · スコア 20.487805 · 採用条件未達 · 順位差 -7.5 / 5.853659000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a8f1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f1fc.md) · スコア 14.634146 · 採用条件未達 · 順位差 -3.6991870000000002 / -5.853659000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a1e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md) · スコア 10.588235 · 採用条件未達 · 順位差 -25.294118000000005 / -9.899570000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a204dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a204dc.md) · スコア 10.588235 · 採用条件未達 · 順位差 -15.935829 / -9.899570000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f182c.md) · スコア 10.0 · 採用条件未達 · 順位差 -53.111111 / -10.487805000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006fbf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbf60.md) · スコア 7.317073 · 採用条件未達 · 順位差 2.872629 / -13.170732000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) · スコア 7.186992 · 採用条件未達 · 順位差 -0.7077450000000001 / -13.300813000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00581cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cec.md) · スコア 6.653659 · 採用条件未達 · 順位差 0.29810300000000023 / -13.834146 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34146341463414637,
          0.34146341463414637
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.5,
        "reverse_margin": 5.853659000000002
      },
      "new": "005f8b54",
      "score": 20.487805
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3225806451612903,
          0.24390243902439024
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.6991870000000002,
        "reverse_margin": -5.853659000000002
      },
      "new": "00a8f1fc",
      "score": 14.634146
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17647058823529413,
          0.21951219512195122
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.294118000000005,
        "reverse_margin": -9.899570000000002
      },
      "new": "00a1e19c",
      "score": 10.588235
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5678489bca84b47b7161e76458b82004"></a>

### v16.0.0 [`0061e5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e5fc.md) FUN_0061e5fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a1fd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd0c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 42.857143 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 0.0 · 採用条件未達 · 順位差 -8.571429 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 42.857143
      },
      "new": "00a1fd0c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.2857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -42.857143
      },
      "new": "005f8c4c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.14285714285714285
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.66666599999999,
        "reverse_margin": -53.333332999999996
      },
      "new": "005f8c28",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d207d5161f0593589c5f3556c08ff81"></a>

### v16.0.0 [`0061e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e618.md) FUN_0061e618

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c14.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 66.0 · 
- 2. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8bf8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c24.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 66.0
      },
      "new": "005f8c14",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c4c",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8bf8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f13789c079c6cf16e14e1d95262e3f80"></a>

### v16.0.0 [`0061e624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e624.md) FUN_0061e624

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c5c.md) · スコア 54.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c24.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c14.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c20",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8c5c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c24",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8f1abc35f13dde4eea84b9ef1ffe3880"></a>

### v16.0.0 [`0061e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e628.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c24.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c60.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c5c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c24",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f8c60",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c20",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-63d716b53ad30f12b8f2189d20135f5a"></a>

### v16.0.0 [`0061e62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e62c.md) FUN_0061e62c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": 0.0
      },
      "new": "005f8c28",
      "score": 0.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "005f8c4c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ee0aeeed87c742055602a9b09d7525ce"></a>

### v16.0.0 [`0061e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e650.md) FUN_0061e650

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f8c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c28.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 0.0 · 採用条件未達 · 順位差 -8.571429 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.0,
        "reverse_margin": 23.333333
      },
      "new": "005f8c4c",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.25
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.66666599999999,
        "reverse_margin": -23.333333
      },
      "new": "005f8c28",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.571429,
        "reverse_margin": -50.0
      },
      "new": "005f9078",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9ca39a7879362e4912bb6aaf3f374396"></a>

### v16.0.0 [`0061e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e660.md) FUN_0061e660

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c5c.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f8c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c60.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9094.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f8c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c4c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c5c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c60",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9094",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d646fff1c55bfff2f8e929b0bbf5d583"></a>

### v16.0.0 [`0061e664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e664.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f8c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c60.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f90a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a0.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c5c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9094.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c60",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f90a0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c5c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0d15952a501dc88b5bcdfe03b9aae3c3"></a>

### v16.0.0 [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) FUN_0061e668

`competing_candidates` 

呼出元 0件  · 呼出先 24件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)

- 1. [`005f8c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c64.md) · スコア 33.898001 · 採用条件未達 · 順位差 24.47494 / 24.214721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006b3674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md) · スコア 9.68328 · 採用条件未達 · 順位差 4.9848669999999995 / -24.214721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007c42e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c42e8.md) · スコア 9.155317 · 採用条件未達 · 順位差 3.68865 / -24.742684 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00840d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md) · スコア 8.087832 · 採用条件未達 · 順位差 1.1898730000000004 / -25.810169000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007c4664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4664.md) · スコア 7.977398 · 採用条件未達 · 順位差 2.510731 / -25.920603 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) · スコア 7.318748 · 採用条件未達 · 順位差 -20.97719 / -26.579253 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007c3fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3fc4.md) · スコア 6.495219 · 採用条件未達 · 順位差 -0.9354850000000008 / -27.402782000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00470404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md) · スコア 6.133584 · 採用条件未達 · 順位差 -0.3734580000000003 / -27.764417 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45320197044334976,
          0.45320197044334976
        ],
        "cfg_coverage": [
          0.2711864406779661,
          0.23529411764705882
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.47494,
        "reverse_margin": 24.214721
      },
      "new": "005f8c64",
      "score": 33.898001
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18518518518518517,
          0.12315270935960591
        ],
        "cfg_coverage": [
          0.029411764705882353,
          0.014705882352941176
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.9848669999999995,
        "reverse_margin": -24.214721
      },
      "new": "006b3674",
      "score": 9.68328
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.26,
          0.12807881773399016
        ],
        "cfg_coverage": [
          0.21739130434782608,
          0.07352941176470588
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 3.68865,
        "reverse_margin": -24.742684
      },
      "new": "007c42e8",
      "score": 9.155317
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1f5f7e3fc005c5fa093374500086cd85"></a>

### v16.0.0 [`0061ea7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061ea7c.md) FUN_0061ea7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / 18.095238000000002 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 8.571429 · 採用条件未達 · 順位差 8.571429 / -18.095238000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.14285714285714285
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.66666599999999,
        "reverse_margin": 18.095238000000002
      },
      "new": "005f90a4",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.14285714285714285
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 8.571429,
        "reverse_margin": -18.095238000000002
      },
      "new": "005f9078",
      "score": 8.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          1.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -80.0,
        "reverse_margin": -26.666667
      },
      "new": "005f90c8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b1f68a899747b269e4d91684409d842b"></a>

### v16.0.0 [`0061ea98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061ea98.md) FUN_0061ea98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9094.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 66.0 · 
- 2. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f90a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f90d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 66.0
      },
      "new": "005f9094",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90c8",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9078",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3875d893d747205b51c2704e1492fd62"></a>

### v16.0.0 [`0061eaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eaa4.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f90a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f90dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90dc.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f90d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90d8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9094.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`005f9078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9078.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90a0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f90dc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90d8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-47d5ee193ba2762de429604992de175e"></a>

### v16.0.0 [`0061eaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eaa8.md) FUN_0061eaa8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`008719c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719c0.md) · スコア 73.333333 · 採用条件未達 · 順位差 0.0 / 46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 46.66666599999999
      },
      "new": "008719c0",
      "score": 73.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.1111111111111111
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.333332999999996,
        "reverse_margin": -46.66666599999999
      },
      "new": "005f90c8",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -73.333333
      },
      "new": "005f90a4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-372e2ddfe8fd40b40ff493779d827545"></a>

### v16.0.0 [`0061eacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eacc.md) FUN_0061eacc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.0,
        "reverse_margin": 12.857143
      },
      "new": "005f90c8",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.857143,
        "reverse_margin": -12.857143
      },
      "new": "005f9138",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -73.333333,
        "reverse_margin": -50.0
      },
      "new": "005f90a4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5acc3a27d3d58b9ce1dc69691ba54efa"></a>

### v16.0.0 [`0061eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eadc.md) FUN_0061eadc

`competing_candidates` 

呼出元 1件 [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · 呼出先 0件 

- 1. [`005f90d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90d8.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`005f90dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90dc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f9154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9154.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f90a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90a4.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "005f90d8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90dc",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9154",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-baae9e99fa0bc4243cad1ad0226e694a"></a>

### v16.0.0 [`0061eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eae0.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f90dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90dc.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f9160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9160.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f90d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90d8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f90c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90c8.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9154.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90dc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f9160",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f90d8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b475d618da1e19a25b83f99519f46dba"></a>

### v16.0.0 [`0061eae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eae4.md) FUN_0061eae4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

- 1. [`005f90e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f90e0.md) · スコア 25.757576 · 採用条件未達 · 順位差 -13.333333000000003 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00601174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601174.md) · スコア 25.757576 · 採用条件未達 · 順位差 -18.787878999999997 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008edb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ed/008edb8c.md) · スコア 25.757576 · 採用条件未達 · 順位差 -34.242424 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f1624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1624.md) · スコア 24.090909 · 採用条件未達 · 順位差 -39.178321999999994 / -1.6666670000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007c99e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c99e0.md) · スコア 5.454545 · 採用条件未達 · 順位差 -54.090909999999994 / -20.303031 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007cab98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab98.md) · スコア 5.454545 · 採用条件未達 · 順位差 -36.363637 / -20.303031 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -25.757576 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -25.757576 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3181818181818182,
          0.3181818181818182
        ],
        "cfg_coverage": [
          0.4,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.333333000000003,
        "reverse_margin": 0.0
      },
      "new": "005f90e0",
      "score": 25.757576
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3181818181818182,
          0.3181818181818182
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.787878999999997,
        "reverse_margin": 0.0
      },
      "new": "00601174",
      "score": 25.757576
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5833333333333334,
          0.3181818181818182
        ],
        "cfg_coverage": [
          0.4,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.242424,
        "reverse_margin": 0.0
      },
      "new": "008edb8c",
      "score": 25.757576
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cf4fc496cb170e8a3f4b002c47f7542c"></a>

### v16.0.0 [`0061eb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb3c.md) FUN_0061eb3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0058b154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b154.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008a5a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a60.md) · スコア 42.857143 · 採用条件未達 · 順位差 42.857143 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.714286,
        "reverse_margin": 25.714286
      },
      "new": "0058b154",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.714286,
        "reverse_margin": -25.714286
      },
      "new": "005f9138",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7142857142857143,
          0.7142857142857143
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 42.857143,
        "reverse_margin": -37.142857
      },
      "new": "008a5a60",
      "score": 42.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e6fcb55253835caa45ff20b57d708b96"></a>

### v16.0.0 [`0061eb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb58.md) FUN_0061eb58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f9154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9154.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 66.0 · 
- 2. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f9160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9160.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9198.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 66.0
      },
      "new": "005f9154",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9188",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9138",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-399fa1bbadcf2fe6dc32b6559ca5cdb0"></a>

### v16.0.0 [`0061eb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb64.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f9160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9160.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f919c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f919c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9198.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9154.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`005f9138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9138.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9160",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f919c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9198",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3246f9e71150d3b90c7966708cf69fdf"></a>

### v16.0.0 [`0061eb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb68.md) FUN_0061eb68

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 60.0 · 採用条件未達 · 順位差 -13.333332999999996 / 26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00879a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a18.md) · スコア 33.333333 · 採用条件未達 · 順位差 33.333333 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.333332999999996,
        "reverse_margin": 26.666666999999997
      },
      "new": "005f9164",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 33.333333,
        "reverse_margin": -26.666666999999997
      },
      "new": "00879a18",
      "score": 33.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0,
          0.0
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -60.0
      },
      "new": "005f9188",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cdaf52a11132076f50b440a9c3b90fd5"></a>

### v16.0.0 [`0061eb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb8c.md) FUN_0061eb8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00879a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a3c.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 42.857143 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 42.857143
      },
      "new": "00879a3c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.5
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.142857,
        "reverse_margin": -42.857143
      },
      "new": "005f91a4",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.25
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.66666599999999,
        "reverse_margin": -53.333332999999996
      },
      "new": "005f9164",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fe7bd8c28745051d44ea085bad4c2e5e"></a>

### v16.0.0 [`0061eb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb9c.md) FUN_0061eb9c

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 0件 

- 1. [`005f9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9198.md) · スコア 54.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`005f91a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a0.md) · スコア 54.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`005f919c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f919c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f91c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91c0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 7. [`005f9164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9164.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f9198",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005f91a0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f919c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-47a1d056b05e6342b7d28e017b21304e"></a>

### v16.0.0 [`0061eba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eba0.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`005f919c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f919c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9198.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f91a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f9188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9188.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f91c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91c0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f919c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9198",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f91a0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c0dd74b0d6118cf34f27d7ee94e636f3"></a>

### v16.0.0 [`0061eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eba4.md) FUN_0061eba4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f9198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9198.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`005f91a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f919c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f919c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005f91c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91c0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "005f9198",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f91a0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f919c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f6b5f1b315617efd839b896188609095"></a>

### v16.0.0 [`0061eba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eba8.md) FUN_0061eba8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.142857,
        "reverse_margin": 54.285714
      },
      "new": "005f91a4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e9660042fb35fe3b320b6702b766f049"></a>

### v16.0.0 [`0061ebc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061ebc4.md) FUN_0061ebc4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f91c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91c0.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 67.2857 · 
- 2. [`005f91a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005f91a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 67.2857
      },
      "new": "005f91c0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f91a4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f91a0",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a8513ea16e7d0c0bde57e3ac94a6b71"></a>

### v16.0.0 [`00620ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md) FUN_00620ee4

`competing_candidates` 

呼出元 2件 [`00620cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620cf0.md) [`00620ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

- 1. [`005fb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fb/005fb4e0.md) · スコア 33.182028 · 採用条件未達 · 順位差 15.850532000000001 / 15.421934000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f93b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f93b0.md) · スコア 17.760094 · 採用条件未達 · 順位差 7.3415089999999985 / -15.421934000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) · スコア 13.214103 · 採用条件未達 · 順位差 5.170895999999999 / -19.967925 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00602628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602628.md) · スコア 12.521581 · 採用条件未達 · 順位差 -5.055882000000002 / -20.660447000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005f1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) · スコア 10.61617 · 採用条件未達 · 順位差 -27.545475 / -22.565858000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f4a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f4a84.md) · スコア 10.354905 · 採用条件未達 · 順位差 -5.420864 / -22.827123 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`009428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/009428a4.md) · スコア 9.48154 · 採用条件未達 · 順位差 2.0491420000000007 / -23.700488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00946864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00946/00946864.md) · スコア 8.716216 · 採用条件未達 · 順位差 0.9765869999999994 / -24.465812000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5167173252279635,
          0.5167173252279635
        ],
        "cfg_coverage": [
          0.10894941634241245,
          0.112
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.850532000000001,
        "reverse_margin": 15.421934000000004
      },
      "new": "005fb4e0",
      "score": 33.182028
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2564885496183206,
          0.2553191489361702
        ],
        "cfg_coverage": [
          0.1220472440944882,
          0.124
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 7.3415089999999985,
        "reverse_margin": -15.421934000000004
      },
      "new": "005f93b0",
      "score": 17.760094
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20766773162939298,
          0.19756838905775076
        ],
        "cfg_coverage": [
          0.09444444444444444,
          0.068
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 5.170895999999999,
        "reverse_margin": -19.967925
      },
      "new": "007525f0",
      "score": 13.214103
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

