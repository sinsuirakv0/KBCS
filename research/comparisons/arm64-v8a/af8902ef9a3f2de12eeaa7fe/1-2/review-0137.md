# v15.7.4 → v16.0.0 · 追加調査 (137)

[一覧の目次](README.md)

<a id="review-261f093b8736c7eaaae5de1a1c06022e"></a>

### v16.0.0 [`00818d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00818/00818d00.md) FUN_00818d00

`competing_candidates` 

呼出元 1件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007e44e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e4/007e44e8.md) · スコア 63.207375 · 採用条件未達 · 順位差 58.990526 / 58.951199 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005d2c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2c18.md) · スコア 4.256176 · 採用条件未達 · 順位差 -68.51615000000001 / -58.951199 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009034dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/009034dc.md) · スコア 4.089005 · 採用条件未達 · 順位差 -2.7119029999999995 / -59.11837 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00632964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632964.md) · スコア 3.720991 · 採用条件未達 · 順位差 -25.983386999999997 / -59.486384 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065c7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c7b4.md) · スコア 3.642764 · 採用条件未達 · 順位差 -1.007838 / -59.564611 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00706234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00706/00706234.md) · スコア 3.373403 · 採用条件未達 · 順位差 0.30409600000000037 / -59.833971999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007059c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00705/007059c8.md) · スコア 2.993829 · 採用条件未達 · 順位差 -0.8594530000000002 / -60.213546 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009d5ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d5ea0.md) · スコア 2.837375 · 採用条件未達 · 順位差 -5.866171 / -60.37 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.788787483702738,
          0.788787483702738
        ],
        "cfg_coverage": [
          0.694006309148265,
          0.7333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 58.990526,
        "reverse_margin": 58.951199
      },
      "new": "007e44e8",
      "score": 63.207375
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025380710659898477,
          0.02607561929595828
        ],
        "cfg_coverage": [
          0.040740740740740744,
          0.03666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -68.51615000000001,
        "reverse_margin": -58.951199
      },
      "new": "005d2c18",
      "score": 4.256176
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09541984732824428,
          0.03259452411994785
        ],
        "cfg_coverage": [
          0.0196078431372549,
          0.006666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.7119029999999995,
        "reverse_margin": -59.11837
      },
      "new": "009034dc",
      "score": 4.089005
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0093f940c2f55ee5cce942036d0e8bd2"></a>

### v16.0.0 [`0081996c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/0081996c.md) FUN_0081996c

`competing_candidates` 

呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

- 1. [`0051aaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051aaec.md) · スコア 29.230769 · 採用条件未達 · 順位差 29.230769 / 21.153845999999998 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007e5154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5154.md) · スコア 8.076923 · 採用条件未達 · 順位差 -21.923077 / -21.153845999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004e9d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9d4c.md) · スコア 6.923077 · 採用条件未達 · 順位差 6.923077 / -22.307692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a06d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06d28.md) · スコア 6.923077 · 採用条件未達 · 順位差 6.923077 / -22.307692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00add6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md) · スコア 4.772727 · 採用条件未達 · 順位差 4.772727 / -24.458042 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006f0aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f0/006f0aa8.md) · スコア 4.736842 · 採用条件未達 · 順位差 4.736842 / -24.493927 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00642008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642008.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -29.230769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0065e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e0a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -4.326923 / -29.230769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.15384615384615385
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
        "margin": 29.230769,
        "reverse_margin": 21.153845999999998
      },
      "new": "0051aaec",
      "score": 29.230769
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14583333333333334,
          0.1346153846153846
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
        "margin": -21.923077,
        "reverse_margin": -21.153845999999998
      },
      "new": "007e5154",
      "score": 8.076923
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1875,
          0.11538461538461539
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
        "margin": 6.923077,
        "reverse_margin": -22.307692
      },
      "new": "004e9d4c",
      "score": 6.923077
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d86594326b86d2ba11fd2725e5cbac70"></a>

### v16.0.0 [`00819f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819f5c.md) FUN_00819f5c

`competing_candidates` 

呼出元 1件 [`0081fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081f/0081fd88.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`0071e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e92c.md)

- 1. [`007e5734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5734.md) · スコア 37.800344 · 採用条件未達 · 順位差 34.330956 / 33.928977 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b9fd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md) · スコア 3.871367 · 採用条件未達 · 順位差 3.871367 / -33.928977 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0064f874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f874.md) · スコア 3.469388 · 採用条件未達 · 順位差 -7.919347 / -34.330956 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009877e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009877e0.md) · スコア 3.428571 · 採用条件未達 · 順位差 -43.006766 / -34.371773000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f61cc.md) · スコア 3.265306 · 採用条件未達 · 順位差 -4.529566 / -34.535038 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007f7410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7410.md) · スコア 3.265306 · 採用条件未達 · 順位差 -57.590485 / -34.535038 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a3d70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d70c.md) · スコア 3.265306 · 採用条件未達 · 順位差 -22.808121 / -34.535038 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00686590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686590.md) · スコア 2.763708 · 採用条件未達 · 順位差 -4.702959 / -35.036636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47619047619047616,
          0.47619047619047616
        ],
        "cfg_coverage": [
          0.3614457831325301,
          0.3614457831325301
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.330956,
        "reverse_margin": 33.928977
      },
      "new": "007e5734",
      "score": 37.800344
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05442176870748299,
          0.05442176870748299
        ],
        "cfg_coverage": [
          0.030303030303030304,
          0.03614457831325301
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 3.871367,
        "reverse_margin": -33.928977
      },
      "new": "00b9fd0c",
      "score": 3.871367
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0821256038647343,
          0.05782312925170068
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
        "margin": -7.919347,
        "reverse_margin": -34.330956
      },
      "new": "0064f874",
      "score": 3.469388
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-865aee3523bafedc8afad48ead945c24"></a>

### v16.0.0 [`0081a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a450.md) FUN_0081a450

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007e5c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5c28.md) · スコア 48.645833 · 採用条件未達 · 順位差 38.333333 / 35.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00501998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501998.md) · スコア 13.520833 · 採用条件未達 · 順位差 1.7175539999999998 / -35.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0063ef44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ef44.md) · スコア 12.25 · 採用条件未達 · 順位差 -21.695577999999998 / -36.395833 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0064248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064248c.md) · スコア 10.537836 · 採用条件未達 · 順位差 2.4890559999999997 / -38.107997000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a80570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a80570.md) · スコア 8.571429 · 採用条件未達 · 順位差 -37.002551 / -40.074404 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008be2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be2a0.md) · スコア 8.4375 · 採用条件未達 · 順位差 -31.68262 / -40.208333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bba4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba4f4.md) · スコア 8.4375 · 採用条件未達 · 順位差 -2.5829079999999998 / -40.208333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) · スコア 8.026316 · 採用条件未達 · 順位差 -33.663125 / -40.619517 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.671875,
          0.671875
        ],
        "cfg_coverage": [
          0.4166666666666667,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 38.333333,
        "reverse_margin": 35.125
      },
      "new": "007e5c28",
      "score": 48.645833
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21311475409836064,
          0.203125
        ],
        "cfg_coverage": [
          0.06666666666666667,
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
        "margin": 1.7175539999999998,
        "reverse_margin": -35.125
      },
      "new": "00501998",
      "score": 13.520833
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24489795918367346,
          0.1875
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.05
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.695577999999998,
        "reverse_margin": -36.395833
      },
      "new": "0063ef44",
      "score": 12.25
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-df6e05a3fd151f9621041a2c0f8efe0f"></a>

### v16.0.0 [`0081a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a550.md) FUN_0081a550

`competing_candidates` 

呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 4件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00819d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819d84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007e5d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5d28.md) · スコア 17.391304 · 採用条件未達 · 順位差 7.020934000000002 / 2.5764890000000022 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0049e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md) · スコア 14.814815 · 採用条件未達 · 順位差 14.814815 / -2.5764890000000022 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0085c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4c4.md) · スコア 14.046753 · 採用条件未達 · 順位差 3.1376620000000006 / -3.344551000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00564c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md) · スコア 13.714286 · 採用条件未達 · 順位差 13.714286 / -3.677018000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00979350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979350.md) · スコア 13.246753 · 採用条件未達 · 順位差 13.246753 / -4.144551000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) · スコア 12.972973 · 採用条件未達 · 順位差 12.972973 / -4.418331000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a6a6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a6cc.md) · スコア 6.956522 · 採用条件未達 · 順位差 -0.9382150000000005 / -10.434782000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00461e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461e04.md) · スコア 3.478261 · 採用条件未達 · 順位差 -3.4282140000000005 / -13.913043000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.29850746268656714,
          0.2898550724637681
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
        "margin": 7.020934000000002,
        "reverse_margin": 2.5764890000000022
      },
      "new": "007e5d28",
      "score": 17.391304
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24691358024691357,
          0.2898550724637681
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
        "margin": 14.814815,
        "reverse_margin": -2.5764890000000022
      },
      "new": "0049e24c",
      "score": 14.814815
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22077922077922077,
          0.2463768115942029
        ],
        "cfg_coverage": [
          0.04,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 3.1376620000000006,
        "reverse_margin": -3.344551000000001
      },
      "new": "0085c4c4",
      "score": 14.046753
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e1557e612accddfe1619cb0451731dba"></a>

### v16.0.0 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) FUN_0081a7d4

`competing_candidates` 

呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 50件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440b3c.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004506c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/004506c0.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md)

- 1. [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) · スコア 25.552642 · 採用条件未達 · 順位差 16.854363 / 16.764156 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0067da3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067da3c.md) · スコア 8.788486 · 採用条件未達 · 順位差 4.151581000000001 / -16.764156 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a4f47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md) · スコア 8.413016 · 採用条件未達 · 順位差 5.816001000000001 / -17.139626 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · スコア 8.292294 · 採用条件未達 · 順位差 -1.9626529999999995 / -17.260348 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00abb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abb/00abb930.md) · スコア 6.225282 · 採用条件未達 · 順位差 -29.083388999999997 / -19.32736 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · スコア 4.300375 · 採用条件未達 · 順位差 -2.2218350000000004 / -21.252267 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · スコア 4.262829 · 採用条件未達 · 順位差 -12.69352 / -21.289813 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009613bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00961/009613bc.md) · スコア 2.39779 · 採用条件未達 · 順位差 -11.132612 / -23.154851999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2664495114006515,
          0.25594493116395495
        ],
        "cfg_coverage": [
          0.1097972972972973,
          0.11035653650254669
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.854363,
        "reverse_margin": 16.764156
      },
      "new": "007e5fa4",
      "score": 25.552642
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03125,
          0.013141426783479349
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.151581000000001,
        "reverse_margin": -16.764156
      },
      "new": "0067da3c",
      "score": 8.788486
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.023809523809523808,
          0.00688360450563204
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 5.816001000000001,
        "reverse_margin": -17.139626
      },
      "new": "00a4f47c",
      "score": 8.413016
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f05eed56b4099ca4a8c8fd08460cc136"></a>

### v16.0.0 [`0081c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md) FUN_0081c2b4

`competing_candidates` 

呼出元 4件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`00830618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830618.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00a6d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d8f8.md) · スコア 31.566502 · 採用条件未達 · 順位差 31.566502 / 2.1022159999999985 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007e7970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7970.md) · スコア 29.464286 · 採用条件未達 · 順位差 1.1607149999999997 / -2.1022159999999985 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`004492e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/004492e0.md) · スコア 14.571429 · 採用条件未達 · 順位差 9.529412 / -16.995072999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0044c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c794.md) · スコア 14.571429 · 採用条件未達 · 順位差 7.071429 / -16.995072999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0053a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a0e0.md) · スコア 11.142857 · 採用条件未達 · 順位差 11.142857 / -20.423645 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00561d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561d88.md) · スコア 11.142857 · 採用条件未達 · 順位差 11.142857 / -20.423645 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006a8de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8de8.md) · スコア 11.142857 · 採用条件未達 · 順位差 11.142857 / -20.423645 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0044fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb34.md) · スコア 10.285714 · 採用条件未達 · 順位差 -6.9224489999999985 / -21.280788 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6037735849056604,
          0.45714285714285713
        ],
        "cfg_coverage": [
          0.3333333333333333,
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
        "margin": 31.566502,
        "reverse_margin": 2.1022159999999985
      },
      "new": "00a6d8f8",
      "score": 31.566502
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42857142857142855,
          0.42857142857142855
        ],
        "cfg_coverage": [
          0.1875,
          0.20689655172413793
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.1607149999999997,
        "reverse_margin": -2.1022159999999985
      },
      "new": "007e7970",
      "score": 29.464286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5666666666666667,
          0.24285714285714285
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
        "margin": 9.529412,
        "reverse_margin": -16.995072999999998
      },
      "new": "004492e0",
      "score": 14.571429
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b08c8c1cfeebfa7bc2c8fee156fd8ca7"></a>

### v16.0.0 [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) FUN_0081cb48

`competing_candidates` 

呼出元 10件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`0081c8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c8c4.md) [`0081cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cea0.md) [`0081fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081f/0081fefc.md) [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00815ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00815/00815ce8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007e8204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8204.md) · スコア 65.793103 · 採用条件未達 · 順位差 54.898213 / 59.414208 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009479b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/009479b4.md) · スコア 6.378895 · 採用条件未達 · 順位差 -46.637148 / -59.414208 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) · スコア 6.275031 · 採用条件未達 · 順位差 -35.414410000000004 / -59.518072000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006ffbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ffbb4.md) · スコア 6.137931 · 採用条件未達 · 順位差 -19.98578 / -59.655172 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006425d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md) · スコア 5.930204 · 採用条件未達 · 順位差 -33.150541000000004 / -59.862899 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md) · スコア 3.724138 · 採用条件未達 · 順位差 -32.475862000000006 / -62.068965000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007d1374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d1/007d1374.md) · スコア 3.672625 · 採用条件未達 · 順位差 -15.843715 / -62.120478000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00644304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644304.md) · スコア 2.0 · 採用条件未達 · 順位差 -4.459459 / -63.793103 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7298850574712644,
          0.7298850574712644
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
        "margin": 54.898213,
        "reverse_margin": 59.414208
      },
      "new": "007e8204",
      "score": 65.793103
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08823529411764706,
          0.06896551724137931
        ],
        "cfg_coverage": [
          0.023255813953488372,
          0.012048192771084338
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -46.637148,
        "reverse_margin": -59.414208
      },
      "new": "009479b4",
      "score": 6.378895
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11458333333333333,
          0.06321839080459771
        ],
        "cfg_coverage": [
          0.05263157894736842,
          0.024096385542168676
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -35.414410000000004,
        "reverse_margin": -59.518072000000004
      },
      "new": "00a08428",
      "score": 6.275031
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-765b897efb0abc0f3864d272cd3ebbef"></a>

### v16.0.0 [`0081cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cea0.md) FUN_0081cea0

`competing_candidates` 

呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007e855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e855c.md) · スコア 70.095851 · 採用条件未達 · 順位差 51.581939999999996 / 51.503032 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009d56bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d56bc.md) · スコア 18.592819 · 採用条件未達 · 順位差 5.733758999999999 / -51.503032 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00897c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897c24.md) · スコア 10.725745 · 採用条件未達 · 順位差 -44.35514499999999 / -59.37010599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · スコア 9.518717 · 採用条件未達 · 順位差 -53.460874999999994 / -60.577133999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) · スコア 9.211612 · 採用条件未達 · 順位差 -0.05494099999999946 / -60.884238999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006b5918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md) · スコア 6.700169 · 採用条件未達 · 順位差 -0.8203050000000003 / -63.395681999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007df104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df104.md) · スコア 5.758242 · 採用条件未達 · 順位差 1.6160310000000004 / -64.337609 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a70ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70ac4.md) · スコア 5.729565 · 採用条件未達 · 順位差 -4.723361 / -64.366286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.839572192513369,
          0.839572192513369
        ],
        "cfg_coverage": [
          0.8860759493670886,
          0.9090909090909091
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 51.581939999999996,
        "reverse_margin": 51.503032
      },
      "new": "007e855c",
      "score": 70.095851
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28187919463087246,
          0.22459893048128343
        ],
        "cfg_coverage": [
          0.2553191489361702,
          0.15584415584415584
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 5.733758999999999,
        "reverse_margin": -51.503032
      },
      "new": "009d56bc",
      "score": 18.592819
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
      "new": "00897c24",
      "score": 10.725745
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bc61fc3845c822d3db96f5a5a8c4762b"></a>

