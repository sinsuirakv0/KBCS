# v16.0.0 → v16.0.1 · 追加調査 (86)

[一覧の目次](README.md)

### v16.0.1 [`00c488c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c488c4.md) FUN_00c488c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4849c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4849c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00c4d334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d334.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00c48380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md) · スコア 68.461538 · 採用条件未達 · 順位差 0.0 / -11.538461999999996 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bf97f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md) · スコア 50.0 · 採用条件未達 · 順位差 0.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bf0140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0140.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bf979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf979c.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bf9b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00c50cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md) · スコア 8.421053 · 採用条件未達 · 順位差 0.0 / -71.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00c4849c",
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
      "new": "00c4d334",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8076923076923077,
          0.8076923076923077
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
        "reverse_margin": -11.538461999999996
      },
      "new": "00c48380",
      "score": 68.461538
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8459ecb9c21d1569f0d7924b016a6788"></a>

### v16.0.1 [`00c48d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48d44.md) FUN_00c48d44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4891c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4891c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe04.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4891c",
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
      "new": "00c4fe04",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-36e962bdfd27246cfdae1df26c5e1bfd"></a>

### v16.0.1 [`00c4bb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb40.md) FUN_00c4bb40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4b718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4cadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cadc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c4cbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4b718",
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
      "new": "00c4c9a8",
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
      "new": "00c4cadc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0d418e8e37b757ba7e41ed8e4a355b0f"></a>

### v16.0.1 [`00c4c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c20c.md) FUN_00c4c20c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bde4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5d4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d304.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4bde4",
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
      "new": "00c4c5d4",
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
      "new": "00c4d304",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-458f271ab01aa25253106a9fa2f937b6"></a>

### v16.0.1 [`00c4c9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c9fc.md) FUN_00c4c9fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bde4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5d4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d304.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4bde4",
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
      "new": "00c4c5d4",
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
      "new": "00c4d304",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fa4f7154d87ccfb3949881f036d1992b"></a>

### v16.0.1 [`00c4cdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdd0.md) FUN_00c4cdd0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4b718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4cadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cadc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c4cbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4b718",
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
      "new": "00c4c9a8",
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
      "new": "00c4cadc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b8b8dd73248869fe067dc34af7df3387"></a>

### v16.0.1 [`00c4cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf04.md) FUN_00c4cf04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4b718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4cadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cadc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c4cbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4b718",
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
      "new": "00c4c9a8",
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
      "new": "00c4cadc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5166311b4bb4c7ec69898e48516c8bc9"></a>

### v16.0.1 [`00c4d024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d024.md) FUN_00c4d024

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4b718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4cadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cadc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c4cbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4b718",
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
      "new": "00c4c9a8",
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
      "new": "00c4cadc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9391b52499c2704fc63e2bc099950fe7"></a>

### v16.0.1 [`00c4d72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d72c.md) FUN_00c4d72c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bde4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5d4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c4d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d304.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4bde4",
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
      "new": "00c4c5d4",
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
      "new": "00c4d304",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.1 [`00c4d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d75c.md) FUN_00c4d75c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4849c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4849c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00c4d334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d334.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00c48380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md) · スコア 68.461538 · 採用条件未達 · 順位差 0.0 / -11.538461999999996 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bf97f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf97f0.md) · スコア 50.0 · 採用条件未達 · 順位差 0.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bf0140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0140.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bf979c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf979c.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bf9b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00c50cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md) · スコア 8.421053 · 採用条件未達 · 順位差 0.0 / -71.578947 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00c4849c",
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
      "new": "00c4d334",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8076923076923077,
          0.8076923076923077
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
        "reverse_margin": -11.538461999999996
      },
      "new": "00c48380",
      "score": 68.461538
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-714246d8540e1dfd3cd4eb53a209cee1"></a>

### v16.0.1 [`00c4d9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9a4.md) FUN_00c4d9a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4d57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d57c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c4d588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d588.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c4d57c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c4d588",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6acf0d35b9b5d752c5c1420494a53617"></a>

### v16.0.1 [`00c4d9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d9b0.md) FUN_00c4d9b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4d588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d588.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c4d57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d57c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c4d588",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c4d57c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ae963bc457abed15e0b457aa86d9eead"></a>

