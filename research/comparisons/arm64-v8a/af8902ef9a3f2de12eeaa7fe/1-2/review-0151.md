# v15.7.4 → v16.0.0 · 追加調査 (151)

[一覧の目次](README.md)

<a id="review-672c1ca157a0f1dc6bb3de9676160440"></a>

### v16.0.0 [`00933940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933940.md) FUN_00933940

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff08c.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff070.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`008fef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fef54.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff098.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ff08c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0c0",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff070",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e8f40b32261608eaa6ea3a6086bf5f9b"></a>

### v16.0.0 [`0093394c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093394c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff098.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`008ff0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff08c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff070.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "008ff098",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0d0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0c0",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a0298c905e7a50ac774c9cd14ab7743a"></a>

### v16.0.0 [`00933950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933950.md) FUN_00933950

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 60.0 · 採用条件未達 · 順位差 33.333332999999996 / 33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff070.md) · スコア 26.666667 · 採用条件未達 · 順位差 -27.619047 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 26.666667 · 採用条件未達 · 順位差 -23.333333 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 33.333332999999996,
        "reverse_margin": 33.333332999999996
      },
      "new": "008ff09c",
      "score": 60.0
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
        "margin": -27.619047,
        "reverse_margin": -33.333332999999996
      },
      "new": "008ff070",
      "score": 26.666667
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
        "margin": -23.333333,
        "reverse_margin": -33.333332999999996
      },
      "new": "008ff0c0",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-72a46dae4f280bdef38a28fb3ec775b7"></a>

### v16.0.0 [`00933974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933974.md) FUN_00933974

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 50.0 · 採用条件未達 · 順位差 23.333333 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 23.333333,
        "reverse_margin": 23.333333
      },
      "new": "008ff0c0",
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
        "margin": -33.333332999999996,
        "reverse_margin": -23.333333
      },
      "new": "008ff09c",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4eee450c269a15d4d8c1d9019e470324"></a>

### v16.0.0 [`00933984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933984.md) FUN_00933984

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ff0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d0.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ff098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff098.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ff0d0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff098",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0d4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6bf36983b96a26b7230c4996b94d0312"></a>

### v16.0.0 [`00933988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933988.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d4.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`008ff0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0c0.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff09c.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "008ff0d4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0d0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0c0",
      "score": 1.9375
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-383fe380eddca2cc8b2bb32ce52cbbf3"></a>

### v16.0.0 [`0093398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093398c.md) FUN_0093398c

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853fa8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

- 1. [`008fef58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fef58.md) · スコア 55.142857 · 採用条件未達 · 順位差 5.648352000000003 / 5.142856999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008fdba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdba8.md) · スコア 50.0 · 採用条件未達 · 順位差 -11.052632000000003 / -5.142856999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008fbf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbf1c.md) · スコア 49.494505 · 採用条件未達 · 順位差 -5.582418000000004 / -5.648352000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008fc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fc1f0.md) · スコア 42.813187 · 採用条件未達 · 順位差 -15.956043999999999 / -12.32967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008ff0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d8.md) · スコア 42.813187 · 採用条件未達 · 順位差 -15.956043999999999 / -12.32967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a6d258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d258.md) · スコア 17.142857 · 採用条件未達 · 順位差 -27.619048 / -38.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0060b124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b124.md) · スコア 15.0 · 採用条件未達 · 順位差 -13.355263 / -40.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0062fd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fd5c.md) · スコア 12.857143 · 採用条件未達 · 順位差 -26.310575 / -42.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5857142857142857,
          0.5857142857142857
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.648352000000003,
        "reverse_margin": 5.142856999999999
      },
      "new": "008fef58",
      "score": 55.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5428571428571428
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.052632000000003,
        "reverse_margin": -5.142856999999999
      },
      "new": "008fdba8",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5846153846153846,
          0.5428571428571428
        ],
        "cfg_coverage": [
          0.8461538461538461,
          0.9166666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.582418000000004,
        "reverse_margin": -5.648352000000003
      },
      "new": "008fbf1c",
      "score": 49.494505
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c3312bf32d620f37c5931ca297ff1d44"></a>

### v16.0.0 [`00933aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933aa4.md) FUN_00933aa4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff070.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff070",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff1dc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f67628610a4b9dcf751c89b6dcf0b2ad"></a>

### v16.0.0 [`00933ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ac0.md) FUN_00933ac0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1f8.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 67.2857 · 
- 2. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff204.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 0.8571 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 67.2857
      },
      "new": "008ff1f8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff1dc",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff0d4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-202fb3fb41cb8ea9295e4d157c8410fc"></a>

### v16.0.0 [`00933acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933acc.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff204.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 71.6667 · 
- 2. [`008ff1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1f8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 71.6667
      },
      "new": "008ff204",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff1f8",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff240",
      "score": 0.9792
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-70aec01ab35139ea13c5b562569ae5a8"></a>

### v16.0.0 [`00933ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ad0.md) FUN_00933ad0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00a3c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c9f4.md) · スコア 73.333333 · 採用条件未達 · 順位差 73.333333 / 44.761904 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 28.571429 · 採用条件未達 · 順位差 4.285715 / -44.761904 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 26.666667 · 採用条件未達 · 順位差 -27.619047 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 26.666667 · 採用条件未達 · 順位差 -13.333333 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 73.333333,
        "reverse_margin": 44.761904
      },
      "new": "00a3c9f4",
      "score": 73.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.2222222222222222
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
        "margin": 4.285715,
        "reverse_margin": -44.761904
      },
      "new": "008ff208",
      "score": 28.571429
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
        "margin": -27.619047,
        "reverse_margin": -46.66666599999999
      },
      "new": "008ff1dc",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9b9ada25a900c13b49d6e39e059ffc8a"></a>

### v16.0.0 [`00933af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933af4.md) FUN_00933af4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a3ca18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca18.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 40.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 40.0 · 採用条件未達 · 順位差 2.8571430000000007 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 24.285714 · 採用条件未達 · 順位差 -4.285715 / -55.714286 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 40.0
      },
      "new": "00a3ca18",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
        "margin": 2.8571430000000007,
        "reverse_margin": -40.0
      },
      "new": "008ff240",
      "score": 40.0
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
      "new": "008ff1dc",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f8d71622541f36bcbf15949c56c9bade"></a>

### v16.0.0 [`00933b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933b04.md) FUN_00933b04

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ff258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff258.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ff204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff204.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff25c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1f8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 0.2857 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ff258",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff204",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff25c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-73e7f1cbb4b5bce13e3c6613eb05a7e4"></a>

### v16.0.0 [`00933b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933b08.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff204.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff25c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff208.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff204",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff25c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff258",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-23e4aac680b85786a04807a73955115d"></a>

### v16.0.0 [`00933b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933b0c.md) FUN_00933b0c

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md)

