# v15.7.4 → v16.0.0 · 追加調査 (175)

[一覧の目次](README.md)

<a id="review-322195450ca5febb02eeb22d9c3ce153"></a>

### v16.0.0 [`00bc16b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc16b0.md) _INIT_288

`competing_candidates` 

呼出元 0件  · 呼出先 4件 [`00b650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b650e8.md) [`00bc0f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f1c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)

- 1. [`00b52d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52d3c.md) · スコア 70.666667 · 採用条件未達 · 順位差 28.666667000000004 / 59.777778000000005 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b5a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a734.md) · スコア 10.888889 · 採用条件未達 · 順位差 -33.93464 / -59.777778000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · スコア 2.0 · 採用条件未達 · 順位差 -34.0 / -68.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 28.666667000000004,
        "reverse_margin": 59.777778000000005
      },
      "new": "00b52d3c",
      "score": 70.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23529411764705882,
          0.14814814814814814
        ],
        "cfg_coverage": [
          0.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.93464,
        "reverse_margin": -59.777778000000005
      },
      "new": "00b5a734",
      "score": 10.888889
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
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.0,
        "reverse_margin": -68.666667
      },
      "new": "00b4aa9c",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f734eb72422a9c15bfd07157dd7851d"></a>

### v16.0.0 [`00bc2974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2974.md) _ZN8firebase13remote_config8internal22custom_signals_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

- 1. [`00aeb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md) · スコア 27.857143 · 採用条件未達 · 順位差 27.857143 / 27.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4642857142857143,
          0.4642857142857143
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
        "margin": 27.857143,
        "reverse_margin": 27.857143
      },
      "new": "00aeb660",
      "score": 27.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7b720b0f971c25b617247552992ca3d9"></a>

### v16.0.0 [`00bc29e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc29e4.md) _ZN8firebase13remote_config8internal22custom_signals_builder11GetMethodIdENS2_6MethodE

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

- 1. [`00aeb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md) · スコア 66.0 · 採用条件未達 · 順位差 66.0 / 66.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7333333333333333,
          0.7333333333333333
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 66.0,
        "reverse_margin": 66.0
      },
      "new": "00aeb6d0",
      "score": 66.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-364150d144d7e915bd26b21a362e76f8"></a>

### v16.0.0 [`00bc7314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16SetCustomSignalsERKNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9

`competing_candidates` 

呼出元 1件 [`00c5d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d330.md) · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

- 1. [`00b58108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md) · スコア 5.511811 · 採用条件未達 · 順位差 1.7022869999999997 / 0.5564299999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00af9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md) · スコア 4.955381 · 採用条件未達 · 順位差 0.4826629999999996 / -0.5564299999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00af1d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1d98.md) · スコア 4.134983 · 採用条件未達 · 順位差 4.134983 / -1.3768279999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b29c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b29c54.md) · スコア 4.134983 · 採用条件未達 · 順位差 -5.849144000000001 / -1.3768279999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md) · スコア 3.058118 · 採用条件未達 · 順位差 3.058118 / -2.453693 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b57b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md) · スコア 2.519685 · 採用条件未達 · 順位差 1.6834479999999998 / -2.992126 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b56b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md) · スコア 2.395201 · 採用条件未達 · 順位差 2.395201 / -3.1166099999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) · スコア 2.084095 · 採用条件未達 · 順位差 2.084095 / -3.4277159999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18518518518518517,
          0.09186351706036745
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
        "margin": 1.7022869999999997,
        "reverse_margin": 0.5564299999999998
      },
      "new": "00b58108",
      "score": 5.511811
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1513157894736842,
          0.06036745406824147
        ],
        "cfg_coverage": [
          0.1044776119402985,
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
        "margin": 0.4826629999999996,
        "reverse_margin": -0.5564299999999998
      },
      "new": "00af9f2c",
      "score": 4.955381
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18811881188118812,
          0.049868766404199474
        ],
        "cfg_coverage": [
          0.1875,
          0.05714285714285714
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 4.134983,
        "reverse_margin": -1.3768279999999997
      },
      "new": "00af1d98",
      "score": 4.134983
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-862923b1785fbd2a31f13ea3d85fadc4"></a>

### v16.0.0 [`00bc79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc79cc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal26SetCustomSignalsLastResultEv

`competing_candidates` 

呼出元 1件 [`00c5d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3b0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

- 1. [`00b56abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md) · スコア 61.538462 · 採用条件未達 · 順位差 55.384616 / 0.0 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00b58078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md) · スコア 61.538462 · 採用条件未達 · 順位差 61.538462 / 0.0 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b584cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md) · スコア 61.538462 · 採用条件未達 · 順位差 50.109891000000005 / 0.0 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b56790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md) · スコア 27.692308 · 採用条件未達 · 順位差 27.692308 / -33.846154 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b56de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56de8.md) · スコア 27.692308 · 採用条件未達 · 順位差 27.692308 / -33.846154 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b57110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -61.538462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 55.384616,
        "reverse_margin": 0.0
      },
      "new": "00b56abc",
      "score": 61.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6923076923076923,
          0.6923076923076923
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
        "margin": 61.538462,
        "reverse_margin": 0.0
      },
      "new": "00b58078",
      "score": 61.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6923076923076923,
          0.6923076923076923
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
        "margin": 50.109891000000005,
        "reverse_margin": 0.0
      },
      "new": "00b584cc",
      "score": 61.538462
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-07ad79907fb15ef6ade9af6ee2675090"></a>

### v16.0.0 [`00bc9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c0c.md) FUN_00bc9c0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b5a70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a70c.md) · スコア 54.285714 · 採用条件未達 · 順位差 30.756301999999998 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b5a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a734.md) · スコア 0.0 · 採用条件未達 · 順位差 -44.823529 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 30.756301999999998,
        "reverse_margin": 54.285714
      },
      "new": "00b5a70c",
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
        "margin": -44.823529,
        "reverse_margin": -54.285714
      },
      "new": "00b5a734",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-acd95f94011cf017627f99a4537e1ccc"></a>

### v16.0.0 [`00bc9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c28.md) FUN_00bc9c28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b5a728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a728.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00b5a70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a70c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00b5a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a734.md) · スコア 0.7059 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b5a728",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b5a70c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b5a734",
      "score": 0.7059
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e9c052847cae76edf03dc6f8e7667fe3"></a>

### v16.0.0 [`00bc9c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c34.md) _INIT_289

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00bc37ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37ec.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)

- 1. [`00b5a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a734.md) · スコア 44.823529 · 採用条件未達 · 順位差 27.823529 / 2.8235290000000006 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b52d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52d3c.md) · スコア 42.0 · 採用条件未達 · 順位差 -28.666667000000004 / -2.8235290000000006 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b5a70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a70c.md) · スコア 23.529412 · 採用条件未達 · 順位差 -30.756301999999998 / -21.294117 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · スコア 17.0 · 採用条件未達 · 順位差 -19.0 / -27.823529 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.0,
          1.0
        ],
        "mapped_data": 5,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 27.823529,
        "reverse_margin": 2.8235290000000006
      },
      "new": "00b5a734",
      "score": 44.823529
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.5294117647058824
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -28.666667000000004,
        "reverse_margin": -2.8235290000000006
      },
      "new": "00b52d3c",
      "score": 42.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.058823529411764705
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
        "margin": -30.756301999999998,
        "reverse_margin": -21.294117
      },
      "new": "00b5a70c",
      "score": 23.529412
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9d8131266d0088a700d78bbccbe1903f"></a>

### v16.0.0 [`00bca0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0a8.md) FUN_00bca0a8

`competing_candidates` [`00b5aba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aba8.md)

呼出元 1件 [`00bcbce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00bca078",
    "00bca0b4",
    "00b5ab78",
    "00b5abb4"
  ],
  "initial_reason": ""
}
~~~

<a id="review-690e05f53ffaebed2fd0af439dfa68ff"></a>

### v16.0.0 [`00bca0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b0.md) FUN_00bca0b0

`competing_candidates` 

呼出元 1件 [`00bcbce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md) · 呼出先 0件 

- 1. [`00b5abb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abb0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 69.0,
        "reverse_margin": 69.0
      },
      "new": "00b5abb0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b1e3aae3edb08febd66fd0d33edd75f0"></a>

### v16.0.0 [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) FUN_00be1e40

`competing_candidates` 

