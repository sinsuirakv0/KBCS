# v15.7.4 → v16.0.0 · 追加調査 (127)

[一覧の目次](README.md)

<a id="review-53864871b915a7edc1045512c13e111d"></a>

### v16.0.0 [`007867cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md) FUN_007867cc

`competing_candidates` 

呼出元 1件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) · 呼出先 13件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00788374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788374.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) [`00a466d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466d0.md)

- 1. [`0075c330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md) · スコア 44.683761 · 採用条件未達 · 順位差 38.872422 / 36.888889 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007f61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f61cc.md) · スコア 7.794872 · 採用条件未達 · 順位差 2.4382289999999998 / -36.888889 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0075bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bf10.md) · スコア 5.787482 · 採用条件未達 · 順位差 -36.841487 / -38.896279 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a2baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2baf4.md) · スコア 5.752574 · 採用条件未達 · 順位差 -19.097704 / -38.931186999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0058f504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f504.md) · スコア 4.644689 · 採用条件未達 · 順位差 -14.377533 / -40.039072 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00770bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770bfc.md) · スコア 4.410256 · 採用条件未達 · 順位差 -6.700854999999999 / -40.273505 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007c5484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c5/007c5484.md) · スコア 4.410256 · 採用条件未達 · 順位差 -10.92128 / -40.273505 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008af36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md) · スコア 3.333079 · 採用条件未達 · 順位差 1.717745 / -41.350682 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6410256410256411,
          0.6410256410256411
        ],
        "cfg_coverage": [
          0.4117647058823529,
          0.3111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 38.872422,
        "reverse_margin": 36.888889
      },
      "new": "0075c330",
      "score": 44.683761
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1337579617834395,
          0.1076923076923077
        ],
        "cfg_coverage": [
          0.1111111111111111,
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
        "margin": 2.4382289999999998,
        "reverse_margin": -36.888889
      },
      "new": "007f61cc",
      "score": 7.794872
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07423580786026202,
          0.08717948717948718
        ],
        "cfg_coverage": [
          0.06666666666666667,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -36.841487,
        "reverse_margin": -38.896279
      },
      "new": "0075bf10",
      "score": 5.787482
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) FUN_00786b68

`competing_candidates` 

呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 8件 [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00a46950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46950.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

- 1. [`0075c6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c6cc.md) · スコア 47.454545 · 採用条件未達 · 順位差 38.363636 / 38.363636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00549ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549ac8.md) · スコア 9.090909 · 採用条件未達 · 順位差 7.542522 / -38.363636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00591df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591df8.md) · スコア 8.117073 · 採用条件未達 · 順位差 0.7999999999999998 / -39.337472000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a3479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a3479c.md) · スコア 5.789474 · 採用条件未達 · 順位差 -29.482767000000003 / -41.665071000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00977c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md) · スコア 5.454545 · 採用条件未達 · 順位差 -3.500678999999999 / -42.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00979c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979c10.md) · スコア 5.454545 · 採用条件未達 · 順位差 2.0742630000000006 / -42.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005221e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005221e4.md) · スコア 4.688995 · 採用条件未達 · 順位差 -0.828246 / -42.765550000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0070a03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a03c.md) · スコア 4.688995 · 採用条件未達 · 順位差 -1.212644 / -42.765550000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7575757575757576,
          0.7575757575757576
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
        "margin": 38.363636,
        "reverse_margin": 38.363636
      },
      "new": "0075c6cc",
      "score": 47.454545
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2564102564102564,
          0.15151515151515152
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
        "margin": 7.542522,
        "reverse_margin": -38.363636
      },
      "new": "00549ac8",
      "score": 9.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12195121951219512,
          0.15151515151515152
        ],
        "cfg_coverage": [
          0.04,
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
        "margin": 0.7999999999999998,
        "reverse_margin": -39.337472000000005
      },
      "new": "00591df8",
      "score": 8.117073
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b23474da30d97e0749e5af8934338309"></a>

### v16.0.0 [`00786c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md) FUN_00786c94

`competing_candidates` 

呼出元 1件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) · 呼出先 16件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`007884ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884ec.md) [`007884f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f0.md) [`008b6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)

- 1. [`0075c7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c7f8.md) · スコア 22.938515 · 採用条件未達 · 順位差 19.124413999999998 / 18.985692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0075c330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075c330.md) · スコア 3.952823 · 採用条件未達 · 順位差 -40.730937999999995 / -18.985692 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a03f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a03/00a03f2c.md) · スコア 2.950889 · 採用条件未達 · 順位差 -32.175298 / -19.987626 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00765cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00765/00765cf0.md) · スコア 2.923434 · 採用条件未達 · 順位差 -6.536142999999999 / -20.015081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) · スコア 2.909931 · 採用条件未達 · 順位差 -61.94721199999999 / -20.028584 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`004aad54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md) · スコア 2.645012 · 採用条件未達 · 順位差 -2.258834 / -20.293502999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a2baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2baf4.md) · スコア 2.264923 · 採用条件未達 · 順位差 -22.585355 / -20.673592 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) · スコア 2.143078 · 採用条件未達 · 順位差 -1.1194950000000001 / -20.795437 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35730858468677495,
          0.35730858468677495
        ],
        "cfg_coverage": [
          0.09183673469387756,
          0.075
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.124413999999998,
        "reverse_margin": 18.985692
      },
      "new": "0075c7f8",
      "score": 22.938515
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13333333333333333,
          0.060324825986078884
        ],
        "cfg_coverage": [
          0.058823529411764705,
          0.016666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -40.730937999999995,
        "reverse_margin": -18.985692
      },
      "new": "0075c330",
      "score": 3.952823
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.060790273556231005,
          0.04640371229698376
        ],
        "cfg_coverage": [
          0.014925373134328358,
          0.008333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.175298,
        "reverse_margin": -19.987626
      },
      "new": "00a03f2c",
      "score": 2.950889
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-109d7fe34c98ca919beb32da7c75b663"></a>

### v16.0.0 [`00787440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md) FUN_00787440

`competing_candidates` 

呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 4件 [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)

- 1. [`0075cfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075cfa4.md) · スコア 33.578947 · 採用条件未達 · 順位差 24.194332 / 31.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0076884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/0076884c.md) · スコア 2.0 · 採用条件未達 · 順位差 -47.116212 / -31.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0075d8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d8a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -3.428571 / -33.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b4e6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e6ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -6.315789 / -33.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5263157894736842,
          0.5263157894736842
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
        "margin": 24.194332,
        "reverse_margin": 31.578947
      },
      "new": "0075cfa4",
      "score": 33.578947
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
        "margin": -47.116212,
        "reverse_margin": -31.578947
      },
      "new": "0076884c",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.428571,
        "reverse_margin": -33.578947
      },
      "new": "0075d8a0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-722622ee688b3e302481482c9db260df"></a>

### v16.0.0 [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) FUN_007874d8

`competing_candidates` 

呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md) [`00806188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806188.md) [`00806264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806264.md)

- 1. [`0075d03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d03c.md) · スコア 30.379531 · 採用条件未達 · 順位差 21.879531 / 22.558635 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0074942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/0074942c.md) · スコア 7.820896 · 採用条件未達 · 順位差 -63.670937 / -22.558635 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0078acdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078a/0078acdc.md) · スコア 7.820896 · 採用条件未達 · 順位差 -65.36684299999999 / -22.558635 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00902dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00902/00902dd0.md) · スコア 7.373134 · 採用条件未達 · 順位差 -16.20094 / -23.006397 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0075b518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b518.md) · スコア 6.705882 · 採用条件未達 · 順位差 -5.141362 / -23.673649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007ab188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab188.md) · スコア 5.58209 · 採用条件未達 · 順位差 -54.885343 / -24.797441 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a251d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a251d8.md) · スコア 4.238806 · 採用条件未達 · 順位差 -6.053877 / -26.140725 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a25500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25500.md) · スコア 3.791045 · 採用条件未達 · 順位差 -1.4347610000000004 / -26.588486 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.475,
          0.4253731343283582
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.16216216216216217
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 21.879531,
        "reverse_margin": 22.558635
      },
      "new": "0075d03c",
      "score": 30.379531
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22413793103448276,
          0.09701492537313433
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
        "margin": -63.670937,
        "reverse_margin": -22.558635
      },
      "new": "0074942c",
      "score": 7.820896
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22413793103448276,
          0.09701492537313433
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
        "margin": -65.36684299999999,
        "reverse_margin": -22.558635
      },
      "new": "0078acdc",
      "score": 7.820896
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f34f14085887329fe8278f4bccb077cd"></a>

