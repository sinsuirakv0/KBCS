# v15.7.4 → v16.0.0 · 追加調査 (180)

[一覧の目次](README.md)

<a id="review-3a426eb94c1e2522c5d4717bd5ecbbc3"></a>

### v16.0.0 [`00c5e460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e460.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1EPKcm

`competing_candidates` 

呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c27e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27e84.md)

- 1. [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee70.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e70.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1870.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be1860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1860.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1880.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1890.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdce70",
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
      "new": "00bdee70",
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
      "new": "00be0e70",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ee253020e3cbd6780d656e2e1e3cbeff"></a>

### v16.0.0 [`00c5e470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e470.md) _ZNSt6__ndk115numpunct_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

`competing_candidates` 

呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c2c0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md)

- 1. [`00bdce80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce80.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00be0e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e80.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1880.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be1860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1860.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be1870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1870.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1890.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdce80",
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
      "new": "00be0e80",
      "score": 80.0
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.0,
        "reverse_margin": -13.0
      },
      "new": "00be1880",
      "score": 67.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f00d13bc22d72e3009ba7b563d5bbcc9"></a>

### v16.0.0 [`00c5e480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e480.md) _ZNSt6__ndk115numpunct_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

`competing_candidates` 

呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c2c408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md)

- 1. [`00bdce90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdee90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0e90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1890.md) · スコア 37.0 · 採用条件未達 · 順位差 -43.0 / -43.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be1860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1860.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1870.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1880.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdce90",
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
      "new": "00bdee90",
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
      "new": "00be0e90",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-371433b45712b6874addb3a74cc73641"></a>

### v16.0.0 [`00c5e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4b0.md) _ZNSt6__ndk110__time_putC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

`competing_candidates` 

呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c32514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md)