呼出元 2件 [`00be1e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e24.md) [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · 呼出先 4件 [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md) [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.982379 · 採用条件未達 · 順位差 -0.03555799999999998 / 0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.85022 · 採用条件未達 · 順位差 -0.033187999999999995 / -0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.718062 · 採用条件未達 · 順位差 -0.030817000000000094 / -0.2643169999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.03303964757709251
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
        "margin": -0.03555799999999998,
        "reverse_margin": 0.13215899999999992
      },
      "new": "00bb5ffc",
      "score": 1.982379
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.030837004405286344
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
        "margin": -0.033187999999999995,
        "reverse_margin": -0.13215899999999992
      },
      "new": "00ba4ab8",
      "score": 1.85022
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.028634361233480177
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
        "margin": -0.030817000000000094,
        "reverse_margin": -0.2643169999999999
      },
      "new": "00bb70c4",
      "score": 1.718062
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9819bafb74231cc39e023c5e6459343e"></a>

### v16.0.0 [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) FUN_00be2578

`competing_candidates` 

呼出元 2件 [`00be2558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2558.md) [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · 呼出先 4件 [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) [`00be96a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be96a4.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.383176 · 採用条件未達 · 順位差 -3.902538 / -0.6347609999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0b2a0dba9247235b0ab3674f0cdb39e3"></a>

### v16.0.0 [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) FUN_00be2c8c

`competing_candidates` 

呼出元 2件 [`00be2c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c70.md) [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) · 呼出先 4件 [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) [`00be9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9c60.md) [`00be9d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9d88.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.982379 · 採用条件未達 · 順位差 -0.03555799999999998 / 0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.85022 · 採用条件未達 · 順位差 -0.033187999999999995 / -0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.718062 · 採用条件未達 · 順位差 -0.030817000000000094 / -0.2643169999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.03303964757709251
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
        "margin": -0.03555799999999998,
        "reverse_margin": 0.13215899999999992
      },
      "new": "00bb5ffc",
      "score": 1.982379
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.030837004405286344
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
        "margin": -0.033187999999999995,
        "reverse_margin": -0.13215899999999992
      },
      "new": "00ba4ab8",
      "score": 1.85022
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.028634361233480177
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
        "margin": -0.030817000000000094,
        "reverse_margin": -0.2643169999999999
      },
      "new": "00bb70c4",
      "score": 1.718062
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b93d21d6697e52fb26368699f3d33e4d"></a>

### v16.0.0 [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) FUN_00be33c0

`competing_candidates` 

呼出元 2件 [`00be33a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33a4.md) [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · 呼出先 4件 [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) [`00bea464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea464.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.982379 · 採用条件未達 · 順位差 -0.03555799999999998 / 0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.85022 · 採用条件未達 · 順位差 -0.033187999999999995 / -0.13215899999999992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.718062 · 採用条件未達 · 順位差 -0.030817000000000094 / -0.2643169999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.03303964757709251
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
        "margin": -0.03555799999999998,
        "reverse_margin": 0.13215899999999992
      },
      "new": "00bb5ffc",
      "score": 1.982379
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.030837004405286344
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
        "margin": -0.033187999999999995,
        "reverse_margin": -0.13215899999999992
      },
      "new": "00ba4ab8",
      "score": 1.85022
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.028634361233480177
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
        "margin": -0.030817000000000094,
        "reverse_margin": -0.2643169999999999
      },
      "new": "00bb70c4",
      "score": 1.718062
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b1e455cd99f504c8808ea22991110bb6"></a>

### v16.0.0 [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) FUN_00be3af8

`competing_candidates` 