### v16.0.0 [`0081d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d18c.md) FUN_0081d18c

`competing_candidates` 

呼出元 3件 [`0072b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b104.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md)

- 1. [`007e8848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8848.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 50.0,
        "reverse_margin": 50.0
      },
      "new": "007e8848",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-42468d7cbebec2a96b284a5b0e46f8d7"></a>

### v16.0.0 [`0081d1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md) FUN_0081d1ac

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`007add18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007e8868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8868.md) · スコア 52.147059 · 採用条件未達 · 順位差 35.942471999999995 / 35.147059 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008c82bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c82bc.md) · スコア 17.0 · 採用条件未達 · 順位差 17.0 / -35.147059 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009dd710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd710.md) · スコア 16.558824 · 採用条件未達 · 順位差 16.558824 / -35.588235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006fb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fb130.md) · スコア 14.209857 · 採用条件未達 · 順位差 -1.3923050000000003 / -37.937202 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00808060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808060.md) · スコア 13.764706 · 採用条件未達 · 順位差 13.764706 / -38.382352999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00807f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/00807f4c.md) · スコア 13.029412 · 採用条件未達 · 順位差 5.2229600000000005 / -39.117647 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00906ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906ad0.md) · スコア 13.029412 · 採用条件未達 · 順位差 13.029412 / -39.117647 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00701c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00701/00701c38.md) · スコア 11.911765 · 採用条件未達 · 順位差 -39.394138 / -40.235293999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7235772357723578,
          0.6544117647058824
        ],
        "cfg_coverage": [
          0.5522388059701493,
          0.5441176470588235
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.942471999999995,
        "reverse_margin": 35.147059
      },
      "new": "007e8868",
      "score": 52.147059
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38961038961038963,
          0.22058823529411764
        ],
        "cfg_coverage": [
          0.1875,
          0.08823529411764706
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 17.0,
        "reverse_margin": -35.147059
      },
      "new": "008c82bc",
      "score": 17.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37662337662337664,
          0.21323529411764705
        ],
        "cfg_coverage": [
          0.17142857142857143,
          0.08823529411764706
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 16.558824,
        "reverse_margin": -35.588235
      },
      "new": "009dd710",
      "score": 16.558824
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-610807cddfd88e3950f33948ccf3a976"></a>

### v16.0.0 [`0081d3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d3cc.md) FUN_0081d3cc

`competing_candidates` 

呼出元 1件 [`0081d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d4c8.md) · 呼出先 3件 [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007cedc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cedc4.md) · スコア 14.285714 · 採用条件未達 · 順位差 -43.345865 / 0.9523810000000008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0069ece4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ece4.md) · スコア 13.333333 · 採用条件未達 · 順位差 -59.607843 / -0.9523810000000008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0073a088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a088.md) · スコア 13.333333 · 採用条件未達 · 順位差 -63.13725500000001 / -0.9523810000000008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0073a110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a110.md) · スコア 13.333333 · 採用条件未達 · 順位差 -63.13725500000001 / -0.9523810000000008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`009dbaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009dbaf8.md) · スコア 9.52381 · 採用条件未達 · 順位差 9.52381 / -4.761904000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007eb404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb404.md) · スコア 8.571429 · 採用条件未達 · 順位差 -14.047619 / -5.714285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008577f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md) · スコア 8.571429 · 採用条件未達 · 順位差 8.571429 / -5.714285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00857d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md) · スコア 8.571429 · 採用条件未達 · 順位差 8.571429 / -5.714285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.19047619047619047
        ],
        "cfg_coverage": [
          0.15789473684210525,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -43.345865,
        "reverse_margin": 0.9523810000000008
      },
      "new": "007cedc4",
      "score": 14.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3235294117647059,
          0.1746031746031746
        ],
        "cfg_coverage": [
          0.17647058823529413,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -59.607843,
        "reverse_margin": -0.9523810000000008
      },
      "new": "0069ece4",
      "score": 13.333333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3235294117647059,
          0.1746031746031746
        ],
        "cfg_coverage": [
          0.17647058823529413,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -63.13725500000001,
        "reverse_margin": -0.9523810000000008
      },
      "new": "0073a088",
      "score": 13.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-91d45bce4d8e6c108dffafb757429916"></a>

### v16.0.0 [`0081d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d4c8.md) FUN_0081d4c8

`competing_candidates` 

呼出元 4件 [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) [`008332d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008332d4.md) [`00833684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/00833684.md) [`008339fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00833/008339fc.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0081d3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d3cc.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007e8a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e8a54.md) · スコア 17.940467 · 採用条件未達 · 順位差 14.277649000000002 / 14.106029000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007e1484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e1/007e1484.md) · スコア 3.834438 · 採用条件未達 · 順位差 -57.643601000000004 / -14.106029000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005c1ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1ab0.md) · スコア 3.197007 · 採用条件未達 · 順位差 -1.686249 / -14.743460000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00617dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/00617dec.md) · スコア 2.299252 · 採用条件未達 · 順位差 -57.112513 / -15.641215000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007eca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007eca30.md) · スコア 2.011739 · 採用条件未達 · 順位差 -7.292456999999999 / -15.928728000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005a18e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a18e0.md) · スコア 2.0 · 採用条件未達 · 順位差 -23.917151 / -15.940467000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00644304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644304.md) · スコア 2.0 · 採用条件未達 · 順位差 -4.459459 / -15.940467000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0066341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066341c.md) · スコア 2.0 · 採用条件未達 · 順位差 -5.206478 / -15.940467000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22863741339491916,
          0.24688279301745636
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.13414634146341464
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.277649000000002,
        "reverse_margin": 14.106029000000001
      },
      "new": "007e8a54",
      "score": 17.940467
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04090909090909091,
          0.022443890274314215
        ],
        "cfg_coverage": [
          0.045454545454545456,
          0.024390243902439025
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -57.643601000000004,
        "reverse_margin": -14.106029000000001
      },
      "new": "007e1484",
      "score": 3.834438
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05925925925925926,
          0.0199501246882793
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
        "margin": -1.686249,
        "reverse_margin": -14.743460000000002
      },
      "new": "005c1ab0",
      "score": 3.197007
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-208eba9975b8b5dcbb6e09d423609c0a"></a>

### v16.0.0 [`0081db0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081db0c.md) FUN_0081db0c

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00822474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822474.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00a7840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a7840c.md) · スコア 6.883913 · 採用条件未達 · 順位差 -34.637214 / 0.5160819999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ac574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007ac574.md) · スコア 6.367831 · 採用条件未達 · 順位差 -68.31509600000001 / -0.5160819999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) · スコア 5.219512 · 採用条件未達 · 順位差 -65.18371400000001 / -1.6644009999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a25500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25500.md) · スコア 5.1971 · 採用条件未達 · 順位差 -0.028706000000000564 / -1.686813 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005a3cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3cbc.md) · スコア 4.926829 · 採用条件未達 · 順位差 -45.066172 / -1.957084 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f5624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5624.md) · スコア 4.323006 · 採用条件未達 · 順位差 -27.414494 / -2.5609069999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0070c1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070c1ac.md) · スコア 4.061069 · 採用条件未達 · 順位差 -5.496183 / -2.822844 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00644984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644984.md) · スコア 3.756098 · 採用条件未達 · 順位差 -9.492688000000001 / -3.1278149999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07868852459016394,
          0.11707317073170732
        ],
        "cfg_coverage": [
          0.008130081300813009,
          0.013513513513513514
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.637214,
        "reverse_margin": 0.5160819999999999
      },
      "new": "00a7840c",
      "score": 6.883913
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11382113821138211,
          0.06829268292682927
        ],
        "cfg_coverage": [
          0.02040816326530612,
          0.013513513513513514
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -68.31509600000001,
        "reverse_margin": -0.5160819999999999
      },
      "new": "007ac574",
      "score": 6.367831
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11827956989247312,
          0.05365853658536585
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
        "margin": -65.18371400000001,
        "reverse_margin": -1.6644009999999998
      },
      "new": "007eafa4",
      "score": 5.219512
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8ed7a8c7831bddb39afcddb0223441de"></a>

### v16.0.0 [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) FUN_0081de40

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`00664a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a4c.md)

- 1. [`007e9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e9/007e9118.md) · スコア 57.164718 · 採用条件未達 · 順位差 52.114265 / 52.393319 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a29a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29a48.md) · スコア 4.771399 · 採用条件未達 · 順位差 -49.415439 / -52.393319 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00a60644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) · スコア 4.529471 · 採用条件未達 · 順位差 -0.7173689999999997 / -52.635247 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · スコア 4.359704 · 採用条件未達 · 順位差 -36.500037999999996 / -52.805014 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · スコア 4.175482 · 採用条件未達 · 順位差 -25.403028000000003 / -52.989236 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`009e44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md) · スコア 4.0 · 採用条件未達 · 順位差 0.6233270000000002 / -53.164718 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 7. [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) · スコア 3.394605 · 採用条件未達 · 順位差 -41.532795 / -53.770113 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) · スコア 3.060575 · 採用条件未達 · 順位差 -33.392276 / -54.104143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7217391304347827,
          0.7047952047952047
        ],
        "cfg_coverage": [
          0.44385026737967914,
          0.4643356643356643
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 52.114265,
        "reverse_margin": 52.393319
      },
      "new": "007e9118",
      "score": 57.164718
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013804527885146328,
          0.012487512487512488
        ],
        "cfg_coverage": [
          0.0011074197120708748,
          0.0013986013986013986
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -49.415439,
        "reverse_margin": -52.393319
      },
      "new": "00a29a48",
      "score": 4.771399
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.016905071521456438,
          0.006493506493506494
        ],
        "cfg_coverage": [
          0.015527950310559006,
          0.006993006993006993
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -0.7173689999999997,
        "reverse_margin": -52.635247
      },
      "new": "00a60644",
      "score": 4.529471
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a04370747098daec1e0822cc980ce0df"></a>

### v16.0.0 [`0081fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081f/0081fd88.md) FUN_0081fd88

`competing_candidates` 

呼出元 4件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) [`008312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b4.md) [`00832094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00832/00832094.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e92c.md) [`00819f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00819/00819f5c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007eafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ea/007eafa4.md) · スコア 70.403226 · 採用条件未達 · 順位差 53.862785 / 54.475357 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a0c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c7dc.md) · スコア 15.927869 · 採用条件未達 · 順位差 -5.593442000000001 / -54.475357 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a09778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09778.md) · スコア 14.073733 · 採用条件未達 · 順位差 -31.62212 / -56.329493 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00905fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905fb0.md) · スコア 13.864919 · 採用条件未達 · 順位差 11.738869000000001 / -56.538307 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0090392c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/0090392c.md) · スコア 12.807988 · 採用条件未達 · 順位差 10.682202 / -57.595238 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a0ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0ae20.md) · スコア 10.863636 · 採用条件未達 · 順位差 -1.125 / -59.539590000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) · スコア 9.875 · 採用条件未達 · 順位差 -31.814441000000002 / -60.528226000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006425d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md) · スコア 9.451613 · 採用条件未達 · 順位差 -29.629132 / -60.951613 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8817204301075269,
          0.8817204301075269
        ],
        "cfg_coverage": [
          0.8157894736842105,
          0.775
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 53.862785,
        "reverse_margin": 54.475357
      },
      "new": "007eafa4",
      "score": 70.403226
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1721311475409836,
          0.22580645161290322
        ],
        "cfg_coverage": [
          0.18,
          0.225
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -5.593442000000001,
        "reverse_margin": -54.475357
      },
      "new": "00a0c7dc",
      "score": 15.927869
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19047619047619047,
          0.21505376344086022
        ],
        "cfg_coverage": [
          0.03225806451612903,
          0.05
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.62212,
        "reverse_margin": -56.329493
      },
      "new": "00a09778",
      "score": 14.073733
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1f3b7e7c73b46340ece317551664ef83"></a>

### v16.0.0 [`0081fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081f/0081fefc.md) FUN_0081fefc

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007eb118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb118.md) · スコア 64.632807 · 採用条件未達 · 順位差 45.463280999999995 / 44.186685 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a60478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md) · スコア 20.446122 · 採用条件未達 · 順位差 11.619143 / -44.186685 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00678588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678588.md) · スコア 13.608247 · 採用条件未達 · 順位差 6.335520000000001 / -51.02456 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00644c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644c1c.md) · スコア 10.851064 · 採用条件未達 · 順位差 6.647241999999999 / -53.781743 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · スコア 8.4994 · 採用条件未達 · 順位差 -54.480191999999995 / -56.133407 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f00b0.md) · スコア 6.845638 · 採用条件未達 · 順位差 -13.246243999999997 / -57.787169 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0059cce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059cce0.md) · スコア 3.546349 · 採用条件未達 · 順位差 -3.7454539999999996 / -61.086458 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00660120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660120.md) · スコア 3.528191 · 採用条件未達 · 順位差 -17.387063 / -61.104616 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8191489361702128,
          0.8191489361702128
        ],
        "cfg_coverage": [
          0.7741935483870968,
          0.7741935483870968
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 45.463280999999995,
        "reverse_margin": 44.186685
      },
      "new": "007eb118",
      "score": 64.632807
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32954545454545453,
          0.30851063829787234
        ],
        "cfg_coverage": [
          0.13043478260869565,
          0.0967741935483871
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 11.619143,
        "reverse_margin": -44.186685
      },
      "new": "00a60478",
      "score": 20.446122
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2268041237113402,
          0.23404255319148937
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
        "margin": 6.335520000000001,
        "reverse_margin": -51.02456
      },
      "new": "00678588",
      "score": 13.608247
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b74a62e3a586a5ef6bbf5dc54a737720"></a>

### v16.0.0 [`00820074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820074.md) FUN_00820074

`competing_candidates` 

呼出元 4件 [`0061706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md) [`0061e428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e428.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 5件 [`00816058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816058.md) [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007eb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb290.md) · スコア 64.276069 · 採用条件未達 · 順位差 48.58214600000001 / 48.446014000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004f6b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md) · スコア 15.830055 · 採用条件未達 · 順位差 6.739146 / -48.446014000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`004f6c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md) · スコア 15.830055 · 採用条件未達 · 順位差 6.739146 / -48.446014000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00721864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721864.md) · スコア 12.903226 · 採用条件未達 · 順位差 -16.620584 / -51.372843 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a600fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md) · スコア 11.29819 · 採用条件未達 · 順位差 -11.668562 / -52.97787900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004dc168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc168.md) · スコア 10.668765 · 採用条件未達 · 順位差 6.053380000000001 / -53.607304000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00adf924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf924.md) · スコア 10.668765 · 採用条件未達 · 順位差 -3.255476999999999 / -53.607304000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00749214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749214.md) · スコア 10.322581 · 採用条件未達 · 順位差 -4.915514 / -53.95348800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8387096774193549,
          0.8387096774193549
        ],
        "cfg_coverage": [
          0.6976744186046512,
          0.7317073170731707
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 48.58214600000001,
        "reverse_margin": 48.446014000000005
      },
      "new": "007eb290",
      "score": 64.276069
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4166666666666667,
          0.21505376344086022
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.14634146341463414
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.739146,
        "reverse_margin": -48.446014000000005
      },
      "new": "004f6b24",
      "score": 15.830055
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4166666666666667,
          0.21505376344086022
        ],
        "cfg_coverage": [
          0.42857142857142855,
          0.14634146341463414
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.739146,
        "reverse_margin": -48.446014000000005
      },
      "new": "004f6c0c",
      "score": 15.830055
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3a64947103a65bf170ff91440615e2d9"></a>

### v16.0.0 [`00820258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820258.md) FUN_00820258

`competing_candidates` 

呼出元 1件 [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00448fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md)

