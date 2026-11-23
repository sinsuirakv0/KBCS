# v15.7.4 → v16.0.0 · 追加調査 (30)

[一覧の目次](README.md)

<a id="review-aebafec53acb2444e175f72af2a1f600"></a>

### v15.7.4 [`00584050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584050.md) FUN_00584050

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a685c.md) · スコア 62.0 · 採用条件未達 · 順位差 41.0 / 62.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005a8790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md) · スコア 21.0 · 採用条件未達 · 順位差 -41.0 / 9.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0059d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0059ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0059f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a0978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005a51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a51fc.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a5b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5b9c.md) · スコア 5.0 · 採用条件未達 · 順位差 -57.0 / -29.933332999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7,
          0.7
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
        "margin": 41.0,
        "reverse_margin": 62.0
      },
      "new": "005a685c",
      "score": 62.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35,
          0.35
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
        "margin": -41.0,
        "reverse_margin": 9.0
      },
      "new": "005a8790",
      "score": 21.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1,
          0.08333333333333333
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
        "margin": -57.0,
        "reverse_margin": -57.5
      },
      "new": "0059d52c",
      "score": 5.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-847a9ec71e6853802b240a20c219571e"></a>

### v15.7.4 [`005840a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/005840a0.md) FUN_005840a0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005b5414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5414.md) · スコア 40.416667 · 採用条件未達 · 順位差 6.416666999999997 / 40.416667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005a5bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5bfc.md) · スコア 34.0 · 採用条件未達 · 順位差 -6.416666999999997 / 7.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0059fbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fbd8.md) · スコア 26.25 · 採用条件未達 · 順位差 -14.166666999999997 / 26.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005a87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md) · スコア 26.25 · 採用条件未達 · 順位差 -14.166666999999997 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0059c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c078.md) · スコア 22.5 · 採用条件未達 · 順位差 -17.916666999999997 / -42.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0059d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d58c.md) · スコア 22.5 · 採用条件未達 · 順位差 -17.916666999999997 / -42.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0059f73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f73c.md) · スコア 22.5 · 採用条件未達 · 順位差 -17.916666999999997 / -42.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a09d8.md) · スコア 22.5 · 採用条件未達 · 順位差 -17.916666999999997 / -42.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5625,
          0.5625
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.416666999999997,
        "reverse_margin": 40.416667
      },
      "new": "005b5414",
      "score": 40.416667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          0.2,
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
        "margin": -6.416666999999997,
        "reverse_margin": 7.75
      },
      "new": "005a5bfc",
      "score": 34.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4375,
          0.4375
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
        "margin": -14.166666999999997,
        "reverse_margin": 26.25
      },
      "new": "0059fbd8",
      "score": 26.25
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dabed9dac0f0eda8d4375449a1c95b99"></a>

### v15.7.4 [`005840e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/005840e0.md) FUN_005840e0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`0059ee54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee54.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005a87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -53.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a8820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8820.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a8830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8830.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 65.0,
        "reverse_margin": 30.0
      },
      "new": "0059ee54",
      "score": 65.0
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
        "margin": -65.0,
        "reverse_margin": -53.75
      },
      "new": "005a87e0",
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
        "margin": -65.0,
        "reverse_margin": 0.0
      },
      "new": "005a8820",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-89106edbad3646b4f73a8672e6cb259b"></a>

### v15.7.4 [`005840f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/005840f0.md) FUN_005840f0

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059ee64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee64.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a8790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md) · スコア 12.0 · 採用条件未達 · 順位差 -58.0 / -9.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -53.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a8820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8820.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005a8830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8830.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "0059ee64",
      "score": 70.0
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
        "margin": -10.0,
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
        "margin": -45.0,
        "reverse_margin": -10.0
      },
      "new": "005a8884",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1e59035457c92527e1ec5fed6533d12b"></a>

### v15.7.4 [`00584120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584120.md) FUN_00584120

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059d60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d60c.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0059f7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7bc.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`0059ff3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff3c.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 57.5 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005a0a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a58.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`005a53dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a53dc.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`005a5d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5d7c.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`0059c058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c058.md) · スコア 42.5 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
      "new": "0059d60c",
      "score": 57.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
      "new": "0059f7bc",
      "score": 57.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "reverse_margin": 57.5
      },
      "new": "0059ff3c",
      "score": 57.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f1d5fdf7e5c3905c3d1bbbeb7da7989c"></a>

### v15.7.4 [`00584140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584140.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a8880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8880.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 77.4167 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`005a8830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8830.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`005a8894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8894.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 5. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 5.0172 · 採用条件未達 · 順位差 — / — · 
- 6. [`005a88c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88c4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005a8820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8820.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 
- 8. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 77.4167
      },
      "new": "005a8880",
      "score": 83.0
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
      "new": "005a8830",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1174bd750d8c8398e5e1ad20b3c76711"></a>

### v15.7.4 [`00584144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584144.md) FUN_00584144

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`0059eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eef8.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005a8830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8830.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a8894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8894.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "0059eef8",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": 10.0
      },
      "new": "005a8884",
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
        "margin": -65.0,
        "reverse_margin": 0.0
      },
      "new": "005a8830",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1d4bd867ad8d424df244d37e2975f457"></a>

### v15.7.4 [`00584154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584154.md) FUN_00584154

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059ef08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ef08.md) · スコア 35.0 · 採用条件未達 · 順位差 15.0 / -25.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 20.0 · 採用条件未達 · 順位差 -15.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a8894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8894.md) · スコア 20.0 · 採用条件未達 · 順位差 -15.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -57.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5833333333333334,
          0.5833333333333334
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
        "margin": 15.0,
        "reverse_margin": -25.0
      },
      "new": "0059ef08",
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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.0,
        "reverse_margin": -40.0
      },
      "new": "0043bd58",
      "score": 20.0
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
        "margin": -15.0,
        "reverse_margin": -45.0
      },
      "new": "005a8894",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a5065fb7c58cdf60450de617c5ffe77e"></a>

### v15.7.4 [`00584184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584184.md) FUN_00584184

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005a88c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88c4.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`005a8880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8880.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005a88c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88c8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005a8894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8894.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "005a88c4",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005a8880",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005a88c8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e18034b6619a50e2642282e9fc485b3a"></a>

### v15.7.4 [`00584188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584188.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a88c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88c8.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 77.4167 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`005a8894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8894.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`005a88c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88c4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 77.4167
      },
      "new": "005a88c8",
      "score": 83.0
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
      "new": "005a8894",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a6cc9360e5afd4f274b22e3de4efa254"></a>

### v15.7.4 [`00585038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585038.md) thunk_FUN_00428c14

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00428c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c14.md)

- 1. [`005a9778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9778.md) · スコア 32.2353 · 採用条件未達 · 順位差 32.2353 / 32.2353 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 32.2353,
        "reverse_margin": 32.2353
      },
      "new": "005a9778",
      "score": 32.2353
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f9f66b03fc39a70dad912b9640bb098c"></a>

### v15.7.4 [`005851ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005851ec.md) FUN_005851ec

`competing_candidates` 

呼出元 0件  · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

- 1. [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) · スコア 16.183673 · 採用条件未達 · 順位差 1.9771949999999983 / 16.183673 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0093614c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md) · スコア 14.206478 · 採用条件未達 · 順位差 -1.9771949999999983 / 14.206478 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00473fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473fd0.md) · スコア 12.328767 · 採用条件未達 · 順位差 -3.8549059999999997 / 12.328767 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004fb360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md) · スコア 12.328767 · 採用条件未達 · 順位差 -3.8549059999999997 / 12.328767 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004fb4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md) · スコア 12.328767 · 採用条件未達 · 順位差 -3.8549059999999997 / 12.328767 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) · スコア 12.186813 · 採用条件未達 · 順位差 -3.996859999999998 / 12.186813 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004c9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md) · スコア 12.151899 · 採用条件未達 · 順位差 -4.031773999999999 / 12.151899 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0052d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) · スコア 10.35443 · 採用条件未達 · 順位差 -5.829242999999998 / 10.35443 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3013698630136986,
          0.22448979591836735
        ],
        "cfg_coverage": [
          0.06666666666666667,
          0.03571428571428571
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.9771949999999983,
        "reverse_margin": 16.183673
      },
      "new": "0051c7cc",
      "score": 16.183673
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3972602739726027,
          0.1858974358974359
        ],
        "cfg_coverage": [
          0.13333333333333333,
          0.05263157894736842
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -1.9771949999999983,
        "reverse_margin": 14.206478
      },
      "new": "0093614c",
      "score": 14.206478
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2054794520547945,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.8549059999999997,
        "reverse_margin": 12.328767
      },
      "new": "00473fd0",
      "score": 12.328767
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d7b34f261a65b55e0c77a26d74ea2f46"></a>