呼出元 2件 [`00be3ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3ad8.md) [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) · 呼出先 4件 [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) [`00beaa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beaa18.md) [`00beab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beab40.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.978022 · 採用条件未達 · 順位差 -0.03991499999999992 / 0.13186799999999987 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.846154 · 採用条件未達 · 順位差 -0.0372539999999999 / -0.13186799999999987 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.714286 · 採用条件未達 · 順位差 -0.034593000000000096 / -0.26373599999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.03296703296703297
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
        "margin": -0.03991499999999992,
        "reverse_margin": 0.13186799999999987
      },
      "new": "00bb5ffc",
      "score": 1.978022
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03076923076923077
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
        "margin": -0.0372539999999999,
        "reverse_margin": -0.13186799999999987
      },
      "new": "00ba4ab8",
      "score": 1.846154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02857142857142857
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
        "margin": -0.034593000000000096,
        "reverse_margin": -0.26373599999999997
      },
      "new": "00bb70c4",
      "score": 1.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-617240ce0eb80362d2a7bf71f6f32421"></a>

### v16.0.0 [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) FUN_00be4234

`competing_candidates` 

呼出元 2件 [`00be4214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4214.md) [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · 呼出先 4件 [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) [`00beb224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb224.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.978022 · 採用条件未達 · 順位差 -0.03991499999999992 / 0.13186799999999987 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.846154 · 採用条件未達 · 順位差 -0.0372539999999999 / -0.13186799999999987 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.714286 · 採用条件未達 · 順位差 -0.034593000000000096 / -0.26373599999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.03296703296703297
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
        "margin": -0.03991499999999992,
        "reverse_margin": 0.13186799999999987
      },
      "new": "00bb5ffc",
      "score": 1.978022
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03076923076923077
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
        "margin": -0.0372539999999999,
        "reverse_margin": -0.13186799999999987
      },
      "new": "00ba4ab8",
      "score": 1.846154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02857142857142857
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
        "margin": -0.034593000000000096,
        "reverse_margin": -0.26373599999999997
      },
      "new": "00bb70c4",
      "score": 1.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f30712b91a2397b1744cfd29b6f668a7"></a>

### v16.0.0 [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) FUN_00be4970

`competing_candidates` 

呼出元 2件 [`00be4950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4950.md) [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · 呼出先 4件 [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) [`00beb7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) [`00beb8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb8e8.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.383176 · 採用条件未達 · 順位差 -3.902538 / -0.6347609999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1d35447ccb5526080cb3e25912e96ca8"></a>

### v16.0.0 [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) FUN_00be5088

`competing_candidates` 

呼出元 2件 [`00be5068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5068.md) [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · 呼出先 4件 [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) [`00bebfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebfac.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.37883 · 採用条件未達 · 順位差 -3.906884 / -0.6391069999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d4a6b2112b002684302408943b9302ff"></a>

### v16.0.0 [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) FUN_00be57a0

`competing_candidates` 

呼出元 2件 [`00be5780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5780.md) [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · 呼出先 4件 [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.380975 · 採用条件未達 · 順位差 -3.9047389999999993 / 0.30474200000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 1.076233 · 採用条件未達 · 順位差 -0.9417039999999999 / -0.30474200000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 0.941704 · 採用条件未達 · 順位差 -0.941704 / -0.4392710000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 0.941704 · 採用条件未達 · 順位差 -0.8071750000000001 / -0.4392710000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06,
          0.020179372197309416
        ],
        "cfg_coverage": [
          0.0425531914893617,
          0.00851063829787234
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.9047389999999993,
        "reverse_margin": 0.30474200000000007
      },
      "new": "0059e044",
      "score": 1.380975
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02416918429003021,
          0.017937219730941704
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
        "margin": -0.9417039999999999,
        "reverse_margin": -0.30474200000000007
      },
      "new": "00bb5ffc",
      "score": 1.076233
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.021021021021021023,
          0.01569506726457399
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
        "margin": -0.941704,
        "reverse_margin": -0.4392710000000001
      },
      "new": "00ba4ab8",
      "score": 0.941704
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5111002d98a254b28d4e5ca4f8760c08"></a>

### v16.0.0 [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) FUN_00be5eb8

`competing_candidates` 

呼出元 2件 [`00be5e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5e98.md) [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · 呼出先 4件 [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.383176 · 採用条件未達 · 順位差 -3.902538 / -0.6347609999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a5d67cc1b963c202c028b6aa5ca9c42e"></a>

### v16.0.0 [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) FUN_00be65d0

`competing_candidates` 

呼出元 2件 [`00be65b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65b0.md) [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · 呼出先 4件 [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.383176 · 採用条件未達 · 順位差 -3.902538 / -0.6347609999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0c111ee86cc439b45c7d5856cc771a0"></a>

### v16.0.0 [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) FUN_00be6ce8

`competing_candidates` 

呼出元 2件 [`00be6cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6cc8.md) [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · 呼出先 4件 [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.383176 · 採用条件未達 · 順位差 -3.902538 / -0.6347609999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f886431f17f9aaae20fe111eb129397"></a>

### v16.0.0 [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) FUN_00be7400

`competing_candidates` 

呼出元 2件 [`00be73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be73e0.md) [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · 呼出先 4件 [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) [`00bee058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee058.md) [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.381703 · 採用条件未達 · 順位差 -3.9040109999999997 / -0.636234 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7d1bf629ee3d9c8e7eac14531101947"></a>

### v16.0.0 [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) FUN_00be7b18

`competing_candidates` 

呼出元 2件 [`00be7af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7af8.md) [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · 呼出先 4件 [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) [`00bee6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee6f8.md) [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md)

- 1. [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · スコア 2.017937 · 採用条件未達 · 順位差 0.0 / 0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · スコア 1.883408 · 採用条件未達 · 順位差 0.0 / -0.1345289999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · スコア 1.748879 · 採用条件未達 · 順位差 0.0 / -0.2690579999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 1.380975 · 採用条件未達 · 順位差 -3.9047389999999993 / -0.6369619999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.045317220543806644,
          0.033632286995515695
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
        "margin": 0.0,
        "reverse_margin": 0.1345289999999999
      },
      "new": "00bb5ffc",
      "score": 2.017937
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.042042042042042045,
          0.03139013452914798
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
        "margin": 0.0,
        "reverse_margin": -0.1345289999999999
      },
      "new": "00ba4ab8",
      "score": 1.883408
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038461538461538464,
          0.02914798206278027
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
        "margin": 0.0,
        "reverse_margin": -0.2690579999999998
      },
      "new": "00bb70c4",
      "score": 1.748879
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c7938ea41ad46ec251ed36c17a717eb2"></a>

### v16.0.0 [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) FUN_00be8c00

`competing_candidates` 

呼出元 1件 [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · 呼出先 1件 [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md)

- 1. [`00996198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / 0.9898989999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md) · スコア 3.568182 · 採用条件未達 · 順位差 0.0 / -0.9898989999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0658682634730539,
          0.0625
        ],
        "cfg_coverage": [
          0.04040404040404041,
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
        "margin": 0.0,
        "reverse_margin": 0.9898989999999994
      },
      "new": "00996198",
      "score": 4.558081
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05555555555555555,
          0.05113636363636364
        ],
        "cfg_coverage": [
          0.029850746268656716,
          0.025
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -0.9898989999999994
      },
      "new": "0051f2b4",
      "score": 3.568182
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-485d65df5ea83a9cbec772f41c5421fc"></a>

### v16.0.0 [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) FUN_00be92dc

`competing_candidates` 

呼出元 1件 [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · 呼出先 1件 [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 5.261324 · 採用条件未達 · 順位差 -0.024389999999999468 / 5.261324 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08,
          0.07142857142857142
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.04878048780487805
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.024389999999999468,
        "reverse_margin": 5.261324
      },
      "new": "0059e044",
      "score": 5.261324
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a16e9564e674fdd46735ec70ab64cba3"></a>

### v16.0.0 [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) FUN_00be99a0

`competing_candidates` 

呼出元 1件 [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) · 呼出先 1件 [`00be9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9c60.md)

- 1. [`00996198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / 1.0137089999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md) · スコア 3.544372 · 採用条件未達 · 順位差 -0.02381000000000011 / -1.0137089999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0658682634730539,
          0.0625
        ],
        "cfg_coverage": [
          0.04040404040404041,
          0.047619047619047616
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 1.0137089999999995
      },
      "new": "00996198",
      "score": 4.558081
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05555555555555555,
          0.05113636363636364
        ],
        "cfg_coverage": [
          0.029850746268656716,
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
        "margin": -0.02381000000000011,
        "reverse_margin": -1.0137089999999995
      },
      "new": "0051f2b4",
      "score": 3.544372
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3818a11e7bd516d121846db3e2dc4977"></a>

### v16.0.0 [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) FUN_00bea07c

`competing_candidates` 

呼出元 1件 [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · 呼出先 1件 [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md)

- 1. [`00996198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / 0.9898989999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md) · スコア 3.568182 · 採用条件未達 · 順位差 0.0 / -0.9898989999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0658682634730539,
          0.0625
        ],
        "cfg_coverage": [
          0.04040404040404041,
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
        "margin": 0.0,
        "reverse_margin": 0.9898989999999994
      },
      "new": "00996198",
      "score": 4.558081
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05555555555555555,
          0.05113636363636364
        ],
        "cfg_coverage": [
          0.029850746268656716,
          0.025
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -0.9898989999999994
      },
      "new": "0051f2b4",
      "score": 3.568182
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bdac7a0ae8a9b56854ca55a3c001889a"></a>

### v16.0.0 [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) FUN_00bea758

`competing_candidates` 

呼出元 1件 [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) · 呼出先 1件 [`00beaa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beaa18.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.75 · 採用条件未達 · 順位差 -0.5357139999999996 / 4.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.0625
        ],
        "cfg_coverage": [
          0.0851063829787234,
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
        "margin": -0.5357139999999996,
        "reverse_margin": 4.75
      },
      "new": "0059e044",
      "score": 4.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2ffb8ce2bb43dbed24c2f00f8b605dca"></a>

### v16.0.0 [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) FUN_00beae3c

`competing_candidates` 

呼出元 1件 [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · 呼出先 1件 [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.75 · 採用条件未達 · 順位差 -0.5357139999999996 / 4.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.0625
        ],
        "cfg_coverage": [
          0.0851063829787234,
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
        "margin": -0.5357139999999996,
        "reverse_margin": 4.75
      },
      "new": "0059e044",
      "score": 4.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e359e372c32228336d169dc236270f48"></a>

### v16.0.0 [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) FUN_00beb520

`competing_candidates` 

呼出元 1件 [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · 呼出先 1件 [`00beb7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 5.205255 · 採用条件未達 · 順位差 -0.08045899999999939 / 5.205255 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08,
          0.07142857142857142
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.04597701149425287
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.08045899999999939,
        "reverse_margin": 5.205255
      },
      "new": "0059e044",
      "score": 5.205255
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3cb88470aecc8e097bb9a27f8e5532b2"></a>

### v16.0.0 [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) FUN_00bebbe4

`competing_candidates` 

呼出元 1件 [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · 呼出先 1件 [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 5.285714 · 採用条件未達 · 順位差 0.024389999999999468 / 5.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08,
          0.07142857142857142
        ],
        "cfg_coverage": [
          0.0851063829787234,
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
        "margin": 0.024389999999999468,
        "reverse_margin": 5.285714
      },
      "new": "0059e044",
      "score": 5.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-81d9c404e8e2cd231fbc5c3f1d0e4a2b"></a>

### v16.0.0 [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) FUN_00bec2a8

`competing_candidates` 

呼出元 1件 [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · 呼出先 1件 [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.928571 · 採用条件未達 · 順位差 -0.35714299999999977 / 4.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
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
        "margin": -0.35714299999999977,
        "reverse_margin": 4.928571
      },
      "new": "0059e044",
      "score": 4.928571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-542028b7d8fc0fe8b3a29bebb429f428"></a>

### v16.0.0 [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) FUN_00bec96c

`competing_candidates` 

呼出元 1件 [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · 呼出先 1件 [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.928571 · 採用条件未達 · 順位差 -0.35714299999999977 / 4.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
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
        "margin": -0.35714299999999977,
        "reverse_margin": 4.928571
      },
      "new": "0059e044",
      "score": 4.928571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6009079355e889d1e564d17cabcd15eb"></a>

### v16.0.0 [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) FUN_00bed030

`competing_candidates` 

呼出元 1件 [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · 呼出先 1件 [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.916226 · 採用条件未達 · 順位差 -0.3694879999999996 / 4.916226 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.04938271604938271
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.3694879999999996,
        "reverse_margin": 4.916226
      },
      "new": "0059e044",
      "score": 4.916226
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d6f38ce53a3b670cd1c3a6bde5e22841"></a>

### v16.0.0 [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) FUN_00bed6f4

`competing_candidates` 

呼出元 1件 [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · 呼出先 1件 [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.869748 · 採用条件未達 · 順位差 -0.41596599999999917 / 4.869748 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.047058823529411764
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.41596599999999917,
        "reverse_margin": 4.869748
      },
      "new": "0059e044",
      "score": 4.869748
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2a5c84bb92f03675ccce97000e33c3fe"></a>

### v16.0.0 [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) FUN_00beddb8

`competing_candidates` 

呼出元 1件 [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · 呼出先 1件 [`00bee058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee058.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.916226 · 採用条件未達 · 順位差 -0.3694879999999996 / 4.916226 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.04938271604938271
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.3694879999999996,
        "reverse_margin": 4.916226
      },
      "new": "0059e044",
      "score": 4.916226
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cc6b97274c09bce6324c36967046f77f"></a>

### v16.0.0 [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) FUN_00bee458

`competing_candidates` 

呼出元 1件 [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · 呼出先 1件 [`00bee6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee6f8.md)

- 1. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 4.892427 · 採用条件未達 · 順位差 -0.39328699999999994 / 4.892427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07333333333333333,
          0.06547619047619048
        ],
        "cfg_coverage": [
          0.0851063829787234,
          0.04819277108433735
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -0.39328699999999994,
        "reverse_margin": 4.892427
      },
      "new": "0059e044",
      "score": 4.892427
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-10f693d08acc36e4c28a95f09b14ba1c"></a>

### v16.0.0 [`00beeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md) FUN_00beeaf8

`competing_candidates` 

呼出元 1件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) · 呼出先 2件 [`00beef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md) [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)

- 1. [`00b96608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md) · スコア 3.193916 · 採用条件未達 · 順位差 3.193916 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00b9681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md) · スコア 3.193916 · 採用条件未達 · 順位差 3.193916 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b98350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md) · スコア 3.193916 · 採用条件未達 · 順位差 3.193916 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b98564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md) · スコア 3.193916 · 採用条件未達 · 順位差 3.193916 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · スコア 2.727389 · 採用条件未達 · 順位差 -2.5583249999999995 / -0.46652700000000014 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1728395061728395,
          0.053231939163498096
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
        "margin": 3.193916,
        "reverse_margin": 0.0
      },
      "new": "00b96608",
      "score": 3.193916
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17721518987341772,
          0.053231939163498096
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
        "margin": 3.193916,
        "reverse_margin": 0.0
      },
      "new": "00b9681c",
      "score": 3.193916
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1728395061728395,
          0.053231939163498096
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
        "margin": 3.193916,
        "reverse_margin": 0.0
      },
      "new": "00b98350",
      "score": 3.193916
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c7b3045cbcac4f979c826f54adabe1a1"></a>

### v16.0.0 [`00bef16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md) FUN_00bef16c

`competing_candidates` 

呼出元 1件 [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) · 呼出先 1件 [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md)

- 1. [`006928c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928c4.md) · スコア 3.75 · 採用条件未達 · 順位差 -2.958075 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`007e5214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5214.md) · スコア 3.75 · 採用条件未達 · 順位差 -2.6500000000000004 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · スコア 3.75 · 採用条件未達 · 順位差 -1.8499999999999996 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0070ec20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070e/0070ec20.md) · スコア 3.25 · 採用条件未達 · 順位差 -2.75 / -0.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0063f0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f0f4.md) · スコア 3.0 · 採用条件未達 · 順位差 -1.9556649999999998 / -0.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b56820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md) · スコア 2.25 · 採用条件未達 · 順位差 -1.35 / -1.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00978d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md) · スコア 2.0 · 採用条件未達 · 順位差 -9.583333 / -1.75 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "no_candidate_with_available_features",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09316770186335403,
          0.0625
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
        "margin": -2.958075,
        "reverse_margin": 0.0
      },
      "new": "006928c4",
      "score": 3.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11363636363636363,
          0.0625
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
        "margin": -2.6500000000000004,
        "reverse_margin": 0.0
      },
      "new": "007e5214",
      "score": 3.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.0625
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
        "margin": -1.8499999999999996,
        "reverse_margin": 0.0
      },
      "new": "00bdaab4",
      "score": 3.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8842186b4df72ccdfbed9472185e6413"></a>