- 1. [`008fc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fc1f0.md) · スコア 58.769231 · 採用条件未達 · 順位差 5.5384619999999956 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff0d8.md) · スコア 58.769231 · 採用条件未達 · 順位差 5.5384619999999956 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`008fbf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbf1c.md) · スコア 52.307692 · 採用条件未達 · 順位差 -2.7692309999999978 / -6.461538999999995 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008fdba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdba8.md) · スコア 48.502024 · 採用条件未達 · 順位差 -12.550608000000004 / -10.267206999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008fef58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fef58.md) · スコア 41.956044 · 採用条件未達 · 順位差 -13.186813 / -16.813187 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a6d258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d258.md) · スコア 19.384615 · 採用条件未達 · 順位差 -25.37729 / -39.384615999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0060b124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b124.md) · スコア 15.789474 · 採用条件未達 · 順位差 -12.565789 / -42.979757 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00610c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c68.md) · スコア 13.846154 · 採用条件未達 · 順位差 -17.487178999999998 / -44.923077 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6461538461538462,
          0.6461538461538462
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.5384619999999956,
        "reverse_margin": 0.0
      },
      "new": "008fc1f0",
      "score": 58.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6461538461538462,
          0.6461538461538462
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.5384619999999956,
        "reverse_margin": 0.0
      },
      "new": "008ff0d8",
      "score": 58.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5384615384615384,
          0.5384615384615384
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.7692309999999978,
        "reverse_margin": -6.461538999999995
      },
      "new": "008fbf1c",
      "score": 52.307692
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-08a89f4611a8a75e2f335c74e8b1050c"></a>

### v16.0.0 [`00933c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c10.md) FUN_00933c10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff1dc.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff240.md) · スコア 37.142857 · 採用条件未達 · 順位差 -2.8571430000000007 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff1dc",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff304",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
        "margin": -2.8571430000000007,
        "reverse_margin": -17.142857
      },
      "new": "008ff240",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8a5c68eca1476a2c2cf76918b22b2b9c"></a>

### v16.0.0 [`00933c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c2c.md) FUN_00933c2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff320.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 67.2857 · 
- 2. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff258.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff25c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff32c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 67.2857
      },
      "new": "008ff320",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff304",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff258",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-63024b1e8b54ed638329cc1521296a68"></a>

### v16.0.0 [`00933c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c38.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff25c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff32c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff320.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff25c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff32c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff320",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aca354ea6d52bc01ace0b0e526a38efe"></a>

### v16.0.0 [`00933c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c3c.md) FUN_00933c3c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 67.142857 · 採用条件未達 · 順位差 42.85714300000001 / 2.1428570000000065 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aad2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad2d0.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / -2.1428570000000065 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 24.285714 · 採用条件未達 · 順位差 -30.0 / -42.85714300000001 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -67.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7857142857142857,
          0.7857142857142857
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
        "margin": 42.85714300000001,
        "reverse_margin": 2.1428570000000065
      },
      "new": "008ff330",
      "score": 67.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
          0.8571428571428571
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 65.0,
        "reverse_margin": -2.1428570000000065
      },
      "new": "00aad2d0",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07142857142857142
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
        "margin": -30.0,
        "reverse_margin": -42.85714300000001
      },
      "new": "008ff304",
      "score": 24.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0a1939e0f5e4c4122df044a4a92d6bd5"></a>

### v16.0.0 [`00933c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c74.md) FUN_00933c74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / 12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 24.285714 · 採用条件未達 · 順位差 -42.85714300000001 / -12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.3333333333333333
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
        "reverse_margin": 12.857143
      },
      "new": "008ff304",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07142857142857142,
          0.16666666666666666
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
        "margin": -42.85714300000001,
        "reverse_margin": -12.857143
      },
      "new": "008ff330",
      "score": 24.285714
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
        "reverse_margin": -37.142857
      },
      "new": "008ff368",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b44f43e8c327ca800b8127651afc6acf"></a>

### v16.0.0 [`00933c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c8c.md) FUN_00933c8c

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ff380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff380.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ff32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff32c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff384.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff320.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 0.2857 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ff380",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff32c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff384",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b8ea83dc7d224e73066903b638c1fcf1"></a>

### v16.0.0 [`00933c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c90.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff32c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff384.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff380.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff32c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff384",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff380",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-af8f67c0d8b0a051a139ad66091aa3c3"></a>

### v16.0.0 [`00933c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c94.md) FUN_00933c94

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d088.md) [`0047d0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d0a0.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

- 1. [`008fe98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fe98c.md) · スコア 67.365854 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff260.md) · スコア 67.365854 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`008feab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008feab4.md) · スコア 62.439024 · 採用条件未達 · 順位差 0.0 / -4.926829999999995 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`008ff388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff388.md) · スコア 44.01084 · 採用条件未達 · 順位差 0.0 / -23.355013999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) · スコア 0.0 · 採用条件未達 · 順位差 -4.772727 / -67.365854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.142857 / -67.365854 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7560975609756098,
          0.7560975609756098
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008fe98c",
      "score": 67.365854
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7560975609756098,
          0.7560975609756098
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff260",
      "score": 67.365854
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7073170731707317,
          0.7073170731707317
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -4.926829999999995
      },
      "new": "008feab4",
      "score": 62.439024
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3774cb83091d6ec3e186c6f04c9215c4"></a>

### v16.0.0 [`00933d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d38.md) FUN_00933d38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff304.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ff330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff330.md) · スコア 24.285714 · 採用条件未達 · 順位差 -42.85714300000001 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff304",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff42c",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07142857142857142,
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
        "margin": -42.85714300000001,
        "reverse_margin": -30.0
      },
      "new": "008ff330",
      "score": 24.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0ed6547f83f99726f5368cd1c10d49be"></a>

### v16.0.0 [`00933d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d54.md) FUN_00933d54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff448.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 67.0 · 
- 2. [`008ff368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff368.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff380.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff384.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff454.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 67.0
      },
      "new": "008ff448",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff368",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff42c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-72af2b65f24b19336ccd31cfcf40565f"></a>

### v16.0.0 [`00933d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d60.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff384.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff454.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff380.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff448.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff384",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff454",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff380",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1accb7ed749b1f5fb3704f494c1d7a03"></a>

### v16.0.0 [`00933d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d64.md) FUN_00933d64

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 54.285714 · 採用条件未達 · 順位差 29.670329 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 24.285714 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 24.285714 · 採用条件未達 · 順位差 -15.714286000000001 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6153846153846154,
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
        "margin": 29.670329,
        "reverse_margin": 30.0
      },
      "new": "008ff458",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07142857142857142
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
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "008ff42c",
      "score": 24.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.07142857142857142
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
        "margin": -15.714286000000001,
        "reverse_margin": -30.0
      },
      "new": "008ff48c",
      "score": 24.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-73c9a1eca2639f2180f838770b40b70f"></a>

### v16.0.0 [`00933d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d9c.md) FUN_00933d9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 40.0 · 採用条件未達 · 順位差 2.8571430000000007 / 2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -15.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
          0.3333333333333333
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
        "reverse_margin": 2.8571430000000007
      },
      "new": "008ff48c",
      "score": 40.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.3333333333333333
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
        "reverse_margin": -2.8571430000000007
      },
      "new": "008ff42c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.16666666666666666
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
        "margin": -29.670329,
        "reverse_margin": -15.384615
      },
      "new": "008ff458",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f274fbce112b290389a92be9d789bbef"></a>

### v16.0.0 [`00933db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933db4.md) FUN_00933db4

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a0.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ff454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff454.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff448.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ff4a0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff454",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff448",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d22fc33f5ae4a77a3a91ea633c91ba4b"></a>

### v16.0.0 [`00933db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933db8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff454.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff448.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff454",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff4a4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff4a0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-06b67ba8864712ccf5cbab3ebfafbc5e"></a>