### v15.7.4 [`00585348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585348.md) FUN_00585348

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

- 1. [`005a9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9aa0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005a9ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -65.6 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a9b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -60.0
      },
      "new": "005a9aa0",
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
        "reverse_margin": -30.0
      },
      "new": "005a9ad0",
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
        "reverse_margin": -65.6
      },
      "new": "005a9b18",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7e1ab3ed1317101825829c428c56a18c"></a>

### v15.7.4 [`00585378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585378.md) FUN_00585378

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`005a3f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md) · スコア 43.333333 · 採用条件未達 · 順位差 13.333333000000003 / 43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0059f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md) · スコア 30.0 · 採用条件未達 · 順位差 -13.333333000000003 / -26.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a9ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md) · スコア 30.0 · 採用条件未達 · 順位差 -13.333333000000003 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0059caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md) · スコア 13.333333 · 採用条件未達 · 順位差 -30.000000000000004 / -43.333333999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0059d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md) · スコア 13.333333 · 採用条件未達 · 順位差 -30.000000000000004 / -43.333333999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0059ec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md) · スコア 13.333333 · 採用条件未達 · 順位差 -30.000000000000004 / -63.33333400000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005a08cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md) · スコア 13.333333 · 採用条件未達 · 順位差 -30.000000000000004 / -63.33333400000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md) · スコア 13.333333 · 採用条件未達 · 順位差 -30.000000000000004 / -43.333333999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3888888888888889,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 13.333333000000003,
        "reverse_margin": 43.333333
      },
      "new": "005a3f58",
      "score": 43.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
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
        "margin": -13.333333000000003,
        "reverse_margin": -26.666666999999997
      },
      "new": "0059f630",
      "score": 30.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
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
        "margin": -13.333333000000003,
        "reverse_margin": 0.0
      },
      "new": "005a9ad0",
      "score": 30.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c096914e725ee220a048a47a6ad2c5a9"></a>

### v15.7.4 [`005853c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005853c0.md) FUN_005853c0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) · スコア 36.0 · 採用条件未達 · 順位差 0.0 / -29.599999999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) · スコア 36.0 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a6988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md) · スコア 26.4 · 採用条件未達 · 順位差 -9.600000000000001 / -34.933333000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0059d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md) · スコア 19.2 · 採用条件未達 · 順位差 -16.8 / -46.39999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0059ecd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md) · スコア 19.2 · 採用条件未達 · 順位差 -16.8 / -46.39999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0059f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md) · スコア 19.2 · 採用条件未達 · 順位差 -16.8 / -46.39999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005a0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md) · スコア 19.2 · 採用条件未達 · 順位差 -16.8 / -46.39999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a5198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md) · スコア 19.2 · 採用条件未達 · 順位差 -16.8 / -46.39999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": -29.599999999999994
      },
      "new": "005a9b18",
      "score": 36.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.6
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005ac3a4",
      "score": 36.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.44,
          0.55
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
        "margin": -9.600000000000001,
        "reverse_margin": -34.933333000000005
      },
      "new": "005a6988",
      "score": 26.4
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0669e714fa5bd54b24d4a45f79a612d2"></a>

### v15.7.4 [`00585424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585424.md) FUN_00585424

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a5b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5b38.md) · スコア 22.133333 · 採用条件未達 · 順位差 2.1333330000000004 / -17.503031 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005a9b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md) · スコア 20.0 · 採用条件未達 · 順位差 -2.1333330000000004 / 5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005ac408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac408.md) · スコア 17.5 · 採用条件未達 · 順位差 -4.633333 / -5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) · スコア 14.4 · 採用条件未達 · 順位差 -7.733333 / -21.6 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) · スコア 9.6 · 採用条件未達 · 順位差 -12.533333 / -55.99999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a5b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5b9c.md) · スコア 2.5 · 採用条件未達 · 順位差 -19.633333 / -32.433333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0059d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.133333 / -62.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0059ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.133333 / -62.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.28
        ],
        "cfg_coverage": [
          0.26666666666666666,
          0.36363636363636365
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.1333330000000004,
        "reverse_margin": -17.503031
      },
      "new": "005a5b38",
      "score": 22.133333
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
          0.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.1333330000000004,
        "reverse_margin": 5.0
      },
      "new": "005a9b7c",
      "score": 20.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.2916666666666667
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
        "margin": -4.633333,
        "reverse_margin": -5.0
      },
      "new": "005ac408",
      "score": 17.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-32f43de0f1e7bc1b1a89b69ae16afeb1"></a>

### v15.7.4 [`00585a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585a7c.md) FUN_00585a7c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`0059f77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f77c.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005aa1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1d4.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005aa1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "0059f77c",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "005aa1d4",
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
        "margin": -65.0,
        "reverse_margin": -35.0
      },
      "new": "005aa1e4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2b30c5f50974a480b496fa561fe33f6a"></a>

### v15.7.4 [`00585a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585a8c.md) FUN_00585a8c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059f78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f78c.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005aa1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1d4.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005aa1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md) · スコア 20.0 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "0059f78c",
      "score": 70.0
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
        "margin": -10.0,
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
        "margin": -45.0,
        "reverse_margin": -40.0
      },
      "new": "005aa1d4",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-67ee0b50e5355d93392e0ee059efb9eb"></a>

### v15.7.4 [`00585ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585ac8.md) FUN_00585ac8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`0059f7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7e0.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 40.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005aa220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005aa230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 40.0
      },
      "new": "0059f7e0",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": 10.0
      },
      "new": "005aa220",
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
        "margin": -65.0,
        "reverse_margin": -20.0
      },
      "new": "005aa230",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c25eba2f51f5ff761eea0e39e8160799"></a>

### v15.7.4 [`00585ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585ad8.md) FUN_00585ad8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059f7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f7f0.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005aa220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005aa230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md) · スコア 20.0 · 採用条件未達 · 順位差 -50.0 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 50.0
      },
      "new": "0059f7f0",
      "score": 70.0
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
        "margin": -10.0,
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
        "margin": -45.0,
        "reverse_margin": -10.0
      },
      "new": "005aa220",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f7d465992955adaa99d3f9d86dbdae1e"></a>

### v15.7.4 [`00585b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585b08.md) FUN_00585b08

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005aa260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa260.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`005aa220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005aa230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005aa260",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005aa220",
      "score": 1.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005aa230",
      "score": 0.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c20e69fc1ba39b3d5eccdb24815c9476"></a>

### v15.7.4 [`00586748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586748.md) thunk_FUN_00428c14

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00428c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c14.md)

- 1. [`005aaea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea0.md) · スコア 32.2353 · 採用条件未達 · 順位差 32.2353 / 32.2353 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 32.2353,
        "reverse_margin": 32.2353
      },
      "new": "005aaea0",
      "score": 32.2353
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-43b26adedf7e9e44f9b5a58813131151"></a>

### v15.7.4 [`00586964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586964.md) FUN_00586964

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

