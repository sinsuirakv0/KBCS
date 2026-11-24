# v16.0.0 → v16.0.1 · 追加調査 (85)

[一覧の目次](README.md)

<a id="review-1259f93c0c29bc20fa71d08a8cb45ecb"></a>

### v16.0.1 [`00bc1274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1274.md) FUN_00bc1274

`competing_candidates` 

呼出元 1件 [`00bc1314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md) · 呼出先 0件 

- 1. [`00bc0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e4c.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bc0e4c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ce1b6fa3677c1d374237c7bf9f32e302"></a>

### v16.0.1 [`00bca034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca034.md) FUN_00bca034

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bc9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c0c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bc9c0c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-65daa6e142f3f711b06fac02d1dca33e"></a>

### v16.0.1 [`00bca050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca050.md) FUN_00bca050

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bc9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c28.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00bc9c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c0c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bc9c28",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bc9c0c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2d4b6cf2e7f4f5d4f37f11efc6cd8447"></a>

### v16.0.1 [`00bca4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d0.md) FUN_00bca4d0

`competing_candidates` [`00bca0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0a8.md)

呼出元 1件 [`00bcc10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00bca4a0",
    "00bca4dc",
    "00bca078",
    "00bca0b4"
  ],
  "initial_reason": ""
}
~~~

<a id="review-4a04f0d14e7c663a5a05ed7c92357801"></a>

### v16.0.1 [`00bca4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d8.md) FUN_00bca4d8

`competing_candidates` 

呼出元 1件 [`00bcc10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) · 呼出先 0件 

- 1. [`00bca0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bca0b0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v16.0.1 [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) FUN_00be2268

`competing_candidates` 

呼出元 2件 [`00be224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be224c.md) [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) · 呼出先 4件 [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) [`00be9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9028.md) [`00be92e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be92e8.md) [`00be9410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9410.md)

- 1. [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · スコア 81.471366 · 採用条件未達 · 順位差 3.902025000000009 / 3.902025000000009 · insufficient_independent_call_anchors
- 2. [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · スコア 77.569341 · 採用条件未達 · 順位差 -3.902025000000009 / -3.902025000000009 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) · スコア 65.991189 · 採用条件未達 · 順位差 8.315214000000005 / -15.480176999999998 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · スコア 52.907489 · 採用条件未達 · 順位差 -28.554394000000002 / -28.563877000000005 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · スコア 30.443994 · 採用条件未達 · 順位差 -0.8434649999999984 / -51.027372 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · スコア 28.566246 · 採用条件未達 · 順位差 -52.895637 / -52.905120000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) · スコア 19.028291 · 採用条件未達 · 順位差 1.0848729999999982 / -62.44307500000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9911894273127754,
          0.9911894273127754
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.902025000000009,
        "reverse_margin": 3.902025000000009
      },
      "new": "00be1e40",
      "score": 81.471366
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9823788546255506,
          0.9823788546255506
        ],
        "cfg_coverage": [
          0.9313304721030042,
          0.9353448275862069
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.902025000000009,
        "reverse_margin": -3.902025000000009
      },
      "new": "00be33c0",
      "score": 77.569341
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7665198237885462,
          0.7665198237885462
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
        "margin": 8.315214000000005,
        "reverse_margin": -15.480176999999998
      },
      "new": "00be2c8c",
      "score": 65.991189
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) FUN_00be29a0

`competing_candidates` 

呼出元 2件 [`00be2980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2980.md) [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) · 呼出先 4件 [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) [`00be9704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9704.md) [`00be99a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be99a4.md) [`00be9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9acc.md)

- 1. [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.243772000000007 / 5.243772000000007 · insufficient_independent_call_anchors
- 2. [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · スコア 76.218111 · 採用条件未達 · 順位差 -5.243772000000007 / -5.243772000000007 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · スコア 72.06278 · 採用条件未達 · 順位差 3.7144360000000063 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · スコア 52.907489 · 採用条件未達 · 順位差 -28.563877000000005 / -28.554394000000002 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · スコア 31.287459 · 採用条件未達 · 順位差 0.8434649999999984 / -50.174424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · スコア 29.282108 · 採用条件未達 · 順位差 -52.189258 / -52.179775 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · スコア 18.951363 · 採用条件未達 · 順位差 0.3543100000000017 / -62.51052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 6.453533 · 採用条件未達 · 順位差 -73.189324 / -75.00835000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.243772000000007,
        "reverse_margin": 5.243772000000007
      },
      "new": "00be2578",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9887892376681614,
          0.9887892376681614
        ],
        "cfg_coverage": [
          0.8445378151260504,
          0.8663793103448276
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.243772000000007,
        "reverse_margin": -5.243772000000007
      },
      "new": "00be5088",
      "score": 76.218111
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8677130044843049,
          0.8677130044843049
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
        "margin": 3.7144360000000063,
        "reverse_margin": -9.399102999999997
      },
      "new": "00be4970",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) FUN_00be37e8

`competing_candidates` 

呼出元 2件 [`00be37cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37cc.md) [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) · 呼出先 4件 [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) [`00bea4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea4a4.md) [`00bea764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea764.md) [`00bea88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea88c.md)

- 1. [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · スコア 81.471366 · 採用条件未達 · 順位差 3.902025000000009 / 3.902025000000009 · insufficient_independent_call_anchors
- 2. [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · スコア 77.569341 · 採用条件未達 · 順位差 -3.902025000000009 / -3.902025000000009 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) · スコア 57.675975 · 採用条件未達 · 順位差 -8.315214000000005 / -23.795391000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · スコア 29.282108 · 採用条件未達 · 順位差 -52.179775 / -52.189258 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · スコア 28.920058 · 採用条件未達 · 順位差 -2.3674009999999974 / -52.551308000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · スコア 27.0529 · 採用条件未達 · 順位差 -54.408983 / -54.418466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) · スコア 17.943418 · 採用条件未達 · 順位差 -1.0848729999999982 / -63.527948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9911894273127754,
          0.9911894273127754
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.902025000000009,
        "reverse_margin": 3.902025000000009
      },
      "new": "00be33c0",
      "score": 81.471366
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9823788546255506,
          0.9823788546255506
        ],
        "cfg_coverage": [
          0.9353448275862069,
          0.9313304721030042
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.902025000000009,
        "reverse_margin": -3.902025000000009
      },
      "new": "00be1e40",
      "score": 77.569341
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7180616740088106,
          0.7180616740088106
        ],
        "cfg_coverage": [
          0.7327586206896551,
          0.7296137339055794
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -8.315214000000005,
        "reverse_margin": -23.795391000000002
      },
      "new": "00be2c8c",
      "score": 57.675975
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) FUN_00be54b0

`competing_candidates` 

呼出元 2件 [`00be5490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5490.md) [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) · 呼出先 4件 [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) [`00bec00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec00c.md) [`00bec2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec2ac.md) [`00bec3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec3d4.md)

- 1. [`00be5088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5088.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.243772000000007 / 5.243772000000007 · insufficient_independent_call_anchors
- 2. [`00be2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2578.md) · スコア 76.218111 · 採用条件未達 · 順位差 -5.243772000000007 / -5.243772000000007 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · スコア 68.348344 · 採用条件未達 · 順位差 -3.7144360000000063 / -13.113539000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · スコア 29.053652 · 採用条件未達 · 順位差 -2.2338069999999988 / -52.408231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1e40.md) · スコア 28.566246 · 採用条件未達 · 順位差 -52.905120000000004 / -52.895637 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be33c0.md) · スコア 27.0529 · 採用条件未達 · 順位差 -54.418466 / -54.408983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · スコア 18.597053 · 採用条件未達 · 順位差 -0.3543100000000017 / -62.86483 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 6.339074 · 採用条件未達 · 順位差 -73.30378300000001 / -75.122809 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.243772000000007,
        "reverse_margin": 5.243772000000007
      },
      "new": "00be5088",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9887892376681614,
          0.9887892376681614
        ],
        "cfg_coverage": [
          0.8663793103448276,
          0.8445378151260504
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.243772000000007,
        "reverse_margin": -5.243772000000007
      },
      "new": "00be2578",
      "score": 76.218111
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8632286995515696,
          0.8632286995515696
        ],
        "cfg_coverage": [
          0.8491379310344828,
          0.8277310924369747
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.7144360000000063,
        "reverse_margin": -13.113539000000003
      },
      "new": "00be4970",
      "score": 68.348344
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b16a12e6a8ed4819bc17fd2f4c9b054f"></a>

### v16.0.1 [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) FUN_00be5bc8

`competing_candidates` 

呼出元 2件 [`00be5ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5ba8.md) [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) · 呼出先 4件 [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) [`00bec6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec6d0.md) [`00bec970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec970.md) [`00beca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00beca98.md)