### v16.0.0 [`00933dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933dbc.md) FUN_00933dbc

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d090.md) [`0047d0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d0dc.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

- 1. [`008fe98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fe98c.md) · スコア 62.439024 · 採用条件未達 · 順位差 -4.926829999999995 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008feab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008feab4.md) · スコア 62.439024 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ff260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff260.md) · スコア 62.439024 · 採用条件未達 · 順位差 -4.926829999999995 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`008ff388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff388.md) · スコア 44.01084 · 採用条件未達 · 順位差 0.0 / -18.428184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00576d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d9c.md) · スコア 0.0 · 採用条件未達 · 順位差 -4.772727 / -62.439024 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -62.439024 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7073170731707317,
          0.7073170731707317
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.926829999999995,
        "reverse_margin": 0.0
      },
      "new": "008fe98c",
      "score": 62.439024
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7073170731707317,
          0.7073170731707317
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008feab4",
      "score": 62.439024
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7073170731707317,
          0.7073170731707317
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.926829999999995,
        "reverse_margin": 0.0
      },
      "new": "008ff260",
      "score": 62.439024
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3a81cdf0acfd9b5df9b65359361eee4a"></a>

### v16.0.0 [`00933e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e60.md) FUN_00933e60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff42c.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -2.8571430000000007 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff458.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff42c",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff9b8",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
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
        "margin": -2.8571430000000007,
        "reverse_margin": -17.142857
      },
      "new": "008ff48c",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-42969c5376aac193e457e55563455dec"></a>

### v16.0.0 [`00933e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e7c.md) FUN_00933e7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ff9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9d4.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 66.6 · 
- 2. [`008ff48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff48c.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 66.6
      },
      "new": "008ff9d4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff48c",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff9b8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6d5b32a5b21a53e7f68033211d7fa66f"></a>

### v16.0.0 [`00933e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e88.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ff9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e0.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff4a4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ff9e0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff4a0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6c6410b2a9a8eac2ec08ea49e302b966"></a>

### v16.0.0 [`00933e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e8c.md) FUN_00933e8c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00a3cc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cc98.md) · スコア 75.384615 · 採用条件未達 · 順位差 75.384615 / 50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 23.076923 · 採用条件未達 · 順位差 23.076923 / -52.307691999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
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
        "margin": 75.384615,
        "reverse_margin": 50.76922999999999
      },
      "new": "00a3cc98",
      "score": 75.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
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
        "margin": -29.670329,
        "reverse_margin": -50.76922999999999
      },
      "new": "008ff9b8",
      "score": 24.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38461538461538464,
          0.38461538461538464
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
        "margin": 23.076923,
        "reverse_margin": -52.307691999999996
      },
      "new": "008ff9e4",
      "score": 23.076923
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a95d55e565e5b3f38d2b5c9279d754cc"></a>

### v16.0.0 [`00933ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ec0.md) FUN_00933ec0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a3cccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cccc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 24.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 56.0 · 採用条件未達 · 順位差 18.857143 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 0.0 · 採用条件未達 · 順位差 -23.076923 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 24.0
      },
      "new": "00a3cccc",
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
        "margin": 18.857143,
        "reverse_margin": -24.0
      },
      "new": "008ffa18",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.4
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
      "new": "008ff9b8",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2a8d58394d9c3bbaeb0ce8f8034d5abd"></a>

### v16.0.0 [`00933ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ed4.md) FUN_00933ed4

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ffa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa2c.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ff9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ff9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ffa2c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff9e0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff9d4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d26bea4d126bf6d921e274179cad47d3"></a>

### v16.0.0 [`00933ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ed8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ff9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa30.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ffa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa2c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ff9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ff9e0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ffa30",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffa2c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-60082eade2af5aef35370714dde82d2c"></a>

### v16.0.0 [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) FUN_00933edc

`competing_candidates` 

呼出元 0件  · 呼出先 23件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0067687c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067687c.md)

- 1. [`008ff4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff4a8.md) · スコア 30.753247 · 採用条件未達 · 順位差 22.086125000000003 / 22.033475000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008fd0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fd0a0.md) · スコア 8.719772 · 採用条件未達 · 順位差 -53.841804 / -22.033475000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008fd65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fd65c.md) · スコア 8.719772 · 採用条件未達 · 順位差 -42.994514 / -22.033475000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008fe34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fe34c.md) · スコア 8.29872 · 採用条件未達 · 順位差 -20.40993 / -22.454527000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008fdd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdd40.md) · スコア 4.179232 · 採用条件未達 · 順位差 -28.833212000000003 / -26.574015000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005b6bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md) · スコア 3.667141 · 採用条件未達 · 順位差 -4.116334 / -27.086106 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a3a38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a38c.md) · スコア 3.357026 · 採用条件未達 · 順位差 -42.688172 / -27.396221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0087a5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5c0.md) · スコア 2.947368 · 採用条件未達 · 順位差 -1.334912 / -27.805879 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
          0.4
        ],
        "cfg_coverage": [
          0.33766233766233766,
          0.35135135135135137
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 22.086125000000003,
        "reverse_margin": 22.033475000000003
      },
      "new": "008ff4a8",
      "score": 30.753247
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1724137931034483,
          0.12280701754385964
        ],
        "cfg_coverage": [
          0.09803921568627451,
          0.06756756756756757
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.841804,
        "reverse_margin": -22.033475000000003
      },
      "new": "008fd0a0",
      "score": 8.719772
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.12280701754385964
        ],
        "cfg_coverage": [
          0.10416666666666667,
          0.06756756756756757
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.994514,
        "reverse_margin": -22.033475000000003
      },
      "new": "008fd65c",
      "score": 8.719772
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c6e267bbf79068fa263cf3d215d14b41"></a>

### v16.0.0 [`009343ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009343ec.md) FUN_009343ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773878.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008ff9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9b8.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 37.142857 · 採用条件未達 · 順位差 -18.857143 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 0.0 · 採用条件未達 · 順位差 -23.076923 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00773878",
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
        "margin": 0.0,
        "reverse_margin": -25.714286
      },
      "new": "008ff9b8",
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
        "margin": 0.0,
        "reverse_margin": -25.714286
      },
      "new": "008ffafc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6617608f8030fb295ac04c29441ffb6d"></a>

### v16.0.0 [`00934408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934408.md) FUN_00934408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa2c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa30.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ff9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ff9e4.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffa18",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffafc",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffa2c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a31d338b06a06d55adf1b65c617f423"></a>

### v16.0.0 [`00934414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934414.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa30.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa2c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb18.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa18.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffa30",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffa2c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb18",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-dc94ca9d9d05caaf53d2321e8b8bef4d"></a>

### v16.0.0 [`00934418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934418.md) FUN_00934418

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`005910a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910a0.md) · スコア 55.384615 · 採用条件未達 · 順位差 55.384615 / 30.769229999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -30.769229999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
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
        "margin": 55.384615,
        "reverse_margin": 30.769229999999997
      },
      "new": "005910a0",
      "score": 55.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
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
        "margin": -29.670329,
        "reverse_margin": -30.769229999999997
      },
      "new": "008ffafc",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cae32f7c91fcb812ef90de147b270e5a"></a>

### v16.0.0 [`0093444c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093444c.md) FUN_0093444c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005910d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910d4.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 42.857143 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 42.857143
      },
      "new": "005910d4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.4
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
      "new": "008ffafc",
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
        "margin": 0.0,
        "reverse_margin": -80.0
      },
      "new": "008ffb28",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5bcf72d627ca9aed93a316b44aaf0022"></a>