### v16.0.0 [`007876f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007876f0.md) FUN_007876f0

`competing_candidates` 

呼出元 1件 [`007858c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858c8.md) · 呼出先 0件 

- 1. [`0075d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d21c.md) · スコア 94.0 · 採用条件未達 · 順位差 93.6419 / 93.6419 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 93.6419,
        "reverse_margin": 93.6419
      },
      "new": "0075d21c",
      "score": 94.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-29bea54894fe6e8edfb6c86e6d5afe37"></a>

### v16.0.0 [`007876f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007876f8.md) FUN_007876f8

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`0075d224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d224.md) · スコア 15.469388 · 採用条件未達 · 順位差 5.996861000000001 / 15.469388 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0075d60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d60c.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.642857 / -15.469388 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00769c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769c2c.md) · スコア 0.0 · 採用条件未達 · 順位差 -18.461538 / -15.469388 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22448979591836735,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.996861000000001,
        "reverse_margin": 15.469388
      },
      "new": "0075d224",
      "score": 15.469388
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
        "margin": -66.642857,
        "reverse_margin": -15.469388
      },
      "new": "0075d60c",
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
        "margin": -18.461538,
        "reverse_margin": -15.469388
      },
      "new": "00769c2c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-053910e39ec18107987968d3383d5d2f"></a>

### v16.0.0 [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) FUN_007877bc

`competing_candidates` 

呼出元 1件 [`00788378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md) · 呼出先 10件 [`00785ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md) [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) [`00787440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)

- 1. [`0075d2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d2e8.md) · スコア 63.355014 · 採用条件未達 · 順位差 52.783584999999995 / 53.140727999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0075bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075bc70.md) · スコア 10.214286 · 採用条件未達 · 順位差 -38.071428 / -53.140727999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0044d28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d28c.md) · スコア 6.290323 · 採用条件未達 · 順位差 0.4838709999999997 / -57.064690999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) · スコア 5.853659 · 採用条件未達 · 順位差 -1.3023039999999995 / -57.501355 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) · スコア 5.853659 · 採用条件未達 · 順位差 -0.7518459999999996 / -57.501355 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009479b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/009479b4.md) · スコア 5.294118 · 採用条件未達 · 順位差 -47.721925000000006 / -58.060896 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005d63f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d63f8.md) · スコア 5.0 · 採用条件未達 · 順位差 -41.262821 / -58.355014 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005d16f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d16f0.md) · スコア 4.390244 · 採用条件未達 · 順位差 -25.334527 / -58.964769999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8373983739837398,
          0.8373983739837398
        ],
        "cfg_coverage": [
          0.5555555555555556,
          0.5555555555555556
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 52.783584999999995,
        "reverse_margin": 53.140727999999996
      },
      "new": "0075d2e8",
      "score": 63.355014
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13690476190476192,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -38.071428,
        "reverse_margin": -53.140727999999996
      },
      "new": "0075bc70",
      "score": 10.214286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10483870967741936,
          0.10569105691056911
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
        "margin": 0.4838709999999997,
        "reverse_margin": -57.064690999999996
      },
      "new": "0044d28c",
      "score": 6.290323
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d0a89093165ffb3435ba41bfa1ca881"></a>

### v16.0.0 [`007879a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007879a8.md) FUN_007879a8

`competing_candidates` 

呼出元 3件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00787ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ae0.md) [`007884f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f4.md) · 呼出先 3件 [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b6efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6efc.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`0075d4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d4d4.md) · スコア 13.538462 · 採用条件未達 · 順位差 7.504849000000001 / 4.065935000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0075d224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d224.md) · スコア 9.472527 · 採用条件未達 · 順位差 -5.996861000000001 / -4.065935000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a34c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34c78.md) · スコア 2.0 · 採用条件未達 · 順位差 -68.0 / -11.538462 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0075d60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d60c.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.642857 / -13.538462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19230769230769232,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 7.504849000000001,
        "reverse_margin": 4.065935000000001
      },
      "new": "0075d4d4",
      "score": 13.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12244897959183673,
          0.07692307692307693
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.996861000000001,
        "reverse_margin": -4.065935000000001
      },
      "new": "0075d224",
      "score": 9.472527
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
        "margin": -68.0,
        "reverse_margin": -11.538462
      },
      "new": "00a34c78",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd0185d8730aed72eaae5444d185d72e"></a>

### v16.0.0 [`00787ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787ae0.md) FUN_00787ae0

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`007879a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007879a8.md)

- 1. [`0075d60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d60c.md) · スコア 66.642857 · 採用条件未達 · 順位差 66.642857 / 66.642857 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9107142857142857,
          0.9107142857142857
        ],
        "cfg_coverage": [
          0.6,
          0.6
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 66.642857,
        "reverse_margin": 66.642857
      },
      "new": "0075d60c",
      "score": 66.642857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a7c3a62818fd1b76c1f76b38903d7da8"></a>

### v16.0.0 [`00787bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md) FUN_00787bc0

`competing_candidates` 

呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 8件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)

- 1. [`0075d6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d6ec.md) · スコア 38.845705 · 採用条件未達 · 順位差 29.341118 / 29.341118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) · スコア 9.504587 · 採用条件未達 · 順位差 -24.165224000000002 / -29.341118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`009e1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1430.md) · スコア 7.504587 · 採用条件未達 · 順位差 -20.209699 / -31.341118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008fb5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fb/008fb5f4.md) · スコア 5.086957 · 採用条件未達 · 順位差 -41.304347 / -33.758748000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`0060f5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f5cc.md) · スコア 4.96 · 採用条件未達 · 順位差 0.2933329999999996 / -33.885705 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) · スコア 4.813559 · 採用条件未達 · 順位差 -27.200102 / -34.032146000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`008f95c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f9/008f95c0.md) · スコア 4.598504 · 採用条件未達 · 順位差 -21.506759000000002 / -34.247201000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`008afd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008afd10.md) · スコア 4.566038 · 採用条件未達 · 順位差 -66.273585 / -34.279667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5504587155963303,
          0.5504587155963303
        ],
        "cfg_coverage": [
          0.09090909090909091,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 29.341118,
        "reverse_margin": 29.341118
      },
      "new": "0075d6ec",
      "score": 38.845705
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09433962264150944,
          0.09174311926605505
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
        "margin": -24.165224000000002,
        "reverse_margin": -29.341118
      },
      "new": "00897610",
      "score": 9.504587
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10989010989010989,
          0.09174311926605505
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
        "margin": -20.209699,
        "reverse_margin": -31.341118
      },
      "new": "009e1430",
      "score": 7.504587
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`007880ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007880ec.md) FUN_007880ec

`competing_candidates` 