- 1. [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.656903 / 5.656903 · insufficient_independent_call_anchors
- 2. [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · スコア 75.80498 · 採用条件未達 · 順位差 -5.656903 / -5.656903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · スコア 16.643068 · 採用条件未達 · 順位差 -1.8065069999999999 / -64.818815 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.656903,
        "reverse_margin": 5.656903
      },
      "new": "00be57a0",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9641255605381166,
          0.9641255605381166
        ],
        "cfg_coverage": [
          0.9094827586206896,
          0.8978723404255319
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.656903,
        "reverse_margin": -5.656903
      },
      "new": "00be65d0",
      "score": 75.80498
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8452914798206278,
          0.8452914798206278
        ],
        "cfg_coverage": [
          0.896551724137931,
          0.8851063829787233
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.042266999999995,
        "reverse_margin": -13.042266999999995
      },
      "new": "00be5eb8",
      "score": 68.419616
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) FUN_00be62e0

`competing_candidates` 

呼出元 2件 [`00be62c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62c0.md) [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) · 呼出先 4件 [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) [`00becd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00becd94.md) [`00bed034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed034.md) [`00bed15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed15c.md)

- 1. [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · スコア 81.461883 · 採用条件未達 · 順位差 2.0 / 2.0 · insufficient_independent_call_anchors
- 2. [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · スコア 79.461883 · 採用条件未達 · 順位差 -2.0 / -2.0 · insufficient_independent_call_anchors
- 3. [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · スコア 18.449575 · 採用条件未達 · 順位差 0.0 / -63.012308000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.0,
        "reverse_margin": 2.0
      },
      "new": "00be5eb8",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.0,
        "reverse_margin": -2.0
      },
      "new": "00be6ce8",
      "score": 79.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8677130044843049,
          0.8677130044843049
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
        "margin": -9.399102999999997,
        "reverse_margin": -9.399102999999997
      },
      "new": "00be65d0",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) FUN_00be69f8

`competing_candidates` 

呼出元 2件 [`00be69d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69d8.md) [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) · 呼出先 4件 [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) [`00bed458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed458.md) [`00bed6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed6f8.md) [`00bed820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed820.md)

- 1. [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.656903 / 5.656903 · insufficient_independent_call_anchors
- 2. [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · スコア 75.80498 · 採用条件未達 · 順位差 -5.656903 / -5.656903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · スコア 18.449575 · 採用条件未達 · 順位差 0.0 / -63.012308000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.656903,
        "reverse_margin": 5.656903
      },
      "new": "00be65d0",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9641255605381166,
          0.9641255605381166
        ],
        "cfg_coverage": [
          0.8978723404255319,
          0.9094827586206896
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.656903,
        "reverse_margin": -5.656903
      },
      "new": "00be57a0",
      "score": 75.80498
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8677130044843049,
          0.8677130044843049
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
        "margin": -9.399102999999997,
        "reverse_margin": -9.399102999999997
      },
      "new": "00be5eb8",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) FUN_00be7110

`competing_candidates` 

呼出元 2件 [`00be70f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be70f0.md) [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) · 呼出先 4件 [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) [`00bedb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bedb1c.md) [`00beddbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00beddbc.md) [`00bedee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bedee4.md)

- 1. [`00be6ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be6ce8.md) · スコア 81.461883 · 採用条件未達 · 順位差 2.0 / 2.0 · insufficient_independent_call_anchors
- 2. [`00be5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be5eb8.md) · スコア 79.461883 · 採用条件未達 · 順位差 -2.0 / -2.0 · insufficient_independent_call_anchors
- 3. [`00be65d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be6/00be65d0.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be57a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be5/00be57a0.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · スコア 18.449575 · 採用条件未達 · 順位差 0.0 / -63.012308000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 2.0,
        "reverse_margin": 2.0
      },
      "new": "00be6ce8",
      "score": 81.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9910313901345291,
          0.9910313901345291
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.0,
        "reverse_margin": -2.0
      },
      "new": "00be5eb8",
      "score": 79.461883
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8677130044843049,
          0.8677130044843049
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
        "margin": -9.399102999999997,
        "reverse_margin": -9.399102999999997
      },
      "new": "00be65d0",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9028.md) FUN_00be9028

`competing_candidates` 

呼出元 1件 [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) · 呼出先 1件 [`00be92e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be92e8.md)

- 1. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 51.758658 · 採用条件未達 · 順位差 -30.241342000000003 / -27.900433000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -30.295454999999997 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.938312000000003 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 44.545455 · 採用条件未達 · 順位差 -37.454545 / -35.11363600000001 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.437757000000005 / -49.453991 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cbc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / -75.10101 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9943181818181818,
          0.9943181818181818
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
      "new": "00be8c00",
      "score": 79.659091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9943181818181818,
          0.9943181818181818
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
      "new": "00bea07c",
      "score": 79.659091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6761363636363636,
          0.6761363636363636
        ],
        "cfg_coverage": [
          0.5595238095238095,
          0.5875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.241342000000003,
        "reverse_margin": -27.900433000000007
      },
      "new": "00be99a0",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d8e7b9b8cc878d8a8423ae1ceef6d1cc"></a>

### v16.0.1 [`00be92e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be92e8.md) FUN_00be92e8

`competing_candidates` 

呼出元 2件 [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) [`00be9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9028.md) · 呼出先 0件 

- 1. [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00be9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9c60.md) · スコア 54.054054 · 採用条件未達 · 順位差 0.0 / -25.945946 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) · スコア 45.135135 · 採用条件未達 · 順位差 0.0 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 0.681818 · 採用条件未達 · 順位差 -78.977273 / -79.318182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00be8ec0",
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
      "new": "00bea33c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5675675675675675,
          0.5675675675675675
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
        "margin": 0.0,
        "reverse_margin": -25.945946
      },
      "new": "00be9c60",
      "score": 54.054054
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9b9cbcc6a0ae2ab6f56b3ff67527e2bc"></a>

### v16.0.1 [`00be9410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9410.md) FUN_00be9410

`competing_candidates` 

呼出元 1件 [`00be2268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2268.md) · 呼出先 0件 

- 1. [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md) · スコア 80.0 · 採用条件未達 · 順位差 4.303351000000006 / 4.303351000000006 · insufficient_independent_call_anchors
- 2. [`00bea464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea464.md) · スコア 75.696649 · 採用条件未達 · 順位差 -4.303351000000006 / -4.303351000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be9d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9d88.md) · スコア 40.977526 · 採用条件未達 · 順位差 -2.1813610000000025 / -39.022474 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be96a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be96a4.md) · スコア 14.967358 · 採用条件未達 · 順位差 -65.032642 / -65.032642 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 9.911817 · 採用条件未達 · 順位差 -12.572832000000002 / -70.088183 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md) · スコア 7.545788 · 採用条件未達 · 順位差 -9.2277 / -72.454212 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 0.31746 · 採用条件未達 · 順位差 -79.341631 / -79.68254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 0.31746 · 採用条件未達 · 順位差 -79.32539700000001 / -79.68254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 4.303351000000006,
        "reverse_margin": 4.303351000000006
      },
      "new": "00be8fe8",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9735449735449735,
          0.9735449735449735
        ],
        "cfg_coverage": [
          0.8974358974358975,
          0.8641975308641975
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.303351000000006,
        "reverse_margin": -4.303351000000006
      },
      "new": "00bea464",
      "score": 75.696649
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5608465608465608,
          0.5608465608465608
        ],
        "cfg_coverage": [
          0.36633663366336633,
          0.4567901234567901
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -2.1813610000000025,
        "reverse_margin": -39.022474
      },
      "new": "00be9d88",
      "score": 40.977526
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be9704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9704.md) FUN_00be9704

`competing_candidates` 

呼出元 1件 [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) · 呼出先 1件 [`00be99a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be99a4.md)

- 1. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 79.642857 · 採用条件未達 · 順位差 3.2665500000000094 / 3.2665500000000094 · insufficient_independent_call_anchors
- 2. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 76.376307 · 採用条件未達 · 順位差 -3.2665500000000094 / -3.2665500000000094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 56.186371 · 採用条件未達 · 順位差 -25.813629 / -23.456486000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 33.907982 · 採用条件未達 · 順位差 -48.092018 / -45.73487500000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.453991 / -49.437757000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.453991 / -49.437757000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 18.754355 · 採用条件未達 · 順位差 -63.245644999999996 / -60.888502 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -67.202381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.2665500000000094,
        "reverse_margin": 3.2665500000000094
      },
      "new": "00be92dc",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9761904761904762,
          0.9761904761904762
        ],
        "cfg_coverage": [
          0.9125,
          0.8902439024390244
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.2665500000000094,
        "reverse_margin": -3.2665500000000094
      },
      "new": "00bebbe4",
      "score": 76.376307
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7678571428571429,
          0.7678571428571429
        ],
        "cfg_coverage": [
          0.5057471264367817,
          0.5365853658536586
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.813629,
        "reverse_margin": -23.456486000000005
      },
      "new": "00beb520",
      "score": 56.186371
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2ee468fcafe17662ae55fc915aace3f5"></a>

### v16.0.1 [`00be99a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be99a4.md) FUN_00be99a4

`competing_candidates` 

