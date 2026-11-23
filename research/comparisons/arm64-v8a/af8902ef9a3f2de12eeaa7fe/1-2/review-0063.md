# v15.7.4 → v16.0.0 · 追加調査 (63)

[一覧の目次](README.md)

<a id="review-d78856051e2b27f623ca992b7d81887c"></a>

### v15.7.4 [`0085c6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6b8.md) FUN_0085c6b8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088f650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f650.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0088f634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f634.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`0088f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f630.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0088f650",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088f634",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088f630",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fd5ba16c0a9b5a73191416fc5c5f2f66"></a>

### v15.7.4 [`0085c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6ec.md) FUN_0085c6ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088f684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f684.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "0088f684",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5dbd06982baa7b3624ded2244d099fec"></a>

### v15.7.4 [`0085c6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c6fc.md) FUN_0085c6fc

`competing_candidates` 

呼出元 1件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) · 呼出先 0件 

- 1. [`0088f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f694.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`0088f684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f684.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "0088f694",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088f684",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d2f3c8db3b495a6bd506a4661d4145b3"></a>

### v15.7.4 [`0085cad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cad4.md) FUN_0085cad4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088fa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa6c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "0088fa6c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8a052a7d8aba4070309c6a88256c7a78"></a>

### v15.7.4 [`0085caf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085caf0.md) FUN_0085caf0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088fa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa88.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0088fa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fa6c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0088fa88",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088fa6c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab2be032511cb2c798a00460267d42ed"></a>

### v15.7.4 [`0085cd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd28.md) FUN_0085cd28

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad74.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`0088fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) · スコア 0.0 · 採用条件未達 · 順位差 -50.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00830bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830bac.md) · スコア 0.0 · 採用条件未達 · 順位差 -50.0 / -27.2 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b09234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09234.md) · スコア 0.0 · 採用条件未達 · 順位差 -50.0 / -5.853659 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "0088fcc0",
      "score": 50.0
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -50.0,
        "reverse_margin": 0.0
      },
      "new": "00440bfc",
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
        "margin": -50.0,
        "reverse_margin": -27.2
      },
      "new": "00830bac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0cbda194164407762cb178e88ce63f77"></a>

### v15.7.4 [`0085cd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd58.md) FUN_0085cd58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088fcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcf0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0088fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "0088fcf0",
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
        "margin": -54.285714,
        "reverse_margin": -50.0
      },
      "new": "0088fcc0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-96fbdc283f256eb57a491e7268f52c48"></a>

### v15.7.4 [`0085cd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd74.md) FUN_0085cd74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088fd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd0c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0088fcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcf0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`0088fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0088fd0c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088fcf0",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088fcc0",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8951e5943ea562a6933af7b1aa6b0bb2"></a>

### v15.7.4 [`0085cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cda8.md) FUN_0085cda8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd40.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "0088fd40",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8409cb138ced2ead1aa0665ffedb6e2c"></a>

### v15.7.4 [`0085cdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cdb8.md) FUN_0085cdb8

`competing_candidates` 

呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 0件 

- 1. [`0088fd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd50.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`0088fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd40.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "0088fd50",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088fd40",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e1fa8390b55ea21bb7945024c9db9acb"></a>

### v15.7.4 [`0085d024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d024.md) FUN_0085d024

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088ffbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffbc.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "0088ffbc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3ae735ccb25ce9ce346e62faa5ef084"></a>

### v15.7.4 [`0085d040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d040.md) FUN_0085d040

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0088ffd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffd8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0088ffbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffbc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0088ffd8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0088ffbc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2099fdac1d1a538e0285aa7d73d59b06"></a>

### v15.7.4 [`0085d278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d278.md) FUN_0085d278

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00890210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890210.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`00890230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890230.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00890214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890214.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "00890210",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00890230",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00890214",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7540e41f8a1e727230b31145609e4f53"></a>

### v15.7.4 [`0085d27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d27c.md) FUN_0085d27c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00890214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890214.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": -25.714286
      },
      "new": "00890214",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a381724eccc221a48310f6221dc3cbe8"></a>

### v15.7.4 [`0085d298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085d/0085d298.md) FUN_0085d298

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00890230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890230.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00890214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890214.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00890210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890210.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00890230",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00890214",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00890210",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-35fcdeff6596844aa48b04e0446d4d5b"></a>

### v15.7.4 [`0085e004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e004.md) FUN_0085e004

`competing_candidates` 

呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008168dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008168dc.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`00822930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822930.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00890f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md) · スコア 37.697959 · 採用条件未達 · 順位差 12.097958999999996 / 19.657142999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004729cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729cc.md) · スコア 25.6 · 採用条件未達 · 順位差 -12.097958999999996 / 25.6 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00890ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890ee4.md) · スコア 6.4 · 採用条件未達 · 順位差 -31.297959 / 6.4 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0084710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/0084710c.md) · スコア 2.4 · 採用条件未達 · 順位差 -35.297959 / -22.540813 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00890710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.697959 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008a5d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5d98.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.697959 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bb7d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.697959 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5466666666666666,
          0.5466666666666666
        ],
        "cfg_coverage": [
          0.3,
          0.24489795918367346
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 12.097958999999996,
        "reverse_margin": 19.657142999999998
      },
      "new": "00890f9c",
      "score": 37.697959
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36,
          0.4576271186440678
        ],
        "cfg_coverage": [
          0.2,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -12.097958999999996,
        "reverse_margin": 25.6
      },
      "new": "004729cc",
      "score": 25.6
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10666666666666667,
          0.17391304347826086
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
        "margin": -31.297959,
        "reverse_margin": 6.4
      },
      "new": "00890ee4",
      "score": 6.4
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ff92dad24a94a7433ad87257989d5e20"></a>

### v15.7.4 [`0085e2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e2f8.md) FUN_0085e2f8

