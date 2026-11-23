# v15.7.4 → v16.0.0 · 追加調査 (59)

[一覧の目次](README.md)

### v15.7.4 [`007ff598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff598.md) FUN_007ff598

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008310a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310a0.md) · スコア 69.411765 · 採用条件未達 · 順位差 27.840336 / 2.268907999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) · スコア 41.571429 · 採用条件未達 · 順位差 -27.840336 / -27.993788000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0083102c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/0083102c.md) · スコア 24.137931 · 採用条件未達 · 順位差 -45.27383400000001 / -32.586207 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 3.157895 · 採用条件未達 · 順位差 -66.25387 / -67.368421 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00830fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830fa4.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.411765 / -73.793103 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00831174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831174.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.411765 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8235294117647058,
          1.0
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
        "margin": 27.840336,
        "reverse_margin": 2.268907999999996
      },
      "new": "008310a0",
      "score": 69.411765
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6470588235294118,
          0.55
        ],
        "cfg_coverage": [
          0.5,
          0.42857142857142855
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.840336,
        "reverse_margin": -27.993788000000002
      },
      "new": "008310d8",
      "score": 41.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11764705882352941,
          0.06896551724137931
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
        "margin": -45.27383400000001,
        "reverse_margin": -32.586207
      },
      "new": "0083102c",
      "score": 24.137931
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9150e8f4d50c8b7b05a2ddd7b2efedca"></a>

### v15.7.4 [`007ff5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff5dc.md) FUN_007ff5dc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) · スコア 69.565217 · 採用条件未達 · 順位差 48.447205000000004 / 27.993788000000002 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008310a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310a0.md) · スコア 21.118012 · 採用条件未達 · 順位差 -48.447205000000004 / -48.293753 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.565217 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0083102c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/0083102c.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.565217 / -56.724138 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.565217 / -70.526316 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00831174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831174.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.565217 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8260869565217391,
          0.95
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
        "margin": 48.447205000000004,
        "reverse_margin": 27.993788000000002
      },
      "new": "008310d8",
      "score": 69.565217
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30434782608695654,
          0.5
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -48.447205000000004,
        "reverse_margin": -48.293753
      },
      "new": "008310a0",
      "score": 21.118012
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
        "margin": -69.565217,
        "reverse_margin": -60.0
      },
      "new": "0043bd58",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-365615fed251723eb391fd4ab1f576c4"></a>

### v15.7.4 [`007ff638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff638.md) FUN_007ff638

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`008310a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310a0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -69.565217 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -70.526316 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -69.411765
      },
      "new": "008310a0",
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
        "reverse_margin": -69.565217
      },
      "new": "008310d8",
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
        "reverse_margin": -70.526316
      },
      "new": "00831128",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7f4f47d22f9b7bbe7e315241fd3d5bbf"></a>

### v15.7.4 [`007ff6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff6c0.md) FUN_007ff6c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b7f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7f58.md) · スコア 73.793103 · 採用条件未達 · 順位差 21.471264000000005 / 73.793103 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0074a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a490.md) · スコア 52.321839 · 採用条件未達 · 順位差 -21.471264000000005 / 52.321839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008310a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.793103 / -69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.793103 / -69.565217 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.793103 / -70.526316 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.793103 / -66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.896551724137931,
          0.896551724137931
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 21.471264000000005,
        "reverse_margin": 73.793103
      },
      "new": "005b7f58",
      "score": 73.793103
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8275862068965517,
          0.8275862068965517
        ],
        "cfg_coverage": [
          0.2857142857142857,
          0.13333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -21.471264000000005,
        "reverse_margin": 52.321839
      },
      "new": "0074a490",
      "score": 52.321839
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
        "margin": -73.793103,
        "reverse_margin": -69.411765
      },
      "new": "008310a0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dbb2508dd49dbe6e2627ebe06ee70bda"></a>

### v15.7.4 [`007ff734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff734.md) FUN_007ff734

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008310d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008310d8.md) · スコア 35.857143 · 採用条件未達 · 順位差 32.699248 / -33.708074 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 3.157895 · 採用条件未達 · 順位差 -32.699248 / -67.368421 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00831174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831174.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.857143 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.857143 / -66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.857143 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.55
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 32.699248,
        "reverse_margin": -33.708074
      },
      "new": "008310d8",
      "score": 35.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07142857142857142,
          0.05263157894736842
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
        "margin": -32.699248,
        "reverse_margin": -67.368421
      },
      "new": "00831128",
      "score": 3.157895
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
        "margin": -35.857143,
        "reverse_margin": -80.0
      },
      "new": "00831174",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a9229395b17201135c3070124d2e12a4"></a>

### v15.7.4 [`007ff76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff76c.md) FUN_007ff76c

`competing_candidates` 

呼出元 1件 [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00560e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md) · スコア 74.0 · 採用条件未達 · 順位差 3.666667000000004 / 74.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`009b7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7f94.md) · スコア 70.333333 · 採用条件未達 · 順位差 -3.666667000000004 / 70.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0079f838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f838.md) · スコア 51.014493 · 採用条件未達 · 順位差 -22.985507 / 51.014493 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.0 / -70.526316 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00831174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831174.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.0 / -66.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 3.666667000000004,
        "reverse_margin": 74.0
      },
      "new": "00560e08",
      "score": 74.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.95,
          0.95
        ],
        "cfg_coverage": [
          0.6666666666666666,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.666667000000004,
        "reverse_margin": 70.333333
      },
      "new": "009b7f94",
      "score": 70.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.85,
          0.7391304347826086
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.375
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
        "margin": -22.985507,
        "reverse_margin": 51.014493
      },
      "new": "0079f838",
      "score": 51.014493
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-53049cde66e57d44cdb7f81586090dc0"></a>

### v15.7.4 [`007ff7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff7bc.md) FUN_007ff7bc

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`00af1c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c5c.md) · スコア 27.929825 · 採用条件未達 · 順位差 4.335622000000001 / -14.570174999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009a3734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3734.md) · スコア 23.594203 · 採用条件未達 · 順位差 -4.335622000000001 / 10.550725 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006942a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/006942a0.md) · スコア 20.280702 · 採用条件未達 · 順位差 -7.6491229999999995 / 20.280702 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008a500c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a500c.md) · スコア 18.45614 · 採用条件未達 · 順位差 -9.473685 / 18.45614 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008ad6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6b0.md) · スコア 18.45614 · 採用条件未達 · 順位差 -9.473685 / 18.45614 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a3e5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e5b8.md) · スコア 18.0 · 採用条件未達 · 順位差 -9.929825000000001 / 18.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00831128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831128.md) · スコア 17.122807 · 採用条件未達 · 順位差 -10.807018 / -53.40350899999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009217e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009217e0.md) · スコア 17.122807 · 採用条件未達 · 順位差 -10.807018 / 17.122807 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42105263157894735,
          0.5
        ],
        "cfg_coverage": [
          0.13333333333333333,
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
        "margin": 4.335622000000001,
        "reverse_margin": -14.570174999999999
      },
      "new": "00af1c5c",
      "score": 27.929825
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3684210526315789,
          0.30434782608695654
        ],
        "cfg_coverage": [
          0.26666666666666666,
          0.2857142857142857
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.335622000000001,
        "reverse_margin": 10.550725
      },
      "new": "009a3734",
      "score": 23.594203
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3157894736842105,
          0.375
        ],
        "cfg_coverage": [
          0.06666666666666667,
          0.16666666666666666
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
        "margin": -7.6491229999999995,
        "reverse_margin": 20.280702
      },
      "new": "006942a0",
      "score": 20.280702
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fef7913336920de043200bcdfe23c840"></a>

### v15.7.4 [`007ff808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff808.md) FUN_007ff808

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831174.md) · スコア 54.285714 · 採用条件未達 · 順位差 17.142857 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 37.142857 · 採用条件未達 · 順位差 -17.142857 / -42.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -25.714286
      },
      "new": "00831174",
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
        "reverse_margin": -42.857143
      },
      "new": "008311d4",
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
        "reverse_margin": -41.538461
      },
      "new": "008311a0",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7c74b1ef34d444486f6ed14d29fa0860"></a>

### v15.7.4 [`007ff824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff824.md) FUN_007ff824

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831190.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 67.2857 · 
- 2. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`0083119c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/0083119c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`008311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311e8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008311ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311ec.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831190",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008311d4",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0083119c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4d6e1f7056352028b4e0940f6b502ae0"></a>

### v15.7.4 [`007ff830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff830.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0083119c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/0083119c.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 68.2175 · 
- 2. [`008311ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311ec.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`008311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311e8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 7. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 68.2175
      },
      "new": "0083119c",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008311ec",
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

<a id="review-0a4339b1567847db3f2e55200eb90fd7"></a>

### v15.7.4 [`007ff834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff834.md) FUN_007ff834

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 66.153846 · 採用条件未達 · 順位差 10.769231000000005 / 15.384615000000004 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00a7bc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc84.md) · スコア 55.384615 · 採用条件未達 · 順位差 -10.769231000000005 / 55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -12.527472 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 10.769231000000005,
        "reverse_margin": 15.384615000000004
      },
      "new": "008311a0",
      "score": 66.153846
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
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
        "margin": -10.769231000000005,
        "reverse_margin": 55.384615
      },
      "new": "00a7bc84",
      "score": 55.384615
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
        "reverse_margin": -55.384615
      },
      "new": "008311d4",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6dacb8640d9a17d1a227c6c170b10505"></a>

### v15.7.4 [`007ff868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff868.md) FUN_007ff868

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 56.0 · 採用条件未達 · 順位差 18.857143 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 37.142857 · 採用条件未達 · 順位差 -18.857143 / 12.527472 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008311a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311a0.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / -41.538461 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -24.0
      },
      "new": "008311d4",
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
        "reverse_margin": 12.527472
      },
      "new": "00831238",
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
        "reverse_margin": -41.538461
      },
      "new": "008311a0",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4f335c4b17cd5488f5e873eb616d3477"></a>

### v15.7.4 [`007ff87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff87c.md) FUN_007ff87c

`competing_candidates` 

呼出元 1件 [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) · 呼出先 0件 