呼出元 2件 [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) [`00be9704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9704.md) · 呼出先 0件 

- 1. [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) · スコア 80.0 · 採用条件未達 · 順位差 19.836199999999998 / 19.836199999999998 · insufficient_independent_call_anchors
- 2. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 60.1638 · 採用条件未達 · 順位差 -19.836199999999998 / -19.836199999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) · スコア 49.63145 · 採用条件未達 · 順位差 -20.638819999999996 / -30.36855 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) · スコア 11.343161 · 採用条件未達 · 順位差 -33.791973999999996 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 0.714286 · 採用条件未達 · 順位差 -78.928571 / -79.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.836199999999998,
        "reverse_margin": 19.836199999999998
      },
      "new": "00be957c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8108108108108109,
          0.8108108108108109
        ],
        "cfg_coverage": [
          0.6129032258064516,
          0.5757575757575758
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.836199999999998,
        "reverse_margin": -19.836199999999998
      },
      "new": "00bebe84",
      "score": 60.1638
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6756756756756757,
          0.6756756756756757
        ],
        "cfg_coverage": [
          0.4838709677419355,
          0.45454545454545453
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -20.638819999999996,
        "reverse_margin": -30.36855
      },
      "new": "00beb7c0",
      "score": 49.63145
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00be9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9acc.md) FUN_00be9acc

`competing_candidates` 

呼出元 1件 [`00be29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be29a0.md) · 呼出先 0件 

- 1. [`00be96a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be96a4.md) · スコア 80.0 · 採用条件未達 · 順位差 2.6282719999999955 / 2.6282719999999955 · insufficient_independent_call_anchors
- 2. [`00bebfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebfac.md) · スコア 77.371728 · 採用条件未達 · 順位差 -2.6282719999999955 / -2.6282719999999955 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb8e8.md) · スコア 64.01178 · 採用条件未達 · 順位差 0.0 / -15.988219999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00beb224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb224.md) · スコア 33.150524 · 採用条件未達 · 順位差 -25.488219 / -46.849476 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md) · スコア 16.773488 · 採用条件未達 · 順位差 0.0 / -63.226512 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md) · スコア 14.967358 · 採用条件未達 · 順位差 -65.032642 / -65.032642 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 2.6282719999999955,
        "reverse_margin": 2.6282719999999955
      },
      "new": "00be96a4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9895287958115183,
          0.9895287958115183
        ],
        "cfg_coverage": [
          0.9230769230769231,
          0.9
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.6282719999999955,
        "reverse_margin": -2.6282719999999955
      },
      "new": "00bebfac",
      "score": 77.371728
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.837696335078534,
          0.837696335078534
        ],
        "cfg_coverage": [
          0.6875,
          0.6875
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
        "reverse_margin": -15.988219999999998
      },
      "new": "00beb8e8",
      "score": 64.01178
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c7897e6f328e83980c6798b75da16fcf"></a>

### v16.0.1 [`00be9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9dc8.md) FUN_00be9dc8

`competing_candidates` 

呼出元 1件 [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) · 呼出先 1件 [`00bea088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea088.md)

- 1. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 82.0 · 採用条件未達 · 順位差 30.241342000000003 / 30.241342000000003 · insufficient_independent_call_anchors
- 2. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 51.758658 · 採用条件未達 · 順位差 -27.900433000000007 / -30.241342000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 51.758658 · 採用条件未達 · 順位差 -27.900433000000007 / -30.241342000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 30.768398 · 採用条件未達 · 順位差 -51.231601999999995 / -51.231601999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 23.32419 · 採用条件未達 · 順位差 -58.67581 / -58.67581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 12.440476 · 採用条件未達 · 順位差 -67.202381 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cbc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / -77.441919 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 30.241342000000003,
        "reverse_margin": 30.241342000000003
      },
      "new": "00be99a0",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6761363636363636,
          0.6761363636363636
        ],
        "cfg_coverage": [
          0.5875,
          0.5595238095238095
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.900433000000007,
        "reverse_margin": -30.241342000000003
      },
      "new": "00be8c00",
      "score": 51.758658
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6761363636363636,
          0.6761363636363636
        ],
        "cfg_coverage": [
          0.5875,
          0.5595238095238095
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.900433000000007,
        "reverse_margin": -30.241342000000003
      },
      "new": "00bea07c",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bea4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea4a4.md) FUN_00bea4a4

`competing_candidates` 

呼出元 1件 [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) · 呼出先 1件 [`00bea764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea764.md)

- 1. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 51.758658 · 採用条件未達 · 順位差 -30.241342000000003 / -27.900433000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -30.295454999999997 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.938312000000003 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 44.545455 · 採用条件未達 · 順位差 -37.454545 / -35.11363600000001 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.437757000000005 / -49.453991 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cbc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md) · スコア 4.558081 · 採用条件未達 · 順位差 0.0 / -75.10101 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9943181818181818,
          0.9943181818181818
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
      "new": "00be8c00",
      "score": 79.659091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9943181818181818,
          0.9943181818181818
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
      "new": "00bea07c",
      "score": 79.659091
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6761363636363636,
          0.6761363636363636
        ],
        "cfg_coverage": [
          0.5595238095238095,
          0.5875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -30.241342000000003,
        "reverse_margin": -27.900433000000007
      },
      "new": "00be99a0",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-13e50b9098b78ec96700e009871186f3"></a>

### v16.0.1 [`00bea764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea764.md) FUN_00bea764

`competing_candidates` 

呼出元 2件 [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) [`00bea4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea4a4.md) · 呼出先 0件 

- 1. [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00be9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9c60.md) · スコア 54.054054 · 採用条件未達 · 順位差 0.0 / -25.945946 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) · スコア 45.135135 · 採用条件未達 · 順位差 0.0 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 0.681818 · 採用条件未達 · 順位差 -78.977273 / -79.318182 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea464.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00be8ec0",
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
      "new": "00bea33c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5675675675675675,
          0.5675675675675675
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
        "margin": 0.0,
        "reverse_margin": -25.945946
      },
      "new": "00be9c60",
      "score": 54.054054
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bcfae11d8380c3a90d7785a93874988d"></a>

### v16.0.1 [`00bea88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea88c.md) FUN_00bea88c

`competing_candidates` 

呼出元 1件 [`00be37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be37e8.md) · 呼出先 0件 

- 1. [`00bea464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea464.md) · スコア 80.0 · 採用条件未達 · 順位差 4.303351000000006 / 4.303351000000006 · insufficient_independent_call_anchors
- 2. [`00be8fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8fe8.md) · スコア 75.696649 · 採用条件未達 · 順位差 -4.303351000000006 / -4.303351000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be9d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9d88.md) · スコア 43.158887 · 採用条件未達 · 順位差 2.1813610000000025 / -36.841113 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 9.911817 · 採用条件未達 · 順位差 -12.572832000000002 / -70.088183 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md) · スコア 7.545788 · 採用条件未達 · 順位差 -9.2277 / -72.454212 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.659091 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 0.0 · 採用条件未達 · 順位差 -82.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 4.303351000000006,
        "reverse_margin": 4.303351000000006
      },
      "new": "00bea464",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9735449735449735,
          0.9735449735449735
        ],
        "cfg_coverage": [
          0.8641975308641975,
          0.8974358974358975
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -4.303351000000006,
        "reverse_margin": -4.303351000000006
      },
      "new": "00be8fe8",
      "score": 75.696649
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5873015873015873,
          0.5873015873015873
        ],
        "cfg_coverage": [
          0.39603960396039606,
          0.5128205128205128
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 2.1813610000000025,
        "reverse_margin": -36.841113
      },
      "new": "00be9d88",
      "score": 43.158887
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00beab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beab80.md) FUN_00beab80

`competing_candidates` 

呼出元 1件 [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) · 呼出先 1件 [`00beae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beae40.md)

- 1. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 82.0 · 採用条件未達 · 順位差 18.022727000000003 / 18.022727000000003 · insufficient_independent_call_anchors
- 2. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 63.977273 · 採用条件未達 · 順位差 -18.022727000000003 / -18.022727000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 44.545455 · 採用条件未達 · 順位差 -35.11363600000001 / -37.454545 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 44.545455 · 採用条件未達 · 順位差 -35.11363600000001 / -37.454545 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 30.768398 · 採用条件未達 · 順位差 -51.231601999999995 / -51.231601999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 28.112591 · 採用条件未達 · 順位差 -53.887409000000005 / -53.887409000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -82.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea464.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -82.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 18.022727000000003,
        "reverse_margin": 18.022727000000003
      },
      "new": "00bea758",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7329545454545454,
          0.7329545454545454
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
        "margin": -18.022727000000003,
        "reverse_margin": -18.022727000000003
      },
      "new": "00beae3c",
      "score": 63.977273
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4090909090909091,
          0.4090909090909091
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
        "margin": -35.11363600000001,
        "reverse_margin": -37.454545
      },
      "new": "00be8c00",
      "score": 44.545455
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00beb264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb264.md) FUN_00beb264

`competing_candidates` 

