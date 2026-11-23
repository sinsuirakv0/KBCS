# v15.7.4 → v16.0.0 · 追加調査 (65)

[一覧の目次](README.md)

<a id="review-557a05236f65f4d326ff751db077af71"></a>

### v15.7.4 [`008797ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/008797ec.md) FUN_008797ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ac98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac98c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ac970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac970.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008ac918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md) · スコア 0.5455 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ac98c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ac970",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ac918",
      "score": 0.5455
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ad99c52c1b450a6bcd7179efafc59c28"></a>

### v15.7.4 [`00879a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a3c.md) FUN_00879a3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0061eb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb8c.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 42.857143 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008acbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acbdc.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 42.857143
      },
      "new": "0061eb8c",
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
      "new": "008acbdc",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9e31be703f234799198f06473281e2e4"></a>

### v15.7.4 [`00879a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a4c.md) FUN_00879a4c

`competing_candidates` 

呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 0件 

- 1. [`008acbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acbec.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008acbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acbdc.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acbec",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acbdc",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-15daa3b54aeb46be2f371a8215d212aa"></a>

### v15.7.4 [`00879a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879a9c.md) FUN_00879a9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc3c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008acc3c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6c863c84364dd1a582fccfa495f7937c"></a>

### v15.7.4 [`00879ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ab8.md) FUN_00879ab8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc58.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008acc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc3c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acc58",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acc3c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9ea630b6500cc970991407a66465882b"></a>

### v15.7.4 [`00879aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879aec.md) FUN_00879aec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc8c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "008acc8c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9e9e3e0468d3cd684819926ae84561da"></a>

### v15.7.4 [`00879afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879afc.md) FUN_00879afc

`competing_candidates` 

呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 0件 

- 1. [`008acc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc9c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008acc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acc8c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acc9c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acc8c",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-17e3e349283287a6a5071405bddb4a92"></a>

### v15.7.4 [`00879b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b04.md) FUN_00879b04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acca4.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`008accc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008accc4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008acca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acca8.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acca4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008accc4",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acca8",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b0ce827594e7ebe86283dafe0a83b28b"></a>

### v15.7.4 [`00879b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b08.md) FUN_00879b08

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acca8.md) · スコア 54.285714 · 採用条件未達 · 順位差 20.0 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`009a3120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3120.md) · スコア 34.285714 · 採用条件未達 · 順位差 -20.0 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 20.0
      },
      "new": "008acca8",
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
      "new": "009a3120",
      "score": 34.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-03423422f48df3c539f49e3733c0873a"></a>

### v15.7.4 [`00879b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b24.md) FUN_00879b24

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008accc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008accc4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008acca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acca8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008acca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acca4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008accc4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acca8",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acca4",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-13e8312073c154b5fb52f416fbc1d166"></a>

### v15.7.4 [`00879b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b58.md) FUN_00879b58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008accf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008accf8.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008accf8",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-09722e28a9ae44d518cd979505d8861e"></a>

### v15.7.4 [`00879b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b68.md) FUN_00879b68

`competing_candidates` 

呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 0件 

- 1. [`008acd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acd08.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008accf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008accf8.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acd08",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008accf8",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ecd2d47363e93e691316acbc67a245f5"></a>

### v15.7.4 [`00879d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879d90.md) FUN_00879d90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf30.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008acf30",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3e715a6c1860d9f7fd32cf3f1158c4c"></a>

### v15.7.4 [`00879dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879dac.md) FUN_00879dac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf4c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008acf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf30.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acf4c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acf30",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b6a2ff19fba933aee1bbb0cbc83b2dd7"></a>

### v15.7.4 [`00879e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879e40.md) FUN_00879e40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acfe0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -42.857143
      },
      "new": "008acfe0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-29c0bba717490a4b590a78634d71c02a"></a>

### v15.7.4 [`00879e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879e5c.md) FUN_00879e5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008acffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acffc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008acfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acfe0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008acffc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008acfe0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-866ef20e44a31f3b1028cabafd24277a"></a>

### v15.7.4 [`00879e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879e90.md) FUN_00879e90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad030.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008ad030",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6144ad221e591d589038042c95ee1b21"></a>

### v15.7.4 [`00879ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ea0.md) FUN_00879ea0

`competing_candidates` 

呼出元 1件 [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 0件 

- 1. [`008ad040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad040.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008ad030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad030.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad040",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad030",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cb8ddf5356f81d18805223203ec7fdf0"></a>

### v15.7.4 [`00879f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879f7c.md) FUN_00879f7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad11c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008ad11c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-edf4b21c215a73343eea23582fa206f4"></a>

### v15.7.4 [`00879f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879f98.md) FUN_00879f98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad138.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ad11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad11c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad138",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad11c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9cfd86a4124741f0f2b562ca98d0fb4c"></a>

### v15.7.4 [`0087a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a0c4.md) FUN_0087a0c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad264.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008ad264",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5f7f9f2edcdde8085636e43c88ba2da7"></a>

### v15.7.4 [`0087a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a0e0.md) FUN_0087a0e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad280.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ad264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad264.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad280",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad264",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6ea877c7045494b58906d58a0f924966"></a>

### v15.7.4 [`0087a4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4a8.md) FUN_0087a4a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0059b19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b19c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008ad648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad648.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0059b19c",
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
      "new": "008ad648",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d7e56b3c14f86ba44dbbc764828cab38"></a>

### v15.7.4 [`0087a4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a4c4.md) FUN_0087a4c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad664.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ad648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad648.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad664",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad648",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bcf9a7f60a06bda75831042835ee0255"></a>

### v15.7.4 [`0087a558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a558.md) FUN_0087a558

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6f8.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008ad6f8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5dfeea58809075057e65e80fcf7b89b1"></a>

### v15.7.4 [`0087a574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a574.md) FUN_0087a574

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ad714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad714.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ad6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6f8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad714",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad6f8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0bdecaa51bd46bd8b1f293551852643c"></a>

### v15.7.4 [`0087a5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5a8.md) FUN_0087a5a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00626c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c54.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008ad748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad748.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00626c54",
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
      "new": "008ad748",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b81fabe31dd3b7e9533fade1dbcb6b0a"></a>

### v15.7.4 [`0087a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a5b8.md) FUN_0087a5b8

`competing_candidates` 

呼出元 1件 [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 0件 

- 1. [`008ad758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad758.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`008ad748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad748.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ad758",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ad748",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f8bfbdaaa34ff99660674dcb4f8f96f9"></a>

### v15.7.4 [`0087a9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a9d8.md) FUN_0087a9d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adb78.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008adb78",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8810e6472fbe872bc9eaca137d5b75f2"></a>

### v15.7.4 [`0087a9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087a9f4.md) FUN_0087a9f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adb94.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008adb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adb78.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008adb94",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008adb78",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e3dcd5276014556ab36ecf1fa24851d3"></a>

### v15.7.4 [`0087aa58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa58.md) FUN_0087aa58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adbf8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008adbf8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a48ba453ea0ea3878b7af38a1ae5d633"></a>

### v15.7.4 [`0087aa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aa74.md) FUN_0087aa74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc14.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008adbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adbf8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008adc14",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008adbf8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d97bf4d5eb48e69e7f16331b96d50590"></a>

### v15.7.4 [`0087aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aad8.md) FUN_0087aad8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc78.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "008adc78",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56dd8320bb359926a0f9d5b24b1b0da7"></a>

### v15.7.4 [`0087aaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aaf4.md) FUN_0087aaf4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc94.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008adc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc78.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008adc94",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008adc78",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-088c1d0493c626f272fda4e78f02152e"></a>

### v15.7.4 [`0087ab38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab38.md) FUN_0087ab38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008adcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adcd8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008adcd8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-45b2c3a92611f8cbf3f58486f34b0a53"></a>

### v15.7.4 [`0087ab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab4c.md) FUN_0087ab4c

`competing_candidates` 

呼出元 1件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 0件 

- 1. [`008adcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adcec.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`008adcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adcd8.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008adcec",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008adcd8",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c84b2b572063df59ca50cffa5354f99c"></a>

### v15.7.4 [`0087ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ac8c.md) FUN_0087ac8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ade2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ade2c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008ade2c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-494d865dc5d697f24b307200bec2c055"></a>

### v15.7.4 [`0087aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087aca8.md) FUN_0087aca8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008ade48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ade48.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008ade2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ade2c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008ade48",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008ade2c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-acab7d23d52faa525a080b94e900f047"></a>

### v15.7.4 [`00883c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c6c.md) FUN_00883c6c

`competing_candidates` [`008b6e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e0c.md)

呼出元 2件 [`0060afa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060afa4.md) [`0075772c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075772c.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00883bb8",
    "00883c74",
    "008b6d58",
    "008b6e14"
  ],
  "initial_reason": ""
}
~~~

<a id="review-6e3a677ef0e19f455614c9c1c79cbbf3"></a>

### v15.7.4 [`00883cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc8.md) FUN_00883cc8

`competing_candidates` [`008b6e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e68.md)

呼出元 7件 [`005a2bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2bb0.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007c4dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4dd8.md) [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00883cc0",
    "00883cd8",
    "008b6e60",
    "008b6e78"
  ],
  "initial_reason": ""
}
~~~

<a id="review-b7c462506e99c5b13fa8c090d402732d"></a>

### v15.7.4 [`00883cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cd0.md) FUN_00883cd0

`competing_candidates` [`008b6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e70.md)

呼出元 7件 [`006059a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006059a0.md) [`00664710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664710.md) [`006aad48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006aa/006aad48.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`0088c5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c5f0.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00883cc0",
    "00883cd8",
    "008b6e60",
    "008b6e78"
  ],
  "initial_reason": ""
}
~~~

<a id="review-44bf16221c1abd693e4e90b9057c7be0"></a>

### v15.7.4 [`00885170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885170.md) FUN_00885170

`competing_candidates` 

呼出元 3件 [`00887594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887594.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`00887e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887e18.md) · 呼出先 20件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

- 1. [`008b8310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b8310.md) · スコア 48.878698 · 採用条件未達 · 順位差 11.452575000000003 / 12.023147000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a81740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a81/00a81740.md) · スコア 37.426123 · 採用条件未達 · 順位差 -11.452575000000003 / 37.426123 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b36fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36fb4.md) · スコア 1.828991 · 採用条件未達 · 順位差 -47.049707 / 1.828991 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · スコア 1.161042 · 採用条件未達 · 順位差 -47.717656 / 1.161042 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0079061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/0079061c.md) · スコア 1.147054 · 採用条件未達 · 順位差 -47.731644 / -46.285378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a91c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a91c18.md) · スコア 1.021158 · 採用条件未達 · 順位差 -47.85754 / 1.021158 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) · スコア 0.734394 · 採用条件未達 · 順位差 -48.144304 / 0.734394 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md) · スコア 0.734394 · 採用条件未達 · 順位差 -48.144304 / 0.734394 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7037943696450428,
          0.6995133819951338
        ],
        "cfg_coverage": [
          0.3488372093023256,
          0.34539473684210525
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.452575000000003,
        "reverse_margin": 12.023147000000002
      },
      "new": "008b8310",
      "score": 48.878698
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5263157894736842,
          0.6323529411764706
        ],
        "cfg_coverage": [
          0.292358803986711,
          0.34375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -11.452575000000003,
        "reverse_margin": 37.426123
      },
      "new": "00a81740",
      "score": 37.426123
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02937576499388005,
          0.11483253588516747
        ],
        "cfg_coverage": [
          0.0033222591362126247,
          0.017857142857142856
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -47.049707,
        "reverse_margin": 1.828991
      },
      "new": "00b36fb4",
      "score": 1.828991
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fc568eb68844cd4dc561ac0137167c74"></a>

### v15.7.4 [`0088654c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088654c.md) FUN_0088654c

`competing_candidates` 

呼出元 1件 [`007c8c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c78.md) · 呼出先 0件 

- 1. [`008b9798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9798.md) · スコア 84.0 · 採用条件未達 · 順位差 71.3158 / 71.3158 · 
- 2. [`008b97a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97a4.md) · スコア 12.6842 · 採用条件未達 · 順位差 — / — · 
- 3. [`008b97bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97bc.md) · スコア 12.6842 · 採用条件未達 · 順位差 — / — · 
- 4. [`008b978c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b978c.md) · スコア 11.5 · 採用条件未達 · 順位差 — / — · 
- 5. [`008b97b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97b0.md) · スコア 9.25 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 71.3158,
        "reverse_margin": 71.3158
      },
      "new": "008b9798",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008b97a4",
      "score": 12.6842
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008b97bc",
      "score": 12.6842
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-72e84465bc8400e2b8109be745f068a7"></a>

### v15.7.4 [`00886558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886558.md) FUN_00886558

`competing_candidates` 

呼出元 1件 [`007c8c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c78.md) · 呼出先 0件 

- 1. [`008b97a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97a4.md) · スコア 84.0 · 採用条件未達 · 順位差 71.3158 / 71.3158 · 
- 2. [`008b9798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9798.md) · スコア 12.6842 · 採用条件未達 · 順位差 — / — · 
- 3. [`008b97bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97bc.md) · スコア 12.6842 · 採用条件未達 · 順位差 — / — · 
- 4. [`008b978c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b978c.md) · スコア 9.25 · 採用条件未達 · 順位差 — / — · 
- 5. [`008b97b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97b0.md) · スコア 9.25 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 71.3158,
        "reverse_margin": 71.3158
      },
      "new": "008b97a4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008b9798",
      "score": 12.6842
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008b97bc",
      "score": 12.6842
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b0d381c178d0541a50760b32576375f1"></a>

### v15.7.4 [`008865b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b8.md) FUN_008865b8

`competing_candidates` 

呼出元 1件 [`00888268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888268.md) · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829328.md)

- 1. [`008b981c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b981c.md) · スコア 61.417481 · 採用条件未達 · 順位差 57.485885 / 57.451402 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008bbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bbd90.md) · スコア 3.931596 · 採用条件未達 · 順位差 -57.485885 / 3.931596 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`004ccc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004ccc3c.md) · スコア 3.127036 · 採用条件未達 · 順位差 -58.290445000000005 / 3.127036 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a84534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84534.md) · スコア 1.701412 · 採用条件未達 · 順位差 -59.716069000000005 / 1.701412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0078fc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fc34.md) · スコア 1.534745 · 採用条件未達 · 順位差 -59.882736 / 1.534745 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0065f778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md) · スコア 1.368078 · 採用条件未達 · 順位差 -60.049403000000005 / -17.141066 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · スコア 1.172638 · 採用条件未達 · 順位差 -60.244843 / -32.725363 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0065f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md) · スコア 0.781759 · 採用条件未達 · 順位差 -60.635722 / -18.565853 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8208469055374593,
          0.8208469055374593
        ],
        "cfg_coverage": [
          0.6083333333333333,
          0.6293103448275862
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 57.485885,
        "reverse_margin": 57.451402
      },
      "new": "008b981c",
      "score": 61.417481
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.048859934853420196,
          0.11450381679389313
        ],
        "cfg_coverage": [
          0.05,
          0.15384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -57.485885,
        "reverse_margin": 3.931596
      },
      "new": "008bbd90",
      "score": 3.931596
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05211726384364821,
          0.05460750853242321
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
        "margin": -58.290445000000005,
        "reverse_margin": 3.127036
      },
      "new": "004ccc3c",
      "score": 3.127036
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0cf431b11ca1a21741de7c1ba1978d7a"></a>

### v15.7.4 [`00886a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886a84.md) FUN_00886a84