### v16.0.0 [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md) FUN_00beff20

`competing_candidates` 

呼出元 1件 [`00bef800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md) · 呼出先 4件 [`00beff74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff74.md) [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

- 1. [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) · スコア 59.5 · 採用条件未達 · 順位差 2.0 / 2.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -2.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) · スコア 57.5 · 採用条件未達 · 順位差 -10.0 / -2.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md) · スコア 53.75 · 採用条件未達 · 順位差 -4.25 / -5.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) · スコア 53.75 · 採用条件未達 · 順位差 -12.25 / -5.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) · スコア 53.75 · 採用条件未達 · 順位差 -2.25 / -5.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) · スコア 38.75 · 採用条件未達 · 順位差 -1.25 / -20.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0050d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d5a0.md) · スコア 37.142857 · 採用条件未達 · 順位差 -14.285713999999999 / -22.357143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.0,
        "reverse_margin": 2.0
      },
      "new": "00b73318",
      "score": 59.5
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
        "reverse_margin": -2.0
      },
      "new": "00b73a80",
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
        "margin": -10.0,
        "reverse_margin": -2.0
      },
      "new": "00b7b35c",
      "score": 57.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8eb5413b4b4f4c6f634bf415d03cd2ee"></a>

### v16.0.0 [`00beff74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff74.md) FUN_00beff74

`competing_candidates` 

呼出元 1件 [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md) · 呼出先 1件 [`00c5a4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4d0.md)

- 1. [`00b7336c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b7336c.md) · スコア 38.571429 · 採用条件未達 · 順位差 -37.142857 / 38.571429 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) · スコア 0.0 · 採用条件未達 · 順位差 -59.5 / -38.571429 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bba3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba3ac.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -38.571429 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.6428571428571429
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
        "reverse_margin": 38.571429
      },
      "new": "00b7336c",
      "score": 38.571429
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
        "margin": -59.5,
        "reverse_margin": -38.571429
      },
      "new": "00b73318",
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -38.571429
      },
      "new": "00bba3ac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2d270b95d3611595f5d000337e821670"></a>

### v16.0.0 [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) FUN_00bf7da4

`competing_candidates` 

呼出元 13件 [`00bf49ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md) [`00bf4b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md) [`00bf4cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md) [`00bf4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md) [`00bf4f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md) · 呼出先 4件 [`00bf7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7df8.md) [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

- 1. [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) · スコア 67.5 · 採用条件未達 · 順位差 3.75 / 3.75 · short_function_requires_other_identity_evidence, instruction_coverage
- 2. [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) · スコア 63.75 · 採用条件未達 · 順位差 -2.25 / -3.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position
- 3. [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) · スコア 57.5 · 採用条件未達 · 順位差 -2.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) · スコア 57.5 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md) · スコア 53.75 · 採用条件未達 · 順位差 -4.25 / -13.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) · スコア 53.75 · 採用条件未達 · 順位差 -2.25 / -13.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) · スコア 38.75 · 採用条件未達 · 順位差 -1.25 / -28.75 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0050d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d5a0.md) · スコア 37.142857 · 採用条件未達 · 順位差 -14.285713999999999 / -30.357143 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage"
        ],
        "margin": 3.75,
        "reverse_margin": 3.75
      },
      "new": "00b7b35c",
      "score": 67.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.5625
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -2.25,
        "reverse_margin": -3.75
      },
      "new": "0041fdf0",
      "score": 63.75
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
        "margin": -2.0,
        "reverse_margin": -10.0
      },
      "new": "00b73318",
      "score": 57.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f83f83df26cc5675d69e1f5690208029"></a>

### v16.0.0 [`00bf830c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf830c.md) FUN_00bf830c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b7b8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8c4.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 65.0,
        "reverse_margin": 65.0
      },
      "new": "00b7b8c4",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0a25c14f10a36cb943f982fbef701821"></a>

### v16.0.0 [`00bf831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf831c.md) FUN_00bf831c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00b7b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md) · スコア 61.538462 · 採用条件未達 · 順位差 6.923076999999999 / 6.923076999999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.184614999999994 / -6.923076999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b7e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md) · スコア 20.689655 · 採用条件未達 · 順位差 -16.413793000000002 / -40.84880700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00428c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c64.md) · スコア 11.538462 · 採用条件未達 · 順位差 -47.461538 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0050fa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fa98.md) · スコア 11.538462 · 採用条件未達 · 順位差 -47.461538 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007240f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/007240f8.md) · スコア 11.538462 · 採用条件未達 · 順位差 -15.461538 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.923076999999999,
        "reverse_margin": 6.923076999999999
      },
      "new": "00b7b8d4",
      "score": 61.538462
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.5769230769230769
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
        "margin": -6.184614999999994,
        "reverse_margin": -6.923076999999999
      },
      "new": "00b7b99c",
      "score": 54.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3448275862068966,
          0.38461538461538464
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
        "margin": -16.413793000000002,
        "reverse_margin": -40.84880700000001
      },
      "new": "00b7e008",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-31c90b72f802b167900b0cde6f8aff47"></a>

### v16.0.0 [`00bf83d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83d4.md) FUN_00bf83d4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b7b98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b98c.md) · スコア 65.0 · 採用条件未達 · 順位差 31.666666999999997 / 31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7ba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba00.md) · スコア 33.333333 · 採用条件未達 · 順位差 -46.666667 / -31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 31.666666999999997,
        "reverse_margin": 31.666666999999997
      },
      "new": "00b7b98c",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2222222222222222,
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
        "margin": -46.666667,
        "reverse_margin": -31.666666999999997
      },
      "new": "00b7ba00",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c5e5f042e0095e913c1429ecc34dfb89"></a>

### v16.0.0 [`00bf83e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83e4.md) FUN_00bf83e4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00b7b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md) · スコア 60.8 · 採用条件未達 · 順位差 6.184614999999994 / 6.184614999999994 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.923076999999999 / -6.184614999999994 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b7e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md) · スコア 20.689655 · 採用条件未達 · 順位差 -16.413793000000002 / -40.110344999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b7ba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba00.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.8 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "margin": 6.184614999999994,
        "reverse_margin": 6.184614999999994
      },
      "new": "00b7b99c",
      "score": 60.8
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5769230769230769,
          0.6
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
        "margin": -6.923076999999999,
        "reverse_margin": -6.184614999999994
      },
      "new": "00b7b8d4",
      "score": 54.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3448275862068966,
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
        "margin": -16.413793000000002,
        "reverse_margin": -40.110344999999995
      },
      "new": "00b7e008",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca2adaa3f873bc1e093186fd46f32fbf"></a>

### v16.0.0 [`00bf8448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8448.md) FUN_00bf8448

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b7ba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba00.md) · スコア 80.0 · 採用条件未達 · 順位差 46.666667 / 46.666667 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00b7b98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b98c.md) · スコア 33.333333 · 採用条件未達 · 順位差 -31.666666999999997 / -46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 46.666667,
        "reverse_margin": 46.666667
      },
      "new": "00b7ba00",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
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
        "margin": -31.666666999999997,
        "reverse_margin": -46.666667
      },
      "new": "00b7b98c",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1c2a529ec38ff415847adb228e3c0718"></a>

### v16.0.0 [`00bf8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md) FUN_00bf8c60

`competing_candidates` 

呼出元 1件 [`00bf8c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c40.md) · 呼出先 4件 [`00bf8c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c0c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddb0.md)

- 1. [`00b7c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md) · スコア 67.714286 · 採用条件未達 · 順位差 39.14285700000001 / 42.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7c280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c280.md) · スコア 25.714286 · 採用条件未達 · 順位差 -43.376622999999995 / -42.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b7c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c2ac.md) · スコア 25.714286 · 採用条件未達 · 順位差 -43.376622999999995 / -42.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0050e32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md) · スコア 10.285714 · 採用条件未達 · 順位差 10.285714 / -57.428572 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0050e534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md) · スコア 10.285714 · 採用条件未達 · 順位差 10.285714 / -57.428572 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0045c584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -67.714286 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0053aac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -67.714286 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b035c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -67.714286 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 39.14285700000001,
        "reverse_margin": 42.0
      },
      "new": "00b7c218",
      "score": 67.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18181818181818182,
          0.09523809523809523
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
        "margin": -43.376622999999995,
        "reverse_margin": -42.0
      },
      "new": "00b7c280",
      "score": 25.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18181818181818182,
          0.09523809523809523
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
        "margin": -43.376622999999995,
        "reverse_margin": -42.0
      },
      "new": "00b7c2ac",
      "score": 25.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0172ff239aacbf1b49435e47a0d83b40"></a>

### v16.0.0 [`00bf8cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cc8.md) FUN_00bf8cc8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)