### v16.0.0 [`00934460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934460.md) FUN_00934460

`competing_candidates` 

呼出元 1件 [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) · 呼出先 0件 

- 1. [`008ffb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb24.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb18.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.2857 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb24",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb18",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb60",
      "score": 0.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8348a83d69a6a7b6958aa47ea5009402"></a>

### v16.0.0 [`00934464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934464.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb24.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`008ffb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb78.md) · スコア 4.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`008ffb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb18.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "008ffb24",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ffb78",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb18",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-10f2467282fbc79e58df60d203a7f1e0"></a>

### v16.0.0 [`00934468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md) FUN_00934468

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

- 1. [`008ffa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffa34.md) · スコア 27.7 · 採用条件未達 · 順位差 15.649999999999999 / 20.007692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f83bc.md) · スコア 7.692308 · 採用条件未達 · 順位差 -32.307692 / -20.007692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007c75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c75e8.md) · スコア 7.2 · 採用条件未達 · 順位差 -2.442856999999999 / -20.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00600efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600efc.md) · スコア 2.5 · 採用条件未達 · 順位差 -32.954545 / -25.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007c4dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4dd8.md) · スコア 0.0 · 採用条件未達 · 順位差 -16.025974 / -27.7 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -27.7 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42,
          0.42
        ],
        "cfg_coverage": [
          0.125,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.649999999999999,
        "reverse_margin": 20.007692
      },
      "new": "008ffa34",
      "score": 27.7
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1282051282051282,
          0.2
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
        "margin": -32.307692,
        "reverse_margin": -20.007692
      },
      "new": "005f83bc",
      "score": 7.692308
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17142857142857143,
          0.12
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
        "margin": -2.442856999999999,
        "reverse_margin": -20.5
      },
      "new": "007c75e8",
      "score": 7.2
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d472fd40738a1c9219fa598ffd3a6ac1"></a>

### v16.0.0 [`00934530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934530.md) FUN_00934530

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffafc.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 37.142857 · 採用条件未達 · 順位差 12.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 17.142857
      },
      "new": "008ffafc",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
        "margin": 12.857143,
        "reverse_margin": -17.142857
      },
      "new": "008ffb60",
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
        "margin": 0.0,
        "reverse_margin": -54.285714
      },
      "new": "008ffb28",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-616295583b81375ac120e201ce5c6174"></a>

### v16.0.0 [`0093454c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093454c.md) FUN_0093454c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb24.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb78.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb7c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.8571 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb60",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc6c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb24",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f2f8d07f613c8906416c2fcd7aa7e72c"></a>

### v16.0.0 [`00934558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934558.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb7c.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`008ffb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb78.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc88.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ffb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb28.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "008ffb7c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb78",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc88",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f58706c20b2f35cde1f7d23c29b5b426"></a>

### v16.0.0 [`0093455c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093455c.md) FUN_0093455c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`008ffb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb60.md) · スコア 24.285714 · 採用条件未達 · 順位差 -12.857143 / 24.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -24.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.07142857142857142
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
        "margin": -12.857143,
        "reverse_margin": 24.285714
      },
      "new": "008ffb60",
      "score": 24.285714
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
        "reverse_margin": -24.285714
      },
      "new": "008ffc6c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-76eaec63785ec39925e193df21b14ef2"></a>

### v16.0.0 [`00934594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934594.md) FUN_00934594

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "008ffc6c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ba9f36e05dd961930ee7e05ae928fbd3"></a>

### v16.0.0 [`009345ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345ac.md) FUN_009345ac

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ffb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc88.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffb7c",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc94",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc88",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-afafdc95dc0c13fcc3dbf771af5870f5"></a>

### v16.0.0 [`009345b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b0.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc94.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 71.6667 · 
- 2. [`008ffc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc88.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 71.6667
      },
      "new": "008ffc94",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc88",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc6c",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c77f290dcccec22b2ef469d6f5122488"></a>

### v16.0.0 [`009345b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b4.md) FUN_009345b4

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e70.md)

- 1. [`008ffb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffb80.md) · スコア 48.677966 · 採用条件未達 · 順位差 19.322034 / 15.655366999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a3b254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b254.md) · スコア 33.022599 · 採用条件未達 · 順位差 -26.620258 / -15.655366999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0060afa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060afa4.md) · スコア 29.971751 · 採用条件未達 · 順位差 -19.937339999999995 / -18.706214999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00aad9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md) · スコア 29.971751 · 採用条件未達 · 順位差 -8.328644 / -18.706214999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00aadb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md) · スコア 29.971751 · 採用条件未達 · 順位差 -12.437339999999995 / -18.706214999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008fc088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fc088.md) · スコア 28.541667 · 採用条件未達 · 順位差 -13.958333 / -20.136298999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00800394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800394.md) · スコア 26.261261 · 採用条件未達 · 順位差 -4.77824 / -22.416704999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006ae45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae45c.md) · スコア 25.652174 · 採用条件未達 · 順位差 -11.304348000000001 / -23.025792 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6779661016949152,
          0.6779661016949152
        ],
        "cfg_coverage": [
          0.4,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.322034,
        "reverse_margin": 15.655366999999998
      },
      "new": "008ffb80",
      "score": 48.677966
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.375,
          0.3559322033898305
        ],
        "cfg_coverage": [
          0.7777777777777778,
          0.5833333333333334
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.620258,
        "reverse_margin": -15.655366999999998
      },
      "new": "00a3b254",
      "score": 33.022599
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45,
          0.3050847457627119
        ],
        "cfg_coverage": [
          0.7,
          0.5833333333333334
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.937339999999995,
        "reverse_margin": -18.706214999999997
      },
      "new": "0060afa4",
      "score": 29.971751
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1e9b0f40f205b4ad2d145b2f96fd507f"></a>

### v16.0.0 [`009346a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346a0.md) FUN_009346a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc6c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "008ffc6c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3aaafe709b112fa51ff144fa7a5f427a"></a>

### v16.0.0 [`009346bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346bc.md) FUN_009346bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ffc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc94.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 2. [`008ffcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcf8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ffcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcfc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffc94",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffcf8",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffcfc",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-774cc37de1252c847b5d5f2fb39baa06"></a>

### v16.0.0 [`009346c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346c8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcfc.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 68.9824 · 
- 2. [`008ffcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcf8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 68.9824
      },
      "new": "008ffcfc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffcf8",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0090010c",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d4421629adfc5e2cded36fa4963b6a3b"></a>

### v16.0.0 [`009346cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346cc.md) FUN_009346cc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00638d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638d6c.md) · スコア 68.75 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006392c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006392c4.md) · スコア 68.75 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00639404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639404.md) · スコア 68.75 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`007c8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8038.md) · スコア 68.75 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`007c9ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9ee4.md) · スコア 68.75 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`0068928c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/0068928c.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / -3.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005f28e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f28e8.md) · スコア 33.75 · 採用条件未達 · 順位差 -16.25 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 23.75 · 採用条件未達 · 順位差 -30.535714 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8125,
          0.8125
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
        "reverse_margin": 0.0
      },
      "new": "00638d6c",
      "score": 68.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8125,
          0.8125
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
        "reverse_margin": 0.0
      },
      "new": "006392c4",
      "score": 68.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8125,
          0.8125
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
        "reverse_margin": 0.0
      },
      "new": "00639404",
      "score": 68.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b31c8141c4ad9d21c597827d08e4d98d"></a>

### v16.0.0 [`0093470c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093470c.md) FUN_0093470c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 35.0 · 採用条件未達 · 順位差 -19.285714 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -19.285714,
        "reverse_margin": 35.0
      },
      "new": "0090010c",
      "score": 35.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e6c91b4210c087604d795ef8d79d8cf8"></a>