- 1. [`007eb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb474.md) · スコア 71.037344 · 採用条件未達 · 順位差 66.22919900000001 / 66.22919900000001 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007d47a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d47a4.md) · スコア 4.808145 · 採用条件未達 · 順位差 -53.723324000000005 / -66.22919900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0042a40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a40c.md) · スコア 4.438551 · 採用条件未達 · 順位差 -2.879631 / -66.598793 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004e21a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md) · スコア 3.983402 · 採用条件未達 · 順位差 -1.093521 / -67.053942 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004ab3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab3f4.md) · スコア 3.940625 · 採用条件未達 · 順位差 -2.697909 / -67.09671900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007bfd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfd30.md) · スコア 3.236515 · 採用条件未達 · 順位差 -5.866031 / -67.80082900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) · スコア 3.193737 · 採用条件未達 · 順位差 -4.9000129999999995 / -67.843607 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · スコア 2.901998 · 採用条件未達 · 順位差 -60.077594 / -68.135346 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8506224066390041,
          0.8506224066390041
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
        "margin": 66.22919900000001,
        "reverse_margin": 66.22919900000001
      },
      "new": "007eb474",
      "score": 71.037344
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24242424242424243,
          0.06639004149377593
        ],
        "cfg_coverage": [
          0.15384615384615385,
          0.041237113402061855
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.723324000000005,
        "reverse_margin": -66.22919900000001
      },
      "new": "007d47a4",
      "score": 4.808145
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12878787878787878,
          0.07053941908713693
        ],
        "cfg_coverage": [
          0.04,
          0.010309278350515464
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.879631,
        "reverse_margin": -66.598793
      },
      "new": "0042a40c",
      "score": 4.438551
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9991f168867f3a4474f0cb6b758e5b35"></a>

### v16.0.0 [`00821814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821814.md) FUN_00821814

`competing_candidates` 

呼出元 1件 [`00821cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821cc0.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00821b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821b84.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007eca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007eca30.md) · スコア 9.304196 · 採用条件未達 · 順位差 4.694716999999999 / 2.2307689999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006b2318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md) · スコア 7.073427 · 採用条件未達 · 順位差 -1.4305760000000012 / -2.2307689999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a5ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ee5c.md) · スコア 5.902098 · 採用条件未達 · 順位差 -57.695291999999995 / -3.4020979999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00901b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/00901b88.md) · スコア 5.181818 · 採用条件未達 · 順位差 5.181818 / -4.122377999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009d0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0a60.md) · スコア 4.748252 · 採用条件未達 · 順位差 -5.831058 / -4.555943999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009d0ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0ce8.md) · スコア 4.748252 · 採用条件未達 · 順位差 -5.431057999999999 / -4.555943999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007f6f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6f30.md) · スコア 4.426573 · 採用条件未達 · 順位差 -60.214954999999996 / -4.877622999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008d95dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d9/008d95dc.md) · スコア 4.311741 · 採用条件未達 · 順位差 -51.928354 / -4.992455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17679558011049723,
          0.14545454545454545
        ],
        "cfg_coverage": [
          0.031578947368421054,
          0.028846153846153848
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.694716999999999,
        "reverse_margin": 2.2307689999999996
      },
      "new": "007eca30",
      "score": 9.304196
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11475409836065574,
          0.09545454545454546
        ],
        "cfg_coverage": [
          0.08139534883720931,
          0.0673076923076923
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -1.4305760000000012,
        "reverse_margin": -2.2307689999999996
      },
      "new": "006b2318",
      "score": 7.073427
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10810810810810811,
          0.07272727272727272
        ],
        "cfg_coverage": [
          0.14035087719298245,
          0.07692307692307693
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -57.695291999999995,
        "reverse_margin": -3.4020979999999996
      },
      "new": "00a5ee5c",
      "score": 5.902098
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-79f9f5eb338e26065a911a3182c2663c"></a>

### v16.0.0 [`00821b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821b84.md) FUN_00821b84

`competing_candidates` 

呼出元 1件 [`00821814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821814.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

- 1. [`00a1bb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1b/00a1bb28.md) · スコア 74.285714 · 採用条件未達 · 順位差 32.307691999999996 / 5.714285000000004 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007f1950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1950.md) · スコア 68.571429 · 採用条件未達 · 順位差 -5.714285000000004 / -5.714285000000004 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`006b66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md) · スコア 65.714286 · 採用条件未達 · 順位差 12.307693 / -8.571427999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007493d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/007493d8.md) · スコア 45.47619 · 採用条件未達 · 順位差 -3.5347989999999996 / -28.809523999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0065064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/0065064c.md) · スコア 35.809524 · 採用条件未達 · 順位差 15.333334000000004 / -38.476189999999995 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a44bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md) · スコア 32.380952 · 採用条件未達 · 順位差 6.761904000000001 / -41.904762 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a0b6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md) · スコア 15.0 · 採用条件未達 · 順位差 -8.611111000000001 / -59.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a0b760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md) · スコア 12.97619 · 採用条件未達 · 順位差 1.5 / -61.309523999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 32.307691999999996,
        "reverse_margin": 5.714285000000004
      },
      "new": "00a1bb28",
      "score": 74.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8095238095238095,
          0.8095238095238095
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
        "margin": -5.714285000000004,
        "reverse_margin": -5.714285000000004
      },
      "new": "007f1950",
      "score": 68.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7619047619047619,
          0.7619047619047619
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
        "margin": 12.307693,
        "reverse_margin": -8.571427999999997
      },
      "new": "006b66b0",
      "score": 65.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-87ccf1113b89eef1f638b0073f00dccc"></a>

### v16.0.0 [`00821bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821bd8.md) FUN_00821bd8

`competing_candidates` 

呼出元 1件 [`00821cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821cc0.md) · 呼出先 0件 

- 1. [`007ecd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecd04.md) · スコア 80.0 · 採用条件未達 · 順位差 63.949843 / 63.949843 · insufficient_independent_call_anchors
- 2. [`007e84bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e84bc.md) · スコア 16.050157 · 採用条件未達 · 順位差 -6.54917 / -63.949843 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007cefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cefe0.md) · スコア 10.094044 · 採用条件未達 · 順位差 -63.360501 / -69.905956 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0069b9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069b9e4.md) · スコア 9.916405 · 採用条件未達 · 順位差 0.09497599999999906 / -70.083595 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00731710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/00731710.md) · スコア 9.059561 · 採用条件未達 · 順位差 -36.940439 / -70.940439 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007eb404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb404.md) · スコア 6.812957 · 採用条件未達 · 順位差 -15.806090999999999 / -73.187043 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`009e4ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4ef4.md) · スコア 6.812957 · 採用条件未達 · 順位差 -26.052539999999997 / -73.187043 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00afcdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md) · スコア 5.172414 · 採用条件未達 · 順位差 -2.327586 / -74.827586 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 63.949843,
        "reverse_margin": 63.949843
      },
      "new": "007ecd04",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3,
          0.20689655172413793
        ],
        "cfg_coverage": [
          0.3,
          0.18181818181818182
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -6.54917,
        "reverse_margin": -63.949843
      },
      "new": "007e84bc",
      "score": 16.050157
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14545454545454545,
          0.13793103448275862
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.09090909090909091
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -63.360501,
        "reverse_margin": -69.905956
      },
      "new": "007cefe0",
      "score": 10.094044
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9dd532e92392c9610b5aa68d3999ace2"></a>

### v16.0.0 [`00821cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821cc0.md) FUN_00821cc0

`competing_candidates` 

呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00821814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821814.md) [`00821bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821bd8.md)

- 1. [`007ecdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecdec.md) · スコア 15.967467 · 採用条件未達 · 順位差 0.7682759999999984 / 4.006297 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ecd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecd04.md) · スコア 11.96117 · 採用条件未達 · 順位差 -68.03883 / -4.006297 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007cefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cefe0.md) · スコア 10.830382 · 採用条件未達 · 順位差 -62.624162999999996 / -5.137084999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006b2318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md) · スコア 8.417842 · 採用条件未達 · 順位差 -0.0861610000000006 / -7.549624999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0061bddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061b/0061bddc.md) · スコア 7.220254 · 採用条件未達 · 順位差 -48.420051 / -8.747212999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006050b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006050b4.md) · スコア 6.459193 · 採用条件未達 · 順位差 -3.356371 / -9.508274 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00aa9300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9300.md) · スコア 5.554244 · 採用条件未達 · 順位差 -60.86085 / -10.413222999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00661498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/00661498.md) · スコア 5.058376 · 採用条件未達 · 順位差 -11.192336000000001 / -10.909091 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3972602739726027,
          0.2396694214876033
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.07936507936507936
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.7682759999999984,
        "reverse_margin": 4.006297
      },
      "new": "007ecdec",
      "score": 15.967467
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3275862068965517,
          0.15702479338842976
        ],
        "cfg_coverage": [
          0.24242424242424243,
          0.12698412698412698
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -68.03883,
        "reverse_margin": -4.006297
      },
      "new": "007ecd04",
      "score": 11.96117
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32727272727272727,
          0.1487603305785124
        ],
        "cfg_coverage": [
          0.2222222222222222,
          0.09523809523809523
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -62.624162999999996,
        "reverse_margin": -5.137084999999999
      },
      "new": "007cefe0",
      "score": 10.830382
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00821ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00821/00821ea4.md) FUN_00821ea4

`competing_candidates` 

呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007ecf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecf10.md) · スコア 61.197264 · 採用条件未達 · 順位差 54.013439 / 55.545375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) · スコア 5.651889 · 採用条件未達 · 順位差 -2.4418610000000003 / -55.545375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) · スコア 5.585534 · 採用条件未達 · 順位差 -0.06479700000000044 / -55.611729999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`00601cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601cfc.md) · スコア 5.290323 · 採用条件未達 · 順位差 -50.638109 / -55.906940999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`006f2878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2878.md) · スコア 4.806452 · 採用条件未達 · 順位差 -15.60755 / -56.390812 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`007c3050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c3/007c3050.md) · スコア 4.806452 · 採用条件未達 · 順位差 -33.027735 / -56.390812 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`0061b64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061b/0061b64c.md) · スコア 4.738485 · 採用条件未達 · 順位差 -10.433868 / -56.458779 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) · スコア 4.736196 · 採用条件未達 · 順位差 0.12269899999999989 / -56.461068 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.782258064516129,
          0.782258064516129
        ],
        "cfg_coverage": [
          0.5130890052356021,
          0.5240641711229946
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 54.013439,
        "reverse_margin": 55.545375
      },
      "new": "007ecf10",
      "score": 61.197264
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.140625,
          0.04838709677419355
        ],
        "cfg_coverage": [
          0.12280701754385964,
          0.0374331550802139
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.4418610000000003,
        "reverse_margin": -55.545375
      },
      "new": "00a0801c",
      "score": 5.651889
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02304147465437788,
          0.026881720430107527
        ],
        "cfg_coverage": [
          0.01015228426395939,
          0.0106951871657754
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -0.06479700000000044,
        "reverse_margin": -55.611729999999994
      },
      "new": "0070cadc",
      "score": 5.585534
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3214ab2967b85c00b514d850ff5c2ad3"></a>

### v16.0.0 [`00822474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822474.md) FUN_00822474

`competing_candidates` 

呼出元 2件 [`0081db0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081db0c.md) [`00822474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822474.md) · 呼出先 8件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00808a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00808/00808a3c.md) [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md)

- 1. [`007ed4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed4e0.md) · スコア 56.372322 · 採用条件未達 · 順位差 48.228775 / 48.993680999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed98c.md) · スコア 7.378641 · 採用条件未達 · 順位差 -49.604091 / -48.993680999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00663c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663c44.md) · スコア 3.347046 · 採用条件未達 · 順位差 -66.04762699999999 / -53.025276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006b5e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md) · スコア 2.524272 · 採用条件未達 · 順位差 -13.479154999999999 / -53.84805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006d6364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6364.md) · スコア 2.330097 · 採用条件未達 · 順位差 -4.041584 / -54.042224999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00803d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00803/00803d90.md) · スコア 1.941748 · 採用条件未達 · 順位差 -3.562839 / -54.430574 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0090596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/0090596c.md) · スコア 1.698206 · 採用条件未達 · 順位差 -14.418911 / -54.674116 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007cee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cee54.md) · スコア 1.504032 · 採用条件未達 · 順位差 -74.253544 / -54.868289999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7959866220735786,
          0.7702265372168284
        ],
        "cfg_coverage": [
          0.5079365079365079,
          0.5423728813559322
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 48.228775,
        "reverse_margin": 48.993680999999995
      },
      "new": "007ed4e0",
      "score": 56.372322
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19387755102040816,
          0.12297734627831715
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
        "margin": -49.604091,
        "reverse_margin": -48.993680999999995
      },
      "new": "007ed98c",
      "score": 7.378641
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1,
          0.038834951456310676
        ],
        "cfg_coverage": [
          0.10526315789473684,
          0.05084745762711865
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -66.04762699999999,
        "reverse_margin": -53.025276
      },
      "new": "00663c44",
      "score": 3.347046
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cc909461cabf345397547ef6514382a4"></a>

### v16.0.0 [`00822948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822948.md) FUN_00822948

`competing_candidates` 

呼出元 1件 [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) · 呼出先 4件 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)

- 1. [`007ed98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed98c.md) · スコア 56.982732 · 採用条件未達 · 順位差 49.604091 / 48.839185 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ed4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007ed4e0.md) · スコア 8.143547 · 採用条件未達 · 順位差 -48.228775 / -48.839185 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006fdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdd28.md) · スコア 4.285714 · 採用条件未達 · 順位差 -64.148021 / -52.697018 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006fde74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fde74.md) · スコア 4.285714 · 採用条件未達 · 順位差 -31.798623 / -52.697018 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007cefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cefe0.md) · スコア 3.716962 · 採用条件未達 · 順位差 -69.737583 / -53.265769999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007ecd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecd04.md) · スコア 3.41084 · 採用条件未達 · 順位差 -76.58916 / -53.571892 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006fdbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · スコア 2.755102 · 採用条件未達 · 順位差 -45.74435 / -54.22763 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f5624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5624.md) · スコア 2.164604 · 採用条件未達 · 順位差 -29.572896 / -54.818128 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8061224489795918,
          0.8061224489795918
        ],
        "cfg_coverage": [
          0.4307692307692308,
          0.45901639344262296
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.604091,
        "reverse_margin": 48.839185
      },
      "new": "007ed98c",
      "score": 56.982732
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13043478260869565,
          0.1989795918367347
        ],
        "cfg_coverage": [
          0.015873015873015872,
          0.03278688524590164
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -48.228775,
        "reverse_margin": -48.839185
      },
      "new": "007ed4e0",
      "score": 8.143547
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1686746987951807,
          0.07142857142857142
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
        "margin": -64.148021,
        "reverse_margin": -52.697018
      },
      "new": "006fdd28",
      "score": 4.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7fedff5530ba8921e0a2f88dc4406eb"></a>

### v16.0.0 [`00822c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822c58.md) FUN_00822c58

`competing_candidates` 

呼出元 2件 [`0081de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081de40.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 5件 [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007edc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007edc9c.md) · スコア 63.52415 · 採用条件未達 · 順位差 55.849731 / 55.849731 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008336f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/008336f0.md) · スコア 7.674419 · 採用条件未達 · 順位差 -9.47155 / -55.849731 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00858c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858c14.md) · スコア 7.674419 · 採用条件未達 · 順位差 -3.7852759999999996 / -55.849731 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a3c714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c714.md) · スコア 7.674419 · 採用条件未達 · 順位差 -3.719916999999999 / -55.849731 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0042d084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d084.md) · スコア 6.990291 · 採用条件未達 · 順位差 3.3416420000000002 / -56.533859 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) · スコア 6.804124 · 採用条件未達 · 順位差 -2.5420300000000005 / -56.720026 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004d9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md) · スコア 6.226415 · 採用条件未達 · 順位差 3.9622640000000002 / -57.297734999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0064104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/0064104c.md) · スコア 6.206897 · 採用条件未達 · 順位差 -17.695923999999998 / -57.317253 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8023255813953488,
          0.8023255813953488
        ],
        "cfg_coverage": [
          0.7692307692307693,
          0.8333333333333334
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 55.849731,
        "reverse_margin": 55.849731
      },
      "new": "007edc9c",
      "score": 63.52415
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12941176470588237,
          0.12790697674418605
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
        "margin": -9.47155,
        "reverse_margin": -55.849731
      },
      "new": "008336f0",
      "score": 7.674419
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.171875,
          0.12790697674418605
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
        "margin": -3.7852759999999996,
        "reverse_margin": -55.849731
      },
      "new": "00858c14",
      "score": 7.674419
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4f38062dd77c48f8767a9484bb0dc71c"></a>

### v16.0.0 [`00822ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822ef0.md) FUN_00822ef0

`competing_candidates` 

呼出元 1件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0081c7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c7b4.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