- 1. [`005a267c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a267c.md) · スコア 65.0 · 採用条件未達 · 順位差 5.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005a67e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a67e4.md) · スコア 60.0 · 採用条件未達 · 順位差 -5.0 / 5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005a9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9aa0.md) · スコア 60.0 · 採用条件未達 · 順位差 -5.0 / 5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0056527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056527c.md) · スコア 55.0 · 採用条件未達 · 順位差 -10.0 / 55.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c17040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17040.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00574a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a00.md) · スコア 33.333333 · 採用条件未達 · 順位差 -31.666666999999997 / 33.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005ab0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0bc.md) · スコア 20.0 · 採用条件未達 · 順位差 -45.0 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009ba704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba704.md) · スコア 8.611955 · 採用条件未達 · 順位差 -56.388045 / 8.611955 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.0,
        "reverse_margin": 10.0
      },
      "new": "005a267c",
      "score": 65.0
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.0,
        "reverse_margin": 5.0
      },
      "new": "005a67e4",
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.0,
        "reverse_margin": 5.0
      },
      "new": "005a9aa0",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fc4e52a02baad2f5b5b31cdc8a1d8188"></a>

### v15.7.4 [`00586b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586b7c.md) FUN_00586b7c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`005ab2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2d4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005ab2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005ab2d4",
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
        "reverse_margin": -20.0
      },
      "new": "005ab2e4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e586a73ece08079838fe9abb6c54f58d"></a>

### v15.7.4 [`00586b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586b8c.md) FUN_00586b8c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff0c.md) · スコア 60.0 · 採用条件未達 · 順位差 40.0 / 15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 20.0 · 採用条件未達 · 順位差 -40.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005ab2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md) · スコア 20.0 · 採用条件未達 · 順位差 -40.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ab2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2d4.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 40.0,
        "reverse_margin": 15.0
      },
      "new": "0059ff0c",
      "score": 60.0
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
        "margin": -40.0,
        "reverse_margin": -40.0
      },
      "new": "0043bd58",
      "score": 20.0
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
        "margin": -40.0,
        "reverse_margin": 0.0
      },
      "new": "005ab2e4",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aec7b14847d560eeafec1f7ac5c477df"></a>

### v15.7.4 [`00586c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586c30.md) FUN_00586c30

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`0059ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff60.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ab398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md) · スコア 25.0 · 採用条件未達 · 順位差 -40.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 0.0
      },
      "new": "0059ff60",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": 10.0
      },
      "new": "005ab388",
      "score": 35.0
    },
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
        "margin": -40.0,
        "reverse_margin": -35.0
      },
      "new": "005ab398",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d093582d011d07fa575bacac3a37b4a1"></a>

### v15.7.4 [`00586c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586c40.md) FUN_00586c40

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059ff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059ff70.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ab398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`005ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "0059ff70",
      "score": 70.0
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
        "margin": -10.0,
        "reverse_margin": 0.0
      },
      "new": "0043bd58",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.0,
        "reverse_margin": 35.0
      },
      "new": "005ab398",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9571ed0a045c21d08efb8e00ff7151b8"></a>

### v15.7.4 [`00586c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586c70.md) FUN_00586c70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005ab3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab3c8.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`005ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005ab398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005ab3c8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005ab388",
      "score": 1.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005ab398",
      "score": 0.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-dc54f8817062f94628c1b8ba4830872c"></a>

### v15.7.4 [`005878b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/005878b8.md) thunk_FUN_00428c14

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00428c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c14.md)

- 1. [`005ac010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac010.md) · スコア 32.2353 · 採用条件未達 · 順位差 32.2353 / 32.2353 · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 32.2353,
        "reverse_margin": 32.2353
      },
      "new": "005ac010",
      "score": 32.2353
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e2880f5b21100bda025151155524fcd0"></a>

### v15.7.4 [`00587ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587ad4.md) FUN_00587ad4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

- 1. [`005ac22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac22c.md) · スコア 51.666667 · 採用条件未達 · 順位差 51.666667 / 51.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 2. [`005ac25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md) · スコア 0.0 · 採用条件未達 · 順位差 -51.666667 / -13.170732 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005ac35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md) · スコア 0.0 · 採用条件未達 · 順位差 -51.666667 / -56.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -51.666667 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.5,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 51.666667,
        "reverse_margin": 51.666667
      },
      "new": "005ac22c",
      "score": 51.666667
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
        "margin": -51.666667,
        "reverse_margin": -13.170732
      },
      "new": "005ac25c",
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
        "margin": -51.666667,
        "reverse_margin": -56.666667
      },
      "new": "005ac35c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b51ffe10733fc33323f2becf62f6e855"></a>

### v15.7.4 [`00587b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587b04.md) FUN_00587b04

`competing_candidates` 

呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0057945c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/0057945c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) · スコア 14.67033 · 採用条件未達 · 順位差 0.604673 / 14.67033 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005788d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md) · スコア 14.065657 · 採用条件未達 · 順位差 -0.604673 / 14.065657 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005ac25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac25c.md) · スコア 13.170732 · 採用条件未達 · 順位差 -1.4995980000000007 / 0.8980049999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005a57d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a57d8.md) · スコア 11.623377 · 採用条件未達 · 順位差 -3.0469530000000002 / 4.246327999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) · スコア 10.673469 · 採用条件未達 · 順位差 -3.996860999999999 / 10.673469 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b06460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06460.md) · スコア 10.567073 · 採用条件未達 · 順位差 -4.103256999999999 / -52.187644 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0088f080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f080.md) · スコア 9.835366 · 採用条件未達 · 順位差 -4.834963999999999 / 9.835366 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0093614c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md) · スコア 9.834008 · 採用条件未達 · 順位差 -4.836321999999999 / 9.834008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32926829268292684,
          0.17307692307692307
        ],
        "cfg_coverage": [
          0.25,
          0.11428571428571428
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.604673,
        "reverse_margin": 14.67033
      },
      "new": "0046d0e0",
      "score": 14.67033
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23170731707317074,
          0.2159090909090909
        ],
        "cfg_coverage": [
          0.0625,
          0.05555555555555555
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.604673,
        "reverse_margin": 14.065657
      },
      "new": "005788d0",
      "score": 14.065657
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21951219512195122,
          0.4
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
        "margin": -1.4995980000000007,
        "reverse_margin": 0.8980049999999995
      },
      "new": "005ac25c",
      "score": 13.170732
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0e64efdda69eaf30107e2f8e73c122a8"></a>