### v16.0.0 [`0093472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093472c.md) FUN_0093472c

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`008ffcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcf8.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008ffcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcfc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00900134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00900128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900128.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ffcf8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffcfc",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900134",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5c65880c995667df40b86ac2daf7769d"></a>

### v16.0.0 [`00934730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934730.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`008ffcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffcfc.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`00900134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900134.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`00900128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900128.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 6. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "008ffcfc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00900134",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900128",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c41b2463f83805c2bd2229f335a16bf7"></a>

### v16.0.0 [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) FUN_00934734

`competing_candidates` 

呼出元 0件  · 呼出先 18件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`008ffd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffd00.md) · スコア 63.348018 · 採用条件未達 · 順位差 51.452870000000004 / 52.275155000000005 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00a6b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b95c.md) · スコア 11.072863 · 採用条件未達 · 順位差 6.263703 / -52.275155000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a6bdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6bdd0.md) · スコア 9.470428 · 採用条件未達 · 順位差 0.4392680000000002 / -53.877590000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007f6a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6a14.md) · スコア 9.453608 · 採用条件未達 · 順位差 2.4261169999999987 / -53.89441000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006a7abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7abc.md) · スコア 7.884525 · 採用条件未達 · 順位差 -2.980696 / -55.463493 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007f64ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f64ac.md) · スコア 6.562939 · 採用条件未達 · 順位差 1.7781120000000001 / -56.785079 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) · スコア 5.550661 · 採用条件未達 · 順位差 -3.55138 / -57.797357000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00595ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md) · スコア 5.550661 · 採用条件未達 · 順位差 -3.55138 / -57.797357000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7224669603524229,
          0.7224669603524229
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 51.452870000000004,
        "reverse_margin": 52.275155000000005
      },
      "new": "008ffd00",
      "score": 63.348018
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1686746987951807,
          0.18502202643171806
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.06382978723404255
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.263703,
        "reverse_margin": -52.275155000000005
      },
      "new": "00a6b95c",
      "score": 11.072863
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18902439024390244,
          0.13656387665198239
        ],
        "cfg_coverage": [
          0.09090909090909091,
          0.06382978723404255
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.4392680000000002,
        "reverse_margin": -53.877590000000005
      },
      "new": "00a6bdd0",
      "score": 9.470428
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fbb198747d313f7938ee31815cfd0929"></a>

### v16.0.0 [`00934b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b40.md) FUN_00934b40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0090010c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090010c.md) · スコア 54.285714 · 採用条件未達 · 順位差 19.285714 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -18.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.285714,
        "reverse_margin": 17.142857
      },
      "new": "0090010c",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
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
        "margin": -18.857143,
        "reverse_margin": -17.142857
      },
      "new": "0090016c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
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
        "margin": -41.538461,
        "reverse_margin": -29.670329
      },
      "new": "00900138",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8671fd70da4338dab595acce869be6e9"></a>

### v16.0.0 [`00934b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b5c.md) FUN_00934b5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900128.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 66.6 · 
- 2. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00900134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900134.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`00900180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900180.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900184.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 66.6
      },
      "new": "00900128",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0090016c",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900134",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3c26a31533e2c23d8462bd70352edf21"></a>

### v16.0.0 [`00934b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b68.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00900134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900134.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`00900184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900184.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`00900180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900180.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "00900134",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00900184",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900180",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6028f5d527b95def144178a63c1ff4c1"></a>

### v16.0.0 [`00934b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b6c.md) FUN_00934b6c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00900138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900138.md) · スコア 66.153846 · 採用条件未達 · 順位差 41.538461 / 41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / -41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7692307692307693,
          0.7692307692307693
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
        "margin": 41.538461,
        "reverse_margin": 41.538461
      },
      "new": "00900138",
      "score": 66.153846
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.07692307692307693
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
        "margin": -31.384615,
        "reverse_margin": -41.538461
      },
      "new": "0090016c",
      "score": 24.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
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
        "margin": -29.670329,
        "reverse_margin": -41.538461
      },
      "new": "0090027c",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ddd42dbd0c0fab1f30738843fedb07e8"></a>

### v16.0.0 [`00934ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ba0.md) FUN_00934ba0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0090016c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090016c.md) · スコア 56.0 · 採用条件未達 · 順位差 18.857143 / 18.857143 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -18.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "margin": 18.857143,
        "reverse_margin": 18.857143
      },
      "new": "0090016c",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.4
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
        "reverse_margin": -18.857143
      },
      "new": "0090027c",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c4237a566ffe9fbe6d98b1feb9064b71"></a>

### v16.0.0 [`00934bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bb4.md) FUN_00934bb4

`competing_candidates` 

呼出元 1件 [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) · 呼出先 0件 

- 1. [`00900180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900180.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`00900184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900184.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`009002a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00900298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900298.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00900180",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900184",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009002a4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5997029caac2b6ac827f50a600f66982"></a>

### v16.0.0 [`00934bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bb8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00900184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900184.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`009002a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`00900298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900298.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 5. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "00900184",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "009002a4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900298",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4c1789f9ae0df02ba87e02db076f788b"></a>

### v16.0.0 [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) FUN_00934bbc

`competing_candidates` 

呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00726f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md)

- 1. [`00900188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900188.md) · スコア 48.52459 · 採用条件未達 · 順位差 31.358314000000004 / 31.358314000000004 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f182c.md) · スコア 17.166276 · 採用条件未達 · 順位差 -45.944835 / -31.358314000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a8de24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8de24.md) · スコア 17.166276 · 採用条件未達 · 順位差 -28.926747000000002 / -31.358314000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0096d92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d92c.md) · スコア 17.071038 · 採用条件未達 · 順位差 -11.983225999999998 / -31.453552000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a8df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df4c.md) · スコア 13.337098 · 採用条件未達 · 順位差 -22.341063000000005 / -35.187492000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f8b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8b54.md) · スコア 10.28103 · 採用条件未達 · 順位差 -17.706775 / -38.24356 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a1e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e19c.md) · スコア 9.297424 · 採用条件未達 · 順位差 -26.584929000000002 / -39.227166000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a204dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a204dc.md) · スコア 9.297424 · 採用条件未達 · 順位差 -17.22664 / -39.227166000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47540983606557374,
          0.47540983606557374
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 31.358314000000004,
        "reverse_margin": 31.358314000000004
      },
      "new": "00900188",
      "score": 48.52459
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2962962962962963,
          0.26229508196721313
        ],
        "cfg_coverage": [
          0.125,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -45.944835,
        "reverse_margin": -31.358314000000004
      },
      "new": "005f182c",
      "score": 17.166276
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37209302325581395,
          0.26229508196721313
        ],
        "cfg_coverage": [
          0.1,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -28.926747000000002,
        "reverse_margin": -31.358314000000004
      },
      "new": "00a8de24",
      "score": 17.166276
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2df11fb405a83a77c3a9671a445ad08b"></a>

### v16.0.0 [`00934cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cb0.md) FUN_00934cb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0083b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b20c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 37.142857 · 採用条件未達 · 順位差 -12.857143 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 25.714286
      },
      "new": "0083b20c",
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
        "margin": 17.142857,
        "reverse_margin": -25.714286
      },
      "new": "0090027c",
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
        "margin": -12.857143,
        "reverse_margin": -42.857143
      },
      "new": "009002cc",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-364d5815c233c68ad8fedae1e808f1e5"></a>

