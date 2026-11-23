# v15.7.4 → v16.0.0 · 追加調査 (53)

[一覧の目次](README.md)

<a id="review-2c7602484f731a439ba79e30184a6b61"></a>

### v15.7.4 [`007c53a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c53a8.md) FUN_007c53a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7584.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "007f7584",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-eccd3d7c9675e0d524194f530531ff2f"></a>

### v15.7.4 [`007c53b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c53b8.md) FUN_007c53b8

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f7594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7594.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`007f7584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7584.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007f7594",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7584",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6fc1e998849744900dd75a81be4cca92"></a>

### v15.7.4 [`007c5408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5408.md) FUN_007c5408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00475ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475ac0.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007f75e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f75e4.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00475ac0",
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
      "new": "007f75e4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e845e75fc0a0fccc7952c546f8f92749"></a>

### v15.7.4 [`007c5424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5424.md) FUN_007c5424

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7600.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007f75e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f75e4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007f7600",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f75e4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-42b535523b67d308817fe63739251082"></a>

### v15.7.4 [`007c5468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5468.md) FUN_007c5468

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00af0db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0db0.md) · スコア 80.0 · 採用条件未達 · 順位差 24.0 / 24.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007f7644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7644.md) · スコア 56.0 · 採用条件未達 · 順位差 -24.0 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 24.0,
        "reverse_margin": 24.0
      },
      "new": "00af0db0",
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
        "reverse_margin": 56.0
      },
      "new": "007f7644",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e31d2ec2c09e1bcf96f0d4ff2464a975"></a>

### v15.7.4 [`007c547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c547c.md) FUN_007c547c

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f7658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7658.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`007f7644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7644.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.2,
        "reverse_margin": 68.2
      },
      "new": "007f7658",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7644",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2d70471e55144ea1898a8b9a72ca0420"></a>

### v15.7.4 [`007c56f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c56f4.md) FUN_007c56f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aefb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefb2c.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007f78d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f78d0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 25.714286
      },
      "new": "00aefb2c",
      "score": 80.0
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
      "new": "007f78d0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b38bfdf3db143cbe4563d2aff540b0ab"></a>

### v15.7.4 [`007c5710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5710.md) FUN_007c5710

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f78ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f78ec.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007f78d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f78d0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007f78ec",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f78d0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9fcd59e52c69412e0f2cce410adf39dd"></a>

### v15.7.4 [`007c5a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5a54.md) FUN_007c5a54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7c30.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -34.285714
      },
      "new": "007f7c30",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1aef2122a72177cecb2919ae9c8682d6"></a>

### v15.7.4 [`007c5a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5a70.md) FUN_007c5a70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7c4c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007f7c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7c30.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007f7c4c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7c30",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b243b9e153f781496790dda3a0ef0629"></a>

### v15.7.4 [`007c5cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5cfc.md) FUN_007c5cfc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ed8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f04.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -43.076923 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "007f7ed8",
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
        "margin": 0.0,
        "reverse_margin": -43.076923
      },
      "new": "007f7f04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ef357a6bf68346bbce1dbdae499eb02e"></a>

### v15.7.4 [`007c5d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d18.md) FUN_007c5d18

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ef4.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 67.2857 · 
- 2. [`007f7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f38.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ed8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f7f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f00.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f04.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 67.2857
      },
      "new": "007f7ef4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7f38",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7ed8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab5cc186dd2bbdb5022d91b7d8537e52"></a>

### v15.7.4 [`007c5d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d24.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f7f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f00.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 71.6667 · 
- 2. [`007f7f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f50.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f7f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f4c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f7ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ef4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f38.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f04.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ed8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 71.6667
      },
      "new": "007f7f00",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7f50",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-03745e9205ffccc84b33d27ffb9800f5"></a>

### v15.7.4 [`007c5d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d28.md) FUN_007c5d28

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f04.md) · スコア 43.076923 · 採用条件未達 · 順位差 39.326923 / 43.076923 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f7f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f54.md) · スコア 3.75 · 採用条件未達 · 順位差 -39.326923 / -31.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f38.md) · スコア 0.0 · 採用条件未達 · 順位差 -43.076923 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38461538461538464,
          0.38461538461538464
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
        "margin": 39.326923,
        "reverse_margin": 43.076923
      },
      "new": "007f7f04",
      "score": 43.076923
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.0625
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
        "margin": -39.326923,
        "reverse_margin": -31.25
      },
      "new": "007f7f54",
      "score": 3.75
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
        "margin": -43.076923,
        "reverse_margin": -56.0
      },
      "new": "007f7f38",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c2e00c3504fcbc5c2e47972245324c33"></a>

### v15.7.4 [`007c5d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d5c.md) FUN_007c5d5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f38.md) · スコア 56.0 · 採用条件未達 · 順位差 18.857143 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f94.md) · スコア 37.142857 · 採用条件未達 · 順位差 -18.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f7f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f04.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.0 / -43.076923 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f7f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f54.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 56.0
      },
      "new": "007f7f38",
      "score": 56.0
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
      "new": "007f7f94",
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
        "margin": -56.0,
        "reverse_margin": -43.076923
      },
      "new": "007f7f04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-040565b97b2b75be95898ad808b3ce74"></a>

### v15.7.4 [`007c5d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d70.md) FUN_007c5d70

`competing_candidates` 

呼出元 1件 [`007c5ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md) · 呼出先 0件 

- 1. [`007f7f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f4c.md) · スコア 58.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8008.md) · スコア 58.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f7f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f50.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 4.016 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f7fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f7fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fb0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f38.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f7f4c",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8008",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7f50",
      "score": 8.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ce0eaf5867862362e6937ef9ad110f6d"></a>

### v15.7.4 [`007c5d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d74.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007c5ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f7f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f50.md) · スコア 77.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 77.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f7fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fbc.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 8.016 · 採用条件未達 · 順位差 — / — · 
- 5. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f7fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fb0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ff4.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f7f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f54.md) · スコア 0.8382 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f7f50",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f800c",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7fbc",
      "score": 73.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f455dd86df33e067dc1dc571bcc949a1"></a>