`competing_candidates` 

呼出元 3件 [`005e97d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e9/005e97d8.md) [`005ee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ee/005ee758.md) [`00888720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888720.md) · 呼出先 21件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md)

- 1. [`008b9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9ce8.md) · スコア 37.384166 · 採用条件未達 · 順位差 32.004856000000004 / 32.081484 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) · スコア 5.37931 · 採用条件未達 · 順位差 -32.004856000000004 / -43.039759000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) · スコア 4.636364 · 採用条件未達 · 順位差 -32.747802 / -40.315525 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`006b6184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b6184.md) · スコア 4.363636 · 採用条件未達 · 順位差 -33.02053 / -43.125658 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) · スコア 4.331034 · 採用条件未達 · 順位差 -33.053132 / -32.991485 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`006122a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00612/006122a4.md) · スコア 4.284698 · 採用条件未達 · 順位差 -33.099468 / -34.074254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`006797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006797c0.md) · スコア 4.163711 · 採用条件未達 · 順位差 -33.220455 / -41.898949 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`00925834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00925/00925834.md) · スコア 4.157895 · 採用条件未達 · 順位差 -33.226271 / -35.026787999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

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
          0.4918032786885246
        ],
        "cfg_coverage": [
          0.1937984496124031,
          0.23148148148148148
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 32.004856000000004,
        "reverse_margin": 32.081484
      },
      "new": "008b9ce8",
      "score": 37.384166
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02727272727272727,
          0.022988505747126436
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
        "margin": -32.004856000000004,
        "reverse_margin": -43.039759000000004
      },
      "new": "005f5750",
      "score": 5.37931
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.010606060606060607,
          0.014314928425357873
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
        "margin": -32.747802,
        "reverse_margin": -40.315525
      },
      "new": "005c7cc0",
      "score": 4.636364
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2723090d8168a8c50a36b0bff656ef15"></a>

### v15.7.4 [`00887594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887594.md) FUN_00887594

`competing_candidates` 

呼出元 64件 [`005a7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md) [`005b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00885170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885170.md) [`008879b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879b8.md) [`0088923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/0088923c.md)

- 1. [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) · スコア 63.875556 · 採用条件未達 · 順位差 28.647424 / 0.6973740000000035 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md) · スコア 35.228132 · 採用条件未達 · 順位差 -28.647424 / 35.228132 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008bb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb0a8.md) · スコア 34.907586 · 採用条件未達 · 順位差 -28.96797 / 34.907586 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004edfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md) · スコア 10.213333 · 採用条件未達 · 順位差 -53.662223000000004 / 10.213333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00560864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md) · スコア 9.662222 · 採用条件未達 · 順位差 -54.213334 / 9.662222 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0087a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a708.md) · スコア 9.662222 · 採用条件未達 · 順位差 -54.213334 / -11.491624000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00519dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519dc0.md) · スコア 4.32 · 採用条件未達 · 順位差 -59.555556 / 4.32 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009e0038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0038.md) · スコア 3.991111 · 採用条件未達 · 順位差 -59.884445 / -9.788793 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.872,
          0.872
        ],
        "cfg_coverage": [
          0.5777777777777777,
          0.6341463414634146
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 28.647424,
        "reverse_margin": 0.6973740000000035
      },
      "new": "008ba824",
      "score": 63.875556
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.556,
          0.556
        ],
        "cfg_coverage": [
          0.18888888888888888,
          0.09340659340659341
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -28.647424,
        "reverse_margin": 35.228132
      },
      "new": "008bac84",
      "score": 35.228132
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.568,
          0.568
        ],
        "cfg_coverage": [
          0.06666666666666667,
          0.041379310344827586
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -28.96797,
        "reverse_margin": 34.907586
      },
      "new": "008bb0a8",
      "score": 34.907586
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-737d89ece6f78843c15d41c441ff16cf"></a>

### v15.7.4 [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) FUN_008895f4

`competing_candidates` 

呼出元 1件 [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) · 呼出先 14件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008bc884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc884.md) · スコア 11.76 · 採用条件未達 · 順位差 8.96 / 8.351372999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ac20e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md) · スコア 2.8 · 採用条件未達 · 順位差 -8.96 / 2.8 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00908178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00908/00908178.md) · スコア 2.68459 · 採用条件未達 · 順位差 -9.07541 / -3.4233719999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · スコア 2.426667 · 採用条件未達 · 順位差 -9.333333 / -11.922419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) · スコア 2.421321 · 採用条件未達 · 順位差 -9.338678999999999 / 2.421321 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) · スコア 2.32 · 採用条件未達 · 順位差 -9.44 / -30.616473 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · スコア 2.286885 · 採用条件未達 · 順位差 -9.473115 / -22.440278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) · スコア 2.241399 · 採用条件未達 · 順位差 -9.518601 / -24.763512 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16266666666666665,
          0.16266666666666665
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
        "margin": 8.96,
        "reverse_margin": 8.351372999999999
      },
      "new": "008bc884",
      "score": 11.76
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013333333333333334,
          0.01910828025477707
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
        "margin": -8.96,
        "reverse_margin": 2.8
      },
      "new": "00ac20e0",
      "score": 2.8
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.016,
          0.010135135135135136
        ],
        "cfg_coverage": [
          0.0041841004184100415,
          0.0038240917782026767
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.07541,
        "reverse_margin": -3.4233719999999996
      },
      "new": "00908178",
      "score": 2.68459
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a2e8eb1a616094838abfc16202893531"></a>

### v15.7.4 [`0088c2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c2d8.md) FUN_0088c2d8

`competing_candidates` 