- 1. [`008311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311e8.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`008311ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311ec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00831260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831260.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00831254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831254.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008311d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311d4.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 6. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 7. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.2222 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008311e8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008311ec",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831260",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-29a08573daaf2b841f3855da70226fac"></a>

### v15.7.4 [`007ff880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff880.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008311ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311ec.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`00831260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831260.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`008311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311e8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00831254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831254.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.7222 · 採用条件未達 · 順位差 — / — · 
- 7. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008311ec",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831260",
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

<a id="review-8875726ac4a4fbd4a7286ec6ea4c2aa1"></a>

### v15.7.4 [`007ff884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff884.md) FUN_007ff884

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

- 1. [`008ad6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6b0.md) · スコア 43.333333 · 採用条件未達 · 順位差 3.333333000000003 / 43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008a500c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a500c.md) · スコア 40.0 · 採用条件未達 · 順位差 -3.333333000000003 / 40.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / -46.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / -46.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00672d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d88.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / -46.666667000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0086d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d574.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009a3968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3968.md) · スコア 23.333333 · 採用条件未達 · 順位差 -20.000000000000004 / 23.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.7142857142857143,
          0.5
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
        "margin": 3.333333000000003,
        "reverse_margin": 43.333333
      },
      "new": "008ad6b0",
      "score": 43.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
        "margin": -3.333333000000003,
        "reverse_margin": 40.0
      },
      "new": "008a500c",
      "score": 40.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3888888888888889,
          0.3888888888888889
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
        "margin": -20.000000000000004,
        "reverse_margin": -46.666667000000004
      },
      "new": "005db034",
      "score": 23.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5c49f5befaa5f295661e3ea4cb0975fe"></a>

### v15.7.4 [`007ff8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff8cc.md) FUN_007ff8cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -37.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -24.615385 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -70.0
      },
      "new": "008311f0",
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
        "reverse_margin": -37.142857
      },
      "new": "00831238",
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
      "new": "00831264",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3c1b469cca4f7c802163ddf2ce9062db"></a>

### v15.7.4 [`007ff8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff8e8.md) FUN_007ff8e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831254.md) · スコア 69.0 · 採用条件未達 · 順位差 66.6 / 66.6 · 
- 2. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00831260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831260.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`008312ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312ac.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`008311f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008311f0.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.6,
        "reverse_margin": 66.6
      },
      "new": "00831254",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831298",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831238",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1eb3fae15df29e927aceb5184aed3c22"></a>

### v15.7.4 [`007ff8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff8f4.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00831260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831260.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`008312b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b0.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 4. [`008312ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00831254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831254.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00831238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831238.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831260",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008312b0",
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

<a id="review-e9daf9b59bc6501c0c235040821b72fb"></a>

### v15.7.4 [`007ff8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff8f8.md) FUN_007ff8f8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 23.076923 · 採用条件未達 · 順位差 3.0769230000000007 / -1.538461999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 20.0 · 採用条件未達 · 順位差 -3.0769230000000007 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 3.0769230000000007,
        "reverse_margin": -1.538461999999999
      },
      "new": "00831264",
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
        "margin": -3.0769230000000007,
        "reverse_margin": 20.0
      },
      "new": "00831298",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0ef4a2d70b4600161e02b8dc7b6dcd05"></a>

### v15.7.4 [`007ff92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff92c.md) FUN_007ff92c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 24.615385 · 採用条件未達 · 順位差 24.615385 / 1.538461999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.615385 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "margin": 24.615385,
        "reverse_margin": 1.538461999999999
      },
      "new": "00831264",
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
        "reverse_margin": -20.0
      },
      "new": "00831298",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-36e03ed1f3d2b9225b3e1131200e8381"></a>

### v15.7.4 [`007ff940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff940.md) FUN_007ff940

`competing_candidates` 

呼出元 1件 [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) · 呼出先 0件 

- 1. [`008312ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312ac.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`00831260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831260.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`008312b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008312ac",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831260",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008312b0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-68a39244aca9e396e27fe0a1b8e58190"></a>

### v15.7.4 [`007ff944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff944.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008312b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b0.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 0.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`008312ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00831298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831298.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 5. [`00831264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831264.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008312b0",
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
      "new": "008312ac",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-750e4740d2cfecbd4fbbe136818a4d83"></a>

### v15.7.4 [`007ffcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffcf4.md) FUN_007ffcf4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831660.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831660",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-050e5ac0b08437efc23a09cf08f1fe3e"></a>

### v15.7.4 [`007ffd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffd10.md) FUN_007ffd10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0083167c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/0083167c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831660.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0083167c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831660",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-740645609cc620179b4480b6f40c2228"></a>

### v15.7.4 [`007ffdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffdb8.md) FUN_007ffdb8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831724.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00831724",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6f748b9776e5758d35348cfa72b684cb"></a>

### v15.7.4 [`007ffdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffdd4.md) FUN_007ffdd4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831740.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831724.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831740",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831724",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2acc8f8ede6e68a21838e90fc839ed80"></a>

### v15.7.4 [`007ffe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe2c.md) FUN_007ffe2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831798.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831798",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7a1846b93960c5460900c6fad97fbc90"></a>

### v15.7.4 [`007ffe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe40.md) FUN_007ffe40

`competing_candidates` 

呼出元 1件 [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) · 呼出先 0件 

- 1. [`008317ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317ac.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`00831798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831798.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008317ac",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831798",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2967952b6a6c23a47fccb854decd6adf"></a>

### v15.7.4 [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) FUN_007ffe48

`competing_candidates` 

呼出元 0件  · 呼出先 9件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`007f19a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f19a4.md) [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md)

- 1. [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · スコア 46.341565 · 採用条件未達 · 順位差 23.021374 / 22.588329 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0082a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082a760.md) · スコア 23.320191 · 採用条件未達 · 順位差 -23.021374 / -27.20283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00827680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/00827680.md) · スコア 22.992322 · 採用条件未達 · 順位差 -23.349243 / -13.223894000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008274b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008274b4.md) · スコア 11.458809 · 採用条件未達 · 順位差 -34.882756 / -56.454234 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) · スコア 6.183856 · 採用条件未達 · 順位差 -40.157709000000004 / -54.408304 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f2a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md) · スコア 4.843328 · 採用条件未達 · 順位差 -41.498237 / -40.267009 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0089398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md) · スコア 4.843328 · 採用条件未達 · 順位差 -41.498237 / -35.788569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) · スコア 4.262295 · 採用条件未達 · 順位差 -42.07927 / 4.262295 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6120218579234973,
          0.6120218579234973
        ],
        "cfg_coverage": [
          0.4810126582278481,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 23.021374,
        "reverse_margin": 22.588329
      },
      "new": "008317b4",
      "score": 46.341565
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.31693989071038253,
          0.31868131868131866
        ],
        "cfg_coverage": [
          0.21518987341772153,
          0.21518987341772153
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.021374,
        "reverse_margin": -27.20283
      },
      "new": "0082a760",
      "score": 23.320191
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3114754098360656,
          0.38
        ],
        "cfg_coverage": [
          0.21518987341772153,
          0.22972972972972974
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.349243,
        "reverse_margin": -13.223894000000001
      },
      "new": "00827680",
      "score": 22.992322
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-133a0ca333d0889b75771ab847a6fa41"></a>

### v15.7.4 [`00800124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800124.md) FUN_00800124

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831a90.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00831a90",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3d3a26f7f9edb52929bc3ebd389a25ff"></a>

### v15.7.4 [`00800140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800140.md) FUN_00800140

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831aac.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831a90.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · スコア 0.0656 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831aac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831a90",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008317b4",
      "score": 0.0656
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bd8597bd9588bd18995e4c5279433598"></a>

### v15.7.4 [`008004bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008004bc.md) FUN_008004bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831e28.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831e28",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7643f945b611cdec9ee1db7f5a7c4aa"></a>

### v15.7.4 [`008004d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008004d8.md) FUN_008004d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831e44.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831e28.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831e44",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831e28",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-28e01717ec198c16065c2ed7e5239ea3"></a>

### v15.7.4 [`008005cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008005cc.md) FUN_008005cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831f38.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831f38",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c1edd4dadc17fbf854539a31ae3940ee"></a>

### v15.7.4 [`008005e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008005e8.md) FUN_008005e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831f54.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831f38.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831f54",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831f38",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a0a16f66b1f2edda6b8b2125232f3033"></a>

### v15.7.4 [`00800648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800648.md) FUN_00800648

`competing_candidates` 

呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`007f7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7e3c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00831fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831fb4.md) · スコア 65.6 · 採用条件未達 · 順位差 4.885713999999993 / 55.99999999999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00630db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630db4.md) · スコア 60.714286 · 採用条件未達 · 順位差 -4.885713999999993 / 0.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005dc0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc0a0.md) · スコア 55.625 · 採用条件未達 · 順位差 -9.974999999999994 / -1.875 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00656c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c70.md) · スコア 55.625 · 採用条件未達 · 順位差 -9.974999999999994 / -1.875 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e2b0.md) · スコア 55.625 · 採用条件未達 · 順位差 -9.974999999999994 / -3.75 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f3574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3574.md) · スコア 54.0 · 採用条件未達 · 順位差 -11.599999999999994 / -10.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007ff924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff924.md) · スコア 36.0 · 採用条件未達 · 順位差 -29.599999999999994 / -16.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0065efb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065efb8.md) · スコア 32.067308 · 採用条件未達 · 順位差 -33.532692 / -6.826923000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 4.885713999999993,
        "reverse_margin": 55.99999999999999
      },
      "new": "00831fb4",
      "score": 65.6
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.76,
          0.6785714285714286
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
        "margin": -4.885713999999993,
        "reverse_margin": 0.0
      },
      "new": "00630db4",
      "score": 60.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.76,
          0.59375
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
        "margin": -9.974999999999994,
        "reverse_margin": -1.875
      },
      "new": "005dc0a0",
      "score": 55.625
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d6b36ffbd9393de4012841e1a2936f3c"></a>

### v15.7.4 [`008006ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008006ac.md) FUN_008006ac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831fb4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -65.6 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00832018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832018.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -65.6
      },
      "new": "00831fb4",
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
      "new": "00832018",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9ec50f8b452a42aa0a8ba351c00b4476"></a>