- 1. [`00bdcec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcec0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdeec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeec0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ec0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be18c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18c0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdcec0",
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
      "new": "00bdeec0",
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
      "new": "00be0ec0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7d63b742f02af09195d45b136619405e"></a>

### v16.0.0 [`00c5e510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e510.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c253f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c253f8.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdef20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1920.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be1740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1740.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be17b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17b0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdcf20",
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
      "new": "00bdef20",
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
      "new": "00be0f20",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-af6bf7609cc82f61052a482a02998e71"></a>

### v16.0.0 [`00c5e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e520.md) _ZNSt6__ndk114collate_bynameIcED2Ev

`competing_candidates` 

呼出元 1件 [`00c25678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25678.md) · 呼出先 1件 [`00c25634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25634.md)

- 1. [`00bdcf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf30.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdef30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef30.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f30.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1940.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdcf30",
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
      "new": "00bdef30",
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
      "new": "00be0f30",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ed85ff58767f4939a61ac4fa30567794"></a>

### v16.0.0 [`00c5e550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e550.md) _ZNSt6__ndk114collate_bynameIwED2Ev

`competing_candidates` 

呼出元 1件 [`00c25c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c58.md) · 呼出先 1件 [`00c25c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c14.md)

- 1. [`00bdef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef60.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00be0f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f60.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1970.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdef60",
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
      "new": "00be0f60",
      "score": 80.0
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
          "instruction_coverage"
        ],
        "margin": -11.0,
        "reverse_margin": -11.0
      },
      "new": "00be1970",
      "score": 69.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-58283534ab3297d3e3fb9db213e2138a"></a>

### v16.0.0 [`00c5e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e580.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c260d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260d0.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdcf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f90.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be19a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19a0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be1740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1740.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be17b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17b0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdcf90",
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
      "new": "00bdef90",
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
      "new": "00be0f90",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3829a1b7c3ca44c126e565612a26ac80"></a>

### v16.0.0 [`00c5e5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5a0.md) _ZNSt6__ndk15ctypeIcED1Ev

`competing_candidates` 

呼出元 2件 [`00c26d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md) [`00c26e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26e58.md) · 呼出先 1件 [`00c26818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26818.md)

- 1. [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) · スコア 84.0 · 採用条件未達 · 順位差 4.0 / 4.0 · short_function_requires_other_identity_evidence, already_matched_elsewhere
- 2. [`00bdcfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfb0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / -4.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdefb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefb0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / -4.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be19c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19c0.md) · スコア 71.0 · 採用条件未達 · 順位差 -9.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) · スコア 69.0 · 採用条件未達 · 順位差 -6.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, already_matched_elsewhere
- 6. [`00be19d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19d0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -17.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
          "already_matched_elsewhere"
        ],
        "margin": 4.0,
        "reverse_margin": 4.0
      },
      "new": "00be0fb0",
      "score": 84.0
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
        "reverse_margin": -4.0
      },
      "new": "00bdcfb0",
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
        "reverse_margin": -4.0
      },
      "new": "00bdefb0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a56233f625ce8839097fef8ac4b59dcd"></a>

### v16.0.0 [`00c5e5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5b0.md) _ZNSt6__ndk15ctypeIcED1Ev

`competing_candidates` 

呼出元 1件 [`00c2686c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2686c.md) · 呼出先 1件 [`00c26818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26818.md)

- 1. [`00bdcfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfc0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fc0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00be19d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19d0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be19c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19c0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdcfc0",
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
      "new": "00bdefc0",
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
        "reverse_margin": 0.0
      },
      "new": "00be0fc0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-411ab8e41f9092a212e2e889246b49bb"></a>

### v16.0.0 [`00c5e5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5e0.md) _ZNSt6__ndk112ctype_bynameIcED2Ev

`competing_candidates` 

呼出元 1件 [`00c26f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26f2c.md) · 呼出先 1件 [`00c31618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md)

- 1. [`00bdcff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcff0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdeff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ff0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a00.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be1d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d30.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdcff0",
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
      "new": "00bdeff0",
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
      "new": "00be0ff0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8c8c70c66dc5d67aca5bae2b800c7829"></a>

### v16.0.0 [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 6件 [`00c272e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md) [`00c273c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md) [`00c31960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31960.md) [`00c31c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c1c.md) [`00c31c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd010.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md) · スコア 75.0 · 採用条件未達 · 順位差 -5.0 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) · スコア 71.0 · 採用条件未達 · 順位差 -9.0 / -9.0 · short_function_requires_other_identity_evidence, instruction_coverage, already_matched_elsewhere
- 7. [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage, already_matched_elsewhere
- 8. [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) · スコア 69.0 · 採用条件未達 · 順位差 -15.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage, already_matched_elsewhere

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb010",
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
      "new": "00bdd010",
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
      "new": "00bdf010",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c98d9407b1e52e494e541af5eeab3b3d"></a>

### v16.0.0 [`00c5e610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e610.md) _ZNSt6__ndk112ctype_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

`competing_candidates` 

呼出元 1件 [`00c31c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md) · 呼出先 1件 [`00c273c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md)

- 1. [`00bdd020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd020.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdf020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf020.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1020.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a30.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdd020",
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
      "new": "00bdf020",
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
      "new": "00be1020",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-016eaf8df740d93ef15ac36f397d8f17"></a>

### v16.0.0 [`00c5e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e700.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c27d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27d3c.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd110.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf110.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00be1110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1110.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b20.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb110",
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
      "new": "00bdd110",
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
        "reverse_margin": 0.0
      },
      "new": "00bdf110",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4aa657ab1d68ec8fe4cf98c305816749"></a>

### v16.0.0 [`00c5e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e790.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c28820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28820.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00be1bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bb0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb1a0",
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
      "new": "00bdd1a0",
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
      "new": "00bdf1a0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-599195315e4d17223a5fa7f2fdec8fa9"></a>

### v16.0.0 [`00c5e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7a0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c2905c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c2905c.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00be1bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bc0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb1b0",
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
      "new": "00bdd1b0",
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
      "new": "00bdf1b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ec893d767d102aa1ee81727f1fb0962a"></a>

### v16.0.0 [`00c5e7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7b0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c291a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c291a8.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1c0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1c0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bd0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb1c0",
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
      "new": "00bdd1c0",
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
      "new": "00bdf1c0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fbef5350bf1b12eaf7f5ee48fcd8aa10"></a>

### v16.0.0 [`00c5e7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7c0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c29964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29964.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1be0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb1d0",
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
      "new": "00bdd1d0",
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
      "new": "00bdf1d0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a20152f48a47e4b50a448df6abf20042"></a>

### v16.0.0 [`00c5e7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7d0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c2b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b994.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bf0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb1e0",
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
      "new": "00bdd1e0",
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
      "new": "00bdf1e0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3fda6ac882565980c86bfe9f352cb7fa"></a>

### v16.0.0 [`00c5e7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7e0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c2b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9c0.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be11f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11f0.md) · スコア 80.0 · 採用条件未達 · 順位差 11.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c00.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb1f0",
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
      "new": "00bdd1f0",
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
      "new": "00bdf1f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5882993bf27897c8abac871ad4c5985b"></a>

### v16.0.0 [`00c5e7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7f0.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c2b9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9ec.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) · スコア 80.0 · 採用条件未達 · 順位差 9.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf200.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1200.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c10.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 9.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb200",
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
      "new": "00bdd200",
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
      "new": "00bdf200",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-14c75afc1bf58be26d9866081e831678"></a>

### v16.0.0 [`00c5e800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e800.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED1Ev

`competing_candidates` 

呼出元 1件 [`00c2ba18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba18.md) · 呼出先 1件 [`00c3544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3544c.md)

- 1. [`00bdb210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb210.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf210.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1210.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00be1c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c20.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb210",
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
      "new": "00bdd210",
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
      "new": "00bdf210",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d1704ec2e6e80aa4381813a5885f5afa"></a>

### v16.0.0 [`00c5e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e810.md) _ZNSt6__ndk115numpunct_bynameIcED1Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c2baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baa0.md)