呼出元 2件 [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) [`008983c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/008983c8.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)

- 1. [`008bf568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf568.md) · スコア 60.71024 · 採用条件未達 · 順位差 49.284960999999996 / 47.245629 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`008cbde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbde8.md) · スコア 11.425279 · 採用条件未達 · 順位差 -49.284960999999996 / 11.425279 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 3. [`008c0d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md) · スコア 7.538694 · 採用条件未達 · 順位差 -53.171546 / -61.825104 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · スコア 5.512112 · 採用条件未達 · 順位差 -55.198128 / -45.545184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) · スコア 4.507614 · 採用条件未達 · 順位差 -56.202625999999995 / -36.081807 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) · スコア 4.507614 · 採用条件未達 · 順位差 -56.202625999999995 / -37.781001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) · スコア 4.259179 · 採用条件未達 · 順位差 -56.451060999999996 / -7.775378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7908496732026143,
          0.7908496732026143
        ],
        "cfg_coverage": [
          0.46296296296296297,
          0.5319148936170213
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 49.284960999999996,
        "reverse_margin": 47.245629
      },
      "new": "008bf568",
      "score": 60.71024
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17647058823529413,
          0.1134453781512605
        ],
        "cfg_coverage": [
          0.05555555555555555,
          0.030927835051546393
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -49.284960999999996,
        "reverse_margin": 11.425279
      },
      "new": "008cbde8",
      "score": 11.425279
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13071895424836602,
          0.04405286343612335
        ],
        "cfg_coverage": [
          0.05555555555555555,
          0.04477611940298507
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -53.171546,
        "reverse_margin": -61.825104
      },
      "new": "008c0d3c",
      "score": 7.538694
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0b3a2151c30663a7f798e63137b71c92"></a>

### v15.7.4 [`0088c580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c580.md) FUN_0088c580

`competing_candidates` 

呼出元 3件 [`0088c2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c2d8.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`0089c544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089c544.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md) [`00a6b4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b4f8.md)

- 1. [`008bf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf810.md) · スコア 52.0 · 採用条件未達 · 順位差 4.285713999999999 / 4.285713999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008c2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2878.md) · スコア 47.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009cc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc994.md) · スコア 32.857143 · 採用条件未達 · 順位差 -19.142857 / 32.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00641f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641f00.md) · スコア 27.769231 · 採用条件未達 · 順位差 -24.230769 / -2.3076919999999994 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ac948c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md) · スコア 5.934426 · 採用条件未達 · 順位差 -46.065574 / 5.934426 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006311dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006311dc.md) · スコア 2.0 · 採用条件未達 · 順位差 -50.0 / -28.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00631224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/00631224.md) · スコア 2.0 · 採用条件未達 · 順位差 -50.0 / -30.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0063126c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/0063126c.md) · スコア 2.0 · 採用条件未達 · 順位差 -50.0 / -56.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.285713999999999,
        "reverse_margin": 4.285713999999999
      },
      "new": "008bf810",
      "score": 52.0
    },
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
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "008c2878",
      "score": 47.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21428571428571427,
          0.3157894736842105
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
        "margin": -19.142857,
        "reverse_margin": 32.857143
      },
      "new": "009cc994",
      "score": 32.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11f7bc7b23a207b02338af154ba30170"></a>

### v15.7.4 [`0088c5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c5f0.md) FUN_0088c5f0

`competing_candidates` 

呼出元 1件 [`0089b410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b410.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c74.md)

- 1. [`008bf880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf880.md) · スコア 31.849885 · 採用条件未達 · 順位差 25.952093 / 25.837479000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`008c02f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c02f0.md) · スコア 5.897792 · 採用条件未達 · 順位差 -25.952093 / -21.660303000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`008c0d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md) · スコア 5.366207 · 採用条件未達 · 順位差 -26.483678 / -63.997591 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · スコア 5.341378 · 採用条件未達 · 順位差 -26.508507 / -45.715918 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`008cbde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbde8.md) · スコア 5.088 · 採用条件未達 · 順位差 -26.761885 / 5.088 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) · スコア 4.43038 · 採用条件未達 · 順位差 -27.419505 / -24.784903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`00645254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645254.md) · スコア 4.361446 · 採用条件未達 · 順位差 -27.488439 / -28.472138 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) · スコア 4.360695 · 採用条件未達 · 順位差 -27.48919 / -22.593526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.41731066460587324,
          0.41731066460587324
        ],
        "cfg_coverage": [
          0.14056224899598393,
          0.16055045871559634
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 25.952093,
        "reverse_margin": 25.837479000000002
      },
      "new": "008bf880",
      "score": 31.849885
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02627511591962906,
          0.0265625
        ],
        "cfg_coverage": [
          0.01606425702811245,
          0.017777777777777778
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -25.952093,
        "reverse_margin": -21.660303000000003
      },
      "new": "008c02f0",
      "score": 5.897792
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02009273570324575,
          0.028634361233480177
        ],
        "cfg_coverage": [
          0.008032128514056224,
          0.029850746268656716
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -26.483678,
        "reverse_margin": -63.997591
      },
      "new": "008c0d3c",
      "score": 5.366207
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cc586a2e76cb690636efdc9c84d60a56"></a>

### v15.7.4 [`0088d060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088d/0088d060.md) FUN_0088d060

`competing_candidates` 

呼出元 1件 [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00827b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827b94.md)

- 1. [`008c02f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c02f0.md) · スコア 27.558095 · 採用条件未達 · 順位差 21.545689000000003 / 21.660303000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`008bf880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf880.md) · スコア 6.012406 · 採用条件未達 · 順位差 -21.545689000000003 / -25.837479000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0068aa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068aa48.md) · スコア 5.3125 · 採用条件未達 · 順位差 -22.245595 / 5.3125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`008c0d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md) · スコア 5.019961 · 採用条件未達 · 順位差 -22.538134 / -64.34383700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`006d3dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md) · スコア 4.985915 · 採用条件未達 · 順位差 -22.572180000000003 / -33.175724 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`008cbde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbde8.md) · スコア 4.644961 · 採用条件未達 · 順位差 -22.913134 / 4.644961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 7. [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) · スコア 4.1875 · 採用条件未達 · 順位差 -23.370595 / -7.8470569999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`00645254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645254.md) · スコア 4.0 · 採用条件未達 · 順位差 -23.558095 / -28.833584000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.309375,
          0.309375
        ],
        "cfg_coverage": [
          0.14977973568281938,
          0.1511111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 21.545689000000003,
        "reverse_margin": 21.660303000000003
      },
      "new": "008c02f0",
      "score": 27.558095
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025,
          0.02472952086553323
        ],
        "cfg_coverage": [
          0.02643171806167401,
          0.027522935779816515
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -21.545689000000003,
        "reverse_margin": -25.837479000000002
      },
      "new": "008bf880",
      "score": 6.012406
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.021875,
          0.06167400881057269
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
          "already_matched_elsewhere"
        ],
        "margin": -22.245595,
        "reverse_margin": 5.3125
      },
      "new": "0068aa48",
      "score": 5.3125
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-de8ca9c57f5fd97a37b1feecd4119f4d"></a>

### v15.7.4 [`0088daac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088d/0088daac.md) FUN_0088daac

`competing_candidates` 

呼出元 1件 [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) · 呼出先 26件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md) [`00444fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fc4.md)

- 1. [`008c0d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md) · スコア 69.363798 · 採用条件未達 · 順位差 58.398763 / 58.398763 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) · スコア 10.965035 · 採用条件未達 · 順位差 -58.398763 / -29.370629 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`008bf568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf568.md) · スコア 8.578656 · 採用条件未達 · 順位差 -60.785142 / -52.131584 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · スコア 7.024668 · 採用条件未達 · 順位差 -62.339130000000004 / -44.032628 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) · スコア 5.85022 · 採用条件未達 · 順位差 -63.513578 / -32.937659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) · スコア 5.322835 · 採用条件未達 · 順位差 -64.040963 / -25.694069 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) · スコア 4.858896 · 採用条件未達 · 順位差 -64.504902 / -40.092993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) · スコア 4.406091 · 採用条件未達 · 順位差 -64.957707 / -36.18333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7973568281938326,
          0.7973568281938326
        ],
        "cfg_coverage": [
          0.8387096774193549,
          0.7761194029850746
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 58.398763,
        "reverse_margin": 58.398763
      },
      "new": "008c0d3c",
      "score": 69.363798
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1828193832599119,
          0.11608391608391608
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
        "margin": -58.398763,
        "reverse_margin": -29.370629
      },
      "new": "006d4d54",
      "score": 10.965035
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04405286343612335,
          0.13071895424836602
        ],
        "cfg_coverage": [
          0.0967741935483871,
          0.1276595744680851
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -60.785142,
        "reverse_margin": -52.131584
      },
      "new": "008bf568",
      "score": 8.578656
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0bfc105081303fd69764b23e1047977f"></a>

### v15.7.4 [`0088e208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md) FUN_0088e208

`competing_candidates` 

呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008c1498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c1/008c1498.md) · スコア 38.895455 · 採用条件未達 · 順位差 36.820361 / 37.150695999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · スコア 2.075094 · 採用条件未達 · 順位差 -36.820361 / -23.477548 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · スコア 2.0 · 採用条件未達 · 順位差 -36.895455 / -40.751085 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) · スコア 2.0 · 採用条件未達 · 順位差 -36.895455 / -19.720849 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) · スコア 2.0 · 採用条件未達 · 順位差 -36.895455 / -64.882353 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0089a514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a514.md) · スコア 2.0 · 採用条件未達 · 順位差 -36.895455 / -9.286822 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) · スコア 2.0 · 採用条件未達 · 順位差 -36.895455 / -24.281092 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00c1bd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md) · スコア 1.848809 · 採用条件未達 · 順位差 -37.046645999999996 / 1.848809 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4893203883495146,
          0.4893203883495146
        ],
        "cfg_coverage": [
          0.4444444444444444,
          0.37681159420289856
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.820361,
        "reverse_margin": 37.150695999999996
      },
      "new": "008c1498",
      "score": 38.895455
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.003883495145631068,
          0.0012515644555694619
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
        "margin": -36.820361,
        "reverse_margin": -23.477548
      },
      "new": "0081a7d4",
      "score": 2.075094
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
        "margin": -36.895455,
        "reverse_margin": -40.751085
      },
      "new": "0061300c",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e57e70a276e975202c8e37e469131f5c"></a>

### v15.7.4 [`0088ebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ebc4.md) FUN_0088ebc4

`competing_candidates` 

呼出元 3件 [`005d5afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d5afc.md) [`0088e208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088e208.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009e4ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4ef4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008c1e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c1/008c1e54.md) · スコア 65.501166 · 採用条件未達 · 順位差 54.627435999999996 / 51.221441999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00684f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684f70.md) · スコア 10.87373 · 採用条件未達 · 順位差 -54.627435999999996 / 10.87373 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00685334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685334.md) · スコア 10.0 · 採用条件未達 · 順位差 -55.501166 / 10.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007fd33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md) · スコア 6.818182 · 採用条件未達 · 順位差 -58.682984 / 6.818182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007ff2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2ec.md) · スコア 5.0 · 採用条件未達 · 順位差 -60.501166 / 5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00931028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931028.md) · スコア 5.0 · 採用条件未達 · 順位差 -60.501166 / -24.295238 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007823ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md) · スコア 4.588235 · 採用条件未達 · 順位差 -60.912931 / 4.588235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009e4570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e4/009e4570.md) · スコア 3.968766 · 採用条件未達 · 順位差 -61.532399999999996 / -3.6108949999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
        ],
        "cfg_coverage": [
          0.8205128205128205,
          0.8421052631578947
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 54.627435999999996,
        "reverse_margin": 51.221441999999996
      },
      "new": "008c1e54",
      "score": 65.501166
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21212121212121213,
          0.1761006289308176
        ],
        "cfg_coverage": [
          0.02564102564102564,
          0.015384615384615385
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -54.627435999999996,
        "reverse_margin": 10.87373
      },
      "new": "00684f70",
      "score": 10.87373
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.19298245614035087
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
        "margin": -55.501166,
        "reverse_margin": 10.0
      },
      "new": "00685334",
      "score": 10.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-18db8e47691821d2bfa3aeaf17621478"></a>