### v15.7.4 [`008006c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/008006c8.md) FUN_008006c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832034.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00832018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832018.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00831fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831fb4.md) · スコア 0.48 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832034",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00832018",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831fb4",
      "score": 0.48
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1025eef044b3b02820ef02348c5f0a35"></a>

### v15.7.4 [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) FUN_00800728

`competing_candidates` 

呼出元 0件  · 呼出先 41件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

- 1. [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · スコア 47.932391 · 採用条件未達 · 順位差 46.292738 / 46.268952000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00820258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820258.md) · スコア 1.639653 · 採用条件未達 · 順位差 -46.292738 / -69.39769100000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006ef704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md) · スコア 1.25523 · 採用条件未達 · 順位差 -46.677161000000005 / -32.578477 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00628120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md) · スコア 1.194432 · 採用条件未達 · 順位差 -46.737959000000004 / 1.194432 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) · スコア 0.941423 · 採用条件未達 · 順位差 -46.990968 / -59.914368 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · スコア 0.753138 · 採用条件未達 · 順位差 -47.179253 / 0.753138 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008b8310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b8310.md) · スコア 0.502092 · 採用条件未達 · 順位差 -47.430299000000005 / -48.376606 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) · スコア 0.439331 · 採用条件未達 · 順位差 -47.49306 / -48.245984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6705020920502092,
          0.6705020920502092
        ],
        "cfg_coverage": [
          0.3851132686084142,
          0.4204946996466431
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 46.292738,
        "reverse_margin": 46.268952000000006
      },
      "new": "00832094",
      "score": 47.932391
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02301255230125523,
          0.0912863070539419
        ],
        "cfg_coverage": [
          0.012944983818770227,
          0.041237113402061855
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.292738,
        "reverse_margin": -69.39769100000001
      },
      "new": "00820258",
      "score": 1.639653
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02092050209205021,
          0.031545741324921134
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
        "margin": -46.677161000000005,
        "reverse_margin": -32.578477
      },
      "new": "006ef704",
      "score": 1.25523
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca5f72fa8d6650bfb80bb444d69a2e6f"></a>

### v15.7.4 [`00801940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801940.md) FUN_00801940

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008332ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332ac.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008332ac",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bef023ba76c2ff53a5cf6add86099308"></a>

### v15.7.4 [`0080195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/0080195c.md) FUN_0080195c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008332c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332c8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008332ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332ac.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00833684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/00833684.md) · スコア 0.0541 · 採用条件未達 · 順位差 — / — · 
- 4. [`008332d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332d4.md) · スコア 0.0508 · 採用条件未達 · 順位差 — / — · 
- 5. [`008339fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008339fc.md) · スコア 0.0269 · 採用条件未達 · 順位差 — / — · 
- 6. [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · スコア 0.0126 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008332c8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008332ac",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00833684",
      "score": 0.0541
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7eafddde799c29732d642e0ac84bb29a"></a>

### v15.7.4 [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) FUN_00801968

`competing_candidates` 

呼出元 3件 [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) [`00801d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801d18.md) · 呼出先 5件 [`007e8a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8a54.md) [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) [`00801d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801d18.md) [`00802090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802090.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) · スコア 59.990838 · 採用条件未達 · 順位差 10.387363999999998 / 59.990838 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008332d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332d4.md) · スコア 49.603474 · 採用条件未達 · 順位差 -10.387363999999998 / 1.2565389999999965 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) · スコア 44.429892 · 採用条件未達 · 順位差 -15.560945999999994 / 44.429892 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) · スコア 41.037494 · 採用条件未達 · 順位差 -18.953343999999994 / 41.037494 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) · スコア 18.430919 · 採用条件未達 · 順位差 -41.559918999999994 / -56.614119 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a7e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e928.md) · スコア 15.906906 · 採用条件未達 · 順位差 -44.083932 / 15.906906 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006fa294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa294.md) · スコア 15.828748 · 採用条件未達 · 順位差 -44.16209 / -42.692213 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008df27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008df/008df27c.md) · スコア 14.987254 · 採用条件未達 · 順位差 -45.003584 / -35.894304 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.788135593220339,
          0.788135593220339
        ],
        "cfg_coverage": [
          0.7121212121212122,
          0.6351351351351351
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 10.387363999999998,
        "reverse_margin": 59.990838
      },
      "new": "006a0648",
      "score": 59.990838
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6991525423728814,
          0.6991525423728814
        ],
        "cfg_coverage": [
          0.4696969696969697,
          0.38271604938271603
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.387363999999998,
        "reverse_margin": 1.2565389999999965
      },
      "new": "008332d4",
      "score": 49.603474
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5889830508474576,
          0.6123348017621145
        ],
        "cfg_coverage": [
          0.45454545454545453,
          0.47619047619047616
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -15.560945999999994,
        "reverse_margin": 44.429892
      },
      "new": "006fcb34",
      "score": 44.429892
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.4 [`00801d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801d18.md) FUN_00801d18

`competing_candidates` 

呼出元 1件 [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) · 呼出先 3件 [`007e8a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8a54.md) [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00833684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/00833684.md) · スコア 72.702703 · 採用条件未達 · 順位差 4.634934000000001 / 10.810811000000001 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006a09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a09f8.md) · スコア 68.067769 · 採用条件未達 · 順位差 -4.634934000000001 / 68.067769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) · スコア 61.891892 · 採用条件未達 · 順位差 -10.810811000000001 / 61.891892 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) · スコア 44.931453 · 採用条件未達 · 順位差 -27.771250000000002 / 44.931453 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) · スコア 40.810811 · 採用条件未達 · 順位差 -31.891892 / 40.810811 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006fa760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa760.md) · スコア 26.183945 · 採用条件未達 · 順位差 -46.518758 / -48.76993699999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md) · スコア 22.807808 · 採用条件未達 · 順位差 -49.894895 / 22.807808 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a7ec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ec68.md) · スコア 22.592311 · 採用条件未達 · 順位差 -50.110392000000004 / 22.592311 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8783783783783784,
          0.8783783783783784
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
        "margin": 4.634934000000001,
        "reverse_margin": 10.810811000000001
      },
      "new": "00833684",
      "score": 72.702703
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8558558558558559,
          0.8558558558558559
        ],
        "cfg_coverage": [
          0.875,
          0.835820895522388
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -4.634934000000001,
        "reverse_margin": 68.067769
      },
      "new": "006a09f8",
      "score": 68.067769
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6981981981981982,
          0.7311320754716981
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -10.810811000000001,
        "reverse_margin": 61.891892
      },
      "new": "006fcec0",
      "score": 61.891892
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.4 [`00802090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802090.md) FUN_00802090

`competing_candidates` 

呼出元 2件 [`00801968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00801/00801968.md) [`00802090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802090.md) · 呼出先 4件 [`007e8a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8a54.md) [`00802090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802090.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

- 1. [`006a0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0d70.md) · スコア 61.429372 · 採用条件未達 · 順位差 4.739387000000001 / 61.429372 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008339fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008339fc.md) · スコア 56.689985 · 採用条件未達 · 順位差 -4.739387000000001 / 1.8774289999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) · スコア 23.724536 · 採用条件未達 · 順位差 -37.704836 / 23.724536 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) · スコア 23.724536 · 採用条件未達 · 順位差 -37.704836 / 23.724536 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006faa28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006faa28.md) · スコア 17.436259 · 採用条件未達 · 順位差 -43.993113 / -56.38101700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a7ef68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7ef68.md) · スコア 17.127909 · 採用条件未達 · 順位差 -44.301463 / -46.672545 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md) · スコア 16.17721 · 採用条件未達 · 順位差 -45.252162 / -54.33903599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a7fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7f/00a7fd88.md) · スコア 7.387145 · 採用条件未達 · 順位差 -54.042227 / 7.387145 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8363228699551569,
          0.8363228699551569
        ],
        "cfg_coverage": [
          0.5785714285714286,
          0.5625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.739387000000001,
        "reverse_margin": 61.429372
      },
      "new": "006a0d70",
      "score": 61.429372
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7937219730941704,
          0.7937219730941704
        ],
        "cfg_coverage": [
          0.4857142857142857,
          0.4533333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.739387000000001,
        "reverse_margin": 1.8774289999999993
      },
      "new": "008339fc",
      "score": 56.689985
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30493273542600896,
          0.31336405529953915
        ],
        "cfg_coverage": [
          0.2714285714285714,
          0.29457364341085274
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -37.704836,
        "reverse_margin": 23.724536
      },
      "new": "006fc46c",
      "score": 23.724536
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-49e060039ee4713981760f60c70a536f"></a>

### v15.7.4 [`00802f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802f8c.md) FUN_00802f8c

`competing_candidates` 

呼出元 2件 [`0080279c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/0080279c.md) [`00802f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802f8c.md) · 呼出先 2件 [`00802f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00802/00802f8c.md) [`008035e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/008035e8.md)

- 1. [`008348f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00834/008348f8.md) · スコア 67.063882 · 採用条件未達 · 順位差 64.17690400000001 / 64.562302 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009fe070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fe/009fe070.md) · スコア 2.886978 · 採用条件未達 · 順位差 -64.17690400000001 / -1.0440559999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009febf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fe/009febf8.md) · スコア 2.297297 · 採用条件未達 · 順位差 -64.766585 / -1.633737 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8992628992628993,
          0.8992628992628993
        ],
        "cfg_coverage": [
          0.6554054054054054,
          0.6928571428571428
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 64.17690400000001,
        "reverse_margin": 64.562302
      },
      "new": "008348f8",
      "score": 67.063882
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.036855036855036855,
          0.05660377358490566
        ],
        "cfg_coverage": [
          0.033783783783783786,
          0.05555555555555555
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -64.17690400000001,
        "reverse_margin": -1.0440559999999999
      },
      "new": "009fe070",
      "score": 2.886978
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02702702702702703,
          0.04150943396226415
        ],
        "cfg_coverage": [
          0.033783783783783786,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -64.766585,
        "reverse_margin": -1.633737
      },
      "new": "009febf8",
      "score": 2.297297
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1b1b9474d4ff8dac202b5509fd77ac57"></a>

### v15.7.4 [`00803ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803ac8.md) FUN_00803ac8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b0cd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cd34.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00835434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835434.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b0cd34",
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
      "new": "00835434",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-30a9e5116b91db0057f6517a9c804cea"></a>