呼出元 1件 [`00764a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md) · 呼出先 2件 [`00788774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788774.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

- 1. [`0075dc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dc18.md) · スコア 65.944272 · 採用条件未達 · 順位差 -10.526316000000008 / 1.1764699999999948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00588ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588ce8.md) · スコア 64.767802 · 採用条件未達 · 順位差 64.767802 / -1.1764699999999948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0069d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069d8e0.md) · スコア 64.767802 · 採用条件未達 · 順位差 64.767802 / -1.1764699999999948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a6b1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md) · スコア 64.767802 · 採用条件未達 · 順位差 -11.702786000000003 / -1.1764699999999948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md) · スコア 63.591331 · 採用条件未達 · 順位差 63.591331 / -2.3529410000000013 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008647dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008647dc.md) · スコア 60.06192 · 採用条件未達 · 順位差 26.247878 / -5.882351999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0090126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/0090126c.md) · スコア 59.380805 · 採用条件未達 · 順位差 59.380805 / -6.563466999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00588db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588db4.md) · スコア 57.956656 · 採用条件未達 · 順位差 43.768622 / -7.987615999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9411764705882353,
          0.9411764705882353
        ],
        "cfg_coverage": [
          0.5625,
          0.47368421052631576
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.526316000000008,
        "reverse_margin": 1.1764699999999948
      },
      "new": "0075dc18",
      "score": 65.944272
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9215686274509803,
          0.9215686274509803
        ],
        "cfg_coverage": [
          0.5625,
          0.47368421052631576
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 64.767802,
        "reverse_margin": -1.1764699999999948
      },
      "new": "00588ce8",
      "score": 64.767802
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9215686274509803,
          0.9215686274509803
        ],
        "cfg_coverage": [
          0.5625,
          0.47368421052631576
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 64.767802,
        "reverse_margin": -1.1764699999999948
      },
      "new": "0069d8e0",
      "score": 64.767802
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a7563559b41b0621a5858b25f55f3b0d"></a>

### v16.0.0 [`007881f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881f0.md) FUN_007881f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd1c.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 56.0,
        "reverse_margin": 56.0
      },
      "new": "0075dd1c",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-298a8a46367b484ac2da66da47c1ea86"></a>

### v16.0.0 [`00788204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788204.md) FUN_00788204

`competing_candidates` 

呼出元 1件 [`007863ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md) · 呼出先 0件 

- 1. [`0075dd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd30.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`0075dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dd1c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.2,
        "reverse_margin": 68.2
      },
      "new": "0075dd30",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0075dd1c",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cccb1c448ec1e1d7cb10f2a2a3657ac5"></a>

### v16.0.0 [`007882e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007882e4.md) FUN_007882e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075de10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de10.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0075de10",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9160e6e74a96b991b3d3748e4e27cf13"></a>

### v16.0.0 [`00788300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788300.md) FUN_00788300

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075de2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de2c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0075de10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de10.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0075de2c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0075de10",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0385e6442e27559fb9860aba53276fee"></a>

### v16.0.0 [`00788350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788350.md) FUN_00788350

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de7c.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008ee76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ee/008ee76c.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007c8c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c8c50.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -65.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0075de7c",
      "score": 65.0
    },
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "008ee76c",
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
        "reverse_margin": -65.0
      },
      "new": "007c8c50",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fc02c81d43903da38391de3f45264046"></a>

### v16.0.0 [`00788370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788370.md) FUN_00788370

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075de9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de9c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.5 / 68.5 · 
- 2. [`0075de7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075de7c.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.5,
        "reverse_margin": 68.5
      },
      "new": "0075de9c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0075de7c",
      "score": 0.5
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f4278855cabe2b3900153d6277ee10dd"></a>

### v16.0.0 [`00788460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788460.md) FUN_00788460

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075df8c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0075df8c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ffb61b1442ba7f832f164bd70565ab7f"></a>

### v16.0.0 [`0078847c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078847c.md) FUN_0078847c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075dfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dfa8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0075df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075df8c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0075dfa8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0075df8c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1df45a7313d048d3d70bdad3993e6d08"></a>

### v16.0.0 [`007884cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884cc.md) FUN_007884cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075dff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075dff8.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 65.0
      },
      "new": "0075dff8",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ffeca48942b59c7eb5fc99b7b22bc2e0"></a>

### v16.0.0 [`007884ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884ec.md) FUN_007884ec

`competing_candidates` 

呼出元 1件 [`00786c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md) · 呼出先 0件 

- 1. [`0075e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e018.md) · スコア 69.0 · 採用条件未達 · 順位差 68.5 / 68.5 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.5,
        "reverse_margin": 68.5
      },
      "new": "0075e018",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7584494c20f12631e31ba8e56e3b10b5"></a>

### v16.0.0 [`0078874c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078874c.md) FUN_0078874c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006d608c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d608c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0075e278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e278.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "006d608c",
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
        "margin": 54.285714,
        "reverse_margin": -25.714286
      },
      "new": "0075e278",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-730db7400d0fd67b053527d675559b37"></a>

### v16.0.0 [`00788768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788768.md) FUN_00788768

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0075e294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e294.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0075e278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e278.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0075e294",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0075e278",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fda1fb4e99ecf729376d408c2051821c"></a>

### v16.0.0 [`00789c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md) FUN_00789c10

`competing_candidates` 

呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 13件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`006766ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006766ec.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md)

- 1. [`0075f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f73c.md) · スコア 30.525 · 採用条件未達 · 順位差 30.343182 / 26.57378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`0075d2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d2e8.md) · スコア 3.95122 · 採用条件未達 · 順位差 -59.403794 / -26.57378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005ce03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ce03c.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.336898 / -30.525 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.39,
          0.39
        ],
        "cfg_coverage": [
          0.15625,
          0.19230769230769232
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 30.343182,
        "reverse_margin": 26.57378
      },
      "new": "0075f73c",
      "score": 30.525
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.032520325203252036,
          0.04
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
        "margin": -59.403794,
        "reverse_margin": -26.57378
      },
      "new": "0075d2e8",
      "score": 3.95122
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
        "margin": -32.336898,
        "reverse_margin": -30.525
      },
      "new": "005ce03c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5375d157d34f7a56daaeaa810809e227"></a>

### v16.0.0 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) FUN_00789da0

`competing_candidates` 

呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 64件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md)

- 1. [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) · スコア 48.552548 · 採用条件未達 · 順位差 37.291469 / 37.198198000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a34cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34cc8.md) · スコア 11.35435 · 採用条件未達 · 順位差 -52.444176 / -37.198198000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · スコア 8.107479 · 採用条件未達 · 順位差 -23.701901999999997 / -40.445069000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`008bc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md) · スコア 6.350133 · 採用条件未達 · 順位差 -0.030095000000000205 / -42.202415 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 5. [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) · スコア 6.318302 · 採用条件未達 · 順位差 -44.738994 / -42.234246 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`008e68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e68f8.md) · スコア 6.189204 · 採用条件未達 · 順位差 -28.375288 / -42.363344 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · スコア 6.0 · 採用条件未達 · 順位差 -16.043619 / -42.552548 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`00a1bb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1b/00a1bb7c.md) · スコア 4.363269 · 採用条件未達 · 順位差 -38.705979 / -44.189279 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5655172413793104,
          0.5655172413793104
        ],
        "cfg_coverage": [
          0.23107569721115537,
          0.2538293216630197
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 37.291469,
        "reverse_margin": 37.198198000000005
      },
      "new": "0075f8cc",
      "score": 48.552548
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01537307836520435,
          0.021750663129973476
        ],
        "cfg_coverage": [
          0.02159827213822894,
          0.02188183807439825
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -52.444176,
        "reverse_margin": -37.198198000000005
      },
      "new": "00a34cc8",
      "score": 11.35435
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0017913121361397223,
          0.00636604774535809
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
        "margin": -23.701901999999997,
        "reverse_margin": -40.445069000000004
      },
      "new": "00749514",
      "score": 8.107479
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-edddf0f8039f39ddd9aac934e5a3104b"></a>

### v16.0.0 [`0078bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md) FUN_0078bd18

`competing_candidates` 

呼出元 1件 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) · 呼出先 12件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078e8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8d4.md)