### v16.0.0 [`00934ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ccc.md) FUN_00934ccc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900298.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 66.0 · 
- 2. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0090027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090027c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`009002a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`009002dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002dc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`009002e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002e0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00900298",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009002cc",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0090027c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6b41326f98f7ae48ca435a5912c330e7"></a>

### v16.0.0 [`00934cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cd8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`009002a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`009002e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002e0.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`009002dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002dc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900298.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "009002a4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "009002e0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009002dc",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b7c15bebc2ecc7682c5a225ccc00b410"></a>

### v16.0.0 [`00934cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cdc.md) FUN_00934cdc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00acd4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd4f8.md) · スコア 73.333333 · 採用条件未達 · 順位差 13.333332999999996 / 13.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 60.0 · 採用条件未達 · 順位差 33.333332999999996 / -13.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`0087213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/0087213c.md) · スコア 33.333333 · 採用条件未達 · 順位差 -39.99999999999999 / -39.99999999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 26.666667 · 採用条件未達 · 順位差 -23.333333 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 13.333332999999996,
        "reverse_margin": 13.333332999999996
      },
      "new": "00acd4f8",
      "score": 73.333333
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.333332999999996,
        "reverse_margin": -13.333332999999996
      },
      "new": "009002a8",
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
        "margin": -39.99999999999999,
        "reverse_margin": -39.99999999999999
      },
      "new": "0087213c",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-79020bf74c217acd85d5663f0cbcce89"></a>

### v16.0.0 [`00934d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d00.md) FUN_00934d00

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00872160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872160.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00acd51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd51c.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 50.0 · 採用条件未達 · 順位差 12.857143 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009002a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002a8.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -53.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "00872160",
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
      "new": "00acd51c",
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
        "margin": 12.857143,
        "reverse_margin": -30.0
      },
      "new": "009002cc",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cad9c80bf978ffe2db6c61e15a2ce38b"></a>

### v16.0.0 [`00934d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d10.md) FUN_00934d10

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 0件 

- 1. [`009002dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002dc.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`009002e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002e0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00900580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900580.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`009002cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002cc.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009002dc",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009002e0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900580",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-96e8ef181b54b51eb7d5ee85179f70e0"></a>

### v16.0.0 [`00934d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d14.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0092e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092e/0092e4d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`009002e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002e0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`0090058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090058c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`009002dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002dc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00900580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900580.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "009002e0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0090058c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009002dc",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-495297dab414e236ec3bd0e9f6aa5f1a"></a>

### v16.0.0 [`00934d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md) FUN_00934d18

`competing_candidates` 

呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0072755c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072755c.md) [`00727560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727560.md)

- 1. [`008febc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008febc0.md) · スコア 63.548387 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`009002e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009002e4.md) · スコア 63.548387 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`00758378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md) · スコア 16.162403 · 採用条件未達 · 順位差 -8.258806999999997 / -47.38598399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008c6b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6b20.md) · スコア 16.162403 · 採用条件未達 · 順位差 -12.635673999999998 / -47.38598399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00960d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00960/00960d40.md) · スコア 16.162403 · 採用条件未達 · 順位差 -26.778772999999997 / -47.38598399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00879b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md) · スコア 14.226919 · 採用条件未達 · 順位差 -13.248942999999999 / -49.321467999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0062fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fecc.md) · スコア 14.058383 · 採用条件未達 · 順位差 -16.518987 / -49.490004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008336f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008336f0.md) · スコア 12.802419 · 採用条件未達 · 順位差 -4.3435500000000005 / -50.745968 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7258064516129032,
          0.7258064516129032
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008febc0",
      "score": 63.548387
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7258064516129032,
          0.7258064516129032
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "009002e4",
      "score": 63.548387
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21359223300970873,
          0.1774193548387097
        ],
        "cfg_coverage": [
          0.32,
          0.27586206896551724
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -8.258806999999997,
        "reverse_margin": -47.38598399999999
      },
      "new": "00758378",
      "score": 16.162403
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c30d70d98f4404ada7134cd9f6ea9db8"></a>

### v16.0.0 [`00934f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934f98.md) FUN_00934f98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 37.142857 · 採用条件未達 · 順位差 -12.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -27.619047 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00900564",
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
        "margin": -12.857143,
        "reverse_margin": -17.142857
      },
      "new": "009005b4",
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
        "reverse_margin": -27.619047
      },
      "new": "00900590",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e53fc9e0c1b0c7967678bab39ea2bd41"></a>

### v16.0.0 [`00934fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fb4.md) FUN_00934fb4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900580.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 66.0 · 
- 2. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00900564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900564.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`0090058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090058c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`009005c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00900580",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009005b4",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900564",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ceabe4229f0f07872a44cf95daa308a8"></a>

### v16.0.0 [`00934fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fc0.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`0090058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090058c.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`009005c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c8.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 3. [`009005c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900580.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "0090058c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "009005c8",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009005c4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e7962f5ce07a0b06c311f4a189983d94"></a>

### v16.0.0 [`00934fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fc4.md) FUN_00934fc4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 60.0 · 採用条件未達 · 順位差 33.333332999999996 / 33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 26.666667 · 採用条件未達 · 順位差 -23.333333 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 33.333332999999996,
        "reverse_margin": 33.333332999999996
      },
      "new": "00900590",
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
        "margin": -23.333333,
        "reverse_margin": -33.333332999999996
      },
      "new": "009005b4",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0a55ade4b4d0111e78beb427da939c78"></a>

### v16.0.0 [`00934fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fe8.md) FUN_00934fe8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 50.0 · 採用条件未達 · 順位差 12.857143 / 12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 26.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 12.857143,
        "reverse_margin": 12.857143
      },
      "new": "009005b4",
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
        "margin": -17.142857,
        "reverse_margin": -12.857143
      },
      "new": "00900614",
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
        "margin": -33.333332999999996,
        "reverse_margin": -23.333333
      },
      "new": "00900590",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-04a28ea4224ef8dedf8eb8d5d4785c44"></a>

### v16.0.0 [`00934ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ff8.md) FUN_00934ff8

`competing_candidates` 

呼出元 1件 [`00934d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md) · 呼出先 0件 

- 1. [`009005c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c4.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`009005c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00900630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900630.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00900590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900590.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009005c4",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009005c8",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900630",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b4fefc73f4c6dcea65310580c953ee34"></a>

### v16.0.0 [`00934ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ffc.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00934d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`009005c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c8.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`0090063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090063c.md) · スコア 4.0226 · 採用条件未達 · 順位差 — / — · 
- 3. [`009005c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005c4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`009005b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005b4.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`00900630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900630.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "009005c8",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0090063c",
      "score": 4.0226
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009005c4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cd02b3e282c220fbd83ad6daaa71c2b3"></a>

### v16.0.0 [`00935000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935000.md) FUN_00935000

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