### v15.7.4 [`00803ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803ae4.md) FUN_00803ae4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00835450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835450.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00835434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835434.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00835450",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00835434",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4df1476c3cef12b6b88284ef920f386b"></a>

### v15.7.4 [`00803f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803f44.md) FUN_00803f44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007aeb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aeb88.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`008358b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008358b0.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "007aeb88",
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
      "new": "008358b0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-489d5c887fbd301b3059c941a2fc3a1c"></a>

### v15.7.4 [`00803f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803f60.md) FUN_00803f60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008358cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008358cc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008358b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/008358b0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008358cc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008358b0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6686a3a99b653709b6fd683a4eb295fa"></a>

### v15.7.4 [`00804394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804394.md) FUN_00804394

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008d84f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d84f4.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 2. [`00835d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d00.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 60.0
      },
      "new": "008d84f4",
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
        "reverse_margin": 0.0
      },
      "new": "00835d00",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1273d24d7943783ccb3d166fa70e7244"></a>

### v15.7.4 [`008043b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008043b0.md) FUN_008043b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00835d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d1c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00835d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d00.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00835d1c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00835d00",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-49c732840e1da7f9034a15f3b01044b0"></a>

### v15.7.4 [`008043e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008043e4.md) FUN_008043e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00835d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d50.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00835d50",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6bef740d249aaa208d7abf4bd3ac597b"></a>

### v15.7.4 [`008043f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/008043f4.md) FUN_008043f4

`competing_candidates` 

呼出元 1件 [`00800728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00800/00800728.md) · 呼出先 0件 

- 1. [`00835d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d60.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`00835d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835d50.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00835d60",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00835d50",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b1518c74c418764072cae36a9274fa55"></a>

### v15.7.4 [`00804444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804444.md) FUN_00804444

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006fb854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb854.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00835db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835db0.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "006fb854",
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
      "new": "00835db0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5ec4f19a8a3d4846ad9f4704d7dd17dd"></a>

### v15.7.4 [`00804460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804460.md) FUN_00804460

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00835dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835dcc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00835db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00835/00835db0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00835dcc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00835db0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6a272eeff90f7b752eaeeb64338c4de4"></a>

### v15.7.4 [`00804c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804c98.md) FUN_00804c98

`competing_candidates` 

呼出元 3件 [`00804634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804634.md) [`00804e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804e34.md) [`008053c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00805/008053c4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00836604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00836/00836604.md) · スコア 29.092606 · 採用条件未達 · 順位差 24.432412 / 24.432412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008fc2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc2c4.md) · スコア 4.660194 · 採用条件未達 · 順位差 -24.432412 / 4.660194 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a3a740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a740.md) · スコア 4.660194 · 採用条件未達 · 順位差 -24.432412 / 4.660194 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0082ab38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ab38.md) · スコア 2.330097 · 採用条件未達 · 順位差 -26.762509 / -42.955617 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.092606 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.092606 / -20.809182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.092606 / -57.138122 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0079d8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d8ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -29.092606 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42718446601941745,
          0.42718446601941745
        ],
        "cfg_coverage": [
          0.17307692307692307,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.432412,
        "reverse_margin": 24.432412
      },
      "new": "00836604",
      "score": 29.092606
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07766990291262135,
          0.08
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
        "margin": -24.432412,
        "reverse_margin": 4.660194
      },
      "new": "008fc2c4",
      "score": 4.660194
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07766990291262135,
          0.08
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
        "margin": -24.432412,
        "reverse_margin": 4.660194
      },
      "new": "00a3a740",
      "score": 4.660194
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fc525edfd2436afcac75e2b3848e4886"></a>

### v15.7.4 [`008070c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008070c8.md) FUN_008070c8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`007f808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f808c.md) [`00a6b4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b4f8.md)

- 1. [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) · スコア 50.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00838a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a54.md) · スコア 20.0 · 採用条件未達 · 順位差 -30.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008bf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf810.md) · スコア 20.0 · 採用条件未達 · 順位差 -30.0 / -32.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "00838a34",
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
        "reverse_margin": -34.285714
      },
      "new": "00838a54",
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
        "reverse_margin": -32.0
      },
      "new": "008bf810",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e566c62617852cd087af5de68dd53968"></a>

### v15.7.4 [`008070e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008070e8.md) FUN_008070e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a54.md) · スコア 54.285714 · 採用条件未達 · 順位差 34.285714 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) · スコア 20.0 · 採用条件未達 · 順位差 -34.285714 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 34.285714,
        "reverse_margin": 34.285714
      },
      "new": "00838a54",
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
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.285714,
        "reverse_margin": -30.0
      },
      "new": "00838a34",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-00a505c3d72ab539c52ddc80d2811985"></a>

### v15.7.4 [`00807104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807104.md) FUN_00807104

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a70.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00838a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a54.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) · スコア 1.5 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00838a70",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838a54",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838a34",
      "score": 1.5
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6bc1d39505e45f30a1613c23da1ed6ce"></a>

### v15.7.4 [`00807164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807164.md) FUN_00807164

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`007f8950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8950.md)

- 1. [`00838ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ad0.md) · スコア 44.0 · 採用条件未達 · 順位差 24.0 / 24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00838ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ae4.md) · スコア 20.0 · 採用条件未達 · 順位差 -24.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.0,
        "reverse_margin": 24.0
      },
      "new": "00838ad0",
      "score": 44.0
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
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.0,
        "reverse_margin": -34.285714
      },
      "new": "00838ae4",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-be13bdae58838a4024c72cce477cb1af"></a>

### v15.7.4 [`00807178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807178.md) FUN_00807178

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00694668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694668.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00838ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ae4.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00838ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ad0.md) · スコア 20.0 · 採用条件未達 · 順位差 -60.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00694668",
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
        "reverse_margin": 34.285714
      },
      "new": "00838ae4",
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
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.0,
        "reverse_margin": -24.0
      },
      "new": "00838ad0",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5b23ed86df19ab9695702364684ce111"></a>

### v15.7.4 [`00807194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807194.md) FUN_00807194

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838b00.md) · スコア 84.0 · 採用条件未達 · 順位差 81.6 / 81.6 · 
- 2. [`00838ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ad0.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00838ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838ae4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 81.6,
        "reverse_margin": 81.6
      },
      "new": "00838b00",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838ad0",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838ae4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bf8230bc81af24099f15d542d3033ae0"></a>

### v15.7.4 [`008071f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008071f4.md) FUN_008071f4

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`007f7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7e3c.md) [`00807354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807354.md) [`00807358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807358.md) [`00a6ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ca44.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

- 1. [`00838b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838b60.md) · スコア 69.5 · 採用条件未達 · 順位差 1.2073170000000033 / 1.2073170000000033 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00ac3154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3154.md) · スコア 68.292683 · 採用条件未達 · 順位差 -1.2073170000000033 / -1.4634149999999977 · instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.825,
          0.825
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
        "margin": 1.2073170000000033,
        "reverse_margin": 1.2073170000000033
      },
      "new": "00838b60",
      "score": 69.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.825,
          0.8048780487804879
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
        "margin": -1.2073170000000033,
        "reverse_margin": -1.4634149999999977
      },
      "new": "00ac3154",
      "score": 68.292683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9d4c92303579faa428b847920097951f"></a>

### v15.7.4 [`008072e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008072e0.md) FUN_008072e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838c4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00838c4c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0d4abd8a5ac2a8060a3ea1c497ae1e08"></a>

### v15.7.4 [`008072fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008072fc.md) FUN_008072fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838c68.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00838c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838c4c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00838b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838b60.md) · スコア 0.3 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00838c68",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838c4c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838b60",
      "score": 0.3
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-507f621b48f8bc7dd8d4d88a0b111f5c"></a>

### v15.7.4 [`00807340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807340.md) FUN_00807340

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cac.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 56.0
      },
      "new": "00838cac",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-76fe357ecd1cba552417cc999d5c3c70"></a>

### v15.7.4 [`00807354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807354.md) FUN_00807354

`competing_candidates` 

呼出元 1件 [`008071f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/008071f4.md) · 呼出先 0件 

- 1. [`00838cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc0.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`00838cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cac.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00838cc0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838cac",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4ccc409d81c6f1191dcbc3e0b4675daf"></a>

### v15.7.4 [`0080735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080735c.md) FUN_0080735c

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829bb8.md) [`00a6a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`008d83dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md) · スコア 38.461538 · 採用条件未達 · 順位差 3.4615379999999973 / 0.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00838cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc8.md) · スコア 35.0 · 採用条件未達 · 順位差 -3.4615379999999973 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a3f04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f04c.md) · スコア 32.941176 · 採用条件未達 · 順位差 -5.520361999999999 / -11.764706000000004 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00ac32c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32c0.md) · スコア 30.0 · 採用条件未達 · 順位差 -8.461537999999997 / -2.608696000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009015b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/009015b0.md) · スコア 27.6 · 採用条件未達 · 順位差 -10.861537999999996 / -2.3999999999999986 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a40d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40d08.md) · スコア 24.0 · 採用条件未達 · 順位差 -14.461537999999997 / -2.0869570000000017 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008ff628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff628.md) · スコア 3.529412 · 採用条件未達 · 順位差 -34.932126 / -11.764705999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009dce3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dce3c.md) · スコア 3.272727 · 採用条件未達 · 順位差 -35.188810999999994 / -9.818182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.3076923076923077
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
        "margin": 3.4615379999999973,
        "reverse_margin": 0.0
      },
      "new": "008d83dc",
      "score": 38.461538
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.5
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.4615379999999973,
        "reverse_margin": 0.0
      },
      "new": "00838cc8",
      "score": 35.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22,
          0.21568627450980393
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
        "margin": -5.520361999999999,
        "reverse_margin": -11.764706000000004
      },
      "new": "00a3f04c",
      "score": 32.941176
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b66b1d0b944b376a514d887eaeba5fb9"></a>

### v15.7.4 [`00807438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807438.md) FUN_00807438

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838da4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00838da4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-38b1d4e83029093f5179ad8c7ff80a43"></a>

