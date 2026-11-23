# v15.7.3 → v15.7.4 · 追加調査 (12)

[一覧の目次](README.md)

### v15.7.3 [`00773d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773d48.md) FUN_00773d48

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773d48.md) · スコア 80.0 · 採用条件未達 · 順位差 4.285713999999999 / 4.285713999999999 · insufficient_independent_call_anchors
- 2. [`00849bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849bd0.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · cfg_coverage, insufficient_independent_call_anchors
- 3. [`00972844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972844.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · cfg_coverage, insufficient_independent_call_anchors
- 4. [`00775088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775088.md) · スコア 72.857143 · 採用条件未達 · 順位差 -7.1428570000000065 / -7.1428570000000065 · cfg_coverage, insufficient_independent_call_anchors
- 5. [`0097cf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cf48.md) · スコア 59.679144 · 採用条件未達 · 順位差 -20.320856 / -20.320856 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007746f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007746f4.md) · スコア 58.609626 · 採用条件未達 · 順位差 -21.390374 / -21.390374 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00972fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972fa0.md) · スコア 56.590909 · 採用条件未達 · 順位差 -23.409090999999997 / -23.409090999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.285713999999999,
        "reverse_margin": 4.285713999999999
      },
      "new": "00773d48",
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
          0.7857142857142857,
          0.8461538461538461
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "00849bd0",
      "score": 75.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          0.7857142857142857,
          0.8461538461538461
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "00972844",
      "score": 75.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-64d494223bf5bfc95f7512cbd9ccccdb"></a>

### v15.7.3 [`00773f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00773/00773f84.md) FUN_00773f84

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773f84.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "00773f84",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-56c2a4cf30614b9c956da2803a82810b"></a>

### v15.7.3 [`0077417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/0077417c.md) FUN_0077417c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0077417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/0077417c.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
        "reverse_margin": 80.0
      },
      "new": "0077417c",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7b445ee65afa4e479f5c0203a59d5a7a"></a>

### v15.7.3 [`00774240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774240.md) FUN_00774240

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00774240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774240.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "00774240",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v15.7.3 [`007746f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/007746f4.md) FUN_007746f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007746f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007746f4.md) · スコア 80.0 · 採用条件未達 · 順位差 19.037433 / 19.037433 · insufficient_independent_call_anchors
- 2. [`0097cf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cf48.md) · スコア 60.962567 · 採用条件未達 · 順位差 -19.037433 / -19.037433 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00773d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773d48.md) · スコア 58.609626 · 採用条件未達 · 順位差 -21.390374 / -21.390374 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00849bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849bd0.md) · スコア 58.609626 · 採用条件未達 · 順位差 -21.390374 / -21.390374 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00972844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972844.md) · スコア 58.609626 · 採用条件未達 · 順位差 -21.390374 / -21.390374 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00775088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775088.md) · スコア 57.433155 · 採用条件未達 · 順位差 -22.566845 / -22.566845 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00773a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773a18.md) · スコア 54.215686 · 採用条件未達 · 順位差 -25.784314000000002 / 54.215686 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00972fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972fa0.md) · スコア 49.625668 · 採用条件未達 · 順位差 -30.374332000000003 / -30.374332000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.037433,
        "reverse_margin": 19.037433
      },
      "new": "007746f4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8787878787878788,
          0.8787878787878788
        ],
        "cfg_coverage": [
          0.4117647058823529,
          0.4117647058823529
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.037433,
        "reverse_margin": -19.037433
      },
      "new": "0097cf48",
      "score": 60.962567
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8787878787878788,
          0.8787878787878788
        ],
        "cfg_coverage": [
          0.29411764705882354,
          0.35714285714285715
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.390374,
        "reverse_margin": -21.390374
      },
      "new": "00773d48",
      "score": 58.609626
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3b12f1c8c753874ec85e8d2eb317b71"></a>

### v15.7.3 [`00774918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774918.md) FUN_00774918

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00774918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774918.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "00774918",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b529ecf7c55267042c23e7cf0f59d20"></a>