### v16.0.1 [`00c4f904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f904.md) FUN_00c4f904

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4dc.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c4f4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4e8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c4f4dc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c4f4e8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c960d992a781923e1a9559586834270f"></a>

### v16.0.1 [`00c4f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f910.md) FUN_00c4f910

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4f4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4e8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c4f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4dc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c4f4e8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c4f4dc",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b247be794207478162b70cc72082925"></a>

### v16.0.1 [`00c50024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50024.md) FUN_00c50024

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c50f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f18.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c513e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c513e4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c50b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b04.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c4cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md) · スコア 25.0 · 採用条件未達 · 順位差 0.0 / -55.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c4850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00c4fbfc",
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
      "new": "00c50f18",
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
      "new": "00c513e4",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fdaa041cdf062c98e55c46f89220ed77"></a>

### v16.0.1 [`00c5022c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5022c.md) FUN_00c5022c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4891c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4891c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c4fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe04.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c4891c",
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
      "new": "00c4fe04",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-590885040a179a7a0e43a857fd36f990"></a>

### v16.0.1 [`00c50ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ca0.md) FUN_00c50ca0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c50878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50878.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c50884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50884.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c50890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50890.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c50878",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c50884",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c50890",
      "score": 2.4
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-52509d4e6653c4b8253ba78d0a12b8b3"></a>

### v16.0.1 [`00c50cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50cac.md) FUN_00c50cac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c50884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50884.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c50878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50878.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c50890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50890.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c50884",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c50878",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c50890",
      "score": 2.4
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e82993be79c3697db53a82c410c00f83"></a>

### v16.0.1 [`00c50cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50cb8.md) FUN_00c50cb8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c50890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50890.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c50890",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2b475fad2f55276b389231100990ba1f"></a>

### v16.0.1 [`00c51340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51340.md) FUN_00c51340

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c50f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f18.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c513e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c513e4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c50b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b04.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c4cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md) · スコア 25.0 · 採用条件未達 · 順位差 0.0 / -55.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c4850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00c4fbfc",
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
      "new": "00c50f18",
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
      "new": "00c513e4",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a982495a83e1d3ceab800ed296f33179"></a>

### v16.0.1 [`00c5180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5180c.md) FUN_00c5180c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c4fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fbfc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c50f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f18.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00c513e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c513e4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00c50b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b04.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c4cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md) · スコア 25.0 · 採用条件未達 · 順位差 0.0 / -55.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c4850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00c4fbfc",
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
      "new": "00c50f18",
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
      "new": "00c513e4",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-efdf49c2e98c7958e93d8c4097b9fe1e"></a>

### v16.0.1 [`00c51b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b64.md) FUN_00c51b64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c5173c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5173c.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00c5173c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ee3d277db2791fd4f979461a909490ff"></a>

### v16.0.1 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) FUN_00c52818

`competing_candidates` 

呼出元 6件 [`00c51f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f64.md) [`00c51ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md) [`00c5209c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5209c.md) [`00c52130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md) [`00c5221c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md) · 呼出先 2件 [`00c52844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52844.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

- 1. [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) · スコア 44.363636 · 採用条件未達 · 順位差 40.363636 / 40.363636 · short_function_requires_other_identity_evidence, instruction_coverage
- 2. [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) · スコア 4.0 · 採用条件未達 · 順位差 4.0 / -40.363636 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2727272727272727,
          0.2727272727272727
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
        "margin": 40.363636,
        "reverse_margin": 40.363636
      },
      "new": "00c523f0",
      "score": 44.363636
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
          "already_matched_elsewhere"
        ],
        "margin": 4.0,
        "reverse_margin": -40.363636
      },
      "new": "00c538e0",
      "score": 4.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9a2b6ff2e75f8c21f196e2f46d817ea9"></a>

### v16.0.1 [`00c52844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52844.md) FUN_00c52844

`competing_candidates` 

呼出元 1件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) · 呼出先 2件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