### v15.7.4 [`00807454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807454.md) FUN_00807454

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00838dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838dc0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00838da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838da4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00838cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc8.md) · スコア 0.24 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00838dc0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838da4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00838cc8",
      "score": 0.24
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c59224d38fbc58643c4da1d367c7d7b0"></a>

### v15.7.4 [`0080834c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/0080834c.md) FUN_0080834c

`competing_candidates` 

呼出元 2件 [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00839cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00839/00839cb8.md) · スコア 74.285714 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008b97c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b97c8.md) · スコア 14.285714 · 採用条件未達 · 順位差 -60.0 / 14.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0057d784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d784.md) · スコア 13.043478 · 採用条件未達 · 順位差 -61.242236 / 13.043478 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0057cd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cd20.md) · スコア 11.428571 · 採用条件未達 · 順位差 -62.857143 / 11.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00769674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769674.md) · スコア 11.111111 · 採用条件未達 · 順位差 -63.174603 / -35.757576 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) · スコア 6.760563 · 採用条件未達 · 順位差 -67.525151 / -52.957747000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a41d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d54.md) · スコア 6.153846 · 採用条件未達 · 順位差 -68.131868 / 6.153846 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.285714 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9047619047619048,
          0.9047619047619048
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
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00839cb8",
      "score": 74.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23809523809523808,
          0.29411764705882354
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
        "margin": -60.0,
        "reverse_margin": 14.285714
      },
      "new": "008b97c8",
      "score": 14.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23809523809523808,
          0.21739130434782608
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
        "margin": -61.242236,
        "reverse_margin": 13.043478
      },
      "new": "0057d784",
      "score": 13.043478
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a9315fce6e38aec93e6fc3d44c945927"></a>

### v15.7.4 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) FUN_00808774

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 142件 [`004489a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/004489a8.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449358.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)

- 1. [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · スコア 20.210967 · 採用条件未達 · 順位差 20.034427 / 20.026671 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · スコア 0.17654 · 採用条件未達 · 順位差 -20.034427 / -21.892255000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · スコア 0.105924 · 採用条件未達 · 順位差 -20.105043 / -36.981977 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · スコア 0.011769 · 採用条件未達 · 順位差 -20.199198 / -31.172933 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.210967 / -6.686567 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.210967 / -18.829777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.210967 / -25.613698 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.210967 / -24.727163 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2601020007846214,
          0.2545594163947015
        ],
        "cfg_coverage": [
          0.25371934057096907,
          0.2468701095461659
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 20.034427,
        "reverse_margin": 20.026671
      },
      "new": "0083a0e0",
      "score": 20.210967
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0029423303256178894,
          0.0033624747814391394
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
        "margin": -20.034427,
        "reverse_margin": -21.892255000000002
      },
      "new": "00a26020",
      "score": 0.17654
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0017653981953707335,
          0.0049532195927352776
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
        "margin": -20.105043,
        "reverse_margin": -36.981977
      },
      "new": "006d1fa4",
      "score": 0.105924
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5919ed92fbbc86e83f6c68f6b307a272"></a>

### v15.7.4 [`0080d71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d71c.md) FUN_0080d71c

`competing_candidates` 

呼出元 2件 [`00860980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860980.md) [`009f5644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f5/009f5644.md) · 呼出先 0件 

- 1. [`0083f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f244.md) · スコア 94.0 · 採用条件未達 · 順位差 93.9977 / 93.9976 · 
- 2. [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · スコア 0.0023 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 93.9977,
        "reverse_margin": 93.9976
      },
      "new": "0083f244",
      "score": 94.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0083a0e0",
      "score": 0.0023
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7130e960f4f9024f996672b1d3360258"></a>

### v15.7.4 [`0080d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d8e0.md) FUN_0080d8e0

`competing_candidates` [`0083f408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f408.md)

呼出元 1件 [`009f426c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f426c.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0080d834",
    "0080d8e8",
    "0083f35c",
    "0083f410"
  ],
  "initial_reason": ""
}
~~~

<a id="review-d3e5a64d94ce411a429b668cd247614a"></a>

### v15.7.4 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) FUN_0080dd1c

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 42件 [`00429de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md) [`00448aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`00449358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449358.md) [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md)

- 1. [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · スコア 6.686567 · 採用条件未達 · 順位差 6.622207 / 6.686567 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · スコア 0.06436 · 採用条件未達 · 順位差 -6.622207 / -18.765417 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -20.210967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -31.900984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -22.068795 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -12.973583 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -25.613698 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.686567 / -31.184702 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04585679806918745,
          0.04477611940298507
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
        "margin": 6.622207,
        "reverse_margin": 6.686567
      },
      "new": "0083f844",
      "score": 6.686567
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0010726736390453205,
          0.0018340210912425492
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
        "margin": -6.622207,
        "reverse_margin": -18.765417
      },
      "new": "0084e55c",
      "score": 0.06436
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
        "margin": -6.686567,
        "reverse_margin": -20.210967
      },
      "new": "0083a0e0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-07d769724c370db2b115fdedcf376f9d"></a>

### v15.7.4 [`0081546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/0081546c.md) FUN_0081546c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00847218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847218.md) · スコア 49.019608 · 採用条件未達 · 順位差 0.0 / 3.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008496f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008496f4.md) · スコア 49.019608 · 採用条件未達 · 順位差 0.0 / 49.019608 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`004fa344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa344.md) · スコア 25.263158 · 採用条件未達 · 順位差 -23.756449999999997 / 25.263158 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) · スコア 24.705882 · 採用条件未達 · 順位差 -24.313726 / 24.705882 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005303fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303fc.md) · スコア 24.705882 · 採用条件未達 · 順位差 -24.313726 / 24.705882 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00571034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571034.md) · スコア 20.869565 · 採用条件未達 · 順位差 -28.150042999999997 / 20.869565 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00571174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571174.md) · スコア 20.869565 · 採用条件未達 · 順位差 -28.150042999999997 / 20.869565 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -49.019608 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7058823529411765,
          0.7058823529411765
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
        "margin": 0.0,
        "reverse_margin": 3.333332999999996
      },
      "new": "00847218",
      "score": 49.019608
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7058823529411765,
          0.7058823529411765
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
        "margin": 0.0,
        "reverse_margin": 49.019608
      },
      "new": "008496f4",
      "score": 49.019608
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47058823529411764,
          0.42105263157894735
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
        "margin": -23.756449999999997,
        "reverse_margin": 25.263158
      },
      "new": "004fa344",
      "score": 25.263158
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-08d84d2c4e142964e811ef9b27e6c30d"></a>

### v15.7.4 [`00815e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815e74.md) FUN_00815e74

`competing_candidates` 

呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00847c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847c20.md) · スコア 11.428571 · 採用条件未達 · 順位差 3.2929779999999997 / 3.8095229999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00470eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470eb0.md) · スコア 8.135593 · 採用条件未達 · 順位差 -3.2929779999999997 / 8.135593 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0084983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/0084983c.md) · スコア 8.135593 · 採用条件未達 · 順位差 -3.2929779999999997 / 8.135593 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0067e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e430.md) · スコア 4.067797 · 採用条件未達 · 順位差 -7.360774 / 4.067797 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008491dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008491dc.md) · スコア 4.067797 · 採用条件未達 · 順位差 -7.360774 / 4.067797 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00847820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847820.md) · スコア 3.636364 · 採用条件未達 · 順位差 -7.792206999999999 / 3.636364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a5e400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e400.md) · スコア 3.478261 · 採用条件未達 · 順位差 -7.95031 / 3.478261 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005ec020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec020.md) · スコア 2.706767 · 採用条件未達 · 順位差 -8.721803999999999 / 2.706767 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2033898305084746,
          0.19047619047619047
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
        "margin": 3.2929779999999997,
        "reverse_margin": 3.8095229999999995
      },
      "new": "00847c20",
      "score": 11.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13559322033898305,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.2929779999999997,
        "reverse_margin": 8.135593
      },
      "new": "00470eb0",
      "score": 8.135593
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13559322033898305,
          0.42105263157894735
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
        "margin": -3.2929779999999997,
        "reverse_margin": 8.135593
      },
      "new": "0084983c",
      "score": 8.135593
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f6a3712222bfb6ab969a061ff4c2c172"></a>

### v15.7.4 [`00815f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815f60.md) FUN_00815f60

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`0049dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc18.md) · スコア 76.129032 · 採用条件未達 · 順位差 0.0 / 76.129032 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0064a5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a5d0.md) · スコア 76.129032 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`00847d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847d1c.md) · スコア 71.129032 · 採用条件未達 · 順位差 -5.0 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009e224c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e224c.md) · スコア 71.129032 · 採用条件未達 · 順位差 -5.0 / 0.0 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 5. [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) · スコア 70.322581 · 採用条件未達 · 順位差 -5.806450999999996 / 70.322581 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005a1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1310.md) · スコア 49.247312 · 採用条件未達 · 順位差 -26.881719999999994 / 49.247312 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00791810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/00791810.md) · スコア 20.5 · 採用条件未達 · 順位差 -55.629031999999995 / 20.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008479f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/008479f8.md) · スコア 20.357143 · 採用条件未達 · 順位差 -55.771888999999994 / 20.357143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9354838709677419,
          0.9354838709677419
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
        "reverse_margin": 76.129032
      },
      "new": "0049dc18",
      "score": 76.129032
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9354838709677419,
          0.9354838709677419
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
      "new": "0064a5d0",
      "score": 76.129032
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9354838709677419,
          0.9354838709677419
        ],
        "cfg_coverage": [
          0.8181818181818182,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.0,
        "reverse_margin": 0.0
      },
      "new": "00847d1c",
      "score": 71.129032
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5bb986b406cede87af213f7b1ab4c90b"></a>

### v15.7.4 [`008161ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008161ac.md) FUN_008161ac

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

- 1. [`00847f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md) · スコア 73.333333 · 採用条件未達 · 順位差 6.666665999999992 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00847fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md) · スコア 66.666667 · 採用条件未達 · 順位差 -6.666665999999992 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.666665999999992,
        "reverse_margin": 0.0
      },
      "new": "00847f68",
      "score": 73.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
        ],
        "cfg_coverage": [
          0.75,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.666665999999992,
        "reverse_margin": 0.0
      },
      "new": "00847fd4",
      "score": 66.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f75e35f0652fdb23e7325cc8f571333f"></a>

### v15.7.4 [`00816218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816218.md) FUN_00816218

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

