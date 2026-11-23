# v15.7.4 → v16.0.0 · 追加調査 (123)

[一覧の目次](README.md)

### v16.0.0 [`0070e560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e560.md) FUN_0070e560

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

- 1. [`006e44c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e44c4.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 5.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008f5c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f5c30.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006e434c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e434c.md) · スコア 60.0 · 採用条件未達 · 順位差 -6.666667000000004 / -10.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00758734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758734.md) · スコア 57.241379 · 採用条件未達 · 順位差 -4.137930999999995 / -12.758620999999998 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006023d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/006023d0.md) · スコア 55.7 · 採用条件未達 · 順位差 0.0 / -14.299999999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006e4630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4630.md) · スコア 49.5 · 採用条件未達 · 順位差 0.0 / -20.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006892e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/006892e4.md) · スコア 43.571429 · 採用条件未達 · 順位差 0.0 / -26.428570999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a3c208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c208.md) · スコア 42.5 · 採用条件未達 · 順位差 -22.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 5.0
      },
      "new": "006e44c4",
      "score": 70.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.782608695652174,
          0.75
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
        "margin": 0.0,
        "reverse_margin": -5.0
      },
      "new": "008f5c30",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.75
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
        "margin": -6.666667000000004,
        "reverse_margin": -10.0
      },
      "new": "006e434c",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0c51d48c3dd3e8a0a039649f55903112"></a>

### v16.0.0 [`0070e5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e5c0.md) FUN_0070e5c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e4690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4690.md) · スコア 45.714286 · 採用条件未達 · 順位差 45.714286 / 45.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42857142857142855,
          0.42857142857142855
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
        "margin": 45.714286,
        "reverse_margin": 45.714286
      },
      "new": "006e4690",
      "score": 45.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-eab6c658744814a266e573ec0f2c9c7c"></a>

### v16.0.0 [`0070e5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e5dc.md) FUN_0070e5dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e46ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e46ac.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`006e4690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4690.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "006e46ac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e4690",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-62f05fba8a99509dfc0f46d68837e8a2"></a>

### v16.0.0 [`0070e624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e624.md) FUN_0070e624

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e46f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e46f4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "006e46f4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-788716fb85f46fe67e7ab85e0fdf2102"></a>

### v16.0.0 [`0070e63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e63c.md) FUN_0070e63c

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 0件 

- 1. [`006e470c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e470c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.3333 / 68.3333 · 
- 2. [`006e46f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e46f4.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.3333,
        "reverse_margin": 68.3333
      },
      "new": "006e470c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e46f4",
      "score": 0.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-887e732121a4436c2cdfe5f5a9a5a85b"></a>

### v16.0.0 [`0070e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e644.md) FUN_0070e644

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`005f6c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f6c14.md)

- 1. [`006e4714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4714.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`006e443c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e443c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`006e45a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e45a8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`006e473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e473c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`006e4720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4720.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "006e4714",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e443c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e45a8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2980d8ab458684610c458e3381806f04"></a>

### v16.0.0 [`0070e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e650.md) FUN_0070e650

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e4720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4720.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "006e4720",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7f0ff1252ae43aa18ef322c2bcc456fb"></a>

### v16.0.0 [`0070e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e66c.md) FUN_0070e66c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e473c.md) · スコア 84.0 · 採用条件未達 · 順位差 80.0 / 80.0 · 
- 2. [`006e4714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4714.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`006e4720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4720.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "006e473c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e4714",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "006e4720",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-da33424f2d76d3da8af33a06b8d49a83"></a>

### v16.0.0 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) FUN_0070ea1c

`competing_candidates` 

呼出元 4件 [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`00714ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714ba8.md) [`00714f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`007153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007153c0.md) · 呼出先 87件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)

- 1. [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · スコア 37.120982 · 採用条件未達 · 順位差 32.846292999999996 / 32.63659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) · スコア 4.484392 · 採用条件未達 · 順位差 0.2232409999999998 / -32.63659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md) · スコア 2.48672 · 採用条件未達 · 順位差 -2.4273 / -34.634262 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009903e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00990/009903e4.md) · スコア 2.377639 · 採用条件未達 · 順位差 -0.5683700000000003 / -34.743342999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · スコア 2.340822 · 採用条件未達 · 順位差 -34.747079 / -34.780159999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00830c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/00830c98.md) · スコア 2.331596 · 採用条件未達 · 順位差 -2.569339 / -34.789386 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0076794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00767/0076794c.md) · スコア 2.264706 · 採用条件未達 · 順位差 -4.7066 / -34.856276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) · スコア 2.158562 · 採用条件未達 · 順位差 -1.9682880000000003 / -34.962419999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.49099099099099097,
          0.4808823529411765
        ],
        "cfg_coverage": [
          0.1134020618556701,
          0.14715719063545152
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 32.846292999999996,
        "reverse_margin": 32.63659
      },
      "new": "006e4aec",
      "score": 37.120982
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.008073196986006458,
          0.022058823529411766
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.2232409999999998,
        "reverse_margin": -32.63659
      },
      "new": "0059815c",
      "score": 4.484392
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.012738853503184714,
          0.0058823529411764705
        ],
        "cfg_coverage": [
          0.012578616352201259,
          0.006688963210702341
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.4273,
        "reverse_margin": -34.634262
      },
      "new": "00831724",
      "score": 2.48672
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c68a19d0ec7941897e80b304c555f33d"></a>

### v16.0.0 [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) FUN_00710090

`competing_candidates` 

呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 15件 [`00ab9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md) [`00af5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md) [`00af5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md) [`00af6068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6068.md) [`00af60d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md)

- 1. [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · スコア 16.212454 · 採用条件未達 · 順位差 16.212454 / 10.673992000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00663af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663af4.md) · スコア 5.538462 · 採用条件未達 · 順位差 -47.128204999999994 / -10.673992000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23846153846153847,
          0.23846153846153847
        ],
        "cfg_coverage": [
          0.10526315789473684,
          0.09523809523809523
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.212454,
        "reverse_margin": 10.673992000000002
      },
      "new": "006e60f0",
      "score": 16.212454
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.09230769230769231
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
        "margin": -47.128204999999994,
        "reverse_margin": -10.673992000000002
      },
      "new": "00663af4",
      "score": 5.538462
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-311611d776005a8c2f2c125e2f57c4f7"></a>

### v16.0.0 [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) FUN_00710298

`competing_candidates` 

呼出元 3件 [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 63件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`005e0e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md) [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md)

- 1. [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · スコア 16.956349 · 採用条件未達 · 順位差 10.956349 / 14.744933 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00442a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md) · スコア 2.211416 · 採用条件未達 · 順位差 1.3158939999999997 / -14.744933 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · スコア 2.052747 · 採用条件未達 · 順位差 -14.116298 / -14.903602 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -16.822947 / -16.956349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0089cc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089cc84.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.633302 / -16.956349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17978339350180506,
          0.17547568710359407
        ],
        "cfg_coverage": [
          0.0213903743315508,
          0.029197080291970802
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.956349,
        "reverse_margin": 14.744933
      },
      "new": "006e62f8",
      "score": 16.956349
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006377551020408163,
          0.0035236081747709656
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.3158939999999997,
        "reverse_margin": -14.744933
      },
      "new": "00442a64",
      "score": 2.211416
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0008791208791208791,
          0.0014094432699083862
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.116298,
        "reverse_margin": -14.903602
      },
      "new": "009f1ea8",
      "score": 2.052747
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4823055127540112e2f7c1a0ffaac146"></a>

### v16.0.0 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) FUN_007119b0

`competing_candidates` 

呼出元 4件 [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`00714d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714d78.md) [`00714f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) [`007153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007153c0.md) · 呼出先 99件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`005e0e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md) [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md)

- 1. [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · スコア 16.822947 · 採用条件未達 · 順位差 15.124058999999999 / 14.707386 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · スコア 2.115561 · 採用条件未達 · 順位差 -35.005421 / -14.707386 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · スコア 0.084507 · 採用条件未達 · 順位差 -9.212420999999999 / -16.73844 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) · スコア 0.039267 · 採用条件未達 · 順位差 -15.931946 / -16.78368 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · スコア 0.026374 · 採用条件未達 · 順位差 -16.142671 / -16.796573 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005fa9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -10.766857 / -16.822947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.634453 / -16.822947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.27163781624500666,
          0.2670157068062827
        ],
        "cfg_coverage": [
          0.040100250626566414,
          0.04289544235924933
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.124058999999999,
        "reverse_margin": 14.707386
      },
      "new": "006e79bc",
      "score": 16.822947
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03453453453453453,
          0.030104712041884817
        ],
        "cfg_coverage": [
          0.015463917525773196,
          0.0160857908847185
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.005421,
        "reverse_margin": -14.707386
      },
      "new": "006e4aec",
      "score": 2.115561
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0014084507042253522,
          0.0032722513089005235
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
        "margin": -9.212420999999999,
        "reverse_margin": -16.73844
      },
      "new": "009c5344",
      "score": 0.084507
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8f16a620a2ed77e2c3d73428cc1b737d"></a>

### v16.0.0 [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) FUN_00713318

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 31件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`005fe208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md)

- 1. [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) · スコア 41.07732 · 採用条件未達 · 順位差 33.456553 / 33.804661 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · スコア 7.272659 · 採用条件未達 · 順位差 -38.616979 / -33.804661 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005d4158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4158.md) · スコア 0.895522 · 採用条件未達 · 順位差 -46.038974 / -40.181798 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ced48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ced48.md) · スコア 0.0 · 採用条件未達 · 順位差 -41.8198 / -41.07732 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6119402985074627,
          0.6119402985074627
        ],
        "cfg_coverage": [
          0.23387096774193547,
          0.21804511278195488
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.456553,
        "reverse_margin": 33.804661
      },
      "new": "006e92bc",
      "score": 41.07732
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10391822827938671,
          0.1011608623548922
        ],
        "cfg_coverage": [
          0.0784313725490196,
          0.06015037593984962
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -38.616979,
        "reverse_margin": -33.804661
      },
      "new": "006ea1c0",
      "score": 7.272659
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02295918367346939,
          0.014925373134328358
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
        "margin": -46.038974,
        "reverse_margin": -40.181798
      },
      "new": "005d4158",
      "score": 0.895522
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-57ad46e650b778733408e4e580c8aa05"></a>

### v16.0.0 [`00713ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) FUN_00713ce4

`competing_candidates` 

呼出元 5件 [`005f8e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8e40.md) [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 26件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00af54c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af54c8.md) [`00af7178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7178.md) [`00af71c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af71c0.md) [`00af7958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7958.md)

- 1. [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · スコア 51.171875 · 採用条件未達 · 順位差 49.0625 / 50.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006ecae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006ecae4.md) · スコア 1.171875 · 採用条件未達 · 順位差 -29.888731 / -50.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.51953125,
          0.51953125
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
        "margin": 49.0625,
        "reverse_margin": 50.0
      },
      "new": "006e9c88",
      "score": 51.171875
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03787878787878788,
          0.01953125
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
        "margin": -29.888731,
        "reverse_margin": -50.0
      },
      "new": "006ecae4",
      "score": 1.171875
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d0b8c439f36b31a821ce1ab868737245"></a>

### v16.0.0 [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) FUN_0071421c

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 28件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`005fe208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md)

- 1. [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · スコア 45.889638 · 採用条件未達 · 順位差 38.616979 / 38.268871 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) · スコア 7.620767 · 採用条件未達 · 順位差 -33.456553 / -38.268871 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0085e328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e328.md) · スコア 0.817717 · 採用条件未達 · 順位差 -4.490014 / -45.071920999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a50324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a50324.md) · スコア 0.761905 · 採用条件未達 · 順位差 -15.554725 / -45.127733 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005ced48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ced48.md) · スコア 0.0 · 採用条件未達 · 順位差 -41.8198 / -45.889638 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00887594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887594.md) · スコア 0.0 · 採用条件未達 · 順位差 -63.875556 / -45.889638 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -61.697778 / -45.889638 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00887e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887e18.md) · スコア 0.0 · 採用条件未達 · 順位差 -63.178182 / -45.889638 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6575809199318569,
          0.6575809199318569
        ],
        "cfg_coverage": [
          0.3627450980392157,
          0.3217391304347826
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 38.616979,
        "reverse_margin": 38.268871
      },
      "new": "006ea1c0",
      "score": 45.889638
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10281923714759536,
          0.10562180579216354
        ],
        "cfg_coverage": [
          0.07258064516129033,
          0.0782608695652174
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.456553,
        "reverse_margin": -38.268871
      },
      "new": "006e92bc",
      "score": 7.620767
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.022727272727272728,
          0.013628620102214651
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
        "margin": -4.490014,
        "reverse_margin": -45.071920999999996
      },
      "new": "0085e328",
      "score": 0.817717
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8297d1e02af4fe32cf4697d333be82f8"></a>

### v16.0.0 [`00714ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714ba8.md) FUN_00714ba8

`competing_candidates` 

呼出元 1件 [`005f7900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) · 呼出先 5件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00af3634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md) [`00afa6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa6a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`006eab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eab4c.md) · スコア 33.142857 · 採用条件未達 · 順位差 11.199461 / 6.495542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006ead1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ead1c.md) · スコア 26.647315 · 採用条件未達 · 順位差 -13.975327 / -6.495542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00557adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md) · スコア 5.490196 · 採用条件未達 · 順位差 -2.1871659999999995 / -27.652661 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0045f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md) · スコア 2.937063 · 採用条件未達 · 順位差 0.0 / -30.205793999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004b6640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) · スコア 2.27027 · 採用条件未達 · 順位差 0.0 / -30.872587 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a4af88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md) · スコア 1.935484 · 採用条件未達 · 順位差 -2.4992990000000006 / -31.207373 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00604288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md) · スコア 1.355932 · 採用条件未達 · 順位差 -2.3728819999999997 / -31.786925 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) · スコア 0.326975 · 採用条件未達 · 順位差 -1.372992 / -32.815882 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5523809523809524,
          0.5523809523809524
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
        "margin": 11.199461,
        "reverse_margin": 6.495542
      },
      "new": "006eab4c",
      "score": 33.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4056603773584906,
          0.4095238095238095
        ],
        "cfg_coverage": [
          0.15,
          0.11538461538461539
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.975327,
        "reverse_margin": -6.495542
      },
      "new": "006ead1c",
      "score": 26.647315
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0915032679738562,
          0.13333333333333333
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
        "margin": -2.1871659999999995,
        "reverse_margin": -27.652661
      },
      "new": "00557adc",
      "score": 5.490196
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-60b915ea7da98931f63b9c9056d87832"></a>

### v16.0.0 [`00714d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714d78.md) FUN_00714d78

`competing_candidates` 

呼出元 1件 [`005f7900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) · 呼出先 5件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00af3634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md) [`00afa6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa6a0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`006ead1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ead1c.md) · スコア 40.622642 · 採用条件未達 · 順位差 13.975327 / 18.679246 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006eab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eab4c.md) · スコア 21.943396 · 採用条件未達 · 順位差 -11.199461 / -18.679246 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00557adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md) · スコア 5.490196 · 採用条件未達 · 順位差 -2.1871659999999995 / -35.132446 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0045f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md) · スコア 2.937063 · 採用条件未達 · 順位差 0.0 / -37.685579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004b6640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) · スコア 2.27027 · 採用条件未達 · 順位差 0.0 / -38.352372 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008d5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5008.md) · スコア 1.007194 · 採用条件未達 · 順位差 -0.9928060000000001 / -39.615448 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00604288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604288.md) · スコア 0.677966 · 採用条件未達 · 順位差 -3.050848 / -39.944676 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) · スコア 0.326975 · 採用条件未達 · 順位差 -1.372992 / -40.295667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.660377358490566,
          0.660377358490566
        ],
        "cfg_coverage": [
          0.05,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.975327,
        "reverse_margin": 18.679246
      },
      "new": "006ead1c",
      "score": 40.622642
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3523809523809524,
          0.3490566037735849
        ],
        "cfg_coverage": [
          0.05,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.199461,
        "reverse_margin": -18.679246
      },
      "new": "006eab4c",
      "score": 21.943396
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0915032679738562,
          0.1320754716981132
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
        "margin": -2.1871659999999995,
        "reverse_margin": -35.132446
      },
      "new": "00557adc",
      "score": 5.490196
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b53c415db37ea2a274055d04a55db08d"></a>

### v16.0.0 [`007153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007153c0.md) FUN_007153c0