- 1. [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c90.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb220",
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
      "new": "00bdd220",
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
      "new": "00bdf220",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f97927434fb1316dd3f9e26ba7783087"></a>

### v16.0.0 [`00c5e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e820.md) _ZNSt6__ndk115numpunct_bynameIcED1Ev

`competing_candidates` 

呼出元 1件 [`00c2baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baf0.md) · 呼出先 1件 [`00c2baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baa0.md)

- 1. [`00bdb230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb230.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd230.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf230.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1230.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c90.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb230",
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
      "new": "00bdd230",
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
      "new": "00bdf230",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1f5434e3aca976ff1212b82287f58764"></a>

### v16.0.0 [`00c5e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e830.md) _ZNSt6__ndk115numpunct_bynameIwED2Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c2bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb1c.md)

- 1. [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf240.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1240.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c60.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cb0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb240",
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
      "new": "00bdd240",
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
      "new": "00bdf240",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-caf623c1ba9031955522f88f2ac0afaf"></a>

### v16.0.0 [`00c5e840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e840.md) _ZNSt6__ndk115numpunct_bynameIwED2Ev

`competing_candidates` 

呼出元 1件 [`00c2bb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb6c.md) · 呼出先 1件 [`00c2bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb1c.md)

- 1. [`00bdb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb250.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1250.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c60.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cb0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb250",
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
      "new": "00bdd250",
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
      "new": "00be1250",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9c6a8be790e17e2a2576f2e36ffa8b60"></a>

### v16.0.0 [`00c5e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e870.md) _ZNSt6__ndk115numpunct_bynameIcED1Ev

`competing_candidates` 

呼出元 1件 [`00c2c144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c144.md) · 呼出先 1件 [`00c2baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baa0.md)

- 1. [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bdd280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd280.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf280.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00be1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1280.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c90.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00be1c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c30.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb280",
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
      "new": "00bdd280",
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
        "reverse_margin": 0.0
      },
      "new": "00bdf280",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2b4a5c97e36679317a3bd994e5dd8103"></a>

### v16.0.0 [`00c5e890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e890.md) _ZNSt6__ndk115numpunct_bynameIwED2Ev

`competing_candidates` 

呼出元 1件 [`00c2c47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c47c.md) · 呼出先 1件 [`00c2bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb1c.md)

- 1. [`00bdf2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00be12a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cb0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 4. [`00be1c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c50.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c60.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdf2a0",
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
      "new": "00be12a0",
      "score": 80.0
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
          "instruction_coverage"
        ],
        "margin": -11.0,
        "reverse_margin": -11.0
      },
      "new": "00be1cb0",
      "score": 69.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-40d0975efa2954f2810ef0f9da90f468"></a>

### v16.0.0 [`00c5e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8c0.md) _ZNSt6__ndk110__time_getD2Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c2e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e358.md)