### v15.7.4 [`0088ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088e/0088ee54.md) FUN_0088ee54

`competing_candidates` 

呼出元 3件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00894d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894d08.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008c20e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c20e4.md) · スコア 40.446247 · 採用条件未達 · 順位差 30.16339 / 26.254466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008dbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md) · スコア 10.282857 · 採用条件未達 · 順位差 -30.16339 / -6.105713999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) · スコア 4.825654 · 採用条件未達 · 順位差 -35.620593 / 4.825654 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00517f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517f10.md) · スコア 4.530088 · 採用条件未達 · 順位差 -35.916159 / 4.530088 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) · スコア 3.842365 · 採用条件未達 · 順位差 -36.603882 / 3.842365 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0045c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md) · スコア 3.293242 · 採用条件未達 · 順位差 -37.153005 / 3.293242 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · スコア 2.937139 · 採用条件未達 · 順位差 -37.509108 / -34.103947999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0047b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) · スコア 2.693878 · 採用条件未達 · 順位差 -37.752369 / 2.693878 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5172413793103449,
          0.5172413793103449
        ],
        "cfg_coverage": [
          0.47058823529411764,
          0.5333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.16339,
        "reverse_margin": 26.254466
      },
      "new": "008c20e4",
      "score": 40.446247
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22167487684729065,
          0.16071428571428573
        ],
        "cfg_coverage": [
          0.0784313725490196,
          0.032
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.16339,
        "reverse_margin": -6.105713999999999
      },
      "new": "008dbf84",
      "score": 10.282857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07389162561576355,
          0.11538461538461539
        ],
        "cfg_coverage": [
          0.0196078431372549,
          0.023809523809523808
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -35.620593,
        "reverse_margin": 4.825654
      },
      "new": "00498308",
      "score": 4.825654
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b17636da3831f4599c58579d7f33f14c"></a>

### v15.7.4 [`0088f20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f20c.md) FUN_0088f20c

`competing_candidates` 

呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

- 1. [`008c249c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c249c.md) · スコア 51.556342 · 採用条件未達 · 順位差 47.041888 / 47.397926 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00604fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604fac.md) · スコア 4.514454 · 採用条件未達 · 順位差 -47.041888 / -34.637061 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004a8360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md) · スコア 4.158416 · 採用条件未達 · 順位差 -47.397926 / 4.158416 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) · スコア 2.654867 · 採用条件未達 · 順位差 -48.901475 / 2.654867 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b0a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a190.md) · スコア 2.654867 · 採用条件未達 · 順位差 -48.901475 / 2.654867 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0074f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074f844.md) · スコア 2.389381 · 採用条件未達 · 順位差 -49.166961 / -24.095073 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a325b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a325b8.md) · スコア 2.123894 · 採用条件未達 · 順位差 -49.432448 / 2.123894 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) · スコア 2.011834 · 採用条件未達 · 順位差 -49.544508 / -34.029765 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6637168141592921,
          0.7142857142857143
        ],
        "cfg_coverage": [
          0.5866666666666667,
          0.5945945945945946
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 47.041888,
        "reverse_margin": 47.397926
      },
      "new": "008c249c",
      "score": 51.556342
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07079646017699115,
          0.14545454545454545
        ],
        "cfg_coverage": [
          0.013333333333333334,
          0.03225806451612903
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -47.041888,
        "reverse_margin": -34.637061
      },
      "new": "00604fac",
      "score": 4.514454
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09292035398230089,
          0.06930693069306931
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
        "margin": -47.397926,
        "reverse_margin": 4.158416
      },
      "new": "004a8360",
      "score": 4.158416
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dd708b5474151248f1f6d48ff4ab3ade"></a>

### v15.7.4 [`0088f628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f628.md) FUN_0088f628

`competing_candidates` 

呼出元 6件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`0089b410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b410.md) [`0089b6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b6c8.md) [`0089b8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b8e8.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md) [`00a6b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md)

- 1. [`008c2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2878.md) · スコア 52.0 · 採用条件未達 · 順位差 4.285713999999999 / 4.285713999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008bf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf810.md) · スコア 47.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b0cecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cecc.md) · スコア 37.0 · 採用条件未達 · 順位差 -15.0 / -18.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008e3af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3af0.md) · スコア 30.571429 · 採用条件未達 · 順位差 -21.428571 / -29.387755000000002 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00641f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641f00.md) · スコア 28.923077 · 採用条件未達 · 順位差 -23.076923 / -1.1538460000000015 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00698958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698958.md) · スコア 10.571429 · 採用条件未達 · 順位差 -41.428571 / -29.323307999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007fc67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc67c.md) · スコア 6.137931 · 採用条件未達 · 順位差 -45.862069 / -29.655172 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ac9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md) · スコア 5.934426 · 採用条件未達 · 順位差 -46.065574 / 5.934426 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.285713999999999,
        "reverse_margin": 4.285713999999999
      },
      "new": "008c2878",
      "score": 52.0
    },
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
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "008bf810",
      "score": 47.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.3888888888888889
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
        "reverse_margin": -18.333333000000003
      },
      "new": "00b0cecc",
      "score": 37.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-43f5481679eaeb443c83468ab2440078"></a>

### v15.7.4 [`0088f698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f698.md) FUN_0088f698

`competing_candidates` 

呼出元 2件 [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f740.md)

- 1. [`008c28e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c28e8.md) · スコア 67.402597 · 採用条件未達 · 順位差 60.950984 / 67.402597 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 2. [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) · スコア 6.451613 · 採用条件未達 · 順位差 -60.950984 / -9.504244 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) · スコア 0.612245 · 採用条件未達 · 順位差 -66.790352 / -10.408163 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.402597 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.402597 / -27.969309 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005aff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005aff1c.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.402597 / -29.090909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008c2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2878.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.402597 / -52.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008c4530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4530.md) · スコア 0.0 · 採用条件未達 · 順位差 -67.402597 / -35.54959 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8809523809523809,
          0.8809523809523809
        ],
        "cfg_coverage": [
          0.7272727272727273,
          0.8
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.950984,
        "reverse_margin": 67.402597
      },
      "new": "008c28e8",
      "score": 67.402597
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23809523809523808,
          0.10752688172043011
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
        "margin": -60.950984,
        "reverse_margin": -9.504244
      },
      "new": "005afc38",
      "score": 6.451613
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.023809523809523808,
          0.01020408163265306
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
        "margin": -66.790352,
        "reverse_margin": -10.408163
      },
      "new": "008c2ce0",
      "score": 0.612245
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cf86283c3c1a7c64a4c6f260dbc8d5de"></a>

### v15.7.4 [`0088f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f740.md) FUN_0088f740

`competing_candidates` 

呼出元 3件 [`0088f698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f698.md) [`0088fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fde0.md) [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) · 呼出先 3件 [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md)

- 1. [`008c2990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2990.md) · スコア 6.509434 · 採用条件未達 · 順位差 0.11890100000000015 / 4.8113209999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aea188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md) · スコア 6.390533 · 採用条件未達 · 順位差 -0.11890100000000015 / -46.852251 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) · スコア 3.195266 · 採用条件未達 · 順位差 -3.3141679999999996 / 3.195266 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008c8744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8744.md) · スコア 2.840237 · 採用条件未達 · 順位差 -3.6691969999999996 / -10.657416 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b0a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md) · スコア 2.840237 · 採用条件未達 · 順位差 -3.6691969999999996 / -63.989031 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0081a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a450.md) · スコア 2.485207 · 採用条件未達 · 順位差 -4.024227 / -46.160626 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009df750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df750.md) · スコア 1.775148 · 採用条件未達 · 順位差 -4.734286 / -1.936192 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009e3b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3b4c.md) · スコア 1.775148 · 採用条件未達 · 順位差 -4.734286 / -7.698536000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13609467455621302,
          0.10849056603773585
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
        "margin": 0.11890100000000015,
        "reverse_margin": 4.8113209999999995
      },
      "new": "008c2990",
      "score": 6.509434
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10650887573964497,
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
        "margin": -0.11890100000000015,
        "reverse_margin": -46.852251
      },
      "new": "00aea188",
      "score": 6.390533
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05325443786982249,
          0.08035714285714286
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
        "margin": -3.3141679999999996,
        "reverse_margin": 3.195266
      },
      "new": "00c3d71c",
      "score": 3.195266
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9ef567ba7d2bd1098cfa87442a9c3f0e"></a>

### v15.7.4 [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) FUN_0088f9e4

`competing_candidates` 

呼出元 19件 [`0058b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7d4.md) [`0058b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b8ec.md) [`0058b9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b9f4.md) [`0058ba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058ba50.md) [`0058bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bad0.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009e4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e58.md)

- 1. [`006e43a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e43a8.md) · スコア 15.497835 · 採用条件未達 · 順位差 0.04329000000000072 / -52.889261999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0068a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068a96c.md) · スコア 15.454545 · 採用条件未達 · 順位差 -0.04329000000000072 / 15.454545 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) · スコア 7.401361 · 採用条件未達 · 順位差 -8.096474 / -3.619047 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) · スコア 5.357143 · 採用条件未達 · 順位差 -10.140692000000001 / 5.357143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009ad9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9dc.md) · スコア 4.545455 · 採用条件未達 · 順位差 -10.952380000000002 / 4.545455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0046c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md) · スコア 4.038462 · 採用条件未達 · 順位差 -11.459373 / 4.038462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`009adc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md) · スコア 3.636364 · 採用条件未達 · 順位差 -11.861471 / 3.636364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009add4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009add4c.md) · スコア 3.636364 · 採用条件未達 · 順位差 -11.861471 / 3.636364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24242424242424243,
          0.25806451612903225
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.04329000000000072,
        "reverse_margin": -52.889261999999995
      },
      "new": "006e43a8",
      "score": 15.497835
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25757575757575757,
          0.32075471698113206
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
        "margin": -0.04329000000000072,
        "reverse_margin": 15.454545
      },
      "new": "0068a96c",
      "score": 15.454545
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.11224489795918367
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.03333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.096474,
        "reverse_margin": -3.619047
      },
      "new": "008c2ce0",
      "score": 7.401361
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6515c922c2ba473655dbcfb762847b0b"></a>