`competing_candidates` 

呼出元 1件 [`005f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f9670.md) · 呼出先 3件 [`005fe244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md)

- 1. [`006eb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb364.md) · スコア 70.625 · 採用条件未達 · 順位差 70.625 / 70.625 · instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.84375,
          0.84375
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
        "margin": 70.625,
        "reverse_margin": 70.625
      },
      "new": "006eb364",
      "score": 70.625
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-761cb2fb9cdbac0ee1f556bcc1ca6f33"></a>

### v16.0.0 [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) FUN_007154c0

`competing_candidates` 

呼出元 2件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 81件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)

- 1. [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · スコア 37.46663 · 採用条件未達 · 順位差 33.245717 / 34.485833 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · スコア 2.980797 · 採用条件未達 · 順位差 -33.465399 / -34.485833 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · スコア 2.0 · 採用条件未達 · 順位差 -35.120982 / -35.46663 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) · スコア 0.397644 · 採用条件未達 · 順位差 -0.753084 / -37.068986 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0054b520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054b/0054b520.md) · スコア 0.397644 · 採用条件未達 · 順位差 0.12450299999999997 / -37.068986 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) · スコア 0.353461 · 採用条件未達 · 順位差 -0.0005209999999999937 / -37.113169 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00664ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md) · スコア 0.353461 · 採用条件未達 · 順位差 -10.167182 / -37.113169 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007028d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007028d0.md) · スコア 0.31477 · 採用条件未達 · 順位差 -8.033898 / -37.15186 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4852724594992636,
          0.4852724594992636
        ],
        "cfg_coverage": [
          0.2175141242937853,
          0.22063037249283668
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.245717,
        "reverse_margin": 34.485833
      },
      "new": "006eb464",
      "score": 37.46663
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015509103169251517,
          0.016936671575846832
        ],
        "cfg_coverage": [
          0.002512562814070352,
          0.0028653295128939827
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.465399,
        "reverse_margin": -34.485833
      },
      "new": "006eccf4",
      "score": 2.980797
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
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.120982,
        "reverse_margin": -35.46663
      },
      "new": "006e4aec",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0502c9ffb43509820ea9fec4176f7703"></a>

### v16.0.0 [`00716b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716b40.md) FUN_00716b40

`competing_candidates` 

呼出元 2件 [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 17件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a519e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md)

- 1. [`006ecae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006ecae4.md) · スコア 31.060606 · 採用条件未達 · 順位差 29.242424 / 26.060606 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00466fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466fc4.md) · スコア 5.0 · 採用条件未達 · 順位差 5.0 / -26.060606 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006f0224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0224.md) · スコア 4.090909 · 採用条件未達 · 順位差 -0.7478009999999999 / -26.969697 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00987ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/00987ebc.md) · スコア 4.090909 · 採用条件未達 · 順位差 -0.7305200000000003 / -26.969697 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00aa1da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1da4.md) · スコア 4.090909 · 採用条件未達 · 順位差 -41.83614300000001 / -26.969697 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0056f1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f1e8.md) · スコア 3.636364 · 採用条件未達 · 順位差 -0.6493499999999996 / -27.424242 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00aa55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa55b0.md) · スコア 3.636364 · 採用条件未達 · 順位差 -30.916826999999998 / -27.424242 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00aa224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa224c.md) · スコア 3.529412 · 採用条件未達 · 順位差 -11.935208999999999 / -27.531194 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5075757575757576,
          0.5075757575757576
        ],
        "cfg_coverage": [
          0.030303030303030304,
          0.03333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 29.242424,
        "reverse_margin": 26.060606
      },
      "new": "006ecae4",
      "score": 31.060606
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.08333333333333333
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
        "margin": 5.0,
        "reverse_margin": -26.060606
      },
      "new": "00466fc4",
      "score": 5.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19148936170212766,
          0.06818181818181818
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
        "margin": -0.7478009999999999,
        "reverse_margin": -26.969697
      },
      "new": "006f0224",
      "score": 4.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-be1df98a1a9159593874a22f741211b2"></a>

### v16.0.0 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) FUN_00716d50

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 123件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)

- 1. [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · スコア 36.446196 · 採用条件未達 · 順位差 33.465399 / 33.513254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) · スコア 2.932942 · 採用条件未達 · 順位差 -34.533688000000005 / -33.513254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) · スコア 0.04035 · 採用条件未達 · 順位差 -52.458504000000005 / -36.405846000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -16.822947 / -36.446196 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.48415374241402565,
          0.4828513786146604
        ],
        "cfg_coverage": [
          0.30402010050251255,
          0.2737556561085973
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.465399,
        "reverse_margin": 33.513254
      },
      "new": "006eccf4",
      "score": 36.446196
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.016200294550810016,
          0.014794889038332213
        ],
        "cfg_coverage": [
          0.002824858757062147,
          0.0022624434389140274
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.533688000000005,
        "reverse_margin": -33.513254
      },
      "new": "006eb464",
      "score": 2.932942
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0013123359580052493,
          0.0006724949562878278
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
        "margin": -52.458504000000005,
        "reverse_margin": -36.405846000000004
      },
      "new": "006ee6c8",
      "score": 0.04035
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4287697e6fd8ed258f7fe895f5e0020d"></a>

### v16.0.0 [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) FUN_00718734

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 24件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md)

- 1. [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) · スコア 52.498854 · 採用条件未達 · 順位差 50.498854 / 51.74235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009f426c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f426c.md) · スコア 0.756504 · 採用条件未達 · 順位差 -50.340135000000004 / -51.74235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0047a5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md) · スコア 0.629921 · 採用条件未達 · 順位差 0.629921 / -51.868933 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005cca80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cca80.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.376238 / -52.498854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6929133858267716,
          0.6929133858267716
        ],
        "cfg_coverage": [
          0.5261194029850746,
          0.4462025316455696
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 50.498854,
        "reverse_margin": 51.74235
      },
      "new": "006ee6c8",
      "score": 52.498854
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02857142857142857,
          0.010498687664041995
        ],
        "cfg_coverage": [
          0.01680672268907563,
          0.006329113924050633
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -50.340135000000004,
        "reverse_margin": -51.74235
      },
      "new": "009f426c",
      "score": 0.756504
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03162055335968379,
          0.010498687664041995
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
        "margin": 0.629921,
        "reverse_margin": -51.868933
      },
      "new": "0047a5ec",
      "score": 0.629921
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6918ed2c5fb11306bc3a678e34b1491f"></a>

### v16.0.0 [`0071931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/0071931c.md) FUN_0071931c

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 19件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`005e0898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0898.md) [`005e08c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08c0.md) [`005e08e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md) [`005e0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md)

- 1. [`006ef2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef2b0.md) · スコア 39.985281 · 採用条件未達 · 順位差 35.337633 / 39.985281 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6160337552742616,
          0.6160337552742616
        ],
        "cfg_coverage": [
          0.19402985074626866,
          0.1511627906976744
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.337633,
        "reverse_margin": 39.985281
      },
      "new": "006ef2b0",
      "score": 39.985281
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-35f3eeed94a314d01fa94493a7f2d7dc"></a>

### v16.0.0 [`0071ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ac84.md) FUN_0071ac84

`competing_candidates` [`006f0c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c18.md)

呼出元 2件 [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071ac74",
    "0071ac94",
    "006f0c08",
    "006f0c28"
  ],
  "initial_reason": ""
}
~~~

<a id="review-d079e76e1b313198206597f92f2dd31e"></a>

### v16.0.0 [`0071acc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acc8.md) FUN_0071acc8

`competing_candidates` [`006f0c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c5c.md)

呼出元 2件 [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071acbc",
    "0071acd0",
    "006f0c50",
    "006f0c64"
  ],
  "initial_reason": ""
}
~~~

<a id="review-851f52984d2821792387a36bf3f9af92"></a>

### v16.0.0 [`0071acd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acd8.md) FUN_0071acd8

`competing_candidates` [`006f0c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c6c.md)

呼出元 3件 [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) [`009113c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00911/009113c4.md) [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071acd0",
    "0071acf0",
    "006f0c64",
    "006f0c84"
  ],
  "initial_reason": ""
}
~~~

<a id="review-007bea06dde6dc18fde112e0ab883bd3"></a>

### v16.0.0 [`0071ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ace0.md) FUN_0071ace0

`competing_candidates` [`006f0c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c74.md)

呼出元 1件 [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071acd0",
    "0071acf0",
    "006f0c64",
    "006f0c84"
  ],
  "initial_reason": ""
}
~~~

<a id="review-e2e2c9534fbf4984f27255ebccd7bb72"></a>

### v16.0.0 [`0071ace8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ace8.md) FUN_0071ace8

`competing_candidates` [`006f0c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c7c.md)

呼出元 2件 [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) [`0090da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090da6c.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071acd0",
    "0071acf0",
    "006f0c64",
    "006f0c84"
  ],
  "initial_reason": ""
}
~~~

<a id="review-f5b962e11ad9f043192fd3cc22953f32"></a>

### v16.0.0 [`0071acf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acf8.md) FUN_0071acf8

`competing_candidates` [`006f0c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c8c.md)

呼出元 3件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071acf0",
    "0071ad00",
    "006f0c84",
    "006f0c94"
  ],
  "initial_reason": ""
}
~~~

<a id="review-891582656573fde948d3525ca20993ba"></a>

### v16.0.0 [`0071ad08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad08.md) FUN_0071ad08

`competing_candidates` [`006f0c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0c9c.md)

呼出元 1件 [`0071b974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b974.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0071ad00",
    "0071ad10",
    "006f0c94",
    "006f0ca4"
  ],
  "initial_reason": ""
}
~~~

<a id="review-0abaac0591483fc67c96b9ecce215855"></a>

### v16.0.0 [`0071b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b894.md) FUN_0071b894

`competing_candidates` 

呼出元 16件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) [`0090cab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090c/0090cab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f1828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1828.md) · スコア 30.0 · 採用条件未達 · 順位差 -35.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1848.md) · スコア 0.0 · 採用条件未達 · 順位差 -47.096774 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f18c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f18c4.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f3104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3104.md) · スコア 0.0 · 採用条件未達 · 順位差 -17.5 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -35.0,
        "reverse_margin": 30.0
      },
      "new": "006f1828",
      "score": 30.0
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
        "margin": -47.096774,
        "reverse_margin": -30.0
      },
      "new": "006f1848",
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
        "reverse_margin": -30.0
      },
      "new": "006f18c4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ebccd5a0972b48e790a31eb2edbb4d63"></a>

### v16.0.0 [`0071b8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b8b4.md) FUN_0071b8b4

`competing_candidates` 

呼出元 13件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) [`0090cab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090c/0090cab8.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`0063ed88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ed88.md) · スコア 18.341014 · 採用条件未達 · 順位差 -18.087556999999997 / 4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md) · スコア 13.548387 · 採用条件未達 · 順位差 -42.880184 / -4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0063e518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e518.md) · スコア 13.548387 · 採用条件未達 · 順位差 -32.165899 / -4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0063e7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e7a8.md) · スコア 13.548387 · 採用条件未達 · 順位差 -30.023042000000004 / -4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0063f008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f008.md) · スコア 13.548387 · 採用条件未達 · 順位差 -20.737327 / -4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f1848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1848.md) · スコア 13.548387 · 採用条件未達 · 順位差 -33.548387000000005 / -4.792627000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0063e844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e844.md) · スコア 11.612903 · 採用条件未達 · 順位差 -36.244240000000005 / -6.728111000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 2.181818 · 採用条件未達 · 順位差 -22.524949 / -16.159196 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.25806451612903225
        ],
        "cfg_coverage": [
          0.25,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.087556999999997,
        "reverse_margin": 4.792627000000001
      },
      "new": "0063ed88",
      "score": 18.341014
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.22580645161290322
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
        "margin": -42.880184,
        "reverse_margin": -4.792627000000001
      },
      "new": "0063e4a8",
      "score": 13.548387
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.22580645161290322
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
        "margin": -32.165899,
        "reverse_margin": -4.792627000000001
      },
      "new": "0063e518",
      "score": 13.548387
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`0071b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b930.md) FUN_0071b930

`competing_candidates` 

呼出元 17件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 0件 

- 1. [`006f18c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f18c4.md) · スコア 60.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 2. [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 0.0 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00adc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc120.md) · スコア 48.421053 · 採用条件未達 · 順位差 48.421053 / -11.578947 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005c2720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2720.md) · スコア 41.176471 · 採用条件未達 · 順位差 41.176471 / -18.823529 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005c2a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2a5c.md) · スコア 37.647059 · 採用条件未達 · 順位差 37.647059 / -22.352941 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0089f578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f578.md) · スコア 17.647059 · 採用条件未達 · 順位差 17.647059 / -42.352941 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "006f18c4",
      "score": 60.0
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
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 60.0,
        "reverse_margin": 0.0
      },
      "new": "00adc094",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47368421052631576,
          0.5294117647058824
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
        "margin": 48.421053,
        "reverse_margin": -11.578947
      },
      "new": "00adc120",
      "score": 48.421053
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5c1734aa0ab336073a0dfa3e0d7ae064"></a>

### v16.0.0 [`0071b974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b974.md) FUN_0071b974

`competing_candidates` 

呼出元 1件 [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0071ad08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad08.md) [`0071b4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b4e4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 24.493506 · 採用条件未達 · 順位差 -0.21326099999999926 / 1.2153109999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1bc8.md) · スコア 23.278195 · 採用条件未達 · 順位差 -35.56390999999999 / -1.2153109999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f2640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2640.md) · スコア 18.516129 · 採用条件未達 · 順位差 -4.820867 / -5.977377000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008e67a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e67a0.md) · スコア 12.363636 · 採用条件未達 · 順位差 -26.108125 / -12.12987 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007d0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0878.md) · スコア 11.432189 · 採用条件未達 · 順位差 -32.420331 / -13.061317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f2e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2e2c.md) · スコア 9.766234 · 採用条件未達 · 順位差 -32.071428 / -14.727272 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00709d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/00709d24.md) · スコア 7.454545 · 採用条件未達 · 順位差 -41.045455 / -17.038961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007dc80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc80c.md) · スコア 5.454545 · 採用条件未達 · 順位差 -15.721926 / -19.038961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32727272727272727,
          0.32727272727272727
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -0.21326099999999926,
        "reverse_margin": 1.2153109999999998
      },
      "new": "006f1908",
      "score": 24.493506
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30701754385964913,
          0.3181818181818182
        ],
        "cfg_coverage": [
          0.2222222222222222,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.56390999999999,
        "reverse_margin": -1.2153109999999998
      },
      "new": "006f1bc8",
      "score": 23.278195
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2619047619047619,
          0.2
        ],
        "cfg_coverage": [
          0.22580645161290322,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.820867,
        "reverse_margin": -5.977377000000001
      },
      "new": "006f2640",
      "score": 18.516129
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0725a729a6e261a14b8aeee068e68e41"></a>

### v16.0.0 [`0071bb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bb2c.md) FUN_0071bb2c

`competing_candidates` 