- 1. [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdf2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ce0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb2d0",
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
      "new": "00bdf2d0",
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
      "new": "00be12d0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8f6702d241124de49bc491119a5b4a98"></a>

### v16.0.0 [`00c5e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e910.md) _ZNSt6__ndk112ctype_bynameIcED2Ev

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c31618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md)

- 1. [`00bdb320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb320.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdf320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf320.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a00.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be1d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d30.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb320",
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
      "new": "00bdf320",
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
      "new": "00be1320",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6bfdbffcd7948cf547a7bd74d5763efe"></a>

### v16.0.0 [`00c5e970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e970.md) _ZNSt10bad_typeidC1Ev

`competing_candidates` 

呼出元 1件 [`00c370d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md) · 呼出先 1件 [`00c37b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b88.md)

- 1. [`00bdb380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb380.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd380.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf380.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1380.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1db0.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb380",
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
      "new": "00bdd380",
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
      "new": "00bdf380",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-12cb206f2b26ec9087d98dc41dcd530e"></a>

### v16.0.0 [`00c5ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea20.md) _ZNSt12out_of_rangeD1Ev

`competing_candidates` 

呼出元 1件 [`00c378fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378fc.md) · 呼出先 1件 [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md)

- 1. [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd430.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf430.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00be1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1430.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be1e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e60.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 6. [`00bdb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb250.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1130.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1210.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb430",
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
      "new": "00bdd430",
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
        "reverse_margin": 0.0
      },
      "new": "00bdf430",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d3c2b75e11e35daf40950a40323ed9b5"></a>

### v16.0.0 [`00c5ea30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea30.md) _ZNSt12out_of_rangeD1Ev

`competing_candidates` 

呼出元 1件 [`00c379c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md) · 呼出先 1件 [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md)

- 1. [`00bdd440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd440.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bdf440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf440.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00be1440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1440.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e70.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00bdb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb250.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be1130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1130.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be1210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1210.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be1e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e60.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdd440",
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
        "reverse_margin": 0.0
      },
      "new": "00bdf440",
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
      "new": "00be1440",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ecec57e178f8a72fc3b9df448b171db8"></a>

### v16.0.0 [`00c5ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea40.md) _ZNSt13runtime_errorD2Ev

`competing_candidates` 

呼出元 1件 [`00c37acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37acc.md) · 呼出先 1件 [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md)

- 1. [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd450.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1450.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e80.md) · スコア 69.0 · 採用条件未達 · 順位差 -11.0 / -11.0 · short_function_requires_other_identity_evidence, instruction_coverage
- 5. [`00bdda70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda70.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00be0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f70.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00be0fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fd0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 8. [`00be11a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11a0.md) · スコア 67.0 · 採用条件未達 · 順位差 -13.0 / -13.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bdb450",
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
      "new": "00bdd450",
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
      "new": "00be1450",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2097bd1a1070641d3185932b517d4565"></a>

### v16.0.0 [`0112a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a000.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`00c57a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a20.md) · 呼出先 0件 

- 1. [`010a5000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5000.md) · スコア 79.0 · 採用条件未達 · 順位差 79.0 / 79.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 79.0,
        "reverse_margin": 79.0
      },
      "new": "010a5000",
      "score": 79.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-95f6fb75c479e1efa2b2a9b6ebfa845e"></a>

### v16.0.0 [`0112a148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a148.md) &lt;EXTERNAL&gt;::closedir

`competing_candidates` 

呼出元 1件 [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) · 呼出先 0件 