### v15.7.4 [`007c5d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d78.md) FUN_007c5d78

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`00af1b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b0c.md) · スコア 65.0 · 採用条件未達 · 順位差 3.75 / 28.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00af1bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1bb4.md) · スコア 61.25 · 採用条件未達 · 順位差 -3.75 / 24.583333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 50.0 · 採用条件未達 · 順位差 -15.0 / 13.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00af1134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1134.md) · スコア 36.666667 · 採用条件未達 · 順位差 -28.333333000000003 / -32.083333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00af11dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11dc.md) · スコア 36.666667 · 採用条件未達 · 順位差 -28.333333000000003 / -32.083333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f7f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f54.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 31.666667 · 採用条件未達 · 順位差 -33.333332999999996 / -38.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00af1c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c5c.md) · スコア 3.75 · 採用条件未達 · 順位差 -61.25 / -38.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.75,
        "reverse_margin": 28.333333000000003
      },
      "new": "00af1b0c",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6875,
          0.6875
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
        "margin": -3.75,
        "reverse_margin": 24.583333000000003
      },
      "new": "00af1bb4",
      "score": 61.25
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.0,
        "reverse_margin": 13.333333000000003
      },
      "new": "005daf8c",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fe514badb636381ac8bf630a2b6badca"></a>

### v15.7.4 [`007c5db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5db8.md) FUN_007c5db8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f94.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ff4.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / 37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f7fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fc0.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / 24.615385 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 17.142857,
        "reverse_margin": 17.142857
      },
      "new": "007f7f94",
      "score": 54.285714
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
        "reverse_margin": 37.142857
      },
      "new": "007f7ff4",
      "score": 37.142857
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
        "reverse_margin": 24.615385
      },
      "new": "007f7fc0",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2f22d19e16175dab6237279cc604bf62"></a>

### v15.7.4 [`007c5dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5dd4.md) FUN_007c5dd4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ff4.md) · スコア 2.4 · 採用条件未達 · 順位差 0.6857 / 0.0 · 
- 2. [`007f831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f831c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f7fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fbc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8008.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f7fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7fc0.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) · スコア 0.0615 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.6857,
        "reverse_margin": 0.0
      },
      "new": "007f7ff4",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f831c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f7fbc",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e9fbe35141207e1808b4a99cb09f21d2"></a>

### v15.7.4 [`007c5de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5de0.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / -4.0 · 
- 2. [`007f8344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8344.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8008.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8338.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7ff4.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f831c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) · スコア 0.0205 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": -4.0
      },
      "new": "007f800c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8344",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-00774dad2ec9456eef6d1e79a182533f"></a>

### v15.7.4 [`007c5de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5de4.md) FUN_007c5de4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f8348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8348.md) · スコア 66.153846 · 採用条件未達 · 順位差 66.153846 / 41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f831c.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 66.153846,
        "reverse_margin": 41.538461
      },
      "new": "007f8348",
      "score": 66.153846
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
        "margin": -66.153846,
        "reverse_margin": 0.0
      },
      "new": "007f831c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9004187861a5df25c7f63472616894f3"></a>

### v15.7.4 [`007c5e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e18.md) FUN_007c5e18

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f837c.md) · スコア 56.0 · 採用条件未達 · 順位差 31.384615 / 18.857143 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8348.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / -41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f831c.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 31.384615,
        "reverse_margin": 18.857143
      },
      "new": "007f837c",
      "score": 56.0
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
      "new": "007f8348",
      "score": 24.615385
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
        "margin": -56.0,
        "reverse_margin": 0.0
      },
      "new": "007f831c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a26ac55c04c0667f48b1494876b8dd53"></a>

### v15.7.4 [`007c5e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e2c.md) FUN_007c5e2c

`competing_candidates` 

呼出元 1件 [`007c5ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md) · 呼出先 0件 

- 1. [`007f7f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f4c.md) · スコア 58.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8008.md) · スコア 58.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8390.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f7f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f50.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 4.016 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8344.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f7f4c",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8008",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8390",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-88311d17d583d733cedc494b7d979ee6"></a>

### v15.7.4 [`007c5e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e30.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007c5ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5ad0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f7f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7f50.md) · スコア 77.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f800c.md) · スコア 77.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8344.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 8.016 · 採用条件未達 · 順位差 — / — · 
- 6. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8390.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8338.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f7f50",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f800c",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8344",
      "score": 73.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1feed7e3e7512de870fc024498fc5f95"></a>

### v15.7.4 [`007c5e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5e34.md) FUN_007c5e34

`competing_candidates` 

呼出元 0件  · 呼出先 23件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md)

- 1. [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) · スコア 31.769231 · 採用条件未達 · 順位差 29.307693 / 26.538462000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0046ba60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046ba60.md) · スコア 2.461538 · 採用条件未達 · 順位差 -29.307693 / 2.461538 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · スコア 2.158654 · 採用条件未達 · 順位差 -29.610577000000003 / 2.158654 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007f7164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7164.md) · スコア 1.846154 · 採用条件未達 · 順位差 -29.923077000000003 / -34.43956 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 1.230769 · 採用条件未達 · 順位差 -30.538462000000003 / -21.888497 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.769231 / -44.951889 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.769231 / -42.000303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0062f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f240.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.769231 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5128205128205128,
          0.5128205128205128
        ],
        "cfg_coverage": [
          0.06818181818181818,
          0.05
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 29.307693,
        "reverse_margin": 26.538462000000003
      },
      "new": "007f8010",
      "score": 31.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.041025641025641026,
          0.16
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -29.307693,
        "reverse_margin": 2.461538
      },
      "new": "0046ba60",
      "score": 2.461538
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03076923076923077,
          0.036585365853658534
        ],
        "cfg_coverage": [
          0.022727272727272728,
          0.015625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -29.610577000000003,
        "reverse_margin": 2.158654
      },
      "new": "0054dd28",
      "score": 2.158654
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a6dd870cd2c2479b85bc0f1b7a322913"></a>

### v15.7.4 [`007c6140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6140.md) FUN_007c6140

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8410.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f837c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -18.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f831c.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 17.142857,
        "reverse_margin": 0.0
      },
      "new": "007f8410",
      "score": 54.285714
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
      "new": "007f837c",
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
        "margin": -54.285714,
        "reverse_margin": 0.0
      },
      "new": "007f831c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-554cb7a5f019a66f0a9743d4fe72bc23"></a>

### v15.7.4 [`007c615c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c615c.md) FUN_007c615c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f842c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f842c.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 67.2857 · 
- 2. [`007f8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8470.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8410.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8438.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f843c.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8398.md) · スコア 0.4 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 67.2857
      },
      "new": "007f842c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8470",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8410",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ed8d9308b7604b3d0b2172dcb8582aba"></a>

### v15.7.4 [`007c6168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6168.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8438.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 71.6667 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8484.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f842c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f842c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8470.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f843c.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8410.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8398.md) · スコア 0.1333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 71.6667
      },
      "new": "007f8438",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8484",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e1c8e6d34cc37a7aa9f23b6e28348497"></a>

### v15.7.4 [`007c616c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c616c.md) FUN_007c616c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f843c.md) · スコア 66.153846 · 採用条件未達 · 順位差 41.538461 / 66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8470.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / 24.615385 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 66.153846
      },
      "new": "007f843c",
      "score": 66.153846
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
        "margin": -41.538461,
        "reverse_margin": 24.615385
      },
      "new": "007f8470",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-74853eef97cd192920b41793449cc270"></a>