呼出元 5件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 56.0 · 採用条件未達 · 順位差 -8.347825999999998 / 4.799999999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 51.2 · 採用条件未達 · 順位差 16.800000000000004 / -4.799999999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 31.190476 · 採用条件未達 · 順位差 -1.0317460000000018 / -24.809524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 16.5 · 採用条件未達 · 順位差 -12.576923 / -39.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0063f964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f964.md) · スコア 12.0 · 採用条件未達 · 順位差 -60.0 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0063f9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f9a0.md) · スコア 12.0 · 採用条件未達 · 順位差 -44.0 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007d0b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0b04.md) · スコア 12.0 · 採用条件未達 · 順位差 -60.0 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a932f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a932f0.md) · スコア 12.0 · 採用条件未達 · 順位差 -60.0 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6521739130434783,
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.347825999999998,
        "reverse_margin": 4.799999999999997
      },
      "new": "006f1b24",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.72,
          0.72
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
        "margin": 16.800000000000004,
        "reverse_margin": -4.799999999999997
      },
      "new": "006f1ac0",
      "score": 51.2
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4642857142857143,
          0.52
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.0317460000000018,
        "reverse_margin": -24.809524
      },
      "new": "006f2790",
      "score": 31.190476
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9de1adfde4e3ad20c0c97838a018458f"></a>

### v16.0.0 [`0071bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bb90.md) FUN_0071bb90

`competing_candidates` 

呼出元 5件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 64.347826 · 採用条件未達 · 順位差 8.347825999999998 / 29.947826 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 34.4 · 採用条件未達 · 順位差 -16.800000000000004 / -29.947826 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 20.47619 · 採用条件未達 · 順位差 -11.746032000000003 / -43.871635999999995 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 16.5 · 採用条件未達 · 順位差 -12.576923 / -47.847826 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b80.md) · スコア 10.434783 · 採用条件未達 · 順位差 -52.89855 / -53.913043 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) · スコア 8.597285 · 採用条件未達 · 順位差 -25.873303 / -55.750541 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1d90.md) · スコア 8.275862 · 採用条件未達 · 順位差 -45.103448 / -56.071963999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006f18c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f18c4.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -64.347826 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7391304347826086,
          0.7391304347826086
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
        "margin": 8.347825999999998,
        "reverse_margin": 29.947826
      },
      "new": "006f1b24",
      "score": 64.347826
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.44,
          0.4782608695652174
        ],
        "cfg_coverage": [
          0.4,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -16.800000000000004,
        "reverse_margin": -29.947826
      },
      "new": "006f1ac0",
      "score": 34.4
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.34782608695652173
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.746032000000003,
        "reverse_margin": -43.871635999999995
      },
      "new": "006f2790",
      "score": 20.47619
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-81cd576ae0223a936f69bf365da30d16"></a>

### v16.0.0 [`0071bbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bbec.md) FUN_0071bbec

`competing_candidates` 

呼出元 1件 [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 3件 [`0071acd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acd0.md) [`0071bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bc34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b80.md) · スコア 63.333333 · 採用条件未達 · 順位差 33.908046 / 34.574712000000005 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006f1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1d90.md) · スコア 28.758621 · 採用条件未達 · 順位差 -24.620688999999995 / -34.574712000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 10.434783 · 採用条件未達 · 順位差 -53.913043 / -52.89855 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a6a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md) · スコア 10.434783 · 採用条件未達 · 順位差 -38.260869 / -52.89855 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 9.6 · 採用条件未達 · 順位差 -41.6 / -53.733333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 8.571429 · 採用条件未達 · 順位差 -23.650793 / -54.761904 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 8.0 · 採用条件未達 · 順位差 -21.076923 / -55.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006c2cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c2/006c2cc4.md) · スコア 7.826087 · 採用条件未達 · 順位差 -46.086956 / -55.507246 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7222222222222222,
          0.7222222222222222
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
        "margin": 33.908046,
        "reverse_margin": 34.574712000000005
      },
      "new": "006f1b80",
      "score": 63.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3793103448275862,
          0.6111111111111112
        ],
        "cfg_coverage": [
          0.3,
          0.6
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.620688999999995,
        "reverse_margin": -34.574712000000005
      },
      "new": "006f1d90",
      "score": 28.758621
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17391304347826086,
          0.2222222222222222
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
        "margin": -53.913043,
        "reverse_margin": -52.89855
      },
      "new": "006f1b24",
      "score": 10.434783
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-51541e6231521aee939c2449aefc0291"></a>

### v16.0.0 [`0071bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bc34.md) FUN_0071bc34

`competing_candidates` 

呼出元 9件 [`0071bbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bbec.md) [`0071bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bdfc.md) [`0071be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be70.md) [`0071c3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c3e0.md) [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0071b4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b4e4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006f1bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1bc8.md) · スコア 58.842105 · 採用条件未達 · 順位差 35.56390999999999 / 34.135338 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 24.706767 · 採用条件未達 · 順位差 0.21326099999999926 / -34.135338 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007d0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0878.md) · スコア 14.85994 · 採用条件未達 · 順位差 -28.992579999999997 / -43.982164999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0062bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bb1c.md) · スコア 14.690058 · 採用条件未達 · 順位差 -60.517489000000005 / -44.152046999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006ee50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee50c.md) · スコア 14.690058 · 採用条件未達 · 順位差 -49.973649 / -44.152046999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005d75d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d7/005d75d4.md) · スコア 13.578947 · 採用条件未達 · 順位差 -46.549395000000004 / -45.263158 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006f2640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2640.md) · スコア 13.528014 · 採用条件未達 · 順位差 -9.808981999999999 / -45.314091 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00870b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00870/00870b84.md) · スコア 11.473684 · 採用条件未達 · 順位差 -43.19478 / -47.368421 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6140350877192983,
          0.6140350877192983
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
        "margin": 35.56390999999999,
        "reverse_margin": 34.135338
      },
      "new": "006f1bc8",
      "score": 58.842105
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3181818181818182,
          0.30701754385964913
        ],
        "cfg_coverage": [
          0.21428571428571427,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.21326099999999926,
        "reverse_margin": -34.135338
      },
      "new": "006f1908",
      "score": 24.706767
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17177914110429449,
          0.24561403508771928
        ],
        "cfg_coverage": [
          0.1276595744680851,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -28.992579999999997,
        "reverse_margin": -43.982164999999995
      },
      "new": "007d0878",
      "score": 14.85994
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bb05930aa1fc6d402eb262755e46daaa"></a>

### v16.0.0 [`0071bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bdfc.md) FUN_0071bdfc

`competing_candidates` 

呼出元 2件 [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 3件 [`0071acd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acd0.md) [`0071bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bc34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1d90.md) · スコア 53.37931 · 採用条件未達 · 順位差 24.620688999999995 / 23.954022999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b80.md) · スコア 29.425287 · 採用条件未達 · 順位差 -33.908046 / -23.954022999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 8.275862 · 採用条件未達 · 順位差 -42.924138 / -45.103448 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 8.275862 · 採用条件未達 · 順位差 -56.071963999999994 / -45.103448 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 8.275862 · 採用条件未達 · 順位差 -23.946360000000002 / -45.103448 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a6a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md) · スコア 8.275862 · 採用条件未達 · 順位差 -40.419790000000006 / -45.103448 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 8.0 · 採用条件未達 · 順位差 -21.076923 / -45.37931 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005b0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md) · スコア 6.206897 · 採用条件未達 · 順位差 -6.293103 / -47.172413 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6896551724137931,
          0.6896551724137931
        ],
        "cfg_coverage": [
          0.6,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.620688999999995,
        "reverse_margin": 23.954022999999996
      },
      "new": "006f1d90",
      "score": 53.37931
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6111111111111112,
          0.3793103448275862
        ],
        "cfg_coverage": [
          0.6,
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
        "margin": -33.908046,
        "reverse_margin": -23.954022999999996
      },
      "new": "006f1b80",
      "score": 29.425287
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16,
          0.13793103448275862
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
        "margin": -42.924138,
        "reverse_margin": -45.103448
      },
      "new": "006f1ac0",
      "score": 8.275862
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-abd3eff522b5831cda1ddd088e6c1f25"></a>

### v16.0.0 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) FUN_0071be98

`competing_candidates` 

呼出元 61件 [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`006270cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md) [`00627c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md) · 呼出先 7件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0071b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b930.md) [`00811630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00811/00811630.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a69414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md)

- 1. [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) · スコア 20.572057 · 採用条件未達 · 順位差 12.230427 / 10.283102000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f48c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f48c4.md) · スコア 10.288955 · 採用条件未達 · 順位差 -48.828548 / -10.283102000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) · スコア 2.331492 · 採用条件未達 · 順位差 -16.157451 / -18.240565 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0061c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061c/0061c140.md) · スコア 1.941815 · 採用条件未達 · 順位差 -34.432993 / -18.630242000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 1.597633 · 採用条件未達 · 順位差 -23.109133999999997 / -18.974424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00615b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00615/00615b10.md) · スコア 0.0 · 採用条件未達 · 順位差 -40.53913 / -20.572057 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25443786982248523,
          0.25443786982248523
        ],
        "cfg_coverage": [
          0.1652892561983471,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 12.230427,
        "reverse_margin": 10.283102000000001
      },
      "new": "006f1e2c",
      "score": 20.572057
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2441860465116279,
          0.1242603550295858
        ],
        "cfg_coverage": [
          0.06578947368421052,
          0.041666666666666664
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -48.828548,
        "reverse_margin": -10.283102000000001
      },
      "new": "006f48c4",
      "score": 10.288955
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0055248618784530384,
          0.01775147928994083
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
        "margin": -16.157451,
        "reverse_margin": -18.240565
      },
      "new": "006f3154",
      "score": 2.331492
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b43108309b36f914ead392a51e3ec985"></a>

### v16.0.0 [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) FUN_0071c420

`competing_candidates` 

呼出元 45件 [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`00616910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md) · 呼出先 3件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) · スコア 51.811414 · 採用条件未達 · 順位差 39.230768999999995 / 40.198510999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a9bb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9b/00a9bb7c.md) · スコア 11.612903 · 採用条件未達 · 順位差 -31.835373 / -40.198510999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aa383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa383c.md) · スコア 11.612903 · 採用条件未達 · 順位差 -28.771711999999997 / -40.198510999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00aa5af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5af4.md) · スコア 11.612903 · 採用条件未達 · 順位差 -31.079404999999998 / -40.198510999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00aa5c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5c94.md) · スコア 11.612903 · 採用条件未達 · 順位差 -31.079404999999998 / -40.198510999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a94d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a94/00a94d50.md) · スコア 10.645161 · 採用条件未達 · 順位差 -52.803115 / -41.166253 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00705000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/00705000.md) · スコア 9.677419 · 採用条件未達 · 順位差 9.677419 / -42.133995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006f4b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4b74.md) · スコア 5.806452 · 採用条件未達 · 順位差 -38.308381 / -46.004962 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7096774193548387,
          0.7096774193548387
        ],
        "cfg_coverage": [
          0.46153846153846156,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 39.230768999999995,
        "reverse_margin": 40.198510999999996
      },
      "new": "006f23b4",
      "score": 51.811414
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.41379310344827586,
          0.1935483870967742
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.835373,
        "reverse_margin": -40.198510999999996
      },
      "new": "00a9bb7c",
      "score": 11.612903
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23076923076923078,
          0.1935483870967742
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
        "margin": -28.771711999999997,
        "reverse_margin": -40.198510999999996
      },
      "new": "00aa383c",
      "score": 11.612903
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d2d14e5f24ab692db040ad7afdd91319"></a>

### v16.0.0 [`0071c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c518.md) FUN_0071c518

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009dbf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf88.md) [`009dbf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf94.md) [`009dbfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbfa0.md)

- 1. [`006f24ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f24ac.md) · スコア 22.625 · 採用条件未達 · 順位差 12.625 / 12.803571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0069b9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069b9e4.md) · スコア 9.821429 · 採用条件未達 · 順位差 -0.09497599999999906 / -12.803571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00473fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473fe0.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -15.125 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0096ea4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096ea4c.md) · スコア 7.5 · 採用条件未達 · 順位差 -40.302198 / -15.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a91e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e58.md) · スコア 4.176471 · 採用条件未達 · 順位差 -53.823529 / -18.448529 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) · スコア 3.870968 · 採用条件未達 · 順位差 0.0 / -18.754032 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a6adf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6adf0.md) · スコア 3.797468 · 採用条件未達 · 順位差 -5.130801999999999 / -18.827532 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00689014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689014.md) · スコア 3.180039 · 採用条件未達 · 順位差 -21.897754 / -19.444961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34375,
          0.34375
        ],
        "cfg_coverage": [
          0.1,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 12.625,
        "reverse_margin": 12.803571
      },
      "new": "006f24ac",
      "score": 22.625
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.15625
        ],
        "cfg_coverage": [
          0.0625,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.09497599999999906,
        "reverse_margin": -12.803571
      },
      "new": "0069b9e4",
      "score": 9.821429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21052631578947367,
          0.125
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 7.5,
        "reverse_margin": -15.125
      },
      "new": "00473fe0",
      "score": 7.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-734dd953f798d46d9e362127a4765378"></a>

### v16.0.0 [`0071c598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c598.md) FUN_0071c598

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f25fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25fc.md) · スコア 40.0 · 採用条件未達 · 順位差 11.764706 / 26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f25b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25b8.md) · スコア 13.333333 · 採用条件未達 · 順位差 -0.7843140000000002 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f24ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f24ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.625 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f252c.md) · スコア 0.0 · 採用条件未達 · 順位差 -13.333333 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f2574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2574.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.705882 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35294117647058826,
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
        "margin": 11.764706,
        "reverse_margin": 26.666667
      },
      "new": "006f25fc",
      "score": 40.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23529411764705882,
          0.2222222222222222
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
        "margin": -0.7843140000000002,
        "reverse_margin": -26.666667
      },
      "new": "006f25b8",
      "score": 13.333333
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
        "margin": -22.625,
        "reverse_margin": -40.0
      },
      "new": "006f24ac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a5b30198884a43937e59c0d87030f4fc"></a>

### v16.0.0 [`0071c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c5e0.md) FUN_0071c5e0

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f25fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25fc.md) · スコア 28.235294 · 採用条件未達 · 順位差 -11.764706 / 3.5294120000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2574.md) · スコア 24.705882 · 採用条件未達 · 順位差 0.0 / -3.5294120000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f252c.md) · スコア 6.666667 · 採用条件未達 · 順位差 -6.666665999999999 / -21.568627 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f24ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f24ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.625 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f25b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25b8.md) · スコア 0.0 · 採用条件未達 · 順位差 -14.117647 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47058823529411764,
          0.47058823529411764
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
        "margin": -11.764706,
        "reverse_margin": 3.5294120000000007
      },
      "new": "006f25fc",
      "score": 28.235294
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4117647058823529,
          0.4117647058823529
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
        "margin": 0.0,
        "reverse_margin": -3.5294120000000007
      },
      "new": "006f2574",
      "score": 24.705882
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.11764705882352941
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
        "margin": -6.666665999999999,
        "reverse_margin": -21.568627
      },
      "new": "006f252c",
      "score": 6.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4d3964b78346e0c640905bca3b2aa5af"></a>

### v16.0.0 [`0071c624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c624.md) FUN_0071c624

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f25b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25b8.md) · スコア 14.117647 · 採用条件未達 · 順位差 0.7843140000000002 / 14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f24ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f24ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.625 / -14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f252c.md) · スコア 0.0 · 採用条件未達 · 順位差 -13.333333 / -14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f2574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2574.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.705882 / -14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f25fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -40.0 / -14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.222222 / -14.117647 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23529411764705882,
          0.23529411764705882
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
        "margin": 0.7843140000000002,
        "reverse_margin": 14.117647
      },
      "new": "006f25b8",
      "score": 14.117647
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
        "margin": -22.625,
        "reverse_margin": -14.117647
      },
      "new": "006f24ac",
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
        "margin": -13.333333,
        "reverse_margin": -14.117647
      },
      "new": "006f252c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dc54ec98903dd0615d12a0646f23771a"></a>