- 1. [`007ee6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ee/007ee6d0.md) · スコア 0.4847 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007ee6d0",
      "score": 0.4847
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e619dda07e712db71195ca6fe2c6988c"></a>

### v16.0.0 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) FUN_00822fd0

`competing_candidates` 

呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md) [`0082ebd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ebd4.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`00818d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00818/00818d00.md)

- 1. [`007edf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007edf34.md) · スコア 28.572725 · 採用条件未達 · 順位差 24.528388999999997 / 22.870929999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0070c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070c5c4.md) · スコア 5.701795 · 採用条件未達 · 順位差 -1.3530950000000006 / -22.870929999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · スコア 5.501432 · 採用条件未達 · 順位差 2.8076770000000004 / -23.071292999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007ee6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ee/007ee6d0.md) · スコア 3.617399 · 採用条件未達 · 順位差 -76.124009 / -24.955326 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0070cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070cadc.md) · スコア 3.481209 · 採用条件未達 · 順位差 -2.169122 / -25.091516 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006b5918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md) · スコア 2.978064 · 採用条件未達 · 順位差 -4.54241 / -25.594661 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005708ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005708ec.md) · スコア 2.754717 · 採用条件未達 · 順位差 0.06821799999999989 / -25.818008 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00649518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md) · スコア 2.515723 · 採用条件未達 · 順位差 -1.1679500000000003 / -26.057001999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3895216400911162,
          0.3584905660377358
        ],
        "cfg_coverage": [
          0.25316455696202533,
          0.2926829268292683
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.528388999999997,
        "reverse_margin": 22.870929999999998
      },
      "new": "007edf34",
      "score": 28.572725
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0736196319018405,
          0.050314465408805034
        ],
        "cfg_coverage": [
          0.046357615894039736,
          0.03414634146341464
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -1.3530950000000006,
        "reverse_margin": -22.870929999999998
      },
      "new": "0070c5c4",
      "score": 5.701795
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.040257648953301126,
          0.05241090146750524
        ],
        "cfg_coverage": [
          0.05429864253393665,
          0.05853658536585366
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 2.8076770000000004,
        "reverse_margin": -23.071292999999997
      },
      "new": "00508860",
      "score": 5.501432
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f62444e934fe2052cf3990928c7a3fc4"></a>

### v16.0.0 [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) FUN_00823820

`competing_candidates` 

呼出元 2件 [`00784414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784414.md) [`0082eab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eab8.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00816af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816af0.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007ee6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ee/007ee6d0.md) · スコア 79.741408 · 採用条件未達 · 順位差 76.124009 / 76.124009 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007edf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ed/007edf34.md) · スコア 3.617399 · 採用条件未達 · 順位差 -24.955326 / -76.124009 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008c8b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8b30.md) · スコア 3.3228 · 採用条件未達 · 順位差 0.9497429999999998 / -76.418608 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006b2318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md) · スコア 2.831802 · 採用条件未達 · 順位差 -5.672201000000001 / -76.90960600000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007e228c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e2/007e228c.md) · スコア 2.687398 · 採用条件未達 · 順位差 -47.766985 / -77.05401 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0070e66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070e66c.md) · スコア 2.589198 · 採用条件未達 · 順位差 -3.5755649999999997 / -77.15221000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00617724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/00617724.md) · スコア 2.392799 · 採用条件未達 · 順位差 -6.330093 / -77.34860900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0067eb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067e/0067eb40.md) · スコア 2.196399 · 採用条件未達 · 順位差 -5.005863 / -77.54500900000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9623567921440261,
          0.9623567921440261
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
        "margin": 76.124009,
        "reverse_margin": 76.124009
      },
      "new": "007ee6d0",
      "score": 79.741408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03416856492027335,
          0.024549918166939442
        ],
        "cfg_coverage": [
          0.008438818565400843,
          0.007220216606498195
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.955326,
        "reverse_margin": -76.124009
      },
      "new": "007edf34",
      "score": 3.617399
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04316546762589928,
          0.019639934533551555
        ],
        "cfg_coverage": [
          0.02247191011235955,
          0.007220216606498195
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.9497429999999998,
        "reverse_margin": -76.418608
      },
      "new": "008c8b30",
      "score": 3.3228
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b6097e3e27817bf40de0795b7a4d2965"></a>

### v16.0.0 [`008241d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008241d8.md) FUN_008241d8

`competing_candidates` 

呼出元 1件 [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

- 1. [`007ef088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef088.md) · スコア 68.285714 · 採用条件未達 · 順位差 56.857143 / 56.857143 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007d2db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2db4.md) · スコア 11.428571 · 採用条件未達 · 順位差 -48.753247 / -56.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007d2e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2e90.md) · スコア 11.428571 · 採用条件未達 · 順位差 -48.753247 / -56.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007d2f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2f6c.md) · スコア 11.428571 · 採用条件未達 · 順位差 -52.025974000000005 / -56.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007d3048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d3/007d3048.md) · スコア 11.428571 · 採用条件未達 · 順位差 -52.025974000000005 / -56.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007d3124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d3/007d3124.md) · スコア 11.428571 · 採用条件未達 · 順位差 -53.116884000000006 / -56.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007cffdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cffdc.md) · スコア 10.571429 · 採用条件未達 · 順位差 -55.69086599999999 / -57.714285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007d3200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d3/007d3200.md) · スコア 5.697581 · 採用条件未達 · 順位差 -40.882643 / -62.588133 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7714285714285715,
          0.7714285714285715
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
        "margin": 56.857143,
        "reverse_margin": 56.857143
      },
      "new": "007ef088",
      "score": 68.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.15714285714285714
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
        "margin": -48.753247,
        "reverse_margin": -56.857143
      },
      "new": "007d2db4",
      "score": 11.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.15714285714285714
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
        "margin": -48.753247,
        "reverse_margin": -56.857143
      },
      "new": "007d2e90",
      "score": 11.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9e5d0b8b2eacda0bf4714de07948be52"></a>

### v16.0.0 [`008242f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md) FUN_008242f0

`competing_candidates` 

呼出元 1件 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) · 呼出先 2件 [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007ef1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef1a0.md) · スコア 53.084112 · 採用条件未達 · 順位差 50.841121 / 16.261682 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007ef34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef34c.md) · スコア 36.82243 · 採用条件未達 · 順位差 31.053198999999996 / -16.261682 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5514018691588785,
          0.5514018691588785
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
        "margin": 50.841121,
        "reverse_margin": 16.261682
      },
      "new": "007ef1a0",
      "score": 53.084112
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28846153846153844,
          0.2803738317757009
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
        "margin": 31.053198999999996,
        "reverse_margin": -16.261682
      },
      "new": "007ef34c",
      "score": 36.82243
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-54f440549779c5aeb54370b1cbfa229b"></a>

### v16.0.0 [`0082449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md) FUN_0082449c

`competing_candidates` 

呼出元 1件 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) · 呼出先 2件 [`0080234c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/0080234c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007ef34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef34c.md) · スコア 5.769231 · 採用条件未達 · 順位差 -31.053198999999996 / 3.5262400000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ef1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef1a0.md) · スコア 2.242991 · 採用条件未達 · 順位差 -50.841121 / -3.5262400000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09615384615384616,
          0.09615384615384616
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
        "margin": -31.053198999999996,
        "reverse_margin": 3.5262400000000005
      },
      "new": "007ef34c",
      "score": 5.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.037383177570093455,
          0.038461538461538464
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
        "margin": -50.841121,
        "reverse_margin": -3.5262400000000005
      },
      "new": "007ef1a0",
      "score": 2.242991
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-43c803fe17fc831b7dcb1dc908f827a1"></a>

### v16.0.0 [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) FUN_0082463c

`competing_candidates` 

呼出元 1件 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)

- 1. [`007ef4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ef/007ef4ec.md) · スコア 25.332587 · 採用条件未達 · 順位差 21.073576 / 20.959562 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · スコア 4.373025 · 採用条件未達 · 順位差 -36.486717 / -20.959562 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · スコア 4.161257 · 採用条件未達 · 順位差 -25.417253000000002 / -21.17133 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) · スコア 2.020033 · 採用条件未達 · 順位差 -31.61442 / -23.312554 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00726b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00726/00726b58.md) · スコア 0.201089 · 採用条件未達 · 順位差 -34.597317999999994 / -25.131498 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0063a620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md) · スコア 0.150817 · 採用条件未達 · 順位差 -2.389043 / -25.18177 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3376681614349776,
          0.3154587348135735
        ],
        "cfg_coverage": [
          0.12566137566137567,
          0.12025316455696203
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 21.073576,
        "reverse_margin": 20.959562
      },
      "new": "007ef4ec",
      "score": 25.332587
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.005772646536412078,
          0.010892333472978634
        ],
        "cfg_coverage": [
          0.0013333333333333333,
          0.002531645569620253
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -36.486717,
        "reverse_margin": -20.959562
      },
      "new": "0086b704",
      "score": 4.373025
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0026876162910895183,
          0.005446166736489317
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
        "margin": -25.417253000000002,
        "reverse_margin": -21.17133
      },
      "new": "0073496c",
      "score": 4.161257
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00826d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d28.md) FUN_00826d28

`competing_candidates` 

呼出元 1件 [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

- 1. [`007f1950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1950.md) · スコア 56.263736 · 採用条件未達 · 順位差 -18.021977999999997 / 2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006b66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md) · スコア 53.406593 · 採用条件未達 · 順位差 -12.307693 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007493d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/007493d8.md) · スコア 49.010989 · 採用条件未達 · 順位差 3.5347989999999996 / -7.252746999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a1bb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1b/00a1bb28.md) · スコア 41.978022 · 採用条件未達 · 順位差 -32.307691999999996 / -14.285713999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00656404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656404.md) · スコア 29.010989 · 採用条件未達 · 順位差 15.783715999999998 / -27.252747000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008f4f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f4/008f4f74.md) · スコア 27.252747 · 採用条件未達 · 順位差 27.252747 / -29.010989000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a44bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md) · スコア 25.619048 · 採用条件未達 · 順位差 -6.761904000000001 / -30.644688000000002 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a0b6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md) · スコア 23.611111 · 採用条件未達 · 順位差 8.611111000000001 / -32.652625 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8095238095238095,
          0.8095238095238095
        ],
        "cfg_coverage": [
          0.45454545454545453,
          0.38461538461538464
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -18.021977999999997,
        "reverse_margin": 2.8571430000000007
      },
      "new": "007f1950",
      "score": 56.263736
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7619047619047619,
          0.7619047619047619
        ],
        "cfg_coverage": [
          0.45454545454545453,
          0.38461538461538464
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
        "margin": -12.307693,
        "reverse_margin": -2.8571430000000007
      },
      "new": "006b66b0",
      "score": 53.406593
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7142857142857143,
          0.7142857142857143
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.3076923076923077
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
        "margin": 3.5347989999999996,
        "reverse_margin": -7.252746999999999
      },
      "new": "007493d8",
      "score": 49.010989
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-db4af370cf53194e0edfc92978b5f57c"></a>

### v16.0.0 [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) FUN_00826d7c

`competing_candidates` 

呼出元 2件 [`0082a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082a760.md) [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · 呼出先 10件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`008242f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/008242f0.md) [`0082449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082449c.md) [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md)

- 1. [`00557864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md) · スコア 5.542293 · 採用条件未達 · 順位差 2.5516389999999998 / 1.3274340000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00a70c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70c90.md) · スコア 4.214859 · 採用条件未達 · 順位差 -0.8678189999999999 / -1.3274340000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0070db34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070db34.md) · スコア 3.552171 · 採用条件未達 · 順位差 -5.600371000000001 / -1.990122 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00905d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/00905d0c.md) · スコア 2.556081 · 採用条件未達 · 順位差 0.05187900000000001 / -2.986212 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006440f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/006440f0.md) · スコア 1.59292 · 採用条件未達 · 順位差 1.59292 / -3.949373 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00724c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724c40.md) · スコア 1.061947 · 採用条件未達 · 順位差 -48.646618000000004 / -4.480346 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007fb9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb9f4.md) · スコア 1.061947 · 採用条件未達 · 順位差 -1.5021559999999998 / -4.480346 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007fca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fca38.md) · スコア 1.061947 · 採用条件未達 · 順位差 -1.5021559999999998 / -4.480346 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17543859649122806,
          0.08849557522123894
        ],
        "cfg_coverage": [
          0.058823529411764705,
          0.011627906976744186
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 2.5516389999999998,
        "reverse_margin": 1.3274340000000002
      },
      "new": "00557864",
      "score": 5.542293
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06912442396313365,
          0.06637168141592921
        ],
        "cfg_coverage": [
          0.014705882352941176,
          0.011627906976744186
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.8678189999999999,
        "reverse_margin": -1.3274340000000002
      },
      "new": "00a70c90",
      "score": 4.214859
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15254237288135594,
          0.03982300884955752
        ],
        "cfg_coverage": [
          0.2,
          0.05813953488372093
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -5.600371000000001,
        "reverse_margin": -1.990122
      },
      "new": "0070db34",
      "score": 3.552171
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd2d8123837680dbf81c9fa6f685fded"></a>

### v16.0.0 [`00827138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/00827138.md) FUN_00827138

`competing_candidates` 

呼出元 2件 [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) · 呼出先 13件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) [`00a466d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466d0.md)

- 1. [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) · スコア 68.115942 · 採用条件未達 · 順位差 49.424819 / 49.424819 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 18.691123 · 採用条件未達 · 順位差 -49.22192 / -49.424819 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) · スコア 12.608696 · 採用条件未達 · 順位差 -23.60752 / -55.507246 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 9.118684 · 採用条件未達 · 順位差 -41.404337 / -58.997258 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ecdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecdec.md) · スコア 8.586957 · 採用条件未達 · 順位差 -7.380509999999999 / -59.528985000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) · スコア 5.217391 · 採用条件未達 · 順位差 2.873641 / -62.898551000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007f97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f97c0.md) · スコア 5.217391 · 採用条件未達 · 順位差 -2.0398240000000003 / -62.898551000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007f718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f718c.md) · スコア 4.728261 · 採用条件未達 · 順位差 -66.70031 / -63.387681 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8019323671497585,
          0.8019323671497585
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
        "margin": 49.424819,
        "reverse_margin": 49.424819
      },
      "new": "007f1d24",
      "score": 68.115942
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3826086956521739,
          0.21256038647342995
        ],
        "cfg_coverage": [
          0.4418604651162791,
          0.296875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -49.22192,
        "reverse_margin": -49.424819
      },
      "new": "007f20a0",
      "score": 18.691123
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21333333333333335,
          0.15458937198067632
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.60752,
        "reverse_margin": -55.507246
      },
      "new": "007f226c",
      "score": 12.608696
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5720cf85952b764ba6c90817b520f53b"></a>

### v16.0.0 [`008274b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008274b4.md) FUN_008274b4

`competing_candidates` 

呼出元 1件 [`0082ab38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ab38.md) · 呼出先 7件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md)

- 1. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 67.913043 · 採用条件未達 · 順位差 49.22192 / 49.22192 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) · スコア 18.691123 · 採用条件未達 · 順位差 -49.424819 / -49.22192 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) · スコア 16.533333 · 採用条件未達 · 順位差 -19.682883000000004 / -51.37971 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ecdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ec/007ecdec.md) · スコア 15.199191 · 採用条件未達 · 順位差 -0.7682759999999984 / -52.713852 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) · スコア 11.458809 · 採用条件未達 · 順位差 -34.882756 / -56.454234 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 10.07425 · 採用条件未達 · 順位差 -40.448771 / -57.838793 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f718c.md) · スコア 8.121335 · 採用条件未達 · 順位差 -63.307236 / -59.791708 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f6f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6f30.md) · スコア 5.859313 · 採用条件未達 · 順位差 -58.782214999999994 / -62.05373 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7652173913043478,
          0.7652173913043478
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
        "margin": 49.22192,
        "reverse_margin": 49.22192
      },
      "new": "007f20a0",
      "score": 67.913043
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21256038647342995,
          0.3826086956521739
        ],
        "cfg_coverage": [
          0.296875,
          0.4418604651162791
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -49.424819,
        "reverse_margin": -49.22192
      },
      "new": "007f1d24",
      "score": 18.691123
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22,
          0.28695652173913044
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.27906976744186046
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.682883000000004,
        "reverse_margin": -51.37971
      },
      "new": "007f226c",
      "score": 16.533333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1f9a784bd000290688b2c176101a6f0e"></a>

### v16.0.0 [`00827680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/00827680.md) FUN_00827680

`competing_candidates` 

呼出元 1件 [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ab0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0300.md)