### v15.7.4 [`007c61a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61a0.md) FUN_007c61a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f843c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8470.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -24.615385 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f85f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f85f8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -66.153846
      },
      "new": "007f843c",
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
        "margin": 0.0,
        "reverse_margin": -24.615385
      },
      "new": "007f8470",
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
        "margin": 0.0,
        "reverse_margin": -54.285714
      },
      "new": "007f85f8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-59fdd14398c4e06f7fa01a5e5f29e273"></a>

### v15.7.4 [`007c61b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61b4.md) FUN_007c61b4

`competing_candidates` 

呼出元 1件 [`007c5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md) · 呼出先 0件 

- 1. [`007f8390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8390.md) · スコア 58.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8484.md) · スコア 58.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8488.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) · スコア 4.0909 · 採用条件未達 · 順位差 — / — · 
- 6. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 4.016 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8620.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8614.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8390",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8484",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8394",
      "score": 8.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-05931f71a3497c4693812447066e73ba"></a>

### v15.7.4 [`007c61b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61b8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007c5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 77.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8488.md) · スコア 77.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8620.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 8.016 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8484.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8614.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8624.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8394",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8488",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8620",
      "score": 73.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f436bc6d875861aec2366d22d70e772a"></a>

### v15.7.4 [`007c61bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c61bc.md) FUN_007c61bc

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00829328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829328.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`009a6f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6f44.md)

- 1. [`007f8398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8398.md) · スコア 22.0 · 採用条件未達 · 順位差 10.0 / 10.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 12.0 · 採用条件未達 · 順位差 -10.0 / -50.769231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f2df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2df0.md) · スコア 4.571429 · 採用条件未達 · 順位差 -17.428570999999998 / -35.764705 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.0 / -63.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007fdf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.0 / -25.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00865668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865668.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.0 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36666666666666664,
          0.36666666666666664
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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "007f8398",
      "score": 22.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.23076923076923078
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
        "margin": -10.0,
        "reverse_margin": -50.769231
      },
      "new": "00616f1c",
      "score": 12.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.26666666666666666,
          0.0761904761904762
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
        "margin": -17.428570999999998,
        "reverse_margin": -35.764705
      },
      "new": "007f2df0",
      "score": 4.571429
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a72df38019a9a5752bb1e142cd37dca8"></a>

### v15.7.4 [`007c6234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6234.md) FUN_007c6234

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a3f12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f12c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007f8410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8410.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f85f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f85f8.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`007f8624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8624.md) · スコア 24.615385 · 採用条件未達 · 順位差 -55.384615 / 24.615385 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8658.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00a3f12c",
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
        "reverse_margin": 0.0
      },
      "new": "007f8410",
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
        "reverse_margin": 54.285714
      },
      "new": "007f85f8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d77c6dab1cd53db53c5b8472a00cfd19"></a>

### v15.7.4 [`007c6250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6250.md) FUN_007c6250

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8658.md) · スコア 2.4 · 採用条件未達 · 順位差 0.6857 / 0.0 · 
- 2. [`007f8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8990.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8620.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f866c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8670.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8624.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8674.md) · スコア 0.0603 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.6857,
        "reverse_margin": 0.0
      },
      "new": "007f8658",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8990",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8620",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-92683655be10506ee2c2a6ca352dede6"></a>

### v15.7.4 [`007c625c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c625c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8670.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 0.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f866c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f89ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89ac.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8658.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8624.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8990.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8674.md) · スコア 0.0201 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 0.0
      },
      "new": "007f8670",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f866c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9c5835613b3ce8b1caa51a2c09330283"></a>

### v15.7.4 [`007c6260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6260.md) FUN_007c6260

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f89bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89bc.md) · スコア 23.076923 · 採用条件未達 · 順位差 23.076923 / -1.538461999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8990.md) · スコア 0.0 · 採用条件未達 · 順位差 -23.076923 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "reverse_margin": -1.538461999999999
      },
      "new": "007f89bc",
      "score": 23.076923
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
        "margin": -23.076923,
        "reverse_margin": -54.285714
      },
      "new": "007f8990",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-243c48d2536e5e6fac501396b985960c"></a>

### v15.7.4 [`007c6294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6294.md) FUN_007c6294

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89f0.md) · スコア 56.0 · 採用条件未達 · 順位差 18.857143 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8990.md) · スコア 37.142857 · 採用条件未達 · 順位差 -18.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f89bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89bc.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / 1.538461999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 56.0
      },
      "new": "007f89f0",
      "score": 56.0
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
      "new": "007f8990",
      "score": 37.142857
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
        "reverse_margin": 1.538461999999999
      },
      "new": "007f89bc",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca16f9de7326e58a8be938b552ce0566"></a>

### v15.7.4 [`007c62a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62a8.md) FUN_007c62a8

`competing_candidates` 

呼出元 1件 [`007c5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md) · 呼出先 0件 

- 1. [`007f8390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8390.md) · スコア 58.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8484.md) · スコア 58.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a04.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8488.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) · スコア 4.0909 · 採用条件未達 · 順位差 — / — · 
- 7. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 4.016 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f89b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89b8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8390",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8484",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8a04",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b982c8d3ecda4a5c7b600f7a72558379"></a>

### v15.7.4 [`007c62ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62ac.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007c5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5770.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8394.md) · スコア 77.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8488.md) · スコア 77.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f89b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89b8.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a08.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 8.016 · 採用条件未達 · 順位差 — / — · 
- 6. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 4.0367 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8394",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8488",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f89b8",
      "score": 73.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f5fb020abb85fb53b6f96af05a2d272c"></a>

### v15.7.4 [`007c62b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c62b0.md) FUN_007c62b0

`competing_candidates` 