### v16.0.0 [`0071c668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c668.md) FUN_0071c668

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f25fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25fc.md) · スコア 28.235294 · 採用条件未達 · 順位差 -11.764706 / 3.5294120000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2574.md) · スコア 24.705882 · 採用条件未達 · 順位差 0.0 / -3.5294120000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f252c.md) · スコア 0.0 · 採用条件未達 · 順位差 -13.333333 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f25b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25b8.md) · スコア 0.0 · 採用条件未達 · 順位差 -14.117647 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.222222 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.076923 / -28.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47058823529411764,
          0.47058823529411764
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
        "margin": -11.764706,
        "reverse_margin": 3.5294120000000007
      },
      "new": "006f25fc",
      "score": 28.235294
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4117647058823529,
          0.4117647058823529
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
        "reverse_margin": -3.5294120000000007
      },
      "new": "006f2574",
      "score": 24.705882
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
        "margin": -13.333333,
        "reverse_margin": -28.235294
      },
      "new": "006f252c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-db6c1ae58cb3487bcada540d241873fc"></a>

### v16.0.0 [`0071c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c6ac.md) FUN_0071c6ac

`competing_candidates` 

呼出元 8件 [`0071c7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c7f8.md) [`0071c868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c868.md) [`0071c8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c8e0.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006f2640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2640.md) · スコア 23.336996 · 採用条件未達 · 順位差 2.392713999999998 / 6.2600729999999984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 17.076923 · 採用条件未達 · 順位差 -7.6298439999999985 / -6.2600729999999984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f1bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1bc8.md) · スコア 16.129555 · 採用条件未達 · 順位差 -42.71254999999999 / -7.207440999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00ade338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md) · スコア 13.629405 · 採用条件未達 · 順位差 -32.659972 / -9.707590999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008978fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/008978fc.md) · スコア 9.601314 · 採用条件未達 · 順位差 0.9757660000000001 / -13.735681999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006afec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afec0.md) · スコア 9.574177 · 採用条件未達 · 順位差 4.3841030000000005 / -13.762818999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006b0524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0524.md) · スコア 8.877138 · 採用条件未達 · 順位差 0.2515900000000002 / -14.459857999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0069ba70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069ba70.md) · スコア 8.692223 · 採用条件未達 · 順位差 0.08496200000000087 / -14.644772999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32142857142857145,
          0.3253012048192771
        ],
        "cfg_coverage": [
          0.12903225806451613,
          0.10256410256410256
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.392713999999998,
        "reverse_margin": 6.2600729999999984
      },
      "new": "006f2640",
      "score": 23.336996
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.26506024096385544
        ],
        "cfg_coverage": [
          0.21428571428571427,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.6298439999999985,
        "reverse_margin": -6.2600729999999984
      },
      "new": "006f1908",
      "score": 17.076923
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18421052631578946,
          0.25301204819277107
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -42.71254999999999,
        "reverse_margin": -7.207440999999999
      },
      "new": "006f1bc8",
      "score": 16.129555
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-77baa6157243d013cf4605f1c03ad771"></a>

### v16.0.0 [`0071c7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c7f8.md) FUN_0071c7f8

`competing_candidates` 

呼出元 2件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 2件 [`0071c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c6ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 32.222222 · 採用条件未達 · 順位差 1.0317460000000018 / 2.142857000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 30.079365 · 採用条件未達 · 順位差 -21.120635000000004 / -2.142857000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 19.365079 · 採用条件未達 · 順位差 -44.982746999999996 / -12.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 16.222222 · 採用条件未達 · 順位差 -12.854701000000002 / -16.000000000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) · スコア 8.597285 · 採用条件未達 · 順位差 -25.873303 / -23.624937000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b80.md) · スコア 8.571429 · 採用条件未達 · 順位差 -54.761904 / -23.650793 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1d90.md) · スコア 8.275862 · 採用条件未達 · 順位差 -45.103448 / -23.946360000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006f2e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2e2c.md) · スコア 6.818182 · 採用条件未達 · 順位差 -35.01948 / -25.404040000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.16666666666666666,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.0317460000000018,
        "reverse_margin": 2.142857000000003
      },
      "new": "006f2790",
      "score": 32.222222
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.52,
          0.4642857142857143
        ],
        "cfg_coverage": [
          0.2,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.120635000000004,
        "reverse_margin": -2.142857000000003
      },
      "new": "006f1ac0",
      "score": 30.079365
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34782608695652173,
          0.2857142857142857
        ],
        "cfg_coverage": [
          0.25,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -44.982746999999996,
        "reverse_margin": -12.857143
      },
      "new": "006f1b24",
      "score": 19.365079
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd3abdf6de7e0a40058cf18ce270c3f3"></a>

### v16.0.0 [`0071c868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c868.md) FUN_0071c868

`competing_candidates` 

呼出元 4件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 2件 [`0071c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c6ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 29.076923 · 採用条件未達 · 順位差 12.576923 / 13.538461 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1ac0.md) · スコア 15.538462 · 採用条件未達 · 順位差 -35.661538 / -13.538461 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f1b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b24.md) · スコア 15.538462 · 採用条件未達 · 順位差 -48.809363999999995 / -13.538461 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 15.538462 · 採用条件未達 · 順位差 -16.68376 / -13.538461 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) · スコア 10.361991 · 採用条件未達 · 順位差 -24.108597 / -18.714932 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1b80.md) · スコア 8.0 · 採用条件未達 · 順位差 -55.333333 / -21.076923 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f1d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1d90.md) · スコア 8.0 · 採用条件未達 · 順位差 -45.37931 / -21.076923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006f25fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f25fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -40.0 / -29.076923 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.43333333333333335,
          0.43333333333333335
        ],
        "cfg_coverage": [
          0.25,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 12.576923,
        "reverse_margin": 13.538461
      },
      "new": "006f2800",
      "score": 29.076923
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28,
          0.23333333333333334
        ],
        "cfg_coverage": [
          0.2,
          0.07692307692307693
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.661538,
        "reverse_margin": -13.538461
      },
      "new": "006f1ac0",
      "score": 15.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30434782608695654,
          0.23333333333333334
        ],
        "cfg_coverage": [
          0.25,
          0.07692307692307693
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -48.809363999999995,
        "reverse_margin": -13.538461
      },
      "new": "006f1b24",
      "score": 15.538462
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-555dac98cabe7ded38841319c459120d"></a>

### v16.0.0 [`0071c8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c8e0.md) FUN_0071c8e0

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0071c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c6ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f2878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2878.md) · スコア 20.414002 · 採用条件未達 · 順位差 15.417459000000001 / 14.347563000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0062f9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f9cc.md) · スコア 6.066439 · 採用条件未達 · 順位差 -29.344902 / -14.347563000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ecf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecf10.md) · スコア 4.806452 · 採用条件未達 · 順位差 -56.390812 / -15.60755 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) · スコア 4.691244 · 採用条件未達 · 順位差 -0.9590870000000002 / -15.722757999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 5. [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) · スコア 4.613497 · 採用条件未達 · 順位差 -0.12269899999999989 / -15.800505000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`0058e620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e620.md) · スコア 4.0 · 採用条件未達 · 順位差 -0.697775 / -16.414002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 7. [`0058e878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e878.md) · スコア 4.0 · 採用条件未達 · 順位差 -2.6816899999999997 / -16.414002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 8. [`00601cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601cfc.md) · スコア 4.0 · 採用条件未達 · 順位差 -51.928432 / -16.414002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2556179775280899,
          0.2556179775280899
        ],
        "cfg_coverage": [
          0.05384615384615385,
          0.06086956521739131
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 15.417459000000001,
        "reverse_margin": 14.347563000000001
      },
      "new": "006f2878",
      "score": 20.414002
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09900990099009901,
          0.056179775280898875
        ],
        "cfg_coverage": [
          0.06060606060606061,
          0.034782608695652174
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -29.344902,
        "reverse_margin": -14.347563000000001
      },
      "new": "0062f9cc",
      "score": 6.066439
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013440860215053764,
          0.014044943820224719
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -56.390812,
        "reverse_margin": -15.60755
      },
      "new": "007ecf10",
      "score": 4.806452
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aee22d2ade539c9a99d5a824cfbcb24d"></a>

### v16.0.0 [`0071ce70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071ce70.md) FUN_0071ce70

`competing_candidates` 

呼出元 1件 [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f2e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2e08.md) · スコア 26.666667 · 採用条件未達 · 順位差 26.666667 / 26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2790.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.222222 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f2800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2800.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.076923 / -26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.4444444444444444
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
        "margin": 26.666667,
        "reverse_margin": 26.666667
      },
      "new": "006f2e08",
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
        "margin": -32.222222,
        "reverse_margin": -26.666667
      },
      "new": "006f2790",
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
        "margin": -29.076923,
        "reverse_margin": -26.666667
      },
      "new": "006f2800",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d5ca6477d71d34cf5cf17bf72d3387f6"></a>

### v16.0.0 [`0071ce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071ce94.md) FUN_0071ce94

`competing_candidates` 

呼出元 1件 [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006f2e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2e2c.md) · スコア 41.837662 · 採用条件未達 · 順位差 30.122758 / 20.89338 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2640.md) · スコア 20.944282 · 採用条件未達 · 順位差 -2.392713999999998 / -20.89338 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006b5e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md) · スコア 15.986294 · 採用条件未達 · 順位差 -0.0171329999999994 / -25.851368 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0064f68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f68c.md) · スコア 13.590909 · 採用条件未達 · 順位差 -18.567462000000003 / -28.246753000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006f1908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1908.md) · スコア 13.376623 · 採用条件未達 · 順位差 -11.330143999999999 / -28.461039 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007d0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0878.md) · スコア 11.178958 · 採用条件未達 · 順位差 -32.673562 / -30.658704 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0067f030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067f/0067f030.md) · スコア 10.993506 · 採用条件未達 · 順位差 0.7991119999999992 / -30.844156 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0070be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070be0c.md) · スコア 8.181818 · 採用条件未達 · 順位差 -3.3971289999999996 / -33.655844 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5568181818181818,
          0.5568181818181818
        ],
        "cfg_coverage": [
          0.32142857142857145,
          0.375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.122758,
        "reverse_margin": 20.89338
      },
      "new": "006f2e2c",
      "score": 41.837662
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.2727272727272727
        ],
        "cfg_coverage": [
          0.12903225806451613,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.392713999999998,
        "reverse_margin": -20.89338
      },
      "new": "006f2640",
      "score": 20.944282
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22330097087378642,
          0.26136363636363635
        ],
        "cfg_coverage": [
          0.029411764705882353,
          0.041666666666666664
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.0171329999999994,
        "reverse_margin": -25.851368
      },
      "new": "006b5e30",
      "score": 15.986294
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-59870287ac3dab3cf45a58e50469b14f"></a>

### v16.0.0 [`0071cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071cff4.md) FUN_0071cff4

`competing_candidates` 

呼出元 16件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`006db3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md) [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 45.5 · 採用条件未達 · 順位差 -19.5 / 10.5 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) · スコア 35.0 · 採用条件未達 · 順位差 22.5 / -10.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005bbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbc10.md) · スコア 17.222222 · 採用条件未達 · 順位差 -26.027778 / -28.277778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4c10.md) · スコア 13.5 · 採用条件未達 · 順位差 -32.382353 / -32.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00548364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md) · スコア 12.55814 · 採用条件未達 · 順位差 0.0 / -32.94186 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006fed90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed90.md) · スコア 7.605634 · 採用条件未達 · 順位差 -58.87323899999999 / -37.894366 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) · スコア 7.5 · 採用条件未達 · 順位差 -5.0 / -38.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0069de94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de94.md) · スコア 5.046729 · 採用条件未達 · 順位差 0.0 / -40.453271 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7083333333333334,
          0.425
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
        "margin": -19.5,
        "reverse_margin": 10.5
      },
      "new": "006f302c",
      "score": 45.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.55,
          0.55
        ],
        "cfg_coverage": [
          0.1,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 22.5,
        "reverse_margin": -10.5
      },
      "new": "006f2f8c",
      "score": 35.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3125,
          0.25
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.027778,
        "reverse_margin": -28.277778
      },
      "new": "005bbc10",
      "score": 17.222222
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7d2f591a3aec7c0c86b2aaf1b9f17f9"></a>

### v16.0.0 [`0071d094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d094.md) FUN_0071d094

`competing_candidates` 

呼出元 13件 [`0074f350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074f350.md) [`0074f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074f844.md) [`007548d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00754/007548d0.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 65.0 · 採用条件未達 · 順位差 19.5 / 44.027778 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`005bbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbc10.md) · スコア 20.972222 · 採用条件未達 · 順位差 -22.277778 / -44.027778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4c10.md) · スコア 15.882353 · 採用条件未達 · 順位差 -30.0 / -49.117647 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00548364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md) · スコア 12.55814 · 採用条件未達 · 順位差 0.0 / -52.44186 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) · スコア 12.5 · 採用条件未達 · 順位差 3.6764709999999994 / -52.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006f308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f308c.md) · スコア 11.666667 · 採用条件未達 · 順位差 -43.333332999999996 / -53.333332999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) · スコア 11.0 · 採用条件未達 · 順位差 -24.0 / -54.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fed90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed90.md) · スコア 7.605634 · 採用条件未達 · 順位差 -58.87323899999999 / -57.394366 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
          0.75
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
        "margin": 19.5,
        "reverse_margin": 44.027778
      },
      "new": "006f302c",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3125,
          0.4166666666666667
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.277778,
        "reverse_margin": -44.027778
      },
      "new": "005bbc10",
      "score": 20.972222
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2647058823529412,
          0.375
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
        "margin": -30.0,
        "reverse_margin": -49.117647
      },
      "new": "006b4c10",
      "score": 15.882353
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c378b3707857d0126b814da052efe720"></a>

### v16.0.0 [`0071d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d0f4.md) FUN_0071d0f4

`competing_candidates` 

呼出元 25件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0060d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md) [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) [`0064db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f308c.md) · スコア 55.0 · 採用条件未達 · 順位差 36.666667000000004 / 36.988304 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007dce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dce2c.md) · スコア 18.011696 · 採用条件未達 · 順位差 -19.590643 / -36.988304 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007dd0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd0bc.md) · スコア 16.634146 · 採用条件未達 · 順位差 -6.390243999999999 / -38.365854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00960c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00960/00960c9c.md) · スコア 13.170732 · 採用条件未達 · 順位差 -44.195122 / -41.829268 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 12.222222 · 採用条件未達 · 順位差 -52.777778 / -42.777778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) · スコア 9.5 · 採用条件未達 · 順位差 -25.5 / -45.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007dd160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd160.md) · スコア 0.740741 · 採用条件未達 · 順位差 -35.438596 / -54.259259 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005bbfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbfb0.md) · スコア 0.0 · 採用条件未達 · 順位差 -53.913043 / -55.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.25,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.666667000000004,
        "reverse_margin": 36.988304
      },
      "new": "006f308c",
      "score": 55.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2631578947368421,
          0.3333333333333333
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.590643,
        "reverse_margin": -36.988304
      },
      "new": "007dce2c",
      "score": 18.011696
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24390243902439024,
          0.3333333333333333
        ],
        "cfg_coverage": [
          0.1,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.390243999999999,
        "reverse_margin": -38.365854
      },
      "new": "007dd0bc",
      "score": 16.634146
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-290219188ff99e26698f794e64d206af"></a>

### v16.0.0 [`0071d16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d16c.md) FUN_0071d16c

`competing_candidates` 

呼出元 23件 [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) [`00641fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md) [`006a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a7/006a7480.md) [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007dca68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dca68.md) · スコア 36.363636 · 採用条件未達 · 順位差 -8.181818999999997 / 2.517482000000001 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007dcac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcac0.md) · スコア 33.846154 · 採用条件未達 · 順位差 -28.376068000000004 / -2.517482000000001 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f3104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3104.md) · スコア 17.5 · 採用条件未達 · 順位差 5.5 / -18.863636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005bbfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbfb0.md) · スコア 0.0 · 採用条件未達 · 順位差 -53.913043 / -36.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006f1828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1828.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -36.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f1848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1848.md) · スコア 0.0 · 採用条件未達 · 順位差 -47.096774 / -36.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) · スコア 0.0 · 採用条件未達 · 順位差 -51.811414 / -36.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -36.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2727272727272727,
          0.3
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
        "margin": -8.181818999999997,
        "reverse_margin": 2.517482000000001
      },
      "new": "007dca68",
      "score": 36.363636
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23076923076923078,
          0.3
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
        "margin": -28.376068000000004,
        "reverse_margin": -2.517482000000001
      },
      "new": "007dcac0",
      "score": 33.846154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.25
        ],
        "cfg_coverage": [
          0.125,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.5,
        "reverse_margin": -18.863636
      },
      "new": "006f3104",
      "score": 17.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-771f0a24c25e7958bc56a7b14c554d93"></a>