### v15.7.4 [`0088faec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088faec.md) FUN_0088faec

`competing_candidates` 

呼出元 1件 [`00aa05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa05ac.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009e4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e58.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`006e3e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3e10.md) · スコア 4.0 · 採用条件未達 · 順位差 2.0 / -38.282828 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00abde5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abde5c.md) · スコア 2.0 · 採用条件未達 · 順位差 -2.0 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md) · スコア 1.323636 · 採用条件未達 · 順位差 -2.676364 / 1.323636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0090d698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090d698.md) · スコア 1.315789 · 採用条件未達 · 順位差 -2.684211 / -54.924305999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008c2e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2e68.md) · スコア 1.286631 · 採用条件未達 · 順位差 -2.713369 / -1.881686 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00640970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00640/00640970.md) · スコア 1.008403 · 採用条件未達 · 順位差 -2.991597 / -21.112979 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008c3294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3294.md) · スコア 0.892857 · 採用条件未達 · 順位差 -3.1071429999999998 / -6.642856999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00729e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) · スコア 0.228137 · 採用条件未達 · 順位差 -3.771863 / -44.642089000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0743801652892562,
          0.06666666666666667
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
        "margin": 2.0,
        "reverse_margin": -38.282828
      },
      "new": "006e3e10",
      "score": 4.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04132231404958678,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.0,
        "reverse_margin": 2.0
      },
      "new": "00abde5c",
      "score": 2.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03305785123966942,
          0.016
        ],
        "cfg_coverage": [
          0.027777777777777776,
          0.01818181818181818
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.676364,
        "reverse_margin": 1.323636
      },
      "new": "006350c4",
      "score": 1.323636
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-36f7ba4a13eb6db7ee4bb1b4553731f2"></a>

### v15.7.4 [`0088fcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fcf8.md) FUN_0088fcf8

`competing_candidates` 

呼出元 4件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`0047f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f31c.md) · スコア 12.1875 · 採用条件未達 · 順位差 3.5277060000000002 / 12.1875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00729cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729cb4.md) · スコア 8.659794 · 採用条件未達 · 順位差 -3.5277060000000002 / -17.463917000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0072ba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072ba5c.md) · スコア 6.222222 · 採用条件未達 · 順位差 -5.965278 / -42.722221999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) · スコア 6.09375 · 採用条件未達 · 順位差 -6.09375 / 6.09375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008065d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/008065d4.md) · スコア 4.5 · 採用条件未達 · 順位差 -7.6875 / -42.080224 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -12.1875 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) · スコア 0.0 · 採用条件未達 · 順位差 -12.1875 / -57.138122 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) · スコア 0.0 · 採用条件未達 · 順位差 -12.1875 / -15.955857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23214285714285715,
          0.203125
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
        "margin": 3.5277060000000002,
        "reverse_margin": 12.1875
      },
      "new": "0047f31c",
      "score": 12.1875
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
      "new": "00729cb4",
      "score": 8.659794
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
          0.1037037037037037
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
        "margin": -5.965278,
        "reverse_margin": -42.722221999999995
      },
      "new": "0072ba5c",
      "score": 6.222222
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-03e21135546c5d916cb6a01a126d82cc"></a>

### v15.7.4 [`0088fdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fdd8.md) FUN_0088fdd8

`competing_candidates` 

呼出元 2件 [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) · 呼出先 0件 

- 1. [`008c3810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3810.md) · スコア 94.0 · 採用条件未達 · 順位差 93.8089 / 93.2932 · 
- 2. [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) · スコア 0.1911 · 採用条件未達 · 順位差 — / — · 
- 3. [`008c4530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4530.md) · スコア 0.0537 · 採用条件未達 · 順位差 — / — · 
- 4. [`008c41ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c41ac.md) · スコア 0.0356 · 採用条件未達 · 順位差 — / — · 
- 5. [`008c2e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2e68.md) · スコア 0.0338 · 採用条件未達 · 順位差 — / — · 
- 6. [`008c3294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3294.md) · スコア 0.0238 · 採用条件未達 · 順位差 — / — · 
- 7. [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) · スコア 0.0136 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 93.8089,
        "reverse_margin": 93.2932
      },
      "new": "008c3810",
      "score": 94.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008c2ce0",
      "score": 0.1911
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008c4530",
      "score": 0.0537
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-274ae0caff1dcee23c7f3bd00a4b3ade"></a>

### v15.7.4 [`0088fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fde0.md) FUN_0088fde0

`competing_candidates` 

呼出元 4件 [`008906a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/008906a8.md) [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) [`0089b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4ec.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f740.md) [`00898484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898484.md)

- 1. [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) · スコア 42.899403 · 採用条件未達 · 順位差 37.465439 / 35.958965 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008c506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c506c.md) · スコア 5.433964 · 採用条件未達 · 順位差 -37.465439 / -32.572998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0072f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) · スコア 4.628493 · 採用条件未達 · 順位差 -38.27091 / 4.628493 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006653cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md) · スコア 3.784387 · 採用条件未達 · 順位差 -39.115016 / 3.784387 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) · スコア 3.772365 · 採用条件未達 · 順位差 -39.127038 / 3.772365 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) · スコア 3.437792 · 採用条件未達 · 順位差 -39.461611 / 3.437792 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a41f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41f9c.md) · スコア 3.202578 · 採用条件未達 · 順位差 -39.696825 / 3.202578 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006a4e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a4/006a4e88.md) · スコア 2.991696 · 採用条件未達 · 順位差 -39.907707 / 2.991696 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6189591078066915,
          0.5672913117546848
        ],
        "cfg_coverage": [
          0.4079601990049751,
          0.34309623430962344
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 37.465439,
        "reverse_margin": 35.958965
      },
      "new": "008c3818",
      "score": 42.899403
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08178438661710037,
          0.06480117820324006
        ],
        "cfg_coverage": [
          0.07960199004975124,
          0.07729468599033816
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.465439,
        "reverse_margin": -32.572998
      },
      "new": "008c506c",
      "score": 5.433964
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03717472118959108,
          0.03745318352059925
        ],
        "cfg_coverage": [
          0.01990049751243781,
          0.022727272727272728
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -38.27091,
        "reverse_margin": 4.628493
      },
      "new": "0072f198",
      "score": 4.628493
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ab81890357623a66adf80191f600161e"></a>

### v15.7.4 [`008906a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/008906a8.md) FUN_008906a8

`competing_candidates` 

呼出元 6件 [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) [`00895118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895118.md) [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) [`0089b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4ec.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 9件 [`005bc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc280.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`0088fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fde0.md)

- 1. [`008c41ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c41ac.md) · スコア 42.584473 · 採用条件未達 · 順位差 39.982432 / 38.051140000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009113c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00911/009113c4.md) · スコア 2.602041 · 採用条件未達 · 順位差 -39.982432 / -38.176835 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00730334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) · スコア 2.376238 · 採用条件未達 · 順位差 -40.208235 / 2.376238 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006d631c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d6/006d631c.md) · スコア 1.061947 · 採用条件未達 · 順位差 -41.522526 / -78.130878 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) · スコア 1.061947 · 採用条件未達 · 順位差 -41.522526 / 1.061947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0068aa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068aa48.md) · スコア 1.057269 · 採用条件未達 · 順位差 -41.527204000000005 / 1.057269 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00ab0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0300.md) · スコア 0.265487 · 採用条件未達 · 順位差 -42.318986 / -54.865636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -42.584473 / -21.315789 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6150442477876106,
          0.6177777777777778
        ],
        "cfg_coverage": [
          0.30120481927710846,
          0.2840909090909091
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 39.982432,
        "reverse_margin": 38.051140000000004
      },
      "new": "008c41ac",
      "score": 42.584473
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0752212389380531,
          0.04336734693877551
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
        "margin": -39.982432,
        "reverse_margin": -38.176835
      },
      "new": "009113c4",
      "score": 2.602041
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08849557522123894,
          0.039603960396039604
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
        "margin": -40.208235,
        "reverse_margin": 2.376238
      },
      "new": "00730334",
      "score": 2.376238
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6e7e0171ebedeca33ab5dc114063ba97"></a>

### v15.7.4 [`00890a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md) FUN_00890a30

`competing_candidates` 

呼出元 4件 [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) [`0089b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b4ec.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008c4530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4530.md) · スコア 35.54959 · 採用条件未達 · 順位差 29.299590000000002 / 29.209164 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0080e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md) · スコア 6.25 · 採用条件未達 · 順位差 -29.299590000000002 / 6.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b0c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md) · スコア 6.25 · 採用条件未達 · 順位差 -29.299590000000002 / 6.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0080dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md) · スコア 5.0 · 採用条件未達 · 順位差 -30.549590000000002 / 5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005e0b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md) · スコア 4.583333 · 採用条件未達 · 順位差 -30.966257000000002 / -24.660973000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00aef6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md) · スコア 4.285714 · 採用条件未達 · 順位差 -31.263876000000003 / 4.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006e44a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md) · スコア 4.0 · 採用条件未達 · 順位差 -31.549590000000002 / -32.595611 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) · スコア 4.0 · 採用条件未達 · 順位差 -31.549590000000002 / -61.697248 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.42953020134228187
        ],
        "cfg_coverage": [
          0.35135135135135137,
          0.28888888888888886
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 29.299590000000002,
        "reverse_margin": 29.209164
      },
      "new": "008c4530",
      "score": 35.54959
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10416666666666667,
          0.11450381679389313
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
        "margin": -29.299590000000002,
        "reverse_margin": 6.25
      },
      "new": "0080e3ac",
      "score": 6.25
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10416666666666667,
          0.11450381679389313
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
        "margin": -29.299590000000002,
        "reverse_margin": 6.25
      },
      "new": "00b0c3f4",
      "score": 6.25
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-03bfe458c9bb14e34f0d42406747155a"></a>

### v15.7.4 [`00890c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md) FUN_00890c70

`competing_candidates` 

呼出元 2件 [`00890a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890a30.md) [`008b7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7948.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md)

- 1. [`008c4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4784.md) · スコア 29.56748 · 採用条件未達 · 順位差 25.76748 / 25.593496 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006dc900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md) · スコア 3.8 · 採用条件未達 · 順位差 -25.76748 / 3.8 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a6cce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md) · スコア 3.792927 · 採用条件未達 · 順位差 -25.774553 / 3.792927 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009b89b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md) · スコア 3.585366 · 採用条件未達 · 順位差 -25.982114 / 3.585366 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · スコア 2.798669 · 採用条件未達 · 順位差 -26.768811 / -28.827604 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0067d490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md) · スコア 2.692308 · 採用条件未達 · 順位差 -26.875172 / 2.692308 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) · スコア 2.609756 · 採用条件未達 · 順位差 -26.957724 / -63.087492000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) · スコア 2.411463 · 採用条件未達 · 順位差 -27.156017 / -19.309386 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4105691056910569,
          0.4105691056910569
        ],
        "cfg_coverage": [
          0.15384615384615385,
          0.14666666666666667
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.76748,
        "reverse_margin": 25.593496
      },
      "new": "008c4784",
      "score": 29.56748
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03048780487804878,
          0.03
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
        "margin": -25.76748,
        "reverse_margin": 3.8
      },
      "new": "006dc900",
      "score": 3.8
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.046747967479674794,
          0.02836004932182491
        ],
        "cfg_coverage": [
          0.006993006993006993,
          0.0045662100456621
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -25.774553,
        "reverse_margin": 3.792927
      },
      "new": "00a6cce4",
      "score": 3.792927
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-62cec8eb54d4307ee197eb15844a818f"></a>

### v15.7.4 [`00891554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891554.md) thunk_FUN_00891558

`competing_candidates` 

呼出元 1件 [`00abe1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abe/00abe1d0.md) · 呼出先 1件 [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md)

- 1. [`008c5068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5068.md) · スコア 23.4586 · 採用条件未達 · 順位差 13.9941 / 13.9941 · 
- 2. [`008c506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c506c.md) · スコア 9.4645 · 採用条件未達 · 順位差 — / — · 
- 3. [`008c79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c7/008c79a4.md) · スコア 0.6787 · 採用条件未達 · 順位差 — / — · 
- 4. [`008c41ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c41ac.md) · スコア 0.5643 · 採用条件未達 · 順位差 — / — · 
- 5. [`008c4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4784.md) · スコア 0.5547 · 採用条件未達 · 順位差 — / — · 
- 6. [`008c4530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4530.md) · スコア 0.3868 · 採用条件未達 · 順位差 — / — · 
- 7. [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) · スコア 0.2405 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 13.9941,
        "reverse_margin": 13.9941
      },
      "new": "008c5068",
      "score": 23.4586
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008c506c",
      "score": 9.4645
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008c79a4",
      "score": 0.6787
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f98faf3560a75f0a826f1ac3bec55061"></a>

### v15.7.4 [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) FUN_00891558

`competing_candidates` 

呼出元 4件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00891554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891554.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 30件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`006ae0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae0f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008c506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c506c.md) · スコア 38.006962 · 採用条件未達 · 順位差 31.066524 / 32.572998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) · スコア 6.940438 · 採用条件未達 · 順位差 -31.066524 / -35.958965 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0062b034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md) · スコア 2.899733 · 採用条件未達 · 順位差 -35.107229000000004 / 2.899733 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009f9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f9/009f9d44.md) · スコア 2.483766 · 採用条件未達 · 順位差 -35.523196 / -1.329421 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) · スコア 2.250826 · 採用条件未達 · 順位差 -35.756136 / -10.584458 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md) · スコア 2.244652 · 採用条件未達 · 順位差 -35.76231 / -2.3833370000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009f7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md) · スコア 2.19385 · 採用条件未達 · 順位差 -35.813112000000004 / -14.540844000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) · スコア 1.941176 · 採用条件未達 · 順位差 -36.065786 / -25.254303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5191176470588236,
          0.5198821796759941
        ],
        "cfg_coverage": [
          0.4034090909090909,
          0.34299516908212563
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 31.066524,
        "reverse_margin": 32.572998
      },
      "new": "008c506c",
      "score": 38.006962
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07941176470588235,
          0.0919931856899489
        ],
        "cfg_coverage": [
          0.14772727272727273,
          0.1087866108786611
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.066524,
        "reverse_margin": -35.958965
      },
      "new": "008c3818",
      "score": 6.940438
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04264705882352941,
          0.11983471074380166
        ],
        "cfg_coverage": [
          0.017045454545454544,
          0.057692307692307696
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -35.107229000000004,
        "reverse_margin": 2.899733
      },
      "new": "0062b034",
      "score": 2.899733
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b3d6c1058dd4b399a75bb91bfe0cda4e"></a>