### v15.7.4 [`00587c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587c9c.md) FUN_00587c9c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`005a08cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a08cc.md) · スコア 76.666667 · 採用条件未達 · 順位差 20.000000000000007 / 20.000000000000007 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0059caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059caf0.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`0059d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d480.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`0059ec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ec8c.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / -20.000000000000007 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`0059f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f630.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`005a16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16a0.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`005a5150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5150.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`005ac35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md) · スコア 56.666667 · 採用条件未達 · 順位差 -20.000000000000007 / 56.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9444444444444444,
          0.9444444444444444
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
        "margin": 20.000000000000007,
        "reverse_margin": 20.000000000000007
      },
      "new": "005a08cc",
      "score": 76.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6111111111111112,
          0.6111111111111112
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
        "margin": -20.000000000000007,
        "reverse_margin": 0.0
      },
      "new": "0059caf0",
      "score": 56.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6111111111111112,
          0.6111111111111112
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
        "margin": -20.000000000000007,
        "reverse_margin": 0.0
      },
      "new": "0059d480",
      "score": 56.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.4 [`00587ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587ce4.md) FUN_00587ce4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) · スコア 65.6 · 採用条件未達 · 順位差 4.799999999999997 / 4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0059d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d4c8.md) · スコア 60.8 · 採用条件未達 · 順位差 -4.799999999999997 / -4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`0059ecd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ecd4.md) · スコア 60.8 · 採用条件未達 · 順位差 -4.799999999999997 / -4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`0059f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f678.md) · スコア 60.8 · 採用条件未達 · 順位差 -4.799999999999997 / -4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 5. [`005a0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0914.md) · スコア 60.8 · 採用条件未達 · 順位差 -4.799999999999997 / -4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`005a5198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a5198.md) · スコア 60.8 · 採用条件未達 · 順位差 -4.799999999999997 / -4.799999999999997 · instruction_coverage, insufficient_independent_call_anchors
- 7. [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) · スコア 36.0 · 採用条件未達 · 順位差 -29.599999999999994 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005a6988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md) · スコア 26.4 · 採用条件未達 · 順位差 -39.199999999999996 / -34.933333000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.76,
          0.76
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
        "margin": 4.799999999999997,
        "reverse_margin": 4.799999999999997
      },
      "new": "005a9b18",
      "score": 65.6
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.68,
          0.68
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
        "margin": -4.799999999999997,
        "reverse_margin": -4.799999999999997
      },
      "new": "0059d4c8",
      "score": 60.8
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.68,
          0.68
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
        "margin": -4.799999999999997,
        "reverse_margin": -4.799999999999997
      },
      "new": "0059ecd4",
      "score": 60.8
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-62a5c21b359b32d6dd6fdd66f8c6980c"></a>

### v15.7.4 [`00587d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587d48.md) FUN_00587d48

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0059d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d52c.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -5.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0059ed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ed38.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -5.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`0059f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f6dc.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -5.0 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`005a0978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0978.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -5.0 · instruction_coverage, insufficient_independent_call_anchors
- 5. [`005ac408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac408.md) · スコア 22.5 · 採用条件未達 · 順位差 -35.0 / 5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a6988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md) · スコア 17.5 · 採用条件未達 · 順位差 -40.0 / -43.833333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) · スコア 16.8 · 採用条件未達 · 順位差 -40.7 / -48.8 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) · スコア 16.8 · 採用条件未達 · 順位差 -40.7 / -19.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "reverse_margin": -5.0
      },
      "new": "0059d52c",
      "score": 57.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "reverse_margin": -5.0
      },
      "new": "0059ed38",
      "score": 57.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "reverse_margin": -5.0
      },
      "new": "0059f6dc",
      "score": 57.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5efd04010c679737a052178c222e0061"></a>

### v15.7.4 [`00587da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587da8.md) FUN_00587da8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005ab1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md) · スコア 67.142857 · 採用条件未達 · 順位差 31.428571000000005 / 67.142857 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005ab268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md) · スコア 35.714286 · 採用条件未達 · 順位差 -31.428571000000005 / 35.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005ac4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md) · スコア 35.714286 · 採用条件未達 · 順位差 -31.428571000000005 / -28.730158000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) · スコア 23.571429 · 採用条件未達 · 順位差 -43.57142800000001 / 23.571429 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005a3e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md) · スコア 22.758621 · 採用条件未達 · 順位差 -44.384236 / 22.758621 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005ac468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md) · スコア 19.285714 · 採用条件未達 · 順位差 -47.85714300000001 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0087a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a510.md) · スコア 14.545455 · 採用条件未達 · 順位差 -52.597402 / -43.636363 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009fcb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcb68.md) · スコア 14.545455 · 採用条件未達 · 順位差 -52.597402 / -52.727272 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 31.428571000000005,
        "reverse_margin": 67.142857
      },
      "new": "005ab1f8",
      "score": 67.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42857142857142855,
          0.4444444444444444
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -31.428571000000005,
        "reverse_margin": 35.714286
      },
      "new": "005ab268",
      "score": 35.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42857142857142855,
          0.4444444444444444
        ],
        "cfg_coverage": [
          0.5454545454545454,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.428571000000005,
        "reverse_margin": -28.730158000000003
      },
      "new": "005ac4d8",
      "score": 35.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-650e28b235270094ccc6622786acb44d"></a>

### v15.7.4 [`00587e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587e18.md) FUN_00587e18

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005ab268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md) · スコア 64.444444 · 採用条件未達 · 順位差 0.0 / 64.444444 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005ac4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md) · スコア 64.444444 · 採用条件未達 · 順位差 0.0 / 28.547008000000005 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ab1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md) · スコア 35.714286 · 採用条件未達 · 順位差 -28.730158000000003 / 35.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007a06c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a06c8.md) · スコア 15.555556 · 採用条件未達 · 順位差 -48.88888800000001 / 15.555556 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005a3e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3e2c.md) · スコア 14.482759 · 採用条件未達 · 順位差 -49.961685 / 14.482759 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0087a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a510.md) · スコア 9.090909 · 採用条件未達 · 順位差 -55.35353500000001 / -49.090908999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009fcb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fc/009fcb68.md) · スコア 9.090909 · 採用条件未達 · 順位差 -55.35353500000001 / -58.18181800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005ac468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md) · スコア 4.285714 · 採用条件未達 · 順位差 -60.158730000000006 / -15.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7407407407407407,
          0.7407407407407407
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 64.444444
      },
      "new": "005ab268",
      "score": 64.444444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7407407407407407,
          0.7407407407407407
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
        "reverse_margin": 28.547008000000005
      },
      "new": "005ac4d8",
      "score": 64.444444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.42857142857142855
        ],
        "cfg_coverage": [
          0.5,
          0.5454545454545454
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -28.730158000000003,
        "reverse_margin": 35.714286
      },
      "new": "005ab1f8",
      "score": 35.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-45f298dcf8b5a821121b0d44072c74fc"></a>

### v15.7.4 [`00587e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587e84.md) FUN_00587e84

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`005a0a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a18.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005ac544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac544.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ac554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md) · スコア 25.0 · 採用条件未達 · 順位差 -40.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "005a0a18",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "005ac544",
      "score": 35.0
    },
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
        "margin": -40.0,
        "reverse_margin": -45.0
      },
      "new": "005ac554",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d23fdde89328fdf1a7be886a93855f56"></a>

### v15.7.4 [`00587e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587e94.md) FUN_00587e94

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a0a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a28.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ac554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`005ac544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac544.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005ac468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -19.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005ac4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -64.444444 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005ac584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "005a0a28",
      "score": 70.0
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
        "margin": -10.0,
        "reverse_margin": 0.0
      },
      "new": "0043bd58",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.0,
        "reverse_margin": -10.0
      },
      "new": "005ac554",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-41b44c26da30b969dc3dc5952ab781b5"></a>

### v15.7.4 [`00587ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587ec4.md) FUN_00587ec4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005ab314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab314.md) · スコア 67.142857 · 採用条件未達 · 順位差 27.142857000000006 / 67.142857 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`005ac584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md) · スコア 40.0 · 採用条件未達 · 順位差 -27.142857000000006 / -2.8571430000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0059ee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059ee94.md) · スコア 34.805195 · 採用条件未達 · 順位差 -32.33766200000001 / 34.805195 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059ccf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059ccf8.md) · スコア 22.922078 · 採用条件未達 · 順位差 -44.22077900000001 / 22.922078 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009e21f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e21f0.md) · スコア 21.428571 · 採用条件未達 · 順位差 -45.714286 / -9.875777 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a6988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6988.md) · スコア 21.103896 · 採用条件未達 · 順位差 -46.03896100000001 / -40.229437000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) · スコア 15.0 · 採用条件未達 · 順位差 -52.14285700000001 / 15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005ac4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md) · スコア 8.571429 · 採用条件未達 · 順位差 -58.571428000000004 / -55.873015 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 27.142857000000006,
        "reverse_margin": 67.142857
      },
      "new": "005ab314",
      "score": 67.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.6428571428571429
        ],
        "cfg_coverage": [
          0.09090909090909091,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.142857000000006,
        "reverse_margin": -2.8571430000000007
      },
      "new": "005ac584",
      "score": 40.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42857142857142855,
          0.5
        ],
        "cfg_coverage": [
          0.45454545454545453,
          0.625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -32.33766200000001,
        "reverse_margin": 34.805195
      },
      "new": "0059ee94",
      "score": 34.805195
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-52543544faba75a22f213e1c5351ac05"></a>

### v15.7.4 [`00587f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587f34.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005ac5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f4.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 77.4167 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`005ac554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 5. [`005ac584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md) · スコア 4.3888 · 採用条件未達 · 順位差 — / — · 
- 6. [`005ac638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac638.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005ac544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac544.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 
- 8. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 77.4167
      },
      "new": "005ac5f4",
      "score": 83.0
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
      "new": "005ac554",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f19fd61fa2eaf8f8531ce29046075d12"></a>

### v15.7.4 [`00587f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587f38.md) FUN_00587f38

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`005a0a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a7c.md) · スコア 65.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 35.0 · 採用条件未達 · 順位差 -30.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ac554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md) · スコア 25.0 · 採用条件未達 · 順位差 -40.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "005a0a7c",
      "score": 65.0
    },
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
        "margin": -30.0,
        "reverse_margin": 10.0
      },
      "new": "005ac5f8",
      "score": 35.0
    },
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
        "margin": -40.0,
        "reverse_margin": -45.0
      },
      "new": "005ac554",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0ce648c513c596cf9a5659254bdab94"></a>

### v15.7.4 [`00587f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587f48.md) FUN_00587f48

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005a0a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0a8c.md) · スコア 70.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 60.0 · 採用条件未達 · 順位差 -10.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 25.0 · 採用条件未達 · 順位差 -45.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) · スコア 20.0 · 採用条件未達 · 順位差 -50.0 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005ac584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": 10.0
      },
      "new": "005a0a8c",
      "score": 70.0
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
        "margin": -10.0,
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
        "margin": -45.0,
        "reverse_margin": -10.0
      },
      "new": "005ac5f8",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3db17559ef1ee9bdc715fd52a7e73412"></a>