`competing_candidates` 

呼出元 2件 [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) [`00adbc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md) · 呼出先 0件 

- 1. [`0058330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058330c.md) · スコア 80.0 · 採用条件未達 · 順位差 8.571428999999995 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00560fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fa4.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 3. [`00571788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571788.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 4. [`00575378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575378.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 5. [`005753a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753a8.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 6. [`005832dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005832dc.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 7. [`0058cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc40.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 8. [`00891290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891290.md) · スコア 50.714286 · 採用条件未達 · 順位差 -29.285714 / -5.714284999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 8.571428999999995,
        "reverse_margin": 0.0
      },
      "new": "0058330c",
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
          0.5714285714285714,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.571428999999995,
        "reverse_margin": -8.571428999999995
      },
      "new": "00560fa4",
      "score": 71.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          0.5714285714285714,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.571428999999995,
        "reverse_margin": -8.571428999999995
      },
      "new": "00571788",
      "score": 71.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8cb21e238d5b28aa412a53ca26487c28"></a>

### v15.7.4 [`0085f634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f634.md) FUN_0085f634

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008925cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925cc.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 69.0,
        "reverse_margin": 69.0
      },
      "new": "008925cc",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-233175cec5bd7a0728bb55d1eb7e94c4"></a>

### v15.7.4 [`0085f71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f71c.md) FUN_0085f71c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008926b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926b4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008926b4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4eeb3987695278662908935ab4bf400c"></a>

### v15.7.4 [`0085f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f738.md) FUN_0085f738

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008926d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926d0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008926b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926b4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008926dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926dc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008926d0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008926b4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008926dc",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0dea017ce8723d6f5d80715320144423"></a>

### v15.7.4 [`0085f744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f744.md) FUN_0085f744

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008926dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926dc.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`008926d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926d0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008926b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926b4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "008926dc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008926d0",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008926b4",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-135337fe64d6a446bc470524a86af57c"></a>

### v15.7.4 [`0085fb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb04.md) FUN_0085fb04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892a9c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00892a9c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-db9d6bc3cc35887a59edb4e7a1f1c62b"></a>

### v15.7.4 [`0085fb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fb20.md) FUN_0085fb20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892ab8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00892a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892a9c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00892ab8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00892a9c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6bd2ec1621402a96f49081c80344e1b6"></a>

### v15.7.4 [`0085fbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fbb4.md) FUN_0085fbb4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00892b4c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2c525c652b878ccc09da0aab5139d66e"></a>

### v15.7.4 [`0085fbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fbd0.md) FUN_0085fbd0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b68.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00892b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b4c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00892b68",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00892b4c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c3ee828f7851b4efd15054ad1181ed90"></a>

### v15.7.4 [`0085fc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc54.md) FUN_0085fc54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bec.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00892bec",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a467f6c9eab34c4b6e6aef5dc0b20b10"></a>

### v15.7.4 [`0085fc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc70.md) FUN_0085fc70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c08.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00892bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bec.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00892c08",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00892bec",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f32d9f41010eaaaf7a9dbaa8aaf42308"></a>

### v15.7.4 [`0085fd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd04.md) FUN_0085fd04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c9c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00892c9c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-063daf22a0156036aec343ccedaf4bae"></a>

### v15.7.4 [`0085fd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fd20.md) FUN_0085fd20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00892cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cb8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00892c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c9c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00892cb8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00892c9c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9c1dfa9ec96d284897a54d61009230d0"></a>

### v15.7.4 [`008600ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008600ec.md) FUN_008600ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00876028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876028.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00893084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893084.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 0.0
      },
      "new": "00876028",
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
        "reverse_margin": 54.285714
      },
      "new": "00893084",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4b34a802e5c76c5850532b4d5fbc00b4"></a>

### v15.7.4 [`00860108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860108.md) FUN_00860108

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008930a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930a0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00893084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893084.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008930a0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893084",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8ad2001c9c2eba4ddece933b896a0c54"></a>

### v15.7.4 [`0086023c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086023c.md) FUN_0086023c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008931d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008931d4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008931d4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-58b74602b0cefa4e63b369a57415660c"></a>

### v15.7.4 [`00860258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860258.md) FUN_00860258

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008931f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008931f0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008931d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008931d4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008931f0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008931d4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9ca9e7d1fbca59beb278adff1c40d872"></a>

### v15.7.4 [`00860388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860388.md) FUN_00860388

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00893320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893320.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": -25.714286
      },
      "new": "00893320",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cfb3d915d0ec13eed2d7c6d6ada1c3fc"></a>

### v15.7.4 [`008603a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008603a4.md) FUN_008603a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0089333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089333c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00893320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893320.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0089333c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893320",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5d4b8016876e4a7d5f4c84d0e7be0f43"></a>

### v15.7.4 [`00860484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860484.md) FUN_00860484

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0079dbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dbd0.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0089341c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089341c.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 80.0
      },
      "new": "0079dbd0",
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
        "reverse_margin": 54.285714
      },
      "new": "0089341c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a196f6fd2100dcb83c84b3ad9662e081"></a>