### v15.7.4 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) FUN_008920f8

`competing_candidates` 

呼出元 1件 [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) · 呼出先 64件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

- 1. [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) · スコア 33.935507 · 採用条件未達 · 順位差 31.311571 / 32.638988 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · スコア 2.623936 · 採用条件未達 · 順位差 -31.311571 / -10.873256999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · スコア 2.483654 · 採用条件未達 · 順位差 -31.451853 / -29.4255 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · スコア 2.251648 · 採用条件未達 · 順位差 -31.683859 / -27.895711000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · スコア 2.159151 · 採用条件未達 · 順位差 -31.776356 / -46.393397 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · スコア 2.107849 · 採用条件未達 · 順位差 -31.827658 / -35.595416 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0090a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090a/0090a41c.md) · スコア 2.071899 · 採用条件未達 · 順位差 -31.863608 / -24.209193 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008d3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md) · スコア 2.0 · 採用条件未達 · 順位差 -31.935507 / -44.310796 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.46255242660275614,
          0.46338535414165666
        ],
        "cfg_coverage": [
          0.13129496402877697,
          0.10911808669656203
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 31.311571,
        "reverse_margin": 32.638988
      },
      "new": "008c5c08",
      "score": 33.935507
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.014979029358897543,
          0.008264462809917356
        ],
        "cfg_coverage": [
          0.01079136690647482,
          0.0064034151547491995
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.311571,
        "reverse_margin": -10.873256999999999
      },
      "new": "005c8ebc",
      "score": 2.623936
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.005991611743559017,
          0.005063291139240506
        ],
        "cfg_coverage": [
          0.008992805755395683,
          0.009057971014492754
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.451853,
        "reverse_margin": -29.4255
      },
      "new": "0064ec78",
      "score": 2.483654
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f90ae66d417f00250054d3cc34fbe309"></a>

### v15.7.4 [`00893ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00893/00893ea0.md) FUN_00893ea0

`competing_candidates` 

呼出元 3件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00895118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895118.md) [`0089bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089bdf0.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047b5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md) [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md)

- 1. [`008c79a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c7/008c79a4.md) · スコア 54.786187 · 採用条件未達 · 順位差 51.305668 / 51.844364999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a41f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41f9c.md) · スコア 3.480519 · 採用条件未達 · 順位差 -51.305668 / 3.480519 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a2de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2de6c.md) · スコア 2.545455 · 採用条件未達 · 順位差 -52.240732 / -31.90254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) · スコア 2.490082 · 採用条件未達 · 順位差 -52.296105 / -26.725201 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) · スコア 2.467532 · 採用条件未達 · 順位差 -52.318655 / -38.121889 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00668db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md) · スコア 2.458015 · 採用条件未達 · 順位差 -52.328171999999995 / 2.458015 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) · スコア 2.420561 · 採用条件未達 · 順位差 -52.365626 / -24.53366 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009e01e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e01e0.md) · スコア 2.38961 · 採用条件未達 · 順位差 -52.396577 / -11.373683000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7584415584415585,
          0.7584415584415585
        ],
        "cfg_coverage": [
          0.36398467432950193,
          0.3861788617886179
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 51.305668,
        "reverse_margin": 51.844364999999996
      },
      "new": "008c79a4",
      "score": 54.786187
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.024675324675324677,
          0.04157549234135667
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
        "margin": -51.305668,
        "reverse_margin": 3.480519
      },
      "new": "00a41f9c",
      "score": 3.480519
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.00909090909090909,
          0.021806853582554516
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
        "margin": -52.240732,
        "reverse_margin": -31.90254
      },
      "new": "00a2de6c",
      "score": 2.545455
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cbb7035cb4786a778c7625b8e64a345d"></a>

### v15.7.4 [`00894b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894b58.md) FUN_00894b58

`competing_candidates` 

呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292ec.md) [`008292f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292f4.md) [`00a6ac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6ac54.md)

- 1. [`008c865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c865c.md) · スコア 31.465517 · 採用条件未達 · 順位差 30.820355999999997 / 31.465517 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) · スコア 0.645161 · 採用条件未達 · 順位差 -30.820355999999997 / -15.310696 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009d3794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md) · スコア 0.530973 · 採用条件未達 · 順位差 -30.934544 / 0.530973 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.465517 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.465517 / -57.138122 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.465517 / -27.969309 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005aff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005aff1c.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.465517 / -29.090909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00636968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636968.md) · スコア 0.0 · 採用条件未達 · 順位差 -31.465517 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4827586206896552,
          0.4827586206896552
        ],
        "cfg_coverage": [
          0.125,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.820355999999997,
        "reverse_margin": 31.465517
      },
      "new": "008c865c",
      "score": 31.465517
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.017241379310344827,
          0.010752688172043012
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
        "margin": -30.820355999999997,
        "reverse_margin": -15.310696
      },
      "new": "005afc38",
      "score": 0.645161
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.017241379310344827,
          0.008849557522123894
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
        "margin": -30.934544,
        "reverse_margin": 0.530973
      },
      "new": "009d3794",
      "score": 0.530973
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e8f3bb97116468e40c750614aabed16b"></a>

### v15.7.4 [`00894c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894c40.md) FUN_00894c40

`competing_candidates` 

呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`0063b50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b50c.md) · スコア 15.015674 · 採用条件未達 · 順位差 1.2509680000000003 / -17.841469 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005e44ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e44ec.md) · スコア 13.764706 · 採用条件未達 · 順位差 -1.2509680000000003 / -21.743315 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005e45b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e45b8.md) · スコア 13.385714 · 採用条件未達 · 順位差 -1.6299600000000005 / -15.542857000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a86514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86514.md) · スコア 11.048951 · 採用条件未達 · 順位差 -3.966723 / -23.192806999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) · スコア 9.642857 · 採用条件未達 · 順位差 -5.372817000000001 / -24.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) · スコア 8.77193 · 採用条件未達 · 順位差 -6.243744000000001 / 8.77193 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00903f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903f30.md) · スコア 8.77193 · 採用条件未達 · 順位差 -6.243744000000001 / 8.77193 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0072ada0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ada0.md) · スコア 8.319328 · 採用条件未達 · 順位差 -6.696346 / 8.319328 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22,
          0.1896551724137931
        ],
        "cfg_coverage": [
          0.18181818181818182,
          0.18181818181818182
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.2509680000000003,
        "reverse_margin": -17.841469
      },
      "new": "0063b50c",
      "score": 15.015674
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.19607843137254902
        ],
        "cfg_coverage": [
          0.18181818181818182,
          0.1
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.2509680000000003,
        "reverse_margin": -21.743315
      },
      "new": "005e44ec",
      "score": 13.764706
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22,
          0.19642857142857142
        ],
        "cfg_coverage": [
          0.18181818181818182,
          0.08
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.6299600000000005,
        "reverse_margin": -15.542857000000001
      },
      "new": "005e45b8",
      "score": 13.385714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-95c6cee0d42e259ffa2d2021d12eccca"></a>

### v15.7.4 [`00894d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894d08.md) FUN_00894d08