- 1. [`00c5241c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5241c.md) · スコア 68.75 · 採用条件未達 · 順位差 61.25 / 61.25 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c2bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bda0.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -61.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c2c0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -61.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c2c198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c198.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -61.25 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c2c408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md) · スコア 7.5 · 採用条件未達 · 順位差 7.5 / -61.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00495478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md) · スコア 3.75 · 採用条件未達 · 順位差 3.75 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) · スコア 3.75 · 採用条件未達 · 順位差 3.75 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bb9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md) · スコア 3.75 · 採用条件未達 · 順位差 3.75 / -65.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8125,
          0.8125
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
        "margin": 61.25,
        "reverse_margin": 61.25
      },
      "new": "00c5241c",
      "score": 68.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.42105263157894735,
          0.125
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
        "margin": 7.5,
        "reverse_margin": -61.25
      },
      "new": "00c2bda0",
      "score": 7.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.34782608695652173,
          0.125
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
        "margin": 7.5,
        "reverse_margin": -61.25
      },
      "new": "00c2c0d4",
      "score": 7.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-928388d2a6ae4310d01e198da8bddd42"></a>

### v16.0.1 [`00c538bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c538bc.md) FUN_00c538bc

`competing_candidates` 

呼出元 1件 [`00c53b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md) · 呼出先 0件 

- 1. [`00c5349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c5349c.md) · スコア 67.368421 · 採用条件未達 · 順位差 67.368421 / 67.368421 · instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7894736842105263,
          0.7894736842105263
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
        "margin": 67.368421,
        "reverse_margin": 67.368421
      },
      "new": "00c5349c",
      "score": 67.368421
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9f5fdaae99773a7a565639ec6b7854fa"></a>

### v16.0.1 [`00c54898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54898.md) FUN_00c54898

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c54478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54478.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c54480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54480.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c54488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54488.md) · スコア 0.4706 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c54478",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54480",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54488",
      "score": 0.4706
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-91e05cb681e719590f3ac4d0128c536c"></a>

### v16.0.1 [`00c548a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548a0.md) FUN_00c548a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c54480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54480.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c54478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54478.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c54488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54488.md) · スコア 0.4706 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00c54480",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54478",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54488",
      "score": 0.4706
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4cafe6ffec30d047867aaf2d15acaf49"></a>

### v16.0.1 [`00c548a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548a8.md) FUN_00c548a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c54488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54488.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00c54488",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cbd70db95c56dc0cc6cd6a3853ff985a"></a>

### v16.0.1 [`00c54abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54abc.md) FUN_00c54abc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c5469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5469c.md) · スコア 80.0 · 採用条件未達 · 順位差 36.0 / 36.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c546b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546b0.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c546c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546c0.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 36.0,
        "reverse_margin": 36.0
      },
      "new": "00c5469c",
      "score": 80.0
    },
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
        "margin": -36.0,
        "reverse_margin": -36.0
      },
      "new": "00c546b0",
      "score": 44.0
    },
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
        "margin": -36.0,
        "reverse_margin": -36.0
      },
      "new": "00c546c0",
      "score": 44.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-af32c03f75d3fcf1e9e946996c58b260"></a>

### v16.0.1 [`00c54ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54ad0.md) FUN_00c54ad0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c546b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546b0.md) · スコア 80.0 · 採用条件未達 · 順位差 15.0 / 15.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c546c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546c0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c5469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5469c.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c546b0",
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "00c546c0",
      "score": 65.0
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
      "new": "00c5469c",
      "score": 44.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d0ecf1ba504363b46d8410e3ccb29756"></a>

### v16.0.1 [`00c54ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54ae0.md) FUN_00c54ae0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c546c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546c0.md) · スコア 80.0 · 採用条件未達 · 順位差 15.0 / 15.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c546b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546b0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00c5469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5469c.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c546c0",
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "00c546b0",
      "score": 65.0
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
      "new": "00c5469c",
      "score": 44.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bbe5b539d4ffa644092a90098411090a"></a>

### v16.0.1 [`00c54c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c24.md) FUN_00c54c24

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57bb8.md)

- 1. [`00c54804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54804.md) · スコア 84.0 · 採用条件未達 · 順位差 80.0 / 80.0 · 
- 2. [`00c54810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54810.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c5481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5481c.md) · スコア 1.0909 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c54804",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54810",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c5481c",
      "score": 1.0909
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-58a7c0ba306cb6e994f622b9660af55e"></a>