- 1. [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) · スコア 36.216216 · 採用条件未達 · 順位差 18.041065000000003 / 12.949213000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 23.267003 · 採用条件未達 · 順位差 -27.256018 / -12.949213000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) · スコア 22.992322 · 採用条件未達 · 順位差 -23.349243 / -13.223894000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 16.443243 · 採用条件未達 · 順位差 -51.469800000000006 / -19.772973000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) · スコア 12.518606 · 採用条件未達 · 順位差 -55.597336000000006 / -23.697610000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) · スコア 6.876536 · 採用条件未達 · 順位差 -33.642331999999996 / -29.33968 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) · スコア 6.681081 · 採用条件未達 · 順位差 -53.911079 / -29.535135000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f718c.md) · スコア 5.881081 · 採用条件未達 · 順位差 -65.54749000000001 / -30.335135 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.3194444444444444,
          0.3108108108108108
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 18.041065000000003,
        "reverse_margin": 12.949213000000004
      },
      "new": "007f226c",
      "score": 36.216216
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3021978021978022,
          0.36666666666666664
        ],
        "cfg_coverage": [
          0.25675675675675674,
          0.25675675675675674
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.256018,
        "reverse_margin": -12.949213000000004
      },
      "new": "007f534c",
      "score": 23.267003
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
      "new": "007ffe48",
      "score": 22.992322
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2a16d9c452c0154cd8fc0a19f1ffe660"></a>

### v16.0.0 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) FUN_008278d8

`competing_candidates` 

呼出元 1件 [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · 呼出先 34件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

- 1. [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) · スコア 43.795013 · 採用条件未達 · 順位差 38.481041 / 36.646007999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · スコア 7.149005 · 採用条件未達 · 順位差 -9.246766000000001 / -36.646007999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00687ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687ba8.md) · スコア 5.729445 · 採用条件未達 · 順位差 -23.708833 / -38.065568 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005d4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4988.md) · スコア 4.774221 · 採用条件未達 · 順位差 -34.705740000000006 / -39.020792 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007d48f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d4/007d48f8.md) · スコア 2.835821 · 採用条件未達 · 順位差 -3.137417 / -40.959191999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a4f47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md) · スコア 2.597015 · 採用条件未達 · 順位差 -5.816001000000001 / -41.197998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007dd8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dd/007dd8d0.md) · スコア 2.416012 · 採用条件未達 · 順位差 -2.718448 / -41.379000999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) · スコア 2.190275 · 採用条件未達 · 順位差 -1.936575 / -41.604738 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4925373134328358,
          0.4925373134328358
        ],
        "cfg_coverage": [
          0.32926829268292684,
          0.31213872832369943
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 38.481041,
        "reverse_margin": 36.646007999999995
      },
      "new": "007f24c4",
      "score": 43.795013
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
      "new": "00868b14",
      "score": 7.149005
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.030601092896174863,
          0.027860696517412936
        ],
        "cfg_coverage": [
          0.0035460992907801418,
          0.002890173410404624
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.708833,
        "reverse_margin": -38.065568
      },
      "new": "00687ba8",
      "score": 5.729445
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0b9828f82ac17db37f3ffd0a2bdc77fa"></a>

### v16.0.0 [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) FUN_00828b9c

`competing_candidates` 

呼出元 1件 [`008317b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008317b4.md) · 呼出先 22件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0081fd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081f/0081fd88.md) [`0082903c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/0082903c.md)

- 1. [`007f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3788.md) · スコア 66.882353 · 採用条件未達 · 順位差 56.089876999999994 / 58.24595599999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`008f5270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f5/008f5270.md) · スコア 8.636397 · 採用条件未達 · 順位差 1.9888600000000007 / -58.24595599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0071748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/0071748c.md) · スコア 8.153846 · 採用条件未達 · 順位差 -31.611472999999997 / -58.72850699999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006d4ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ba0.md) · スコア 7.882353 · 採用条件未達 · 順位差 -0.7410239999999995 / -58.99999999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005f09c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f09c4.md) · スコア 7.536232 · 採用条件未達 · 順位差 -1.7391299999999994 / -59.346121 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a7240c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7240c.md) · スコア 7.12766 · 採用条件未達 · 順位差 -31.904598 / -59.754692999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007c77c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md) · スコア 7.09389 · 採用条件未達 · 順位差 -22.369597 / -59.78846299999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00855450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855450.md) · スコア 6.269727 · 採用条件未達 · 順位差 1.9115389999999994 / -60.61262599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6813725490196079,
          0.6813725490196079
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 56.089876999999994,
        "reverse_margin": 58.24595599999999
      },
      "new": "007f3788",
      "score": 66.882353
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11444141689373297,
          0.20588235294117646
        ],
        "cfg_coverage": [
          0.08849557522123894,
          0.2127659574468085
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.9888600000000007,
        "reverse_margin": -58.24595599999999
      },
      "new": "008f5270",
      "score": 8.636397
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10384615384615385,
          0.1323529411764706
        ],
        "cfg_coverage": [
          0.09615384615384616,
          0.10638297872340426
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -31.611472999999997,
        "reverse_margin": -58.72850699999999
      },
      "new": "0071748c",
      "score": 8.153846
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-83a30d75c4373563268c536dd61ca399"></a>

### v16.0.0 [`0082903c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/0082903c.md) FUN_0082903c

`competing_candidates` 

呼出元 2件 [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) [`008312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b4.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0082089c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/0082089c.md) [`00830234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830234.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) · スコア 40.518868 · 採用条件未達 · 順位差 33.642331999999996 / 34.373931999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 6.144936 · 採用条件未達 · 順位差 -44.378085 / -34.373931999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0050995c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050995c.md) · スコア 6.136364 · 採用条件未達 · 順位差 -4.714699999999999 / -34.382504 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004c898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md) · スコア 3.75 · 採用条件未達 · 順位差 3.75 / -36.768868 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004f11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) · スコア 3.75 · 採用条件未達 · 順位差 -6.376829000000001 / -36.768868 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004bdd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md) · スコア 3.567568 · 採用条件未達 · 順位差 0.6486490000000003 / -36.951299999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004d7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md) · スコア 3.409091 · 採用条件未達 · 順位差 -10.289344 / -37.109776999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00585ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585ea0.md) · スコア 3.068182 · 採用条件未達 · 順位差 3.068182 / -37.450686 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          0.1702127659574468,
          0.1509433962264151
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.642331999999996,
        "reverse_margin": 34.373931999999996
      },
      "new": "007f3c28",
      "score": 40.518868
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09340659340659341,
          0.09659090909090909
        ],
        "cfg_coverage": [
          0.02702702702702703,
          0.03773584905660377
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -44.378085,
        "reverse_margin": -34.373931999999996
      },
      "new": "007f534c",
      "score": 6.144936
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24,
          0.10227272727272728
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
        "margin": -4.714699999999999,
        "reverse_margin": -34.382504
      },
      "new": "0050995c",
      "score": 6.136364
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) FUN_00829354

`competing_candidates` 

呼出元 3件 [`00828b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00828/00828b9c.md) [`0082be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082be28.md) [`008312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/008312b4.md) · 呼出先 5件 [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) · スコア 60.59216 · 採用条件未達 · 順位差 45.620731 / 43.552960999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0070da24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070d/0070da24.md) · スコア 17.039199 · 採用条件未達 · 順位差 13.013667 / -43.552960999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007e7f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7f80.md) · スコア 13.55 · 採用条件未達 · 順位差 6.200000000000001 / -47.042159999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00627b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627b1c.md) · スコア 9.290618 · 採用条件未達 · 順位差 -67.025171 / -51.301542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) · スコア 7.514595 · 採用条件未達 · 順位差 7.514595 / -53.077565 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004f10f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md) · スコア 7.514595 · 採用条件未達 · 順位差 -6.235405 / -53.077565 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007f718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f718c.md) · スコア 7.418682 · 採用条件未達 · 順位差 -64.009889 / -53.173478 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00566e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566e98.md) · スコア 7.155963 · 採用条件未達 · 順位差 4.155963 / -53.436197 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7522935779816514,
          0.7522935779816514
        ],
        "cfg_coverage": [
          0.8095238095238095,
          0.7727272727272727
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 45.620731,
        "reverse_margin": 43.552960999999996
      },
      "new": "007f3f40",
      "score": 60.59216
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45614035087719296,
          0.23853211009174313
        ],
        "cfg_coverage": [
          0.25,
          0.13636363636363635
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 13.013667,
        "reverse_margin": -43.552960999999996
      },
      "new": "0070da24",
      "score": 17.039199
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21333333333333335,
          0.29357798165137616
        ],
        "cfg_coverage": [
          0.0375,
          0.06818181818181818
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.200000000000001,
        "reverse_margin": -47.042159999999996
      },
      "new": "007e7f80",
      "score": 13.55
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7f891fc2ce6b3050d10c1b559c055d91"></a>

### v16.0.0 [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) FUN_00829534

`competing_candidates` 

呼出元 2件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`0082dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md) · 呼出先 31件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

- 1. [`007f4120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f4/007f4120.md) · スコア 30.140533 · 採用条件未達 · 順位差 27.149879000000002 / 26.677157 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006f2878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2878.md) · スコア 3.463376 · 採用条件未達 · 順位差 -16.950626 / -26.677157 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00abd464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abd/00abd464.md) · スコア 2.803738 · 採用条件未達 · 順位差 -14.05122 / -27.336795000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) · スコア 2.793993 · 採用条件未達 · 順位差 -31.090435 / -27.34654 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00634d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md) · スコア 2.793993 · 採用条件未達 · 順位差 -29.940699000000002 / -27.34654 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00798f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00798/00798f70.md) · スコア 2.607077 · 採用条件未達 · 順位差 -30.724082999999997 / -27.533456 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) · スコア 1.188587 · 採用条件未達 · 順位差 -42.606426 / -28.951946 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · スコア 1.053865 · 採用条件未達 · 順位差 0.5673790000000001 / -29.086668000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3862928348909657,
          0.3862928348909657
        ],
        "cfg_coverage": [
          0.15204678362573099,
          0.14814814814814814
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 27.149879000000002,
        "reverse_margin": 26.677157
      },
      "new": "007f4120",
      "score": 30.140533
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05056179775280899,
          0.018691588785046728
        ],
        "cfg_coverage": [
          0.046153846153846156,
          0.017094017094017096
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -16.950626,
        "reverse_margin": -26.677157
      },
      "new": "006f2878",
      "score": 3.463376
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.060810810810810814,
          0.04672897196261682
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
        "margin": -14.05122,
        "reverse_margin": -27.336795000000002
      },
      "new": "00abd464",
      "score": 2.803738
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9564d975693f397fa7ed68f4c3065147"></a>

### v16.0.0 [`0082a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082a760.md) FUN_0082a760

`competing_candidates` 

呼出元 2件 [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) [`0082dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md) · 呼出先 9件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00728698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728698.md) [`00728710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728710.md) [`00826d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00826/00826d7c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 50.523021 · 採用条件未達 · 順位差 26.769785 / 27.20283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ffe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ffe48.md) · スコア 23.320191 · 採用条件未達 · 順位差 -23.021374 / -27.20283 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) · スコア 16.554458 · 採用条件未達 · 順位差 -19.661758000000003 / -33.968563 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 9.937404 · 採用条件未達 · 順位差 -57.975639 / -40.585617 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) · スコア 8.981838 · 採用条件未達 · 順位差 -59.13410400000001 / -41.541183000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) · スコア 6.617054 · 採用条件未達 · 順位差 -33.901813999999995 / -43.905967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`004d9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md) · スコア 6.263736 · 採用条件未達 · 順位差 -8.977500000000001 / -44.259285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0044b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b6b0.md) · スコア 5.934066 · 採用条件未達 · 順位差 -6.185422000000001 / -44.588955 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6648351648351648,
          0.6648351648351648
        ],
        "cfg_coverage": [
          0.5675675675675675,
          0.5316455696202531
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 26.769785,
        "reverse_margin": 27.20283
      },
      "new": "007f534c",
      "score": 50.523021
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
      "new": "007ffe48",
      "score": 23.320191
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2733333333333333,
          0.22527472527472528
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.1518987341772152
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.661758000000003,
        "reverse_margin": -33.968563
      },
      "new": "007f226c",
      "score": 16.554458
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2a6de9f6aeafb7926d1dccee8bc3bffc"></a>

### v16.0.0 [`0082aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082aa38.md) FUN_0082aa38

`competing_candidates` 

呼出元 2件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`0082dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

- 1. [`007f5624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5624.md) · スコア 31.7375 · 採用条件未達 · 順位差 23.3 / 23.3 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008b818c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b818c.md) · スコア 8.4375 · 採用条件未達 · 順位差 -1.7511790000000005 / -23.3 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00529c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529c48.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -24.2375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008fbb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fbb48.md) · スコア 7.5 · 採用条件未達 · 順位差 2.4579829999999996 / -24.2375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0099fc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fc10.md) · スコア 7.132867 · 採用条件未達 · 順位差 -26.245510999999997 / -24.604633 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00837810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837810.md) · スコア 6.428571 · 採用条件未達 · 順位差 2.1428570000000002 / -25.308929 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00420580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420580.md) · スコア 4.6875 · 採用条件未達 · 順位差 0.816532 / -27.05 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00420858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420858.md) · スコア 4.6875 · 採用条件未達 · 順位差 0.816532 / -27.05 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.515625,
          0.515625
        ],
        "cfg_coverage": [
          0.07142857142857142,
          0.04
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 23.3,
        "reverse_margin": 23.3
      },
      "new": "007f5624",
      "score": 31.7375
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16981132075471697,
          0.140625
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
        "margin": -1.7511790000000005,
        "reverse_margin": -23.3
      },
      "new": "008b818c",
      "score": 8.4375
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25806451612903225,
          0.125
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
        "margin": 7.5,
        "reverse_margin": -24.2375
      },
      "new": "00529c48",
      "score": 7.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a2e01b3491580736816d4cdfda119011"></a>

### v16.0.0 [`0082ab38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ab38.md) FUN_0082ab38

`competing_candidates` 

呼出元 1件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) · 呼出先 2件 [`008274b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008274b4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007f5724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5724.md) · スコア 45.285714 · 採用条件未達 · 順位差 41.285714 / 36.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007733d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007733d8.md) · スコア 8.428571 · 採用条件未達 · 順位差 8.428571 / -36.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00773684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773684.md) · スコア 8.428571 · 採用条件未達 · 順位差 8.428571 / -36.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00773800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773800.md) · スコア 8.428571 · 採用条件未達 · 順位差 8.428571 / -36.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008c83f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c83f0.md) · スコア 2.4 · 採用条件未達 · 順位差 -2.260194 / -42.885714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009dd844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd844.md) · スコア 2.4 · 採用条件未達 · 順位差 -3.558759 / -42.885714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00804c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00804/00804c98.md) · スコア 2.330097 · 採用条件未達 · 順位差 -26.762509 / -42.955617 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.5,
          0.4642857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 41.285714,
        "reverse_margin": 36.857143
      },
      "new": "007f5724",
      "score": 45.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23333333333333334,
          0.11666666666666667
        ],
        "cfg_coverage": [
          0.14285714285714285,
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
        "margin": 8.428571,
        "reverse_margin": -36.857143
      },
      "new": "007733d8",
      "score": 8.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23333333333333334,
          0.11666666666666667
        ],
        "cfg_coverage": [
          0.13333333333333333,
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
        "margin": 8.428571,
        "reverse_margin": -36.857143
      },
      "new": "00773684",
      "score": 8.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-433ddb23e1d490f3153a38568f1bfe1f"></a>

### v16.0.0 [`0082ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ac28.md) FUN_0082ac28

`competing_candidates` 

呼出元 1件 [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) · 呼出先 26件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)

- 1. [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) · スコア 51.057296 · 採用条件未達 · 順位差 44.032628 / 44.032628 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0088daac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088d/0088daac.md) · スコア 7.024668 · 採用条件未達 · 順位差 -62.339130000000004 / -44.032628 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) · スコア 6.286472 · 採用条件未達 · 順位差 -42.266076 / -44.770824000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00671c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md) · スコア 5.821632 · 採用条件未達 · 順位差 -32.966246999999996 / -45.235664 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`008bf204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf204.md) · スコア 5.514372 · 採用条件未達 · 順位差 -19.818961 / -45.542924 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`0088c2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c2d8.md) · スコア 5.512112 · 採用条件未達 · 順位差 -55.198128 / -45.545184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) · スコア 5.49792 · 採用条件未達 · 順位差 -28.815447 / -45.559376 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`0088c5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088c/0088c5f0.md) · スコア 5.341378 · 採用条件未達 · 順位差 -26.508507 / -45.715918 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6470588235294118,
          0.6470588235294118
        ],
        "cfg_coverage": [
          0.3157894736842105,
          0.3116883116883117
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 44.032628,
        "reverse_margin": 44.032628
      },
      "new": "007f5814",
      "score": 51.057296
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.019823788546255508,
          0.017077798861480076
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
        "margin": -62.339130000000004,
        "reverse_margin": -44.032628
      },
      "new": "0088daac",
      "score": 7.024668
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.004774535809018567,
          0.017077798861480076
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
        "margin": -42.266076,
        "reverse_margin": -44.770824000000005
      },
      "new": "0075f8cc",
      "score": 6.286472
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-447b691a6b15924e83010abe4f13d637"></a>

### v16.0.0 [`0082c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c344.md) FUN_0082c344