- 1. [`009005cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009005cc.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 70.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -61.632653 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8333333333333334,
          0.8333333333333334
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
        "reverse_margin": 70.0
      },
      "new": "009005cc",
      "score": 70.0
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
        "reverse_margin": -70.0
      },
      "new": "00900614",
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
        "margin": -61.632653,
        "reverse_margin": -70.0
      },
      "new": "009009cc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8f7e2ed2a6c4027d46732b72ab10a4c6"></a>

### v16.0.0 [`00935048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935048.md) FUN_00935048

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00900614",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f8d26a4c14f1f7fcd62ce7e9c978bbb6"></a>

### v16.0.0 [`00935064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935064.md) FUN_00935064

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00900630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900630.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 67.2857 · 
- 2. [`00900614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900614.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) · スコア 0.2449 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00900630",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00900614",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009009cc",
      "score": 0.2449
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8982c4c87339a16e2b2c6061a27280f8"></a>

### v16.0.0 [`00935070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935070.md) _INIT_184

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`0090063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/0090063c.md) · スコア 50.822034 · 採用条件未達 · 順位差 -7.478207999999995 / 5.300377000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0060b354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b354.md) · スコア 45.521657 · 採用条件未達 · 順位差 45.521657 / -5.300377000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -61.632653 / -50.822034 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.655367231638418,
          0.655367231638418
        ],
        "cfg_coverage": [
          0.5757575757575758,
          0.475
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.478207999999995,
        "reverse_margin": 5.300377000000005
      },
      "new": "0090063c",
      "score": 50.822034
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.632768361581921,
          0.632768361581921
        ],
        "cfg_coverage": [
          0.2777777777777778,
          0.375
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 45.521657,
        "reverse_margin": -5.300377000000005
      },
      "new": "0060b354",
      "score": 45.521657
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
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -61.632653,
        "reverse_margin": -50.822034
      },
      "new": "009009cc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1c2c729119ad02334972ba180d5d982e"></a>

### v16.0.0 [`00935400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935400.md) FUN_00935400

`competing_candidates` 

呼出元 1件 [`009b873c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md) · 呼出先 3件 [`00935514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md) [`00acb85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb85c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

- 1. [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) · スコア 61.632653 · 採用条件未達 · 順位差 46.938775 / 48.163264999999996 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004c177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c177c.md) · スコア 13.469388 · 採用条件未達 · 順位差 13.469388 / -48.163264999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008cb610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb610.md) · スコア 13.469388 · 採用条件未達 · 順位差 6.546311 / -48.163264999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009e1b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md) · スコア 13.469388 · 採用条件未達 · 順位差 6.546311 / -48.163264999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0085c1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c1c0.md) · スコア 12.413793 · 採用条件未達 · 順位差 0.0 / -49.21886 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007205e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007205e8.md) · スコア 11.37931 · 採用条件未達 · 順位差 11.37931 / -50.253343 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0052ad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ad78.md) · スコア 11.076923 · 採用条件未達 · 順位差 4.7307690000000004 / -50.55573 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007d8fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d8/007d8fa4.md) · スコア 10.285714 · 採用条件未達 · 順位差 5.7857140000000005 / -51.346939 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6938775510204082,
          0.6938775510204082
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 46.938775,
        "reverse_margin": 48.163264999999996
      },
      "new": "009009cc",
      "score": 61.632653
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3793103448275862,
          0.22448979591836735
        ],
        "cfg_coverage": [
          1.0,
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
        "margin": 13.469388,
        "reverse_margin": -48.163264999999996
      },
      "new": "004c177c",
      "score": 13.469388
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2391304347826087,
          0.22448979591836735
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
        "margin": 6.546311,
        "reverse_margin": -48.163264999999996
      },
      "new": "008cb610",
      "score": 13.469388
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dfbe65685d3ca411e80dd4046982ad97"></a>

### v16.0.0 [`00935d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d6c.md) FUN_00935d6c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)

- 1. [`00901338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901338.md) · スコア 35.0 · 採用条件未達 · 順位差 10.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00901348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901348.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.0,
        "reverse_margin": 35.0
      },
      "new": "00901338",
      "score": 35.0
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
        "margin": -65.0,
        "reverse_margin": -35.0
      },
      "new": "00901348",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3c7e9c491f475539d85cdc4d7ed20c1"></a>

### v16.0.0 [`00935d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d7c.md) FUN_00935d7c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00901338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901338.md) · スコア 25.0 · 採用条件未達 · 順位差 -10.0 / 5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00901348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901348.md) · スコア 20.0 · 採用条件未達 · 順位差 -45.0 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.08333333333333333
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
        "margin": -10.0,
        "reverse_margin": 5.0
      },
      "new": "00901338",
      "score": 25.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.3333333333333333
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
        "margin": -45.0,
        "reverse_margin": -5.0
      },
      "new": "00901348",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-14f570270def6378a339e7d5d6b25324"></a>

### v16.0.0 [`00937924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md) FUN_00937924

`competing_candidates` 

呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0071e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e92c.md) [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0080b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00902ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902ef0.md) · スコア 33.694841 · 採用条件未達 · 順位差 20.666875999999995 / 25.311861999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0075d03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d03c.md) · スコア 8.382979 · 採用条件未達 · 順位差 -21.996552 / -25.311861999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009a81ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a81ec.md) · スコア 7.850762 · 採用条件未達 · 順位差 0.24802899999999983 / -25.844078999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) · スコア 6.696881 · 採用条件未達 · 順位差 -34.992560000000005 / -26.997959999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0064f874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f874.md) · スコア 6.578927 · 採用条件未達 · 順位差 -4.809808 / -27.115913999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0080816c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/0080816c.md) · スコア 5.510638 · 採用条件未達 · 順位差 -0.48936199999999985 / -28.184202999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007e8868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8868.md) · スコア 5.375109 · 採用条件未達 · 順位差 -46.77195 / -28.319731999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006425d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md) · スコア 5.146313 · 採用条件未達 · 順位差 -33.934432 / -28.548527999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.44385026737967914,
          0.44148936170212766
        ],
        "cfg_coverage": [
          0.27941176470588236,
          0.2602739726027397
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 20.666875999999995,
        "reverse_margin": 25.311861999999998
      },
      "new": "00902ef0",
      "score": 33.694841
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.10638297872340426
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
        "margin": -21.996552,
        "reverse_margin": -25.311861999999998
      },
      "new": "0075d03c",
      "score": 8.382979
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08787878787878788,
          0.15425531914893617
        ],
        "cfg_coverage": [
          0.028901734104046242,
          0.0684931506849315
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.24802899999999983,
        "reverse_margin": -25.844078999999997
      },
      "new": "009a81ec",
      "score": 7.850762
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd1c6176a2f99fde1ca1518ee48af3e6"></a>

### v16.0.0 [`009385d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d0.md) FUN_009385d0