- 1. [`00847f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847f68.md) · スコア 73.333333 · 採用条件未達 · 順位差 6.666665999999992 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00847fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847fd4.md) · スコア 66.666667 · 採用条件未達 · 順位差 -6.666665999999992 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.666665999999992,
        "reverse_margin": 0.0
      },
      "new": "00847f68",
      "score": 73.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
        ],
        "cfg_coverage": [
          0.75,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.666665999999992,
        "reverse_margin": 0.0
      },
      "new": "00847fd4",
      "score": 66.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-eb2292880c21f9acb8ce91bdab0e03b0"></a>

### v15.7.4 [`0081673c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/0081673c.md) FUN_0081673c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`0096f1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f1d8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008484f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008484f8.md) · スコア 72.0 · 採用条件未達 · 順位差 0.0 / 44.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00a6c254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c254.md) · スコア 72.0 · 採用条件未達 · 順位差 0.0 / 44.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00848534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848534.md) · スコア 16.0 · 採用条件未達 · 順位差 -56.0 / -5.1695910000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -72.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8666666666666667,
          0.8666666666666667
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
        "reverse_margin": 44.0
      },
      "new": "008484f8",
      "score": 72.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8666666666666667,
          0.8666666666666667
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
        "reverse_margin": 44.0
      },
      "new": "00a6c254",
      "score": 72.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.26666666666666666,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -56.0,
        "reverse_margin": -5.1695910000000005
      },
      "new": "00848534",
      "score": 16.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2d2a47ac7b3928dd1d0a172775339850"></a>

### v15.7.4 [`00817ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817ac0.md) FUN_00817ac0

`competing_candidates` 

呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`008498b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008498b8.md) · スコア 64.469987 · 採用条件未達 · 順位差 32.094508000000005 / 35.938697000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) · スコア 32.375479 · 採用条件未達 · 順位差 -32.094508000000005 / 32.375479 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) · スコア 26.896552 · 採用条件未達 · 順位差 -37.573435 / 26.896552 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00868a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00868/00868a80.md) · スコア 16.170034 · 採用条件未達 · 順位差 -48.299953 / 16.170034 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00848be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848be0.md) · スコア 15.96424 · 採用条件未達 · 順位差 -48.505747 / 15.96424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0086b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md) · スコア 15.948718 · 採用条件未達 · 順位差 -48.521269000000004 / 15.948718 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0046134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/0046134c.md) · スコア 15.517241 · 採用条件未達 · 順位差 -48.952746000000005 / 15.517241 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) · スコア 15.517241 · 採用条件未達 · 順位差 -48.952746000000005 / 15.517241 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8275862068965517,
          0.8275862068965517
        ],
        "cfg_coverage": [
          0.7407407407407407,
          0.7407407407407407
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 32.094508000000005,
        "reverse_margin": 35.938697000000005
      },
      "new": "008498b8",
      "score": 64.469987
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.46551724137931033,
          0.54
        ],
        "cfg_coverage": [
          0.2222222222222222,
          0.2857142857142857
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -32.094508000000005,
        "reverse_margin": 32.375479
      },
      "new": "0046e864",
      "score": 32.375479
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3793103448275862,
          0.39285714285714285
        ],
        "cfg_coverage": [
          0.2222222222222222,
          0.20689655172413793
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -37.573435,
        "reverse_margin": 26.896552
      },
      "new": "0051ac84",
      "score": 26.896552
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ea3e67b2ab3eee00e5441b640f428f01"></a>

### v15.7.4 [`00817dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817dd8.md) FUN_00817dd8

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00849c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849c94.md) · スコア 9.63361 · 採用条件未達 · 順位差 9.63361 / 9.63361 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00849bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849bd0.md) · スコア 0.0 · 採用条件未達 · 順位差 -9.63361 / -7.058824 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14606741573033707,
          0.14606741573033707
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.043478260869565216
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 9.63361,
        "reverse_margin": 9.63361
      },
      "new": "00849c94",
      "score": 9.63361
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
        "margin": -9.63361,
        "reverse_margin": -7.058824
      },
      "new": "00849bd0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f7804bff2a8834fd908defc63780c293"></a>

### v15.7.4 [`00817f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817f84.md) FUN_00817f84

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00849efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849efc.md) · スコア 71.06383 · 採用条件未達 · 順位差 52.563323 / 52.563323 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00849e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849e40.md) · スコア 18.500507 · 採用条件未達 · 順位差 -52.563323 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0087dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md) · スコア 14.553672 · 採用条件未達 · 順位差 -56.510158 / 14.553672 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c35778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md) · スコア 8.478261 · 採用条件未達 · 順位差 -62.58556899999999 / 8.478261 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c358e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c358e8.md) · スコア 8.478261 · 採用条件未達 · 順位差 -62.58556899999999 / -2.886754 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -71.06383 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00849fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849fb8.md) · スコア 0.0 · 採用条件未達 · 順位差 -71.06383 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.851063829787234,
          0.851063829787234
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
        "margin": 52.563323,
        "reverse_margin": 52.563323
      },
      "new": "00849efc",
      "score": 71.06383
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2765957446808511,
          0.2765957446808511
        ],
        "cfg_coverage": [
          0.1,
          0.09523809523809523
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -52.563323,
        "reverse_margin": 0.0
      },
      "new": "00849e40",
      "score": 18.500507
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2765957446808511,
          0.22033898305084745
        ],
        "cfg_coverage": [
          0.1,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -56.510158,
        "reverse_margin": 14.553672
      },
      "new": "0087dbe4",
      "score": 14.553672
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e3070c6a6a7a0d43d764080b1f260992"></a>

### v15.7.4 [`00818040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818040.md) FUN_00818040

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00849e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849e40.md) · スコア 18.500507 · 採用条件未達 · 順位差 0.0 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00849efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849efc.md) · スコア 18.500507 · 採用条件未達 · 順位差 0.0 / -52.563323 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0087dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md) · スコア 16.587571 · 採用条件未達 · 順位差 -1.9129359999999984 / 16.587571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c35778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md) · スコア 8.478261 · 採用条件未達 · 順位差 -10.022245999999999 / 8.478261 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c358e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c358e8.md) · スコア 8.478261 · 採用条件未達 · 順位差 -10.022245999999999 / -2.886754 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 0.0 · 採用条件未達 · 順位差 -18.500507 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00849fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849fb8.md) · スコア 0.0 · 採用条件未達 · 順位差 -18.500507 / -73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2765957446808511,
          0.2765957446808511
        ],
        "cfg_coverage": [
          0.09523809523809523,
          0.09523809523809523
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
      "new": "00849e40",
      "score": 18.500507
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2765957446808511,
          0.2765957446808511
        ],
        "cfg_coverage": [
          0.09523809523809523,
          0.1
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": -52.563323
      },
      "new": "00849efc",
      "score": 18.500507
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3191489361702128,
          0.2542372881355932
        ],
        "cfg_coverage": [
          0.09523809523809523,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -1.9129359999999984,
        "reverse_margin": 16.587571
      },
      "new": "0087dbe4",
      "score": 16.587571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3d967f4a5c5f4a3a165e4003d226d4e2"></a>

### v15.7.4 [`008180fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/008180fc.md) FUN_008180fc

`competing_candidates` 

呼出元 1件 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00849fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849fb8.md) · スコア 73.333333 · 採用条件未達 · 順位差 3.333332999999996 / 3.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0066c014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066c/0066c014.md) · スコア 70.0 · 採用条件未達 · 順位差 -3.333332999999996 / 70.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c35a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35a58.md) · スコア 65.0 · 採用条件未達 · 順位差 -8.333332999999996 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c35aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35aa8.md) · スコア 65.0 · 採用条件未達 · 順位差 -8.333332999999996 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00849df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849df8.md) · スコア 61.428571 · 採用条件未達 · 順位差 -11.904761999999998 / 61.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00aa321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa321c.md) · スコア 53.333333 · 採用条件未達 · 順位差 -19.999999999999993 / -19.607842999999995 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00479670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479670.md) · スコア 10.0 · 採用条件未達 · 順位差 -63.333332999999996 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005a1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ae0.md) · スコア 10.0 · 採用条件未達 · 順位差 -63.333332999999996 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 3.333332999999996,
        "reverse_margin": 3.333332999999996
      },
      "new": "00849fb8",
      "score": 73.333333
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.333332999999996,
        "reverse_margin": 70.0
      },
      "new": "0066c014",
      "score": 70.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8333333333333334,
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
        "margin": -8.333332999999996,
        "reverse_margin": 65.0
      },
      "new": "00c35a58",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a375c4d9ccd2932a69d0e06c5efb02fd"></a>

### v15.7.4 [`00818144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00818/00818144.md) _INIT_151

`competing_candidates` 

呼出元 0件  · 呼出先 20件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md)