- 1. [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) · スコア 33.375 · 採用条件未達 · 順位差 6.589286000000001 / 7.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) · スコア 26.25 · 採用条件未達 · 順位差 -33.919492 / -7.125 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) · スコア 9.125 · 採用条件未達 · 順位差 -35.159112 / -24.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007ca13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca13c.md) · スコア 8.625 · 採用条件未達 · 順位差 -6.623670000000001 / -24.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) · スコア 7.625 · 採用条件未達 · 順位差 -35.008333 / -25.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007cc93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007cc93c.md) · スコア 7.125 · 採用条件未達 · 順位差 -36.294233 / -26.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md) · スコア 5.954545 · 採用条件未達 · 順位差 -1.1783219999999996 / -27.420455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00764408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764408.md) · スコア 2.125 · 採用条件未達 · 順位差 -26.671296 / -31.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.48333333333333334,
          0.48333333333333334
        ],
        "cfg_coverage": [
          0.25,
          0.21875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.589286000000001,
        "reverse_margin": 7.125
      },
      "new": "00761844",
      "score": 33.375
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3813559322033898,
          0.375
        ],
        "cfg_coverage": [
          0.21428571428571427,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.919492,
        "reverse_margin": -7.125
      },
      "new": "00761ab0",
      "score": 26.25
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1588785046728972,
          0.14166666666666666
        ],
        "cfg_coverage": [
          0.04,
          0.03125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.159112,
        "reverse_margin": -24.25
      },
      "new": "00a33760",
      "score": 9.125
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b980ef69a825644a9e7312f3d80876f7"></a>

### v16.0.0 [`0078bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md) FUN_0078bf84

`competing_candidates` 

呼出元 1件 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md)

- 1. [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) · スコア 60.169492 · 採用条件未達 · 順位差 33.919492 / 33.383778 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) · スコア 26.785714 · 採用条件未達 · 順位差 -6.589286000000001 / -33.383778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) · スコア 15.66586 · 採用条件未達 · 順位差 6.565860000000001 / -44.503631999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) · スコア 14.64891 · 採用条件未達 · 順位差 5.826688000000001 / -45.520582 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00848bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848bc0.md) · スコア 13.42615 · 採用条件未達 · 順位差 4.217454 / -46.743342 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) · スコア 9.358354 · 採用条件未達 · 順位差 -33.274979 / -50.811138 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) · スコア 7.83293 · 採用条件未達 · 順位差 -36.451182 / -52.336562 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ad9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9118.md) · スコア 6.307506 · 採用条件未達 · 順位差 -13.300336999999999 / -53.861986 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6694915254237288,
          0.6694915254237288
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
        "margin": 33.919492,
        "reverse_margin": 33.383778
      },
      "new": "00761ab0",
      "score": 60.169492
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.375,
          0.3813559322033898
        ],
        "cfg_coverage": [
          0.21428571428571427,
          0.21428571428571427
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.589286000000001,
        "reverse_margin": -33.383778
      },
      "new": "00761844",
      "score": 26.785714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3218390804597701,
          0.23728813559322035
        ],
        "cfg_coverage": [
          0.08333333333333333,
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
        "margin": 6.565860000000001,
        "reverse_margin": -44.503631999999996
      },
      "new": "008423bc",
      "score": 15.66586
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-04e103314776bcf0e79251f81bce1bcc"></a>

### v16.0.0 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) FUN_0078def8

`competing_candidates` 

呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00606448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md)

- 1. [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) · スコア 48.351852 · 採用条件未達 · 順位差 34.724494 / 38.106482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f2714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2714.md) · スコア 10.24537 · 採用条件未達 · 順位差 -38.411302 / -38.106482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0060081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/0060081c.md) · スコア 8.74537 · 採用条件未達 · 順位差 -35.375842 / -39.606482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008a4bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4bfc.md) · スコア 8.74537 · 採用条件未達 · 順位差 -20.988619999999997 / -39.606482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00764190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764190.md) · スコア 6.87037 · 採用条件未達 · 順位差 4.421390000000001 / -41.481482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a59cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59cf4.md) · スコア 6.75 · 採用条件未達 · 順位差 -23.027778 / -41.601852 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0043aadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md) · スコア 5.24537 · 採用条件未達 · 順位差 -4.159019 / -43.106482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00988400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988400.md) · スコア 4.861111 · 採用条件未達 · 順位差 -6.477472 / -43.490741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.575,
          0.575
        ],
        "cfg_coverage": [
          0.6037735849056604,
          0.5925925925925926
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.724494,
        "reverse_margin": 38.106482
      },
      "new": "00763a24",
      "score": 48.351852
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2413793103448276,
          0.13125
        ],
        "cfg_coverage": [
          0.043478260869565216,
          0.018518518518518517
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -38.411302,
        "reverse_margin": -38.106482
      },
      "new": "005f2714",
      "score": 10.24537
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18888888888888888,
          0.10625
        ],
        "cfg_coverage": [
          0.022727272727272728,
          0.018518518518518517
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -35.375842,
        "reverse_margin": -39.606482
      },
      "new": "0060081c",
      "score": 8.74537
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-338cd2b383db1ae528e74fa2f9bf41d5"></a>

### v16.0.0 [`0078e1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e1c4.md) FUN_0078e1c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00763cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763cf0.md) · スコア 54.285714 · 採用条件未達 · 順位差 20.0 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 20.0,
        "reverse_margin": 54.285714
      },
      "new": "00763cf0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4f3c96546222dbd71b0321def1887cab"></a>

### v16.0.0 [`0078e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e1e0.md) FUN_0078e1e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00763d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d0c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00763cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763cf0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00763d0c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00763cf0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f5ae7f965c6c0563b5f5ebbb30346394"></a>

### v16.0.0 [`0078e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md) FUN_0078e240

`competing_candidates` 

呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md) [`007441fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441fc.md) [`0080018c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/0080018c.md)

- 1. [`00763d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763d6c.md) · スコア 39.52381 · 採用条件未達 · 順位差 34.110276 / 33.142858 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f182c.md) · スコア 6.380952 · 採用条件未達 · 順位差 -56.730159 / -33.142858 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a3b254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b254.md) · スコア 5.904762 · 採用条件未達 · 順位差 -53.738095 / -33.619048 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md) · スコア 5.714286 · 採用条件未達 · 順位差 5.714286 / -33.809523999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a44d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44d74.md) · スコア 4.511278 · 採用条件未達 · 順位差 -3.1206449999999997 / -35.012532 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00993f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00993/00993f28.md) · スコア 3.564356 · 採用条件未達 · 順位差 -9.810847 / -35.959453999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) · スコア 3.5 · 採用条件未達 · 順位差 -44.851852 / -36.02381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0075d8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075d/0075d8a0.md) · スコア 3.428571 · 採用条件未達 · 順位差 3.428571 / -36.095239 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5142857142857142,
          0.5142857142857142
        ],
        "cfg_coverage": [
          0.3684210526315789,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 34.110276,
        "reverse_margin": 33.142858
      },
      "new": "00763d6c",
      "score": 39.52381
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.05714285714285714
        ],
        "cfg_coverage": [
          0.125,
          0.047619047619047616
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -56.730159,
        "reverse_margin": -33.142858
      },
      "new": "005f182c",
      "score": 6.380952
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.125,
          0.06666666666666667
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
        "margin": -53.738095,
        "reverse_margin": -33.619048
      },
      "new": "00a3b254",
      "score": 5.904762
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b91b4db04ce53f003fac0da027f3ef84"></a>

### v16.0.0 [`0078e3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e3e4.md) FUN_0078e3e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00763f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f10.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 54.285714
      },
      "new": "00763f10",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5a68ce9add6d81507657c940d5eebd62"></a>

### v16.0.0 [`0078e400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e400.md) FUN_0078e400

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00763f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f2c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00763f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f10.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00763f2c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00763f10",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a8177d4ed829558e593e114e848e0a97"></a>