### v16.0.1 [`00c54c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c30.md) FUN_00c54c30

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c54810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54810.md) · スコア 84.0 · 採用条件未達 · 順位差 80.0 / 80.0 · 
- 2. [`00c54804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54804.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c5481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5481c.md) · スコア 1.0909 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c54810",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c54804",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c5481c",
      "score": 1.0909
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9d91156263d5bbaf5b5e11994add0bfd"></a>

### v16.0.1 [`00c54c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c3c.md) FUN_00c54c3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c5481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c5481c.md) · スコア 80.0 · 採用条件未達 · 順位差 21.818182 / 21.818182 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md) · スコア 58.181818 · 採用条件未達 · 順位差 58.181818 / -21.818182 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 21.818182,
        "reverse_margin": 21.818182
      },
      "new": "00c5481c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7,
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
        "margin": 58.181818,
        "reverse_margin": -21.818182
      },
      "new": "00c53ff8",
      "score": 58.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bd4a9064369704a286f5bc3612b0f07c"></a>

### v16.0.1 [`00c54ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54ea4.md) FUN_00c54ea4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57b88.md)

- 1. [`00c54a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54a84.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00c54a84",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-63d8671f012e0cc9752ae87ccc89203f"></a>

### v16.0.1 [`00c57b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57b88.md) FUN_00c57b88

`competing_candidates` 

呼出元 1件 [`00c54ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54ea4.md) · 呼出先 0件 

- 1. [`00c57768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57768.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c57798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57798.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00c57768",
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
        "reverse_margin": -60.0
      },
      "new": "00c57798",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9beee834d8082c01f81222d827d435d1"></a>

### v16.0.1 [`00c57bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57bb8.md) FUN_00c57bb8

`competing_candidates` 

呼出元 1件 [`00c54c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c24.md) · 呼出先 0件 

- 1. [`00c57798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57798.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · insufficient_independent_call_anchors
- 2. [`00c57768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57768.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00c57798",
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
        "margin": -60.0,
        "reverse_margin": -80.0
      },
      "new": "00c57768",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5803bb96fb307982640a270f2614afc4"></a>

### v16.0.1 [`00c57ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ce4.md) FUN_00c57ce4

`competing_candidates` 

呼出元 1件 [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) · 呼出先 1件 [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md)

- 1. [`00c578dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578dc.md) · スコア 6.2222 · 採用条件未達 · 順位差 — / — · 
- 2. [`00c578d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578d4.md) · スコア 5.5789 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c578e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578e4.md) · スコア 5.5789 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c578c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578c4.md) · スコア 5.3636 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c578cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578cc.md) · スコア 5.2857 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {},
      "new": "00c578dc",
      "score": 6.2222
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c578d4",
      "score": 5.5789
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c578e4",
      "score": 5.5789
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c64e02c4e4fcff65f32d4ceaca4edc66"></a>

### v16.0.1 [`00c57cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cec.md) FUN_00c57cec

`competing_candidates` 

呼出元 1件 [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 1件 [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md)

- 1. [`00c578dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578dc.md) · スコア 12.3333 · 採用条件未達 · 順位差 6.1111 / 5.0 · 
- 2. [`00c578c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578c4.md) · スコア 7.3333 · 採用条件未達 · 順位差 1.9697 / 0.0 · 
- 3. [`00c578cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578cc.md) · スコア 7.1034 · 採用条件未達 · 順位差 1.8177 / -0.2299 · 
- 4. [`00c578d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578d4.md) · スコア 5.875 · 採用条件未達 · 順位差 0.2961 / -1.4583 · 
- 5. [`00c578e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578e4.md) · スコア 5.875 · 採用条件未達 · 順位差 0.2961 / -1.4583 · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 6.1111,
        "reverse_margin": 5.0
      },
      "new": "00c578dc",
      "score": 12.3333
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 1.9697,
        "reverse_margin": 0.0
      },
      "new": "00c578c4",
      "score": 7.3333
    },
    {
      "eligible": "",
      "evidence": {
        "margin": 1.8177,
        "reverse_margin": -0.2299
      },
      "new": "00c578cc",
      "score": 7.1034
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8713ab68a940860c62c4fece3fef1968"></a>

### v16.0.1 [`00c57e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e00.md) FUN_00c57e00

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c57a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a00.md) · スコア 68.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a210.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5c210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c210.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c5e210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e210.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c57a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a20.md) · スコア 56.0 · 採用条件未達 · 順位差 -24.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00c57a00",
      "score": 68.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          0.8
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
        "margin": 68.0,
        "reverse_margin": 0.0
      },
      "new": "00c58210",
      "score": 68.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          0.8
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
        "margin": 68.0,
        "reverse_margin": 0.0
      },
      "new": "00c5a210",
      "score": 68.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e8c0576c484f23eea66ee00c18a2bb27"></a>