### v15.7.4 [`008604a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604a0.md) FUN_008604a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00893438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893438.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0089341c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089341c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "00893438",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0089341c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9a28f7d0744d089cbf6bd48d9e1c88bd"></a>

### v15.7.4 [`008604ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604ec.md) FUN_008604ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00893484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893484.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`008934a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934a4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00893488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893488.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "00893484",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008934a4",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893488",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-86d89248ef4f2262ba50366d23e1981e"></a>

### v15.7.4 [`008604f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008604f0.md) FUN_008604f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00893488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893488.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00893488",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2d38b101c5a34db3ab5a875699b7a71e"></a>

### v15.7.4 [`0086050c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/0086050c.md) FUN_0086050c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008934a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934a4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00893488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893488.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00893484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893484.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008934a4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893488",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893484",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-27e2cbbbc090036f65deaaa20d5dea9e"></a>

### v15.7.4 [`008605c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008605c8.md) FUN_008605c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00893560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893560.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00893560",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0e57e9cb36784eaf0e72461e136d87b"></a>

### v15.7.4 [`008605e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008605e4.md) FUN_008605e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0089357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089357c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00893560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893560.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "0089357c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00893560",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-468dac38e920c1dd45a3f00f7f94a69e"></a>

### v15.7.4 [`00860980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860980.md) FUN_00860980

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f48.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`0080d71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d71c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`0071be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be70.md) · スコア 28.275862 · 採用条件未達 · 順位差 24.137931000000002 / 28.275862 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0089350c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md) · スコア 4.137931 · 採用条件未達 · 順位差 -24.137931000000002 / 4.137931 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00893918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893918.md) · スコア 4.137931 · 採用条件未達 · 順位差 -24.137931000000002 / -26.206896999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008abb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abb80.md) · スコア 4.137931 · 採用条件未達 · 順位差 -24.137931000000002 / -39.862069 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008cf2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf2a8.md) · スコア 4.137931 · 採用条件未達 · 順位差 -24.137931000000002 / 4.137931 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008cf560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf560.md) · スコア 4.137931 · 採用条件未達 · 順位差 -24.137931000000002 / -59.708223 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f292c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md) · スコア 4.0 · 採用条件未達 · 順位差 -24.275862 / -36.909091 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -28.275862 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13793103448275862,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 24.137931000000002,
        "reverse_margin": 28.275862
      },
      "new": "0071be70",
      "score": 28.275862
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06896551724137931,
          0.09523809523809523
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
        "margin": -24.137931000000002,
        "reverse_margin": 4.137931
      },
      "new": "0089350c",
      "score": 4.137931
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06896551724137931,
          0.06896551724137931
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
        "margin": -24.137931000000002,
        "reverse_margin": -26.206896999999998
      },
      "new": "00893918",
      "score": 4.137931
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-59a38563809041cb18bd9dd4a6309c4a"></a>

### v15.7.4 [`008609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008609f4.md) FUN_008609f4

`competing_candidates` 

呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md) [`0046fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`0089398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md) · スコア 40.631897 · 採用条件未達 · 順位差 28.258503000000005 / 28.258503000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) · スコア 12.373394 · 採用条件未達 · 順位差 -28.258503000000005 / 12.373394 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) · スコア 12.373394 · 採用条件未達 · 順位差 -28.258503000000005 / 12.373394 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0087d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d8b0.md) · スコア 7.959184 · 採用条件未達 · 順位差 -32.672713 / 7.959184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · スコア 4.853322 · 採用条件未達 · 順位差 -35.778575000000004 / -41.488243000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) · スコア 2.294118 · 採用条件未達 · 順位差 -38.337779000000005 / -64.588235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) · スコア 0.842105 · 採用条件未達 · 順位差 -39.789792000000006 / -29.911142 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008ad760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad760.md) · スコア 0.304569 · 採用条件未達 · 順位差 -40.327328 / 0.304569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5204081632653061,
          0.5204081632653061
        ],
        "cfg_coverage": [
          0.37037037037037035,
          0.37037037037037035
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 28.258503000000005,
        "reverse_margin": 28.258503000000005
      },
      "new": "0089398c",
      "score": 40.631897
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19387755102040816,
          0.31666666666666665
        ],
        "cfg_coverage": [
          0.037037037037037035,
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
        "margin": -28.258503000000005,
        "reverse_margin": 12.373394
      },
      "new": "00596eec",
      "score": 12.373394
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19387755102040816,
          0.31666666666666665
        ],
        "cfg_coverage": [
          0.037037037037037035,
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
        "margin": -28.258503000000005,
        "reverse_margin": 12.373394
      },
      "new": "00596fdc",
      "score": 12.373394
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e906307da10ccc38ad5dd180092a1fee"></a>

### v15.7.4 [`00860ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860ba8.md) FUN_00860ba8

`competing_candidates` 