### v16.0.0 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) FUN_0071d1bc

`competing_candidates` 

呼出元 8件 [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`0064db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md) [`00696290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696290.md) [`00698d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d94.md) [`006e9364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9364.md) · 呼出先 17件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00697128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md) [`0071b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b930.md) [`0071e2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md)

- 1. [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) · スコア 18.488943 · 採用条件未達 · 順位差 16.157451 / 16.488943 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) · スコア 2.0 · 採用条件未達 · 順位差 -18.572057 / -16.488943 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24861878453038674,
          0.24861878453038674
        ],
        "cfg_coverage": [
          0.07859078590785908,
          0.11328125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.157451,
        "reverse_margin": 16.488943
      },
      "new": "006f3154",
      "score": 18.488943
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
        "margin": -18.572057,
        "reverse_margin": -16.488943
      },
      "new": "006f1e2c",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d3b6eaaa411258304559ddacbc9510d4"></a>

### v16.0.0 [`0071e2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e2b4.md) FUN_0071e2b4

`competing_candidates` 

呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 3件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)

- 1. [`006f424c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f424c.md) · スコア 34.833333 · 採用条件未達 · 順位差 34.833333 / 20.928571000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aa927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md) · スコア 13.904762 · 採用条件未達 · 順位差 -47.91342 / -20.928571000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md) · スコア 3.54067 · 採用条件未達 · 順位差 -41.842105000000004 / -31.292663000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00886068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886068.md) · スコア 2.255639 · 採用条件未達 · 順位差 -0.9511280000000002 / -32.577694 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006f42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f42ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -36.058743 / -34.833333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006f4724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4724.md) · スコア 0.0 · 採用条件未達 · 順位差 -39.230769 / -34.833333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.525,
          0.525
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.21428571428571427
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.833333,
        "reverse_margin": 20.928571000000005
      },
      "new": "006f424c",
      "score": 34.833333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24242424242424243,
          0.2
        ],
        "cfg_coverage": [
          0.09523809523809523,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -47.91342,
        "reverse_margin": -20.928571000000005
      },
      "new": "00aa927c",
      "score": 13.904762
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.043859649122807015,
          0.125
        ],
        "cfg_coverage": [
          0.045454545454545456,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -41.842105000000004,
        "reverse_margin": -31.292663000000005
      },
      "new": "006f4518",
      "score": 3.54067
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3fbeb3a4b6041519e26482baf2f92ebb"></a>

### v16.0.0 [`0071e354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md) FUN_0071e354

`competing_candidates` 

呼出元 3件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00921948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921948.md) [`0097d818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d818.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)

- 1. [`006f42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f42ec.md) · スコア 36.058743 · 採用条件未達 · 順位差 14.986339000000001 / 11.468578999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md) · スコア 24.590164 · 採用条件未達 · 順位差 -20.792611 / -11.468578999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004d9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md) · スコア 15.241236 · 採用条件未達 · 順位差 0.4304060000000014 / -20.817507 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005ec820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec820.md) · スコア 13.105386 · 採用条件未達 · 順位差 1.5122140000000002 / -22.953357 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005ff11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff11c.md) · スコア 13.105386 · 採用条件未達 · 順位差 1.5122140000000002 / -22.953357 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0044b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b6b0.md) · スコア 10.899297 · 採用条件未達 · 順位差 -1.2201909999999998 / -25.159446 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00557264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md) · スコア 9.915691 · 採用条件未達 · 順位差 -0.6248499999999986 / -26.143051999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004d7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md) · スコア 8.852459 · 採用条件未達 · 順位差 -4.845976 / -27.206284 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5245901639344263,
          0.5245901639344263
        ],
        "cfg_coverage": [
          0.22916666666666666,
          0.3142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.986339000000001,
        "reverse_margin": 11.468578999999998
      },
      "new": "006f42ec",
      "score": 36.058743
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.43859649122807015,
          0.4098360655737705
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
        "margin": -20.792611,
        "reverse_margin": -11.468578999999998
      },
      "new": "006f4518",
      "score": 24.590164
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2462686567164179,
          0.27049180327868855
        ],
        "cfg_coverage": [
          0.023255813953488372,
          0.02857142857142857
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.4304060000000014,
        "reverse_margin": -20.817507
      },
      "new": "004d9c58",
      "score": 15.241236
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f15cb78394d103aea9ffc16e5c3d3efe"></a>

### v16.0.0 [`0071e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md) FUN_0071e580

`competing_candidates` 

呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3baf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3baf8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006f4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md) · スコア 45.382775 · 採用条件未達 · 順位差 20.792611 / 24.310371000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f42ec.md) · スコア 21.072404 · 採用条件未達 · 順位差 -14.986339000000001 / -24.310371000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004d9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md) · スコア 14.81083 · 採用条件未達 · 順位差 -0.4304060000000014 / -30.571945000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005ada74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md) · スコア 13.775835 · 採用条件未達 · 順位差 13.775835 / -31.60694 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005af1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md) · スコア 13.775835 · 採用条件未達 · 順位差 13.775835 / -31.60694 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004d7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md) · スコア 13.698435 · 採用条件未達 · 順位差 3.739553000000001 / -31.684340000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0044b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b6b0.md) · スコア 12.119488 · 採用条件未達 · 順位差 1.2201909999999998 / -33.263287000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005ec820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec820.md) · スコア 11.593172 · 採用条件未達 · 順位差 -1.5122140000000002 / -33.789603 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6578947368421053,
          0.6578947368421053
        ],
        "cfg_coverage": [
          0.29545454545454547,
          0.35135135135135137
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 20.792611,
        "reverse_margin": 24.310371000000004
      },
      "new": "006f4518",
      "score": 45.382775
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3442622950819672,
          0.3684210526315789
        ],
        "cfg_coverage": [
          0.020833333333333332,
          0.02702702702702703
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.986339000000001,
        "reverse_margin": -24.310371000000004
      },
      "new": "006f42ec",
      "score": 21.072404
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23134328358208955,
          0.2719298245614035
        ],
        "cfg_coverage": [
          0.046511627906976744,
          0.05405405405405406
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.4304060000000014,
        "reverse_margin": -30.571945000000003
      },
      "new": "004d9c58",
      "score": 14.81083
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8e1cda26219e69e533518768dcb22fc7"></a>

### v16.0.0 [`0071e78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e78c.md) FUN_0071e78c

`competing_candidates` 

呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 3件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)

- 1. [`006f4724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4724.md) · スコア 39.230769 · 採用条件未達 · 順位差 38.278388 / 39.230769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f424c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f424c.md) · スコア 0.0 · 採用条件未達 · 順位差 -34.833333 / -39.230769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6538461538461539,
          0.6538461538461539
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
        "margin": 38.278388,
        "reverse_margin": 39.230769
      },
      "new": "006f4724",
      "score": 39.230769
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
        "margin": -34.833333,
        "reverse_margin": -39.230769
      },
      "new": "006f424c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e7460005fcaeeb7b4ba17dcca85fb9f3"></a>

### v16.0.0 [`0071e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md) FUN_0071e7f4

`competing_candidates` 

呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 6件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`006f478c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f478c.md) · スコア 48.809524 · 採用条件未達 · 順位差 34.99186 / 31.666667000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md) · スコア 17.142857 · 採用条件未達 · 順位差 11.310709 / -31.666667000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) · スコア 14.285714 · 採用条件未達 · 順位差 2.164073 / -34.523810000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004f6cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6cf4.md) · スコア 13.360324 · 採用条件未達 · 順位差 5.975709 / -35.449200000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005b97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md) · スコア 11.085094 · 採用条件未達 · 順位差 4.8967529999999995 / -37.724430000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00611ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611ad8.md) · スコア 10.416667 · 採用条件未達 · 順位差 2.4166670000000003 / -38.39285700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00adadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md) · スコア 10.416667 · 採用条件未達 · 順位差 7.410592 / -38.39285700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004aa8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md) · スコア 10.196078 · 採用条件未達 · 順位差 3.8802890000000003 / -38.613446 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7301587301587301,
          0.7301587301587301
        ],
        "cfg_coverage": [
          0.3076923076923077,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.99186,
        "reverse_margin": 31.666667000000004
      },
      "new": "006f478c",
      "score": 48.809524
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3050847457627119,
          0.2857142857142857
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
        "margin": 11.310709,
        "reverse_margin": -31.666667000000004
      },
      "new": "00670de0",
      "score": 17.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3488372093023256,
          0.23809523809523808
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
        "margin": 2.164073,
        "reverse_margin": -34.523810000000005
      },
      "new": "0073d968",
      "score": 14.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c775a670f90ec0f6dd995f8ca4f111cd"></a>

### v16.0.0 [`0071e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e92c.md) FUN_0071e92c

`competing_candidates` 

呼出元 6件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00799c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md) [`00819f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819f5c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00937924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md) [`00a6a4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a4a8.md)

- 1. [`006f48c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f48c4.md) · スコア 59.117503 · 採用条件未達 · 順位差 48.828548 / 50.775873 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) · スコア 8.34163 · 採用条件未達 · 順位差 -12.230427 / -50.775873 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006f4b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4b74.md) · スコア 2.790698 · 採用条件未達 · 順位差 -41.324135 / -56.326805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007dd160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd160.md) · スコア 0.0 · 採用条件未達 · 順位差 -36.179337 / -59.117503 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7151162790697675,
          0.7151162790697675
        ],
        "cfg_coverage": [
          0.7105263157894737,
          0.7605633802816901
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 48.828548,
        "reverse_margin": 50.775873
      },
      "new": "006f48c4",
      "score": 59.117503
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09467455621301775,
          0.18604651162790697
        ],
        "cfg_coverage": [
          0.03305785123966942,
          0.056338028169014086
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.230427,
        "reverse_margin": -50.775873
      },
      "new": "006f1e2c",
      "score": 8.34163
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14035087719298245,
          0.046511627906976744
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
        "margin": -41.324135,
        "reverse_margin": -56.326805
      },
      "new": "006f4b74",
      "score": 2.790698
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4756f98cb2090e320a6a37ea8b544b73"></a>

### v16.0.0 [`0071ebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ebdc.md) FUN_0071ebdc

`competing_candidates` 

呼出元 1件 [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) · 呼出先 2件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f4b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4b74.md) · スコア 44.114833 · 採用条件未達 · 順位差 33.588516999999996 / 33.588516999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005bfd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bfd84.md) · スコア 10.526316 · 採用条件未達 · 順位差 -9.985048 / -33.588516999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a96d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96d1c.md) · スコア 10.526316 · 採用条件未達 · 順位差 -32.598684 / -33.588516999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) · スコア 5.806452 · 採用条件未達 · 順位差 -46.004962 / -38.308381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005bf81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bf81c.md) · スコア 4.210526 · 採用条件未達 · 順位差 -31.297494999999998 / -39.904306999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007dc944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc944.md) · スコア 4.210526 · 採用条件未達 · 順位差 -12.932331 / -39.904306999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007dcd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcd28.md) · スコア 4.210526 · 採用条件未達 · 順位差 -28.097166 / -39.904306999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a9c684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9c684.md) · スコア 4.210526 · 採用条件未達 · 順位差 -42.189474 / -39.904306999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6140350877192983,
          0.6140350877192983
        ],
        "cfg_coverage": [
          0.5,
          0.36363636363636365
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.588516999999996,
        "reverse_margin": 33.588516999999996
      },
      "new": "006f4b74",
      "score": 44.114833
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3125,
          0.17543859649122806
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
        "margin": -9.985048,
        "reverse_margin": -33.588516999999996
      },
      "new": "005bfd84",
      "score": 10.526316
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3125,
          0.17543859649122806
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.598684,
        "reverse_margin": -33.588516999999996
      },
      "new": "00a96d1c",
      "score": 10.526316
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b4a4badff3bfc5263f9f2c3965ce66d0"></a>

### v16.0.0 [`0071ecc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ecc0.md) FUN_0071ecc0

`competing_candidates` 

呼出元 43件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`0060d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f4c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4c58.md) · スコア 46.666667 · 採用条件未達 · 順位差 13.666666999999997 / 14.222223 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00500168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/00500168.md) · スコア 32.444444 · 採用条件未達 · 順位差 4.876875999999996 / -14.222223 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007dc9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dc9d0.md) · スコア 26.549708 · 採用条件未達 · 順位差 -21.871345 / -20.116958999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00470da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470da8.md) · スコア 24.444444 · 採用条件未達 · 順位差 8.228228000000001 / -22.222222999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00540d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540d88.md) · スコア 24.444444 · 採用条件未達 · 順位差 14.252136 / -22.222222999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0065efb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065efb0.md) · スコア 19.459459 · 採用条件未達 · 順位差 -14.972973 / -27.207207999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006c06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c06f0.md) · スコア 15.428571 · 採用条件未達 · 順位差 -27.428572000000003 / -31.238096 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0044a524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a524.md) · スコア 9.72973 · 採用条件未達 · 順位差 4.72973 / -36.936937 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.375,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.666666999999997,
        "reverse_margin": 14.222223
      },
      "new": "006f4c58",
      "score": 46.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4827586206896552,
          0.4666666666666667
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.876875999999996,
        "reverse_margin": -14.222223
      },
      "new": "00500168",
      "score": 32.444444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3684210526315789,
          0.4666666666666667
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.871345,
        "reverse_margin": -20.116958999999998
      },
      "new": "007dc9d0",
      "score": 26.549708
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-994156b7b8882542f4b49924a8f70284"></a>

### v16.0.0 [`0071ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ed38.md) FUN_0071ed38

`competing_candidates` 

呼出元 7件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006f4cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4cd0.md) · スコア 38.855769 · 採用条件未達 · 順位差 32.086538000000004 / 33.625 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00911ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00911/00911ba8.md) · スコア 5.230769 · 採用条件未達 · 順位差 -0.2907030000000006 / -33.625 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009daa54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009da/009daa54.md) · スコア 5.230769 · 採用条件未達 · 順位差 -0.2907030000000006 / -33.625 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0096b7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096b/0096b7d8.md) · スコア 4.615385 · 採用条件未達 · 順位差 -2.0512820000000005 / -34.240384000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00984184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984184.md) · スコア 4.615385 · 採用条件未達 · 順位差 -4.195804000000001 / -34.240384000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00888268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888268.md) · スコア 4.577303 · 採用条件未達 · 順位差 3.6862139999999997 / -34.278466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a8c898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c898.md) · スコア 4.307692 · 採用条件未達 · 順位差 -32.123746 / -34.548077 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009d1474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d1/009d1474.md) · スコア 4.022989 · 採用条件未達 · 順位差 -22.891246000000002 / -34.83278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5538461538461539,
          0.5538461538461539
        ],
        "cfg_coverage": [
          0.28125,
          0.3103448275862069
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 32.086538000000004,
        "reverse_margin": 33.625
      },
      "new": "006f4cd0",
      "score": 38.855769
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10429447852760736,
          0.08717948717948718
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
        "margin": -0.2907030000000006,
        "reverse_margin": -33.625
      },
      "new": "00911ba8",
      "score": 5.230769
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10429447852760736,
          0.08717948717948718
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
        "margin": -0.2907030000000006,
        "reverse_margin": -33.625
      },
      "new": "009daa54",
      "score": 5.230769
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1e0b53a067fb38ff7e9da3df561ad703"></a>

### v16.0.0 [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) FUN_00720050

`competing_candidates` 

呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 49件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md)