呼出元 1件 [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) · 呼出先 1件 [`00beb524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb524.md)

- 1. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 82.0 · 採用条件未達 · 順位差 18.022727000000003 / 18.022727000000003 · insufficient_independent_call_anchors
- 2. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 63.977273 · 採用条件未達 · 順位差 -18.022727000000003 / -18.022727000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 53.75 · 採用条件未達 · 順位差 -25.892857000000006 / -28.25 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -30.295454999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -30.295454999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 33.907982 · 採用条件未達 · 順位差 -45.73487500000001 / -48.092018 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 18.022727000000003,
        "reverse_margin": 18.022727000000003
      },
      "new": "00beae3c",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7329545454545454,
          0.7329545454545454
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
        "margin": -18.022727000000003,
        "reverse_margin": -18.022727000000003
      },
      "new": "00bea758",
      "score": 63.977273
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5892857142857143,
          0.5625
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
        "margin": -25.892857000000006,
        "reverse_margin": -28.25
      },
      "new": "00bebbe4",
      "score": 53.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00beb948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb948.md) FUN_00beb948

`competing_candidates` 

呼出元 1件 [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) · 呼出先 1件 [`00bebbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebbe8.md)

- 1. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 82.0 · 採用条件未達 · 順位差 23.133004999999997 / 23.133004999999997 · insufficient_independent_call_anchors
- 2. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 58.866995 · 採用条件未達 · 順位差 -20.775862000000004 / -23.133004999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 56.186371 · 採用条件未達 · 順位差 -23.456486000000005 / -25.813629 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) · スコア 28.112591 · 採用条件未達 · 順位差 -53.887409000000005 / -53.887409000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) · スコア 23.32419 · 採用条件未達 · 順位差 -58.67581 / -58.67581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 21.178161 · 採用条件未達 · 順位差 -60.821839 / -60.821839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · スコア 5.88047 · 採用条件未達 · 順位差 -66.18231 / -76.11953 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 23.133004999999997,
        "reverse_margin": 23.133004999999997
      },
      "new": "00beb520",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7857142857142857,
          0.7857142857142857
        ],
        "cfg_coverage": [
          0.6375,
          0.5862068965517241
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -20.775862000000004,
        "reverse_margin": -23.133004999999997
      },
      "new": "00bebbe4",
      "score": 58.866995
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7678571428571429,
          0.7678571428571429
        ],
        "cfg_coverage": [
          0.5365853658536586,
          0.5057471264367817
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.456486000000005,
        "reverse_margin": -25.813629
      },
      "new": "00be92dc",
      "score": 56.186371
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bec00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec00c.md) FUN_00bec00c

`competing_candidates` 

呼出元 1件 [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) · 呼出先 1件 [`00bec2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec2ac.md)

- 1. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 79.642857 · 採用条件未達 · 順位差 3.2665500000000094 / 3.2665500000000094 · insufficient_independent_call_anchors
- 2. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 76.376307 · 採用条件未達 · 順位差 -3.2665500000000094 / -3.2665500000000094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 58.866995 · 採用条件未達 · 順位差 -23.133004999999997 / -20.775862000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) · スコア 53.75 · 採用条件未達 · 順位差 -28.25 / -25.892857000000006 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8c00.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -27.938312000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea07c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -27.938312000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 38.571429 · 採用条件未達 · 順位差 -41.071428000000004 / -41.071428000000004 · instruction_coverage, insufficient_independent_call_anchors
- 8. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 21.450617 · 採用条件未達 · 順位差 -60.549383 / -58.192240000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 3.2665500000000094,
        "reverse_margin": 3.2665500000000094
      },
      "new": "00bebbe4",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9761904761904762,
          0.9761904761904762
        ],
        "cfg_coverage": [
          0.8902439024390244,
          0.9125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -3.2665500000000094,
        "reverse_margin": -3.2665500000000094
      },
      "new": "00be92dc",
      "score": 76.376307
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7857142857142857,
          0.7857142857142857
        ],
        "cfg_coverage": [
          0.5862068965517241,
          0.6375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.133004999999997,
        "reverse_margin": -20.775862000000004
      },
      "new": "00beb520",
      "score": 58.866995
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bec2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec2ac.md) FUN_00bec2ac

`competing_candidates` 

呼出元 2件 [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) [`00bec00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec00c.md) · 呼出先 0件 

- 1. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 80.0 · 採用条件未達 · 順位差 9.729730000000004 / 9.729730000000004 · insufficient_independent_call_anchors
- 2. [`00beb7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) · スコア 70.27027 · 採用条件未達 · 順位差 20.638819999999996 / -9.729730000000004 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be957c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be957c.md) · スコア 60.1638 · 採用条件未達 · 順位差 -19.836199999999998 / -19.836199999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00be8ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8ec0.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bea33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea33c.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) · スコア 45.135135 · 採用条件未達 · 順位差 0.0 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 24.054054 · 採用条件未達 · 順位差 -55.945946 / -55.945946 · instruction_coverage, insufficient_independent_call_anchors
- 8. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 0.714286 · 採用条件未達 · 順位差 -78.928571 / -79.285714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 9.729730000000004,
        "reverse_margin": 9.729730000000004
      },
      "new": "00bebe84",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8378378378378378,
          0.8378378378378378
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
        "margin": 20.638819999999996,
        "reverse_margin": -9.729730000000004
      },
      "new": "00beb7c0",
      "score": 70.27027
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8108108108108109,
          0.8108108108108109
        ],
        "cfg_coverage": [
          0.5757575757575758,
          0.6129032258064516
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.836199999999998,
        "reverse_margin": -19.836199999999998
      },
      "new": "00be957c",
      "score": 60.1638
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bec3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec3d4.md) FUN_00bec3d4

`competing_candidates` 

呼出元 1件 [`00be54b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be54b0.md) · 呼出先 0件 

- 1. [`00bebfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebfac.md) · スコア 80.0 · 採用条件未達 · 順位差 2.6282719999999955 / 2.6282719999999955 · insufficient_independent_call_anchors
- 2. [`00be96a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be96a4.md) · スコア 77.371728 · 採用条件未達 · 順位差 -2.6282719999999955 / -2.6282719999999955 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb8e8.md) · スコア 64.01178 · 採用条件未達 · 順位差 0.0 / -15.988219999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00beb224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb224.md) · スコア 58.638743 · 採用条件未達 · 順位差 25.488219 / -21.361257000000002 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 47.643979 · 採用条件未達 · 順位差 -32.356021 / -32.356021 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md) · スコア 16.773488 · 採用条件未達 · 順位差 0.0 / -63.226512 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 2.6282719999999955,
        "reverse_margin": 2.6282719999999955
      },
      "new": "00bebfac",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9895287958115183,
          0.9895287958115183
        ],
        "cfg_coverage": [
          0.9,
          0.9230769230769231
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.6282719999999955,
        "reverse_margin": -2.6282719999999955
      },
      "new": "00be96a4",
      "score": 77.371728
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.837696335078534,
          0.837696335078534
        ],
        "cfg_coverage": [
          0.6875,
          0.7051282051282052
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
        "reverse_margin": -15.988219999999998
      },
      "new": "00beb8e8",
      "score": 64.01178
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bec6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec6d0.md) FUN_00bec6d0

`competing_candidates` 

呼出元 1件 [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) · 呼出先 1件 [`00bec970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec970.md)

- 1. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 79.642857 · 採用条件未達 · 順位差 1.3447969999999998 / 1.3447969999999998 · insufficient_independent_call_anchors
- 2. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 78.29806 · 採用条件未達 · 順位差 -1.3447969999999998 / -1.3447969999999998 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 72.142857 · 採用条件未達 · 順位差 -7.5 / -7.5 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 38.571429 · 採用条件未達 · 順位差 -41.071428000000004 / -41.071428000000004 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.3447969999999998,
        "reverse_margin": 1.3447969999999998
      },
      "new": "00bec2a8",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9880952380952381,
          0.9880952380952381
        ],
        "cfg_coverage": [
          0.9506172839506173,
          0.9625
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.3447969999999998,
        "reverse_margin": -1.3447969999999998
      },
      "new": "00bed030",
      "score": 78.29806
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8690476190476191,
          0.8690476190476191
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
        "margin": -7.5,
        "reverse_margin": -7.5
      },
      "new": "00bec96c",
      "score": 72.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3b404cea414c06367a50ea4e90a73e76"></a>

### v16.0.1 [`00bec970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec970.md) FUN_00bec970

`competing_candidates` 

呼出元 2件 [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) [`00bec6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00bec6d0.md) · 呼出先 0件 

- 1. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebe84.md) · スコア 24.054054 · 採用条件未達 · 順位差 -55.945946 / -55.945946 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bebfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebfac.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bec548",
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
      "new": "00bed2d0",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6756756756756757,
          0.6756756756756757
        ],
        "cfg_coverage": [
          0.34285714285714286,
          0.3870967741935484
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.602317,
        "reverse_margin": -32.602317
      },
      "new": "00becc0c",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00beca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00beca98.md) FUN_00beca98

`competing_candidates` 

呼出元 1件 [`00be5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be5/00be5bc8.md) · 呼出先 0件 