`competing_candidates` [`00903b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/00903b98.md)

呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00938364",
    "009385d8",
    "0090392c",
    "00903ba0"
  ],
  "initial_reason": ""
}
~~~

<a id="review-02e4096edce40c236f901c72fefb651b"></a>

### v16.0.0 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) FUN_0093b5d4

`competing_candidates` 

呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 63件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)

- 1. [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · スコア 13.095147 · 採用条件未達 · 順位差 4.869932 / 4.802062000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · スコア 8.293085 · 採用条件未達 · 順位差 -32.566657 / -4.802062000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008673f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00867/008673f0.md) · スコア 6.0 · 採用条件未達 · 順位差 -5.286822000000001 / -7.095147000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00687ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687ba8.md) · スコア 4.33557 · 採用条件未達 · 順位差 -25.102708 / -8.759577 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · スコア 4.0 · 採用条件未達 · 順位差 -11.527798 / -9.095147 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) · スコア 2.246085 · 採用条件未達 · 順位差 -3.535844 / -10.849062 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) · スコア 0.324324 · 採用条件未達 · 順位差 -19.053863 / -12.770823 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) · スコア 0.201342 · 採用条件未達 · 順位差 -10.668735 / -12.893805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08112449799196787,
          0.07531692766592095
        ],
        "cfg_coverage": [
          0.029787234042553193,
          0.02880658436213992
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.869932,
        "reverse_margin": 4.802062000000001
      },
      "new": "00906b9c",
      "score": 13.095147
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.004662522202486678,
          0.007829977628635347
        ],
        "cfg_coverage": [
          0.0006666666666666666,
          0.0013717421124828531
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.566657,
        "reverse_margin": -4.802062000000001
      },
      "new": "0086b704",
      "score": 8.293085
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
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.286822000000001,
        "reverse_margin": -7.095147000000001
      },
      "new": "008673f0",
      "score": 6.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`0093eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eca4.md) FUN_0093eca4

`competing_candidates` 

呼出元 2件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

- 1. [`005e89a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e89a4.md) · スコア 65.333333 · 採用条件未達 · 順位差 5.856208999999993 / 0.730158000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005e87e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e87e8.md) · スコア 64.603175 · 採用条件未達 · 順位差 0.0 / -0.730158000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005e8a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8a98.md) · スコア 60.138889 · 採用条件未達 · 順位差 -1.4297380000000004 / -5.194443999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a599ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a599ac.md) · スコア 53.194444 · 採用条件未達 · 順位差 5.416665999999999 / -12.138888999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.6,
          0.6923076923076923
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.856208999999993,
        "reverse_margin": 0.730158000000003
      },
      "new": "005e89a4",
      "score": 65.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8148148148148148,
          0.8148148148148148
        ],
        "cfg_coverage": [
          0.7857142857142857,
          0.8461538461538461
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -0.730158000000003
      },
      "new": "005e87e8",
      "score": 64.603175
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8148148148148148,
          0.8148148148148148
        ],
        "cfg_coverage": [
          0.5625,
          0.6923076923076923
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.4297380000000004,
        "reverse_margin": -5.194443999999997
      },
      "new": "005e8a98",
      "score": 60.138889
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`0093eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093e/0093eef8.md) FUN_0093eef8

`competing_candidates` 

呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00a0ccb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ccb4.md) · スコア 49.597719 · 採用条件未達 · 順位差 10.195419999999999 / 19.296799999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md) · スコア 30.300919 · 採用条件未達 · 順位差 30.300919 / -19.296799999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00499040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md) · スコア 30.009503 · 採用条件未達 · 順位差 30.009503 / -19.588216 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004c46d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c46d8.md) · スコア 28.451061 · 採用条件未達 · 順位差 24.641537 / -21.146658 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00839c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839c70.md) · スコア 22.115933 · 採用条件未達 · 順位差 22.115933 / -27.481786 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0062ce84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ce84.md) · スコア 18.802661 · 採用条件未達 · 順位差 18.802661 / -30.795057999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00817698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817698.md) · スコア 18.731748 · 採用条件未達 · 順位差 16.378807 / -30.865971 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00836b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00836/00836b08.md) · スコア 18.363636 · 採用条件未達 · 順位差 0.6818179999999998 / -31.234083 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8275862068965517,
          0.6233766233766234
        ],
        "cfg_coverage": [
          0.8333333333333334,
          0.6097560975609756
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.195419999999999,
        "reverse_margin": 19.296799999999998
      },
      "new": "00a0ccb4",
      "score": 49.597719
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6037735849056604,
          0.4155844155844156
        ],
        "cfg_coverage": [
          0.4074074074074074,
          0.2682926829268293
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 30.300919,
        "reverse_margin": -19.296799999999998
      },
      "new": "00608594",
      "score": 30.300919
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5344827586206896,
          0.4025974025974026
        ],
        "cfg_coverage": [
          0.41379310344827586,
          0.2926829268292683
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 30.009503,
        "reverse_margin": -19.588216
      },
      "new": "00499040",
      "score": 30.009503
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-039556db291261e5ad701faaa4a86a37"></a>

### v16.0.0 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) FUN_009470d0

`competing_candidates` 

呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 112件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)

- 1. [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) · スコア 23.985674 · 採用条件未達 · 順位差 15.721511999999999 / 15.836108999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · スコア 8.149565 · 採用条件未達 · 順位差 -25.798466999999995 / -15.836108999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · スコア 8.092159 · 採用条件未達 · 順位差 -12.283548999999999 / -15.893514999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · スコア 8.073539 · 採用条件未達 · 順位差 -50.187870000000004 / -15.912135 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · スコア 6.15525 · 採用条件未達 · 順位差 -22.285094 / -17.830424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · スコア 6.122566 · 採用条件未達 · 順位差 -7.552641 / -17.863108 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · スコア 6.083055 · 採用条件未達 · 順位差 -33.904301 / -17.902619 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · スコア 6.057197 · 採用条件未達 · 順位差 -35.967712999999996 / -17.928477 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22600834492350486,
          0.2212991965136865
        ],
        "cfg_coverage": [
          0.1368577075098814,
          0.135386119257087
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 15.721511999999999,
        "reverse_margin": 15.836108999999999
      },
      "new": "009121c4",
      "score": 23.985674
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.002348643006263048,
          0.002451314176766989
        ],
        "cfg_coverage": [
          0.00043233895373973193,
          0.0004887585532746823
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -25.798466999999995,
        "reverse_margin": -15.836108999999999
      },
      "new": "00a788d0",
      "score": 8.149565
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0015359859566998245,
          0.002859866539561487
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -12.283548999999999,
        "reverse_margin": -15.893514999999999
      },
      "new": "0079bdf0",
      "score": 8.092159
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-59444baf9c6e4848e179d3246aa2c695"></a>

### v16.0.0 [`00961550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961550.md) FUN_00961550

`competing_candidates` 

呼出元 10件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 0件 

- 1. [`00698600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00698/00698600.md) · スコア 66.666667 · 採用条件未達 · 順位差 26.666667000000004 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00796a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00796/00796a84.md) · スコア 66.666667 · 採用条件未達 · 順位差 26.666667000000004 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008680dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/008680dc.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`008dd050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008dd/008dd050.md) · スコア 66.666667 · 採用条件未達 · 順位差 26.666667000000004 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0092bb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bb54.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`005dfeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfeb0.md) · スコア 40.0 · 採用条件未達 · 順位差 0.0 / -26.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005e0000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e0000.md) · スコア 40.0 · 採用条件未達 · 順位差 -40.0 / -26.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006181a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/006181a0.md) · スコア 40.0 · 採用条件未達 · 順位差 0.0 / -26.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7777777777777778,
          0.7777777777777778
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
        "margin": 26.666667000000004,
        "reverse_margin": 0.0
      },
      "new": "00698600",
      "score": 66.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7777777777777778,
          0.7777777777777778
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
        "margin": 26.666667000000004,
        "reverse_margin": 0.0
      },
      "new": "00796a84",
      "score": 66.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7777777777777778,
          0.7777777777777778
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
        "reverse_margin": 0.0
      },
      "new": "008680dc",
      "score": 66.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