### v16.0.0 [`0078e460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e460.md) FUN_0078e460

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`00763f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763f8c.md) · スコア 57.294118 · 採用条件未達 · 順位差 55.294118 / 37.294118 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00763fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763fd0.md) · スコア 20.0 · 採用条件未達 · 順位差 20.0 / -37.294118 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5882352941176471,
          0.5882352941176471
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
        "margin": 55.294118,
        "reverse_margin": 37.294118
      },
      "new": "00763f8c",
      "score": 57.294118
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
        "margin": 20.0,
        "reverse_margin": -37.294118
      },
      "new": "00763fd0",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-351ad2c35690fbc70b614362fa0feb2a"></a>

### v16.0.0 [`0078e4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e4a4.md) FUN_0078e4a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00601310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601310.md) · スコア 34.285714 · 採用条件未達 · 順位差 0.0 / 34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00763fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763fd0.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 34.285714
      },
      "new": "00601310",
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
        "margin": -20.0,
        "reverse_margin": -34.285714
      },
      "new": "00763fd0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5e405fabbce9e58cde63cf40d1e79524"></a>

### v16.0.0 [`0078e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e4c0.md) FUN_0078e4c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00763fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763fec.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00763fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763fd0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00763fec",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00763fd0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-343467b9747255d5df79380add72d277"></a>

### v16.0.0 [`0078e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e528.md) FUN_0078e528

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764054.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`00764074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764074.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00764058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764058.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "00764054",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764074",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764058",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0471042b186e433a068ef27dc93ac53e"></a>

### v16.0.0 [`0078e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e52c.md) FUN_0078e52c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764058.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00764058",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-80615b802783394a888752c3dd8dd3ad"></a>

### v16.0.0 [`0078e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e548.md) FUN_0078e548

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764074.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00764058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764058.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00764054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764054.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00764074",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764058",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764054",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-37582e0a80ecef6bfc0776872b4b0f87"></a>

### v16.0.0 [`0078e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e5a8.md) FUN_0078e5a8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)

- 1. [`007640d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007640d4.md) · スコア 22.5 · 採用条件未達 · 順位差 22.5 / 22.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00764114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764114.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -22.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.375,
          0.375
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
        "margin": 22.5,
        "reverse_margin": 22.5
      },
      "new": "007640d4",
      "score": 22.5
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
        "reverse_margin": -22.5
      },
      "new": "00764114",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c63f64d60e2b6f96faad0c1b5ad881ca"></a>

### v16.0.0 [`0078e5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e5e8.md) FUN_0078e5e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764114.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00764114",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4ee274721ae6ae938f89a85e0515dd87"></a>

### v16.0.0 [`0078e604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e604.md) FUN_0078e604

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764130.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00764114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764114.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00764130",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764114",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-223c5c66fe7fdc2cc494f19186e7b0e4"></a>

### v16.0.0 [`0078e778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e778.md) FUN_0078e778

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007642a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007642a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "007642a4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6527d5ecf885956b632b5c85b1109ef5"></a>

### v16.0.0 [`0078e794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e794.md) FUN_0078e794

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007642c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007642c0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007642a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007642a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007642c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007642a4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b9d339cbd710577f77e9aeb572e0b414"></a>

### v16.0.0 [`0078e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7f4.md) FUN_0078e7f4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0085bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bb30.md)

- 1. [`00764828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764828.md) · スコア 62.0 · 採用条件未達 · 順位差 35.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00764320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764320.md) · スコア 27.0 · 採用条件未達 · 順位差 -26.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00764370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764370.md) · スコア 20.0 · 採用条件未達 · 順位差 20.0 / -42.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a1fd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd88.md) · スコア 0.0 · 採用条件未達 · 順位差 -32.0 / -62.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": 35.0,
        "reverse_margin": 35.0
      },
      "new": "00764828",
      "score": 62.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45,
          0.45
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
        "margin": -26.0,
        "reverse_margin": -35.0
      },
      "new": "00764320",
      "score": 27.0
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
        "margin": 20.0,
        "reverse_margin": -42.0
      },
      "new": "00764370",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a9f77b39d5a4a3b0ec63743c0fa040f6"></a>

### v16.0.0 [`0078e844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e844.md) FUN_0078e844

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764370.md) · スコア 0.0 · 採用条件未達 · 順位差 -20.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -20.0,
        "reverse_margin": 0.0
      },
      "new": "00764370",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b66e4fe60f37ea8a84c989fb7acb2957"></a>

### v16.0.0 [`0078e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e860.md) FUN_0078e860

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076438c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076438c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00764370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764370.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0076438c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764370",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bf4945734beb94e1490fed0fa98c9823"></a>

### v16.0.0 [`0078e8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8bc.md) FUN_0078e8bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007643e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643e8.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "007643e8",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-266a1f6debdda2e69b3e1bf70b294e89"></a>

### v16.0.0 [`0078e8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8d4.md) FUN_0078e8d4

`competing_candidates` 

呼出元 1件 [`0078bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md) · 呼出先 0件 

- 1. [`00764400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764400.md) · スコア 69.0 · 採用条件未達 · 順位差 68.3333 / 68.3333 · 
- 2. [`007643e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007643e8.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00764400",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007643e8",
      "score": 0.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-64252068ce6c6eb18ca45d62ce455e2d"></a>

### v16.0.0 [`0078e8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md) FUN_0078e8dc

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf4.md) [`0078ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf8.md)

- 1. [`0076461c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076461c.md) · スコア 36.8438 · 採用条件未達 · 順位差 16.028985000000002 / 8.047504 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00764408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764408.md) · スコア 28.796296 · 採用条件未達 · 順位差 3.5541310000000017 / -8.047504 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0058cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cfe0.md) · スコア 16.474074 · 採用条件未達 · 順位差 -1.1498069999999991 / -20.369726 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0043aadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md) · スコア 9.404389 · 採用条件未達 · 順位差 3.4824859999999997 / -27.439411 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00583e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583e6c.md) · スコア 7.951807 · 採用条件未達 · 順位差 -8.172691 / -28.891993000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00770a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770a74.md) · スコア 7.058824 · 採用条件未達 · 順位差 5.819448 / -29.784976 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004c93c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md) · スコア 2.962963 · 採用条件未達 · 順位差 2.962963 / -33.880837 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a62748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62748.md) · スコア 2.696629 · 採用条件未達 · 順位差 -43.905832 / -34.147171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4691358024691358,
          0.4691358024691358
        ],
        "cfg_coverage": [
          0.5,
          0.43478260869565216
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.028985000000002,
        "reverse_margin": 8.047504
      },
      "new": "0076461c",
      "score": 36.8438
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38271604938271603,
          0.38271604938271603
        ],
        "cfg_coverage": [
          0.2916666666666667,
          0.30434782608695654
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.5541310000000017,
        "reverse_margin": -8.047504
      },
      "new": "00764408",
      "score": 28.796296
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2835820895522388,
          0.2345679012345679
        ],
        "cfg_coverage": [
          0.12,
          0.13043478260869565
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -1.1498069999999991,
        "reverse_margin": -20.369726
      },
      "new": "0058cfe0",
      "score": 16.474074
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7e6947e3cc335beb6220e52de374ced6"></a>

### v16.0.0 [`0078ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ea6c.md) FUN_0078ea6c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764598.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00764598",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-df01ba65102617bfc23b9f179f27c9f9"></a>

### v16.0.0 [`0078ea88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ea88.md) FUN_0078ea88

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007645b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007645b4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00764598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764598.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007645b4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764598",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f89266ea91dd159cb494cd89d46f3008"></a>

### v16.0.0 [`0078ead0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ead0.md) FUN_0078ead0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f1604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1604.md) · スコア 46.666667 · 採用条件未達 · 順位差 0.0 / 6.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005b7644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7644.md) · スコア 40.0 · 採用条件未達 · 順位差 40.0 / -6.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007645fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007645fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.3333333333333333,
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
        "margin": 0.0,
        "reverse_margin": 6.666666999999997
      },
      "new": "005f1604",
      "score": 46.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.6666666666666666
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
        "margin": 40.0,
        "reverse_margin": -6.666666999999997
      },
      "new": "005b7644",
      "score": 40.0
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
        "margin": -70.0,
        "reverse_margin": -46.666667
      },
      "new": "007645fc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5689f6a2972a1355ad50ec28b5152afe"></a>