- 1. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 80.0 · 採用条件未達 · 順位差 5.476051999999996 / 5.476051999999996 · insufficient_independent_call_anchors
- 2. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 74.523948 · 採用条件未達 · 順位差 -5.476051999999996 / -5.476051999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 58.058996 · 採用条件未達 · 順位差 -21.941004 / -21.941004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 55.434796 · 採用条件未達 · 順位差 -24.565204 / -24.565204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bebfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebfac.md) · スコア 47.643979 · 採用条件未達 · 順位差 -32.356021 / -32.356021 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 22.484649 · 採用条件未達 · 順位差 0.0 / -57.515350999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 5.476051999999996,
        "reverse_margin": 5.476051999999996
      },
      "new": "00bec670",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9581151832460733,
          0.9581151832460733
        ],
        "cfg_coverage": [
          0.8518518518518519,
          0.8846153846153846
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.476051999999996,
        "reverse_margin": -5.476051999999996
      },
      "new": "00bed3f8",
      "score": 74.523948
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7643979057591623,
          0.7643979057591623
        ],
        "cfg_coverage": [
          0.6097560975609756,
          0.6410256410256411
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.941004,
        "reverse_margin": -21.941004
      },
      "new": "00becd34",
      "score": 58.058996
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00becd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00becd94.md) FUN_00becd94

`competing_candidates` 

呼出元 1件 [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) · 呼出先 1件 [`00bed034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed034.md)

- 1. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 79.642857 · 採用条件未達 · 順位差 7.5 / 7.5 · insufficient_independent_call_anchors
- 2. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 72.142857 · 採用条件未達 · 順位差 -7.5 / -7.5 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 71.731092 · 採用条件未達 · 順位差 -7.911765000000003 / -7.911765000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 66.653439 · 採用条件未達 · 順位差 -12.989418 / -12.989418 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.685864 / -79.328721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 7.5,
        "reverse_margin": 7.5
      },
      "new": "00bec96c",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8690476190476191,
          0.8690476190476191
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
        "margin": -7.5,
        "reverse_margin": -7.5
      },
      "new": "00bec2a8",
      "score": 72.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9523809523809523,
          0.9523809523809523
        ],
        "cfg_coverage": [
          0.7294117647058823,
          0.775
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.911765000000003,
        "reverse_margin": -7.911765000000003
      },
      "new": "00bed6f4",
      "score": 71.731092
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0042f5c74b005635f51b9f43e17f3857"></a>

### v16.0.1 [`00bed034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed034.md) FUN_00bed034

`competing_candidates` 

呼出元 2件 [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) [`00becd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bec/00becd94.md) · 呼出先 0件 

- 1. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 80.0 · 採用条件未達 · 順位差 14.818533000000002 / 14.818533000000002 · insufficient_independent_call_anchors
- 2. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 65.181467 · 採用条件未達 · 順位差 -14.818533000000002 / -14.818533000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 14.818533000000002,
        "reverse_margin": 14.818533000000002
      },
      "new": "00becc0c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9054054054054054,
          0.9054054054054054
        ],
        "cfg_coverage": [
          0.59375,
          0.5428571428571428
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.818533000000002,
        "reverse_margin": -14.818533000000002
      },
      "new": "00bed994",
      "score": 65.181467
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6756756756756757,
          0.6756756756756757
        ],
        "cfg_coverage": [
          0.3870967741935484,
          0.34285714285714286
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.602317,
        "reverse_margin": -32.602317
      },
      "new": "00bec548",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bed15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed15c.md) FUN_00bed15c

`competing_candidates` 

呼出元 1件 [`00be62e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be62e0.md) · 呼出先 0件 

- 1. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 80.0 · 採用条件未達 · 順位差 19.791780000000003 / 19.791780000000003 · insufficient_independent_call_anchors
- 2. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 60.20822 · 採用条件未達 · 順位差 -19.791780000000003 / -19.791780000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 58.058996 · 採用条件未達 · 順位差 -21.941004 / -21.941004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 54.640531 · 採用条件未達 · 順位差 -25.359468999999997 / -25.359468999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 22.43647 · 採用条件未達 · 順位差 -0.04817900000000108 / -57.56353 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.328721 / -79.685864 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.328721 / -79.685864 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.791780000000003,
        "reverse_margin": 19.791780000000003
      },
      "new": "00becd34",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8272251308900523,
          0.8272251308900523
        ],
        "cfg_coverage": [
          0.5287356321839081,
          0.5609756097560976
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.791780000000003,
        "reverse_margin": -19.791780000000003
      },
      "new": "00bedabc",
      "score": 60.20822
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7643979057591623,
          0.7643979057591623
        ],
        "cfg_coverage": [
          0.6410256410256411,
          0.6097560975609756
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.941004,
        "reverse_margin": -21.941004
      },
      "new": "00bec670",
      "score": 58.058996
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c1fa21f7c114b55cf3db9a01ba6ddc40"></a>

### v16.0.1 [`00bed458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed458.md) FUN_00bed458

`competing_candidates` 

呼出元 1件 [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) · 呼出先 1件 [`00bed6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed6f8.md)

- 1. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 79.642857 · 採用条件未達 · 順位差 1.3447969999999998 / 1.3447969999999998 · insufficient_independent_call_anchors
- 2. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 78.29806 · 採用条件未達 · 順位差 -1.3447969999999998 / -1.3447969999999998 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 66.653439 · 採用条件未達 · 順位差 -12.989418 / -12.989418 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.685864 / -79.328721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.3447969999999998,
        "reverse_margin": 1.3447969999999998
      },
      "new": "00bed030",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9880952380952381,
          0.9880952380952381
        ],
        "cfg_coverage": [
          0.9625,
          0.9506172839506173
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.3447969999999998,
        "reverse_margin": -1.3447969999999998
      },
      "new": "00bec2a8",
      "score": 78.29806
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8392857142857143,
          0.8392857142857143
        ],
        "cfg_coverage": [
          0.825,
          0.8148148148148148
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.989418,
        "reverse_margin": -12.989418
      },
      "new": "00bec96c",
      "score": 66.653439
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0be79f4d8ec0bdb92e05de0656b14952"></a>

### v16.0.1 [`00bed6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed6f8.md) FUN_00bed6f8

`competing_candidates` 

呼出元 2件 [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) [`00bed458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed458.md) · 呼出先 0件 

- 1. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bec548",
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
      "new": "00bed2d0",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6756756756756757,
          0.6756756756756757
        ],
        "cfg_coverage": [
          0.34285714285714286,
          0.3870967741935484
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.602317,
        "reverse_margin": -32.602317
      },
      "new": "00becc0c",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bed820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bed820.md) FUN_00bed820

`competing_candidates` 

呼出元 1件 [`00be69f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be6/00be69f8.md) · 呼出先 0件 

- 1. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 80.0 · 採用条件未達 · 順位差 5.476051999999996 / 5.476051999999996 · insufficient_independent_call_anchors
- 2. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 74.523948 · 採用条件未達 · 順位差 -5.476051999999996 / -5.476051999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 54.640531 · 採用条件未達 · 順位差 -25.359468999999997 / -25.359468999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 53.741349 · 採用条件未達 · 順位差 -26.258651 / -26.258651 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 22.484649 · 採用条件未達 · 順位差 0.0 / -57.515350999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 5.476051999999996,
        "reverse_margin": 5.476051999999996
      },
      "new": "00bed3f8",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9581151832460733,
          0.9581151832460733
        ],
        "cfg_coverage": [
          0.8846153846153846,
          0.8518518518518519
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.476051999999996,
        "reverse_margin": -5.476051999999996
      },
      "new": "00bec670",
      "score": 74.523948
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7277486910994765,
          0.7277486910994765
        ],
        "cfg_coverage": [
          0.5487804878048781,
          0.5555555555555556
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -25.359468999999997,
        "reverse_margin": -25.359468999999997
      },
      "new": "00becd34",
      "score": 54.640531
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3193b6301107544bf77922ab0d2191d8"></a>

### v16.0.1 [`00bedb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bedb1c.md) FUN_00bedb1c

`competing_candidates` 

呼出元 1件 [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) · 呼出先 1件 [`00beddbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00beddbc.md)

- 1. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 79.642857 · 採用条件未達 · 順位差 7.911765000000003 / 7.911765000000003 · insufficient_independent_call_anchors
- 2. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 71.731092 · 採用条件未達 · 順位差 -7.911765000000003 / -7.911765000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) · スコア 18.659664 · 採用条件未達 · 順位差 -63.340336 / -60.98319300000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 9.147059 · 採用条件未達 · 順位差 -72.852941 / -70.49579800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.642857 / -79.28571400000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9940476190476191,
          0.9940476190476191
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 7.911765000000003,
        "reverse_margin": 7.911765000000003
      },
      "new": "00bed6f4",
      "score": 79.642857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9523809523809523,
          0.9523809523809523
        ],
        "cfg_coverage": [
          0.775,
          0.7294117647058823
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -7.911765000000003,
        "reverse_margin": -7.911765000000003
      },
      "new": "00bec96c",
      "score": 71.731092
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8035714285714286,
          0.8035714285714286
        ],
        "cfg_coverage": [
          0.5875,
          0.5529411764705883
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -20.36974800000001,
        "reverse_margin": -20.36974800000001
      },
      "new": "00bec2a8",
      "score": 59.273109
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-92ce3807030cf3a4aa6ece279acc2ee5"></a>

### v16.0.1 [`00beddbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00beddbc.md) FUN_00beddbc

`competing_candidates` 