### v15.7.3 [`00774b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774b10.md) FUN_00774b10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00774b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774b10.md) · スコア 80.0 · 採用条件未達 · 順位差 10.588234999999997 / 10.588234999999997 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00593fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593fc8.md) · スコア 69.411765 · 採用条件未達 · 順位差 -10.588234999999997 / 69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008534fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008534fc.md) · スコア 69.411765 · 採用条件未達 · 順位差 -10.588234999999997 / 69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00773fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773fe0.md) · スコア 34.235294 · 採用条件未達 · 順位差 -45.764706 / 34.235294 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 10.588234999999997,
        "reverse_margin": 10.588234999999997
      },
      "new": "00774b10",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          0.8235294117647058
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
        "margin": -10.588234999999997,
        "reverse_margin": 69.411765
      },
      "new": "00593fc8",
      "score": 69.411765
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          0.8235294117647058
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
        "margin": -10.588234999999997,
        "reverse_margin": 69.411765
      },
      "new": "008534fc",
      "score": 69.411765
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c77680b185c3c82add010dacccb54b65"></a>

### v15.7.3 [`00774bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00774/00774bd4.md) FUN_00774bd4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00774bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/00774bd4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "00774bd4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v15.7.3 [`00775088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775088.md) FUN_00775088

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00775088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775088.md) · スコア 80.0 · 採用条件未達 · 順位差 4.285713999999999 / 4.285713999999999 · insufficient_independent_call_anchors
- 2. [`00849bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849bd0.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · cfg_coverage, insufficient_independent_call_anchors
- 3. [`00972844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972844.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -4.285713999999999 · cfg_coverage, insufficient_independent_call_anchors
- 4. [`00773d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773d48.md) · スコア 72.857143 · 採用条件未達 · 順位差 -7.1428570000000065 / -7.1428570000000065 · cfg_coverage, insufficient_independent_call_anchors
- 5. [`0097cf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cf48.md) · スコア 58.502674 · 採用条件未達 · 順位差 -21.497326 / -21.497326 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007746f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00774/007746f4.md) · スコア 57.433155 · 採用条件未達 · 順位差 -22.566845 / -22.566845 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00972fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00972/00972fa0.md) · スコア 54.090909 · 採用条件未達 · 順位差 -25.909090999999997 / -25.909090999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.285713999999999,
        "reverse_margin": 4.285713999999999
      },
      "new": "00775088",
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
          0.7857142857142857,
          0.8461538461538461
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "00849bd0",
      "score": 75.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          0.7857142857142857,
          0.8461538461538461
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.285713999999999,
        "reverse_margin": -4.285713999999999
      },
      "new": "00972844",
      "score": 75.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-168cb61ef1045829c73a1913675946f6"></a>

### v15.7.3 [`007752c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/007752c4.md) FUN_007752c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007752c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/007752c4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007752c4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-40c0517998414ac443c4c9b06c94c818"></a>

### v15.7.3 [`007754bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/007754bc.md) FUN_007754bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007754bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/007754bc.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
        "reverse_margin": 80.0
      },
      "new": "007754bc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-57659e1db69617a3176b4d2298be067a"></a>

### v15.7.3 [`00775580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00775/00775580.md) FUN_00775580

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00775580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775580.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "00775580",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9afb539cade694e0134e6069b06d4b74"></a>

### v15.7.3 [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) FUN_007acf88

`competing_candidates` 

呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 214件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md)