呼出元 1件 [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 14件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

- 1. [`00893b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md) · スコア 7.605634 · 採用条件未達 · 順位差 6.338028 / 6.338028 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008ea120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea120.md) · スコア 1.267606 · 採用条件未達 · 順位差 -6.338028 / -64.384568 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0063bc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / -43.234427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0064e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00753fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753fc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / -45.642847 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00785538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785538.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / -31.52381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / -3.859649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007fdf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.605634 / -25.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1267605633802817,
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
        "margin": 6.338028,
        "reverse_margin": 6.338028
      },
      "new": "00893b40",
      "score": 7.605634
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02112676056338028,
          0.06521739130434782
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
        "margin": -6.338028,
        "reverse_margin": -64.384568
      },
      "new": "008ea120",
      "score": 1.267606
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
        "margin": -7.605634,
        "reverse_margin": -43.234427
      },
      "new": "0063bc58",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6555440f979e2fa66268186cb32c7287"></a>

### v15.7.4 [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) FUN_00860de0

`competing_candidates` 

呼出元 0件  · 呼出先 52件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c894.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md)

- 1. [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · スコア 10.873332 · 採用条件未達 · 順位差 8.805432999999999 / 8.873332 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · スコア 2.067899 · 採用条件未達 · 順位差 -8.805432999999999 / -42.429467 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · スコア 2.023758 · 採用条件未達 · 順位差 -8.849574 / -40.001152 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · スコア 2.0 · 採用条件未達 · 順位差 -8.873332 / -26.963011 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · スコア 1.131906 · 採用条件未達 · 順位差 -9.741425999999999 / -29.35026 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · スコア 0.438497 · 採用条件未達 · 順位差 -10.434835 / -16.435792999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1327665140614781,
          0.1326797385620915
        ],
        "cfg_coverage": [
          0.045627376425855515,
          0.05150214592274678
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 8.805432999999999,
        "reverse_margin": 8.873332
      },
      "new": "00893d78",
      "score": 10.873332
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.001962066710268149,
          0.001131648434552999
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
        "margin": -8.805432999999999,
        "reverse_margin": -42.429467
      },
      "new": "00a8e3bc",
      "score": 2.067899
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0013080444735120995,
          0.0003959611958028113
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
        "margin": -8.849574,
        "reverse_margin": -40.001152
      },
      "new": "00914c94",
      "score": 2.023758
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6698bcf5156983b1018010622fc5b3cb"></a>

### v15.7.4 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) FUN_008629ec

`competing_candidates` 

呼出元 0件  · 呼出先 99件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md)

- 1. [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · スコア 16.87429 · 採用条件未達 · 順位差 14.691807999999998 / 12.974317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · スコア 2.182482 · 採用条件未達 · 順位差 -14.691807999999998 / -28.299684 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · スコア 0.403648 · 採用条件未達 · 順位差 -16.470641999999998 / -10.469683999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · スコア 0.40146 · 採用条件未達 · 順位差 -16.47283 / -15.994311 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b1dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1d/00b1dc60.md) · スコア 0.218978 · 採用条件未達 · 順位差 -16.655312 / -42.392347 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · スコア 0.182482 · 採用条件未達 · 順位差 -16.691807999999998 / -32.863067 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18309002433090024,
          0.18309002433090024
        ],
        "cfg_coverage": [
          0.09864603481624758,
          0.09444444444444444
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 14.691807999999998,
        "reverse_margin": 12.974317
      },
      "new": "0089598c",
      "score": 16.87429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0030413625304136255,
          0.004492362982929021
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
        "margin": -14.691807999999998,
        "reverse_margin": -28.299684
      },
      "new": "0089d484",
      "score": 2.182482
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006082725060827251,
          0.006535947712418301
        ],
        "cfg_coverage": [
          0.0019342359767891683,
          0.002145922746781116
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -16.470641999999998,
        "reverse_margin": -10.469683999999999
      },
      "new": "00893d78",
      "score": 0.403648
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d0c839adecb6995e6846c60735060796"></a>

### v15.7.4 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) FUN_008648a8

`competing_candidates` 

呼出元 0件  · 呼出先 57件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md)

- 1. [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · スコア 15.527798 · 採用条件未達 · 順位差 11.117111000000001 / 11.431412000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · スコア 4.410687 · 採用条件未達 · 順位差 -11.117111000000001 / -36.449054999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) · スコア 4.026714 · 採用条件未達 · 順位差 -11.501084 / -7.260108000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · スコア 4.0 · 採用条件未達 · 順位差 -11.527798 / -9.095147 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · スコア 0.347284 · 採用条件未達 · 順位差 -15.180514 / 0.347284 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00641fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md) · スコア 0.213713 · 採用条件未達 · 順位差 -15.314085 / 0.213713 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007548d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00754/007548d0.md) · スコア 0.133571 · 採用条件未達 · 順位差 -15.394227 / 0.133571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00aae348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae348.md) · スコア 0.026714 · 採用条件未達 · 順位差 -15.501084 / -16.289916 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15093499554764025,
          0.14745541539799914
        ],
        "cfg_coverage": [
          0.04121863799283154,
          0.034023668639053255
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.117111000000001,
        "reverse_margin": 11.431412000000002
      },
      "new": "00897848",
      "score": 15.527798
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013802315227070348,
          0.006844778096710091
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.117111000000001,
        "reverse_margin": -36.449054999999994
      },
      "new": "0089e838",
      "score": 4.410687
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0004452359750667854,
          0.0012919896640826874
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.501084,
        "reverse_margin": -7.260108000000001
      },
      "new": "0089a514",
      "score": 4.026714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-159320c1f5aa876fb1425d1b691eda0d"></a>

### v15.7.4 [`008673f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00867/008673f0.md) FUN_008673f0

`competing_candidates` 

呼出元 2件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 14件 [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`006fd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd890.md) [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md)

- 1. [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) · スコア 11.286822 · 採用条件未達 · 順位差 5.286822000000001 / 7.260108000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · スコア 6.0 · 採用条件未達 · 順位差 -5.286822000000001 / -7.095147000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · スコア 4.026098 · 採用条件未達 · 順位差 -7.260724000000001 / -11.5017 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) · スコア 2.0 · 採用条件未達 · 順位差 -9.286822 / -34.909077 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · スコア 2.0 · 採用条件未達 · 順位差 -9.286822 / -66.915851 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b1b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1b/00b1b3c0.md) · スコア 2.0 · 採用条件未達 · 順位差 -9.286822 / -33.308671 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) · スコア 1.085271 · 採用条件未達 · 順位差 -10.201551 / 1.085271 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) · スコア 0.071685 · 採用条件未達 · 順位差 -11.215137 / -45.54982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08656330749354005,
          0.08656330749354005
        ],
        "cfg_coverage": [
          0.005,
          0.004651162790697674
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.286822000000001,
        "reverse_margin": 7.260108000000001
      },
      "new": "0089a514",
      "score": 11.286822
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
      "new": "0093b5d4",
      "score": 6.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0012919896640826874,
          0.00043497172683775554
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.260724000000001,
        "reverse_margin": -11.5017
      },
      "new": "00897848",
      "score": 4.026098
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.4 [`008680dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/008680dc.md) FUN_008680dc

`competing_candidates` 

呼出元 2件 [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 0件 

- 1. [`00604e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e14.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0063dc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dc88.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006be964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006be964.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0091110c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00911/0091110c.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00961550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961550.md) · スコア 66.666667 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`0089b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b200.md) · スコア 46.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00604f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604f64.md) · スコア 40.0 · 採用条件未達 · 順位差 -26.666667000000004 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007c7b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b38.md) · スコア 40.0 · 採用条件未達 · 順位差 -26.666667000000004 / 40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 0.0,
        "reverse_margin": 66.666667
      },
      "new": "00604e14",
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
        "margin": 0.0,
        "reverse_margin": 66.666667
      },
      "new": "0063dc88",
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
        "margin": 0.0,
        "reverse_margin": 66.666667
      },
      "new": "006be964",
      "score": 66.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-027e2fa590ef8bc7853228e42248a9b0"></a>