### v15.7.4 [`00587f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587f78.md) FUN_00587f78

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005ac638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac638.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`005ac5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005ac63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac63c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "005ac638",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005ac5f4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005ac63c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-14b28888488c6ff063cc83514b08d6bf"></a>

### v15.7.4 [`00587f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587f7c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005ac63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac63c.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 77.4167 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`005ac638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac638.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) · スコア 3.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 77.4167
      },
      "new": "005ac63c",
      "score": 83.0
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
      "new": "005ac608",
      "score": 5.5833
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c62b1480e221993b18cf6fe8e134e6b0"></a>

### v15.7.4 [`00588344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588344.md) FUN_00588344

`competing_candidates` 

呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`00577b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577b80.md)

- 1. [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · スコア 12.093023 · 採用条件未達 · 順位差 3.7342950000000013 / 1.3590850000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · スコア 8.358728 · 採用条件未達 · 順位差 -3.7342950000000013 / -0.47572400000000137 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004e8960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md) · スコア 4.651163 · 採用条件未達 · 順位差 -7.44186 / 4.651163 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0063b784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md) · スコア 3.953488 · 採用条件未達 · 順位差 -8.139535 / 3.953488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00798020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md) · スコア 3.909491 · 採用条件未達 · 順位差 -8.183532 / 3.909491 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) · スコア 3.72093 · 採用条件未達 · 順位差 -8.372093 / 3.72093 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · スコア 3.568241 · 採用条件未達 · 順位差 -8.524782 / 3.568241 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) · スコア 2.912621 · 採用条件未達 · 順位差 -9.180402 / 2.912621 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16279069767441862,
          0.18502202643171806
        ],
        "cfg_coverage": [
          0.13513513513513514,
          0.11627906976744186
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.7342950000000013,
        "reverse_margin": 1.3590850000000003
      },
      "new": "00598d80",
      "score": 12.093023
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12015503875968993,
          0.14027149321266968
        ],
        "cfg_coverage": [
          0.06756756756756757,
          0.05747126436781609
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.7342950000000013,
        "reverse_margin": -0.47572400000000137
      },
      "new": "005aca04",
      "score": 8.358728
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07751937984496124,
          0.11049723756906077
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
        "margin": -7.44186,
        "reverse_margin": 4.651163
      },
      "new": "004e8960",
      "score": 4.651163
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.4 [`00588808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588808.md) FUN_00588808

`competing_candidates` 

呼出元 1件 [`00588344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588344.md) · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005991dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005991dc.md) · スコア 72.5 · 採用条件未達 · 順位差 14.318182 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00533ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md) · スコア 58.181818 · 採用条件未達 · 順位差 -14.318182 / 58.181818 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00534128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md) · スコア 58.181818 · 採用条件未達 · 順位差 -14.318182 / 58.181818 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005ace40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace40.md) · スコア 37.5 · 採用条件未達 · 順位差 -35.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00599610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md) · スコア 24.0 · 採用条件未達 · 順位差 -48.5 / 24.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005ad248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md) · スコア 24.0 · 採用条件未達 · 順位差 -48.5 / 24.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006355dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006355dc.md) · スコア 21.5 · 採用条件未達 · 順位差 -51.0 / 21.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00635be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635be4.md) · スコア 19.318182 · 採用条件未達 · 順位差 -53.181818 / 19.318182 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.875,
          0.875
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
        "margin": 14.318182,
        "reverse_margin": 0.0
      },
      "new": "005991dc",
      "score": 72.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.875,
          0.6363636363636364
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
        "margin": -14.318182,
        "reverse_margin": 58.181818
      },
      "new": "00533ffc",
      "score": 58.181818
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.875,
          0.6363636363636364
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
        "margin": -14.318182,
        "reverse_margin": 58.181818
      },
      "new": "00534128",
      "score": 58.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-025b9781c339b80db03feea4ff872df7"></a>

### v15.7.4 [`00588848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588848.md) FUN_00588848

`competing_candidates` 

呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0058a280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a280.md)

- 1. [`005ace80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md) · スコア 18.259031 · 採用条件未達 · 順位差 5.672027 / 4.376678 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) · スコア 12.587004 · 採用条件未達 · 順位差 -5.672027 / 2.290533 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) · スコア 9.622404 · 採用条件未達 · 順位差 -8.636627 / 9.622404 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007aacc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md) · スコア 7.439594 · 採用条件未達 · 順位差 -10.819437 / -7.560406 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) · スコア 6.220647 · 採用条件未達 · 順位差 -12.038384 / 6.220647 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0051a73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a73c.md) · スコア 5.814978 · 採用条件未達 · 順位差 -12.444053 / 5.814978 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · スコア 5.391866 · 採用条件未達 · 順位差 -12.867165 / -6.701157 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) · スコア 5.3785 · 採用条件未達 · 順位差 -12.880531000000001 / -3.455952000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2643171806167401,
          0.3076923076923077
        ],
        "cfg_coverage": [
          0.13636363636363635,
          0.12
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.672027,
        "reverse_margin": 4.376678
      },
      "new": "005ace80",
      "score": 18.259031
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18061674008810572,
          0.19902912621359223
        ],
        "cfg_coverage": [
          0.10606060606060606,
          0.0875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.672027,
        "reverse_margin": 2.290533
      },
      "new": "0059921c",
      "score": 12.587004
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13656387665198239,
          0.14553990610328638
        ],
        "cfg_coverage": [
          0.07575757575757576,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -8.636627,
        "reverse_margin": 9.622404
      },
      "new": "0045868c",
      "score": 9.622404
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c8014287fe49189fcd0d0a7be930f0a5"></a>

### v15.7.4 [`00588e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588e80.md) FUN_00588e80

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0057753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md)

- 1. [`005ad444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md) · スコア 29.142857 · 採用条件未達 · 順位差 8.061775999999998 / -1.6679540000000017 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005ad4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md) · スコア 21.081081 · 採用条件未達 · 順位差 -8.061775999999998 / 21.081081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0088b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md) · スコア 3.125 · 採用条件未達 · 順位差 -26.017857 / 3.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4857142857142857,
          0.4857142857142857
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
        "margin": 8.061775999999998,
        "reverse_margin": -1.6679540000000017
      },
      "new": "005ad444",
      "score": 29.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37142857142857144,
          0.35135135135135137
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
        "margin": -8.061775999999998,
        "reverse_margin": 21.081081
      },
      "new": "005ad4d0",
      "score": 21.081081
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.052083333333333336
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
        "margin": -26.017857,
        "reverse_margin": 3.125
      },
      "new": "0088b2d4",
      "score": 3.125
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8ea6f756220df022df07229758fcf78b"></a>

### v15.7.4 [`00589fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/00589fbc.md) FUN_00589fbc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005ae580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae580.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005ae580",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b23c158a64b6bdc83721a99124eea53a"></a>