- 1. [`010a5148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5148.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a5148",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-64d00965dea27e54d896e78e0c50c2a7"></a>

### v16.0.0 [`0112a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a188.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`00c594e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594e0.md) · 呼出先 0件 

- 1. [`010a5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5188.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a5188",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-43a5af62148536944ebd3c89c2688a9d"></a>

### v16.0.0 [`0112a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a280.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`00c59d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d90.md) · 呼出先 0件 

- 1. [`010a5280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5280.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5288.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "010a5280",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "010a5288",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3bf48381d62844f22ff8c200e2e1fa2c"></a>

### v16.0.0 [`0112a288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a288.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 1件 [`00c59da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59da0.md) · 呼出先 0件 

- 1. [`010a5288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5288.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5280.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "010a5288",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "010a5280",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fd2b34551abe0c5a176c2ea1766bcebe"></a>

### v16.0.0 [`0112a2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a2b0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`00c59df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59df0.md) · 呼出先 0件 

- 1. [`010a52b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a52b0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-17ebf3c20b37c627edf6c63ad61a05e4"></a>

### v16.0.0 [`0112a2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a2f8.md) &lt;EXTERNAL&gt;::rename

`competing_candidates` 

呼出元 1件 [`00c59e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e90.md) · 呼出先 0件 

- 1. [`010a52f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a52f8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7d58a271b151c2877a102754abd6d05a"></a>

### v16.0.0 [`0112a3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c0.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`00c5a030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a030.md) · 呼出先 0件 

- 1. [`010a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "010a53c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "010a53c8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4609e947def68b1daf48d0cbe171d1a2"></a>

### v16.0.0 [`0112a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c8.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`00c5a040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a040.md) · 呼出先 0件 

- 1. [`010a53c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "010a53c8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "010a53c0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-95e447fae8e1e1cf24b14a635d200e13"></a>

### v16.0.0 [`0112a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3f8.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`00c5a0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0a0.md) · 呼出先 0件 

- 1. [`010a53f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a53f8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-57bca243635317391a639a6d79e4f2e2"></a>

### v16.0.0 [`0112a558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a558.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`00c5a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a520.md) · 呼出先 0件 

- 1. [`010a5558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5558.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a5558",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2409922e34a8b7d0d9745b1063f7dd2b"></a>

### v16.0.0 [`0112a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a568.md) &lt;EXTERNAL&gt;::atan2

`competing_candidates` 

呼出元 1件 [`00c5a750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a750.md) · 呼出先 0件 

- 1. [`010a5568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5568.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 84.0,
        "reverse_margin": 84.0
      },
      "new": "010a5568",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v15.7.4 [`00421b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b38.md) FUN_00421b38

`initial_match_conflict` [`00444638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444638.md)

呼出元 1件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00421924",
    "00422098",
    "00444424",
    "00444b98"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0042ca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca50.md) FUN_0042ca50

`initial_match_conflict` [`0044f8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8e8.md)

呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0042ca08",
    "0042ca70",
    "0044f8a0",
    "0044f908"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 30.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 30.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00449c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c2c.md) FUN_00449c2c

`initial_match_conflict` [`0046cac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cac4.md)

呼出元 1件 [`0046d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00449c14",
    "00449c34",
    "0046caac",
    "0046cacc"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044b8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8b8.md) FUN_0044b8b8

`initial_match_conflict` [`0046e750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e750.md)

呼出元 3件 [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044b8b0",
    "0044b8c0",
    "0046e748",
    "0046e758"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8d4.md) FUN_0044b8d4

`initial_match_conflict` [`0046e76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e76c.md)

呼出元 8件 [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) [`00686764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`008bc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044b8c8",
    "0044b8ec",
    "0046e760",
    "0046e784"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044b8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8dc.md) FUN_0044b8dc

`initial_match_conflict` [`0046e774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e774.md)

呼出元 8件 [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) [`00686764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`008bc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044b8c8",
    "0044b8ec",
    "0046e760",
    "0046e784"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044b8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8e4.md) FUN_0044b8e4

`initial_match_conflict` [`0046e77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e77c.md)

呼出元 9件 [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) [`00686764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`008b3390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044b8c8",
    "0044b8ec",
    "0046e760",
    "0046e784"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d24c.md) FUN_0044d24c

`initial_match_conflict` [`004700e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700e4.md)

呼出元 2件 [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`008e68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e68f8.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044d208",
    "0044d254",
    "004700a0",
    "004700ec"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044d264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d264.md) FUN_0044d264

`initial_match_conflict` [`004700fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700fc.md)

呼出元 3件 [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044d254",
    "0044d27c",
    "004700ec",
    "00470114"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044d26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d26c.md) FUN_0044d26c

`initial_match_conflict` [`00470104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470104.md)

呼出元 3件 [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044d254",
    "0044d27c",
    "004700ec",
    "00470114"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044d274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d274.md) FUN_0044d274

`initial_match_conflict` [`0047010c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/0047010c.md)

呼出元 8件 [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) [`005d76a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d7/005d76a0.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044d254",
    "0044d27c",
    "004700ec",
    "00470114"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044fb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fb28.md) FUN_0044fb28

`initial_match_conflict` [`004729c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729c0.md)

呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044f798",
    "0044fb34",
    "00472630",
    "004729cc"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 99.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 99.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0044fcd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fcd4.md) FUN_0044fcd4

`initial_match_conflict` [`00472b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b6c.md)

呼出元 5件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) [`009a6250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6250.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0044fc20",
    "0044fce4",
    "00472ab8",
    "00472b7c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00456ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456ee0.md) FUN_00456ee0

`initial_match_conflict` [`00479d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d78.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00456ed4",
    "00456ef0",
    "00479d6c",
    "00479d88"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 95.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 95.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`004588e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588e8.md) FUN_004588e8

`initial_match_conflict` [`0047b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b780.md)

呼出元 3件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`008226b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008226b4.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00458634",
    "004588f4",
    "0047b4cc",
    "0047b78c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0045becc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045becc.md) FUN_0045becc

`initial_match_conflict` [`0047ed64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed64.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0045bec4",
    "0045bedc",
    "0047ed5c",
    "0047ed74"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0045bed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bed4.md) FUN_0045bed4

`initial_match_conflict` [`0047ed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed6c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0045bec4",
    "0045bedc",
    "0047ed5c",
    "0047ed74"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00469e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e08.md) FUN_00469e08

`initial_match_conflict` [`0048cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cca0.md)

呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00469a60",
    "00469e10",
    "0048c8f8",
    "0048cca8"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0047a220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a220.md) FUN_0047a220

`initial_match_conflict` [`0049d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0b8.md)

呼出元 1件 [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0047a1b0",
    "0047a228",
    "0049d048",
    "0049d0c0"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`004ac5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac5e0.md) FUN_004ac5e0

`initial_match_conflict` [`004cf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf478.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "004abba0",
    "004ac5ec",
    "004cea38",
    "004cf484"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`004ac614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac614.md) FUN_004ac614

`initial_match_conflict` [`004cf4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4ac.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "004ac5ec",
    "004ac61c",
    "004cf484",
    "004cf4b4"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`004d3a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a7c.md) FUN_004d3a7c

`initial_match_conflict` [`004f6914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6914.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "004d3a38",
    "004d3a84",
    "004f68d0",
    "004f691c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050c240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c240.md) FUN_0050c240

`initial_match_conflict` [`0052f0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f0d8.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c218",
    "0050c390",
    "0052f0b0",
    "0052f228"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c52c.md) FUN_0050c52c

`initial_match_conflict` [`0052f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f3c4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c504",
    "0050c67c",
    "0052f39c",
    "0052f514"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c818.md) FUN_0050c818

`initial_match_conflict` [`0052f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f6b0.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c7f0",
    "0050c968",
    "0052f688",
    "0052f800"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050c9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c9b4.md) FUN_0050c9b4

`initial_match_conflict` [`0052f84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f84c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c968",
    "0050c9c4",
    "0052f800",
    "0052f85c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050c9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c9bc.md) FUN_0050c9bc

`initial_match_conflict` [`0052f854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f854.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c968",
    "0050c9c4",
    "0052f800",
    "0052f85c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050ca2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050ca2c.md) FUN_0050ca2c

`initial_match_conflict` [`0052f8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8c4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050c9c4",
    "0050ca48",
    "0052f85c",
    "0052f8e0"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d21c.md) FUN_0050d21c

`initial_match_conflict` [`005300b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005300b4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050d18c",
    "0050d248",
    "00530024",
    "005300e0"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 96.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 96.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d3f4.md) FUN_0050d3f4

`initial_match_conflict` [`0053028c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053028c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050d38c",
    "0050d410",
    "00530224",
    "005302a8"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050d77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d77c.md) FUN_0050d77c

`initial_match_conflict` [`00530614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530614.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050d738",
    "0050d78c",
    "005305d0",
    "00530624"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 95.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 95.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050d784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d784.md) FUN_0050d784

`initial_match_conflict` [`0053061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053061c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050d738",
    "0050d78c",
    "005305d0",
    "00530624"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 95.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 95.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050d8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8ec.md) FUN_0050d8ec

`initial_match_conflict` [`00530784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530784.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050d8cc",
    "0050d8f4",
    "00530764",
    "0053078c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 99.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 99.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050dfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfcc.md) FUN_0050dfcc

`initial_match_conflict` [`00530e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e64.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050df4c",
    "0050dfd4",
    "00530de4",
    "00530e6c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 97.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 97.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050e224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e224.md) FUN_0050e224

`initial_match_conflict` [`005310bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310bc.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050e1e4",
    "0050e234",
    "0053107c",
    "005310cc"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050e42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e42c.md) FUN_0050e42c

`initial_match_conflict` [`005312c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312c4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050e32c",
    "0050e43c",
    "005311c4",
    "005312d4"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050e634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e634.md) FUN_0050e634

`initial_match_conflict` [`005314cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314cc.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050e534",
    "0050e67c",
    "005313cc",
    "00531514"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 4,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050e834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e834.md) FUN_0050e834

`initial_match_conflict` [`005316cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005316cc.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050e7fc",
    "0050e944",
    "00531694",
    "005317dc"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050ea04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea04.md) FUN_0050ea04

`initial_match_conflict` [`0053189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053189c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050e9cc",
    "0050ea1c",
    "00531864",
    "005318b4"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050ed1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed1c.md) FUN_0050ed1c

`initial_match_conflict` [`00531bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bb4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050ecac",
    "0050edd4",
    "00531b44",
    "00531c6c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee84.md) FUN_0050ee84

`initial_match_conflict` [`00531d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d1c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050ee5c",
    "0050ee8c",
    "00531cf4",
    "00531d24"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 99.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 99.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050f18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f18c.md) FUN_0050f18c

`initial_match_conflict` [`00532024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532024.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050ef84",
    "0050f19c",
    "00531e1c",
    "00532034"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 98.2047,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.2047,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050f670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f670.md) FUN_0050f670

`initial_match_conflict` [`00532508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532508.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050f62c",
    "0050f680",
    "005324c4",
    "00532518"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 98.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050fbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fbb0.md) FUN_0050fbb0

`initial_match_conflict` [`00532a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532a48.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050fb78",
    "0050fbb8",
    "00532a10",
    "00532a50"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 99.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 99.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050fc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc54.md) FUN_0050fc54

`initial_match_conflict` [`00532aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532aec.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050fbb8",
    "0050fc5c",
    "00532a50",
    "00532af4"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0050fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fea0.md) FUN_0050fea0

`initial_match_conflict` [`00532d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d38.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0050fe60",
    "0050ffa4",
    "00532cf8",
    "00532e3c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 98.8095,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.8095,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00510c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c68.md) FUN_00510c68

`initial_match_conflict` [`00533b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b00.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00510c3c",
    "00510c70",
    "00533ad4",
    "00533b08"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 99.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 99.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00510ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510ef8.md) FUN_00510ef8

`initial_match_conflict` [`00533d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533d90.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00510dc0",
    "00510f14",
    "00533c58",
    "00533dac"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`005110a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005110a8.md) FUN_005110a8

`initial_match_conflict` [`00533f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533f40.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "005110a4",
    "005110e0",
    "00533f3c",
    "00533f78"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 97.9091,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 97.9091,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`005110e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005110e4.md) FUN_005110e4

`initial_match_conflict` [`00533f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533f7c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "005110e0",
    "005110f4",
    "00533f78",
    "00533f8c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`00511118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511118.md) FUN_00511118

`initial_match_conflict` [`00533fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533fb0.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "005110f4",
    "00511124",
    "00533f8c",
    "00533fbc"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`005111c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c0.md) FUN_005111c0

`initial_match_conflict` [`00534058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534058.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "00511164",
    "005111c8",
    "00533ffc",
    "00534060"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 2,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 97.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 97.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`005112ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112ec.md) FUN_005112ec

`initial_match_conflict` [`00534184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534184.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "005111c8",
    "005112f4",
    "00534060",
    "0053418c"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 97.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 97.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.4 [`0051178c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051178c.md) FUN_0051178c

`initial_match_conflict` [`00534624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534624.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "anchor_audit": {
    "independent_anchor": false,
    "origin": "initial_estimate",
    "structure_states": [
      "available",
      "available"
    ]
  },
  "audit_reason": "ambiguous_short_function",
  "bounds": [
    "0051175c",
    "0051179c",
    "005345f4",
    "00534634"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 3,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": true,
  "local_unique_shape": true,
  "margin": 15.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "normalized_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 15.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