### v15.7.4 [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) FUN_00868124

`competing_candidates` 

呼出元 0件  · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00428714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

- 1. [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · スコア 13.04498 · 採用条件未達 · 順位差 11.018396000000001 / 10.786658000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · スコア 2.026584 · 採用条件未達 · 順位差 -11.018396000000001 / -26.936427000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) · スコア 1.554404 · 採用条件未達 · 順位差 -11.490576 / 1.554404 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · スコア 1.450777 · 採用条件未達 · 順位差 -11.594203 / -7.383675 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) · スコア 1.450777 · 採用条件未達 · 順位差 -11.594203 / 1.450777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005ace80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md) · スコア 1.243523 · 採用条件未達 · 順位差 -11.801457000000001 / -17.015508 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00666768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md) · スコア 1.036269 · 採用条件未達 · 順位差 -12.008711 / 1.036269 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00666be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md) · スコア 1.036269 · 採用条件未達 · 順位差 -12.008711 / 1.036269 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16580310880829016,
          0.1646655231560892
        ],
        "cfg_coverage": [
          0.061224489795918366,
          0.05825242718446602
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.018396000000001,
        "reverse_margin": 10.786658000000001
      },
      "new": "0089b248",
      "score": 13.04498
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0017271157167530224,
          0.00044306601683650863
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
        "margin": -11.018396000000001,
        "reverse_margin": -26.936427000000002
      },
      "new": "00856dec",
      "score": 2.026584
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025906735751295335,
          0.08522727272727272
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
        "margin": -11.490576,
        "reverse_margin": 1.554404
      },
      "new": "008856e4",
      "score": 1.554404
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-16882862488cda55d2b7575e1a3e82ea"></a>

### v15.7.4 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) FUN_00868b14

`competing_candidates` 

呼出元 0件  · 呼出先 69件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md)

- 1. [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · スコア 16.395771 · 採用条件未達 · 順位差 9.246766000000001 / 14.395771 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · スコア 7.149005 · 採用条件未達 · 順位差 -9.246766000000001 / -36.646007999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00acc3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc3d4.md) · スコア 6.107962 · 採用条件未達 · 順位差 -10.287809 / -19.748177 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00adf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00adf/00adf01c.md) · スコア 4.4 · 採用条件未達 · 順位差 -11.995771 / -0.7815069999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · スコア 3.899973 · 採用条件未達 · 順位差 -12.495798 / -12.974317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00658d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658d6c.md) · スコア 3.895278 · 採用条件未達 · 順位差 -12.500493 / -23.119999999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0065ad00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065a/0065ad00.md) · スコア 3.499254 · 採用条件未達 · 順位差 -12.896517 / -30.385174 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009bf53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md) · スコア 2.999254 · 採用条件未達 · 順位差 -13.396517 / -35.245945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1925,
          0.29653401797175866
        ],
        "cfg_coverage": [
          0.04228855721393035,
          0.058823529411764705
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 9.246766000000001,
        "reverse_margin": 14.395771
      },
      "new": "0089c00c",
      "score": 16.395771
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015833333333333335,
          0.01890547263681592
        ],
        "cfg_coverage": [
          0.009950248756218905,
          0.011560693641618497
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.246766000000001,
        "reverse_margin": -36.646007999999995
      },
      "new": "008278d8",
      "score": 7.149005
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0033333333333333335,
          0.001799370220422852
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.287809,
        "reverse_margin": -19.748177
      },
      "new": "00acc3d4",
      "score": 6.107962
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-197347a78af7e7f0ee8c40dc48741bbb"></a>