- 1. [`00b7c280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c280.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c2ac.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00b7c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md) · スコア 25.714286 · 採用条件未達 · 順位差 -42.0 / -43.376622999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00b7c280",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00b7c2ac",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09523809523809523,
          0.18181818181818182
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
        "margin": -42.0,
        "reverse_margin": -43.376622999999995
      },
      "new": "00b7c218",
      "score": 25.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9e0b922bd40fd8123cf9727149980747"></a>

### v16.0.0 [`00bf8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8cf4.md) FUN_00bf8cf4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)

- 1. [`00b7c280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c280.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b7c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c2ac.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00b7c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md) · スコア 25.714286 · 採用条件未達 · 順位差 -42.0 / -43.376622999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00b7c280",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00b7c2ac",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.09523809523809523,
          0.18181818181818182
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
        "margin": -42.0,
        "reverse_margin": -43.376622999999995
      },
      "new": "00b7c218",
      "score": 25.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11339a5a31a5a8d1e3a07296a017e234"></a>

### v16.0.0 [`00bf8f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f98.md) FUN_00bf8f98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b7c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c550.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00b7c550",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7c871646f7855d4e09ed8d0010fbca42"></a>

### v16.0.0 [`00bf8fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8fa8.md) FUN_00bf8fa8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00b7c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c560.md) · スコア 26.602871 · 採用条件未達 · 順位差 21.340945 / 21.340945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004ffc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffc88.md) · スコア 5.261926 · 採用条件未達 · 順位差 5.261926 / -21.340945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a5ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ee5c.md) · スコア 3.59412 · 採用条件未達 · 順位差 -60.00327 / -23.008751 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · スコア 1.401869 · 採用条件未達 · 順位差 -5.007319000000001 / -25.201002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006568ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md) · スコア 0.194805 · 採用条件未達 · 順位差 -14.116883 / -26.408066 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.460568 / -26.602871 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) · スコア 0.0 · 採用条件未達 · 順位差 -5.217391 / -26.602871 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -26.602871 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.4444444444444444,
          0.42105263157894735
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 21.340945,
        "reverse_margin": 21.340945
      },
      "new": "00b7c560",
      "score": 26.602871
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07462686567164178,
          0.10101010101010101
        ],
        "cfg_coverage": [
          0.0392156862745098,
          0.10526315789473684
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 5.261926,
        "reverse_margin": -21.340945
      },
      "new": "004ffc88",
      "score": 5.261926
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05405405405405406,
          0.08080808080808081
        ],
        "cfg_coverage": [
          0.017543859649122806,
          0.05263157894736842
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.00327,
        "reverse_margin": -23.008751
      },
      "new": "00a5ee5c",
      "score": 3.59412
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-473060986e6deb3030152732d264abac"></a>

### v16.0.0 [`00bf9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9c60.md) FUN_00bf9c60

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00b7d218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md) · スコア 56.521739 · 採用条件未達 · 順位差 5.217390999999999 / 5.217390999999999 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf90.md) · スコア 51.304348 · 採用条件未達 · 順位差 -6.590389000000002 / -5.217390999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0043bfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bfdc.md) · スコア 51.304348 · 採用条件未達 · 順位差 -2.9813660000000013 / -5.217390999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0045ca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045ca50.md) · スコア 51.304348 · 採用条件未達 · 順位差 -2.9813660000000013 / -5.217390999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00596708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596708.md) · スコア 51.304348 · 採用条件未達 · 順位差 -2.9813660000000013 / -5.217390999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0056459c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/0056459c.md) · スコア 15.652174 · 採用条件未達 · 順位差 -35.776396999999996 / -40.869564999999994 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`004a7cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7cbc.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.714286 / -56.521739 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00b7d274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d274.md) · スコア 0.0 · 採用条件未達 · 順位差 -69.090909 / -56.521739 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6086956521739131,
          0.6086956521739131
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
        "margin": 5.217390999999999,
        "reverse_margin": 5.217390999999999
      },
      "new": "00b7d218",
      "score": 56.521739
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.631578947368421,
          0.5217391304347826
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
        "margin": -6.590389000000002,
        "reverse_margin": -5.217390999999999
      },
      "new": "0043bf90",
      "score": 51.304348
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5217391304347826
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
        "margin": -2.9813660000000013,
        "reverse_margin": -5.217390999999999
      },
      "new": "0043bfdc",
      "score": 51.304348
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b9cca1fa3ad619285faa6cb3bf96fa01"></a>

### v16.0.0 [`00bf9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9cbc.md) FUN_00bf9cbc

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)

- 1. [`00b7d274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d274.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / 16.047431000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b7d218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md) · スコア 33.043478 · 採用条件未達 · 順位差 -23.478260999999996 / -16.047431000000003 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": -19.999999999999993,
        "reverse_margin": 16.047431000000003
      },
      "new": "00b7d274",
      "score": 49.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21739130434782608,
          0.45454545454545453
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
        "margin": -23.478260999999996,
        "reverse_margin": -16.047431000000003
      },
      "new": "00b7d218",
      "score": 33.043478
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-92574591c1f99771df2828a9553f1dfb"></a>

### v16.0.0 [`00bfa854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md) FUN_00bfa854

`competing_candidates` 

呼出元 1件 [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)

- 1. [`00b7de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de0c.md) · スコア 71.428571 · 採用条件未達 · 順位差 71.428571 / 71.428571 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 71.428571,
        "reverse_margin": 71.428571
      },
      "new": "00b7de0c",
      "score": 71.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6100afb5caa5bdd875c03b2f377a0f26"></a>

### v16.0.0 [`00bfaa40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa40.md) FUN_00bfaa40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b7dff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dff8.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 65.0,
        "reverse_margin": 65.0
      },
      "new": "00b7dff8",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dd4c907afc83b2ee67e3f97f2e93c580"></a>

### v16.0.0 [`00bfaa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa50.md) FUN_00bfaa50

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

- 1. [`00b7e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md) · スコア 37.103448 · 採用条件未達 · 順位差 16.413793000000002 / 16.413793000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b7b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.84880700000001 / -16.413793000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b7b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.110344999999995 / -16.413793000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00428bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428bc0.md) · スコア 10.344828 · 採用条件未達 · 順位差 -49.655172 / -26.75862 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5517241379310345,
          0.5517241379310345
        ],
        "cfg_coverage": [
          0.2,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 16.413793000000002,
        "reverse_margin": 16.413793000000002
      },
      "new": "00b7e008",
      "score": 37.103448
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38461538461538464,
          0.3448275862068966
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
        "margin": -40.84880700000001,
        "reverse_margin": -16.413793000000002
      },
      "new": "00b7b8d4",
      "score": 20.689655
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
          0.3448275862068966
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
        "margin": -40.110344999999995,
        "reverse_margin": -16.413793000000002
      },
      "new": "00b7b99c",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-507211fe24479598281b7752efb3d5b2"></a>

### v16.0.0 [`00bfb6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6f4.md) FUN_00bfb6f4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daf0.md)

- 1. [`00b7ecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ecac.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 69.090909 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.090908999999996,
        "reverse_margin": 69.090909
      },
      "new": "00b7ecac",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c530d9153e4a5bb9f44a166142b0b3ba"></a>

### v16.0.0 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) FUN_00c05b30

`competing_candidates` 

呼出元 71件 [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) [`00c0dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) · 呼出先 4件 [`00c37b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e080.md)

- 1. [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) · スコア 68.571429 · 採用条件未達 · 順位差 38.571428999999995 / 9.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage
- 2. [`00b736e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b736e8.md) · スコア 58.571429 · 採用条件未達 · 順位差 58.571429 / -9.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -14.285714999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) · スコア 30.0 · 採用条件未達 · 順位差 -50.0 / -38.571428999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 5. [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) · スコア 30.0 · 採用条件未達 · 順位差 -60.0 / -38.571428999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 6. [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) · スコア 30.0 · 採用条件未達 · 順位差 -50.0 / -38.571428999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 7. [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) · スコア 30.0 · 採用条件未達 · 順位差 -45.0 / -38.571428999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position
- 8. [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) · スコア 30.0 · 採用条件未達 · 順位差 -52.0 / -38.571428999999995 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.6428571428571429
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage"
        ],
        "margin": 38.571428999999995,
        "reverse_margin": 9.999999999999993
      },
      "new": "00b890e8",
      "score": 68.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.6428571428571429
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
        "margin": 58.571429,
        "reverse_margin": -9.999999999999993
      },
      "new": "00b736e8",
      "score": 58.571429
    },
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 54.285714,
        "reverse_margin": -14.285714999999996
      },
      "new": "0041e380",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-62791976409e321f2e9bdfa23dea58a9"></a>

### v16.0.0 [`00c05bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md) FUN_00c05bd4

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