- 1. [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) · スコア 27.004911 · 採用条件未達 · 順位差 20.647479 / 20.809273 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · スコア 6.195638 · 採用条件未達 · 順位差 -33.791717999999996 / -20.809273 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · スコア 6.127382 · 採用条件未達 · 順位差 -35.897528 / -20.877529 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) · スコア 6.0 · 採用条件未達 · 順位差 -53.739747 / -21.004911 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · スコア 4.325218 · 採用条件未達 · 順位差 -28.288359 / -22.679693 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · スコア 4.064955 · 採用条件未達 · 順位差 -38.536096 / -22.939956 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · スコア 4.05962 · 採用条件未達 · 順位差 -45.027117999999994 / -22.945291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) · スコア 2.241399 · 採用条件未達 · 順位差 -9.518601 / -24.763512 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.29097605893186,
          0.2869596803487105
        ],
        "cfg_coverage": [
          0.10246433203631647,
          0.08936651583710407
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 20.647479,
        "reverse_margin": 20.809273
      },
      "new": "006f5fe8",
      "score": 27.004911
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.002999192525089399,
          0.00944424264438794
        ],
        "cfg_coverage": [
          0.000784313725490196,
          0.0022624434389140274
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -33.791717999999996,
        "reverse_margin": -20.809273
      },
      "new": "00957f9c",
      "score": 6.195638
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0017832375668714088,
          0.0032691609153650564
        ],
        "cfg_coverage": [
          0.0010193679918450561,
          0.0022624434389140274
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -35.897528,
        "reverse_margin": -20.877529
      },
      "new": "008e0bc0",
      "score": 6.127382
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-af8e2980747b19957e74945158d04efe"></a>

### v16.0.0 [`00722bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00722/00722bc0.md) FUN_00722bc0

`competing_candidates` 

呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 24件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md)

- 1. [`006f8ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f8/006f8ac0.md) · スコア 39.34485 · 採用条件未達 · 順位差 34.460235 / 34.806388 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0064a3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064a/0064a3cc.md) · スコア 4.538462 · 採用条件未達 · 順位差 -47.780414 / -34.806388 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00729ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729ff0.md) · スコア 4.461538 · 採用条件未達 · 順位差 -33.063961000000006 / -34.883312000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00a10814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a10/00a10814.md) · スコア 4.423077 · 採用条件未達 · 順位差 -69.45063099999999 / -34.921773 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`005cefb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005cefb4.md) · スコア 2.423077 · 採用条件未達 · 順位差 -44.424642 / -36.921773 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a67360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a67/00a67360.md) · スコア 2.192308 · 採用条件未達 · 順位差 -27.599366 / -37.152542000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5698717948717948,
          0.5698717948717948
        ],
        "cfg_coverage": [
          0.06938775510204082,
          0.0576271186440678
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 34.460235,
        "reverse_margin": 34.806388
      },
      "new": "006f8ac0",
      "score": 39.34485
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015909090909090907,
          0.008974358974358974
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -47.780414,
        "reverse_margin": -34.806388
      },
      "new": "0064a3cc",
      "score": 4.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.026607538802660754,
          0.007692307692307693
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -33.063961000000006,
        "reverse_margin": -34.883312000000004
      },
      "new": "00729ff0",
      "score": 4.461538
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ab59a10d9136d4bc0be995429273ec5c"></a>

### v16.0.0 [`00726f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f08.md) FUN_00726f08

`competing_candidates` 

呼出元 4件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00930278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930278.md) [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`00550984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550984.md)

- 1. [`006fce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fce08.md) · スコア 74.0 · 採用条件未達 · 順位差 6.0 / 6.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006fce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fc/006fce30.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / -6.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9,
          0.9
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
        "margin": 6.0,
        "reverse_margin": 6.0
      },
      "new": "006fce08",
      "score": 74.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8
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
        "margin": 68.0,
        "reverse_margin": -6.0
      },
      "new": "006fce30",
      "score": 68.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-268342a6c8c9d4e95bd56ebe627f0ebd"></a>

### v16.0.0 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) FUN_00727990

`competing_candidates` 

呼出元 37件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006b8a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md) [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b2f3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md) [`00b2f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md)

- 1. [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) · スコア 9.0 · 採用条件未達 · 順位差 5.333333 / 6.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a5cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cf70.md) · スコア 3.0 · 採用条件未達 · 順位差 -51.482759 / -6.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00895118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895118.md) · スコア 0.677966 · 採用条件未達 · 順位差 -7.433145 / -8.322034 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.560748 / -9.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0063edf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063edf8.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.240964 / -9.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0063ef44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ef44.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.945578 / -9.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0063f460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f460.md) · スコア 0.0 · 採用条件未達 · 順位差 -21.152751 / -9.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0063f840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f840.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.136986 / -9.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15,
          0.15
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
        "margin": 5.333333,
        "reverse_margin": 6.0
      },
      "new": "006fd890",
      "score": 9.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15517241379310345,
          0.05
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
        "margin": -51.482759,
        "reverse_margin": -6.0
      },
      "new": "00a5cf70",
      "score": 3.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.011299435028248588,
          0.03333333333333333
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
        "margin": -7.433145,
        "reverse_margin": -8.322034
      },
      "new": "00895118",
      "score": 0.677966
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5920d05e26f4245c2a39cc59e5603dd4"></a>

### v16.0.0 [`00727c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c60.md) FUN_00727c60

`competing_candidates` 

呼出元 3件 [`006650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006650d0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 1件 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md)

- 1. [`006fdb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb60.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "006fdb60",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5ebc679c513ad19b071354009367223b"></a>

### v16.0.0 [`00727c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727c7c.md) FUN_00727c7c

`competing_candidates` 

呼出元 2件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`00a26b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26b68.md) · スコア 50.0 · 採用条件未達 · 順位差 -5.454545000000003 / 15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005bbbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbbc8.md) · スコア 35.0 · 採用条件未達 · 順位差 -21.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fdb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb7c.md) · スコア 20.0 · 採用条件未達 · 順位差 13.617021000000001 / -30.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0082f314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f314.md) · スコア 6.382979 · 採用条件未達 · 順位差 -62.127659 / -43.617021 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006fdb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb60.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5454545454545454,
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
        "margin": -5.454545000000003,
        "reverse_margin": 15.0
      },
      "new": "00a26b68",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
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
        "margin": -21.0,
        "reverse_margin": -15.0
      },
      "new": "005bbbc8",
      "score": 35.0
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
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.617021000000001,
        "reverse_margin": -30.0
      },
      "new": "006fdb7c",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-980195781ff5a24033a9b6086b977179"></a>

### v16.0.0 [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md) FUN_00727cdc

`competing_candidates` 

呼出元 28件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) [`00739e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739e04.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdd28.md) · スコア 68.433735 · 採用条件未達 · 順位差 0.0 / 19.934283 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · スコア 48.499452 · 採用条件未達 · 順位差 0.0 / -19.934283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fde74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fde74.md) · スコア 36.084337 · 採用条件未達 · 順位差 0.0 / -32.349398 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed98c.md) · スコア 3.979592 · 採用条件未達 · 順位差 -53.00314 / -64.454143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0096e480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096e480.md) · スコア 2.946429 · 採用条件未達 · 順位差 -11.964285 / -65.487306 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0066da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md) · スコア 0.872727 · 採用条件未達 · 順位差 -36.069983 / -67.561008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) · スコア 0.0 · 採用条件未達 · 順位差 -9.0 / -68.433735 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fdb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb7c.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -68.433735 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8072289156626506,
          0.8072289156626506
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
        "reverse_margin": 19.934283
      },
      "new": "006fdd28",
      "score": 68.433735
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6265060240963856,
          0.6265060240963856
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -19.934283
      },
      "new": "006fdbdc",
      "score": 48.499452
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5180722891566265,
          0.5180722891566265
        ],
        "cfg_coverage": [
          0.25,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -32.349398
      },
      "new": "006fde74",
      "score": 36.084337
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dd686bd3789f436d0bf945ae3e354555"></a>

### v16.0.0 [`00727e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md) FUN_00727e28

`competing_candidates` 

呼出元 8件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdd28.md) · スコア 68.433735 · 採用条件未達 · 順位差 0.0 / 19.934283 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · スコア 48.499452 · 採用条件未達 · 順位差 0.0 / -19.934283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fde74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fde74.md) · スコア 36.084337 · 採用条件未達 · 順位差 0.0 / -32.349398 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed98c.md) · スコア 3.979592 · 採用条件未達 · 順位差 -53.00314 / -64.454143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0096e480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096e/0096e480.md) · スコア 2.946429 · 採用条件未達 · 順位差 -11.964285 / -65.487306 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0066da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md) · スコア 0.872727 · 採用条件未達 · 順位差 -36.069983 / -67.561008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) · スコア 0.0 · 採用条件未達 · 順位差 -9.0 / -68.433735 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fdb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb7c.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -68.433735 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8072289156626506,
          0.8072289156626506
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
        "reverse_margin": 19.934283
      },
      "new": "006fdd28",
      "score": 68.433735
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6265060240963856,
          0.6265060240963856
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -19.934283
      },
      "new": "006fdbdc",
      "score": 48.499452
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5180722891566265,
          0.5180722891566265
        ],
        "cfg_coverage": [
          0.25,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -32.349398
      },
      "new": "006fde74",
      "score": 36.084337
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8f6308656df29aeeb4126130ec4b5c2f"></a>

### v16.0.0 [`00727f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md) FUN_00727f74

`competing_candidates` 

呼出元 8件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) [`00a35500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fde74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fde74.md) · スコア 28.64635 · 採用条件未達 · 順位差 -7.437986999999996 / 4.337349000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdd28.md) · スコア 24.309001 · 採用条件未達 · 順位差 -44.124734000000004 / -4.337349000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · スコア 21.417434 · 採用条件未達 · 順位差 -27.082017999999998 / -7.228916000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed98c.md) · スコア 4.593407 · 採用条件未達 · 順位差 -52.389325 / -24.052943000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0059c81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c81c.md) · スコア 1.276596 · 採用条件未達 · 順位差 -3.856334 / -27.369754 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0066da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md) · スコア 0.872727 · 採用条件未達 · 順位差 -36.069983 / -27.773623 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) · スコア 0.333333 · 採用条件未達 · 順位差 -8.666667 / -28.313017000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fdb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdb7c.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -28.64635 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4578313253012048,
          0.4578313253012048
        ],
        "cfg_coverage": [
          0.08333333333333333,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.437986999999996,
        "reverse_margin": 4.337349000000003
      },
      "new": "006fde74",
      "score": 28.64635
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3855421686746988,
          0.3855421686746988
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -44.124734000000004,
        "reverse_margin": -4.337349000000003
      },
      "new": "006fdd28",
      "score": 24.309001
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3373493975903614,
          0.3373493975903614
        ],
        "cfg_coverage": [
          0.09090909090909091,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.082017999999998,
        "reverse_margin": -7.228916000000002
      },
      "new": "006fdbdc",
      "score": 21.417434
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dee89e633df74f01fe5a8fc763746066"></a>

### v16.0.0 [`00728710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728710.md) FUN_00728710

`competing_candidates` 

呼出元 6件 [`0082a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082a760.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) [`008f30c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`00a6025c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a6025c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fe610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe610.md) · スコア 41.5311 · 採用条件未達 · 順位差 28.899521 / 30.239234000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00449d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449d9c.md) · スコア 11.291866 · 採用条件未達 · 順位差 -51.833134 / -30.239234000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) · スコア 7.894737 · 採用条件未達 · 順位差 0.7077450000000001 / -33.636363 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007ceacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007ceacc.md) · スコア 3.809524 · 採用条件未達 · 順位差 -0.3000649999999996 / -37.721576 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007cf370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf370.md) · スコア 3.809524 · 採用条件未達 · 順位差 -0.3000649999999996 / -37.721576 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00663784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663784.md) · スコア 3.692308 · 採用条件未達 · 順位差 -0.41728099999999957 / -37.838792000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.631578947368421,
          0.631578947368421
        ],
        "cfg_coverage": [
          0.2,
          0.18181818181818182
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 28.899521,
        "reverse_margin": 30.239234000000003
      },
      "new": "006fe610",
      "score": 41.5311
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1875,
          0.15789473684210525
        ],
        "cfg_coverage": [
          0.125,
          0.09090909090909091
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -51.833134,
        "reverse_margin": -30.239234000000003
      },
      "new": "00449d9c",
      "score": 11.291866
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15625,
          0.13157894736842105
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
        "margin": 0.7077450000000001,
        "reverse_margin": -33.636363
      },
      "new": "0045a030",
      "score": 7.894737
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-05e5b1386d257b20c204d25c38816a8b"></a>

### v16.0.0 [`007287f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007287f8.md) FUN_007287f8

`competing_candidates` 

呼出元 4件 [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) [`006dc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md) [`006dc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc3b0.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fe6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe6f8.md) · スコア 33.921569 · 採用条件未達 · 順位差 14.374057999999998 / 11.568627999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fe7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe7c4.md) · スコア 22.352941 · 採用条件未達 · 順位差 7.058823000000002 / -11.568627999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fea2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fea2c.md) · スコア 8.842105 · 採用条件未達 · 順位差 -18.947369 / -25.079463999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006fe890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe890.md) · スコア 5.825243 · 採用条件未達 · 順位差 -22.788349 / -28.096325999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0063ef44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ef44.md) · スコア 4.705882 · 採用条件未達 · 順位差 -29.239696 / -29.215687 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007d0be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0be0.md) · スコア 1.472393 · 採用条件未達 · 順位差 -41.598987 / -32.449176 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006050b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006050b4.md) · スコア 0.0 · 採用条件未達 · 順位差 -9.815564 / -33.921569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -33.921569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5098039215686274,
          0.5098039215686274
        ],
        "cfg_coverage": [
          0.2,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.374057999999998,
        "reverse_margin": 11.568627999999997
      },
      "new": "006fe6f8",
      "score": 33.921569
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37254901960784315,
          0.37254901960784315
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
        "margin": 7.058823000000002,
        "reverse_margin": -11.568627999999997
      },
      "new": "006fe7c4",
      "score": 22.352941
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14736842105263157,
          0.27450980392156865
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
        "margin": -18.947369,
        "reverse_margin": -25.079463999999998
      },
      "new": "006fea2c",
      "score": 8.842105
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-81e3069014ca1b486a8d0fd45acf08e9"></a>

### v16.0.0 [`007288c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007288c4.md) FUN_007288c4

`competing_candidates` 

呼出元 1件 [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fe6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe6f8.md) · スコア 19.547511 · 採用条件未達 · 順位差 -14.374057999999998 / 4.253393000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fe7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe7c4.md) · スコア 15.294118 · 採用条件未達 · 順位差 -7.058823000000002 / -4.253393000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0054243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054243c.md) · スコア 11.764706 · 採用条件未達 · 順位差 -0.23529399999999967 / -7.782805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007075f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007075f4.md) · スコア 11.764706 · 採用条件未達 · 順位差 -0.2725609999999996 / -7.782805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) · スコア 11.764706 · 採用条件未達 · 順位差 -31.435294000000003 / -7.782805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0056d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d0d0.md) · スコア 10.588235 · 採用条件未達 · 順位差 -48.95722 / -8.959276000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) · スコア 9.166667 · 採用条件未達 · 順位差 0.8333340000000007 / -10.380844 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0070dc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070dc20.md) · スコア 8.0 · 採用条件未達 · 順位差 -4.912820999999999 / -11.547511 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.27450980392156865,
          0.27450980392156865
        ],
        "cfg_coverage": [
          0.2,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.374057999999998,
        "reverse_margin": 4.253393000000001
      },
      "new": "006fe6f8",
      "score": 19.547511
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2549019607843137,
          0.2549019607843137
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
        "margin": -7.058823000000002,
        "reverse_margin": -4.253393000000001
      },
      "new": "006fe7c4",
      "score": 15.294118
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2222222222222222,
          0.19607843137254902
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
        "margin": -0.23529399999999967,
        "reverse_margin": -7.782805
      },
      "new": "0054243c",
      "score": 11.764706
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7eed52302464052ca9c3ef9d3c5451d8"></a>

### v16.0.0 [`00728990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728990.md) FUN_00728990

`competing_candidates` 

呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`006db3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) [`00728b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728b2c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fe890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe890.md) · スコア 28.613592 · 採用条件未達 · 順位差 22.205825 / 22.205825 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) · スコア 6.407767 · 採用条件未達 · 順位差 -2.7589000000000006 / -22.205825 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006fe6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe6f8.md) · スコア 6.407767 · 採用条件未達 · 順位差 -27.513802 / -22.205825 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0054243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054243c.md) · スコア 5.825243 · 採用条件未達 · 順位差 -6.174757 / -22.788349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · スコア 5.825243 · 採用条件未達 · 順位差 -42.674209 / -22.788349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007075f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007075f4.md) · スコア 5.825243 · 採用条件未達 · 順位差 -6.2120239999999995 / -22.788349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0070dc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070dc20.md) · スコア 5.825243 · 採用条件未達 · 順位差 -7.087577999999999 / -22.788349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) · スコア 5.825243 · 採用条件未達 · 順位差 -37.374757 / -22.788349 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4368932038834951,
          0.4368932038834951
        ],
        "cfg_coverage": [
          0.12,
          0.125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 22.205825,
        "reverse_margin": 22.205825
      },
      "new": "006fe890",
      "score": 28.613592
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1527777777777778,
          0.10679611650485436
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
        "margin": -2.7589000000000006,
        "reverse_margin": -22.205825
      },
      "new": "00525f90",
      "score": 6.407767
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21568627450980393,
          0.10679611650485436
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
        "margin": -27.513802,
        "reverse_margin": -22.205825
      },
      "new": "006fe6f8",
      "score": 6.407767
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-47602344b490c2f04f32944d909fa792"></a>

### v16.0.0 [`00728b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728b2c.md) FUN_00728b2c

`competing_candidates` 

呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`00728990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728990.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fea2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fea2c.md) · スコア 27.789474 · 採用条件未達 · 順位差 18.947369 / 18.31579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fe6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe6f8.md) · スコア 9.473684 · 採用条件未達 · 順位差 -24.447885 / -18.31579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fe7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe7c4.md) · スコア 8.210526 · 採用条件未達 · 順位差 -14.142415000000002 / -19.578947999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md) · スコア 7.971104 · 採用条件未達 · 順位差 -28.228896000000002 / -19.818369999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00700df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/00700df0.md) · スコア 6.947368 · 採用条件未達 · 順位差 -3.224061 / -20.842105999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00701060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701060.md) · スコア 6.947368 · 採用条件未達 · 順位差 -3.4870740000000007 / -20.842105999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md) · スコア 6.947368 · 採用条件未達 · 順位差 -3.4870740000000007 / -20.842105999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006fe890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe890.md) · スコア 5.825243 · 採用条件未達 · 順位差 -22.788349 / -21.964230999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4631578947368421,
          0.4631578947368421
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
        "margin": 18.947369,
        "reverse_margin": 18.31579
      },
      "new": "006fea2c",
      "score": 27.789474
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.29411764705882354,
          0.15789473684210525
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
        "margin": -24.447885,
        "reverse_margin": -18.31579
      },
      "new": "006fe6f8",
      "score": 9.473684
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2549019607843137,
          0.1368421052631579
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
        "margin": -14.142415000000002,
        "reverse_margin": -19.578947999999997
      },
      "new": "006fe7c4",
      "score": 8.210526
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d575ed6a8a668e93e6bef4f974f8b22"></a>

### v16.0.0 [`00728ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728ca8.md) FUN_00728ca8

`competing_candidates` 

呼出元 2件 [`0075ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006feba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feba8.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.217391 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · スコア 0.0 · 採用条件未達 · 順位差 -28.695652 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -25.217391,
        "reverse_margin": 0.0
      },
      "new": "006feba8",
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
        "margin": -28.695652,
        "reverse_margin": 0.0
      },
      "new": "006fecac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6ae365805cbca74b7bdbbc2d1c1ca422"></a>

### v16.0.0 [`00728cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728cc8.md) FUN_00728cc8

`competing_candidates` 

呼出元 4件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00ab0be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0be0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`005722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722b8.md) · スコア 4.210526 · 採用条件未達 · 順位差 4.210526 / 4.210526 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`006fe890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe890.md) · スコア 0.0 · 採用条件未達 · 順位差 -28.613592 / -4.210526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006febc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006febc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -0.631579 / -4.210526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006fecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · スコア 0.0 · 採用条件未達 · 順位差 -28.695652 / -4.210526 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006fed90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed90.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.478873 / -4.210526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.07017543859649122
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.210526,
        "reverse_margin": 4.210526
      },
      "new": "005722b8",
      "score": 4.210526
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
        "margin": -28.613592,
        "reverse_margin": -4.210526
      },
      "new": "006fe890",
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
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -0.631579,
        "reverse_margin": -4.210526
      },
      "new": "006febc8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0b303e2c0a760b83077c72aa36b10fca"></a>

### v16.0.0 [`00728dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728dac.md) FUN_00728dac

`competing_candidates` 

呼出元 2件 [`0075ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · スコア 28.695652 · 採用条件未達 · 順位差 18.260869 / 3.478261 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006feba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feba8.md) · スコア 25.217391 · 採用条件未達 · 順位差 25.217391 / -3.478261 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fed08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed08.md) · スコア 21.176471 · 採用条件未達 · 順位差 -20.352941 / -7.519181 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0058bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bef8.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.05618 / -28.695652 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006febc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006febc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -0.631579 / -28.695652 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006feeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feeac.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.666667 / -28.695652 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md) · スコア 0.0 · 採用条件未達 · 順位差 -71.818182 / -28.695652 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007dd3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd3e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.5 / -28.695652 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4782608695652174,
          0.4782608695652174
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
        "margin": 18.260869,
        "reverse_margin": 3.478261
      },
      "new": "006fecac",
      "score": 28.695652
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.08695652173913043
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
        "margin": 25.217391,
        "reverse_margin": -3.478261
      },
      "new": "006feba8",
      "score": 25.217391
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35294117647058826,
          0.5217391304347826
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
        "margin": -20.352941,
        "reverse_margin": -7.519181
      },
      "new": "006fed08",
      "score": 21.176471
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f332ba348d610ea61d0147aaa21286f3"></a>

### v16.0.0 [`00728e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e08.md) FUN_00728e08

`competing_candidates` 

呼出元 6件 [`00728fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728fd0.md) [`007290c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) [`0074be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074be70.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 3件 [`00728e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fed08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed08.md) · スコア 41.529412 · 採用条件未達 · 順位差 20.352941 / 32.705883 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · スコア 8.823529 · 採用条件未達 · 順位差 -19.872123 / -32.705883 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006feeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feeac.md) · スコア 7.058824 · 採用条件未達 · 順位差 -59.607843 / -34.470588 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) · スコア 3.225806 · 採用条件未達 · 順位差 0.0 / -38.303606 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007d2a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2a98.md) · スコア 3.076923 · 採用条件未達 · 順位差 -10.787120000000002 / -38.452489 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007d27e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d27e0.md) · スコア 3.0 · 採用条件未達 · 順位差 -50.0 / -38.529412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007d2920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2920.md) · スコア 2.553191 · 採用条件未達 · 順位差 -20.903436999999997 / -38.976221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007d2bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2bd0.md) · スコア 1.983471 · 採用条件未達 · 順位差 -8.947451000000001 / -39.545941 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5588235294117647,
          0.5588235294117647
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
        "margin": 20.352941,
        "reverse_margin": 32.705883
      },
      "new": "006fed08",
      "score": 41.529412
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21739130434782608,
          0.14705882352941177
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
        "margin": -19.872123,
        "reverse_margin": -32.705883
      },
      "new": "006fecac",
      "score": 8.823529
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.11764705882352941
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
        "margin": -59.607843,
        "reverse_margin": -34.470588
      },
      "new": "006feeac",
      "score": 7.058824
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-efdbcb61773ccba35e914336df7c6af9"></a>

### v16.0.0 [`00728e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e90.md) FUN_00728e90

`competing_candidates` 

呼出元 3件 [`00728e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e08.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006fed90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed90.md) · スコア 66.478873 · 採用条件未達 · 順位差 58.87323899999999 / 58.87323899999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00548364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md) · スコア 7.605634 · 採用条件未達 · 順位差 -4.952506 / -58.87323899999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005bbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbc10.md) · スコア 7.605634 · 採用条件未達 · 順位差 -35.644366 / -58.87323899999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006f302c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f302c.md) · スコア 7.605634 · 採用条件未達 · 順位差 -57.394366 / -58.87323899999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0069de94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de94.md) · スコア 5.046729 · 採用条件未達 · 順位差 0.0 / -61.432143999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) · スコア 4.225352 · 採用条件未達 · 順位差 -30.774648 / -62.25352099999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006febc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006febc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -0.631579 / -66.478873 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · スコア 0.0 · 採用条件未達 · 順位差 -28.695652 / -66.478873 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7746478873239436,
          0.7746478873239436
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
        "margin": 58.87323899999999,
        "reverse_margin": 58.87323899999999
      },
      "new": "006fed90",
      "score": 66.478873
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20930232558139536,
          0.1267605633802817
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
        "margin": -4.952506,
        "reverse_margin": -58.87323899999999
      },
      "new": "00548364",
      "score": 7.605634
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28125,
          0.1267605633802817
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
        "margin": -35.644366,
        "reverse_margin": -58.87323899999999
      },
      "new": "005bbc10",
      "score": 7.605634
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fb3a4a0e3a0dafede4719e82cb039cee"></a>

### v16.0.0 [`00728fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728fac.md) FUN_00728fac

`competing_candidates` 

呼出元 4件 [`0075ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 0件 

- 1. [`006feeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feeac.md) · スコア 66.666667 · 採用条件未達 · 順位差 59.607843 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 59.607843,
        "reverse_margin": 66.666667
      },
      "new": "006feeac",
      "score": 66.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e829ad849caf94767e20739473b834de"></a>

### v16.0.0 [`00728fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728fd0.md) FUN_00728fd0

`competing_candidates` 

呼出元 1件 [`007290c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) · 呼出先 2件 [`00728e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006feed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006feed0.md) · スコア 33.870968 · 採用条件未達 · 順位差 25.161291 / 25.161291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006ba3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006ba3cc.md) · スコア 8.709677 · 採用条件未達 · 順位差 -51.935484 / -25.161291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0070db34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070db34.md) · スコア 8.709677 · 採用条件未達 · 順位差 -0.4428650000000012 / -25.161291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005bf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bf9d0.md) · スコア 8.307692 · 採用条件未達 · 順位差 -23.490385 / -25.563276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0063f840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f840.md) · スコア 7.39726 · 採用条件未達 · 順位差 -62.73972599999999 / -26.473708 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00baaa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md) · スコア 5.647059 · 採用条件未達 · 順位差 5.647059 / -28.223909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) · スコア 4.83871 · 採用条件未達 · 順位差 -39.706745 / -29.032258 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) · スコア 0.0 · 採用条件未達 · 順位差 -12.5 / -33.870968 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5645161290322581,
          0.5645161290322581
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
        "margin": 25.161291,
        "reverse_margin": 25.161291
      },
      "new": "006feed0",
      "score": 33.870968
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2903225806451613,
          0.14516129032258066
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
        "margin": -51.935484,
        "reverse_margin": -25.161291
      },
      "new": "006ba3cc",
      "score": 8.709677
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15254237288135594,
          0.14516129032258066
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
        "margin": -0.4428650000000012,
        "reverse_margin": -25.161291
      },
      "new": "0070db34",
      "score": 8.709677
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ccaef06c502b88248f1b3509c626f8a2"></a>

### v16.0.0 [`00729a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729a64.md) FUN_00729a64

`competing_candidates` 

呼出元 2件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00787d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

- 1. [`006ff964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ff964.md) · スコア 30.251414 · 採用条件未達 · 順位差 25.310238000000002 / 25.310238000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) · スコア 4.941176 · 採用条件未達 · 順位差 -56.0 / -25.310238000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008b89f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b89f8.md) · スコア 4.834763 · 採用条件未達 · 順位差 -50.072041 / -25.416651 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a91b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91b1c.md) · スコア 0.405405 · 採用条件未達 · 順位差 -36.996657 / -29.846009000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008a8630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md) · スコア 0.333333 · 採用条件未達 · 順位差 -1.0 / -29.918081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007f64ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f64ac.md) · スコア 0.331492 · 採用条件未達 · 順位差 -6.231447 / -29.919922 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4189189189189189,
          0.4189189189189189
        ],
        "cfg_coverage": [
          0.2558139534883721,
          0.36666666666666664
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.310238000000002,
        "reverse_margin": 25.310238000000002
      },
      "new": "006ff964",
      "score": 30.251414
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08235294117647059,
          0.0945945945945946
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
        "margin": -56.0,
        "reverse_margin": -25.310238000000002
      },
      "new": "006bacc8",
      "score": 4.941176
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06037735849056604,
          0.10810810810810811
        ],
        "cfg_coverage": [
          0.06060606060606061,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -50.072041,
        "reverse_margin": -25.416651
      },
      "new": "008b89f8",
      "score": 4.834763
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a92ce431cb29477078f61c3628eb3b54"></a>

### v16.0.0 [`00729cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729cb4.md) FUN_00729cb4

`competing_candidates` 

呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00801ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801ef8.md) [`00801f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801f48.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`006ffbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ffbb4.md) · スコア 26.123711 · 採用条件未達 · 順位差 14.226804 / 15.228821 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007e8204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8204.md) · スコア 10.89489 · 採用条件未達 · 順位差 -54.898213 / -15.228821 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0088fcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fcf8.md) · スコア 8.659794 · 採用条件未達 · 順位差 -3.5277060000000002 / -17.463917000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005530c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md) · スコア 8.191911 · 採用条件未達 · 順位差 -0.5201770000000003 / -17.931800000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) · スコア 8.09375 · 採用条件未達 · 順位差 0.353618 / -18.029961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0045c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md) · スコア 8.041237 · 採用条件未達 · 順位差 0.3745700000000003 / -18.082473999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0063e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e910.md) · スコア 7.42268 · 採用条件未達 · 順位差 3.4882539999999995 / -18.701031 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) · スコア 6.804124 · 採用条件未達 · 順位差 -0.42479200000000006 / -19.319587 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4020618556701031,
          0.4020618556701031
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
        "margin": 14.226804,
        "reverse_margin": 15.228821
      },
      "new": "006ffbb4",
      "score": 26.123711
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13218390804597702,
          0.23711340206185566
        ],
        "cfg_coverage": [
          0.04819277108433735,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -54.898213,
        "reverse_margin": -15.228821
      },
      "new": "007e8204",
      "score": 10.89489
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.14432989690721648
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
        "margin": -3.5277060000000002,
        "reverse_margin": -17.463917000000002
      },
      "new": "0088fcf8",
      "score": 8.659794
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e862b81958697464d13d4f33a98976b2"></a>

### v16.0.0 [`00729e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) FUN_00729e38

`competing_candidates` 

呼出元 1件 [`0072ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ace0.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0072a2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072a2dc.md) [`0072aaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aaac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`006ffd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ffd38.md) · スコア 44.870226 · 採用条件未達 · 順位差 41.904447000000005 / 43.501405000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009d62e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d62e0.md) · スコア 1.368821 · 採用条件未達 · 順位差 -7.396801 / -43.501405000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007e5734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5734.md) · スコア 1.22449 · 採用条件未達 · 順位差 -36.575854 / -43.645736 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00492db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md) · スコア 1.140684 · 採用条件未達 · 順位差 -4.402794 / -43.729542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0065e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e0a0.md) · スコア 1.140684 · 採用条件未達 · 順位差 -3.1862389999999996 / -43.729542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009d3360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d3/009d3360.md) · スコア 1.140684 · 採用条件未達 · 順位差 -6.2066349999999995 / -43.729542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007d55c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d5/007d55c8.md) · スコア 0.926054 · 採用条件未達 · 順位差 -3.020842 / -43.944172 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008adfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008adfe8.md) · スコア 0.505263 · 採用条件未達 · 順位差 -3.2433319999999997 / -44.364963 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6463878326996197,
          0.6463878326996197
        ],
        "cfg_coverage": [
          0.3111111111111111,
          0.30434782608695654
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 41.904447000000005,
        "reverse_margin": 43.501405000000005
      },
      "new": "006ffd38",
      "score": 44.870226
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04,
          0.022813688212927757
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
        "margin": -7.396801,
        "reverse_margin": -43.501405000000005
      },
      "new": "009d62e0",
      "score": 1.368821
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02040816326530612,
          0.022813688212927757
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
        "margin": -36.575854,
        "reverse_margin": -43.645736
      },
      "new": "007e5734",
      "score": 1.22449
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1c6f4bfcae0cb579b3efeedf18ffb442"></a>

### v16.0.0 [`0072a2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072a2dc.md) FUN_0072a2dc