### v15.7.4 [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) FUN_0086a350

`competing_candidates` 

呼出元 0件  · 呼出先 54件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0044fcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fce4.md)

- 1. [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · スコア 30.482166 · 採用条件未達 · 順位差 27.718783 / 28.182166 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · スコア 2.763383 · 採用条件未達 · 順位差 -27.718783 / -37.334398 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009ee198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009ee198.md) · スコア 2.318866 · 採用条件未達 · 順位差 -28.1633 / -10.14517 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · スコア 2.145985 · 採用条件未達 · 順位差 -28.336181 / -14.728304999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · スコア 1.116553 · 採用条件未達 · 順位差 -29.365613 / -9.756779 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · スコア 0.661226 · 採用条件未達 · 順位差 -29.82094 / -42.089859000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · スコア 0.212578 · 採用条件未達 · 順位差 -30.269588 / -16.183193 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009d7e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7e4c.md) · スコア 0.106289 · 採用条件未達 · 順位差 -30.375877 / 0.106289 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32063773250664307,
          0.3252470799640611
        ],
        "cfg_coverage": [
          0.2621951219512195,
          0.2670807453416149
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 27.718783,
        "reverse_margin": 28.182166
      },
      "new": "0089d484",
      "score": 30.482166
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015943312666076175,
          0.008658008658008658
        ],
        "cfg_coverage": [
          0.024390243902439025,
          0.012195121951219513
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.718783,
        "reverse_margin": -37.334398
      },
      "new": "0088c830",
      "score": 2.763383
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.005314437555358724,
          0.017191977077363897
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
        "margin": -28.1633,
        "reverse_margin": -10.14517
      },
      "new": "009ee198",
      "score": 2.318866
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d4f387d7b7bb693aeaf5d441abd377e9"></a>

### v15.7.4 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) FUN_0086b704

`competing_candidates` 

呼出元 0件  · 呼出先 153件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b014.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md)

- 1. [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · スコア 40.859742 · 採用条件未達 · 順位差 30.504352999999995 / 30.342914999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · スコア 10.355389 · 採用条件未達 · 順位差 -30.504352999999995 / -18.084955 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · スコア 8.293085 · 採用条件未達 · 順位差 -32.566657 / -4.802062000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · スコア 6.828016 · 採用条件未達 · 順位差 -34.031726 / -22.750494000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · スコア 6.319185 · 採用条件未達 · 順位差 -34.540557 / -25.490195999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · スコア 6.265743 · 採用条件未達 · 順位差 -34.593999 / -42.820994999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · スコア 6.237432 · 採用条件未達 · 順位差 -34.62231 / -24.344617999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · スコア 6.213156 · 採用条件未達 · 順位差 -34.646586 / -34.809592 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3994227353463588,
          0.3972179289026275
        ],
        "cfg_coverage": [
          0.15133333333333332,
          0.15687629578438148
        ],
        "mapped_data": 8,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 30.504352999999995,
        "reverse_margin": 30.342914999999998
      },
      "new": "0089e838",
      "score": 40.859742
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.007992895204262877,
          0.00511654349061967
        ],
        "cfg_coverage": [
          0.0026666666666666666,
          0.0024198427102238356
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -30.504352999999995,
        "reverse_margin": -18.084955
      },
      "new": "00a47d08",
      "score": 10.355389
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
      "new": "0093b5d4",
      "score": 8.293085
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d029e162ab26b8594649669caba94e0c"></a>

### v15.7.4 [`008710b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710b4.md) FUN_008710b4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009335dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009335dc.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008a4254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4254.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "009335dc",
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
        "reverse_margin": 50.0
      },
      "new": "008a4254",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d6bd3a4d09595b43d40b7a3dcf95a355"></a>

### v15.7.4 [`008710c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710c4.md) FUN_008710c4

`competing_candidates` 

呼出元 1件 [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) · 呼出先 0件 

- 1. [`008a4264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4264.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a4254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4254.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a4264",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4254",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-53f8beb7d38dd0fc3bdf8efde999a828"></a>

### v15.7.4 [`008711a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711a0.md) FUN_008711a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4340.md) · スコア 37.142857 · 採用条件未達 · 順位差 2.8571430000000007 / 37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008a71fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a71fc.md) · スコア 34.285714 · 採用条件未達 · 順位差 -2.8571430000000007 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 37.142857
      },
      "new": "008a4340",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
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
        "margin": -2.8571430000000007,
        "reverse_margin": 34.285714
      },
      "new": "008a71fc",
      "score": 34.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-747e08c5d6940152bb7dc7044451e1a6"></a>

### v15.7.4 [`008711bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008711bc.md) FUN_008711bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a435c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4340.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a435c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4340",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1cae1b443d86779c9cf957ddf2f63c5b"></a>

### v15.7.4 [`008712e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008712e8.md) FUN_008712e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4488.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4488",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-593ac5c30744cba0a64e8ec7b9090625"></a>