呼出元 0件  · 呼出先 4件 [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

- 1. [`007f848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f848c.md) · スコア 27.472527 · 採用条件未達 · 順位差 25.361974 / 25.361974 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8674.md) · スコア 2.110553 · 採用条件未達 · 順位差 -25.361974 / -29.849246 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 0.550459 · 採用条件未達 · 順位差 -26.922068 / -22.568807 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00ab7f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7f44.md) · スコア 0.27027 · 採用条件未達 · 順位差 -27.202257 / -34.324325 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f7164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7164.md) · スコア 0.0 · 採用条件未達 · 順位差 -27.472527 / -36.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f8010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8010.md) · スコア 0.0 · 採用条件未達 · 順位差 -27.472527 / -31.769231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4065934065934066,
          0.4065934065934066
        ],
        "cfg_coverage": [
          0.15384615384615385,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.361974,
        "reverse_margin": 25.361974
      },
      "new": "007f848c",
      "score": 27.472527
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.035175879396984924
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
        "margin": -25.361974,
        "reverse_margin": -29.849246
      },
      "new": "007f8674",
      "score": 2.110553
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01098901098901099,
          0.009174311926605505
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
        "margin": -26.922068,
        "reverse_margin": -22.568807
      },
      "new": "007f8a0c",
      "score": 0.550459
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-88834987087903fd00de990f86d70d38"></a>

### v15.7.4 [`007c641c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c641c.md) FUN_007c641c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006fe540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe540.md) · スコア 34.285714 · 採用条件未達 · 順位差 34.285714 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f85f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f85f8.md) · スコア 0.0 · 採用条件未達 · 順位差 -34.285714 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f89f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f89f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -34.285714 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8bec.md) · スコア 0.0 · 採用条件未達 · 順位差 -34.285714 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 34.285714,
        "reverse_margin": 34.285714
      },
      "new": "006fe540",
      "score": 34.285714
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
        "margin": -34.285714,
        "reverse_margin": -54.285714
      },
      "new": "007f85f8",
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
        "margin": -34.285714,
        "reverse_margin": -56.0
      },
      "new": "007f89f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f29ee08dc483b1ce8fd6265702deff11"></a>

### v15.7.4 [`007c6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6438.md) FUN_007c6438

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c08.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 67.2857 · 
- 2. [`007f8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8bec.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a04.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a08.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c14.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c18.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 0.1101 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 67.2857
      },
      "new": "007f8c08",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8bec",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8a04",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b7498c102f9739e26ed92b9347c5bf1"></a>

### v15.7.4 [`007c6444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6444.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c14.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 71.6667 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 4.0367 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c4c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c3c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c08.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c18.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8bec.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 71.6667
      },
      "new": "007f8c14",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8a0c",
      "score": 4.0367
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9d53930990edeb7e6689db631853b3d6"></a>

### v15.7.4 [`007c6448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6448.md) FUN_007c6448

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00794878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794878.md) · スコア 32.307692 · 採用条件未達 · 順位差 32.307692 / 32.307692 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007f8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8bec.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.307692 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c18.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.307692 / -33.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c3c.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.307692 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5384615384615384,
          0.5384615384615384
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
        "margin": 32.307692,
        "reverse_margin": 32.307692
      },
      "new": "00794878",
      "score": 32.307692
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
        "margin": -32.307692,
        "reverse_margin": -54.285714
      },
      "new": "007f8bec",
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
        "margin": -32.307692,
        "reverse_margin": -33.333333
      },
      "new": "007f8c18",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5cd7bae55e748c2ce78dc4f72884dfb6"></a>

### v15.7.4 [`007c647c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c647c.md) FUN_007c647c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007948ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948ac.md) · スコア 80.0 · 採用条件未達 · 順位差 36.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007f8c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c3c.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c9c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c18.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -6.666666000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c54.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 36.0,
        "reverse_margin": 80.0
      },
      "new": "007948ac",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
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
        "margin": -36.0,
        "reverse_margin": -36.0
      },
      "new": "007f8c3c",
      "score": 44.0
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
        "margin": -42.857143,
        "reverse_margin": -17.142857
      },
      "new": "007f8c9c",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9c570a47dbfb4ab6b07b2c7992ea599f"></a>

### v15.7.4 [`007c6490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6490.md) FUN_007c6490

`competing_candidates` 

呼出元 1件 [`007c5484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md) · 呼出先 0件 

- 1. [`007f866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f866c.md) · スコア 58.0 · 採用条件未達 · 順位差 4.0 / 54.0 · 
- 2. [`007f8c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c4c.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8670.md) · スコア 8.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) · スコア 4.0909 · 採用条件未達 · 順位差 — / — · 
- 5. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 4.016 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c50.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cb8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c3c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 4.0,
        "reverse_margin": 54.0
      },
      "new": "007f866c",
      "score": 58.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8c4c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8670",
      "score": 8.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a68dae9ee095d2ac01b3614faecf78e7"></a>

### v15.7.4 [`007c6494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6494.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007c5484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8670.md) · スコア 77.0 · 採用条件未達 · 順位差 4.0 / 4.0 · 
- 2. [`007f8c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c50.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 8.016 · 採用条件未達 · 順位差 — / — · 
- 5. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c4c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cb8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 4.0,
        "reverse_margin": 4.0
      },
      "new": "007f8670",
      "score": 77.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8c50",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8cc4",
      "score": 73.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e499661d2d8fb940db1c28b9d5e44669"></a>

### v15.7.4 [`007c6498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6498.md) FUN_007c6498

`competing_candidates` 

呼出元 0件  · 呼出先 7件 [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md) [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md)

- 1. [`007f8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8674.md) · スコア 31.959799 · 採用条件未達 · 順位差 24.723618000000002 / 28.341709 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0046aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aee0.md) · スコア 7.236181 · 採用条件未達 · 順位差 -24.723618000000002 / 7.236181 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0046b19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b19c.md) · スコア 7.093596 · 採用条件未達 · 順位差 -24.866203 / 7.093596 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) · スコア 4.705882 · 採用条件未達 · 順位差 -27.253917 / 4.705882 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) · スコア 3.564356 · 採用条件未達 · 順位差 -28.395443 / 3.564356 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007f848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f848c.md) · スコア 2.110553 · 採用条件未達 · 順位差 -29.849246 / -25.361974 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00555284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555284.md) · スコア 1.809045 · 採用条件未達 · 順位差 -30.150754 / 1.809045 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) · スコア 0.083218 · 採用条件未達 · 順位差 -31.876581 / -34.230149 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5326633165829145,
          0.5326633165829145
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
        "margin": 24.723618000000002,
        "reverse_margin": 28.341709
      },
      "new": "007f8674",
      "score": 31.959799
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12060301507537688,
          0.13714285714285715
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
        "margin": -24.723618000000002,
        "reverse_margin": 7.236181
      },
      "new": "0046aee0",
      "score": 7.236181
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12060301507537688,
          0.11822660098522167
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
        "margin": -24.866203,
        "reverse_margin": 7.093596
      },
      "new": "0046b19c",
      "score": 7.093596
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b308a7d8e0bfad4f5efb200b66a5563d"></a>

### v15.7.4 [`007c67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67b4.md) FUN_007c67b4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8990.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c9c.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f8cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cec.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc8.md) · スコア 26.666667 · 採用条件未達 · 順位差 -27.619047 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 17.142857
      },
      "new": "007f8990",
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
        "reverse_margin": 17.142857
      },
      "new": "007f8c9c",
      "score": 54.285714
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
      "new": "007f8cec",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7f1b6a2a2ebf8377cb095e055dcaeef3"></a>