`competing_candidates` 

呼出元 1件 [`0082c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c69c.md) · 呼出先 5件 [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md) [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007f6f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6f30.md) · スコア 64.641528 · 採用条件未達 · 順位差 51.38013699999999 / 51.610021999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00627b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627b1c.md) · スコア 13.031506 · 採用条件未達 · 順位差 -63.284282999999995 / -51.610021999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009d0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0a60.md) · スコア 10.57931 · 採用条件未達 · 順位差 2.074047 / -54.062217999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009d0ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d0/009d0ce8.md) · スコア 10.17931 · 採用条件未達 · 順位差 2.6978289999999996 / -54.46221799999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009d6538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md) · スコア 8.97544 · 採用条件未達 · 順位差 -12.470083 / -55.666087999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a70ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70ac4.md) · スコア 8.97544 · 採用条件未達 · 順位差 -1.477485999999999 / -55.666087999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) · スコア 6.990821 · 採用条件未達 · 順位差 -53.601338999999996 / -57.650707 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 5.782684 · 採用条件未達 · 順位差 -62.130359 / -58.85884399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.841726618705036,
          0.841726618705036
        ],
        "cfg_coverage": [
          0.7592592592592593,
          0.7068965517241379
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 51.38013699999999,
        "reverse_margin": 51.610021999999994
      },
      "new": "007f6f30",
      "score": 64.641528
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20175438596491227,
          0.16546762589928057
        ],
        "cfg_coverage": [
          0.1956521739130435,
          0.15517241379310345
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -63.284282999999995,
        "reverse_margin": -51.610021999999994
      },
      "new": "00627b1c",
      "score": 13.031506
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15333333333333332,
          0.16546762589928057
        ],
        "cfg_coverage": [
          0.07017543859649122,
          0.06896551724137931
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 2.074047,
        "reverse_margin": -54.062217999999994
      },
      "new": "009d0a60",
      "score": 10.57931
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f631187e618f23bbdfbf722878829b9f"></a>

### v16.0.0 [`0082c5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c5a0.md) FUN_0082c5a0

`competing_candidates` 

呼出元 1件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007f718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f718c.md) · スコア 71.428571 · 採用条件未達 · 順位差 63.307236 / 63.307236 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f20a0.md) · スコア 8.121335 · 採用条件未達 · 順位差 -59.791708 / -63.307236 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) · スコア 7.483617 · 採用条件未達 · 順位差 -53.108543 / -63.944954 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00686590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686590.md) · スコア 7.466667 · 採用条件未達 · 順位差 4.702959 / -63.961904000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007f226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f226c.md) · スコア 5.911111 · 採用条件未達 · 順位差 -30.305105000000005 / -65.51746 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f6f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6f30.md) · スコア 5.859313 · 採用条件未達 · 順位差 -58.782214999999994 / -65.569258 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f534c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f534c.md) · スコア 5.096525 · 採用条件未達 · 順位差 -45.426496 / -66.332046 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f1d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f1/007f1d24.md) · スコア 4.728261 · 採用条件未達 · 順位差 -63.387681 / -66.70031 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 63.307236,
        "reverse_margin": 63.307236
      },
      "new": "007f718c",
      "score": 71.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10434782608695652,
          0.19047619047619047
        ],
        "cfg_coverage": [
          0.09302325581395349,
          0.1
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -59.791708,
        "reverse_margin": -63.307236
      },
      "new": "007f20a0",
      "score": 8.121335
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10091743119266056,
          0.1746031746031746
        ],
        "cfg_coverage": [
          0.07142857142857142,
          0.075
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -53.108543,
        "reverse_margin": -63.944954
      },
      "new": "007f3f40",
      "score": 7.483617
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ae9db155bfed3340cf11bf85200ab1bc"></a>

### v16.0.0 [`0082c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c69c.md) FUN_0082c69c

`competing_candidates` 

呼出元 1件 [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) · 呼出先 9件 [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`0082b5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b5e0.md) [`0082b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082b8c0.md) [`0082bc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082bc18.md) [`0082be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082be28.md)

- 1. [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) · スコア 62.979592 · 採用条件未達 · 順位差 52.931526 / 52.560728999999995 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 2. [`009d6538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6538.md) · スコア 10.418863 · 採用条件未達 · 順位差 -11.026660000000001 / -52.560728999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a70ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70ac4.md) · スコア 10.148186 · 採用条件未達 · 順位差 -0.3047399999999989 / -52.831405999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007e855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e8/007e855c.md) · スコア 9.472687 · 採用条件未達 · 順位差 -60.623163999999996 / -53.506904999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00627b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627b1c.md) · スコア 8.764302 · 採用条件未達 · 順位差 -67.551487 / -54.215289999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007eb118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007eb/007eb118.md) · スコア 8.44898 · 採用条件未達 · 順位差 -56.183827 / -54.530612 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) · スコア 5.976231 · 採用条件未達 · 順位差 -3.2903219999999997 / -57.003361 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008a36b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a3/008a36b4.md) · スコア 5.698709 · 採用条件未達 · 順位差 -1.4117639999999998 / -57.280882999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7448979591836735,
          0.7448979591836735
        ],
        "cfg_coverage": [
          0.9411764705882353,
          0.9142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 52.931526,
        "reverse_margin": 52.560728999999995
      },
      "new": "007f7288",
      "score": 62.979592
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11650485436893204,
          0.12244897959183673
        ],
        "cfg_coverage": [
          0.2,
          0.17142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -11.026660000000001,
        "reverse_margin": -52.560728999999995
      },
      "new": "009d6538",
      "score": 10.418863
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11650485436893204,
          0.12244897959183673
        ],
        "cfg_coverage": [
          0.15789473684210525,
          0.17142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.3047399999999989,
        "reverse_margin": -52.831405999999994
      },
      "new": "00a70ac4",
      "score": 10.148186
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1678b293728812ac492d8737c193f09e"></a>

### v16.0.0 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) FUN_0082c824

`competing_candidates` 

呼出元 3件 [`0082c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c69c.md) [`00831d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831d00.md) [`00831ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831ea4.md) · 呼出先 16件 [`0081cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081cb48.md) [`0082aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082aa38.md) [`0082c5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c5a0.md) [`0082dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dd64.md) [`008305cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305cc.md)

- 1. [`007f7410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7410.md) · スコア 60.855791 · 採用条件未達 · 順位差 55.248314 / 56.154756000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) · スコア 4.701035 · 採用条件未達 · 順位差 -43.719349 / -56.154756000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a3d70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d70c.md) · スコア 4.647887 · 採用条件未達 · 順位差 -21.425539999999998 / -56.207904000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f3f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3f40.md) · スコア 4.058461 · 採用条件未達 · 順位差 -56.533699 / -56.79733 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) · スコア 3.834586 · 採用条件未達 · 順位差 -0.06785300000000039 / -57.021205 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004e5e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md) · スコア 3.834586 · 採用条件未達 · 順位差 -0.06785300000000039 / -57.021205 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0066da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md) · スコア 3.709091 · 採用条件未達 · 順位差 -33.233619 / -57.1467 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007f61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f61cc.md) · スコア 3.157895 · 採用条件未達 · 順位差 -4.636977 / -57.697896 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8082706766917294,
          0.8082706766917294
        ],
        "cfg_coverage": [
          0.6790123456790124,
          0.6179775280898876
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 55.248314,
        "reverse_margin": 56.154756000000006
      },
      "new": "007f7410",
      "score": 60.855791
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07476635514018691,
          0.09022556390977443
        ],
        "cfg_coverage": [
          0.010752688172043012,
          0.011235955056179775
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -43.719349,
        "reverse_margin": -56.154756000000006
      },
      "new": "007f78c4",
      "score": 4.701035
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07746478873239436,
          0.08270676691729323
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
        "margin": -21.425539999999998,
        "reverse_margin": -56.207904000000006
      },
      "new": "00a3d70c",
      "score": 4.647887
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e73da333e1f33cac7e54071f0f0404ea"></a>

### v16.0.0 [`0082ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccbc.md) FUN_0082ccbc

`competing_candidates` 

呼出元 1件 [`009dce3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dce3c.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md)

- 1. [`007f78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78a8.md) · スコア 45.714286 · 採用条件未達 · 順位差 18.514286000000002 / 45.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007ff184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff184.md) · スコア 0.0 · 採用条件未達 · 順位差 -42.5 / -45.714286 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 18.514286000000002,
        "reverse_margin": 45.714286
      },
      "new": "007f78a8",
      "score": 45.714286
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
        "margin": -42.5,
        "reverse_margin": -45.714286
      },
      "new": "007ff184",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0f308d929e08fa21f702ea35ed06e2e3"></a>

### v16.0.0 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) FUN_0082ccd8

`competing_candidates` 

呼出元 1件 [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) · 呼出先 21件 [`00816058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00816/00816058.md) [`00829534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829534.md) [`0082ab38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082a/0082ab38.md) [`0082d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md) [`0082d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md)

- 1. [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) · スコア 48.420384 · 採用条件未達 · 順位差 41.719738 / 42.228969 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8354.md) · スコア 6.191415 · 採用条件未達 · 順位差 -35.828288 / -42.228969 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f7410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7410.md) · スコア 5.607477 · 採用条件未達 · 順位差 -55.248314 / -42.812906999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009d2d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d2/009d2d94.md) · スコア 3.375066 · 採用条件未達 · 順位差 -2.4437650000000004 / -45.045318 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a0c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md) · スコア 3.375066 · 採用条件未達 · 順位差 -10.008051 / -45.045318 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0070c1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070c/0070c1ac.md) · スコア 3.2186 · 採用条件未達 · 順位差 -6.338652 / -45.201783999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006283ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/006283ec.md) · スコア 3.17757 · 採用条件未達 · 順位差 -6.009703 / -45.242813999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004f1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1c30.md) · スコア 2.999471 · 採用条件未達 · 順位差 -5.026007 / -45.420913 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6573208722741433,
          0.6573208722741433
        ],
        "cfg_coverage": [
          0.3978494623655914,
          0.3490566037735849
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 41.719738,
        "reverse_margin": 42.228969
      },
      "new": "007f78c4",
      "score": 48.420384
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06042296072507553,
          0.06230529595015576
        ],
        "cfg_coverage": [
          0.036585365853658534,
          0.02830188679245283
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.828288,
        "reverse_margin": -42.228969
      },
      "new": "007f8354",
      "score": 6.191415
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11278195488721804,
          0.09345794392523364
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
        "margin": -55.248314,
        "reverse_margin": -42.812906999999996
      },
      "new": "007f7410",
      "score": 5.607477
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6d45974229c7f83d1226151d432c1a35"></a>

### v16.0.0 [`0082d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d250.md) FUN_0082d250

`competing_candidates` 

呼出元 5件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`00831fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831fb4.md) [`00838b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838b60.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`007f7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7e3c.md) · スコア 2.810811 · 採用条件未達 · 順位差 0.8108110000000002 / 0.8108110000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006837ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00683/006837ac.md) · スコア 2.0 · 採用条件未達 · 順位差 -10.169492 / -0.8108110000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007f808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f808c.md) · スコア 2.0 · 採用条件未達 · 順位差 -5.288326 / -0.8108110000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008afc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008afc4c.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.959184 / -0.8108110000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008f9c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f9/008f9c04.md) · スコア 2.0 · 採用条件未達 · 順位差 -15.092025 / -0.8108110000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013513513513513514,
          0.013513513513513514
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
        "margin": 0.8108110000000002,
        "reverse_margin": 0.8108110000000002
      },
      "new": "007f7e3c",
      "score": 2.810811
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
        "margin": -10.169492,
        "reverse_margin": -0.8108110000000002
      },
      "new": "006837ac",
      "score": 2.0
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
        "margin": -5.288326,
        "reverse_margin": -0.8108110000000002
      },
      "new": "007f808c",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-071af9597c3d55d6e3d0fc91c976f087"></a>

### v16.0.0 [`0082d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d4a0.md) FUN_0082d4a0

`competing_candidates` 

呼出元 2件 [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b6f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f0c.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`007f808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f808c.md) · スコア 7.288326 · 採用条件未達 · 順位差 4.1490849999999995 / 4.1490849999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008f9c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f9/008f9c04.md) · スコア 3.139241 · 採用条件未達 · 順位差 -13.952784 / -4.1490849999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00607318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607318.md) · スコア 2.0 · 採用条件未達 · 順位差 -5.236181 / -5.288326 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007f7e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7e3c.md) · スコア 2.0 · 採用条件未達 · 順位差 -0.8108110000000002 / -5.288326 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a6b4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b4f8.md) · スコア 2.0 · 採用条件未達 · 順位差 -3.934426 / -5.288326 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06962025316455696,
          0.06962025316455696
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.1490849999999995,
        "reverse_margin": 4.1490849999999995
      },
      "new": "007f808c",
      "score": 7.288326
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.022222222222222223,
          0.0189873417721519
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
        "margin": -13.952784,
        "reverse_margin": -4.1490849999999995
      },
      "new": "008f9c04",
      "score": 3.139241
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -5.236181,
        "reverse_margin": -5.288326
      },
      "new": "00607318",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f1e458bbddfb9a125151ddbc91a4a09b"></a>

### v16.0.0 [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) FUN_0082d768

`competing_candidates` 

呼出元 1件 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · 呼出先 16件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469028.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0081c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c2b4.md)

- 1. [`007f8354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8354.md) · スコア 42.019703 · 採用条件未達 · 順位差 35.828288 / 35.319057 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) · スコア 6.700646 · 採用条件未達 · 順位差 -41.719738 / -35.319057 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00508250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508250.md) · スコア 5.119684 · 採用条件未達 · 順位差 -2.580786 / -36.900019 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007f6f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6f30.md) · スコア 3.153816 · 採用条件未達 · 順位差 -61.487711999999995 / -38.865887 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0090596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00905/0090596c.md) · スコア 3.153816 · 採用条件未達 · 順位差 -12.963301000000001 / -38.865887 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00421b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · スコア 2.900302 · 採用条件未達 · 順位差 0.03255499999999989 / -39.119400999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) · スコア 2.362757 · 採用条件未達 · 順位差 -69.63482499999999 / -39.656946 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0071b248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b248.md) · スコア 2.356495 · 採用条件未達 · 順位差 -6.707432 / -39.663208 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5438066465256798,
          0.5438066465256798
        ],
        "cfg_coverage": [
          0.4146341463414634,
          0.3695652173913043
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.828288,
        "reverse_margin": 35.319057
      },
      "new": "007f8354",
      "score": 42.019703
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06230529595015576,
          0.06042296072507553
        ],
        "cfg_coverage": [
          0.053763440860215055,
          0.05434782608695652
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -41.719738,
        "reverse_margin": -35.319057
      },
      "new": "007f78c4",
      "score": 6.700646
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08571428571428572,
          0.07250755287009064
        ],
        "cfg_coverage": [
          0.038461538461538464,
          0.043478260869565216
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.580786,
        "reverse_margin": -36.900019
      },
      "new": "00508250",
      "score": 5.119684
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-682ba738f77eda5de2731e9dccdd85ab"></a>

### v16.0.0 [`0082dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082dce0.md) FUN_0082dce0

`competing_candidates` 

呼出元 1件 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`007f88cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f88cc.md) · スコア 26.848485 · 採用条件未達 · 順位差 17.575758 / 17.575758 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007c511c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c511c.md) · スコア 9.272727 · 採用条件未達 · 順位差 -56.363637 / -17.575758 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30303030303030304,
          0.30303030303030304
        ],
        "cfg_coverage": [
          0.4,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.575758,
        "reverse_margin": 17.575758
      },
      "new": "007f88cc",
      "score": 26.848485
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36363636363636365,
          0.12121212121212122
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
        "margin": -56.363637,
        "reverse_margin": -17.575758
      },
      "new": "007c511c",
      "score": 9.272727
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d3bcadcfc3464821b0907a22e1d4c31c"></a>

### v16.0.0 [`0082eab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eab8.md) FUN_0082eab8