- 1. [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · スコア 94.252142 · 採用条件未達 · 順位差 77.79268900000001 / 77.79268900000001 · instruction_coverage, unexplained_entry_return_or_effect_position
- 2. [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · スコア 16.459453 · 採用条件未達 · 順位差 -77.79268900000001 / 16.459453 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 3. [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · スコア 16.399782 · 採用条件未達 · 順位差 -77.85236 / 16.399782 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · スコア 16.386646 · 採用条件未達 · 順位差 -77.86549600000001 / 16.386646 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 5. [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · スコア 16.373047 · 採用条件未達 · 順位差 -77.879095 / 16.373047 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`008e68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e68f8.md) · スコア 16.242578 · 採用条件未達 · 順位差 -78.00956400000001 / 16.242578 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 7. [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · スコア 16.18836 · 採用条件未達 · 順位差 -78.063782 / 16.18836 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 8. [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · スコア 16.124847 · 採用条件未達 · 順位差 -78.127295 / 16.124847 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9708690330477356,
          0.9708690330477356
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 19,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 77.79268900000001,
        "reverse_margin": 77.79268900000001
      },
      "new": "007acf88",
      "score": 94.252142
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0067931456548347615,
          0.016569637259292433
        ],
        "cfg_coverage": [
          0.002593192868719611,
          0.0062256809338521405
        ],
        "mapped_data": 11,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -77.79268900000001,
        "reverse_margin": 16.459453
      },
      "new": "00749514",
      "score": 16.459453
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006425948592411261,
          0.007679929783499123
        ],
        "cfg_coverage": [
          0.0009724473257698541,
          0.0007112375533428165
        ],
        "mapped_data": 17,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -77.85236,
        "reverse_margin": 16.399782
      },
      "new": "0079bdf0",
      "score": 16.399782
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-26c5be0861995b7827d182b28bfdefb1"></a>

### v15.7.3 [`007c014c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c014c.md) FUN_007c014c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c014c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c014c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c014c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-714e4755db30ba312f7c11c3a03b0f7b"></a>

### v15.7.3 [`007c0744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0744.md) FUN_007c0744

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c0744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0744.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c0744",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2360c31b7b3b7c140f953257d9b6b084"></a>

### v15.7.3 [`007c0824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0824.md) FUN_007c0824

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c0824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0824.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c0824",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-23356c603cde707f3a63001f6b902a1b"></a>

### v15.7.3 [`007c0b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0b44.md) FUN_007c0b44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c0b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0b44.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c0b44",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-55b94c7c707ed159ace93369a5bd5298"></a>

### v15.7.3 [`007c0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0bf4.md) FUN_007c0bf4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c0bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0bf4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c0bf4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cf97e188449a36bdecc7648daf42a146"></a>

### v15.7.3 [`007c0e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c0/007c0e14.md) FUN_007c0e14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c0e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0e14.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c0e14",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5b3f704ebbae61011204227c44613614"></a>

### v15.7.3 [`007c1058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1058.md) FUN_007c1058

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c1058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1058.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c1058",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-947769228d184d7eb938a25118aa1567"></a>

### v15.7.3 [`007c12f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c12f8.md) FUN_007c12f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c12f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c12f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c12f8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-41c206c6ab52afa8c46866970628cdc0"></a>

### v15.7.3 [`007c1378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1378.md) FUN_007c1378

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c1378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1378.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c1378",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-477ecb97f7c16fa18123282cdd77fc13"></a>

### v15.7.3 [`007c146c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c146c.md) FUN_007c146c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c146c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c146c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c146c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-834d880d2b165595feac08c7518db204"></a>

### v15.7.3 [`007c1778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1778.md) FUN_007c1778

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1778.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c1778",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d668e8564a3d71bdf75f57521ecd2df7"></a>

### v15.7.3 [`007c17f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c17f8.md) FUN_007c17f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c17f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c17f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c17f8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-61e0f4ce0289aea4d404e618eb99cc5d"></a>

### v15.7.3 [`007c1b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1b90.md) FUN_007c1b90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c1b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1b90.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c1b90",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fc63910c4d9d231c110030ea82b5766b"></a>

### v15.7.3 [`007c1c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c40.md) FUN_007c1c40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c40.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c1c40",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c2f68e213e0227708f615a9c085d309d"></a>

### v15.7.3 [`007c247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c247c.md) FUN_007c247c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c247c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c247c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c247c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-34174ee5175f003f22c70bd4738a1a78"></a>

### v15.7.3 [`007c2564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2564.md) FUN_007c2564

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c2564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2564.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c2564",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c1b94e86620ad41f4a20bdb8e0a73981"></a>

### v15.7.3 [`007c266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c266c.md) FUN_007c266c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c266c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c266c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9e8011cf9bfa7ca69264dcc99fed23b4"></a>

### v15.7.3 [`007c27d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c27d8.md) FUN_007c27d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c27d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c27d8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c27d8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c5b95e4b43f09063b65dc6f97662c89d"></a>

### v15.7.3 [`007c28a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c28a0.md) FUN_007c28a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c28a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c28a0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c28a0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b144f4ebe9f767cfc8ebd25539873c4c"></a>

### v15.7.3 [`007c2fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c2/007c2fe8.md) FUN_007c2fe8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c2fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c2/007c2fe8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c2fe8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c89829aaa8ff09722fd59b6d2523e173"></a>

### v15.7.3 [`007c3470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3470.md) FUN_007c3470

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3470.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3470",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a040a003c07311bb1d400b6ff7a3330a"></a>

### v15.7.3 [`007c36b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36b0.md) FUN_007c36b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c36b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c36b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c36b0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-451296f87b197cda33f31d7dc73cf9e3"></a>

### v15.7.3 [`007c37b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37b4.md) FUN_007c37b4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c37b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c37b4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c37b4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-823236160e13a8c1ef988c63cd04482b"></a>

### v15.7.3 [`007c3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3864.md) FUN_007c3864

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3864.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3864",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c256d578f046c6aa51f693222eaada07"></a>

### v15.7.3 [`007c3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c38.md) FUN_007c3c38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3c38.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3c38",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-159bb35af0fad6f7410be05bc7e810e1"></a>

### v15.7.3 [`007c3d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d1c.md) FUN_007c3d1c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3d1c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3d1c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c7dae4782fd65b06c4d0d8ffbe4642e3"></a>

### v15.7.3 [`007c3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ebc.md) FUN_007c3ebc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3ebc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3ebc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4431586e75f76de5ead05474098b3789"></a>

### v15.7.3 [`007c3f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3f64.md) FUN_007c3f64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c3f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3f64.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c3f64",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ee5086795ec4ca1c5570da4902a91be0"></a>

### v15.7.3 [`007c4288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4288.md) FUN_007c4288

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4288.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4288",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4224e4abe2354b01db0f344808b00350"></a>

### v15.7.3 [`007c4524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4524.md) FUN_007c4524

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4524.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4524",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0e0020968b54055244fc060754e6c972"></a>

### v15.7.3 [`007c4604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4604.md) FUN_007c4604

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4604.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4604",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d392af99b48e2980d7be93456031ba0b"></a>

### v15.7.3 [`007c48a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48a0.md) FUN_007c48a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c48a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c48a0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c48a0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9d8ca61129ae981fa6459f72fda9237b"></a>

### v15.7.3 [`007c4980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4980.md) FUN_007c4980

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4980.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4980",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-23b51f2cf6ab283d1fbc0b6328e99838"></a>

### v15.7.3 [`007c4cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4cf8.md) FUN_007c4cf8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4cf8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4cf8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5bc497e0769b06083eb1df2edbf639fc"></a>

### v15.7.3 [`007c4d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d58.md) FUN_007c4d58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d58.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "007c4d58",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8adf34e2dfda07191a52cb8b93581033"></a>

### v15.7.3 [`007c4d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d78.md) FUN_007c4d78

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4d78.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4d78",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d28e141ecd47755498607372f1cb1722"></a>

### v15.7.3 [`007c4f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f28.md) FUN_007c4f28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c4f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c4/007c4f28.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c4f28",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-38d29da1f6fe8b4987f10509b3d66de7"></a>

### v15.7.3 [`007c50bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c50bc.md) FUN_007c50bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c50bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c50bc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c50bc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7dfe76e7e86e6c732de3be94247c9c4a"></a>

### v15.7.3 [`007c5164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5164.md) FUN_007c5164

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5164.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5164",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-00bce0eaf1dbd1f6fa3d1bd0de28f99d"></a>

### v15.7.3 [`007c5214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5214.md) FUN_007c5214

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5214.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5214",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-453f0e7c36351e7981d32232b184645f"></a>

### v15.7.3 [`007c52c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52c4.md) FUN_007c52c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c52c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c52c4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c52c4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8e6a0cfe606f1b680b0513e13f90c09b"></a>

### v15.7.3 [`007c5374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5374.md) FUN_007c5374

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5374.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5374",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a83ae190588e021442be3ffe6817089"></a>

### v15.7.3 [`007c5424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5424.md) FUN_007c5424

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5424.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5424",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f68fe2a728995a3995382fcc2c50b930"></a>

### v15.7.3 [`007c5710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5710.md) FUN_007c5710

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5710.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5710",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e6f05240787d590fc9c8812d48116415"></a>

### v15.7.3 [`007c5a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5a70.md) FUN_007c5a70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5a70.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5a70",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5d662167e3aa22378d2a153dec32acf0"></a>

### v15.7.3 [`007c5d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d18.md) FUN_007c5d18

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5d18.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5d18",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-77accd24407b0c2b9b92152378144a33"></a>

### v15.7.3 [`007c5dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5dd4.md) FUN_007c5dd4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c5dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5dd4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c5dd4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ac102b2b1bc505b31be35369873764a4"></a>

### v15.7.3 [`007c615c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c615c.md) FUN_007c615c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c615c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c615c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c615c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-80c7616e6c767aa25f60212c6eac57cc"></a>

### v15.7.3 [`007c6250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6250.md) FUN_007c6250

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6250.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6250",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-694b86e1916a1535b6f2cdccd249ba46"></a>

### v15.7.3 [`007c6438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6438.md) FUN_007c6438

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6438.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6438",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2c1bd7c6a853a624a102b3bb0682609d"></a>

### v15.7.3 [`007c67d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c67d0.md) FUN_007c67d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c67d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c67d0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c67d0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-98d0240f4c51aa71224367faca15647e"></a>

### v15.7.3 [`007c6a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a2c.md) FUN_007c6a2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6a2c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6a2c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6cada121084739356502a9ea959ba2ab"></a>

### v15.7.3 [`007c6adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6adc.md) FUN_007c6adc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6adc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6adc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-30897d7666659ca2c78ad534410020ae"></a>

### v15.7.3 [`007c6b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b8c.md) FUN_007c6b8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6b8c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6b8c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7e431334c9a4daa2c130e975e3d0d8ed"></a>

### v15.7.3 [`007c6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c3c.md) FUN_007c6c3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6c3c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6c3c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f471f4953fb80145bf33e7afb35ede83"></a>

### v15.7.3 [`007c6cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6cec.md) FUN_007c6cec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6cec.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6cec",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eeb2c60cedf3dbfd1d60b5e49adcd6b4"></a>

### v15.7.3 [`007c6d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6d9c.md) FUN_007c6d9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6d9c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6d9c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a6af247cb9332ccd7bd6444ee0ee6cbf"></a>

### v15.7.3 [`007c6e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e68.md) FUN_007c6e68

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6e68.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6e68",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b5bc78cfbded80832338b7d053faaf82"></a>

### v15.7.3 [`007c6f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f18.md) FUN_007c6f18

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c6f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c6/007c6f18.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c6f18",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-24502a36df4dd4161fbb5828da0e44bd"></a>

### v15.7.3 [`007c7580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7580.md) FUN_007c7580

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c7580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7580.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c7580",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aeead89b25b55b6706a93b6cbd01e4b2"></a>

### v15.7.3 [`007c7690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7690.md) FUN_007c7690

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c7690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7690.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c7690",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-05469cfa2a65c017f873a093f591d1c9"></a>

### v15.7.3 [`007c7740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7740.md) FUN_007c7740

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c7740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7740.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c7740",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-45f69734034e9a02a68645b7f30a445e"></a>

### v15.7.3 [`007c77c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c0.md) FUN_007c77c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c77c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "007c77c0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7a44e91cb9f9db787573e795e13377d4"></a>

### v15.7.3 [`007c7da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7da0.md) FUN_007c7da0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c7da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c7da0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c7da0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8520a4e131e49e502881ad031363d734"></a>

### v15.7.3 [`007c8028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8028.md) FUN_007c8028

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c8028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8028.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c8028",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-86b7514050f018ba1859f51d40011f6e"></a>

### v15.7.3 [`007c8c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c00.md) FUN_007c8c00

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c8c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c00.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c8c00",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eee8d15dec81d2eae7c2eb348d8d5ae0"></a>

### v15.7.3 [`007c8c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c70.md) FUN_007c8c70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c8c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c70.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "007c8c70",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e80cbf7735312925dc3940a24d5d2f98"></a>

### v15.7.3 [`007c8eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8eac.md) FUN_007c8eac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c8eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8eac.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c8eac",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-99a1fb130be289b724097691b36699c3"></a>

### v15.7.3 [`007c8f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f5c.md) FUN_007c8f5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c8f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8f5c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c8f5c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f1802853be4226b77667061ef788a0b9"></a>

### v15.7.3 [`007c900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c900c.md) FUN_007c900c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c900c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c900c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c900c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9e0896cefc3e2a666f59e86d501ec065"></a>

### v15.7.3 [`007c90bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c90bc.md) FUN_007c90bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c90bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c90bc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c90bc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e560c3cf6911241d2006918a74ce76e3"></a>

### v15.7.3 [`007c9180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9180.md) FUN_007c9180

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9180.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9180",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aaa8b9a7e00af3fd1961c2d8e5ad5435"></a>

### v15.7.3 [`007c9244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9244.md) FUN_007c9244

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9244.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9244",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-39f567810d68a56d1a34c64708e177d1"></a>

### v15.7.3 [`007c92f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c92f4.md) FUN_007c92f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c92f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c92f4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c92f4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c33462276f2881e6dfa328f073d36490"></a>

### v15.7.3 [`007c9354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9354.md) FUN_007c9354

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)

- 1. [`007c9354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9354.md) · スコア 84.0 · 採用条件未達 · 順位差 34.757576 / 34.757576 · insufficient_independent_call_anchors
- 2. [`007c9cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9cac.md) · スコア 49.242424 · 採用条件未達 · 順位差 -34.757576 / 49.242424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007c9d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d9c.md) · スコア 49.242424 · 採用条件未達 · 順位差 -34.757576 / 49.242424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007c3710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3710.md) · スコア 42.272727 · 採用条件未達 · 順位差 -41.727273 / 42.272727 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a3c2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c2c4.md) · スコア 40.606061 · 採用条件未達 · 順位差 -43.393939 / 40.606061 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00aad21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md) · スコア 33.636364 · 採用条件未達 · 順位差 -50.363636 / 33.636364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00aad338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md) · スコア 33.636364 · 採用条件未達 · 順位差 -50.363636 / 33.636364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007c944c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c944c.md) · スコア 28.205128 · 採用条件未達 · 順位差 -55.794872 / 28.205128 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "mapped_data": 2,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.757576,
        "reverse_margin": 34.757576
      },
      "new": "007c9354",
      "score": 84.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6388888888888888,
          0.8518518518518519
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -34.757576,
        "reverse_margin": 49.242424
      },
      "new": "007c9cac",
      "score": 49.242424
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6388888888888888,
          0.8518518518518519
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -34.757576,
        "reverse_margin": 49.242424
      },
      "new": "007c9d9c",
      "score": 49.242424
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e5f22c89ce18e6ec51e341de1b489094"></a>