### v15.7.4 [`00871304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871304.md) FUN_00871304

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a44a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44a4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4488.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a44a4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4488",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-574a42eeb482a0a7c4c38ea3cf317ef5"></a>

### v15.7.4 [`008716cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008716cc.md) FUN_008716cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a486c.md) · スコア 54.285714 · 採用条件未達 · 順位差 20.0 / 11.428570999999998 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008cbd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbd6c.md) · スコア 34.285714 · 採用条件未達 · 順位差 -20.0 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009a36b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a36b8.md) · スコア 34.285714 · 採用条件未達 · 順位差 -20.0 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 20.0,
        "reverse_margin": 11.428570999999998
      },
      "new": "008a486c",
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
        "margin": -20.0,
        "reverse_margin": 34.285714
      },
      "new": "008cbd6c",
      "score": 34.285714
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
        "margin": -20.0,
        "reverse_margin": -2.8571430000000007
      },
      "new": "009a36b8",
      "score": 34.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f2885eddfcd6394a759ef66add1763a4"></a>

### v15.7.4 [`008716e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008716e8.md) FUN_008716e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4888.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a486c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4888",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a486c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6db749d71cd960fb5180f6a79481d1d8"></a>

### v15.7.4 [`0087177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/0087177c.md) FUN_0087177c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a491c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": -80.0
      },
      "new": "008a491c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ccb8c9f6dc00b6970eea54d68c2596ff"></a>

### v15.7.4 [`00871798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871798.md) FUN_00871798

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4938.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a491c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4938",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a491c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-19750a09374286294127abee5eff0002"></a>

### v15.7.4 [`008717cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717cc.md) FUN_008717cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a496c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a496c.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "008a496c",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e5b398b7a8d69833bd1267b631feedab"></a>

### v15.7.4 [`008717dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008717dc.md) FUN_008717dc

`competing_candidates` 

呼出元 1件 [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) · 呼出先 0件 

- 1. [`008a497c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a497c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a496c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a496c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a497c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a496c",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2c3d7f048783c26dcac53a0141112631"></a>

### v15.7.4 [`008718e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008718e4.md) FUN_008718e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4a84.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4a84",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-845a796b780b6ba355f88a4ec3fa32a1"></a>

### v15.7.4 [`00871900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871900.md) FUN_00871900

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4aa0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4a84.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4aa0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4a84",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6cd54fdd4ad81b8d6e99aebdfb9818e1"></a>

### v15.7.4 [`00871934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871934.md) FUN_00871934

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ad4.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "008a4ad4",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4a3c4ffba98683bd68e9f35eb1cd650f"></a>

### v15.7.4 [`00871944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871944.md) FUN_00871944

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a4ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ae4.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a4ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ad4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a4ae4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4ad4",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c5a8c11b13a6e1935ade2fd5414bdebb"></a>

### v15.7.4 [`00871994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871994.md) FUN_00871994

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b34.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4b34",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-848c3589753ce9337ca7c7b0aa35589e"></a>

### v15.7.4 [`008719b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719b0.md) FUN_008719b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b50.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b34.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4b50",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4b34",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5875beffa99b23bbd0ab6d2f88b2b8b4"></a>

### v15.7.4 [`008719e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719e4.md) FUN_008719e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b84.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4b84",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-03e7359bd6ea36a4ba6535268dcd6d36"></a>

### v15.7.4 [`008719f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719f4.md) FUN_008719f4

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a4b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b94.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a4b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b84.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a4b94",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4b84",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f1a447002ec5badb4102b96d5b4c7457"></a>

### v15.7.4 [`008719fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008719fc.md) FUN_008719fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b9c.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`008a4bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bc8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008a4bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bbc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008a4ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ba0.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "008a4b9c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4bc8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4bbc",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-24a6c676c9e3f411e726245745cdab27"></a>

### v15.7.4 [`00871a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a00.md) FUN_00871a00

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ba0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4ba0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e4c6b7f3acc3d43b2082d2510cc86f09"></a>

### v15.7.4 [`00871a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a1c.md) FUN_00871a1c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bbc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ba0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008a4b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b9c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008a4bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bc8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4bbc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4ba0",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4b9c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b2bf14953acc278adb3b54f733cb4455"></a>

### v15.7.4 [`00871a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a28.md) FUN_00871a28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bc8.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`008a4b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4b9c.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008a4bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bbc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008a4ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ba0.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "008a4bc8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4b9c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4bbc",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-93a2fbfab6a42cac8fc71f06b6028007"></a>

### v15.7.4 [`00871a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a54.md) FUN_00871a54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bf4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a4bf4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ec46a01a2d213a0848cbea1aebd09245"></a>

### v15.7.4 [`00871a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a64.md) FUN_00871a64

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a4c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4c04.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a4bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4bf4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a4c04",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4bf4",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7124caf0fb7bea51e1f4866da08051cd"></a>

### v15.7.4 [`00871d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871d54.md) FUN_00871d54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00626cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626cc4.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008a4ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ef4.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 0.0
      },
      "new": "00626cc4",
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
        "reverse_margin": 54.285714
      },
      "new": "008a4ef4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8c3c5e0d36877bc372f0610b560bcab3"></a>

### v15.7.4 [`00871d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871d70.md) FUN_00871d70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f10.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ef4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4f10",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4ef4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b8a5e8e48f557446934b650db47f5634"></a>