- 1. [`00b8918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8918c.md) · スコア 56.909091 · 採用条件未達 · 順位差 8.623376999999998 / 8.623376999999998 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b89294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89294.md) · スコア 48.285714 · 採用条件未達 · 順位差 -25.714286 / -8.623376999999998 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b89210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89210.md) · スコア 44.181818 · 採用条件未達 · 順位差 -30.909090999999997 / -12.727272999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b316c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md) · スコア 31.294118 · 採用条件未達 · 順位差 -29.999999999999996 / -25.614972999999996 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b314d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md) · スコア 29.636364 · 採用条件未達 · 順位差 -19.589442 / -27.272726999999996 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b3154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md) · スコア 29.636364 · 採用条件未達 · 順位差 -44.363636 / -27.272726999999996 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0041876c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) · スコア 6.382979 · 採用条件未達 · 順位差 6.382979 / -50.526112 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b315c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b315c4.md) · スコア 6.0 · 採用条件未達 · 順位差 -20.625 / -50.909091 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5151515151515151,
          0.5151515151515151
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 8.623376999999998,
        "reverse_margin": 8.623376999999998
      },
      "new": "00b8918c",
      "score": 56.909091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.37142857142857144,
          0.3939393939393939
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.714286,
        "reverse_margin": -8.623376999999998
      },
      "new": "00b89294",
      "score": 48.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30303030303030304,
          0.30303030303030304
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.909090999999997,
        "reverse_margin": -12.727272999999997
      },
      "new": "00b89210",
      "score": 44.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e4fa7228a3446ddd84de9065591fe7bd"></a>

### v16.0.0 [`00c05c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md) FUN_00c05c58

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

- 1. [`00b89210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89210.md) · スコア 75.090909 · 採用条件未達 · 順位差 6.233766000000003 / 6.233766000000003 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b89294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89294.md) · スコア 68.857143 · 採用条件未達 · 順位差 -5.1428570000000065 / -6.233766000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b8918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8918c.md) · スコア 44.181818 · 採用条件未達 · 順位差 -12.727272999999997 / -30.909090999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b316c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md) · スコア 33.058824 · 採用条件未達 · 順位差 -28.235293999999996 / -42.032084999999995 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b314d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md) · スコア 31.454545 · 採用条件未達 · 順位差 -17.771261 / -43.636364 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b3154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md) · スコア 31.454545 · 採用条件未達 · 順位差 -42.545455000000004 / -43.636364 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00b315c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b315c4.md) · スコア 6.0 · 採用条件未達 · 順位差 -20.625 / -69.090909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00b31644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31644.md) · スコア 6.0 · 採用条件未達 · 順位差 -20.625 / -69.090909 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.233766000000003,
        "reverse_margin": 6.233766000000003
      },
      "new": "00b89210",
      "score": 75.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7142857142857143,
          0.7575757575757576
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.1428570000000065,
        "reverse_margin": -6.233766000000003
      },
      "new": "00b89294",
      "score": 68.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30303030303030304,
          0.30303030303030304
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.727272999999997,
        "reverse_margin": -30.909090999999997
      },
      "new": "00b8918c",
      "score": 44.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fb64f0b293240be02be4bc74caeb2d66"></a>

### v16.0.0 [`00c05cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md) FUN_00c05cdc

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

- 1. [`00b89294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89294.md) · スコア 74.0 · 採用条件未達 · 順位差 5.1428570000000065 / 5.1428570000000065 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00b89210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89210.md) · スコア 68.857143 · 採用条件未達 · 順位差 -6.233766000000003 / -5.1428570000000065 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b8918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8918c.md) · スコア 48.285714 · 採用条件未達 · 順位差 -8.623376999999998 / -25.714286 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b316c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md) · スコア 34.571429 · 採用条件未達 · 順位差 -26.722688999999995 / -39.428571 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b315c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b315c4.md) · スコア 6.0 · 採用条件未達 · 順位差 -20.625 / -68.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b31644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31644.md) · スコア 6.0 · 採用条件未達 · 順位差 -20.625 / -68.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00b8976c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8976c.md) · スコア 0.0 · 採用条件未達 · 順位差 -38.285714 / -74.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00b89814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89814.md) · スコア 0.0 · 採用条件未達 · 順位差 -34.285714 / -74.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8,
          0.8
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.1428570000000065,
        "reverse_margin": 5.1428570000000065
      },
      "new": "00b89294",
      "score": 74.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7575757575757576,
          0.7142857142857143
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -6.233766000000003,
        "reverse_margin": -5.1428570000000065
      },
      "new": "00b89210",
      "score": 68.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3939393939393939,
          0.37142857142857144
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.623376999999998,
        "reverse_margin": -25.714286
      },
      "new": "00b8918c",
      "score": 48.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-afc85fe2e17570a50a5999be09465329"></a>

### v16.0.0 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) FUN_00c05d68

`competing_candidates` 

呼出元 1件 [`00c06350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md) · 呼出先 12件 [`00c061b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md) [`00c0625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md) [`00c06414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md) [`00c06aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md) [`00c578e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578e4.md)

- 1. [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · スコア 9.272727 · 採用条件未達 · 順位差 1.4805190000000001 / 6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00b80e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md) · スコア 2.874251 · 採用条件未達 · 順位差 -1.228313 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b8506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md) · スコア 2.874251 · 採用条件未達 · 順位差 -1.2996619999999997 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) · スコア 2.874251 · 採用条件未達 · 順位差 -3.125749 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) · スコア 2.874251 · 採用条件未達 · 順位差 -3.2016979999999995 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) · スコア 2.874251 · 採用条件未達 · 順位差 -3.4415379999999995 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) · スコア 2.874251 · 採用条件未達 · 順位差 -3.4415379999999995 / -6.398476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) · スコア 2.51497 · 採用条件未達 · 順位差 -4.737777 / -6.757757 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12121212121212122,
          0.16766467065868262
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
        "margin": 1.4805190000000001,
        "reverse_margin": 6.398476
      },
      "new": "00b89320",
      "score": 9.272727
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06837606837606838,
          0.04790419161676647
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
        "margin": -1.228313,
        "reverse_margin": -6.398476
      },
      "new": "00b80e30",
      "score": 2.874251
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06956521739130435,
          0.04790419161676647
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
        "margin": -1.2996619999999997,
        "reverse_margin": -6.398476
      },
      "new": "00b8506c",
      "score": 2.874251
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-00fd5a202ab88354a3e22f83a77bd3cd"></a>

### v16.0.0 [`00c06004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06004.md) FUN_00c06004

`competing_candidates` 

呼出元 1件 [`00c578e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578e4.md) · 呼出先 2件 [`00c0625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

- 1. [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · スコア 7.792208 · 採用条件未達 · 順位差 -1.4805190000000001 / 1.476419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) · スコア 6.315789 · 採用条件未達 · 順位差 3.4415379999999995 / -1.476419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) · スコア 6.315789 · 採用条件未達 · 順位差 3.4415379999999995 / -1.476419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) · スコア 6.075949 · 採用条件未達 · 順位差 3.2016979999999995 / -1.716259 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) · スコア 6.0 · 採用条件未達 · 順位差 3.125749 / -1.7922079999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) · スコア 5.373134 · 採用条件未達 · 順位差 -1.879613 / -2.4190739999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b8506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md) · スコア 4.173913 · 採用条件未達 · 順位差 1.2996619999999997 / -3.618295 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b80e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md) · スコア 4.102564 · 採用条件未達 · 順位差 1.228313 / -3.6896439999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12987012987012986,
          0.46875
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
        "margin": -1.4805190000000001,
        "reverse_margin": 1.476419
      },
      "new": "00b89320",
      "score": 7.792208
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10526315789473684,
          0.125
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
        "margin": 3.4415379999999995,
        "reverse_margin": -1.476419
      },
      "new": "00bb97f8",
      "score": 6.315789
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10526315789473684,
          0.125
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
        "margin": 3.4415379999999995,
        "reverse_margin": -1.476419
      },
      "new": "00bb9940",
      "score": 6.315789
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-868a34179d0d89c2898b97661dd524f6"></a>

### v16.0.0 [`00c061b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md) FUN_00c061b4

`competing_candidates` 

呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 4件 [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

- 1. [`00b8976c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8976c.md) · スコア 38.285714 · 採用条件未達 · 順位差 4.0 / 1.1428569999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004a5654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md) · スコア 37.142857 · 採用条件未達 · 順位差 0.0 / -1.1428569999999993 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00584fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md) · スコア 37.142857 · 採用条件未達 · 順位差 0.0 / -1.1428569999999993 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b89814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89814.md) · スコア 34.285714 · 採用条件未達 · 順位差 0.0 / -4.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) · スコア 13.714286 · 採用条件未達 · 順位差 0.0 / -24.571427999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004e6a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md) · スコア 12.0 · 採用条件未達 · 順位差 0.0 / -26.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00583d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md) · スコア 12.0 · 採用条件未達 · 順位差 0.0 / -26.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005866f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md) · スコア 8.571429 · 採用条件未達 · 順位差 0.0 / -29.714284999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 4.0,
        "reverse_margin": 1.1428569999999993
      },
      "new": "00b8976c",
      "score": 38.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5882352941176471,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -1.1428569999999993
      },
      "new": "004a5654",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45454545454545453,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -1.1428569999999993
      },
      "new": "00584fe0",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1ff0a4f7528d66d0a4099f1eb68d0069"></a>

### v16.0.0 [`00c0625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md) FUN_00c0625c

`competing_candidates` 

呼出元 2件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06004.md) · 呼出先 4件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfe0.md)