### v15.7.4 [`00589fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/00589fd8.md) FUN_00589fd8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005ae59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae59c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005ae580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae580.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005ae59c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005ae580",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-40ac86649f643852f46cfee5021aa40f"></a>

### v15.7.4 [`0058b154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b154.md) FUN_0058b154

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0061eb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb3c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005af718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af718.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 25.714286
      },
      "new": "0061eb3c",
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
      "new": "005af718",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6f86b585ba58a423c54d3ed8d104a8b9"></a>

### v15.7.4 [`0058b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b170.md) FUN_0058b170

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005af734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af734.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005af718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af718.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005af734",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005af718",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c784e50ea2db3884be13108b4f5afdad"></a>

### v15.7.4 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) FUN_0058b674

`competing_candidates` 

呼出元 11件 [`0058b7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7b8.md) [`0058b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7d4.md) [`0058b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b8ec.md) [`0058ba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058ba50.md) [`0058bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bad0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008cfcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfcf0.md) [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) · スコア 15.955857 · 採用条件未達 · 順位差 9.599356 / 7.215619 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00729cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729cb4.md) · スコア 6.356501 · 採用条件未達 · 順位差 -9.599356 / -19.76721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md) · スコア 3.832061 · 採用条件未達 · 順位差 -12.123796 / -18.969844000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) · スコア 3.764706 · 採用条件未達 · 順位差 -12.191151 / -55.647059000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00689dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689dfc.md) · スコア 1.333333 · 採用条件未達 · 順位差 -14.622524 / -51.333333999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00689f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689f64.md) · スコア 0.952381 · 採用条件未達 · 順位差 -15.003476 / -68.442292 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -15.955857 / -8.780488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) · スコア 0.0 · 採用条件未達 · 順位差 -15.955857 / -5.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24691358024691357,
          0.21505376344086022
        ],
        "cfg_coverage": [
          0.06451612903225806,
          0.05263157894736842
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 9.599356,
        "reverse_margin": 7.215619
      },
      "new": "005afc38",
      "score": 15.955857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07407407407407407,
          0.061855670103092786
        ],
        "cfg_coverage": [
          0.03225806451612903,
          0.038461538461538464
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.599356,
        "reverse_margin": -19.76721
      },
      "new": "00729cb4",
      "score": 6.356501
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09876543209876543,
          0.030534351145038167
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
        "margin": -12.123796,
        "reverse_margin": -18.969844000000002
      },
      "new": "00b02304",
      "score": 3.832061
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-db99bd527a090090db2a87e60605a881"></a>

### v15.7.4 [`0058b7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7b8.md) FUN_0058b7b8

`competing_candidates` 

呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 1件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md)

- 1. [`005afdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdac.md) · スコア 62.857143 · 採用条件未達 · 順位差 62.857143 / 62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005b0024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0024.md) · スコア 0.0 · 採用条件未達 · 順位差 -62.857143 / -44.347826 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7142857142857143,
          0.7142857142857143
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
        "margin": 62.857143,
        "reverse_margin": 62.857143
      },
      "new": "005afdac",
      "score": 62.857143
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
        "margin": -62.857143,
        "reverse_margin": -44.347826
      },
      "new": "005b0024",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0242ebaa4329aca046b5949f1cc115ac"></a>

### v15.7.4 [`0058b7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b7d4.md) FUN_0058b7d4

`competing_candidates` 

呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 6件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`0063c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c560.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) [`008cfcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfcf0.md)

- 1. [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) · スコア 27.969309 · 採用条件未達 · 順位差 21.969309 / 23.028133 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005b0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0080.md) · スコア 6.0 · 採用条件未達 · 順位差 -21.969309 / -24.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005e7824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md) · スコア 4.285714 · 採用条件未達 · 順位差 -23.683595 / -36.077922 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005e4328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4328.md) · スコア 3.428571 · 採用条件未達 · 順位差 -24.540737999999997 / -35.142858000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006dc844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc844.md) · スコア 3.428571 · 採用条件未達 · 順位差 -24.540737999999997 / -44.071429 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md) · スコア 0.0 · 採用条件未達 · 順位差 -27.969309 / -15.955857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -27.969309 / -8.780488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) · スコア 0.0 · 採用条件未達 · 順位差 -27.969309 / -5.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.44285714285714284,
          0.36470588235294116
        ],
        "cfg_coverage": [
          0.4666666666666667,
          0.30434782608695654
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 21.969309,
        "reverse_margin": 23.028133
      },
      "new": "005afdc8",
      "score": 27.969309
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1,
          0.21875
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
        "margin": -21.969309,
        "reverse_margin": -24.0
      },
      "new": "005b0080",
      "score": 6.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07142857142857142,
          0.09090909090909091
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
        "margin": -23.683595,
        "reverse_margin": -36.077922
      },
      "new": "005e7824",
      "score": 4.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9d70304ec0155c82f8df9eb3a2dda0e5"></a>

### v15.7.4 [`0058b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b8ec.md) FUN_0058b8ec

`competing_candidates` 

呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 4件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md)

- 1. [`005aff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005aff1c.md) · スコア 29.090909 · 採用条件未達 · 順位差 18.181818 / 21.818182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aff9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00aff9ec.md) · スコア 10.909091 · 採用条件未達 · 順位差 -18.181818 / -23.157576000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00afff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md) · スコア 10.909091 · 採用条件未達 · 順位差 -18.181818 / -35.128645000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005b0024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0024.md) · スコア 7.272727 · 採用条件未達 · 順位差 -21.818182 / -37.075098999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ab9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md) · スコア 3.157895 · 採用条件未達 · 順位差 -25.933014 / -49.010526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00af3ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3ecc.md) · スコア 1.297297 · 採用条件未達 · 順位差 -27.793612 / -28.547298 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005e03e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e03e4.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.090909 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005e0c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0c80.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.090909 / -53.913043 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.48484848484848486,
          0.48484848484848486
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
        "margin": 18.181818,
        "reverse_margin": 21.818182
      },
      "new": "005aff1c",
      "score": 29.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18181818181818182,
          0.24
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
        "margin": -18.181818,
        "reverse_margin": -23.157576000000002
      },
      "new": "00aff9ec",
      "score": 10.909091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18181818181818182,
          0.22641509433962265
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
        "margin": -18.181818,
        "reverse_margin": -35.128645000000006
      },
      "new": "00afff54",
      "score": 10.909091
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-58b97b52db76536ce5e540b016cd0238"></a>

### v15.7.4 [`0058b9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b9f4.md) FUN_0058b9f4

`competing_candidates` 

呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 2件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md)

- 1. [`005b0024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0024.md) · スコア 44.347826 · 採用条件未達 · 順位差 37.075098999999994 / 11.222825999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005aff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005aff1c.md) · スコア 7.272727 · 採用条件未達 · 順位差 -37.075098999999994 / -21.818182 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aff9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00aff9ec.md) · スコア 4.8 · 採用条件未達 · 順位差 -39.547826 / -29.266667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00afff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00afff54.md) · スコア 4.528302 · 採用条件未達 · 順位差 -39.819524 / -41.509434 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ab9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md) · スコア 3.157895 · 採用条件未達 · 順位差 -41.189931 / -49.010526 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -44.347826 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) · スコア 0.0 · 採用条件未達 · 順位差 -44.347826 / -27.969309 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005b0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0080.md) · スコア 0.0 · 採用条件未達 · 順位差 -44.347826 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 37.075098999999994,
        "reverse_margin": 11.222825999999998
      },
      "new": "005b0024",
      "score": 44.347826
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34782608695652173,
          0.12121212121212122
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
        "margin": -37.075098999999994,
        "reverse_margin": -21.818182
      },
      "new": "005aff1c",
      "score": 7.272727
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17391304347826086,
          0.08
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
        "margin": -39.547826,
        "reverse_margin": -29.266667
      },
      "new": "00aff9ec",
      "score": 4.8
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-229fcdb0bb74150c307e48b63700e025"></a>

### v15.7.4 [`0058ba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058ba50.md) FUN_0058ba50