`competing_candidates` 

呼出元 1件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) · 呼出先 14件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00827b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827b94.md) [`008292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292ec.md) [`008292f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292f4.md)

- 1. [`008c8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8860.md) · スコア 31.822581 · 採用条件未達 · 順位差 27.709678 / 27.467742 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00acea58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md) · スコア 4.112903 · 採用条件未達 · 順位差 -27.709678 / 4.112903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) · スコア 3.870968 · 採用条件未達 · 順位差 -27.951613 / -7.14944 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009edd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ed/009edd60.md) · スコア 3.870968 · 採用条件未達 · 順位差 -27.951613 / -11.800361 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009f77f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f77f4.md) · スコア 3.870968 · 採用条件未達 · 順位差 -27.951613 / -5.401759 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00aebb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md) · スコア 3.870968 · 採用条件未達 · 順位差 -27.951613 / -32.56047 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006cb2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb2d4.md) · スコア 3.145161 · 採用条件未達 · 順位差 -28.677419999999998 / -10.796231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) · スコア 2.903226 · 採用条件未達 · 順位差 -28.919355 / 2.903226 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4637096774193548,
          0.4637096774193548
        ],
        "cfg_coverage": [
          0.2,
          0.2
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 27.709678,
        "reverse_margin": 27.467742
      },
      "new": "008c8860",
      "score": 31.822581
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06854838709677419,
          0.1650485436893204
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
        "margin": -27.709678,
        "reverse_margin": 4.112903
      },
      "new": "00acea58",
      "score": 4.112903
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06451612903225806,
          0.16326530612244897
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
        "margin": -27.951613,
        "reverse_margin": -7.14944
      },
      "new": "008c2ce0",
      "score": 3.870968
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-37d0be07ccf835f08adc4d1113a22929"></a>

### v15.7.4 [`00895118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895118.md) FUN_00895118

`competing_candidates` 

呼出元 1件 [`0089b8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b8e8.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008906a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/008906a8.md) [`00893ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00893/00893ea0.md)

- 1. [`008c8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8c70.md) · スコア 8.111111 · 採用条件未達 · 順位差 6.096185999999999 / 6.773083 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · スコア 2.014925 · 採用条件未達 · 順位差 -6.096185999999999 / -21.202888 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a41f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41f9c.md) · スコア 1.920904 · 採用条件未達 · 順位差 -6.190206999999999 / 1.920904 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a413b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a413b4.md) · スコア 1.581921 · 採用条件未達 · 順位差 -6.52919 / 1.581921 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009c2c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c2c48.md) · スコア 1.468927 · 採用条件未達 · 順位差 -6.642183999999999 / 1.468927 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00ac08a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac08a0.md) · スコア 1.468927 · 採用条件未達 · 順位差 -6.642183999999999 / -43.53866 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00aeb76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md) · スコア 1.468927 · 採用条件未達 · 順位差 -6.642183999999999 / -42.506248 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00aea2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md) · スコア 1.129944 · 採用条件未達 · 順位差 -6.981166999999999 / -32.258945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15065913370998116,
          0.11851851851851852
        ],
        "cfg_coverage": [
          0.06504065040650407,
          0.05
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.096185999999999,
        "reverse_margin": 6.773083
      },
      "new": "008c8c70",
      "score": 8.111111
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03389830508474576,
          0.033582089552238806
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
        "margin": -6.096185999999999,
        "reverse_margin": -21.202888
      },
      "new": "005ef56c",
      "score": 2.014925
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.032015065913371,
          0.037199124726477024
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
        "margin": -6.190206999999999,
        "reverse_margin": 1.920904
      },
      "new": "00a41f9c",
      "score": 1.920904
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-094cac8bdc4dddd36e4e27b9b433e52e"></a>

### v15.7.4 [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) FUN_008959c8

`competing_candidates` 

呼出元 1件 [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

- 1. [`008c9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c9/008c9770.md) · スコア 32.013661 · 採用条件未達 · 順位差 26.946994 / 27.200102 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) · スコア 5.066667 · 採用条件未達 · 順位差 -26.946994 / -33.721211999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00787bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md) · スコア 4.813559 · 採用条件未達 · 順位差 -27.200102 / -34.032146000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · スコア 4.683112 · 採用条件未達 · 順位差 -27.330548999999998 / -46.374184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) · スコア 4.613497 · 採用条件未達 · 順位差 -27.400164 / -40.338392 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) · スコア 4.5763 · 採用条件未達 · 順位差 -27.437361 / -37.424003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`0068bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md) · スコア 4.46875 · 採用条件未達 · 順位差 -27.544911 / 4.46875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 8. [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) · スコア 4.416089 · 採用条件未達 · 順位差 -27.597572 / -29.897278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.46440677966101696,
          0.46440677966101696
        ],
        "cfg_coverage": [
          0.007462686567164179,
          0.022222222222222223
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 26.946994,
        "reverse_margin": 27.200102
      },
      "new": "008c9770",
      "score": 32.013661
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02711864406779661,
          0.017777777777777778
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
        "margin": -26.946994,
        "reverse_margin": -33.721211999999994
      },
      "new": "00697f94",
      "score": 5.066667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013559322033898305,
          0.03669724770642202
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
        "margin": -27.200102,
        "reverse_margin": -34.032146000000004
      },
      "new": "00787bc0",
      "score": 4.813559
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-09a8dfb159dd8e9249158a7fdf7a2e86"></a>

### v15.7.4 [`00895e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md) FUN_00895e64

`competing_candidates` 

呼出元 2件 [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) [`008b89f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b89f8.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d90.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md)

- 1. [`008c9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c9/008c9c0c.md) · スコア 28.138487 · 採用条件未達 · 順位差 24.912681000000003 / 26.11146 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00821ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821ea4.md) · スコア 3.225806 · 採用条件未達 · 順位差 -24.912681000000003 / -57.971458 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006741b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006741b0.md) · スコア 2.857143 · 採用条件未達 · 順位差 -25.281344 / 2.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a32d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32d9c.md) · スコア 2.689076 · 採用条件未達 · 順位差 -25.449411 / 2.689076 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008f30c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md) · スコア 1.756757 · 採用条件未達 · 順位差 -26.38173 / -23.576576 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008c9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c9/008c9770.md) · スコア 1.008403 · 採用条件未達 · 順位差 -27.130084 / -31.005257999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00aee7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md) · スコア 1.008403 · 採用条件未達 · 順位差 -27.130084 / -42.606504 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a005e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md) · スコア 0.847059 · 採用条件未達 · 順位差 -27.291428 / -3.567945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4369747899159664,
          0.4369747899159664
        ],
        "cfg_coverage": [
          0.096,
          0.13333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.912681000000003,
        "reverse_margin": 26.11146
      },
      "new": "008c9c0c",
      "score": 28.138487
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.056022408963585436,
          0.053763440860215055
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
        "margin": -24.912681000000003,
        "reverse_margin": -57.971458
      },
      "new": "00821ea4",
      "score": 3.225806
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.047619047619047616,
          0.13076923076923078
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
        "margin": -25.281344,
        "reverse_margin": 2.857143
      },
      "new": "006741b0",
      "score": 2.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-34f4800a868ec97ac5109269a4b1a991"></a>

### v15.7.4 [`00896c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c68.md) FUN_00896c68

`competing_candidates` 