- 1. [`0084a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084a/0084a000.md) · スコア 23.379444 · 採用条件未達 · 順位差 16.995124 / 17.010497 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aae348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae348.md) · スコア 6.38432 · 採用条件未達 · 順位差 -16.995124 / -9.932310000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a95e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a95e04.md) · スコア 6.092237 · 採用条件未達 · 順位差 -17.287207 / -9.934473 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · スコア 6.075251 · 採用条件未達 · 順位差 -17.304192999999998 / -17.058165000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b1b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1b/00b1b3c0.md) · スコア 6.030746 · 採用条件未達 · 順位差 -17.348698 / -29.277924999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · スコア 6.022859 · 採用条件未達 · 順位差 -17.356585 / -3.7959829999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) · スコア 6.0 · 採用条件未達 · 順位差 -17.379444 / -30.909077000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a7/006a7480.md) · スコア 2.570815 · 採用条件未達 · 順位差 -20.808629 / 2.570815 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19497822188060465,
          0.19497822188060465
        ],
        "cfg_coverage": [
          0.3235294117647059,
          0.284037558685446
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.995124,
        "reverse_margin": 17.010497
      },
      "new": "0084a000",
      "score": 23.379444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006405329233922624,
          0.01957713390759593
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
        "margin": -16.995124,
        "reverse_margin": -9.932310000000001
      },
      "new": "00aae348",
      "score": 6.38432
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0015372790161414297,
          0.003126628452318916
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
        "margin": -17.287207,
        "reverse_margin": -9.934473
      },
      "new": "00a95e04",
      "score": 6.092237
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-889785668d4460ed1ae15709184ec2ff"></a>

### v15.7.4 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) FUN_0081c6a0

`competing_candidates` 

呼出元 4件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00822930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822930.md) [`00996ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md) [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md) · 呼出先 78件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00448aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448aac.md) [`00449290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449290.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

- 1. [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · スコア 18.829777 · 採用条件未達 · 順位差 18.299582 / 18.554674 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · スコア 0.530195 · 採用条件未達 · 順位差 -18.299582 / -44.397377 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · スコア 0.263989 · 採用条件未達 · 順位差 -18.565788 / -30.920713000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · スコア 0.111524 · 採用条件未達 · 順位差 -18.718253 / -36.976377 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) · スコア 0.083643 · 採用条件未達 · 順位差 -18.746134 / -37.037338999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · スコア 0.0269 · 採用条件未達 · 順位差 -18.802877 / -22.041895 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · スコア 0.023037 · 採用条件未達 · 順位差 -18.80674 / -20.18793 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · スコア 0.0 · 採用条件未達 · 順位差 -18.829777 / -6.686567 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24953531598513012,
          0.24621733149931224
        ],
        "cfg_coverage": [
          0.11553784860557768,
          0.10283687943262411
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 18.299582,
        "reverse_margin": 18.554674
      },
      "new": "0084e55c",
      "score": 18.829777
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006505576208178439,
          0.016666666666666666
        ],
        "cfg_coverage": [
          0.00796812749003984,
          0.006993006993006993
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.299582,
        "reverse_margin": -44.397377
      },
      "new": "00850798",
      "score": 0.530195
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.004182156133828996,
          0.0038395904436860067
        ],
        "cfg_coverage": [
          0.00398406374501992,
          0.0016806722689075631
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.565788,
        "reverse_margin": -30.920713000000003
      },
      "new": "00a73338",
      "score": 0.263989
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4048c0e2144fa6bbc2da5b484238687d"></a>

### v15.7.4 [`0081e868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081e/0081e868.md) FUN_0081e868

`competing_candidates` 

呼出元 2件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 7件 [`00595388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595388.md) [`0076e8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e8c0.md) [`0076e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e910.md) [`007d8fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d8/007d8fa4.md) [`00839f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839f88.md)

- 1. [`00850798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00850/00850798.md) · スコア 44.927572 · 採用条件未達 · 順位差 44.354693999999995 / 44.397377 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) · スコア 0.572878 · 採用条件未達 · 順位差 -44.354693999999995 / 0.572878 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f9670.md) · スコア 0.572792 · 採用条件未達 · 順位差 -44.35478 / -38.907169 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) · スコア 0.314295 · 採用条件未達 · 順位差 -44.613277 / 0.314295 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · スコア 0.055021 · 採用条件未達 · 順位差 -44.872550999999994 / -18.774756 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6384248210023866,
          0.6369047619047619
        ],
        "cfg_coverage": [
          0.34408602150537637,
          0.3356643356643357
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 44.354693999999995,
        "reverse_margin": 44.397377
      },
      "new": "00850798",
      "score": 44.927572
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.008353221957040573,
          0.024054982817869417
        ],
        "cfg_coverage": [
          0.0035842293906810036,
          0.0125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -44.354693999999995,
        "reverse_margin": 0.572878
      },
      "new": "008d7058",
      "score": 0.572878
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.00954653937947494,
          0.01032258064516129
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
        "margin": -44.35478,
        "reverse_margin": -38.907169
      },
      "new": "005f9670",
      "score": 0.572792
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cec2589ee62c65b8e7150796f0a362f0"></a>

### v15.7.4 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) FUN_0081f58c

`competing_candidates` 

呼出元 0件  · 呼出先 41件 [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`00421b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b38.md) [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`004502bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md)

- 1. [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · スコア 19.904615 · 採用条件未達 · 順位差 18.986248 / 15.055384 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009f5918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f5918.md) · スコア 0.918367 · 採用条件未達 · 順位差 -18.986248 / -1.8802280000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006b70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b70f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / -26.693548 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006e8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / -35.16196 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / -33.045549 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`009f6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / -5.206541 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a6b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b610.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / -25.599178 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a9abdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9abdc.md) · スコア 0.0 · 採用条件未達 · 順位差 -19.904615 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3054393305439331,
          0.292
        ],
        "cfg_coverage": [
          0.02127659574468085,
          0.019230769230769232
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 18.986248,
        "reverse_margin": 15.055384
      },
      "new": "008514c4",
      "score": 19.904615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02510460251046025,
          0.015306122448979591
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
        "margin": -18.986248,
        "reverse_margin": -1.8802280000000002
      },
      "new": "009f5918",
      "score": 0.918367
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
        "margin": -19.904615,
        "reverse_margin": -26.693548
      },
      "new": "006b70f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e85ae51f978b35916267add7b015288b"></a>

### v15.7.4 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) FUN_0081fa64

`competing_candidates` 

呼出元 20件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`0081f9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f9ac.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0083dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dac4.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md)

- 1. [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · スコア 24.600955 · 採用条件未達 · 順位差 22.219752999999997 / 20.512262999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) · スコア 2.381202 · 採用条件未達 · 順位差 -22.219752999999997 / -34.150146 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00912918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00912/00912918.md) · スコア 2.312215 · 採用条件未達 · 順位差 -22.288739999999997 / -20.197618 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) · スコア 2.311342 · 採用条件未達 · 順位差 -22.289613 / -34.597735 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) · スコア 2.290456 · 採用条件未達 · 順位差 -22.310499 / -35.948175 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a95e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a95e04.md) · スコア 2.218864 · 採用条件未達 · 順位差 -22.382091 / -13.807846000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0082e2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082e2e0.md) · スコア 2.17791 · 採用条件未達 · 順位差 -22.423045 / 2.17791 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · スコア 2.176076 · 採用条件未達 · 順位差 -22.424878999999997 / -27.971283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2965159377316531,
          0.29563932002956395
        ],
        "cfg_coverage": [
          0.15991471215351813,
          0.1431297709923664
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 22.219752999999997,
        "reverse_margin": 20.512262999999997
      },
      "new": "008519cc",
      "score": 24.600955
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006671608598962194,
          0.005642633228840125
        ],
        "cfg_coverage": [
          0.0021321961620469083,
          0.0021551724137931034
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.219752999999997,
        "reverse_margin": -34.150146
      },
      "new": "00922c2c",
      "score": 2.381202
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006671608598962194,
          0.0046248715313463515
        ],
        "cfg_coverage": [
          0.0021321961620469083,
          0.001736111111111111
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.288739999999997,
        "reverse_margin": -20.197618
      },
      "new": "00912918",
      "score": 2.312215
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ce9a5eeacbd7dcf4f380c5f05e29f338"></a>

### v15.7.4 [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) FUN_00821350

`competing_candidates` 

呼出元 0件  · 呼出先 22件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`00450394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450394.md) [`00450398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md)

- 1. [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) · スコア 28.295938 · 採用条件未達 · 順位差 19.254939999999998 / 22.551257 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006dd430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md) · スコア 9.040998 · 採用条件未達 · 順位差 -19.254939999999998 / 9.040998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · スコア 7.318748 · 採用条件未達 · 順位差 -20.97719 / -26.579253 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) · スコア 5.757576 · 採用条件未達 · 順位差 -22.538362 / 5.757576 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00536af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md) · スコア 5.115865 · 採用条件未達 · 順位差 -23.180073 / 5.115865 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0068a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068a684.md) · スコア 4.491979 · 採用条件未達 · 順位差 -23.803959 / 4.491979 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) · スコア 3.127349 · 採用条件未達 · 順位差 -25.168589 / -17.775411000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) · スコア 2.552995 · 採用条件未達 · 順位差 -25.742943 / -62.30414799999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37967914438502676,
          0.3776595744680851
        ],
        "cfg_coverage": [
          0.18181818181818182,
          0.19672131147540983
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.254939999999998,
        "reverse_margin": 22.551257
      },
      "new": "008532c8",
      "score": 28.295938
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11229946524064172,
          0.15555555555555556
        ],
        "cfg_coverage": [
          0.015151515151515152,
          0.029411764705882353
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -19.254939999999998,
        "reverse_margin": 9.040998
      },
      "new": "006dd430",
      "score": 9.040998
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09090909090909091,
          0.08374384236453201
        ],
        "cfg_coverage": [
          0.015151515151515152,
          0.014705882352941176
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -20.97719,
        "reverse_margin": -26.579253
      },
      "new": "0061e668",
      "score": 7.318748
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-efcd0d8b2886012e541f22f302d90737"></a>

### v15.7.4 [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) FUN_008216e4

`competing_candidates` 