- 1. [`004a5654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md) · スコア 37.142857 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00584fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md) · スコア 37.142857 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00b8976c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b8976c.md) · スコア 34.285714 · 採用条件未達 · 順位差 -4.0 / -2.8571430000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b89814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89814.md) · スコア 34.285714 · 採用条件未達 · 順位差 0.0 / -2.8571430000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) · スコア 13.714286 · 採用条件未達 · 順位差 0.0 / -23.428570999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004e6a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md) · スコア 12.0 · 採用条件未達 · 順位差 0.0 / -25.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00583d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md) · スコア 12.0 · 採用条件未達 · 順位差 0.0 / -25.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005866f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md) · スコア 8.571429 · 採用条件未達 · 順位差 0.0 / -28.571427999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "004a5654",
      "score": 37.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.45454545454545453,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00584fe0",
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
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.0,
        "reverse_margin": -2.8571430000000007
      },
      "new": "00b8976c",
      "score": 34.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2d06e6227479c7c222387027ec04806a"></a>

### v16.0.0 [`00c06a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06a7c.md) FUN_00c06a7c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfc0.md)

- 1. [`00b8a034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a034.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 69.090909 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.090908999999996,
        "reverse_margin": 69.090909
      },
      "new": "00b8a034",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4e5fb19fa3e890de1ee882ee5547193a"></a>

### v16.0.0 [`00c06e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e08.md) FUN_00c06e08

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfc0.md)

- 1. [`00b8a3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3c0.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 69.090909 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.090908999999996,
        "reverse_margin": 69.090909
      },
      "new": "00b8a3c0",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fb90c44673896b1a2eaf1a8b5304fb27"></a>

### v16.0.0 [`00c070fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md) _INIT_2

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00c063e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c063e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5e0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md)

- 1. [`00b8a6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a6b4.md) · スコア 64.352941 · 採用条件未達 · 順位差 62.352941 / 64.352941 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 62.352941,
        "reverse_margin": 64.352941
      },
      "new": "00b8a6b4",
      "score": 64.352941
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2f09531b5a7ebf8c7f51ec91f77424c3"></a>

### v16.0.0 [`00c2b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b41c.md) FUN_00c2b41c

`competing_candidates` 

呼出元 2件 [`00c2b3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b3ac.md) [`00c2b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b8c0.md) · 呼出先 0件 

- 1. [`00bae9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae9d4.md) · スコア 76.659146 · 採用条件未達 · 順位差 69.83216700000001 / 69.82515400000001 · cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00bac130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac130.md) · スコア 6.833992 · 採用条件未達 · 順位差 6.833992 / -69.82515400000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md) · スコア 6.257669 · 採用条件未達 · 順位差 2.298237 / -70.401477 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9815950920245399,
          0.9815950920245399
        ],
        "cfg_coverage": [
          0.6881720430107527,
          0.7191011235955056
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 69.83216700000001,
        "reverse_margin": 69.82515400000001
      },
      "new": "00bae9d4",
      "score": 76.659146
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10303030303030303,
          0.10429447852760736
        ],
        "cfg_coverage": [
          0.03260869565217391,
          0.033707865168539325
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 6.833992,
        "reverse_margin": -69.82515400000001
      },
      "new": "00bac130",
      "score": 6.833992
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11724137931034483,
          0.10429447852760736
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
        "margin": 2.298237,
        "reverse_margin": -70.401477
      },
      "new": "00bacaa4",
      "score": 6.257669
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-721f8380c7f654d46687e668cba93de9"></a>

### v16.0.0 [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) FUN_00c2cb6c

`competing_candidates` 

呼出元 1件 [`00c2caec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2caec.md) · 呼出先 5件 [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md) [`00c358e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c358e8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

- 1. [`00bb0124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0124.md) · スコア 21.237569 · 採用条件未達 · 順位差 15.485957 / 13.015347 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bafc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc6c.md) · スコア 8.222222 · 採用条件未達 · 順位差 6.222222 / -13.015347 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb0bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0bb8.md) · スコア 3.818182 · 採用条件未達 · 順位差 -10.363636 / -17.419387 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bb0464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0464.md) · スコア 2.0 · 採用条件未達 · 順位差 -2.4713960000000004 / -19.237569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bb114c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb114c.md) · スコア 2.0 · 採用条件未達 · 順位差 2.0 / -19.237569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bb1298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1298.md) · スコア 2.0 · 採用条件未達 · 順位差 -2.2105259999999998 / -19.237569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00467098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.383178 / -21.237569 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.287292817679558,
          0.287292817679558
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
        "margin": 15.485957,
        "reverse_margin": 13.015347
      },
      "new": "00bb0124",
      "score": 21.237569
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1037037037037037,
          0.15469613259668508
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
        "margin": 6.222222,
        "reverse_margin": -13.015347
      },
      "new": "00bafc6c",
      "score": 8.222222
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.030303030303030304,
          0.055248618784530384
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
        "margin": -10.363636,
        "reverse_margin": -17.419387
      },
      "new": "00bb0bb8",
      "score": 3.818182
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ba564aa67b920aff2bc0603845680258"></a>

### v16.0.0 [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) FUN_00c2d600

`competing_candidates` 

呼出元 1件 [`00c2d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d580.md) · 呼出先 5件 [`00bf2f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2f78.md) [`00c35aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35aa8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

- 1. [`00bb0bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0bb8.md) · スコア 14.181818 · 採用条件未達 · 順位差 10.363636 / 9.710422 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bb0464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0464.md) · スコア 4.471396 · 採用条件未達 · 順位差 2.4713960000000004 / -9.710422 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb0124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0124.md) · スコア 3.818182 · 採用条件未達 · 順位差 -17.419387 / -10.363636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bafc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc6c.md) · スコア 2.0 · 採用条件未達 · 順位差 -6.222222 / -12.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00467098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.383178 / -14.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1696969696969697,
          0.1696969696969697
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
        "margin": 10.363636,
        "reverse_margin": 9.710422
      },
      "new": "00bb0bb8",
      "score": 14.181818
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.041189931350114416,
          0.05454545454545454
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
        "margin": 2.4713960000000004,
        "reverse_margin": -9.710422
      },
      "new": "00bb0464",
      "score": 4.471396
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.055248618784530384,
          0.030303030303030304
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
        "margin": -17.419387,
        "reverse_margin": -10.363636
      },
      "new": "00bb0124",
      "score": 3.818182
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-79f2f8983a7d242fb8fd724e02002393"></a>

### v16.0.0 [`00c34834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34834.md) FUN_00c34834

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)

- 1. [`00b88c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md) · スコア 69.090909 · 採用条件未達 · 順位差 69.090909 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bb8724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md) · スコア 69.090909 · 採用条件未達 · 順位差 69.090909 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dec.md) · スコア 21.818182 · 採用条件未達 · 順位差 -47.272726999999996 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bb7e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e18.md) · スコア 21.818182 · 採用条件未達 · 順位差 -47.272726999999996 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": 69.090909,
        "reverse_margin": 0.0
      },
      "new": "00b88c34",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 69.090909,
        "reverse_margin": 0.0
      },
      "new": "00bb8724",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36363636363636365,
          0.36363636363636365
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
        "margin": -47.272726999999996,
        "reverse_margin": -47.272726999999996
      },
      "new": "00bb7dec",
      "score": 21.818182
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e03e1f743081df5227c272869b2834f2"></a>

### v16.0.0 [`00c34860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34860.md) FUN_00c34860

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)

- 1. [`00bb7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dec.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb7e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e18.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 14.090908999999996,
        "reverse_margin": 0.0
      },
      "new": "00bb7dec",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 14.090908999999996,
        "reverse_margin": 0.0
      },
      "new": "00bb7e18",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b9e61d190d02178046effe7ee9f1249a"></a>

### v16.0.0 [`00c348e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348e4.md) FUN_00c348e4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)

- 1. [`00bb7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e9c.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb7ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ec8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ef4.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f20.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb7e9c",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ec8",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ef4",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e438563b461c4dd4bae580123720eea0"></a>

### v16.0.0 [`00c34910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34910.md) FUN_00c34910

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)

- 1. [`00bb7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e9c.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb7ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ec8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ef4.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f20.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb7e9c",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ec8",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ef4",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00c3493c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3493c.md) FUN_00c3493c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)

- 1. [`00bba420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md) · スコア 69.090909 · 採用条件未達 · 順位差 10.909090999999997 / 19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00ba9688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bbb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) · スコア 27.272727 · 採用条件未達 · 順位差 0.0 / -41.81818199999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0051a82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a82c.md) · スコア 21.818182 · 採用条件未達 · 順位差 -44.848485000000004 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md) · スコア 21.818182 · 採用条件未達 · 順位差 -36.363636 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0072b94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b94c.md) · スコア 21.818182 · 採用条件未達 · 順位差 -24.848484999999997 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bb7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e9c.md) · スコア 21.818182 · 採用条件未達 · 順位差 -47.272726999999996 / -47.272726999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": 10.909090999999997,
        "reverse_margin": 19.999999999999993
      },
      "new": "00bba420",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": -19.999999999999993,
        "reverse_margin": -19.999999999999993
      },
      "new": "00ba9688",
      "score": 49.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": -19.999999999999993,
        "reverse_margin": -19.999999999999993
      },
      "new": "00bbb000",
      "score": 49.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7867be9401ba11cdf27323f2cea644f1"></a>

### v16.0.0 [`00c34968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34968.md) FUN_00c34968

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)

- 1. [`00bb7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e9c.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb7ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ec8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ef4.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f20.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb7e9c",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ec8",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb7ef4",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7719685c0decd43cc610ff46efaf548f"></a>

### v16.0.0 [`00c34a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a80.md) FUN_00c34a80

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e380.md)