`competing_candidates` 

呼出元 1件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 4件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md)

- 1. [`006dc844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc844.md) · スコア 36.875 · 採用条件未達 · 順位差 3.75 / -10.625 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005b0024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0024.md) · スコア 33.125 · 採用条件未達 · 順位差 -3.75 / -11.222825999999998 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005b0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0080.md) · スコア 30.0 · 採用条件未達 · 順位差 -6.875 / 2.3636359999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006dc8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc8a4.md) · スコア 7.5 · 採用条件未達 · 順位差 -29.375 / 7.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005afdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afdc8.md) · スコア 4.941176 · 採用条件未達 · 順位差 -31.933824 / -23.028133 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005e7824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7824.md) · スコア 4.363636 · 採用条件未達 · 順位差 -32.511364 / -36.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) · スコア 4.0 · 採用条件未達 · 順位差 -32.875 / 4.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) · スコア 3.495146 · 採用条件未達 · 順位差 -33.379854 / -28.435814 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28125,
          0.375
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
        "margin": 3.75,
        "reverse_margin": -10.625
      },
      "new": "006dc844",
      "score": 36.875
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21875,
          0.30434782608695654
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
        "reverse_margin": -11.222825999999998
      },
      "new": "005b0024",
      "score": 33.125
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
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
        "margin": -6.875,
        "reverse_margin": 2.3636359999999996
      },
      "new": "005b0080",
      "score": 30.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cf9044d9ac99c1702ca5da80c86d4e89"></a>

### v15.7.4 [`0058bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bad0.md) FUN_0058bad0

`competing_candidates` 

呼出元 1件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) · 呼出先 8件 [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md) [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`005c022c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c022c.md) [`007cd100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd100.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`005b0100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0100.md) · スコア 22.781955 · 採用条件未達 · 順位差 19.849624 / 20.075188 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b06230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06230.md) · スコア 2.932331 · 採用条件未達 · 順位差 -19.849624 / -25.167441999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005e2bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2bb8.md) · スコア 1.804511 · 採用条件未達 · 順位差 -20.977444 / -14.042847 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00738590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738590.md) · スコア 1.804511 · 採用条件未達 · 順位差 -20.977444 / 1.804511 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009be144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be144.md) · スコア 1.804511 · 採用条件未達 · 順位差 -20.977444 / 1.804511 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) · スコア 1.12782 · 採用条件未達 · 順位差 -21.654135 / -30.80314 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005f950c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f950c.md) · スコア 1.12782 · 採用条件未達 · 順位差 -21.654135 / -58.75982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005b0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0528.md) · スコア 0.902256 · 採用条件未達 · 順位差 -21.879699 / -34.153923999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37969924812030076,
          0.37969924812030076
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
        "margin": 19.849624,
        "reverse_margin": 20.075188
      },
      "new": "005b0100",
      "score": 22.781955
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04887218045112782,
          0.1326530612244898
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
        "margin": -19.849624,
        "reverse_margin": -25.167441999999998
      },
      "new": "00b06230",
      "score": 2.932331
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03007518796992481,
          0.0547945205479452
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
        "margin": -20.977444,
        "reverse_margin": -14.042847
      },
      "new": "005e2bb8",
      "score": 1.804511
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dc53f8792159a3cafd0d4c74707eecbe"></a>

### v15.7.4 [`0058bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058bef8.md) FUN_0058bef8

`competing_candidates` 

呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 4件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088f9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088f9e4.md) [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md)

- 1. [`005b0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0528.md) · スコア 35.05618 · 採用条件未達 · 順位差 26.292135 / 25.617977999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0049d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d3b8.md) · スコア 8.764045 · 採用条件未達 · 順位差 -26.292135 / 8.764045 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009e20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e20b8.md) · スコア 8.764045 · 採用条件未達 · 順位差 -26.292135 / -2.005186 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) · スコア 7.647059 · 採用条件未達 · 順位差 -27.409121 / -1.176470000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009e0fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0fbc.md) · スコア 4.044944 · 採用条件未達 · 順位差 -31.011235999999997 / -2.3672699999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0069e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e8d0.md) · スコア 3.71134 · 採用条件未達 · 順位差 -31.344839999999998 / 3.71134 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00726f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f54.md) · スコア 3.130435 · 採用条件未達 · 順位差 -31.925745 / 3.130435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00af5084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5084.md) · スコア 2.696629 · 採用条件未達 · 順位差 -32.359550999999996 / -62.303371 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5842696629213483,
          0.5842696629213483
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
        "margin": 26.292135,
        "reverse_margin": 25.617977999999997
      },
      "new": "005b0528",
      "score": 35.05618
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14606741573033707,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -26.292135,
        "reverse_margin": 8.764045
      },
      "new": "0049d3b8",
      "score": 8.764045
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14606741573033707,
          0.16666666666666666
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
        "margin": -26.292135,
        "reverse_margin": -2.005186
      },
      "new": "009e20b8",
      "score": 8.764045
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-65390f8c1d755216eb7007850a4d903a"></a>

### v15.7.4 [`0058c05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c05c.md) FUN_0058c05c

`competing_candidates` 

呼出元 4件 [`005d18a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d18a4.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 11件 [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)

- 1. [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) · スコア 31.597222 · 採用条件未達 · 順位差 25.347222 / 25.189455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) · スコア 6.25 · 採用条件未達 · 順位差 -25.347222 / 6.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a4277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a4277c.md) · スコア 5.625 · 採用条件未達 · 順位差 -25.972222 / 5.625 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00aff078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00aff078.md) · スコア 4.848485 · 採用条件未達 · 順位差 -26.748737 / -41.212120999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00728990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728990.md) · スコア 3.495146 · 採用条件未達 · 順位差 -28.102075999999997 / -25.118446 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00806188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806188.md) · スコア 3.125 · 採用条件未達 · 順位差 -28.472222 / -49.238636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00806264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806264.md) · スコア 3.125 · 採用条件未達 · 順位差 -28.472222 / -48.127525 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00806340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806340.md) · スコア 3.125 · 採用条件未達 · 順位差 -28.472222 / -49.826872 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4895833333333333,
          0.4895833333333333
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.11764705882352941
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.347222,
        "reverse_margin": 25.189455
      },
      "new": "005b068c",
      "score": 31.597222
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10416666666666667,
          0.11764705882352941
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
        "margin": -25.347222,
        "reverse_margin": 6.25
      },
      "new": "005d0610",
      "score": 6.25
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09375,
          0.11842105263157894
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
        "margin": -25.972222,
        "reverse_margin": 5.625
      },
      "new": "00a4277c",
      "score": 5.625
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3244590c00e6f0a53463ced6e6c7d027"></a>

### v15.7.4 [`00590b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590b64.md) FUN_00590b64

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`005b5194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5194.md) · スコア 35.0 · 採用条件未達 · 順位差 10.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005b51a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51a4.md) · スコア 25.0 · 採用条件未達 · 順位差 -10.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.0,
        "reverse_margin": -30.0
      },
      "new": "005b5194",
      "score": 35.0
    },
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
        "reverse_margin": -45.0
      },
      "new": "005b51a4",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-479f3cee23d78e4311510ef940afc947"></a>

### v15.7.4 [`00590b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590b74.md) FUN_00590b74

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 20.0 · 採用条件未達 · 順位差 0.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005b51a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51a4.md) · スコア 20.0 · 採用条件未達 · 順位差 0.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005b5194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5194.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": -40.0
      },
      "new": "0043bd58",
      "score": 20.0
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
        "margin": 0.0,
        "reverse_margin": -50.0
      },
      "new": "005b51a4",
      "score": 20.0
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
        "margin": -20.0,
        "reverse_margin": -65.0
      },
      "new": "005b5194",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b18ffc117804d0f7a7d158dfd80ee047"></a>