`competing_candidates` 

呼出元 21件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006270cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006adef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006adef0.md) [`006ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md) · 呼出先 2件 [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

- 1. [`007f96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.923077 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -56.923077,
        "reverse_margin": 0.0
      },
      "new": "007f96a4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ad8d3a770a112a1f71d14f295486873e"></a>

### v16.0.0 [`0082ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ecf8.md) FUN_0082ecf8

`competing_candidates` 

呼出元 1件 [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) · 呼出先 5件 [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007f98e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f98e4.md) · スコア 70.666667 · 採用条件未達 · 順位差 59.567657000000004 / 59.567657000000004 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) · スコア 11.09901 · 採用条件未達 · 順位差 11.09901 / -59.567657000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`004e7de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md) · スコア 5.625 · 採用条件未達 · 順位差 2.897727 / -65.041667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0056ea48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ea48.md) · スコア 5.333333 · 採用条件未達 · 順位差 5.333333 / -65.33333400000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00557264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md) · スコア 4.8 · 採用条件未達 · 順位差 -5.7405409999999994 / -65.866667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009969b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/009969b8.md) · スコア 3.116883 · 採用条件未達 · 順位差 -0.1558440000000001 / -67.549784 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007f97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f97c0.md) · スコア 0.0 · 採用条件未達 · 順位差 -7.257215 / -70.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b6b80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b80c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -70.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8444444444444444,
          0.8444444444444444
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
        "margin": 59.567657000000004,
        "reverse_margin": 59.567657000000004
      },
      "new": "007f98e4",
      "score": 70.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16831683168316833,
          0.37777777777777777
        ],
        "cfg_coverage": [
          0.05,
          0.2
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 11.09901,
        "reverse_margin": -59.567657000000004
      },
      "new": "00565720",
      "score": 11.09901
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09375,
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
        "margin": 2.897727,
        "reverse_margin": -65.041667
      },
      "new": "004e7de0",
      "score": 5.625
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ce0edebc60c43dcb5cd0c255c3e831b4"></a>

### v16.0.0 [`0082eddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eddc.md) FUN_0082eddc

`competing_candidates` 

呼出元 1件 [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) · 呼出先 0件 

- 1. [`007f99c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99c8.md) · スコア 69.0 · 採用条件未達 · 順位差 68.9111 / 68.9111 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.9111,
        "reverse_margin": 68.9111
      },
      "new": "007f99c8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ed2872d2fd6eb50ad1fa4874572152c8"></a>

### v16.0.0 [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) FUN_0082f0e8

`competing_candidates` 

呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044c21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc0c.md)

- 1. [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) · スコア 53.138838 · 採用条件未達 · 順位差 49.561376 / 49.355716 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00942564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/00942564.md) · スコア 3.783122 · 採用条件未達 · 順位差 1.533122 / -49.355716 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00942/009428a4.md) · スコア 3.534444 · 採用条件未達 · 順位差 -5.947096 / -49.604394 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00944ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00944/00944ab4.md) · スコア 3.220932 · 採用条件未達 · 順位差 -9.177522 / -49.917906 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005f6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f6/005f6340.md) · スコア 2.783483 · 採用条件未達 · 順位差 -36.97101 / -50.355355 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008cacc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cacc4.md) · スコア 2.384755 · 採用条件未達 · 順位差 -50.257011 / -50.754083 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009e1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1120.md) · スコア 2.384755 · 採用条件未達 · 順位差 -39.308793 / -50.754083 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) · スコア 2.322442 · 採用条件未達 · 順位差 -8.547635 / -50.816396 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6681034482758621,
          0.6681034482758621
        ],
        "cfg_coverage": [
          0.5965909090909091,
          0.5526315789473685
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.561376,
        "reverse_margin": 49.355716
      },
      "new": "007f9cd4",
      "score": 53.138838
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1780821917808219,
          0.05603448275862069
        ],
        "cfg_coverage": [
          0.08,
          0.021052631578947368
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.533122,
        "reverse_margin": -49.355716
      },
      "new": "00942564",
      "score": 3.783122
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04061470911086718,
          0.07974137931034483
        ],
        "cfg_coverage": [
          0.054878048780487805,
          0.09473684210526316
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -5.947096,
        "reverse_margin": -49.604394
      },
      "new": "009428a4",
      "score": 3.534444
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0f45c17d81110f0cd939f421ac447fa1"></a>

### v16.0.0 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) FUN_0082fb2c

`competing_candidates` 

呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 22件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)

- 1. [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) · スコア 28.145221 · 採用条件未達 · 順位差 18.176471 / 18.176471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`009e1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1430.md) · スコア 9.96875 · 採用条件未達 · 順位差 -17.745536 / -18.176471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008cafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cafd4.md) · スコア 6.6875 · 採用条件未達 · 順位差 -49.00947 / -21.457721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a8b5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b5e4.md) · スコア 6.21875 · 採用条件未達 · 順位差 -34.604779 / -21.926471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`004a4ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md) · スコア 4.6875 · 採用条件未達 · 順位差 1.051136 / -23.457721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0068fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068fe30.md) · スコア 4.0 · 採用条件未達 · 順位差 -43.489294 / -24.145221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`006994e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006994e8.md) · スコア 4.0 · 採用条件未達 · 順位差 -28.959887000000002 / -24.145221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`00932074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00932/00932074.md) · スコア 4.0 · 採用条件未達 · 順位差 -1.448276 / -24.145221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3828125,
          0.3828125
        ],
        "cfg_coverage": [
          0.058823529411764705,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 18.176471,
        "reverse_margin": 18.176471
      },
      "new": "007fa718",
      "score": 28.145221
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18681318681318682,
          0.1328125
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
        "margin": -17.745536,
        "reverse_margin": -18.176471
      },
      "new": "009e1430",
      "score": 9.96875
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09090909090909091,
          0.078125
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
        "margin": -49.00947,
        "reverse_margin": -21.457721
      },
      "new": "008cafd4",
      "score": 6.6875
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-77bb8f5478f815c64ed0165d8093c5ec"></a>

### v16.0.0 [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) FUN_00830020

`competing_candidates` 

呼出元 2件 [`0082d768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082d/0082d768.md) [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) · 呼出先 7件 [`0081a784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a784.md) [`008206dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/008206dc.md) [`00830234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830234.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

- 1. [`007fac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fac0c.md) · スコア 21.0 · 採用条件未達 · 順位差 11.0 / 11.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007e7d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e7/007e7d84.md) · スコア 10.0 · 採用条件未達 · 順位差 10.0 / -11.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007f3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f3/007f3c28.md) · スコア 3.409091 · 採用条件未達 · 順位差 -37.109776999999994 / -17.590909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.462342 / -21.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -21.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00482154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -21.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00482df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -21.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004f4d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4d5c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -21.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.0,
        "reverse_margin": 11.0
      },
      "new": "007fac0c",
      "score": 21.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1694915254237288,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 10.0,
        "reverse_margin": -11.0
      },
      "new": "007e7d84",
      "score": 10.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.056818181818181816,
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
        "margin": -37.109776999999994,
        "reverse_margin": -17.590909
      },
      "new": "007f3c28",
      "score": 3.409091
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dc0dc4f5736e234c69cb4fa78a3eed10"></a>

### v16.0.0 [`008302b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008302b8.md) FUN_008302b8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)

- 1. [`007faea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faea4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007faeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faeb4.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007faea4",
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
        "reverse_margin": 0.0
      },
      "new": "007faeb4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2b9952bbc8cfd2e506c9cad19e980981"></a>

### v16.0.0 [`008302c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008302c8.md) FUN_008302c8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007faeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faeb4.md) · スコア 20.0 · 採用条件未達 · 順位差 -40.0 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007faea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007faea4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -40.0,
        "reverse_margin": 20.0
      },
      "new": "007faeb4",
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
        "reverse_margin": -20.0
      },
      "new": "007faea4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5da6a9775f915aa002bb1a5a118f2d1a"></a>

### v16.0.0 [`008303c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008303c0.md) FUN_008303c0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)

- 1. [`007fafac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafac.md) · スコア 35.0 · 採用条件未達 · 順位差 10.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007fafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafbc.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "007fafac",
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
        "margin": -20.0,
        "reverse_margin": -35.0
      },
      "new": "007fafbc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6ee465ab6867cb673899cb4e6163a4bf"></a>

### v16.0.0 [`008303d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008303d0.md) FUN_008303d0

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007fafac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafac.md) · スコア 25.0 · 採用条件未達 · 順位差 -10.0 / 5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007fafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafbc.md) · スコア 20.0 · 採用条件未達 · 順位差 0.0 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "007fafac",
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
        "margin": 0.0,
        "reverse_margin": -5.0
      },
      "new": "007fafbc",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11ecb927eb3b2ba4329cc90128888e76"></a>

### v16.0.0 [`00830584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830584.md) FUN_00830584

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)

- 1. [`007fb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb170.md) · スコア 35.0 · 採用条件未達 · 順位差 10.0 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007fb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb180.md) · スコア 25.0 · 採用条件未達 · 順位差 -35.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 10.0
      },
      "new": "007fb170",
      "score": 35.0
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
      "new": "007fb180",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-46d386ba92028cdb67c221c1f1a6678c"></a>

### v16.0.0 [`00830594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830594.md) FUN_00830594

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007fb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb180.md) · スコア 60.0 · 採用条件未達 · 順位差 0.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007fb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb170.md) · スコア 25.0 · 採用条件未達 · 順位差 -10.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 35.0
      },
      "new": "007fb180",
      "score": 60.0
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
        "reverse_margin": -35.0
      },
      "new": "007fb170",
      "score": 25.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-835b1f43e540b5990010162abd651d71"></a>

### v16.0.0 [`008305c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008305c4.md) FUN_008305c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007fb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb1b0.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`007fb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb170.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb180.md) · スコア 0.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.0,
        "reverse_margin": 68.0
      },
      "new": "007fb1b0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fb170",
      "score": 1.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fb180",
      "score": 0.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v16.0.0 [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) FUN_008307b8

`competing_candidates` 

呼出元 8件 [`0081c8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081c8c4.md) [`00822fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00822/00822fd0.md) [`00823820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00823/00823820.md) [`00829354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00829/00829354.md) [`0082c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c344.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00830020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830020.md) [`008308c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008308c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`007fb3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb3a4.md) · スコア 61.898305 · 採用条件未達 · 順位差 7.436767000000003 / 7.118644000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00519534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519534.md) · スコア 54.779661 · 採用条件未達 · 順位差 5.018466999999994 / -7.118644000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0063995c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063995c.md) · スコア 50.461538 · 採用条件未達 · 順位差 26.073477999999998 / -11.436767000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) · スコア 47.809414 · 採用条件未達 · 順位差 23.421353999999997 / -14.088891000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a4ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md) · スコア 47.19403 · 採用条件未達 · 順位差 22.80597 / -14.704275000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005714ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md) · スコア 42.979021 · 採用条件未達 · 順位差 25.755140000000004 / -18.919283999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0070fdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070f/0070fdfc.md) · スコア 35.838384 · 採用条件未達 · 順位差 20.405547999999996 / -26.059921000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00adb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md) · スコア 35.507246 · 採用条件未達 · 順位差 35.507246 / -26.391059 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8983050847457628,
          0.8983050847457628
        ],
        "cfg_coverage": [
          0.3,
          0.3
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 7.436767000000003,
        "reverse_margin": 7.118644000000003
      },
      "new": "007fb3a4",
      "score": 61.898305
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8070175438596491,
          0.7796610169491526
        ],
        "cfg_coverage": [
          0.3,
          0.3
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 5.018466999999994,
        "reverse_margin": -7.118644000000003
      },
      "new": "00519534",
      "score": 54.779661
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7076923076923077,
          0.7796610169491526
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.3
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 26.073477999999998,
        "reverse_margin": -11.436767000000003
      },
      "new": "0063995c",
      "score": 50.461538
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`008308c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008308c8.md) FUN_008308c8

`competing_candidates` 

呼出元 1件 [`008307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/008307b8.md) · 呼出先 0件 

- 1. [`00418de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418de8.md) · スコア 78.666667 · 採用条件未達 · 順位差 1.199918000000011 / 0.0 · cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0067c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c560.md) · スコア 78.666667 · 採用条件未達 · 順位差 1.199918000000011 / 0.0 · cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a2924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a2924c.md) · スコア 78.666667 · 採用条件未達 · 順位差 1.199918000000011 / 0.0 · cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a500dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md) · スコア 78.666667 · 採用条件未達 · 順位差 1.199918000000011 / 0.0 · cfg_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0062ccdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ccdc.md) · スコア 74.672058 · 採用条件未達 · 順位差 -0.38634299999999655 / -3.994608999999997 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a439a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a439a0.md) · スコア 73.539982 · 採用条件未達 · 順位差 0.8834979999999888 / -5.126685000000009 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00639a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639a84.md) · スコア 73.298844 · 採用条件未達 · 順位差 -1.8563599999999951 / -5.367823000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a53614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53614.md) · スコア 71.521607 · 採用条件未達 · 順位差 0.6017960000000073 / -7.145060000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.9491525423728814,
          0.9333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.199918000000011,
        "reverse_margin": 0.0
      },
      "new": "00418de8",
      "score": 78.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          0.9491525423728814,
          0.9333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.199918000000011,
        "reverse_margin": 0.0
      },
      "new": "0067c560",
      "score": 78.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          1.0
        ],
        "cfg_coverage": [
          0.9491525423728814,
          0.9333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.199918000000011,
        "reverse_margin": 0.0
      },
      "new": "00a2924c",
      "score": 78.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e0547d215634d4cd022429f38fb67d81"></a>

### v16.0.0 [`00830a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830a70.md) FUN_00830a70

`competing_candidates` 

呼出元 1件 [`0082463c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00824/0082463c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

- 1. [`007fb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb65c.md) · スコア 58.0 · 採用条件未達 · 順位差 58.0 / 58.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "mapped_data": 1,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 58.0,
        "reverse_margin": 58.0
      },
      "new": "007fb65c",
      "score": 58.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ed32ac13e7c80d89223323ee876e74d3"></a>

### v16.0.0 [`00830a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830a84.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007fb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb65c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 2. [`007fb4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb4b4.md) · スコア 0.0377 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fc484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc484.md) · スコア 0.0286 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fbbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbbc8.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fb670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb670.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc6b4.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 7. [`007fbf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbf48.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007fb65c",
      "score": 0.8
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fb4b4",
      "score": 0.0377
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fc484",
      "score": 0.0286
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-dc62c24cf91174428a0c18e1d68c5b92"></a>

### v16.0.0 [`00830a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830a88.md) FUN_00830a88

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00672688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md) · スコア 33.75 · 採用条件未達 · 順位差 -35.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007ff11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff11c.md) · スコア 33.75 · 採用条件未達 · 順位差 -35.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008ffc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ff/008ffc98.md) · スコア 33.75 · 採用条件未達 · 順位差 -35.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005f28e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f28e8.md) · スコア 22.5 · 採用条件未達 · 順位差 -27.5 / -11.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00638d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638d6c.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006392c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006392c4.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00639404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639404.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007c8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8038.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": -35.0,
        "reverse_margin": 0.0
      },
      "new": "00672688",
      "score": 33.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5625,
          0.5625
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
        "margin": -35.0,
        "reverse_margin": 0.0
      },
      "new": "007ff11c",
      "score": 33.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5625,
          0.5625
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
        "margin": -35.0,
        "reverse_margin": 0.0
      },
      "new": "008ffc98",
      "score": 33.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1c8b0d3c55caf5107a171e62dcbbd015"></a>

### v16.0.0 [`00830ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830ac8.md) FUN_00830ac8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007fc484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc484.md) · スコア 0.3943 · 採用条件未達 · 順位差 — / — · 
- 2. [`007fbbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbbc8.md) · スコア 0.3086 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fcc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcc0c.md) · スコア 0.3086 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fb670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fb670.md) · スコア 0.308 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc6b4.md) · スコア 0.308 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fd4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fd4c8.md) · スコア 0.308 · 採用条件未達 · 順位差 0.0236 / -68.692 · 
- 7. [`007fbf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbf48.md) · スコア 0.0955 · 採用条件未達 · 順位差 — / — · 
- 8. [`007fcf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcf8c.md) · スコア 0.0955 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007fc484",
      "score": 0.3943
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fbbc8",
      "score": 0.3086
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fcc0c",
      "score": 0.3086
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5ffcac2d60e521483a259c751ed7a38b"></a>

### v16.0.0 [`00830ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830ae8.md) FUN_00830ae8