`competing_candidates` 

呼出元 2件 [`00729e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) [`0072aaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aaac.md) · 呼出先 10件 [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0063dc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dc88.md) [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`0072ada0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ada0.md) [`00794134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794134.md)

- 1. [`007001dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/007001dc.md) · スコア 41.173459 · 採用条件未達 · 順位差 39.044023 / 39.044023 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a9ea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9ea40.md) · スコア 2.129436 · 採用条件未達 · 順位差 -32.07793 / -39.044023 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00667814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00667/00667814.md) · スコア 1.815681 · 採用条件未達 · 順位差 -1.8349379999999997 / -39.357778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007009ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/007009ac.md) · スコア 1.47688 · 採用条件未達 · 順位差 -41.981453 / -39.696579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a9fbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9fbcc.md) · スコア 1.127349 · 採用条件未達 · 順位差 -25.822375 / -40.04611 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00458f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md) · スコア 0.501044 · 採用条件未達 · 順位差 -8.707030999999999 / -40.672415 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007013b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/007013b8.md) · スコア 0.501044 · 採用条件未達 · 順位差 0.501044 / -40.672415 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008f5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f5270.md) · スコア 0.125261 · 採用条件未達 · 順位差 -8.511136 / -41.048198 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5615866388308977,
          0.5615866388308977
        ],
        "cfg_coverage": [
          0.3739130434782609,
          0.42574257425742573
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 39.044023,
        "reverse_margin": 39.044023
      },
      "new": "007001dc",
      "score": 41.173459
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03854875283446712,
          0.03549060542797495
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
        "margin": -32.07793,
        "reverse_margin": -39.044023
      },
      "new": "00a9ea40",
      "score": 2.129436
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.030261348005502064,
          0.04592901878914405
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
        "margin": -1.8349379999999997,
        "reverse_margin": -39.357778
      },
      "new": "00667814",
      "score": 1.815681
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7c2aca26fad92342936b79f0b96f5de9"></a>

### v16.0.0 [`0072aaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aaac.md) FUN_0072aaac

`competing_candidates` 

呼出元 1件 [`00729e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0072a2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072a2dc.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007009ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/007009ac.md) · スコア 43.458333 · 採用条件未達 · 順位差 33.064051000000006 / 34.558333000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a5fea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md) · スコア 8.9 · 採用条件未達 · 順位差 2.1000000000000005 / -34.558333000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006b294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md) · スコア 8.354167 · 採用条件未達 · 順位差 0.03989100000000079 / -35.104166000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00905634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905634.md) · スコア 6.124743 · 採用条件未達 · 順位差 2.1977049999999996 / -37.33359 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md) · スコア 4.737341 · 採用条件未達 · 順位差 -2.691871 / -38.720992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00983810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md) · スコア 4.53125 · 採用条件未達 · 順位差 4.53125 / -38.927083 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004cf4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf4d8.md) · スコア 3.229167 · 採用条件未達 · 順位差 3.229167 / -40.229166000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0055b540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b540.md) · スコア 2.34375 · 採用条件未達 · 順位差 -0.9895830000000001 / -41.114583 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.53125,
          0.53125
        ],
        "cfg_coverage": [
          0.48936170212765956,
          0.4791666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.064051000000006,
        "reverse_margin": 34.558333000000005
      },
      "new": "007009ac",
      "score": 43.458333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.0859375
        ],
        "cfg_coverage": [
          0.15384615384615385,
          0.125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 2.1000000000000005,
        "reverse_margin": -34.558333000000005
      },
      "new": "00a5fea4",
      "score": 8.9
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14084507042253522,
          0.078125
        ],
        "cfg_coverage": [
          0.19047619047619047,
          0.08333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.03989100000000079,
        "reverse_margin": -35.104166000000006
      },
      "new": "006b294c",
      "score": 8.354167
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e6057b92a8d121cb7318f31699a28f97"></a>

### v16.0.0 [`0072b01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b01c.md) FUN_0072b01c

`competing_candidates` 

呼出元 4件 [`0072ada0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ada0.md) [`0072aef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aef0.md) [`0072b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b104.md) [`0072b160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b160.md) · 呼出先 0件 

- 1. [`00700f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00700/00700f1c.md) · スコア 43.87931 · 採用条件未達 · 順位差 43.87931 / 43.87931 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6896551724137931,
          0.6896551724137931
        ],
        "cfg_coverage": [
          0.13043478260869565,
          0.125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 43.87931,
        "reverse_margin": 43.87931
      },
      "new": "00700f1c",
      "score": 43.87931
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fb1b3f3028fe65311137e767ccd83d95"></a>

### v16.0.0 [`0072ba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072ba5c.md) FUN_0072ba5c

`competing_candidates` 

呼出元 1件 [`0072b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b264.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`0070195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/0070195c.md) · スコア 48.944444 · 採用条件未達 · 順位差 41.66959 / 41.277777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0045c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c484.md) · スコア 7.666667 · 採用条件未達 · 順位差 -0.3745700000000003 / -41.277777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006ffbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ffbb4.md) · スコア 6.242894 · 採用条件未達 · 順位差 -19.880817 / -42.70155 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0088fcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fcf8.md) · スコア 6.222222 · 採用条件未達 · 順位差 -5.965278 / -42.722221999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) · スコア 5.777778 · 採用条件未達 · 順位差 -55.854875 / -43.166666 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) · スコア 5.777778 · 採用条件未達 · 順位差 -2.3159720000000004 / -43.166666 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0047a520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a520.md) · スコア 2.666667 · 採用条件未達 · 順位差 -8.102564 / -46.277777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) · スコア 2.222222 · 採用条件未達 · 順位差 -68.181004 / -46.722221999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.674074074074074,
          0.674074074074074
        ],
        "cfg_coverage": [
          0.4473684210526316,
          0.425
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 41.66959,
        "reverse_margin": 41.277777
      },
      "new": "0070195c",
      "score": 48.944444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.234375,
          0.1111111111111111
        ],
        "cfg_coverage": [
          0.18181818181818182,
          0.05
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.3745700000000003,
        "reverse_margin": -41.277777
      },
      "new": "0045c484",
      "score": 7.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13402061855670103,
          0.0962962962962963
        ],
        "cfg_coverage": [
          0.023255813953488372,
          0.025
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.880817,
        "reverse_margin": -42.70155
      },
      "new": "006ffbb4",
      "score": 6.242894
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-caceef059d3fa6b635cc8ed4ce00eecc"></a>

### v16.0.0 [`0072bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bd38.md) FUN_0072bd38

`competing_candidates` 

呼出元 1件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`00701c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701c38.md) · スコア 51.305903 · 採用条件未達 · 順位差 36.320148 / 35.703741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006fb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fb130.md) · スコア 15.602162 · 採用条件未達 · 順位差 1.3923050000000003 / -35.703741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009d5d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5d14.md) · スコア 8.944544 · 採用条件未達 · 順位差 -4.242269 / -42.361359 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0099d9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d9e8.md) · スコア 7.966607 · 採用条件未達 · 順位差 -3.7366899999999994 / -43.339296000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00adf924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf924.md) · スコア 6.666667 · 採用条件未達 · 順位差 -7.257574999999999 / -44.639236 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00701e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701e0c.md) · スコア 5.365854 · 採用条件未達 · 順位差 -44.989368 / -45.940049 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`004dc168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md) · スコア 4.615385 · 採用条件未達 · 順位差 -6.053380000000001 / -46.690518 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004f11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) · スコア 4.615385 · 採用条件未達 · 順位差 -5.511444000000001 / -46.690518 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6923076923076923,
          0.6923076923076923
        ],
        "cfg_coverage": [
          0.525,
          0.4883720930232558
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.320148,
        "reverse_margin": 35.703741
      },
      "new": "00701c38",
      "score": 51.305903
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.224,
          0.23931623931623933
        ],
        "cfg_coverage": [
          0.10810810810810811,
          0.18604651162790697
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.3923050000000003,
        "reverse_margin": -35.703741
      },
      "new": "006fb130",
      "score": 15.602162
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.10256410256410256
        ],
        "cfg_coverage": [
          0.3157894736842105,
          0.13953488372093023
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -4.242269,
        "reverse_margin": -42.361359
      },
      "new": "009d5d14",
      "score": 8.944544
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-674328608335aa610e745585166ee262"></a>

### v16.0.0 [`0072bf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bf0c.md) FUN_0072bf0c

`competing_candidates` 

呼出元 6件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00741590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741590.md) [`009222f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/009222f8.md) [`0092472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d05c.md) [`0067682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md)

- 1. [`00701e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701e0c.md) · スコア 50.355222 · 採用条件未達 · 順位差 37.131232 / 30.794245999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0072e494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e494.md) · スコア 19.560976 · 採用条件未達 · 順位差 -33.873744 / -30.794245999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0078cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cc00.md) · スコア 13.219512 · 採用条件未達 · 順位差 7.490698 / -37.135709999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005b64fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b64fc.md) · スコア 12.825321 · 採用条件未達 · 順位差 -18.985726 / -37.529900999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0072e1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e1d0.md) · スコア 11.268293 · 採用条件未達 · 順位差 5.539479 / -39.086929 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) · スコア 8.693182 · 採用条件未達 · 順位差 -1.125 / -41.66204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007d3a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d3/007d3a14.md) · スコア 8.318182 · 採用条件未達 · 順位差 -28.545454 / -42.03704 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007d400c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d400c.md) · スコア 7.780952 · 採用条件未達 · 順位差 -23.626985 / -42.57427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6178861788617886,
          0.6178861788617886
        ],
        "cfg_coverage": [
          0.5789473684210527,
          0.5641025641025641
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 37.131232,
        "reverse_margin": 30.794245999999998
      },
      "new": "00701e0c",
      "score": 50.355222
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3431372549019608,
          0.2845528455284553
        ],
        "cfg_coverage": [
          0.024390243902439025,
          0.02564102564102564
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.873744,
        "reverse_margin": -30.794245999999998
      },
      "new": "0072e494",
      "score": 19.560976
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.18699186991869918
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
        "margin": 7.490698,
        "reverse_margin": -37.135709999999996
      },
      "new": "0078cc00",
      "score": 13.219512
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-80e7c5c57eeb6ae5ea3c6b75a8a7379a"></a>

### v16.0.0 [`0072c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c804.md) FUN_0072c804

`competing_candidates` [`00702704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702704.md)

呼出元 3件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0072c474",
    "0072c80c",
    "00702374",
    "0070270c"
  ],
  "initial_reason": ""
}
~~~

<a id="review-017196b33bd46777e779e02b1d76870a"></a>

### v16.0.0 [`0072c86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c86c.md) FUN_0072c86c

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`00731ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`0070276c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070276c.md) · スコア 59.230769 · 採用条件未達 · 順位差 29.230769000000002 / 29.230769000000002 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007027fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007027fc.md) · スコア 30.0 · 採用条件未達 · 順位差 -30.0 / -29.230769000000002 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008546a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008546a8.md) · スコア 17.142857 · 採用条件未達 · 順位差 -54.285714000000006 / -42.087912 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005bc0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc0ac.md) · スコア 8.135593 · 採用条件未達 · 順位差 -20.0 / -51.095176 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0063c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c560.md) · スコア 6.575342 · 採用条件未達 · 順位差 -52.785389 / -52.655427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007d2a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2a98.md) · スコア 6.153846 · 採用条件未達 · 順位差 -7.710197000000001 / -53.076923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007071e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00707/007071e8.md) · スコア 5.263158 · 採用条件未達 · 順位差 -3.560371000000001 / -53.967611000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00840b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840b80.md) · スコア 5.217391 · 採用条件未達 · 順位差 -27.903010000000002 / -54.013378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6538461538461539,
          0.6538461538461539
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
        "margin": 29.230769000000002,
        "reverse_margin": 29.230769000000002
      },
      "new": "0070276c",
      "score": 59.230769
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.19230769230769232
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
        "margin": -30.0,
        "reverse_margin": -29.230769000000002
      },
      "new": "007027fc",
      "score": 30.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
          0.3076923076923077
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
        "margin": -54.285714000000006,
        "reverse_margin": -42.087912
      },
      "new": "008546a8",
      "score": 17.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b96ecf241824ff7f78639b1e102734a2"></a>

### v16.0.0 [`0072c8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md) FUN_0072c8fc

`competing_candidates` 

呼出元 1件 [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007027fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/007027fc.md) · スコア 60.0 · 採用条件未達 · 順位差 30.0 / 30.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0070276c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070276c.md) · スコア 30.0 · 採用条件未達 · 順位差 -29.230769000000002 / -30.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008f4fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f4/008f4fc8.md) · スコア 16.0 · 採用条件未達 · 順位差 -10.086957000000002 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a26c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26c00.md) · スコア 16.0 · 採用条件未達 · 順位差 -43.130435 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a26c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26c70.md) · スコア 16.0 · 採用条件未達 · 順位差 -43.130435 / -44.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00549424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549424.md) · スコア 12.0 · 採用条件未達 · 順位差 0.0 / -48.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00564ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md) · スコア 10.909091 · 採用条件未達 · 順位差 0.0 / -49.090908999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007d27e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d27e0.md) · スコア 6.0 · 採用条件未達 · 順位差 -47.0 / -54.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "007027fc",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19230769230769232,
          0.16666666666666666
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
        "margin": -29.230769000000002,
        "reverse_margin": -30.0
      },
      "new": "0070276c",
      "score": 30.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47058823529411764,
          0.26666666666666666
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -10.086957000000002,
        "reverse_margin": -44.0
      },
      "new": "008f4fc8",
      "score": 16.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6baa3592423460ab2e7983de0d451a2a"></a>

### v16.0.0 [`0072c974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c974.md) FUN_0072c974

`competing_candidates` 

呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00702874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702874.md) · スコア 56.024845 · 採用条件未達 · 順位差 -3.1055899999999994 / 13.043478999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00699448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/00699448.md) · スコア 42.981366 · 採用条件未達 · 順位差 42.981366 / -13.043478999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00815778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815778.md) · スコア 27.962382 · 採用条件未達 · 順位差 27.962382 / -28.062462999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00816068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816068.md) · スコア 27.962382 · 採用条件未達 · 順位差 27.962382 / -28.062462999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0081742c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081742c.md) · スコア 27.582418 · 採用条件未達 · 順位差 22.419288 / -28.442427 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006f012c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f012c.md) · スコア 23.896104 · 採用条件未達 · 順位差 23.896104 / -32.128741 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6956521739130435,
          0.6956521739130435
        ],
        "cfg_coverage": [
          0.8333333333333334,
          0.7142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.1055899999999994,
        "reverse_margin": 13.043478999999998
      },
      "new": "00702874",
      "score": 56.024845
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6111111111111112,
          0.4782608695652174
        ],
        "cfg_coverage": [
          0.8333333333333334,
          0.7142857142857143
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
        "margin": 42.981366,
        "reverse_margin": -13.043478999999998
      },
      "new": "00699448",
      "score": 42.981366
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3448275862068966,
          0.43478260869565216
        ],
        "cfg_coverage": [
          0.36363636363636365,
          0.5714285714285714
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
        "margin": 27.962382,
        "reverse_margin": -28.062462999999997
      },
      "new": "00815778",
      "score": 27.962382
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