呼出元 2件 [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) [`00bedb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bedb1c.md) · 呼出先 0件 

- 1. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 80.0 · 採用条件未達 · 順位差 14.818533000000002 / 14.818533000000002 · insufficient_independent_call_anchors
- 2. [`00becc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becc0c.md) · スコア 65.181467 · 採用条件未達 · 順位差 -14.818533000000002 / -14.818533000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec548.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed2d0.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.28571400000001 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 0.357143 · 採用条件未達 · 順位差 -81.642857 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 14.818533000000002,
        "reverse_margin": 14.818533000000002
      },
      "new": "00bed994",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9054054054054054,
          0.9054054054054054
        ],
        "cfg_coverage": [
          0.5428571428571428,
          0.59375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.818533000000002,
        "reverse_margin": -14.818533000000002
      },
      "new": "00becc0c",
      "score": 65.181467
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6486486486486487,
          0.6486486486486487
        ],
        "cfg_coverage": [
          0.41935483870967744,
          0.40625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -32.956081,
        "reverse_margin": -32.956081
      },
      "new": "00bec548",
      "score": 47.043919
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00bedee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bed/00bedee4.md) FUN_00bedee4

`competing_candidates` 

呼出元 1件 [`00be7110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7110.md) · 呼出先 0件 

- 1. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 80.0 · 採用条件未達 · 順位差 19.791780000000003 / 19.791780000000003 · insufficient_independent_call_anchors
- 2. [`00becd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00becd34.md) · スコア 60.20822 · 採用条件未達 · 順位差 -19.791780000000003 / -19.791780000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec670.md) · スコア 55.434796 · 採用条件未達 · 順位差 -24.565204 / -24.565204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed3f8.md) · スコア 53.741349 · 採用条件未達 · 順位差 -26.258651 / -26.258651 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md) · スコア 21.208401 · 採用条件未達 · 順位差 -1.2762480000000025 / -58.791599000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 0.0 · 採用条件未達 · 順位差 -82.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.791780000000003,
        "reverse_margin": 19.791780000000003
      },
      "new": "00bedabc",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8272251308900523,
          0.8272251308900523
        ],
        "cfg_coverage": [
          0.5609756097560976,
          0.5287356321839081
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.791780000000003,
        "reverse_margin": -19.791780000000003
      },
      "new": "00becd34",
      "score": 60.20822
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7591623036649214,
          0.7591623036649214
        ],
        "cfg_coverage": [
          0.5512820512820513,
          0.4942528735632184
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -24.565204,
        "reverse_margin": -24.565204
      },
      "new": "00bec670",
      "score": 55.434796
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-af7c6126195c090ce17ea6d87aabadd4"></a>

### v16.0.1 [`00bee1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee1e0.md) FUN_00bee1e0

`competing_candidates` 

呼出元 1件 [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) · 呼出先 1件 [`00bee480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee480.md)

- 1. [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) · スコア 82.0 · 採用条件未達 · 順位差 60.549383 / 60.549383 · insufficient_independent_call_anchors
- 2. [`00bebbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00bebbe4.md) · スコア 21.450617 · 採用条件未達 · 順位差 -58.192240000000005 / -60.549383 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) · スコア 21.178161 · 採用条件未達 · 順位差 -60.821839 / -60.821839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00be92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be92dc.md) · スコア 18.754355 · 採用条件未達 · 順位差 -60.888502 / -63.245644999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 9.147059 · 採用条件未達 · 順位差 -70.49579800000001 / -72.852941 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · スコア 6.072285 · 採用条件未達 · 順位差 -12.879078 / -75.927715 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bed994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed994.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.642857 / -81.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bedabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bedabc.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -82.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 60.549383,
        "reverse_margin": 60.549383
      },
      "new": "00beddb8",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.2916666666666667
        ],
        "cfg_coverage": [
          0.2,
          0.19753086419753085
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -58.192240000000005,
        "reverse_margin": -60.549383
      },
      "new": "00bebbe4",
      "score": 21.450617
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.2916666666666667
        ],
        "cfg_coverage": [
          0.1839080459770115,
          0.19753086419753085
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.821839,
        "reverse_margin": -60.821839
      },
      "new": "00beb520",
      "score": 21.178161
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4569a392212107ba6d1f2abe9f269041"></a>

### v16.0.1 [`00bee880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee880.md) FUN_00bee880

`competing_candidates` 

呼出元 1件 [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) · 呼出先 1件 [`00beeb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beeb20.md)

- 1. [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) · スコア 82.0 · 採用条件未達 · 順位差 60.644577999999996 / 60.644577999999996 · insufficient_independent_call_anchors
- 2. [`00bec2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec2a8.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bec/00bec96c.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bed030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed030.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00bed6f4.md) · スコア 18.659664 · 採用条件未達 · 順位差 -60.98319300000001 / -63.340336 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · スコア 6.206087 · 採用条件未達 · 順位差 -12.243488 / -75.793913 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 60.644577999999996,
        "reverse_margin": 60.644577999999996
      },
      "new": "00bee458",
      "score": 82.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.2916666666666667
        ],
        "cfg_coverage": [
          0.2,
          0.1927710843373494
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -58.287435,
        "reverse_margin": -60.644577999999996
      },
      "new": "00bec2a8",
      "score": 21.355422
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.2916666666666667
        ],
        "cfg_coverage": [
          0.2,
          0.1927710843373494
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -58.287435,
        "reverse_margin": -60.644577999999996
      },
      "new": "00bec96c",
      "score": 21.355422
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-50ceea9b480f0f737bee871ddc41451a"></a>

### v16.0.1 [`00bf8734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8734.md) FUN_00bf8734

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf830c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf830c.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bf830c",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0ab69aa360dde23ba2951b0bd3376971"></a>

### v16.0.1 [`00bf8744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8744.md) FUN_00bf8744

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf8610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

- 1. [`00bf831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf831c.md) · スコア 61.538462 · 採用条件未達 · 順位差 6.923076999999999 / 6.923076999999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf83e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83e4.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.184614999999994 / -6.923076999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bfaa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa50.md) · スコア 20.689655 · 採用条件未達 · 順位差 -42.758621000000005 / -40.84880700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00532930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532930.md) · スコア 11.538462 · 採用条件未達 · 順位差 -47.461538 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0074e2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074e/0074e2a4.md) · スコア 11.538462 · 採用条件未達 · 順位差 -47.461538 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bf831c",
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
      "new": "00bf83e4",
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
        "margin": -42.758621000000005,
        "reverse_margin": -40.84880700000001
      },
      "new": "00bfaa50",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-257f7f252d58d12f0790d8dea8e52ff4"></a>

### v16.0.1 [`00bf87fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87fc.md) FUN_00bf87fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf83d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83d4.md) · スコア 65.0 · 採用条件未達 · 順位差 31.666666999999997 / 31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf8448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8448.md) · スコア 33.333333 · 採用条件未達 · 順位差 -46.666667 / -31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bf83d4",
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
      "new": "00bf8448",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1c3cd56bc31b670af996ae83e40dbf79"></a>

### v16.0.1 [`00bf880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf880c.md) FUN_00bf880c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf8610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

- 1. [`00bf83e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83e4.md) · スコア 60.8 · 採用条件未達 · 順位差 6.184614999999994 / 6.184614999999994 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf831c.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.923076999999999 / -6.184614999999994 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bfaa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa50.md) · スコア 20.689655 · 採用条件未達 · 順位差 -42.758621000000005 / -40.110344999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bf8448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8448.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.8 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bf83e4",
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
      "new": "00bf831c",
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
        "margin": -42.758621000000005,
        "reverse_margin": -40.110344999999995
      },
      "new": "00bfaa50",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f35f6a3713dc9fe2d2bb51dbd02a834a"></a>

### v16.0.1 [`00bf8870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8870.md) FUN_00bf8870

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf8448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8448.md) · スコア 80.0 · 採用条件未達 · 順位差 46.666667 / 46.666667 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bf83d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83d4.md) · スコア 33.333333 · 採用条件未達 · 順位差 -31.666666999999997 / -46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bf8448",
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
      "new": "00bf83d4",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-042046fe701f464bc0eb43ae85829c72"></a>

### v16.0.1 [`00bf93c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf93c0.md) FUN_00bf93c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf8f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8f98.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bf8f98",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0735ba79912e6ba9d3e471fbc4528d5d"></a>

### v16.0.1 [`00bf93d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf93d0.md) FUN_00bf93d0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

- 1. [`00bf8fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8fa8.md) · スコア 48.484848 · 採用条件未達 · 順位差 43.222922 / 43.222922 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00522b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522b20.md) · スコア 5.261926 · 採用条件未達 · 順位差 5.261926 / -43.222922 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00abce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abce14.md) · スコア 3.588071 · 採用条件未達 · 順位差 -54.628145 / -44.896777 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · スコア 1.401869 · 採用条件未達 · 順位差 -4.766355000000001 / -47.082979 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -48.484848 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -48.484848 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47474747474747475,
          0.47474747474747475
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
        "margin": 43.222922,
        "reverse_margin": 43.222922
      },
      "new": "00bf8fa8",
      "score": 48.484848
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
        "reverse_margin": -43.222922
      },
      "new": "00522b20",
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
          0.017241379310344827,
          0.05263157894736842
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -54.628145,
        "reverse_margin": -44.896777
      },
      "new": "00abce14",
      "score": 3.588071
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-380cb4200cb56e7a6f253c6c4cd8a666"></a>

### v16.0.1 [`00bfae68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae68.md) FUN_00bfae68

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bfaa40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa40.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bfaa40",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-da708413c0c5c8028fba35991b2b77c8"></a>