### v15.7.4 [`007c67d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67d0.md) FUN_007c67d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cb8.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 67.2857 · 
- 2. [`007f8cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cec.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cfc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d00.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d04.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 67.2857
      },
      "new": "007f8cb8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8cec",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8cc4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f988424bf2eb2cf7a7c11d8baeab564a"></a>

### v15.7.4 [`007c67dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67dc.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d00.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cfc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cec.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cc8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d04.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8cc4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8d00",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-74c7fb0e21717ac3bbe00fa605c15972"></a>

### v15.7.4 [`007c67e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67e0.md) FUN_007c67e0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f8cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8cec.md) · スコア 24.615385 · 採用条件未達 · 順位差 0.0 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 24.615385 · 採用条件未達 · 順位差 0.0 / -29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d04.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.615385 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
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
        "margin": 0.0,
        "reverse_margin": -55.384615
      },
      "new": "007f8cec",
      "score": 24.615385
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
        "margin": 0.0,
        "reverse_margin": -29.670329
      },
      "new": "007f8d4c",
      "score": 24.615385
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
        "margin": -24.615385,
        "reverse_margin": 0.0
      },
      "new": "007f8d04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c59fba58f500d7176f9a85d8511537fd"></a>

### v15.7.4 [`007c6814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6814.md) FUN_007c6814

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 37.142857 · 採用条件未達 · 順位差 10.476189999999999 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d78.md) · スコア 26.666667 · 採用条件未達 · 順位差 -10.476189999999999 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d04.md) · スコア 0.0 · 採用条件未達 · 順位差 -37.142857 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "margin": 10.476189999999999,
        "reverse_margin": -17.142857
      },
      "new": "007f8d4c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
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
        "reverse_margin": -46.66666599999999
      },
      "new": "007f8d78",
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
        "margin": -37.142857,
        "reverse_margin": 0.0
      },
      "new": "007f8d04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a480360f7c5b46c2ea745042d02da4f7"></a>

### v15.7.4 [`007c6828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6828.md) FUN_007c6828

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f8dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dac.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`007f8d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d74.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d68.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d9c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d78.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d04.md) · スコア 0.2222 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "007f8dac",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8d74",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8d68",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-afe4a03cc2f92913464bff6c5b008967"></a>

### v15.7.4 [`007c682c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c682c.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d74.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 68.9633 · 
- 2. [`007f8db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d9c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d68.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d78.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 68.9633
      },
      "new": "007f8d74",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8db0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aba68b19d8c6e8cd53a59214b44a87eb"></a>

### v15.7.4 [`007c6830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6830.md) FUN_007c6830

`competing_candidates` 

呼出元 0件  · 呼出先 11件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

- 1. [`007f8a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8a0c.md) · スコア 23.119266 · 採用条件未達 · 順位差 14.311926999999999 / 12.660549999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0081c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c510.md) · スコア 8.807339 · 採用条件未達 · 順位差 -14.311926999999999 / 8.807339 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005170d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/005170d0.md) · スコア 8.256881 · 採用条件未達 · 順位差 -14.862385 / 8.256881 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) · スコア 8.181818 · 採用条件未達 · 順位差 -14.937448 / -3.468014 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ab7cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7cac.md) · スコア 3.575758 · 採用条件未達 · 順位差 -19.543508 / -26.20202 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0057681c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057681c.md) · スコア 3.378305 · 採用条件未達 · 順位差 -19.740961 / 3.378305 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0054507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054507c.md) · スコア 3.254466 · 採用条件未達 · 順位差 -19.8648 / 3.254466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0064bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064bd14.md) · スコア 3.254466 · 採用条件未達 · 順位差 -19.8648 / 3.254466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3853211009174312,
          0.3853211009174312
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
        "margin": 14.311926999999999,
        "reverse_margin": 12.660549999999999
      },
      "new": "007f8a0c",
      "score": 23.119266
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14678899082568808,
          0.14953271028037382
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
        "margin": -14.311926999999999,
        "reverse_margin": 8.807339
      },
      "new": "0081c510",
      "score": 8.807339
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13761467889908258,
          0.19230769230769232
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
        "margin": -14.862385,
        "reverse_margin": 8.256881
      },
      "new": "005170d0",
      "score": 8.256881
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5e147d1aab5e2adb9234908d4219fbdf"></a>

### v15.7.4 [`007c6a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a10.md) FUN_007c6a10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8bec.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dfc.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f8d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d9c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d78.md) · スコア 26.666667 · 採用条件未達 · 順位差 -27.619047 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 54.285714
      },
      "new": "007f8bec",
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
      "new": "007f8dfc",
      "score": 54.285714
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
      "new": "007f8d9c",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b22e98b41a5e7fde1cd4dc741f392928"></a>

### v15.7.4 [`007c6a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a2c.md) FUN_007c6a2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e18.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 66.0 · 
- 2. [`007f8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dfc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dac.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e24.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e28.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db4.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.2857,
        "reverse_margin": 66.0
      },
      "new": "007f8e18",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8dfc",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8dac",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5d0032dc501a032bd83cdf8e094eed97"></a>

### v15.7.4 [`007c6a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a38.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db0.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e24.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e4c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e18.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e28.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8db4.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dfc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8db0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8e24",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5bf63f408dc11512b286ed1d53a832ba"></a>

### v15.7.4 [`007c6a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a3c.md) FUN_007c6a3c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00af1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b78.md) · スコア 73.333333 · 採用条件未達 · 順位差 13.333332999999996 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f8e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e28.md) · スコア 60.0 · 採用条件未達 · 順位差 -13.333332999999996 / 33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dfc.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -27.619047 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e4c.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / -23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 0.0
      },
      "new": "00af1b78",
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
        "margin": -13.333332999999996,
        "reverse_margin": 33.333332999999996
      },
      "new": "007f8e28",
      "score": 60.0
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
        "reverse_margin": -27.619047
      },
      "new": "007f8dfc",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-85fb832512a0a03aa064c71a95b5ef67"></a>

### v15.7.4 [`007c6a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a60.md) FUN_007c6a60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00af1b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b9c.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007f8e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e4c.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f8e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e28.md) · スコア 26.666667 · 採用条件未達 · 順位差 -53.333332999999996 / -33.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00af1b9c",
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
        "reverse_margin": 23.333333
      },
      "new": "007f8e4c",
      "score": 50.0
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
      "new": "007f8e28",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-75324f18016a47d43d94473c476448e0"></a>