呼出元 1件 [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) · 呼出先 22件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`004665d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004665d0.md) [`00467cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467cf8.md) [`00467d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467d30.md)

- 1. [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · スコア 37.850331 · 採用条件未達 · 順位差 36.296932999999996 / 34.161010999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) · スコア 1.553398 · 採用条件未達 · 順位差 -36.296932999999996 / 1.553398 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) · スコア 1.553398 · 採用条件未達 · 順位差 -36.296932999999996 / -11.033606 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) · スコア 0.776699 · 採用条件未達 · 順位差 -37.073631999999996 / -11.316324 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00675e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675e90.md) · スコア 0.776699 · 採用条件未達 · 順位差 -37.073631999999996 / 0.776699 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b59cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md) · スコア 0.776699 · 採用条件未達 · 順位差 -37.073631999999996 / 0.776699 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · スコア 0.399334 · 採用条件未達 · 順位差 -37.450996999999994 / -31.226939 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) · スコア 0.38835 · 採用条件未達 · 順位差 -37.461980999999994 / 0.38835 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.49514563106796117,
          0.49514563106796117
        ],
        "cfg_coverage": [
          0.42201834862385323,
          0.40707964601769914
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.296932999999996,
        "reverse_margin": 34.161010999999995
      },
      "new": "00853660",
      "score": 37.850331
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025889967637540454,
          0.03278688524590164
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
        "margin": -36.296932999999996,
        "reverse_margin": 1.553398
      },
      "new": "0043df70",
      "score": 1.553398
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025889967637540454,
          0.038834951456310676
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
        "margin": -36.296932999999996,
        "reverse_margin": -11.033606
      },
      "new": "0059921c",
      "score": 1.553398
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b94a1a690cde277a270d10a620458d1a"></a>

### v15.7.4 [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) FUN_00821cb4

`competing_candidates` 

呼出元 40件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`005bc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc280.md) [`006440f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/006440f0.md) [`00644238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644238.md) [`00644304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644304.md) · 呼出先 0件 

- 1. [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) · スコア 36.4286 · 採用条件未達 · 順位差 31.8953 / 36.2335 · 
- 2. [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) · スコア 4.5333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00853fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853fa8.md) · スコア 0.1951 · 採用条件未達 · 順位差 — / — · 
- 4. [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) · スコア 0.0426 · 採用条件未達 · 順位差 — / — · 
- 5. [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · スコア 0.0402 · 採用条件未達 · 順位差 — / — · 
- 6. [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · スコア 0.0259 · 採用条件未達 · 順位差 — / — · 
- 7. [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · スコア 0.0059 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 31.8953,
        "reverse_margin": 36.2335
      },
      "new": "00853c30",
      "score": 36.4286
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "004428f0",
      "score": 4.5333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00853fa8",
      "score": 0.1951
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ae46947ec91d7a62d12c51741e6d65eb"></a>

### v15.7.4 [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) FUN_00821cbc

`competing_candidates` 

呼出元 0件  · 呼出先 24件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f48.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`0045a2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a2e4.md) [`0045a320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md)

- 1. [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · スコア 64.40201 · 採用条件未達 · 順位差 57.467337 / 57.467337 · instruction_coverage
- 2. [`00483fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/00483fb0.md) · スコア 6.934673 · 採用条件未達 · 順位差 -57.467337 / 6.934673 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0071e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md) · スコア 4.513613 · 採用条件未達 · 順位差 -59.888397000000005 / -44.295911000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`004cd748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) · スコア 3.006075 · 採用条件未達 · 順位差 -61.395935 / 3.006075 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00798020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md) · スコア 3.006075 · 採用条件未達 · 順位差 -61.395935 / 3.006075 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b3a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md) · スコア 3.006075 · 採用条件未達 · 順位差 -61.395935 / 3.006075 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b1eb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md) · スコア 2.42915 · 採用条件未達 · 順位差 -61.972860000000004 / -25.147484 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) · スコア 1.585903 · 採用条件未達 · 順位差 -62.816107 / -61.762115 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6733668341708543,
          0.6733668341708543
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage"
        ],
        "margin": 57.467337,
        "reverse_margin": 57.467337
      },
      "new": "00853c38",
      "score": 64.40201
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11557788944723618,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -57.467337,
        "reverse_margin": 6.934673
      },
      "new": "00483fb0",
      "score": 6.934673
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06030150753768844,
          0.19047619047619047
        ],
        "cfg_coverage": [
          0.04477611940298507,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -59.888397000000005,
        "reverse_margin": -44.295911000000004
      },
      "new": "0071e7f4",
      "score": 4.513613
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fabba3a15642a6f23fa12c7a621fb4dd"></a>

### v15.7.4 [`0082202c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/0082202c.md) FUN_0082202c

`competing_candidates` 

呼出元 4件 [`005bc078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc078.md) [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`008fef58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fe/008fef58.md) · 呼出先 2件 [`00574760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574760.md) [`005bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc058.md)

- 1. [`00853fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853fa8.md) · スコア 69.756098 · 採用条件未達 · 順位差 69.756098 / 69.756098 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008545cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008545cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.756098 / -48.8 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009305cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.756098 / -55.076923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0093398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093398c.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.756098 / -55.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.756098 / -48.52459 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b2cf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf10.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.756098 / -11.230769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8292682926829268,
          0.8292682926829268
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
        "margin": 69.756098,
        "reverse_margin": 69.756098
      },
      "new": "00853fa8",
      "score": 69.756098
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
        "margin": -69.756098,
        "reverse_margin": -48.8
      },
      "new": "008545cc",
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
        "margin": -69.756098,
        "reverse_margin": -55.076923
      },
      "new": "009305cc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4172f27a484a14b2e8b4255206f77979"></a>

### v15.7.4 [`00822650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822650.md) FUN_00822650

`competing_candidates` 

呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f50.md) [`00574760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574760.md) [`005bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc058.md)

- 1. [`008545cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008545cc.md) · スコア 48.8 · 採用条件未達 · 順位差 48.8 / 48.8 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00853fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853fa8.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.8 / -69.756098 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.48,
          0.48
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
        "margin": 48.8,
        "reverse_margin": 48.8
      },
      "new": "008545cc",
      "score": 48.8
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
        "margin": -48.8,
        "reverse_margin": -69.756098
      },
      "new": "00853fa8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1212012a081bd9d7c7dc8470e6b97721"></a>

### v15.7.4 [`008226b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008226b4.md) FUN_008226b4

`competing_candidates` 

呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`004588e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588e8.md) [`00458970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458970.md) [`00458e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458e28.md) [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md)

- 1. [`00854630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/00854630.md) · スコア 6.836848 · 採用条件未達 · 順位差 1.9188149999999995 / 4.019823 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0078f164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078f164.md) · スコア 4.918033 · 採用条件未達 · 順位差 -1.9188149999999995 / 4.918033 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a92a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a92/00a92a30.md) · スコア 1.509434 · 採用条件未達 · 順位差 -5.327414 / -50.490566 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) · スコア 0.377358 · 採用条件未達 · 順位差 -6.45949 / -44.563117999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0086584c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/0086584c.md) · スコア 0.377358 · 採用条件未達 · 順位差 -6.45949 / 0.377358 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006b70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b70f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.836848 / -26.693548 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006ec68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ec/006ec68c.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.836848 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00735b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.836848 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09433962264150944,
          0.09433962264150944
        ],
        "cfg_coverage": [
          0.058823529411764705,
          0.06976744186046512
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.9188149999999995,
        "reverse_margin": 4.019823
      },
      "new": "00854630",
      "score": 6.836848
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09433962264150944,
          0.08196721311475409
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
        "margin": -1.9188149999999995,
        "reverse_margin": 4.918033
      },
      "new": "0078f164",
      "score": 4.918033
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025157232704402517,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.327414,
        "reverse_margin": -50.490566
      },
      "new": "00a92a30",
      "score": 1.509434
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c0cf12b15d998a3cd9cd17820a9f9b61"></a>

### v15.7.4 [`00822930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/00822930.md) FUN_00822930

`competing_candidates` 

呼出元 0件  · 呼出先 10件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00824d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824d74.md) [`00845f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f00.md) [`0085474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/0085474c.md) [`0085e004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e004.md)

- 1. [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · スコア 16.552016 · 採用条件未達 · 順位差 16.11255 / 16.369802999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00756264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00756/00756264.md) · スコア 0.439466 · 採用条件未達 · 順位差 -16.11255 / 0.439466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) · スコア 0.180956 · 採用条件未達 · 順位差 -16.37106 / -21.539893000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00adf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00adf/00adf01c.md) · スコア 0.180956 · 採用条件未達 · 順位差 -16.37106 / -5.000551 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009c1478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c1478.md) · スコア 0.155106 · 採用条件未達 · 順位差 -16.39691 / 0.155106 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) · スコア 0.129255 · 採用条件未達 · 順位差 -16.422760999999998 / -32.210663 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) · スコア 0.129255 · 採用条件未達 · 順位差 -16.422760999999998 / 0.129255 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · スコア 0.051702 · 採用条件未達 · 順位差 -16.500314 / -30.095657000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21844032744506678,
          0.21995661605206074
        ],
        "cfg_coverage": [
          0.172279792746114,
          0.18421052631578946
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.11255,
        "reverse_margin": 16.369802999999997
      },
      "new": "008548ac",
      "score": 16.552016
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.007324429125376993,
          0.008985200845665961
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
        "margin": -16.11255,
        "reverse_margin": 0.439466
      },
      "new": "00756264",
      "score": 0.439466
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.003015941404566997,
          0.0036784025223331584
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
        "margin": -16.37106,
        "reverse_margin": -21.539893000000003
      },
      "new": "006b01f8",
      "score": 0.180956
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-35ae5d9e13346a75d1678fce9523ccc6"></a>

### v15.7.4 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) FUN_00824eb0

`competing_candidates` 

呼出元 0件  · 呼出先 166件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00428648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md)

- 1. [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · スコア 28.963011 · 採用条件未達 · 順位差 26.51723 / 26.601156000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · スコア 2.445781 · 採用条件未達 · 順位差 -26.51723 / -42.051585 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · スコア 2.40388 · 採用条件未達 · 順位差 -26.559131 / -39.62103 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · スコア 2.0 · 採用条件未達 · 順位差 -26.963011 / -8.873332 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · スコア 0.853381 · 採用条件未達 · 順位差 -28.109630000000003 / -23.747574 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00aa9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa9/00aa9230.md) · スコア 0.83517 · 採用条件未達 · 順位差 -28.127841 / 0.83517 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00979548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md) · スコア 0.630251 · 採用条件未達 · 順位差 -28.33276 / 0.630251 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · スコア 0.495697 · 採用条件未達 · 順位差 -28.467314000000002 / -32.11788 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3276861346411057,
          0.32565352237483386
        ],
        "cfg_coverage": [
          0.17118997912317327,
          0.1752136752136752
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 26.51723,
        "reverse_margin": 26.601156000000003
      },
      "new": "00856dec",
      "score": 28.963011
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.008024966562639322,
          0.0067898906073179935
        ],
        "cfg_coverage": [
          0.0020876826722338203,
          0.0019193857965451055
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.51723,
        "reverse_margin": -42.051585
      },
      "new": "00a8e3bc",
      "score": 2.445781
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015158270173874276,
          0.006731340328647793
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
        "margin": -26.559131,
        "reverse_margin": -39.62103
      },
      "new": "00914c94",
      "score": 2.40388
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