`competing_candidates` 

呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 0件 

- 1. [`007fc484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc484.md) · スコア 0.0286 · 採用条件未達 · 順位差 — / — · 
- 2. [`007fbbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbbc8.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fcc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcc0c.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc6b4.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fd4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fd4c8.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fbf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbf48.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 
- 7. [`007fcf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcf8c.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007fc484",
      "score": 0.0286
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fbbc8",
      "score": 0.0179
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fcc0c",
      "score": 0.0179
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-17619fa9c858bbe5829c651d17b9a47e"></a>

### v16.0.0 [`00830aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830aec.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007fc484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc484.md) · スコア 0.0286 · 採用条件未達 · 順位差 — / — · 
- 2. [`007fcc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcc0c.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fda34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fda34.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fc6b4.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fd4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fd4c8.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fbf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fb/007fbf48.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 
- 7. [`007fcf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcf8c.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007fc484",
      "score": 0.0286
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fcc0c",
      "score": 0.0179
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fda34",
      "score": 0.0179
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-32151bbce8c5d3df95fbbbc894c8d2c2"></a>

### v16.0.0 [`00830af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830af0.md) FUN_00830af0

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ab0be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0be0.md) [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md)

- 1. [`007ff184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff184.md) · スコア 18.75 · 採用条件未達 · 順位差 -23.75 / 18.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0063e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e6d4.md) · スコア 0.0 · 採用条件未達 · 順位差 -13.5 / -18.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00689200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689200.md) · スコア 0.0 · 採用条件未達 · 順位差 -22.5 / -18.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007f78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78a8.md) · スコア 0.0 · 採用条件未達 · 順位差 -45.714286 / -18.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3125,
          0.3125
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
        "margin": -23.75,
        "reverse_margin": 18.75
      },
      "new": "007ff184",
      "score": 18.75
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
        "margin": -13.5,
        "reverse_margin": -18.75
      },
      "new": "0063e6d4",
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
        "margin": -22.5,
        "reverse_margin": -18.75
      },
      "new": "00689200",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-058c77332fbdcf16b927c5d17b42ef30"></a>

### v16.0.0 [`00830b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830b30.md) FUN_00830b30

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007ff1c4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3cb89fd158c76a8da53c8eebe156ec06"></a>

### v16.0.0 [`00830b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830b4c.md) FUN_00830b4c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007fcc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcc0c.md) · スコア 0.0536 · 採用条件未達 · 順位差 — / — · 
- 2. [`007fda34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fda34.md) · スコア 0.0536 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fe85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe85c.md) · スコア 0.0536 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fd4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fd4c8.md) · スコア 0.0533 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fe2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe2f0.md) · スコア 0.0533 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fcf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcf8c.md) · スコア 0.0358 · 採用条件未達 · 順位差 — / — · 
- 7. [`007fddb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fddb4.md) · スコア 0.0358 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007fcc0c",
      "score": 0.0536
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fda34",
      "score": 0.0536
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fe85c",
      "score": 0.0536
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e43c8a1361cef90d7a5bc8a96147b1f9"></a>

### v16.0.0 [`00830b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830b58.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007ff118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff118.md) · スコア 73.0 · 採用条件未達 · 順位差 0.0 / 72.9672 · 
- 2. [`007fda34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fda34.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 3. [`007fe85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe85c.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fd4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fd4c8.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fe2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe2f0.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fcf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fc/007fcf8c.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 
- 7. [`007fddb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fddb4.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 
- 8. [`007febdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007febdc.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 0.0,
        "reverse_margin": 72.9672
      },
      "new": "007ff118",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fda34",
      "score": 0.0179
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007fe85c",
      "score": 0.0179
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-18442686cc175be0912ff7d0db893218"></a>

### v16.0.0 [`00830b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830b5c.md) FUN_00830b5c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00856700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856700.md) · スコア 75.384615 · 採用条件未達 · 順位差 75.384615 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00a3c600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c600.md) · スコア 75.384615 · 採用条件未達 · 順位差 75.384615 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009843fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843fc.md) · スコア 23.076923 · 採用条件未達 · 順位差 -24.615384999999996 / -52.307691999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "reverse_margin": 0.0
      },
      "new": "00856700",
      "score": 75.384615
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
        "reverse_margin": 0.0
      },
      "new": "00a3c600",
      "score": 75.384615
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -24.615384999999996,
        "reverse_margin": -52.307691999999996
      },
      "new": "009843fc",
      "score": 23.076923
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cb884b645904f24b9aedeb045fe19ed8"></a>

### v16.0.0 [`00830b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830b90.md) FUN_00830b90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00984430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984430.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00a3c634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c634.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00984430",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 80.0,
        "reverse_margin": 0.0
      },
      "new": "00a3c634",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-336f44709148f8df7789810e462342e5"></a>

### v16.0.0 [`00830ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830ba4.md) FUN_00830ba4

`competing_candidates` 

呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 0件 

- 1. [`007ff17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff17c.md) · スコア 54.0 · 採用条件未達 · 順位差 50.0 / 50.0 · 
- 2. [`007ff118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff118.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`007ff180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff180.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fe85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe85c.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 5. [`007fe2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe2f0.md) · スコア 0.0178 · 採用条件未達 · 順位差 — / — · 
- 6. [`007fddb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fd/007fddb4.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 
- 7. [`007febdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007febdc.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007ff17c",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff118",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff180",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-28257270fedb5263f40bff5f6ffd0f52"></a>

### v16.0.0 [`00830ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830ba8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007ff118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff118.md) · スコア 73.0 · 採用条件未達 · 順位差 — / — · 
- 2. [`007ff180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff180.md) · スコア 73.0 · 採用条件未達 · 順位差 67.4167 / 0.0 · 
- 3. [`007ff17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff17c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`007fe85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007fe85c.md) · スコア 0.0179 · 採用条件未達 · 順位差 — / — · 
- 5. [`007febdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007febdc.md) · スコア 0.0119 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff118",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 67.4167,
        "reverse_margin": 0.0
      },
      "new": "007ff180",
      "score": 73.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff17c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-98dfb8b0c32a50cc1319d57eed3e2b16"></a>

### v16.0.0 [`00830bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830bac.md) FUN_00830bac

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bb30.md) [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md)

- 1. [`007f78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78a8.md) · スコア 27.2 · 採用条件未達 · 順位差 -18.514286000000002 / 27.2 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ff184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff184.md) · スコア 0.0 · 採用条件未達 · 順位差 -42.5 / -27.2 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -27.2 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff240.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.5 / -27.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0085cd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085cd28.md) · スコア 0.0 · 採用条件未達 · 順位差 -50.0 / -27.2 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0089c82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089c82c.md) · スコア 0.0 · 採用条件未達 · 順位差 -26.0 / -27.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a1fd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd88.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.0 / -27.2 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00aa97bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md) · スコア 0.0 · 採用条件未達 · 順位差 -5.853659 / -27.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.12
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
        "margin": -18.514286000000002,
        "reverse_margin": 27.2
      },
      "new": "007f78a8",
      "score": 27.2
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
        "margin": -42.5,
        "reverse_margin": -27.2
      },
      "new": "007ff184",
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
        "reverse_margin": -27.2
      },
      "new": "007ff1c4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d83d8bf3bf931c846cc148638eab259"></a>

### v16.0.0 [`00830c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830c10.md) FUN_00830c10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 8.571427999999997 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 8.571427999999997,
        "reverse_margin": 54.285714
      },
      "new": "007ff2a4",
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
      "new": "007ff1c4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b1a7c5967bd7330612a4ea762c426440"></a>

### v16.0.0 [`00830c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830c2c.md) FUN_00830c2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1e0.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 67.2857 · 
- 2. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007ff17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff17c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`007ff180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff180.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`007ff1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1ec.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007ff1e0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff1c4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff17c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5dea100310545218ba4c3a21dc493157"></a>

### v16.0.0 [`00830c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830c38.md) FUN_00830c38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ff224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff224.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007ff1c4",
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
        "margin": -66.153846,
        "reverse_margin": 0.0
      },
      "new": "007ff1f0",
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
      "new": "007ff224",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9cafc063207c33a9cf3495c1c15d9dda"></a>

### v16.0.0 [`00830c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830c7c.md) FUN_00830c7c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 10.434783 · 採用条件未達 · 順位差 -55.719063000000006 / 10.434783 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ff1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1c4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -10.434783 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3076923076923077,
          0.17391304347826086
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
        "margin": -55.719063000000006,
        "reverse_margin": 10.434783
      },
      "new": "007ff1f0",
      "score": 10.434783
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
        "reverse_margin": -10.434783
      },
      "new": "007ff1c4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fad80bd90e1260fe852629372ea72393"></a>

### v16.0.0 [`00830cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830cd8.md) FUN_00830cd8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -66.153846,
        "reverse_margin": 0.0
      },
      "new": "007ff1f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-17670292e8f64c7e04ba8388d3b6a4e7"></a>

### v16.0.0 [`00830d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830d60.md) FUN_00830d60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -66.153846,
        "reverse_margin": 0.0
      },
      "new": "007ff1f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e67745269f3d2625f1b371183c7dac36"></a>

### v16.0.0 [`00830dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830dd4.md) FUN_00830dd4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00981c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c3c.md) · スコア 69.411765 · 採用条件未達 · 順位差 0.0 / 26.218488 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) · スコア 43.193277 · 採用条件未達 · 順位差 -29.747898999999997 / -26.218488 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / -69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ff224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff224.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 26.218488
      },
      "new": "00981c3c",
      "score": 69.411765
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5294117647058824,
          0.6428571428571429
        ],
        "cfg_coverage": [
          0.6666666666666666,
          0.5714285714285714
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -29.747898999999997,
        "reverse_margin": -26.218488
      },
      "new": "007ff2cc",
      "score": 43.193277
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
        "margin": -66.153846,
        "reverse_margin": -69.411765
      },
      "new": "007ff1f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4e0fde4839b2a2e3f6be7acc8f44f1ce"></a>

### v16.0.0 [`00830e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830e0c.md) FUN_00830e0c

`competing_candidates` 

呼出元 1件 [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`007ff310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff310.md) · スコア 54.23913 · 採用条件未達 · 順位差 -17.934782999999996 / 12.667701000000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) · スコア 41.571429 · 採用条件未達 · 順位差 -31.369746999999997 / -12.667701000000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ff1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff1f0.md) · スコア 12.0 · 採用条件未達 · 順位差 -54.153846 / -42.23913 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ff224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff224.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.23913 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -54.23913 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.8
        ],
        "cfg_coverage": [
          0.625,
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
        "margin": -17.934782999999996,
        "reverse_margin": 12.667701000000001
      },
      "new": "007ff310",
      "score": 54.23913
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
        "margin": -31.369746999999997,
        "reverse_margin": -12.667701000000001
      },
      "new": "007ff2cc",
      "score": 41.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3076923076923077,
          0.2
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
        "margin": -54.153846,
        "reverse_margin": -42.23913
      },
      "new": "007ff1f0",
      "score": 12.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-21e90ad5e39ce365a2b73c04a2f90004"></a>

### v16.0.0 [`00830e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830e5c.md) FUN_00830e5c

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00acaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaacc.md)

- 1. [`00a3ca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3ca30.md) · スコア 63.125 · 採用条件未達 · 順位差 18.933081 / 2.916666999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007ff4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff4f0.md) · スコア 60.208333 · 採用条件未達 · 順位差 13.421546000000006 / -2.916666999999997 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 3. [`007c99e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c99e0.md) · スコア 45.555556 · 採用条件未達 · 順位差 -13.989898999999994 / -17.569443999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006d46f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46f8.md) · スコア 39.144144 · 採用条件未達 · 順位差 4.901719999999997 / -23.980856000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a91fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91fb0.md) · スコア 35.692308 · 採用条件未達 · 順位差 -3.8959270000000004 / -27.432692000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007cab98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007cab98.md) · スコア 35.0 · 採用条件未達 · 順位差 -6.818182 / -28.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a91e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e58.md) · スコア 26.882353 · 採用条件未達 · 順位差 -31.117647 / -36.242647000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`007c952c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c9/007c952c.md) · スコア 18.448276 · 採用条件未達 · 順位差 -17.344827000000002 / -44.676724 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7931034482758621,
          0.71875
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
        "margin": 18.933081,
        "reverse_margin": 2.916666999999997
      },
      "new": "00a3ca30",
      "score": 63.125
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.78125,
          0.78125
        ],
        "cfg_coverage": [
          0.6666666666666666,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.421546000000006,
        "reverse_margin": -2.916666999999997
      },
      "new": "007ff4f0",
      "score": 60.208333
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.6875
        ],
        "cfg_coverage": [
          0.7777777777777778,
          0.875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.989898999999994,
        "reverse_margin": -17.569443999999997
      },
      "new": "007c99e0",
      "score": 45.555556
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5a561b66859a29d4b23b378d433dac1f"></a>

### v16.0.0 [`00830edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830edc.md) FUN_00830edc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff570.md) · スコア 54.285714 · 採用条件未達 · 順位差 0.0 / 8.571427999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 45.714286 · 採用条件未達 · 順位差 -8.571427999999997 / -8.571427999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -72.941176 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ff310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff310.md) · スコア 0.0 · 採用条件未達 · 順位差 -72.173913 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ff468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff468.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 8.571427999999997
      },
      "new": "007ff570",
      "score": 54.285714
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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.571427999999997,
        "reverse_margin": -8.571427999999997
      },
      "new": "007ff2a4",
      "score": 45.714286
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
        "margin": -72.941176,
        "reverse_margin": -54.285714
      },
      "new": "007ff2cc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f2d0c7ee9ade0d6cce26e604811d034"></a>

### v16.0.0 [`00830ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830ef8.md) FUN_00830ef8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2c0.md) · スコア 69.0 · 採用条件未達 · 順位差 67.2857 / 67.2857 · 
- 2. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007ff468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff468.md) · スコア 0.8571 · 採用条件未達 · 順位差 — / — · 
- 4. [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) · スコア 0.7059 · 採用条件未達 · 順位差 — / — · 
- 5. [`007ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff4a0.md) · スコア 0.6 · 採用条件未達 · 順位差 — / — · 
- 6. [`007ff310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff310.md) · スコア 0.5217 · 採用条件未達 · 順位差 — / — · 
- 7. [`007ff36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff36c.md) · スコア 0.4138 · 採用条件未達 · 順位差 — / — · 
- 8. [`007ff3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff3f4.md) · スコア 0.4138 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007ff2c0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff2a4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007ff468",
      "score": 0.8571
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d1f95c595cf7d7f02481a0621cc717f4"></a>

### v16.0.0 [`00830f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830f04.md) FUN_00830f04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007ff2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2cc.md) · スコア 72.941176 · 採用条件未達 · 順位差 29.747898999999997 / 35.462184 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007ff468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff468.md) · スコア 37.478992 · 採用条件未達 · 順位差 -42.521008 / -35.462184 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`007ff4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff4a0.md) · スコア 23.0 · 採用条件未達 · 順位差 -25.0 / -49.941176 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ff310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff310.md) · スコア 18.152174 · 採用条件未達 · 順位差 -54.021739 / -54.789001999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`007ff3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff3f4.md) · スコア 2.068966 · 採用条件未達 · 順位差 -57.586206 / -70.87221 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007ff2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff2a4.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -72.941176 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007ff36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff36c.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.793103 / -72.941176 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8823529411764706,
          0.8823529411764706
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
        "margin": 29.747898999999997,
        "reverse_margin": 35.462184
      },
      "new": "007ff2cc",
      "score": 72.941176
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.5294117647058824
        ],
        "cfg_coverage": [
          0.2857142857142857,
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
        "margin": -42.521008,
        "reverse_margin": -35.462184
      },
      "new": "007ff468",
      "score": 37.478992
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35,
          0.4117647058823529
        ],
        "cfg_coverage": [
          0.1,
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
        "margin": -25.0,
        "reverse_margin": -49.941176
      },
      "new": "007ff4a0",
      "score": 23.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