### v16.0.0 [`0078eae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eae8.md) FUN_0078eae8

`competing_candidates` 

呼出元 1件 [`0078bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md) · 呼出先 0件 

- 1. [`00764614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764614.md) · スコア 69.0 · 採用条件未達 · 順位差 68.3333 / 68.3333 · 
- 2. [`007645fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007645fc.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00764614",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007645fc",
      "score": 0.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a875514d849d78c0a21faac3dffb3581"></a>

### v16.0.0 [`0078eaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md) FUN_0078eaf0

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf4.md) [`0078ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf8.md)

- 1. [`00764408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764408.md) · スコア 25.242165 · 採用条件未達 · 順位差 -3.5541310000000017 / 6.495726000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0085f63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f63c.md) · スコア 18.746439 · 採用条件未達 · 順位差 -19.151459 / -6.495726000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0076461c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076461c.md) · スコア 14.843305 · 採用条件未達 · 順位差 -22.000495 / -10.398859999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00588db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588db4.md) · スコア 14.188034 · 採用条件未達 · 順位差 -43.768622 / -11.054131 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00879ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ea8.md) · スコア 14.188034 · 採用条件未達 · 順位差 -14.161112000000001 / -11.054131 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0058f864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f864.md) · スコア 11.880342 · 採用条件未達 · 順位差 -37.119658 / -13.361823 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0058d660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d660.md) · スコア 11.225071 · 採用条件未達 · 順位差 -33.997151 / -14.017094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007717a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00771/007717a8.md) · スコア 11.139601 · 採用条件未達 · 順位差 -35.706553 / -14.102564 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3950617283950617,
          0.3950617283950617
        ],
        "cfg_coverage": [
          0.08333333333333333,
          0.07692307692307693
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.5541310000000017,
        "reverse_margin": 6.495726000000001
      },
      "new": "00764408",
      "score": 25.242165
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4594594594594595,
          0.20987654320987653
        ],
        "cfg_coverage": [
          0.4444444444444444,
          0.3076923076923077
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -19.151459,
        "reverse_margin": -6.495726000000001
      },
      "new": "0085f63c",
      "score": 18.746439
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2345679012345679,
          0.2345679012345679
        ],
        "cfg_coverage": [
          0.05,
          0.038461538461538464
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.000495,
        "reverse_margin": -10.398859999999999
      },
      "new": "0076461c",
      "score": 14.843305
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0238ae9f26c13b253d2df81f7069a5e3"></a>

### v16.0.0 [`0078ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ec80.md) FUN_0078ec80

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006e4524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4524.md) · スコア 62.857143 · 採用条件未達 · 順位差 62.857143 / 62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007647ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007647ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "006e4524",
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
        "reverse_margin": -62.857143
      },
      "new": "007647ac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c8e505cd0ac3d7cf9fdc3560ad8e2981"></a>

### v16.0.0 [`0078ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ec9c.md) FUN_0078ec9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007647c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007647c8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007647ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/007647ac.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007647c8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007647ac",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-179f672323cc7e302a7de6810cd5f616"></a>

### v16.0.0 [`0078ece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ece0.md) FUN_0078ece0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00717a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717a58.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00858a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a5c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0076480c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076480c.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00717a58",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00858a5c",
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
        "margin": 56.0,
        "reverse_margin": -24.0
      },
      "new": "0076480c",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-490912e02f45cd48d28ac3bfc6bbedd7"></a>

### v16.0.0 [`0078ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf4.md) FUN_0078ecf4

`competing_candidates` 

呼出元 4件 [`0078bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md) [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) [`0078e8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md) [`0078eaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md) · 呼出先 0件 

- 1. [`00764820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764820.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`0076480c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/0076480c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.2,
        "reverse_margin": 68.2
      },
      "new": "00764820",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0076480c",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-18fbe71ad423a8dbca0b25125d6355d9"></a>

### v16.0.0 [`0078ecfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecfc.md) FUN_0078ecfc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0085bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bb30.md)

- 1. [`00764320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764320.md) · スコア 53.0 · 採用条件未達 · 順位差 26.0 / 21.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a1fd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd88.md) · スコア 32.0 · 採用条件未達 · 順位差 6.285713999999999 / -21.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00764828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764828.md) · スコア 27.0 · 採用条件未達 · 順位差 -35.0 / -26.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00764878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764878.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -53.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.55,
          0.55
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
        "margin": 26.0,
        "reverse_margin": 21.0
      },
      "new": "00764320",
      "score": 53.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2857142857142857,
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
        "margin": 6.285713999999999,
        "reverse_margin": -21.0
      },
      "new": "00a1fd88",
      "score": 32.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45,
          0.45
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
        "reverse_margin": -26.0
      },
      "new": "00764828",
      "score": 27.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4b4e74db191a1a1caf83131957f5e9c7"></a>

### v16.0.0 [`0078ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed4c.md) FUN_0078ed4c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764878.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 54.285714
      },
      "new": "00764878",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fca6f1eb2c3a64b5c2212b709d8d8548"></a>

### v16.0.0 [`0078ed68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed68.md) FUN_0078ed68

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00764894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764894.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00764878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764878.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00764894",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00764878",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0fba46ae3d41c4fdb43170d3ce1d38a4"></a>

### v16.0.0 [`0079061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/0079061c.md) FUN_0079061c

`competing_candidates` 

呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 14件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`0065250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/0065250c.md) [`0078fc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fc34.md) [`007911e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/007911e4.md)

- 1. [`00766148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00766/00766148.md) · スコア 47.432432 · 採用条件未達 · 順位差 46.152632 / 45.81081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · スコア 1.621622 · 採用条件未達 · 順位差 -36.623577 / -45.81081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00885170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885170.md) · スコア 1.147054 · 採用条件未達 · 順位差 -47.731644 / -46.285378 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) · スコア 1.019144 · 採用条件未達 · 順位差 -0.09713499999999997 / -46.413288 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) · スコア 0.9497 · 採用条件未達 · 順位差 -1.5100699999999998 / -46.482732 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) · スコア 0.798235 · 採用条件未達 · 順位差 -0.05826399999999998 / -46.634197 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) · スコア 0.475549 · 採用条件未達 · 順位差 -2.012918 / -46.956883 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) · スコア 0.456541 · 採用条件未達 · 順位差 -33.427887 / -46.975891 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6516516516516516,
          0.6516516516516516
        ],
        "cfg_coverage": [
          0.4332129963898917,
          0.4166666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 46.152632,
        "reverse_margin": 45.81081
      },
      "new": "00766148",
      "score": 47.432432
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02735562310030395,
          0.02702702702702703
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
        "margin": -36.623577,
        "reverse_margin": -45.81081
      },
      "new": "00989a48",
      "score": 1.621622
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.014687882496940025,
          0.018018018018018018
        ],
        "cfg_coverage": [
          0.013289036544850499,
          0.013888888888888888
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -47.731644,
        "reverse_margin": -46.285378
      },
      "new": "00885170",
      "score": 1.147054
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b9af44b002405e9ec4a56f51ccb423d0"></a>

### v16.0.0 [`00792c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792c94.md) FUN_00792c94

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`007687c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/007687c0.md) · スコア 43.428571 · 採用条件未達 · 順位差 35.781512 / 41.428571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a34c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34c78.md) · スコア 2.0 · 採用条件未達 · 順位差 -68.0 / -41.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a901d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a901d8.md) · スコア 2.0 · 採用条件未達 · 順位差 0.0 / -41.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6571428571428571,
          0.6571428571428571
        ],
        "cfg_coverage": [
          0.1,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.781512,
        "reverse_margin": 41.428571
      },
      "new": "007687c0",
      "score": 43.428571
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
        "margin": -68.0,
        "reverse_margin": -41.428571
      },
      "new": "00a34c78",
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
        "reverse_margin": -41.428571
      },
      "new": "00a901d8",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6b1b1ad10ab5765fba1f60f2d76fc556"></a>

### v16.0.0 [`00792d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792d20.md) FUN_00792d20

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