### v15.7.4 [`007c6a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a70.md) FUN_007c6a70

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f8e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e5c.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`007f8e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e60.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ec8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e4c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8eac.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e28.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e64.md) · スコア 0.2222 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "007f8e5c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8e60",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8ec8",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5e4134dc1590e12f5197167cf3b91c42"></a>

### v15.7.4 [`007c6a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a74.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e60.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 69.0 · 
- 2. [`007f8ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed4.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e5c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e4c.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ec8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e64.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8eac.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 69.0
      },
      "new": "007f8e60",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8ed4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ac9e4bd09bf1bc4c59925927b1a82b83"></a>

### v15.7.4 [`007c6a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a78.md) FUN_007c6a78

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`007f74ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f74ec.md) · スコア 70.0 · 採用条件未達 · 順位差 20.0 / 70.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 50.0 · 採用条件未達 · 順位差 -20.0 / -13.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 45.333333 · 採用条件未達 · 順位差 -24.666666999999997 / -24.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 45.333333 · 採用条件未達 · 順位差 -24.666666999999997 / -24.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e64.md) · スコア 45.333333 · 採用条件未達 · 順位差 -24.666666999999997 / 45.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 30.666667 · 採用条件未達 · 順位差 -39.333332999999996 / -19.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 20.512821 · 採用条件未達 · 順位差 -49.487179 / -42.25641 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0062677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md) · スコア 8.275862 · 採用条件未達 · 順位差 -61.724137999999996 / -43.534482999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 20.0,
        "reverse_margin": 70.0
      },
      "new": "007f74ec",
      "score": 70.0
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -20.0,
        "reverse_margin": -13.333333000000003
      },
      "new": "0061c9d8",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.6,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.666666999999997,
        "reverse_margin": -24.666666999999997
      },
      "new": "005db034",
      "score": 45.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7c966ba96d646f9de078da279c91d7ea"></a>

### v15.7.4 [`007c6ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6ac0.md) FUN_007c6ac0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8c9c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8e64.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -45.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8eac.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8efc.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -54.285714
      },
      "new": "007f8c9c",
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
        "margin": 0.0,
        "reverse_margin": -45.333333
      },
      "new": "007f8e64",
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
        "margin": 0.0,
        "reverse_margin": -54.285714
      },
      "new": "007f8eac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d68e31a4cebe11893c802f9b95a7d59e"></a>

### v15.7.4 [`007c6adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6adc.md) FUN_007c6adc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ec8.md) · スコア 69.0 · 採用条件未達 · 順位差 66.0 / 67.2857 · 
- 2. [`007f8efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8efc.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8eac.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f0c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f10.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.0,
        "reverse_margin": 67.2857
      },
      "new": "007f8ec8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8efc",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8eac",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e4eb1629bead120d3dc7bcb0095280e8"></a>

### v15.7.4 [`007c6ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6ae8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed4.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f10.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f0c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8efc.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed8.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f14.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8ed4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8f10",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-68fba57d874de22770377bab2999555c"></a>

### v15.7.4 [`007c6aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6aec.md) FUN_007c6aec

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f8ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8ed8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8efc.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f14.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -73.333333
      },
      "new": "007f8ed8",
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
        "margin": 0.0,
        "reverse_margin": -80.0
      },
      "new": "007f8efc",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8f14",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3156d1e11364278d5994867a3f49cf96"></a>

### v15.7.4 [`007c6b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b10.md) FUN_007c6b10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00af1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c44.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 10.0 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 2. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f88.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -24.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.0,
        "reverse_margin": 10.0
      },
      "new": "00af1c44",
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
        "margin": -60.0,
        "reverse_margin": -80.0
      },
      "new": "007f8f5c",
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
        "margin": -60.0,
        "reverse_margin": -24.285714
      },
      "new": "007f8f88",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8918a05ec9cf5528bed0e5b42a9b7b1a"></a>

### v15.7.4 [`007c6b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b20.md) FUN_007c6b20

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f8f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f10.md) · スコア 4.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f8f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f84.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f8f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f78.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fc0.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f88.md) · スコア 0.2857 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f14.md) · スコア 0.2222 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8f10",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8f84",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8f78",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3fee1d2bccee5b951f20144d30ee124a"></a>

### v15.7.4 [`007c6b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b24.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f84.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 69.0 · 
- 2. [`007f8fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fdc.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fd8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f78.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f8fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fc0.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f88.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 69.0
      },
      "new": "007f8f84",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8fdc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-91cc5b277aedd7a2290db8ccd135b22b"></a>

### v15.7.4 [`007c6b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b28.md) FUN_007c6b28

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`007fdccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdccc.md) · スコア 46.666667 · 採用条件未達 · 順位差 3.3333339999999936 / 46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 43.333333 · 採用条件未達 · 順位差 -3.3333339999999936 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 43.333333 · 採用条件未達 · 順位差 -3.3333339999999936 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fe0.md) · スコア 43.333333 · 採用条件未達 · 順位差 -3.3333339999999936 / 43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 36.666667 · 採用条件未達 · 順位差 -10.0 / -26.666666000000006 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 30.0 · 採用条件未達 · 順位差 -16.666666999999997 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 20.512821 · 採用条件未達 · 順位差 -26.153845999999998 / -42.25641 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00694a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a00.md) · スコア 16.666667 · 採用条件未達 · 順位差 -29.999999999999996 / 16.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          0.6666666666666666,
          0.8
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
        "margin": 3.3333339999999936,
        "reverse_margin": 46.666667
      },
      "new": "007fdccc",
      "score": 46.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.5,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.3333339999999936,
        "reverse_margin": -26.666666999999997
      },
      "new": "005db034",
      "score": 43.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.5,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.3333339999999936,
        "reverse_margin": -26.666666999999997
      },
      "new": "00626858",
      "score": 43.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1fdc13a2df478db7351847cf38afa7c5"></a>

### v15.7.4 [`007c6b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b70.md) FUN_007c6b70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8d4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f9028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9028.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f8fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fc0.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / 37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f88.md) · スコア 24.285714 · 採用条件未達 · 順位差 -30.0 / 24.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f8fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fe0.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 17.142857
      },
      "new": "007f8d4c",
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
      "new": "007f9028",
      "score": 54.285714
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
        "reverse_margin": 37.142857
      },
      "new": "007f8fc0",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b2a637ccf8c3efa0a5f5740de7570a2d"></a>

### v15.7.4 [`007c6b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b8c.md) FUN_007c6b8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f9044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9044.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 66.0 · 
- 2. [`007f8fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fc0.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f9028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9028.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f8fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fd8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f8fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fdc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9050.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fe0.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 66.0
      },
      "new": "007f9044",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f8fc0",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9028",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-277bdb9578387df8af0748f805b4e050"></a>

### v15.7.4 [`007c6b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b98.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f8fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fdc.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f9050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9050.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9078.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f9044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9044.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9054.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f8fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fe0.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f9028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9028.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f8fdc",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9050",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0b13eb6dae896a9695949573d09e8bbe"></a>

### v15.7.4 [`007c6b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b9c.md) FUN_007c6b9c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f8fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8fe0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f9028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9028.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9054.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f9078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9078.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -43.333333
      },
      "new": "007f8fe0",
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
        "margin": 0.0,
        "reverse_margin": -54.285714
      },
      "new": "007f9028",
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
        "margin": 0.0,
        "reverse_margin": -73.333333
      },
      "new": "007f9054",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f38c5088dcb359fa9fd30d767b34d9f0"></a>