### v16.0.1 [`00c57e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e20.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`0043ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae10.md) · 呼出先 1件 [`0112a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a000.md)

- 1. [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e220.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c57a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a20.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00c57a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a00.md) · スコア 56.0 · 採用条件未達 · 順位差 -12.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00c58220",
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
      "new": "00c5a220",
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
      "new": "00c5c220",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a6ea98e04bfd5b2fde1e149b7d9ca3ef"></a>

### v16.0.1 [`00c598e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598e0.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`004fca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fca18.md) · 呼出先 1件 [`0112a188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a188.md)

- 1. [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bce0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dce0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c594e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594e0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c57ce0",
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
      "new": "00c59ce0",
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
      "new": "00c5bce0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f7b722202f1197e4280f46e6d04c2b49"></a>

### v16.0.1 [`00c5a190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a190.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`0057d100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d100.md) · 呼出先 1件 [`0112a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a280.md)

- 1. [`00c58590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58590.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a590.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c590.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c59d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d90.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00c59da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59da0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c58590",
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
      "new": "00c5a590",
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
      "new": "00c5c590",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1f6f5656f46477fc3358926de4200d54"></a>

### v16.0.1 [`00c5a1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1a0.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 2件 [`0057d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d190.md) [`0057d1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d1a4.md) · 呼出先 1件 [`0112a288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a288.md)

- 1. [`00c585a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c59d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d90.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00c59da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59da0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c585a0",
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
      "new": "00c5a5a0",
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
      "new": "00c5c5a0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-001af7fe3d0463ff5783695b872d8331"></a>

### v16.0.1 [`00c5a1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1f0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`0057d324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d324.md) · 呼出先 1件 [`0112a2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a2b0.md)

- 1. [`00c585f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c59df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59df0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c585f0",
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
      "new": "00c5a5f0",
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
      "new": "00c5c5f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f97a55d0613840ccc6303b027b57ca28"></a>

### v16.0.1 [`00c5a430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a430.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`00591800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591800.md) · 呼出先 1件 [`0112a3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3c0.md)

- 1. [`00c58830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58830.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c830.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e830.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c5a030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a030.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00c5a040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a040.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c58830",
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
      "new": "00c5a830",
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
      "new": "00c5c830",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5a1379c6df6f0948d5ee09707e194fe7"></a>

### v16.0.1 [`00c5a440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a440.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`00591808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591808.md) · 呼出先 1件 [`0112a3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3c8.md)

- 1. [`00c58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c840.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e840.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c5a030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a030.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00c5a040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a040.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c58840",
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
      "new": "00c5a840",
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
      "new": "00c5c840",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-381ee6b313c1fd859aa0ca42291b27a8"></a>

### v16.0.1 [`00c5a4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4a0.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`00591b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b08.md) · 呼出先 1件 [`0112a3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3f8.md)

- 1. [`00c588a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5c8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5e8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c5a0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0a0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c588a0",
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
      "new": "00c5a8a0",
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
      "new": "00c5c8a0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6319efdaf2867b73152ecada17e989d4"></a>

### v16.0.1 [`00c5a920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a920.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`0112a558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a558.md)

- 1. [`00c58d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c5cd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c5a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a520.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00c58d20",
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
      "new": "00c5ad20",
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
      "new": "00c5cd20",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-064dc21bf783aa4e0d4c5a6899466778"></a>

### v16.0.1 [`0112a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a000.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`00c57e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e20.md) · 呼出先 0件 

- 1. [`0112a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a000.md) · スコア 79.0 · 採用条件未達 · 順位差 79.0 / 79.0 · 

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
      "new": "0112a000",
      "score": 79.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cb933a82af6b4b92625a0131e9de9842"></a>

### v16.0.1 [`0112a148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a148.md) &lt;EXTERNAL&gt;::closedir

`competing_candidates` 

呼出元 1件 [`004fbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) · 呼出先 0件 

- 1. [`0112a148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a148.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0112a148",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b876bfa0d3cd6f93be8d60afd05bfd93"></a>

### v16.0.1 [`0112a188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a188.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`00c598e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598e0.md) · 呼出先 0件 

- 1. [`0112a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a188.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0112a188",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c391c22967dd848081e15e6642369c75"></a>

### v16.0.1 [`0112a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a280.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`00c5a190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a190.md) · 呼出先 0件 

- 1. [`0112a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a280.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0112a288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a288.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0112a280",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0112a288",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7267cdccf694d9a81a864e304f8e98c4"></a>

### v16.0.1 [`0112a288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a288.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 1件 [`00c5a1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1a0.md) · 呼出先 0件 

- 1. [`0112a288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a288.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0112a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a280.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0112a288",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0112a280",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a3f84f46be6ad96cc65671e5fb116241"></a>

### v16.0.1 [`0112a2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a2b0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`00c5a1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1f0.md) · 呼出先 0件 

- 1. [`0112a2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a2b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0112a2b0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e2ea3667cab6c90711aaac97aaaaed96"></a>

### v16.0.1 [`0112a3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3c0.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`00c5a430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a430.md) · 呼出先 0件 

- 1. [`0112a3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0112a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0112a3c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0112a3c8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b23885dc04fe9778e06679ab1ee55e27"></a>

### v16.0.1 [`0112a3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3c8.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`00c5a440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a440.md) · 呼出先 0件 

- 1. [`0112a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0112a3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3c0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0112a3c8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0112a3c0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2d5476e0723e02834f504a022a905ee7"></a>

### v16.0.1 [`0112a3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a3f8.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`00c5a4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4a0.md) · 呼出先 0件 

- 1. [`0112a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a3f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0112a3f8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aa6402e00c8997430632ae64d1614b5a"></a>

### v16.0.1 [`0112a558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a558.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`00c5a920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a920.md) · 呼出先 0件 

- 1. [`0112a558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a558.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0112a558",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v16.0.0 [`00444638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444638.md) FUN_00444638

`initial_match_conflict` [`00444678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444678.md)

呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 0件 


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
    "004445d4",
    "00444b98",
    "00444614",
    "00444bd8"
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

### v16.0.0 [`00467e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e5c.md) FUN_00467e5c

`initial_match_conflict` [`00467e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md)

呼出元 6件 [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`0068bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md) [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) [`00862868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00862/00862868.md) · 呼出先 0件 


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
    "00467d7c",
    "00467e6c",
    "00467dbc",
    "00467eac"
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

### v16.0.0 [`00467e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e64.md) FUN_00467e64

`initial_match_conflict` [`00467ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ea4.md)

呼出元 9件 [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`006797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006797c0.md) [`0068bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md) [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) · 呼出先 0件 


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
    "00467d7c",
    "00467e6c",
    "00467dbc",
    "00467eac"
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

### v16.0.0 [`0046cac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cac4.md) FUN_0046cac4

`initial_match_conflict` [`0046cb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb04.md)

呼出元 1件 [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) · 呼出先 0件 


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
    "0046caac",
    "0046cacc",
    "0046caec",
    "0046cb0c"
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

### v16.0.0 [`0046e750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e750.md) FUN_0046e750

`initial_match_conflict` [`0046e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e790.md)

呼出元 3件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 0件 


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
    "0046e748",
    "0046e758",
    "0046e788",
    "0046e798"
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

### v16.0.0 [`0046e76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e76c.md) FUN_0046e76c

`initial_match_conflict` [`0046e7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7ac.md)

呼出元 8件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006acaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`008f0838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md) · 呼出先 0件 


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
    "0046e760",
    "0046e784",
    "0046e7a0",
    "0046e7c4"
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

### v16.0.0 [`0046e774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e774.md) FUN_0046e774

`initial_match_conflict` [`0046e7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7b4.md)

呼出元 8件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006acaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`008f0838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md) · 呼出先 0件 


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
    "0046e760",
    "0046e784",
    "0046e7a0",
    "0046e7c4"
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

### v16.0.0 [`0046e77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e77c.md) FUN_0046e77c

`initial_match_conflict` [`0046e7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7bc.md)

呼出元 9件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006acaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`008e7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md) · 呼出先 0件 


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
    "0046e760",
    "0046e784",
    "0046e7a0",
    "0046e7c4"
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

### v16.0.0 [`004700e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700e4.md) FUN_004700e4

`initial_match_conflict` [`00470124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470124.md)

呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 0件 


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
    "004700a0",
    "004700ec",
    "004700e0",
    "0047012c"
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

### v16.0.0 [`004700fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700fc.md) FUN_004700fc

`initial_match_conflict` [`0047013c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/0047013c.md)

呼出元 3件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 0件 


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
    "004700ec",
    "00470114",
    "0047012c",
    "00470154"
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

### v16.0.0 [`00470104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470104.md) FUN_00470104

`initial_match_conflict` [`00470144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470144.md)

呼出元 3件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 0件 


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
    "004700ec",
    "00470114",
    "0047012c",
    "00470154"
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

### v16.0.0 [`0047010c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/0047010c.md) FUN_0047010c

`initial_match_conflict` [`0047014c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/0047014c.md)

呼出元 8件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 0件 


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
    "004700ec",
    "00470114",
    "0047012c",
    "00470154"
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

### v16.0.0 [`004729c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/004729c0.md) FUN_004729c0

`initial_match_conflict` [`00472a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a00.md)

呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 0件 


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
    "00472630",
    "004729cc",
    "00472670",
    "00472a0c"
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

### v16.0.0 [`00472b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b6c.md) FUN_00472b6c

`initial_match_conflict` [`00472bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bac.md)

呼出元 4件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 0件 


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
    "00472ab8",
    "00472b7c",
    "00472af8",
    "00472bbc"
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

### v16.0.0 [`00479d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d78.md) FUN_00479d78

`initial_match_conflict` [`00479db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479db8.md)

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
    "00479d6c",
    "00479d88",
    "00479dac",
    "00479dc8"
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

### v16.0.0 [`0047b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b780.md) FUN_0047b780

`initial_match_conflict` [`0047b7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7c0.md)

呼出元 3件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00854630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/00854630.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 0件 


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
    "0047b4cc",
    "0047b78c",
    "0047b50c",
    "0047b7cc"
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

### v16.0.0 [`0047ed64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed64.md) FUN_0047ed64

`initial_match_conflict` [`0047eda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eda4.md)

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
    "0047ed5c",
    "0047ed74",
    "0047ed9c",
    "0047edb4"
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

### v16.0.0 [`0047ed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed6c.md) FUN_0047ed6c

`initial_match_conflict` [`0047edac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edac.md)

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
    "0047ed5c",
    "0047ed74",
    "0047ed9c",
    "0047edb4"
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

### v16.0.0 [`0048cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cca0.md) FUN_0048cca0

`initial_match_conflict` [`0048cce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cce0.md)

呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 0件 


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
    "0048c8f8",
    "0048cca8",
    "0048c938",
    "0048cce8"
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

### v16.0.0 [`00493938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493938.md) FUN_00493938

`initial_match_conflict` [`00493978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493978.md)

呼出元 1件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) · 呼出先 0件 


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
    "00493894",
    "00493940",
    "004938d4",
    "00493980"
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

### v16.0.0 [`0049d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0b8.md) FUN_0049d0b8

`initial_match_conflict` [`0049d0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d0f8.md)

呼出元 1件 [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 0件 


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
    "0049d048",
    "0049d0c0",
    "0049d088",
    "0049d100"
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

### v16.0.0 [`004cf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf478.md) FUN_004cf478

`initial_match_conflict` [`004cf4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf4b8.md)

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
    "004cea38",
    "004cf484",
    "004cea78",
    "004cf4c4"
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

### v16.0.0 [`004cf4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4ac.md) FUN_004cf4ac

`initial_match_conflict` [`004cf4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf4ec.md)

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
    "004cf484",
    "004cf4b4",
    "004cf4c4",
    "004cf4f4"
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

### v16.0.0 [`004f6914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6914.md) FUN_004f6914

`initial_match_conflict` [`004f6954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6954.md)

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
    "004f68d0",
    "004f691c",
    "004f6910",
    "004f695c"
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

### v16.0.0 [`0052f0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f0d8.md) FUN_0052f0d8

`initial_match_conflict` [`0052f118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f118.md)

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
    "0052f0b0",
    "0052f228",
    "0052f0f0",
    "0052f268"
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

### v16.0.0 [`0052f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f3c4.md) FUN_0052f3c4

`initial_match_conflict` [`0052f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f404.md)

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
    "0052f39c",
    "0052f514",
    "0052f3dc",
    "0052f554"
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

### v16.0.0 [`0052f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f6b0.md) FUN_0052f6b0

`initial_match_conflict` [`0052f6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f6f0.md)

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
    "0052f688",
    "0052f800",
    "0052f6c8",
    "0052f840"
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

### v16.0.0 [`0052f84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f84c.md) FUN_0052f84c

`initial_match_conflict` [`0052f88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f88c.md)

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
    "0052f800",
    "0052f85c",
    "0052f840",
    "0052f89c"
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

### v16.0.0 [`0052f854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f854.md) FUN_0052f854

`initial_match_conflict` [`0052f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f894.md)

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
    "0052f800",
    "0052f85c",
    "0052f840",
    "0052f89c"
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

### v16.0.0 [`0052f8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8c4.md) FUN_0052f8c4

`initial_match_conflict` [`0052f904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f904.md)

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
    "0052f85c",
    "0052f8e0",
    "0052f89c",
    "0052f920"
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

### v16.0.0 [`005300b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005300b4.md) FUN_005300b4

`initial_match_conflict` [`005300f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005300f4.md)

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
    "00530024",
    "005300e0",
    "00530064",
    "00530120"
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

### v16.0.0 [`0053028c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053028c.md) FUN_0053028c

`initial_match_conflict` [`005302cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302cc.md)

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
    "00530224",
    "005302a8",
    "00530264",
    "005302e8"
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

### v16.0.0 [`00530614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530614.md) FUN_00530614

`initial_match_conflict` [`00530654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530654.md)

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
    "005305d0",
    "00530624",
    "00530610",
    "00530664"
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

### v16.0.0 [`0053061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053061c.md) FUN_0053061c

`initial_match_conflict` [`0053065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053065c.md)

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
    "005305d0",
    "00530624",
    "00530610",
    "00530664"
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

### v16.0.0 [`00530784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530784.md) FUN_00530784

`initial_match_conflict` [`005307c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307c4.md)

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
    "00530764",
    "0053078c",
    "005307a4",
    "005307cc"
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

### v16.0.0 [`00530e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e64.md) FUN_00530e64

`initial_match_conflict` [`00530ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ea4.md)

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
    "00530de4",
    "00530e6c",
    "00530e24",
    "00530eac"
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

### v16.0.0 [`005310bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310bc.md) FUN_005310bc

`initial_match_conflict` [`005310fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005310fc.md)

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
    "0053107c",
    "005310cc",
    "005310bc",
    "0053110c"
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

### v16.0.0 [`005312c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312c4.md) FUN_005312c4

`initial_match_conflict` [`00531304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531304.md)

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
    "005311c4",
    "005312d4",
    "00531204",
    "00531314"
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

### v16.0.0 [`005314cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314cc.md) FUN_005314cc

`initial_match_conflict` [`0053150c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053150c.md)

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
    "005313cc",
    "00531514",
    "0053140c",
    "00531554"
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

### v16.0.0 [`005316cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005316cc.md) FUN_005316cc

`initial_match_conflict` [`0053170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053170c.md)

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
    "00531694",
    "005317dc",
    "005316d4",
    "0053181c"
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

### v16.0.0 [`0053189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053189c.md) FUN_0053189c

`initial_match_conflict` [`005318dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318dc.md)

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
    "00531864",
    "005318b4",
    "005318a4",
    "005318f4"
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