- 1. [`0076884c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/0076884c.md) · スコア 49.116212 · 採用条件未達 · 順位差 46.366212 / 41.469153 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007687c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/007687c0.md) · スコア 7.647059 · 採用条件未達 · 順位差 -35.781512 / -41.469153 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0075cfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075c/0075cfa4.md) · スコア 2.0 · 採用条件未達 · 順位差 -31.578947 / -47.116212 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.4146341463414634,
          0.53125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 46.366212,
        "reverse_margin": 41.469153
      },
      "new": "0076884c",
      "score": 49.116212
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22857142857142856,
          0.09411764705882353
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
        "margin": -35.781512,
        "reverse_margin": -41.469153
      },
      "new": "007687c0",
      "score": 7.647059
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
        "margin": -31.578947,
        "reverse_margin": -47.116212
      },
      "new": "0075cfa4",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-45e2c14b14ba67de843df4dce674851a"></a>

### v16.0.0 [`0079370c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/0079370c.md) FUN_0079370c

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00928ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00928/00928ff0.md)

- 1. [`00769238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769238.md) · スコア 54.081633 · 採用条件未達 · 順位差 47.630019999999995 / 42.63950799999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007692fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/007692fc.md) · スコア 11.442125 · 採用条件未達 · 順位差 -37.294118 / -42.63950799999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0057243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/0057243c.md) · スコア 8.346939 · 採用条件未達 · 順位差 -1.7894249999999996 / -45.734694 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bdac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md) · スコア 5.714286 · 採用条件未達 · 順位差 0.0 / -48.367346999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a6ce68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ce68.md) · スコア 4.897959 · 採用条件未達 · 順位差 -2.521396 / -49.183673999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) · スコア 4.298137 · 採用条件未達 · 順位差 0.22440399999999983 / -49.783496 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a0b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b5fc.md) · スコア 4.210526 · 採用条件未達 · 順位差 -9.421053 / -49.871106999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a0bb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bb38.md) · スコア 4.210526 · 採用条件未達 · 順位差 -11.526316 / -49.871106999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7346938775510204,
          0.7346938775510204
        ],
        "cfg_coverage": [
          0.5,
          0.55
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 47.630019999999995,
        "reverse_margin": 42.63950799999999
      },
      "new": "00769238",
      "score": 54.081633
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16129032258064516,
          0.20408163265306123
        ],
        "cfg_coverage": [
          0.08823529411764706,
          0.15
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.294118,
        "reverse_margin": -42.63950799999999
      },
      "new": "007692fc",
      "score": 11.442125
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2727272727272727,
          0.12244897959183673
        ],
        "cfg_coverage": [
          0.07692307692307693,
          0.05
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
        "margin": -1.7894249999999996,
        "reverse_margin": -45.734694
      },
      "new": "0057243c",
      "score": 8.346939
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fbe787155c4f2aaa76440b005c8ad93a"></a>

### v16.0.0 [`007937d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007937d0.md) FUN_007937d0

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 5件 [`007938c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00928ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00928/00928ff0.md)

- 1. [`007692fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/007692fc.md) · スコア 48.736243 · 採用条件未達 · 順位差 37.294118 / 38.026566 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005f182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f182c.md) · スコア 10.709677 · 採用条件未達 · 順位差 -52.401434 / -38.026566 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00900188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/00900188.md) · スコア 8.709677 · 採用条件未達 · 順位差 -39.814913000000004 / -40.026566 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a6ce68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ce68.md) · スコア 7.419355 · 採用条件未達 · 順位差 2.521396 / -41.316888 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0057243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/0057243c.md) · スコア 6.451613 · 採用条件未達 · 順位差 -3.6847510000000003 / -42.28463 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00769238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769238.md) · スコア 6.451613 · 採用条件未達 · 順位差 -47.630019999999995 / -42.28463 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bdac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md) · スコア 5.714286 · 採用条件未達 · 順位差 0.0 / -43.021957 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005bb3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3f8.md) · スコア 4.83871 · 採用条件未達 · 順位差 4.83871 / -43.897533 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6612903225806451,
          0.6612903225806451
        ],
        "cfg_coverage": [
          0.35294117647058826,
          0.3870967741935484
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 37.294118,
        "reverse_margin": 38.026566
      },
      "new": "007692fc",
      "score": 48.736243
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
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
        "margin": -52.401434,
        "reverse_margin": -38.026566
      },
      "new": "005f182c",
      "score": 10.709677
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14754098360655737,
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
        "margin": -39.814913000000004,
        "reverse_margin": -40.026566
      },
      "new": "00900188",
      "score": 8.709677
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1e8b5ea350023ef133cf73032be5fc47"></a>

### v16.0.0 [`00794100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794100.md) FUN_00794100

`competing_candidates` 

呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md)

- 1. [`00769c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769c2c.md) · スコア 18.461538 · 採用条件未達 · 順位差 18.461538 / 18.461538 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.3076923076923077
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
        "margin": 18.461538,
        "reverse_margin": 18.461538
      },
      "new": "00769c2c",
      "score": 18.461538
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-47b0e3cb8c5b66e078bcce90511ef936"></a>

### v16.0.0 [`00794760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794760.md) FUN_00794760

`competing_candidates` 

呼出元 1件 [`009292fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/009292fc.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00928ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00928/00928ff0.md)

- 1. [`0076a28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a28c.md) · スコア 65.142857 · 採用条件未達 · 順位差 55.731092000000004 / 55.731092000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009a9454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9454.md) · スコア 9.411765 · 採用条件未達 · 順位差 -26.25 / -55.731092000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) · スコア 0.0 · 採用条件未達 · 順位差 -51.811414 / -65.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8857142857142857,
          0.8857142857142857
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
        "margin": 55.731092000000004,
        "reverse_margin": 55.731092000000004
      },
      "new": "0076a28c",
      "score": 65.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1568627450980392,
          0.22857142857142856
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
        "margin": -26.25,
        "reverse_margin": -55.731092000000004
      },
      "new": "009a9454",
      "score": 9.411765
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
        "margin": -51.811414,
        "reverse_margin": -65.142857
      },
      "new": "006f23b4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8ed9b2ec1f18833a0362b6ebe1b71cc5"></a>

### v16.0.0 [`0079484c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/0079484c.md) FUN_0079484c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076a378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a378.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0076a378",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bae889af7fc744cf93d8cfb17eebd3a7"></a>

### v16.0.0 [`00794868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794868.md) FUN_00794868

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076a394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a394.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0076a378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a378.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0076a394",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0076a378",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c95f85314ca83c560045a6b3976d1c21"></a>

### v16.0.0 [`007948d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948d4.md) FUN_007948d4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a400.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0076a400",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-126dc292e99fd9918ff746e9110e8a01"></a>

### v16.0.0 [`007948f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948f0.md) FUN_007948f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076a41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a41c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0076a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a400.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0076a41c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0076a400",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2c3f563741f977fea2461ed988c0b7a7"></a>

### v16.0.0 [`00795104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795104.md) FUN_00795104

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076ac30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ac30.md) · スコア 71.428571 · 採用条件未達 · 順位差 71.428571 / 71.428571 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors

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
          0.5714285714285714,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 71.428571,
        "reverse_margin": 71.428571
      },
      "new": "0076ac30",
      "score": 71.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-481a52a79d15444191968227e8480909"></a>

### v16.0.0 [`007951f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/007951f0.md) FUN_007951f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dfe0.md) · スコア 71.428571 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00594d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594d00.md) · スコア 71.428571 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`0076ad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ad1c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -71.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "0053dfe0",
      "score": 71.428571
    },
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00594d00",
      "score": 71.428571
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
        "reverse_margin": -71.428571
      },
      "new": "0076ad1c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-20a3cfdb201e5086fac5fa7a13c78c9d"></a>