### v15.7.4 [`007c6bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bc0.md) FUN_007c6bc0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f9078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9078.md) · スコア 50.0 · 採用条件未達 · 順位差 23.333333 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9054.md) · スコア 26.666667 · 採用条件未達 · 順位差 -23.333333 / -46.66666599999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 23.333333,
        "reverse_margin": 50.0
      },
      "new": "007f9078",
      "score": 50.0
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
        "reverse_margin": -46.66666599999999
      },
      "new": "007f9054",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ee4426612d6ebf44a724779b12376f62"></a>

### v15.7.4 [`007c6bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bd0.md) FUN_007c6bd0

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f9088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9088.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`007f9050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9050.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f908c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f908c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9078.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f90d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90d8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9054.md) · スコア 0.4444 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f9090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9090.md) · スコア 0.2222 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "007f9088",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9050",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f908c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-470ac29b8a1eb4356ad8c2318f07f112"></a>

### v15.7.4 [`007c6bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bd4.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f908c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f908c.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f9088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9088.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9078.md) · スコア 1.9375 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f90f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90f4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9054.md) · スコア 0.9283 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f9090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9090.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f90d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90d8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "007f908c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9088",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5be6ccddbfdf94668911bd1b766d164f"></a>

### v15.7.4 [`007c6bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6bd8.md) FUN_007c6bd8

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f9090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9090.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 70.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 38.666667 · 採用条件未達 · 順位差 -31.333333000000003 / -24.666666000000006 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 31.666667 · 採用条件未達 · 順位差 -38.333332999999996 / -18.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 20.512821 · 採用条件未達 · 順位差 -49.487179 / -42.25641 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0062677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md) · スコア 8.275862 · 採用条件未達 · 順位差 -61.724137999999996 / -43.534482999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005dbf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf3c.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -41.921182 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 0.0
      },
      "new": "005db034",
      "score": 70.0
    },
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
        "reverse_margin": 0.0
      },
      "new": "00626858",
      "score": 70.0
    },
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
      "new": "007f9090",
      "score": 70.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-98a0ff599c253b0dd44ffda88c2916be"></a>

### v15.7.4 [`007c6c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c20.md) FUN_007c6c20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831f38.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0088a478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a478.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`007f8dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8dfc.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`007f90d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90d8.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`007f9138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9138.md) · スコア 37.142857 · 採用条件未達 · 順位差 -42.857143 / -6.857143000000001 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f9104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9104.md) · スコア 24.615385 · 採用条件未達 · 順位差 -55.384615 / -9.230768999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f9090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9090.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 25.714286
      },
      "new": "00831f38",
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
        "reverse_margin": 25.714286
      },
      "new": "0088a478",
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
        "reverse_margin": 0.0
      },
      "new": "007f8dfc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f13b886d04766930dc731c07fa9415b"></a>

### v15.7.4 [`007c6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c3c.md) FUN_007c6c3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f90f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90f4.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 67.2857 · 
- 2. [`007f9138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9138.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f90d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90d8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9100.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f914c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f914c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9150.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f9104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9104.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 67.2857
      },
      "new": "007f90f4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9138",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f90d8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-36748695619873577d0f8a88c5140895"></a>

### v15.7.4 [`007c6c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c48.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f9100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9100.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 71.6667 · 
- 2. [`007f9150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9150.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f914c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f914c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f90f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f90f4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9138.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f9104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9104.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f9154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9154.md) · スコア 0.4861 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 71.6667
      },
      "new": "007f9100",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9150",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e1f683fa6309c774a5aa2a368ee7f445"></a>

### v15.7.4 [`007c6c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c4c.md) FUN_007c6c4c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f9104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9104.md) · スコア 33.846154 · 採用条件未達 · 順位差 7.179486999999998 / 9.230768999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f9138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9138.md) · スコア 26.666667 · 採用条件未達 · 順位差 -7.179486999999998 / -17.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f91b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91b8.md) · スコア 26.666667 · 採用条件未達 · 順位差 -7.179486999999998 / -10.476189999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f9154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9154.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.846154 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.23076923076923078
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
        "margin": 7.179486999999998,
        "reverse_margin": 9.230768999999999
      },
      "new": "007f9104",
      "score": 33.846154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
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
        "margin": -7.179486999999998,
        "reverse_margin": -17.333333
      },
      "new": "007f9138",
      "score": 26.666667
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
        "margin": -7.179486999999998,
        "reverse_margin": -10.476189999999999
      },
      "new": "007f91b8",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0555d5dd4159879c0d4a51ce8051e165"></a>

### v15.7.4 [`007c6c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c70.md) FUN_007c6c70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f9138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9138.md) · スコア 44.0 · 採用条件未達 · 順位差 6.857143000000001 / 6.857143000000001 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f91b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91b8.md) · スコア 37.142857 · 採用条件未達 · 順位差 -6.857143000000001 / 10.476189999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 6.857143000000001,
        "reverse_margin": 6.857143000000001
      },
      "new": "007f9138",
      "score": 44.0
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
        "margin": -6.857143000000001,
        "reverse_margin": 10.476189999999999
      },
      "new": "007f91b8",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aa48e979b29c7d2abca3c34834f24bb3"></a>

### v15.7.4 [`007c6c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c80.md) FUN_007c6c80

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f9150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9150.md) · スコア 4.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`007f91e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91e0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f91d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f921c.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f91b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91b8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f91e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91e4.md) · スコア 0.2857 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f9154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9154.md) · スコア 0.16 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f9150",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f91e0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f91d4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ff74d1a3afb1206f07b237c9e5f067a6"></a>

### v15.7.4 [`007c6c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c84.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f91e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91e0.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f9234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f91d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f921c.md) · スコア 0.9792 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f91b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91b8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f91e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91e4.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f9154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9154.md) · スコア 0.4861 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "007f91e0",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9234",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1bed39ec6563e739389d2ef2d016f1c3"></a>