### v15.7.4 [`00590cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590cec.md) FUN_00590cec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b531c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b531c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005b531c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4a7c4f526336ad433b0f80cf0935a702"></a>

### v15.7.4 [`00590d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d08.md) FUN_00590d08

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5338.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b531c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b531c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5338",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b531c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9813166df7bb496fb0f3d4cf506cc273"></a>

### v15.7.4 [`00590d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d9c.md) FUN_00590d9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a9ae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9ae84.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005b53cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b53cc.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00a9ae84",
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
      "new": "005b53cc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-98ac031ef7202f497471e00428d442ae"></a>

### v15.7.4 [`00590db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590db8.md) FUN_00590db8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b53e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b53e8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b53cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b53cc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b53e8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b53cc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2f5d13f6a3baed9dc3912e454fac2781"></a>

### v15.7.4 [`00590f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f38.md) FUN_00590f38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5568.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -60.0
      },
      "new": "005b5568",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e142e590505f092b9879b16541ed3ddf"></a>

### v15.7.4 [`00590f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f54.md) FUN_00590f54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5584.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5568.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5584",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5568",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-023ff769665f34b39a8840f325ab262d"></a>

### v15.7.4 [`00590fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590fec.md) FUN_00590fec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b561c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b561c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e0ab0e627c6e06281defb852ac5a931b"></a>

### v15.7.4 [`00591008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591008.md) FUN_00591008

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5638.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b561c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5644.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5638",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b561c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5644",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d316182661551be871b10e96e9ed3bed"></a>

### v15.7.4 [`00591014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591014.md) FUN_00591014

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5644.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b5638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5638.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b561c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5644",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5638",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b561c",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e5571be585af6e34ef34b09fa935e118"></a>

### v15.7.4 [`00591074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591074.md) FUN_00591074

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b56a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b56a4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cf3354318c4d36820843c6bfef868854"></a>

### v15.7.4 [`00591090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591090.md) FUN_00591090

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b56c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56c0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b56a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b56c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b56a4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a937b41e364db6a8b8f5714eac06977"></a>

### v15.7.4 [`00591128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591128.md) FUN_00591128

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5758.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005b5758",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9322c3d7f918ec615c4589bb184c2028"></a>

### v15.7.4 [`00591144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591144.md) FUN_00591144

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5774.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5758.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5774",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5758",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2c2d59b41a3df7d6b0fb30808c159d52"></a>

### v15.7.4 [`0059134c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059134c.md) FUN_0059134c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b597c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005b597c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-69d630eeac0fda176591b82b5a9bcceb"></a>

### v15.7.4 [`00591368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591368.md) FUN_00591368

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5998.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b597c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5998",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b597c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e0e1db26a9987a376d919d557ff99075"></a>

### v15.7.4 [`005913c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005913c4.md) FUN_005913c4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

- 1. [`005b59f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59f4.md) · スコア 35.0 · 採用条件未達 · 順位差 35.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005b5a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a04.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 35.0,
        "reverse_margin": 35.0
      },
      "new": "005b59f4",
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
        "reverse_margin": -50.0
      },
      "new": "005b5a04",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56098323479b64b64ea2b7e00f2e28a5"></a>

### v15.7.4 [`005913d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005913d4.md) FUN_005913d4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`005b5a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a04.md) · スコア 50.0 · 採用条件未達 · 順位差 30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 20.0 · 採用条件未達 · 順位差 -30.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005b59f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -50.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.0,
        "reverse_margin": 50.0
      },
      "new": "005b5a04",
      "score": 50.0
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
        "margin": -30.0,
        "reverse_margin": -40.0
      },
      "new": "0043bd58",
      "score": 20.0
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
        "reverse_margin": -35.0
      },
      "new": "005b59f4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd385f0f90c7edcdb21cc2e6f4cadd2b"></a>

### v15.7.4 [`005914b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005914b4.md) FUN_005914b4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ae4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b5ae4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2966f11af6ea844d0f6645c37cc03001"></a>

### v15.7.4 [`005914d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005914d0.md) FUN_005914d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b00.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ae4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b0c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5b00",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5ae4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5b0c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5e24df06bb9858c1b74ef4ea8317f48b"></a>

### v15.7.4 [`005914dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005914dc.md) FUN_005914dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b0c.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b5b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b00.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ae4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5b0c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5b00",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5ae4",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5aff1a330f34ed5a583c18375f5a4eaa"></a>

### v15.7.4 [`00591560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591560.md) FUN_00591560

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b90.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b5b90",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-35438e492ced8ccf33bfe889c52dd637"></a>

### v15.7.4 [`0059157c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059157c.md) FUN_0059157c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5bac.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b90.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5bac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5b90",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1b310c285466f3baf33128b0364d4cf2"></a>

### v15.7.4 [`005915f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005915f4.md) FUN_005915f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b0cf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf14.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005b5c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c24.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 25.714286
      },
      "new": "00b0cf14",
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
      "new": "005b5c24",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7b714ee3449d13145ef5e161e10f34d7"></a>

### v15.7.4 [`00591610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591610.md) FUN_00591610

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c40.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c24.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5c40",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5c24",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8bb51f10450ccce0739d23cd2a05754f"></a>

### v15.7.4 [`0059171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059171c.md) FUN_0059171c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 20.0
      },
      "new": "005b5d4c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d8abe3e13a4c7f18bfc9be6a8ddab691"></a>

### v15.7.4 [`00591738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591738.md) FUN_00591738

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d68.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d4c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5d68",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5d4c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b4451ac9e6e0efac52de327d93fcb41b"></a>

### v15.7.4 [`005917b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917b0.md) FUN_005917b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5de0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005b5de0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-89abb84e2ef906fdfcb604c2f5eedd68"></a>

### v15.7.4 [`005917cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917cc.md) FUN_005917cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dfc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5de0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e08.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5dfc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5de0",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5e08",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1dbb9e0a4b45c1b569fb75f5b56c0de8"></a>

### v15.7.4 [`005917d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917d8.md) FUN_005917d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e08.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b5dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dfc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5de0.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5e08",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5dfc",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5de0",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-911439509b46a1dd25d9c3560e48f015"></a>

### v15.7.4 [`00591904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591904.md) FUN_00591904

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f34.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b5f34",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-34b6b15aaef01d26aa5d71df52cd4b3f"></a>

### v15.7.4 [`00591920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591920.md) FUN_00591920

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f50.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b5f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f34.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f5c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5f50",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5f34",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5f5c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f2ca2ee096cc5fc93ec71e3c656e982e"></a>

### v15.7.4 [`0059192c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059192c.md) FUN_0059192c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f5c.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b5f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f50.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b5f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f34.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b5f5c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5f50",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b5f34",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d9ee968a78a8905726bd4e09d7588962"></a>

### v15.7.4 [`00591a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a70.md) FUN_00591a70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b60a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60a0.md) · スコア 71.428571 · 採用条件未達 · 順位差 71.428571 / 71.428571 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "005b60a0",
      "score": 71.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ac45a26165e4e59ea74e6406c4dd71ef"></a>

### v15.7.4 [`00591a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a8c.md) FUN_00591a8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b60bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60bc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b60a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60a0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b60bc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b60a0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6a3991cff56495ad174cf51e79388ad0"></a>

### v15.7.4 [`00591b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b04.md) FUN_00591b04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6134.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005b6134",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-75cd5fc6c7589e8862dcd4fe0567b64b"></a>

### v15.7.4 [`00591b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b20.md) FUN_00591b20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6150.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`005b6134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6134.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b615c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b615c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b6150",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b6134",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b615c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-47d765d071ee0dce9a5540c77e046db1"></a>

### v15.7.4 [`00591b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b2c.md) FUN_00591b2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b615c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b615c.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6150.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`005b6134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6134.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b615c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b6150",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b6134",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