呼出元 3件 [`005d5afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d5afc.md) [`005d62c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d62c8.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 0件 

- 1. [`008caa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa10.md) · スコア 94.0 · 採用条件未達 · 順位差 83.4375 / 83.4375 · 
- 2. [`008caa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa18.md) · スコア 10.5625 · 採用条件未達 · 順位差 — / — · 
- 3. [`008caa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa20.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · スコア 0.0166 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 83.4375,
        "reverse_margin": 83.4375
      },
      "new": "008caa10",
      "score": 94.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa18",
      "score": 10.5625
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa20",
      "score": 2.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2b0d94bba789bf9cac3ce2fb2b642d6c"></a>

### v15.7.4 [`00896c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c70.md) FUN_00896c70

`competing_candidates` 

呼出元 3件 [`005d5afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d5afc.md) [`005d62c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d62c8.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 0件 

- 1. [`008caa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa18.md) · スコア 94.0 · 採用条件未達 · 順位差 83.4375 / 83.4375 · 
- 2. [`008caa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa10.md) · スコア 10.5625 · 採用条件未達 · 順位差 — / — · 
- 3. [`008caa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa20.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) · スコア 0.0684 · 採用条件未達 · 順位差 — / — · 
- 5. [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · スコア 0.0166 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 83.4375,
        "reverse_margin": 83.4375
      },
      "new": "008caa18",
      "score": 94.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa10",
      "score": 10.5625
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa20",
      "score": 2.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3e376e7858d4c272ad0ef6a11d647d1c"></a>

### v15.7.4 [`00896c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c78.md) FUN_00896c78

`competing_candidates` 

呼出元 1件 [`008b7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7948.md) · 呼出先 0件 

- 1. [`008caa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa20.md) · スコア 64.0 · 採用条件未達 · 順位差 62.0 / 62.0 · 
- 2. [`008caa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa10.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008caa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa18.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) · スコア 0.0377 · 採用条件未達 · 順位差 — / — · 
- 5. [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) · スコア 0.0342 · 採用条件未達 · 順位差 — / — · 
- 6. [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · スコア 0.0083 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 62.0,
        "reverse_margin": 62.0
      },
      "new": "008caa20",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa10",
      "score": 2.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008caa18",
      "score": 2.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-75d340f9ce9d43ada355fe2678544caa"></a>

### v15.7.4 [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) FUN_00896c7c

`competing_candidates` 

呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md)

- 1. [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · スコア 14.349086 · 採用条件未達 · 順位差 10.496354 / 11.351165 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) · スコア 3.852732 · 採用条件未達 · 順位差 -10.496354 / 3.852732 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · スコア 3.810166 · 採用条件未達 · 順位差 -10.53892 / -27.816107000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006e2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md) · スコア 3.710214 · 採用条件未達 · 順位差 -10.638872 / 3.710214 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007c970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md) · スコア 3.140684 · 採用条件未達 · 順位差 -11.208402 / -38.019984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · スコア 3.076233 · 採用条件未達 · 順位差 -11.272853 / -39.674852 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008bc884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc884.md) · スコア 2.693333 · 採用条件未達 · 順位差 -11.655753 / -9.066666999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0074edec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074e/0074edec.md) · スコア 2.628988 · 採用条件未達 · 順位差 -11.720098 / -47.079577 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16864608076009502,
          0.14760914760914762
        ],
        "cfg_coverage": [
          0.10309278350515463,
          0.07462686567164178
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.496354,
        "reverse_margin": 11.351165
      },
      "new": "008caa24",
      "score": 14.349086
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.030878859857482184,
          0.07692307692307693
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
        "margin": -10.496354,
        "reverse_margin": 3.852732
      },
      "new": "0082ede0",
      "score": 3.852732
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.040380047505938245,
          0.028286189683860232
        ],
        "cfg_coverage": [
          0.010309278350515464,
          0.005649717514124294
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.53892,
        "reverse_margin": -27.816107000000002
      },
      "new": "00a992ac",
      "score": 3.810166
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-39fecea6a24885999938de224c371d25"></a>

### v15.7.4 [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) FUN_00897400

`competing_candidates` 

呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 13件 [`00429ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ac4.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad74.md) [`0046c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) · スコア 25.55711 · 採用条件未達 · 順位差 19.916084 / 17.501166 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ac0700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0700.md) · スコア 5.641026 · 採用条件未達 · 順位差 -19.916084 / -40.961434999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0058bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md) · スコア 3.589744 · 採用条件未達 · 順位差 -21.967366000000002 / 3.589744 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · スコア 3.589744 · 採用条件未達 · 順位差 -21.967366000000002 / 3.589744 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00783470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md) · スコア 3.589744 · 採用条件未達 · 順位差 -21.967366000000002 / 3.589744 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · スコア 3.096774 · 採用条件未達 · 順位差 -22.460336 / -49.54499199999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a3e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e01c.md) · スコア 3.096774 · 採用条件未達 · 順位差 -22.460336 / -14.993922999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00b2bb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bb0c.md) · スコア 2.564103 · 採用条件未達 · 順位差 -22.993007000000002 / 2.564103 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4017094017094017,
          0.4017094017094017
        ],
        "cfg_coverage": [
          0.11764705882352941,
          0.07272727272727272
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.916084,
        "reverse_margin": 17.501166
      },
      "new": "008cb298",
      "score": 25.55711
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09401709401709402,
          0.12359550561797752
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
        "margin": -19.916084,
        "reverse_margin": -40.961434999999994
      },
      "new": "00ac0700",
      "score": 5.641026
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05982905982905983,
          0.08433734939759036
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
        "margin": -21.967366000000002,
        "reverse_margin": 3.589744
      },
      "new": "0058bdfc",
      "score": 3.589744
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aacf6c9f0a7d33b2ffaed35c223f2569"></a>

### v15.7.4 [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) FUN_00897610

`competing_candidates` 

呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 18件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) · スコア 33.669811 · 採用条件未達 · 順位差 16.386792000000003 / 8.344339000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a3e32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e32c.md) · スコア 17.283019 · 採用条件未達 · 順位差 -16.386792000000003 / -10.431267000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008feea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feea4.md) · スコア 16.181818 · 採用条件未達 · 順位差 -17.487993000000003 / -39.515152 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00787bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md) · スコア 9.504587 · 採用条件未達 · 順位差 -24.165224000000002 / -29.341118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`006350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md) · スコア 4.96 · 採用条件未達 · 順位差 -28.709811000000002 / 4.96 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`006153cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006153cc.md) · スコア 4.0 · 採用条件未達 · 順位差 -29.669811000000003 / -38.550725 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`0062f7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md) · スコア 4.0 · 採用条件未達 · 順位差 -29.669811000000003 / -28.571429000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4528301886792453,
          0.4528301886792453
        ],
        "cfg_coverage": [
          0.15384615384615385,
          0.125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 16.386792000000003,
        "reverse_margin": 8.344339000000002
      },
      "new": "008cb4a8",
      "score": 33.669811
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25471698113207547,
          0.2967032967032967
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
        "margin": -16.386792000000003,
        "reverse_margin": -10.431267000000002
      },
      "new": "00a3e32c",
      "score": 17.283019
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24528301886792453,
          0.23636363636363636
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
        "margin": -17.487993000000003,
        "reverse_margin": -39.515152
      },
      "new": "008feea4",
      "score": 16.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c95bd85a71b79aa398035a0ac4748d02"></a>

### v15.7.4 [`00897b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897b94.md) FUN_00897b94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba2c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 54.285714,
        "reverse_margin": 54.285714
      },
      "new": "008cba2c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ea90e623540450e1ec7c3ff16b989467"></a>

### v15.7.4 [`00897bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897bb0.md) FUN_00897bb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cba48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba48.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008cba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba2c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cba48",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cba2c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1afa0053fe5ebb8d1d9c3ddc61fa265d"></a>

### v15.7.4 [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) FUN_00897c24

`competing_candidates` 

呼出元 0件  · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`008cbabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbabc.md) · スコア 55.08089 · 採用条件未達 · 順位差 44.35514499999999 / 46.553171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0081cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cea0.md) · スコア 10.725745 · 採用条件未達 · 順位差 -44.35514499999999 / -59.37010599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a6a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a510.md) · スコア 7.034884 · 採用条件未達 · 順位差 -48.046006 / 7.034884 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009eec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eec8c.md) · スコア 6.794742 · 採用条件未達 · 順位差 -48.286148 / -14.726569000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) · スコア 6.794742 · 採用条件未達 · 順位差 -48.286148 / -55.282553 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) · スコア 6.686047 · 採用条件未達 · 順位差 -48.394842999999995 / 6.686047 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00675e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675e90.md) · スコア 6.538988 · 採用条件未達 · 順位差 -48.54190199999999 / 6.538988 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 5.62709 · 採用条件未達 · 順位差 -49.453799999999994 / -29.058806999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          0.6086956521739131,
          0.6363636363636364
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 44.35514499999999,
        "reverse_margin": 46.553171
      },
      "new": "008cbabc",
      "score": 55.08089
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18023255813953487,
          0.1657754010695187
        ],
        "cfg_coverage": [
          0.06521739130434782,
          0.03896103896103896
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -44.35514499999999,
        "reverse_margin": -59.37010599999999
      },
      "new": "0081cea0",
      "score": 10.725745
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0755813953488372,
          0.10655737704918032
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -48.046006,
        "reverse_margin": 7.034884
      },
      "new": "00a6a510",
      "score": 7.034884
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2486ca3ae0968220e09db50ae8d1d3b1"></a>

### v15.7.4 [`00897ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897ed4.md) FUN_00897ed4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cbd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbd6c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008cbd6c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1aa38bc880753ee3e5ccd7b3b7af1657"></a>

### v15.7.4 [`00897ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897ef0.md) FUN_00897ef0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cbd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbd88.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008cbd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbd6c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008cbabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbabc.md) · スコア 0.0698 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cbd88",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cbd6c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cbabc",
      "score": 0.0698
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2ad68c7985271b35ddb1e3d1f34d02a6"></a>

### v15.7.4 [`0089834c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/0089834c.md) FUN_0089834c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cc1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc1e4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008cc1e4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b16bc22c22b06e0570ee711969abd879"></a>

### v15.7.4 [`00898368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898368.md) FUN_00898368

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cc200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc200.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008cc1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc1e4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cc200",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cc1e4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6b8d5bea9d4f782eff57a7f59a3887d8"></a>

### v15.7.4 [`0089841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/0089841c.md) FUN_0089841c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cc2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2b4.md) · スコア 54.285714 · 採用条件未達 · 順位差 25.714285 / 25.714285 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008cc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2dc.md) · スコア 28.571429 · 採用条件未達 · 順位差 -25.714285 / -6.428571000000002 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 25.714285,
        "reverse_margin": 25.714285
      },
      "new": "008cc2b4",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
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
        "margin": -25.714285,
        "reverse_margin": -6.428571000000002
      },
      "new": "008cc2dc",
      "score": 28.571429
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
        "reverse_margin": -65.0
      },
      "new": "008cc2ec",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-87c3fe8cb297f78b2e0d918c5dfa13d1"></a>

### v15.7.4 [`00898438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898438.md) FUN_00898438

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cc2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2d0.md) · スコア 84.0 · 採用条件未達 · 順位差 81.0 / 81.0 · 
- 2. [`008cc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2dc.md) · スコア 3.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008cc2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2b4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`008cc31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc31c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 81.0,
        "reverse_margin": 81.0
      },
      "new": "008cc2d0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cc2dc",
      "score": 3.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cc2b4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-499a69be77bfb0c64bb79332caaf6c2b"></a>

### v15.7.4 [`00898444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898444.md) FUN_00898444

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`008cc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2dc.md) · スコア 35.0 · 採用条件未達 · 順位差 6.428571000000002 / 6.428571000000002 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008cc2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2b4.md) · スコア 28.571429 · 採用条件未達 · 順位差 -6.428571000000002 / -25.714285 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 6.428571000000002,
        "reverse_margin": 6.428571000000002
      },
      "new": "008cc2dc",
      "score": 35.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25,
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
        "margin": -6.428571000000002,
        "reverse_margin": -25.714285
      },
      "new": "008cc2b4",
      "score": 28.571429
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
        "margin": -35.0,
        "reverse_margin": -65.0
      },
      "new": "008cc2ec",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-35b9a7798fabe2bd58c62f0a1ae6a75f"></a>

### v15.7.4 [`00898454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898454.md) FUN_00898454

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 35.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008cc2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2b4.md) · スコア 25.0 · 採用条件未達 · 順位差 -35.0 / -29.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008cc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2dc.md) · スコア 25.0 · 採用条件未達 · 順位差 -35.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) · スコア 20.0 · 採用条件未達 · 順位差 -40.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.0,
        "reverse_margin": 0.0
      },
      "new": "0043bd58",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08333333333333333,
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
        "margin": -35.0,
        "reverse_margin": -29.285714
      },
      "new": "008cc2b4",
      "score": 25.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08333333333333333,
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
        "margin": -35.0,
        "reverse_margin": -10.0
      },
      "new": "008cc2dc",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b849cf722f79afc19e3bd42128ffc271"></a>

### v15.7.4 [`00898484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00898/00898484.md) FUN_00898484

`competing_candidates` 

呼出元 2件 [`0088fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fde0.md) [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) · 呼出先 0件 

- 1. [`008cc31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc31c.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`008cc2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2d0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`008cc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2dc.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cc31c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cc2d0",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cc2dc",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-25c3e3fb5eb26562c4e08f293ba97c46"></a>

### v15.7.4 [`0089b3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b3f4.md) FUN_0089b3f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cf28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf28c.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 56.0,
        "reverse_margin": -24.0
      },
      "new": "008cf28c",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3a0f270490278394e5f7ebb3e0b31d8e"></a>

### v15.7.4 [`0089b408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b408.md) FUN_0089b408

`competing_candidates` 

呼出元 1件 [`00891558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00891/00891558.md) · 呼出先 0件 

- 1. [`008cf2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf2a0.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`008cf28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf28c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cf2a0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cf28c",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-54521c3749af5951952d815794448b65"></a>

### v15.7.4 [`0089b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b470.md) FUN_0089b470

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cf308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf308.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008cf308",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f3d028e8e0bdd79c77cde16c4c9620e0"></a>

### v15.7.4 [`0089b48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089b/0089b48c.md) FUN_0089b48c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008cf324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf324.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008cf308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cf/008cf308.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008cf324",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008cf308",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