### v15.7.3 [`007c9400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9400.md) FUN_007c9400

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9400.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9400",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d81900e3098a4c8e806470cb8d965922"></a>

### v15.7.3 [`007c94e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c94e0.md) FUN_007c94e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c94e0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c94e0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a1e2dbf940d659e1b9627bc11643898"></a>

### v15.7.3 [`007c9630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9630.md) FUN_007c9630

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9630.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9630",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-dacc9eefb57a1aa301777d4cdba582a7"></a>

### v15.7.3 [`007c96e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c96e0.md) FUN_007c96e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c96e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c96e0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c96e0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e8f59cc4942cf11c2bdf290828fed79e"></a>

### v15.7.3 [`007c9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9790.md) FUN_007c9790

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9790.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9790",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d9a6c48a66486e86e48395ec6e6fec6f"></a>

### v15.7.3 [`007c9840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9840.md) FUN_007c9840

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9840.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9840",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-48225dc0160c12e01e05f876249be5e8"></a>

### v15.7.3 [`007c9978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9978.md) FUN_007c9978

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9978.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9978",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2ee3c1abe263662de6b887b463625640"></a>

### v15.7.3 [`007c9aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9aac.md) FUN_007c9aac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9aac.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9aac",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2e25753770cfa0421c00d41848cadcb2"></a>

### v15.7.3 [`007c9b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9b78.md) FUN_007c9b78

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9b78.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9b78",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-002c3a949eefb10c5b00ba493d9cd950"></a>

### v15.7.3 [`007c9c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c44.md) FUN_007c9c44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9c44.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9c44",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7bb79bf8de1db8977aa0b8889c5123b0"></a>

### v15.7.3 [`007c9d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d34.md) FUN_007c9d34

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9d34.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9d34",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-86fff1c30d88d87c074c1d7ee70109d2"></a>

### v15.7.3 [`007c9e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e24.md) FUN_007c9e24

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007c9e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c9e24.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "007c9e24",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