- 1. [`00bb8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8038.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8064.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb8038",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb8064",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb80bc",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.0 [`00c34aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34aac.md) FUN_00c34aac

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e360.md)

- 1. [`00ba9688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bba420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bbb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) · スコア 27.272727 · 採用条件未達 · 順位差 0.0 / -21.818182000000004 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0051a82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a82c.md) · スコア 21.818182 · 採用条件未達 · 順位差 -44.848485000000004 / -27.272727000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md) · スコア 21.818182 · 採用条件未達 · 順位差 -36.363636 / -27.272727000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0072b94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b94c.md) · スコア 21.818182 · 採用条件未達 · 順位差 -24.848484999999997 / -27.272727000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bb8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8038.md) · スコア 21.818182 · 採用条件未達 · 順位差 -47.272726999999996 / -27.272727000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": -19.999999999999993,
        "reverse_margin": 0.0
      },
      "new": "00ba9688",
      "score": 49.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": -19.999999999999993,
        "reverse_margin": 0.0
      },
      "new": "00bba420",
      "score": 49.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": -19.999999999999993,
        "reverse_margin": 0.0
      },
      "new": "00bbb000",
      "score": 49.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d8cfbf9e9843499b56b1b1516c88378"></a>

### v16.0.0 [`00c34ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ad8.md) FUN_00c34ad8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8038.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8064.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb8038",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb8064",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb80bc",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-30985a7c6226612a2873fdf96e234863"></a>

### v16.0.0 [`00c34b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b04.md) FUN_00c34b04

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8038.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8064.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb8038",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb8064",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb80bc",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-abc124ed3ab076ef88c0aa27fbd08308"></a>

### v16.0.0 [`00c34b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b30.md) FUN_00c34b30

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00b7d274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d274.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00baf6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf6fc.md) · スコア 49.090909 · 採用条件未達 · 順位差 49.090909 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb800c.md) · スコア 49.090909 · 採用条件未達 · 順位差 49.090909 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bb8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8064.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "reverse_margin": 19.999999999999993
      },
      "new": "00b7d274",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 49.090909,
        "reverse_margin": -19.999999999999993
      },
      "new": "00baf6fc",
      "score": 49.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 49.090909,
        "reverse_margin": -19.999999999999993
      },
      "new": "00bb800c",
      "score": 49.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5d579314b0d0384a099ae882ba8e639f"></a>

### v16.0.0 [`00c34b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b5c.md) FUN_00c34b5c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb80bc",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb80e8",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
      "new": "00bb8114",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4733d582e61c568438710dcb784e4370"></a>

### v16.0.0 [`00c34b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b88.md) _ZNSt6__ndk119__shared_weak_countD1Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb8140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8140.md) · スコア 28.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8174.md) · スコア 13.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8140",
      "score": 28.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8174",
      "score": 13.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb80bc",
      "score": 3.4545
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0006fe32a858509f2575dab0954ce968"></a>

### v16.0.0 [`00c34b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34b90.md) FUN_00c34b90

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00b72b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b5c.md) · スコア 69.090909 · 採用条件未達 · 順位差 69.090909 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bbb2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2ec.md) · スコア 69.090909 · 採用条件未達 · 順位差 69.090909 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bbb44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb44c.md) · スコア 69.090909 · 採用条件未達 · 順位差 69.090909 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 49.090909 · 採用条件未達 · 順位差 -19.999999999999993 / -19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) · スコア 45.0 · 採用条件未達 · 順位差 -25.0 / -24.090908999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
        "margin": 69.090909,
        "reverse_margin": 0.0
      },
      "new": "00b72b5c",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 69.090909,
        "reverse_margin": 0.0
      },
      "new": "00bbb2ec",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 69.090909,
        "reverse_margin": 0.0
      },
      "new": "00bbb44c",
      "score": 69.090909
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e3eed7f9f38b09f783bbaaff6acebfc3"></a>

### v16.0.0 [`00c34bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bbc.md) _ZNSt6__ndk119__shared_weak_countD1Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb8174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8174.md) · スコア 28.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8140.md) · スコア 13.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 3.4545 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) · スコア 2.8095 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8174",
      "score": 28.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8140",
      "score": 13.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8114",
      "score": 3.4545
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ce0754611dfb3fb9eebda6dfff852563"></a>

### v16.0.0 [`00c34bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bc4.md) FUN_00c34bc4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 69.090909 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 69.090909 · 採用条件未達 · 順位差 14.090908999999996 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) · スコア 65.0 · 採用条件未達 · 順位差 -5.0 / -4.090908999999996 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) · スコア 58.571429 · 採用条件未達 · 順位差 -4.285713999999999 / -10.519479999999994 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
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
      "new": "00bb8148",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8181818181818182,
          0.8181818181818182
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
        "margin": 14.090908999999996,
        "reverse_margin": 0.0
      },
      "new": "00bb817c",
      "score": 69.090909
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
          0.8181818181818182
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
        "reverse_margin": -4.090908999999996
      },
      "new": "00bb81a8",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a890a70809ffbea1298eae1eb597095c"></a>

### v16.0.0 [`00c34bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34bf0.md) FUN_00c34bf0

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00c36824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00b82a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md) · スコア 50.0 · 採用条件未達 · 順位差 -20.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) · スコア 50.0 · 採用条件未達 · 順位差 -20.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bb82c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82c4.md) · スコア 50.0 · 採用条件未達 · 順位差 -20.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) · スコア 45.0 · 採用条件未達 · 順位差 -24.090908999999996 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 45.0 · 採用条件未達 · 順位差 -24.090908999999996 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) · スコア 42.857143 · 採用条件未達 · 順位差 -20.0 / -7.142856999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bb82f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82f4.md) · スコア 42.857143 · 採用条件未達 · 順位差 -20.0 / -7.142856999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00b7ca74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ca74.md) · スコア 21.176471 · 採用条件未達 · 順位差 -30.588234999999997 / -28.823529 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": -20.0,
        "reverse_margin": 0.0
      },
      "new": "00b82a34",
      "score": 50.0
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
      "new": "00bb81a8",
      "score": 50.0
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
      "new": "00bb82c4",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-841cb2673005221052036431301ee1e8"></a>

### v16.0.0 [`00c34c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c20.md) FUN_00c34c20

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`00c36824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36824.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)

- 1. [`00bbb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb160.md) · スコア 45.714286 · 採用条件未達 · 順位差 45.714286 / 2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00b82a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md) · スコア 42.857143 · 採用条件未達 · 順位差 -27.142857 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) · スコア 42.857143 · 採用条件未達 · 順位差 -27.142857 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) · スコア 42.857143 · 採用条件未達 · 順位差 -20.0 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bb82c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82c4.md) · スコア 42.857143 · 採用条件未達 · 順位差 -27.142857 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bb82f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82f4.md) · スコア 42.857143 · 採用条件未達 · 順位差 -20.0 / -2.8571430000000007 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) · スコア 38.571429 · 採用条件未達 · 順位差 -30.519479999999994 / -7.142856999999999 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ba8bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8bec.md) · スコア 30.0 · 採用条件未達 · 順位差 30.0 / -15.714286000000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 45.714286,
        "reverse_margin": 2.8571430000000007
      },
      "new": "00bbb160",
      "score": 45.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8333333333333334,
          0.7142857142857143
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
        "margin": -27.142857,
        "reverse_margin": -2.8571430000000007
      },
      "new": "00b82a34",
      "score": 42.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8333333333333334,
          0.7142857142857143
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
        "margin": -27.142857,
        "reverse_margin": -2.8571430000000007
      },
      "new": "00bb81a8",
      "score": 42.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c48da075f087cb9453ef1f102368f4ce"></a>

### v16.0.0 [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) FUN_00c34c64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb821c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8338.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8228.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb821c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8338",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8228",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-316c765c56ddcfdba740f10261e074e8"></a>

### v16.0.0 [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) FUN_00c34c70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8228.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8344.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb821c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8228",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8344",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb821c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a8917f7d5989602455824884e97ce25f"></a>

### v16.0.0 [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) FUN_00c34c7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8350.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb821c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8228.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8234",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8350",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb821c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6cfd75d8e424072116c9b3e0462176e6"></a>

### v16.0.0 [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) FUN_00c34c88

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb835c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb835c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb821c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8228.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8240",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb835c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb821c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c896bbaa54afb834e1e458323fd05f35"></a>

### v16.0.0 [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) FUN_00c34c94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8368.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8228.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb8270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8270.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb824c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8368",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8228",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ebbf8ca832473696babc3507db527432"></a>

### v16.0.0 [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) FUN_00c34ca0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8374.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8234.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8270.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb827c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8258",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8374",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8234",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-db10bb7e774aa63609d13bdb37db27c3"></a>

### v16.0.0 [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) FUN_00c34cac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8380.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8240.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb8270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8270.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb827c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb8288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8288.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8264",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8380",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8240",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab747f872102678c1dcaa1e456c78a84"></a>

### v16.0.0 [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) FUN_00c34cb8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb8270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8270.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb838c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb838c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb824c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb827c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8288.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb8294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8294.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb8270",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb838c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb824c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0588da8f5cdf537c7e7cf560c347156a"></a>

### v16.0.0 [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) FUN_00c34cc4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb827c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bb8398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8398.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bb8258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8258.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bb8264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8264.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bb8270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8270.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bb8288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8288.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00bb8294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8294.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00bb82a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bb827c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8398",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bb8258",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