### v15.7.4 [`007c6c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c88.md) FUN_007c6c88

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 38.666667 · 採用条件未達 · 順位差 -31.333333000000003 / -24.666666000000006 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 31.666667 · 採用条件未達 · 順位差 -38.333332999999996 / -18.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 20.512821 · 採用条件未達 · 順位差 -49.487179 / -42.25641 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0062677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md) · スコア 8.275862 · 採用条件未達 · 順位差 -61.724137999999996 / -43.534482999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0061e428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e428.md) · スコア 5.333333 · 採用条件未達 · 順位差 -64.666667 / -19.111111 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005dbf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf3c.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -41.921182 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 0.0
      },
      "new": "005db034",
      "score": 70.0
    },
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
        "reverse_margin": 0.0
      },
      "new": "00626858",
      "score": 70.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.4444444444444444
        ],
        "cfg_coverage": [
          0.75,
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
        "margin": -31.333333000000003,
        "reverse_margin": -24.666666000000006
      },
      "new": "0061c9d8",
      "score": 38.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dbe43a065434bf0c12737b59f4cfaa4e"></a>

### v15.7.4 [`007c6cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cd0.md) FUN_007c6cd0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8eac.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f943c.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007f921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f921c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / 37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f91e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f91e4.md) · スコア 24.285714 · 採用条件未達 · 順位差 -30.0 / 24.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 54.285714
      },
      "new": "007f8eac",
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
        "reverse_margin": 17.142857
      },
      "new": "007f943c",
      "score": 54.285714
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
        "reverse_margin": 37.142857
      },
      "new": "007f921c",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bb19df6c94d71286951dc30a54c3df82"></a>

### v15.7.4 [`007c6cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cec.md) FUN_007c6cec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9458.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 66.0 · 
- 2. [`007f921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f921c.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f943c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9234.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f9238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9238.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9464.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md) · スコア 0.0938 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 66.0
      },
      "new": "007f9458",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f921c",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f943c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-185534a65582335c36acf14f26d6f3de"></a>

### v15.7.4 [`007c6cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cf8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f9238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9238.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 71.6667 · 
- 2. [`007f9464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9464.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9458.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9468.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f943c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f923c.md) · スコア 0.0312 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 71.6667
      },
      "new": "007f9238",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9464",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-22dfa5ef2d9ea79295b803aeb75558ac"></a>

### v15.7.4 [`007c6cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cfc.md) FUN_007c6cfc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007f9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9468.md) · スコア 33.846154 · 採用条件未達 · 順位差 7.179486999999998 / 9.230768999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f943c.md) · スコア 26.666667 · 採用条件未達 · 順位差 -7.179486999999998 / -27.619047 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f949c.md) · スコア 26.666667 · 採用条件未達 · 順位差 -7.179486999999998 / -17.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.23076923076923078
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
        "margin": 7.179486999999998,
        "reverse_margin": 9.230768999999999
      },
      "new": "007f9468",
      "score": 33.846154
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
        "margin": -7.179486999999998,
        "reverse_margin": -27.619047
      },
      "new": "007f943c",
      "score": 26.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
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
        "margin": -7.179486999999998,
        "reverse_margin": -17.333333
      },
      "new": "007f949c",
      "score": 26.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5d9d9d7864e2d8ca18e6cbc70ec06f64"></a>

### v15.7.4 [`007c6d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d20.md) FUN_007c6d20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f949c.md) · スコア 44.0 · 採用条件未達 · 順位差 6.857143000000001 / 17.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f943c.md) · スコア 37.142857 · 採用条件未達 · 順位差 -6.857143000000001 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9468.md) · スコア 24.615385 · 採用条件未達 · 順位差 -19.384615 / -9.230768999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 6.857143000000001,
        "reverse_margin": 17.333333
      },
      "new": "007f949c",
      "score": 44.0
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
        "margin": -6.857143000000001,
        "reverse_margin": -17.142857
      },
      "new": "007f943c",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
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
        "margin": -19.384615,
        "reverse_margin": -9.230768999999999
      },
      "new": "007f9468",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b27dac2b63c1350ca34e593a84bba792"></a>

### v15.7.4 [`007c6d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d30.md) FUN_007c6d30

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 0件 

- 1. [`007f94b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b0.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`007f9464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9464.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9458.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f949c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9468.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) · スコア 0.16 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "007f94b0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9464",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f94b4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d02aef134d2bbb72b75b4a642e9c510e"></a>

### v15.7.4 [`007c6d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d34.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`007f94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b4.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 69.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f94b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9538.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f949c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f949c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9468.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f951c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f951c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) · スコア 0.4861 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 69.0
      },
      "new": "007f94b4",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f94b0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-52a78f0556713e0ecc51bc552c262b8e"></a>

### v15.7.4 [`007c6d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d38.md) FUN_007c6d38

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`008acf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf98.md) · スコア 45.714286 · 採用条件未達 · 順位差 3.8095240000000032 / 45.714286 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 41.904762 · 採用条件未達 · 順位差 -3.8095240000000032 / -28.095238000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 41.904762 · 採用条件未達 · 順位差 -3.8095240000000032 / -28.095238000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) · スコア 35.238095 · 採用条件未達 · 順位差 -10.476191 / -28.095238000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) · スコア 29.52381 · 採用条件未達 · 順位差 -16.190476 / -20.47619 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) · スコア 25.371429 · 採用条件未達 · 順位差 -20.342857000000002 / -30.628571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) · スコア 20.512821 · 採用条件未達 · 順位差 -25.201465000000002 / -42.25641 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0062677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md) · スコア 8.275862 · 採用条件未達 · 順位差 -37.438424 / -43.534482999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          0.2857142857142857,
          0.2857142857142857
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
        "margin": 3.8095240000000032,
        "reverse_margin": 45.714286
      },
      "new": "008acf98",
      "score": 45.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.8095240000000032,
        "reverse_margin": -28.095238000000002
      },
      "new": "005db034",
      "score": 41.904762
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.8095240000000032,
        "reverse_margin": -28.095238000000002
      },
      "new": "00626858",
      "score": 41.904762
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-511b66a6049505e6dd95e901fbfa22ef"></a>

### v15.7.4 [`007c6d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d80.md) FUN_007c6d80

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f8/007f8f5c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f951c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f951c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f9548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9548.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -67.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9580.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "007f8f5c",
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
        "margin": 0.0,
        "reverse_margin": -56.0
      },
      "new": "007f94b8",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f951c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e27264fcbd24fa8f849eea110e9f3088"></a>

### v15.7.4 [`007c6d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d9c.md) FUN_007c6d9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f9538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9538.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 67.2857 · 
- 2. [`007f9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9580.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007f951c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f951c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`007f9544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9544.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007f9598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9598.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007f9548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f9548.md) · スコア 0.8571 · 採用条件未達 · 順位差 — / — · 
- 7. [`007f94b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f9/007f94b8.md) · スコア 0.48 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 67.2857
      },
      "new": "007f9538",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f9580",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007f951c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