### v16.0.1 [`00bfae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae78.md) FUN_00bfae78

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf8610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

- 1. [`00bfaa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa50.md) · スコア 63.448276 · 採用条件未達 · 順位差 42.758621000000005 / 42.758621000000005 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf831c.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.84880700000001 / -42.758621000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bf83e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83e4.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.110344999999995 / -42.758621000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7241379310344828,
          0.7241379310344828
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
        "margin": 42.758621000000005,
        "reverse_margin": 42.758621000000005
      },
      "new": "00bfaa50",
      "score": 63.448276
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
        "reverse_margin": -42.758621000000005
      },
      "new": "00bf831c",
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
        "reverse_margin": -42.758621000000005
      },
      "new": "00bf83e4",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cdfc6869ae1b715f49e1f8613325e174"></a>

### v16.0.1 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) FUN_00c06190

`competing_candidates` 

呼出元 1件 [`00c06778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06778.md) · 呼出先 11件 [`00c065dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c065dc.md) [`00c06684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06684.md) [`00c0683c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c0683c.md) [`00c06ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ed0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

- 1. [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · スコア 38.103896 · 採用条件未達 · 順位差 35.229645 / 8.233766 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00c06004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06004.md) · スコア 29.87013 · 採用条件未達 · 順位差 23.554341 / -8.233766 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bfd878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md) · スコア 4.155844 · 採用条件未達 · 順位差 4.155844 / -33.948052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c01ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md) · スコア 4.155844 · 採用条件未達 · 順位差 4.155844 / -33.948052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c360ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md) · スコア 4.155844 · 採用条件未達 · 順位差 4.155844 / -33.948052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c36240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md) · スコア 4.155844 · 採用条件未達 · 順位差 4.155844 / -33.948052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00c36388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md) · スコア 4.155844 · 採用条件未達 · 順位差 4.155844 / -33.948052 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00686a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00686/00686a38.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -38.103896 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3712574850299401,
          0.2683982683982684
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
        "margin": 35.229645,
        "reverse_margin": 8.233766
      },
      "new": "00c05d68",
      "score": 38.103896
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.59375,
          0.1645021645021645
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
        "margin": 23.554341,
        "reverse_margin": -8.233766
      },
      "new": "00c06004",
      "score": 29.87013
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13675213675213677,
          0.06926406926406926
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
        "margin": 4.155844,
        "reverse_margin": -33.948052
      },
      "new": "00bfd878",
      "score": 4.155844
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-88c23f74617357d53b810d3ecf5a3c23"></a>

### v16.0.1 [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) FUN_00c2cf94

`competing_candidates` 

呼出元 1件 [`00c2cf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md) · 呼出先 5件 [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) [`00c35d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35d10.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

- 1. [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) · スコア 59.801105 · 採用条件未達 · 順位差 55.982923 / 42.774215999999996 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) · スコア 17.026889 · 採用条件未達 · 順位差 -45.154928999999996 / -42.774215999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c2c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) · スコア 2.0 · 採用条件未達 · 順位差 0.0 / -57.801105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c2ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md) · スコア 2.0 · 採用条件未達 · 順位差 0.0 / -57.801105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c2db94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md) · スコア 2.0 · 採用条件未達 · 順位差 2.0 / -57.801105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c2dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md) · スコア 2.0 · 採用条件未達 · 順位差 -2.2105259999999998 / -57.801105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -59.801105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5966850828729282,
          0.5966850828729282
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 55.982923,
        "reverse_margin": 42.774215999999996
      },
      "new": "00c2cb6c",
      "score": 59.801105
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23636363636363636,
          0.430939226519337
        ],
        "cfg_coverage": [
          0.04225352112676056,
          0.08823529411764706
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -45.154928999999996,
        "reverse_margin": -42.774215999999996
      },
      "new": "00c2d600",
      "score": 17.026889
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -57.801105
      },
      "new": "00c2c6b4",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2488bb0254c0026b0d428c19e9aba2de"></a>

### v16.0.1 [`00c2da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2da28.md) FUN_00c2da28

`competing_candidates` 

呼出元 1件 [`00c2d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md) · 呼出先 5件 [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) [`00c35ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ed0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

- 1. [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) · スコア 62.181818 · 採用条件未達 · 順位差 45.154928999999996 / 58.363636 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) · スコア 3.818182 · 採用条件未達 · 順位差 -55.982923 / -58.363636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c2c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) · スコア 2.0 · 採用条件未達 · 順位差 0.0 / -60.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c2ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md) · スコア 2.0 · 採用条件未達 · 順位差 0.0 / -60.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -62.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6363636363636364,
          0.6363636363636364
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 45.154928999999996,
        "reverse_margin": 58.363636
      },
      "new": "00c2d600",
      "score": 62.181818
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
        "margin": -55.982923,
        "reverse_margin": -58.363636
      },
      "new": "00c2cb6c",
      "score": 3.818182
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 0.0,
        "reverse_margin": -60.181818
      },
      "new": "00c2c6b4",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-31862a83e86eaddc5453962892cfed84"></a>

### v16.0.1 [`00c3508c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3508c.md) FUN_00c3508c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d80.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34c64",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d80",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c70",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-318c4e1d6597df01ed8262ac04ac4950"></a>

### v16.0.1 [`00c35098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35098.md) FUN_00c35098

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34c70",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d8c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c64",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-34b95559eb4974ce0752c9dfc0f7725e"></a>

### v16.0.1 [`00c350a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350a4.md) FUN_00c350a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34c7c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d98",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c64",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6ba562f6063e1d0f766f6ccf99451541"></a>

### v16.0.1 [`00c350b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350b0.md) FUN_00c350b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34c88",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34da4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c64",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8472da9fc25d19dea2e70fd1988f1e7f"></a>

### v16.0.1 [`00c350bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350bc.md) FUN_00c350bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34c94",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34db0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c70",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e9b9709abf08bf4a579f8f80c79ee794"></a>

### v16.0.1 [`00c350c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350c8.md) FUN_00c350c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34ca0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dbc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c7c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1a93edbac7974ea90f3133efd5985a39"></a>

### v16.0.1 [`00c350d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350d4.md) FUN_00c350d4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dc8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c88",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-479bb4e15fe1820516026c9fa9e30d7e"></a>

### v16.0.1 [`00c350e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350e0.md) FUN_00c350e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cb8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dd4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c94",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d3572262ce2266b293f5679e2985d248"></a>

### v16.0.1 [`00c350ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350ec.md) FUN_00c350ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cc4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34de0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34ca0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4e072c52019b6f9aa2ef6e25c2ddf6f4"></a>

### v16.0.1 [`00c350f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c350f8.md) FUN_00c350f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cd0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dec",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cac",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1b082241ef47ac50f5227ffb089a8d30"></a>

### v16.0.1 [`00c35104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35104.md) FUN_00c35104

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d00.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cdc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34df8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cb8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9b3af74a68852684b326356ad942884b"></a>

### v16.0.1 [`00c35110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35110.md) FUN_00c35110

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d00.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34ce8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34e04",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cc4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d0b0a574bc18b90913a9aa28e229ca08"></a>

### v16.0.1 [`00c3511c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3511c.md) FUN_00c3511c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d00.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34cf4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34e10",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cd0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d8ef5f3306e900d7cb47d797fb94d0b9"></a>

### v16.0.1 [`00c35128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35128.md) FUN_00c35128

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d00.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34d00",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34e1c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cdc",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b364666afa55cdc911e83e41c5d715f3"></a>

### v16.0.1 [`00c351a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351a8.md) FUN_00c351a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d80.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c64.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34d80",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c64",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d8c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1c3ce286437d4dac5f80b86594ae9175"></a>

### v16.0.1 [`00c351b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351b4.md) FUN_00c351b4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c70.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d80.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34d8c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c70",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d80",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0e887693a6c8dd805e1cbf7d4cb51f8a"></a>

### v16.0.1 [`00c351c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351c0.md) FUN_00c351c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c7c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d80.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34d98",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c7c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d80",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-00d3143979eb9aaed32df04fbaa6f000"></a>

### v16.0.1 [`00c351cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351cc.md) FUN_00c351cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c88.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d80.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34da4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c88",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d80",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c78eb58cb812211ce45b8c7fa8b21e8f"></a>

### v16.0.1 [`00c351d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351d8.md) FUN_00c351d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34c94.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34db0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34c94",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d8c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d1008b593dc5fdec292abacee403073b"></a>

### v16.0.1 [`00c351e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351e4.md) FUN_00c351e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ca0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d98.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34dbc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34ca0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d98",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-15db8617f86f2f38f0f3b43086efcc2f"></a>