### v16.0.0 [`0079520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079520c.md) FUN_0079520c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0076ad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ad38.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0076ad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076ad1c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0076ad38",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0076ad1c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e920ab9106f9334c0dae3b470c1f8eb7"></a>

### v16.0.0 [`00797ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797ff4.md) FUN_00797ff4

`competing_candidates` 

呼出元 2件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 0件 

- 1. [`0076db20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db20.md) · スコア 80.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0076db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db38.md) · スコア 20.0 · 採用条件未達 · 順位差 -60.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "0076db20",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
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
        "margin": -60.0,
        "reverse_margin": -60.0
      },
      "new": "0076db38",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-90caeb65bd58fb998f8f788fcc4ca7d6"></a>

### v16.0.0 [`0079800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/0079800c.md) FUN_0079800c

`competing_candidates` 

呼出元 2件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 0件 

- 1. [`0076db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db38.md) · スコア 80.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0076db20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076db20.md) · スコア 20.0 · 採用条件未達 · 順位差 -60.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "0076db38",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.4
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
        "reverse_margin": -60.0
      },
      "new": "0076db20",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-137692d21dd6b81697dc60b8266ecbd4"></a>

### v16.0.0 [`0079c97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c97c.md) FUN_0079c97c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005565c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/005565c8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`007724a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007724a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00772590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772590.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 4. [`00772678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772678.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 5. [`00ad7474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7474.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 6. [`00ada56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada56c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 7. [`00848ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848ab0.md) · スコア 65.113636 · 採用条件未達 · 順位差 -4.318182000000007 / -14.886364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00970554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970554.md) · スコア 49.454545 · 採用条件未達 · 順位差 0.0 / -30.545454999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005565c8",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007724a8",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00772590",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`0079ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079ca64.md) FUN_0079ca64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005565c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/005565c8.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007724a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007724a8.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00772590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772590.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00772678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772678.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ad7474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7474.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00ada56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada56c.md) · スコア 70.649351 · 採用条件未達 · 順位差 -9.350649000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00848ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848ab0.md) · スコア 63.295455 · 採用条件未達 · 順位差 -6.13636300000001 / -7.353895999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0097063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/0097063c.md) · スコア 52.636364 · 採用条件未達 · 順位差 -10.909090999999997 / -18.012986999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.7692307692307693,
          0.7142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.350649000000004,
        "reverse_margin": 0.0
      },
      "new": "005565c8",
      "score": 70.649351
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.7692307692307693,
          0.7142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.350649000000004,
        "reverse_margin": 0.0
      },
      "new": "007724a8",
      "score": 70.649351
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.7692307692307693,
          0.7142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.350649000000004,
        "reverse_margin": 0.0
      },
      "new": "00772590",
      "score": 70.649351
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f698a1e7f96a4267e81a46a6305ac9b6"></a>

### v16.0.0 [`0079cb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cb4c.md) FUN_0079cb4c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005565c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/005565c8.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007724a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007724a8.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00772590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772590.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00772678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772678.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ad7474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7474.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00ada56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada56c.md) · スコア 69.220779 · 採用条件未達 · 順位差 -10.779221000000007 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00848ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848ab0.md) · スコア 55.909091 · 採用条件未達 · 順位差 -13.52272700000001 / -13.311687999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00970554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00970/00970554.md) · スコア 47.636364 · 採用条件未達 · 順位差 -1.8181810000000027 / -21.584414999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.6923076923076923,
          0.6428571428571429
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.779221000000007,
        "reverse_margin": 0.0
      },
      "new": "005565c8",
      "score": 69.220779
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.6923076923076923,
          0.6428571428571429
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.779221000000007,
        "reverse_margin": 0.0
      },
      "new": "007724a8",
      "score": 69.220779
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9393939393939394,
          0.9393939393939394
        ],
        "cfg_coverage": [
          0.6923076923076923,
          0.6428571428571429
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.779221000000007,
        "reverse_margin": 0.0
      },
      "new": "00772590",
      "score": 69.220779
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-739ee1d1c8bbf450b0d61af6e00bc10d"></a>

### v16.0.0 [`0079d408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d408.md) FUN_0079d408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00772f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772f34.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 54.285714
      },
      "new": "00772f34",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f055d90f89efacd490f04a35872e2aa0"></a>

### v16.0.0 [`0079d424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d424.md) FUN_0079d424

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00772f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772f50.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00772f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772f34.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00772f50",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00772f34",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3ec4a3060dbe7cce6e9a5e72bb506abd"></a>

### v16.0.0 [`0079d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d830.md) FUN_0079d830

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0077335c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077335c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0077335c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-69dc4fe26182cea53a43207d4a1d70ff"></a>

### v16.0.0 [`0079d84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d84c.md) FUN_0079d84c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773378.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0077335c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077335c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00773378",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0077335c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a153e2cf9eb6896144db5367acb93d5c"></a>

### v16.0.0 [`0079d924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d924.md) FUN_0079d924

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773450.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 54.285714
      },
      "new": "00773450",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ebccad14140e13ec31762521dc2f9ab8"></a>

### v16.0.0 [`0079d940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d940.md) FUN_0079d940

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0077346c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077346c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00773450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773450.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00773478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773478.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0077346c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773450",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773478",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e20365e5c477b28dcfc26372f2eda323"></a>

### v16.0.0 [`0079d94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d94c.md) FUN_0079d94c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773478.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`0077346c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077346c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00773450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773450.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "00773478",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0077346c",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773450",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4ac62a2e0e4a4eb888daa4b347b96c3d"></a>

### v16.0.0 [`0079da54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da54.md) FUN_0079da54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00592228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592228.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00773580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773580.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00592228",
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
        "margin": 54.285714,
        "reverse_margin": -25.714286
      },
      "new": "00773580",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bf28ed44a529b11e32e01bccfa9596a2"></a>

### v16.0.0 [`0079da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da70.md) FUN_0079da70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0077359c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077359c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00773580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773580.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`007735a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735a8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0077359c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773580",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007735a8",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a54a73a07859aa4cae3c23490f961ad6"></a>

### v16.0.0 [`0079da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da7c.md) FUN_0079da7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007735a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007735a8.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`0077359c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/0077359c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00773580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773580.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "007735a8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0077359c",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773580",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-25ec43e6489b20d63f57efbe3f37ffd8"></a>

### v16.0.0 [`0079dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dadc.md) FUN_0079dadc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773608.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00773608",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a8280b777e88e0ef087b03b515a07a93"></a>

### v16.0.0 [`0079daf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079daf8.md) FUN_0079daf8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773624.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00773608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773608.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00773624",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773608",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b2ad5c853556591f653e67ce0da7a8bf"></a>

### v16.0.0 [`0079dbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dbd0.md) FUN_0079dbd0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00860484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860484.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`007736fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007736fc.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 80.0
      },
      "new": "00860484",
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
      "new": "007736fc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e6b42e2579e7e8236f4fad91717a4480"></a>

### v16.0.0 [`0079dbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dbec.md) FUN_0079dbec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773718.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`007736fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007736fc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00773724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773724.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00773718",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007736fc",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773724",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6219c91991af08a0d37200e5882bc002"></a>

### v16.0.0 [`0079dbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dbf8.md) FUN_0079dbf8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773724.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`00773718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773718.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`007736fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007736fc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.6667,
        "reverse_margin": 67.6667
      },
      "new": "00773724",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773718",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "007736fc",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b89cf3b6baa269fa223c37088cf35df3"></a>

### v16.0.0 [`0079dc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc58.md) FUN_0079dc58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773784.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00773784",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-142a303726dd58ebb49f52c9e6b3d344"></a>

### v16.0.0 [`0079dc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc74.md) FUN_0079dc74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007737a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007737a0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00773784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773784.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "007737a0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00773784",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7a766c70a6db1a1bc56e6709d76a8916"></a>

### v16.0.0 [`0079dd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dd4c.md) FUN_0079dd4c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00773878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/00773878.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 54.285714
      },
      "new": "00773878",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