### v15.7.4 [`00871e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e04.md) FUN_00871e04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fa4.md) · スコア 71.428571 · 採用条件未達 · 順位差 71.428571 / 71.428571 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8571428571428571,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 71.428571,
        "reverse_margin": 71.428571
      },
      "new": "008a4fa4",
      "score": 71.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1b49335deecce9bac17649d172680aa4"></a>

### v15.7.4 [`00871e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e20.md) FUN_00871e20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fc0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a4fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fa4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a4fc0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4fa4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-558949fddcb7d15807bf3468ed9c596b"></a>

### v15.7.4 [`00871e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e54.md) FUN_00871e54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a4ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ff4.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": -30.0
      },
      "new": "008a4ff4",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c4453593fe3f2da3708ae7a3df5403bb"></a>

### v15.7.4 [`00871e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e64.md) FUN_00871e64

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a5004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5004.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a4ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ff4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a5004",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a4ff4",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cc50f3641e38bf117a21af922361305a"></a>

### v15.7.4 [`00871e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871e8c.md) FUN_00871e8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a502c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008a502c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f28b0582af866158f1027699e48459e"></a>

### v15.7.4 [`00871ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871ea8.md) FUN_00871ea8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5048.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a502c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a5048",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a502c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c514559e397323e84e8c4c4bbd045fcb"></a>

### v15.7.4 [`00871edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871edc.md) FUN_00871edc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a507c.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "008a507c",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9c918b74a0182545aaf9ccb5866bc6ff"></a>

### v15.7.4 [`00871eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871eec.md) FUN_00871eec

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a508c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a507c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a508c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a507c",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8685c66e78ed4ae2f7aa5a2f9f153aa2"></a>

### v15.7.4 [`00872110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872110.md) FUN_00872110

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a52b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a52b0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008a52b0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a81ed46d1e1d0594dcf31b5d8ad03ba7"></a>

### v15.7.4 [`0087212c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/0087212c.md) FUN_0087212c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a52cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a52cc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a52b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a52b0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a52cc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a52b0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ef67bd9e539055a5fb120f9eec2db7fa"></a>

### v15.7.4 [`00872160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872160.md) FUN_00872160

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d00.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008a5300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5300.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00934d00",
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
        "reverse_margin": 50.0
      },
      "new": "008a5300",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8a67629714e16aa14fa61ba75a76517e"></a>

### v15.7.4 [`00872170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872170.md) FUN_00872170

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a5310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5310.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a5300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5300.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a5310",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a5300",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6c1cb8d26335413aca0073da3c569380"></a>

### v15.7.4 [`00872268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872268.md) FUN_00872268

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a5408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5408.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a5408",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cfb36fd2e36a0e16dcadb3b774c57939"></a>

### v15.7.4 [`00872284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/00872284.md) FUN_00872284

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a5424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5424.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008a5408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5408.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 82.2857
      },
      "new": "008a5424",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a5408",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-00b305fd89c0f167222dae555b4ba81f"></a>

### v15.7.4 [`008722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722b8.md) FUN_008722b8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a5458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5458.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a5458",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-181226dd8ca288ab62f886980b6ae865"></a>

### v15.7.4 [`008722c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722c8.md) FUN_008722c8

`competing_candidates` 

呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 0件 

- 1. [`008a5468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5468.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008a5458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5458.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "008a5468",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008a5458",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7f8e42a6afe25247296787aa169eef27"></a>

### v15.7.4 [`008722d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008722d0.md) FUN_008722d0

`competing_candidates` 

呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

- 1. [`008a5470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5470.md) · スコア 24.52761 · 採用条件未達 · 順位差 15.716135 / 15.253563 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) · スコア 8.811475 · 採用条件未達 · 順位差 -15.716135 / 8.811475 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008a596c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a596c.md) · スコア 7.232528 · 採用条件未達 · 順位差 -17.295082 / -19.320663000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) · スコア 5.854185 · 採用条件未達 · 順位差 -18.673424999999998 / 5.854185 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0053fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) · スコア 5.526316 · 採用条件未達 · 順位差 -19.001294 / 5.526316 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a91900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a91900.md) · スコア 3.468208 · 採用条件未達 · 順位差 -21.059402 / -11.445087 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00733380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733380.md) · スコア 3.389831 · 採用条件未達 · 順位差 -21.137779 / 3.389831 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0062c7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c7b0.md) · スコア 2.741117 · 採用条件未達 · 順位差 -21.786493 / 2.741117 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34868421052631576,
          0.34868421052631576
        ],
        "cfg_coverage": [
          0.18032786885245902,
          0.1896551724137931
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.716135,
        "reverse_margin": 15.253563
      },
      "new": "008a5470",
      "score": 24.52761
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.125,
          0.19387755102040816
        ],
        "cfg_coverage": [
          0.06557377049180328,
          0.1
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -15.716135,
        "reverse_margin": 8.811475
      },
      "new": "004c0774",
      "score": 8.811475
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09868421052631579,
          0.11538461538461539
        ],
        "cfg_coverage": [
          0.06557377049180328,
          0.0851063829787234
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.295082,
        "reverse_margin": -19.320663000000003
      },
      "new": "008a596c",
      "score": 7.232528
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9792cd861ef764e66a8d95175a5865a6"></a>

### v15.7.4 [`008725c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00872/008725c8.md) FUN_008725c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008a5768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5768.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "008a5768",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