### v16.0.1 [`00c351f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351f0.md) FUN_00c351f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cac.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34da4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34dc8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cac",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34da4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4ebfe70b1fe190d18349d2179ea02c73"></a>

### v16.0.1 [`00c351fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c351fc.md) FUN_00c351fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cb8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34db0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34dd4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cb8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34db0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-69ee9c421345d30a4c167ecaaf6cbb5e"></a>

### v16.0.1 [`00c35208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35208.md) FUN_00c35208

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cc4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dbc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34de0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cc4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dbc",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c0d0b37f1f4e8519c2f2c83e3eb8bdd8"></a>

### v16.0.1 [`00c35214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35214.md) FUN_00c35214

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cd0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dc8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34dec",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cd0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dc8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a7ba22d89263f74c0db5b472f53f110e"></a>

### v16.0.1 [`00c35220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35220.md) FUN_00c35220

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cdc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dd4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c34e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e1c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34df8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cdc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dd4",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cfd3c0f2df709693eaf9e092605facb5"></a>

### v16.0.1 [`00c3522c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3522c.md) FUN_00c3522c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34ce8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34de0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c34e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e1c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34e04",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34ce8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34de0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c5f8e055b055736b96e0b7df6353418f"></a>

### v16.0.1 [`00c35238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35238.md) FUN_00c35238

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34cf4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34dec.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c34e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e1c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34e10",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34cf4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34dec",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c65e593460a41fc80a60c70f9d284aef"></a>

### v16.0.1 [`00c35244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35244.md) FUN_00c35244

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c34e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e1c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c34d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d00.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c34df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34df8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c34e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e04.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c34e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34e10.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c34e1c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34d00",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c34df8",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ba6a8545cf76853e56945a08aa94ab40"></a>

### v16.0.1 [`00c35d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35d10.md) FUN_00c35d10

`competing_candidates` 

呼出元 1件 [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

- 1. [`00c35778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md) · スコア 70.869565 · 採用条件未達 · 順位差 70.869565 / 0.0 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c358e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c358e8.md) · スコア 70.869565 · 採用条件未達 · 順位差 0.652173999999988 / 0.0 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`00849e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849e40.md) · スコア 8.478261 · 採用条件未達 · 順位差 8.478261 / -62.39130399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00849efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849efc.md) · スコア 8.478261 · 採用条件未達 · 順位差 8.478261 / -62.39130399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0087dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md) · スコア 8.478261 · 採用条件未達 · 順位差 8.478261 / -62.39130399999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8478260869565217,
          0.8478260869565217
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
        "margin": 70.869565,
        "reverse_margin": 0.0
      },
      "new": "00c35778",
      "score": 70.869565
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8478260869565217,
          0.8478260869565217
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
        "margin": 0.652173999999988,
        "reverse_margin": 0.0
      },
      "new": "00c358e8",
      "score": 70.869565
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2765957446808511,
          0.14130434782608695
        ],
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
        "margin": 8.478261,
        "reverse_margin": -62.39130399999999
      },
      "new": "00849e40",
      "score": 8.478261
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b1f53d2fa3091bb4f7a22b319216540c"></a>

### v16.0.1 [`00c37b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b24.md) FUN_00c37b24

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c376fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c376fc.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00c376fc",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aa269947e37db15800fe312f53d2281b"></a>

### v16.0.1 [`00c38118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38118.md) FUN_00c38118

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf0.md) · スコア 29.3846 · 採用条件未達 · 順位差 25.3846 / 25.3846 · 
- 2. [`00c37cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c37d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d00.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 25.3846,
        "reverse_margin": 25.3846
      },
      "new": "00c37cf0",
      "score": 29.3846
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37cf8",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37d00",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a104dcd922afc19ab9277cb4c6e04751"></a>

### v16.0.1 [`00c38120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38120.md) FUN_00c38120

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf8.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c37d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d00.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c37cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c37cf8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37d00",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37cf0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1d28ea29f04e52a4c9f5c8072ce8b5b1"></a>

### v16.0.1 [`00c38128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38128.md) FUN_00c38128

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d00.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c37cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c37cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37cf0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c37d00",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37cf8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37cf0",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-469a4ee809663c87d2fcac7cbc135ca7"></a>

### v16.0.1 [`00c382e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c382e8.md) FUN_00c382e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ec0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c37ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ef0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c37ec0",
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
        "margin": -80.0,
        "reverse_margin": -80.0
      },
      "new": "00c37ef0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-41bd5ae6b90e6dfc72b2fdce19b139c0"></a>

### v16.0.1 [`00c38300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38300.md) FUN_00c38300

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ed8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c37ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ee4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c37ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ec0.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c37ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ef0.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c37ed8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37ee4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37ec0",
      "score": 2.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4475b9044cf6dee2dbf243510c6b01cc"></a>

### v16.0.1 [`00c3830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3830c.md) FUN_00c3830c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ee4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c37ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ed8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c37ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ec0.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c37ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ef0.md) · スコア 2.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c37ee4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37ed8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c37ec0",
      "score": 2.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-767ad92e3e0c02a61a62178efb33c3a4"></a>

### v16.0.1 [`00c38318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38318.md) FUN_00c38318

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c37ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ef0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c37ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ec0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c37ef0",
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
        "reverse_margin": -80.0
      },
      "new": "00c37ec0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-10c83977233f60844a126b5c6ea90f91"></a>

### v16.0.1 [`00c39604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39604.md) FUN_00c39604

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

- 1. [`00c391dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c391dc.md) · スコア 79.574468 · 採用条件未達 · 順位差 74.042553 / 74.042553 · insufficient_independent_call_anchors
- 2. [`005e0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md) · スコア 5.531915 · 採用条件未達 · 順位差 -0.023641000000000467 / -74.042553 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005f1ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1ca4.md) · スコア 5.531915 · 採用条件未達 · 順位差 5.531915 / -74.042553 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00629b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b48.md) · スコア 5.531915 · 採用条件未達 · 順位差 0.8747720000000001 / -74.042553 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) · スコア 5.106383 · 採用条件未達 · 順位差 5.106383 / -74.468085 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) · スコア 5.106383 · 採用条件未達 · 順位差 5.106383 / -74.468085 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00c1cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md) · スコア 4.948454 · 採用条件未達 · 順位差 4.948454 / -74.626014 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00c0e390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e390.md) · スコア 4.675325 · 採用条件未達 · 順位差 4.675325 / -74.899143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9929078014184397,
          0.9929078014184397
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 74.042553,
        "reverse_margin": 74.042553
      },
      "new": "00c391dc",
      "score": 79.574468
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12037037037037036,
          0.09219858156028368
        ],
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
        "margin": -0.023641000000000467,
        "reverse_margin": -74.042553
      },
      "new": "005e0960",
      "score": 5.531915
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20967741935483872,
          0.09219858156028368
        ],
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
        "margin": 5.531915,
        "reverse_margin": -74.042553
      },
      "new": "005f1ca4",
      "score": 5.531915
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-71779587129c0f940d748473ddfb545b"></a>

### v16.0.1 [`00c3dd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd04.md) FUN_00c3dd04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8dc.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8e8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d900.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c3d8dc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8e8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8f4",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5a5b43f34c125fe05cba52411b0a3ef6"></a>

### v16.0.1 [`00c3dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd10.md) FUN_00c3dd10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8e8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8dc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d900.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c3d8e8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8dc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8f4",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5ab1f04a177f12dbdd04f5ab16946a58"></a>

### v16.0.1 [`00c3dd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd1c.md) FUN_00c3dd1c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8f4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8dc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8e8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d900.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c3d8f4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8dc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8e8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-63618eed339c66bf32058ead9bc46e0c"></a>

### v16.0.1 [`00c3dd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd28.md) FUN_00c3dd28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d900.md) · スコア 69.0 · 採用条件未達 · 順位差 66.3333 / 66.3333 · 
- 2. [`00c3d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8dc.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3d8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8e8.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d8f4.md) · スコア 2.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 66.3333,
        "reverse_margin": 66.3333
      },
      "new": "00c3d900",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8dc",
      "score": 2.6667
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3d8e8",
      "score": 2.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a876fe28859c6247794391d07ff83023"></a>

### v16.0.1 [`00c3de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de10.md) FUN_00c3de10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d9e8.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 67.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 67.0,
        "reverse_margin": 67.0
      },
      "new": "00c3d9e8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e0d8762d373b9324ebadd5e5eb47f813"></a>

### v16.0.1 [`00c3de18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de18.md) FUN_00c3de18

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d9f0.md) · スコア 80.0 · 採用条件未達 · 順位差 45.0 / 45.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0056bf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bf38.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0056bf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bf48.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0056bf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bf88.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0057adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057adf0.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0057ae04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae04.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 45.0,
        "reverse_margin": 45.0
      },
      "new": "00c3d9f0",
      "score": 80.0
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -45.0,
        "reverse_margin": -45.0
      },
      "new": "0056bf38",
      "score": 35.0
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -45.0,
        "reverse_margin": -45.0
      },
      "new": "0056bf48",
      "score": 35.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-084c375474f030085e87e1dcd163e00b"></a>

### v16.0.1 [`00c3e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e310.md) FUN_00c3e310

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3dee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3dee8.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c3dee8",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

