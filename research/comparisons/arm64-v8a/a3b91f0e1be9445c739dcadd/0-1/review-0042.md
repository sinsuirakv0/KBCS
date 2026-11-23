# v15.7.2 → v15.7.3 · 追加調査 (42)

[一覧の目次](README.md)

<a id="review-71f832d77545c912125a3fba0526f566"></a>

### v15.7.3 [`00bc0f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f5c.md) FUN_00bc0f5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bc0e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0e94.md) · スコア 69.0 · 採用条件未達 · 順位差 67.0 / 67.0 · 

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
      "new": "00bc0e94",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-323293e39d6c94f200f0c3bcb2be2b37"></a>

### v15.7.3 [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) FUN_00bc0f64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bc0e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0e9c.md) · スコア 80.0 · 採用条件未達 · 順位差 45.0 / 45.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005490a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/005490a0.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005490b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/005490b0.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005490f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/005490f0.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00557f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557f58.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00557f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557f6c.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bc0e9c",
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
      "new": "005490a0",
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
      "new": "005490b0",
      "score": 35.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7dbb27ac7024c9f15c104f3b9b49aaf3"></a>

### v15.7.3 [`00bc145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc145c.md) FUN_00bc145c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bc1394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1394.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bc1394",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.3 [`00bcba10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba10.md) FUN_00bcba10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcb948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb948.md) · スコア 80.0 · 採用条件未達 · 順位差 17.948718 / 17.948718 · insufficient_independent_call_anchors
- 2. [`00bd07e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd07e0.md) · スコア 62.051282 · 採用条件未達 · 順位差 -17.948718 / -17.948718 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b7cc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc9c.md) · スコア 50.0 · 採用条件未達 · 順位差 29.230769 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bcb82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb82c.md) · スコア 46.153846 · 採用条件未達 · 順位差 4.615383999999999 / -33.846154 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b7342c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b7cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc48.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b7d040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d040.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00ba7e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e98.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 17.948718,
        "reverse_margin": 17.948718
      },
      "new": "00bcb948",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.948718,
        "reverse_margin": -17.948718
      },
      "new": "00bd07e0",
      "score": 62.051282
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5652173913043478,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 29.230769,
        "reverse_margin": -30.0
      },
      "new": "00b7cc9c",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b2402a06f889aa5234c440ea9d3069c5"></a>

### v15.7.3 [`00bcbe90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe90.md) FUN_00bcbe90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcbdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbdc8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd32b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcbdc8",
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
      "new": "00bd32b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9ab6a7f111b8fffcf46936ce318585d4"></a>

### v15.7.3 [`00bcec8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bcec8c.md) FUN_00bcec8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcebc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebc4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfe54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfe54.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bcff88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcff88.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd00a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd00a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcebc4",
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
      "new": "00bcfe54",
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
      "new": "00bcff88",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bdba3561c27225b0690058c288a16ac3"></a>

### v15.7.3 [`00bcf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf358.md) FUN_00bcf358

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf290.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa80.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd07b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd07b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcf290",
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
      "new": "00bcfa80",
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
      "new": "00bd07b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-90f44345eae79b81bae179debb8e083e"></a>

### v15.7.3 [`00bcfb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb48.md) FUN_00bcfb48

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf290.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa80.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd07b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd07b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcf290",
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
      "new": "00bcfa80",
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
      "new": "00bd07b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11295c137a59ab219b839276fd36a2cf"></a>

### v15.7.3 [`00bcff1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcff1c.md) FUN_00bcff1c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcebc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebc4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfe54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfe54.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bcff88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcff88.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd00a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd00a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcebc4",
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
      "new": "00bcfe54",
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
      "new": "00bcff88",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-565cd50b4d397b522315e2e6b5b48f39"></a>

### v15.7.3 [`00bd0050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0050.md) FUN_00bd0050

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcebc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebc4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfe54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfe54.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bcff88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcff88.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd00a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd00a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcebc4",
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
      "new": "00bcfe54",
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
      "new": "00bcff88",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6ef0cf8fc4474b51e93f367807638147"></a>

### v15.7.3 [`00bd0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0170.md) FUN_00bd0170

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcebc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebc4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfe54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfe54.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bcff88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcff88.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd00a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd00a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcebc4",
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
      "new": "00bcfe54",
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
      "new": "00bcff88",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4b79e4d3036ab1806256a3ecd67cb498"></a>

### v15.7.3 [`00bd0878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0878.md) FUN_00bd0878

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf290.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bcfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa80.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd07b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd07b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcf290",
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
      "new": "00bcfa80",
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
      "new": "00bd07b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v15.7.3 [`00bd08a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd08a8.md) FUN_00bd08a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd07e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd07e0.md) · スコア 80.0 · 採用条件未達 · 順位差 17.948718 / 17.948718 · insufficient_independent_call_anchors
- 2. [`00bcb948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb948.md) · スコア 62.051282 · 採用条件未達 · 順位差 -17.948718 / -17.948718 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bcb82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb82c.md) · スコア 41.538462 · 採用条件未達 · 順位差 -4.615383999999999 / -38.461538 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b7cc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc9c.md) · スコア 20.769231 · 採用条件未達 · 順位差 -29.230769 / -59.230768999999995 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bcf1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf1c8.md) · スコア 14.4 · 採用条件未達 · 順位差 14.4 / -65.6 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b7342c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b7cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cc48.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b7d040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d040.md) · スコア 9.230769 · 採用条件未達 · 順位差 0.0 / -70.769231 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 17.948718,
        "reverse_margin": 17.948718
      },
      "new": "00bd07e0",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
        ],
        "cfg_coverage": [
          0.5,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -17.948718,
        "reverse_margin": -17.948718
      },
      "new": "00bcb948",
      "score": 62.051282
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6923076923076923,
          0.6923076923076923
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
        "margin": -4.615383999999999,
        "reverse_margin": -38.461538
      },
      "new": "00bcb82c",
      "score": 41.538462
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-81e600c6418b331b96745e3cef1fa57b"></a>

### v15.7.3 [`00bd0af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0af0.md) FUN_00bd0af0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd0a28",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a34",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd2988",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-006fffb1a0f1f57c62ba4f404531dc05"></a>

### v15.7.3 [`00bd0afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0afc.md) FUN_00bd0afc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd0a34",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a28",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd2988",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b5876cbda4cfb31995c5b7f24b499dc6"></a>

### v15.7.3 [`00bd2a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a50.md) FUN_00bd2a50

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd2988",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a28",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a34",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d3684faedacdf1bef5bd4425585881a2"></a>

### v15.7.3 [`00bd2a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a5c.md) FUN_00bd2a5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd2994",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a28",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a34",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d91a52cea309bbbc7229ebf894d0963b"></a>

### v15.7.3 [`00bd3170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3170.md) FUN_00bd3170

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd30a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd30a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd43c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43c4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd4890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4890.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd3fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fb0.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bd03d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd03d4.md) · スコア 24.0 · 採用条件未達 · 順位差 0.0 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bcb9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00bd30a8",
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
      "new": "00bd43c4",
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
      "new": "00bd4890",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f665641e3273f84c5026135f8103c224"></a>

### v15.7.3 [`00bd3378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3378.md) FUN_00bd3378

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcbdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbdc8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd32b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bcbdc8",
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
      "new": "00bd32b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-21ade3879177973eb7a4288775899b4c"></a>

### v15.7.3 [`00bd3dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3dec.md) FUN_00bd3dec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd3d24",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a28",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a34",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6a2700b9c673b4fcc761191fd688f4f8"></a>

### v15.7.3 [`00bd3df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3df8.md) FUN_00bd3df8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd3d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d30.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd0a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a28.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd0a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a34.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00bd2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2988.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00bd2994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2994.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bd3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d24.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0050d0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d0d0.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 
- 8. [`005135f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/005135f8.md) · スコア 67.6667 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd3d30",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a28",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd0a34",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-72edb2929f69896504dd396a2dcf7dc6"></a>

### v15.7.3 [`00bd3e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e04.md) FUN_00bd3e04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd3d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d3c.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bd3d3c",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0bf7b3e7d4f39cc8cfb68263a08d0643"></a>

### v15.7.3 [`00bd448c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd448c.md) FUN_00bd448c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd30a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd30a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd43c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43c4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd4890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4890.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd3fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fb0.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bd03d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd03d4.md) · スコア 24.0 · 採用条件未達 · 順位差 0.0 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bcb9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00bd30a8",
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
      "new": "00bd43c4",
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
      "new": "00bd4890",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3e3f846e64ba38b600ae27ba4377ae97"></a>

### v15.7.3 [`00bd4958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4958.md) FUN_00bd4958

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd30a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd30a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd43c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43c4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bd4890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4890.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00bd3fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fb0.md) · スコア 70.0 · 採用条件未達 · 順位差 0.0 / -10.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bd03d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd03d4.md) · スコア 24.0 · 採用条件未達 · 順位差 0.0 / -56.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bcb9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md) · スコア 5.106383 · 採用条件未達 · 順位差 0.0 / -74.893617 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00bd30a8",
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
      "new": "00bd43c4",
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
      "new": "00bd4890",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-95b41f9321c95845f70e0b57b51c1771"></a>

### v15.7.3 [`00bd4cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cb0.md) FUN_00bd4cb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd4be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4be8.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bd4be8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7caf4208dbc6265fd21518949e11a850"></a>

### v15.7.3 [`00bd79e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd79e8.md) FUN_00bd79e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7928.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd7930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7930.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd7938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7938.md) · スコア 0.4706 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd7928",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7930",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7938",
      "score": 0.4706
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5921a4661672ec8328abe5868c3e662d"></a>

### v15.7.3 [`00bd79f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd79f0.md) FUN_00bd79f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7930.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00bd7928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7928.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd7938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7938.md) · スコア 0.4706 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd7930",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7928",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7938",
      "score": 0.4706
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b48e30bd14571b670ceda82f6437f44b"></a>

### v15.7.3 [`00bd79f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd79f8.md) FUN_00bd79f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7938.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00bd7938",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-afa2e5ff7986e6c613dab4712569cba3"></a>

### v15.7.3 [`00bd7c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c0c.md) FUN_00bd7c0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b4c.md) · スコア 80.0 · 採用条件未達 · 順位差 36.0 / 36.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd7b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b60.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bd7b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b70.md) · スコア 44.0 · 採用条件未達 · 順位差 -21.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bd7b4c",
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
      "new": "00bd7b60",
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
        "margin": -21.0,
        "reverse_margin": -36.0
      },
      "new": "00bd7b70",
      "score": 44.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-73550ba02f0de0793b1b7b88f7f43352"></a>

### v15.7.3 [`00bd7c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c20.md) FUN_00bd7c20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b60.md) · スコア 80.0 · 採用条件未達 · 順位差 36.0 / 15.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd7b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b70.md) · スコア 65.0 · 採用条件未達 · 順位差 21.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bd7b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b4c.md) · スコア 44.0 · 採用条件未達 · 順位差 -36.0 / -36.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 15.0
      },
      "new": "00bd7b60",
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
        "margin": 21.0,
        "reverse_margin": -15.0
      },
      "new": "00bd7b70",
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
      "new": "00bd7b4c",
      "score": 44.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56a113113925075b98dfb4f9d57935cb"></a>

### v15.7.3 [`00bd7c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c30.md) FUN_00bd7c30

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b4c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bd7b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b60.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bd7b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b70.md) · スコア 0.0 · 採用条件未達 · 順位差 -65.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "00bd7b4c",
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
      "new": "00bd7b60",
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
      "new": "00bd7b70",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6b733aa5e6462e8a38244fa92933abbc"></a>

### v15.7.3 [`00bd7d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d74.md) FUN_00bd7d74

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdad08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad08.md)

- 1. [`00bd7cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cb4.md) · スコア 84.0 · 採用条件未達 · 順位差 80.0 / 80.0 · 
- 2. [`00bd7cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cc0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd7ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7ccc.md) · スコア 1.0909 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd7cb4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7cc0",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7ccc",
      "score": 1.0909
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1a48541b3c267869ad78dd7e607bbe00"></a>

### v15.7.3 [`00bd7d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d80.md) FUN_00bd7d80

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cc0.md) · スコア 84.0 · 採用条件未達 · 順位差 80.0 / 80.0 · 
- 2. [`00bd7cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cb4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00bd7ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7ccc.md) · スコア 1.0909 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bd7cc0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7cb4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bd7ccc",
      "score": 1.0909
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1372b5002c42e066e820352f3c116f31"></a>

### v15.7.3 [`00bd7d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d8c.md) FUN_00bd7d8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bd7ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7ccc.md) · スコア 80.0 · 採用条件未達 · 順位差 21.818182 / 21.818182 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bd74a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74a8.md) · スコア 58.181818 · 採用条件未達 · 順位差 58.181818 / -21.818182 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
      "new": "00bd7ccc",
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
      "new": "00bd74a8",
      "score": 58.181818
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-720740d7949a41d5c3aad9967c6cc2a8"></a>

### v15.7.3 [`00bd7ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7ff4.md) FUN_00bd7ff4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdacd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdacd8.md)

- 1. [`00bd7f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7f34.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00bd7f34",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7cd726866e80200c4c5d96aed6cbf1c5"></a>

### v15.7.3 [`00bdacd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdacd8.md) FUN_00bdacd8

`competing_candidates` 

呼出元 1件 [`00bd7ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7ff4.md) · 呼出先 0件 

- 1. [`00bdac18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdac18.md) · スコア 30.0 · 採用条件未達 · 順位差 30.0 / 30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bdac48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdac48.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 30.0,
        "reverse_margin": 30.0
      },
      "new": "00bdac18",
      "score": 30.0
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
        "margin": -80.0,
        "reverse_margin": -30.0
      },
      "new": "00bdac48",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e4c536aa5a8f3b95d3aaaa488626f0f5"></a>

### v15.7.3 [`00bdad08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad08.md) FUN_00bdad08

`competing_candidates` 

呼出元 1件 [`00bd7d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d74.md) · 呼出先 0件 

- 1. [`00bdac48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdac48.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · insufficient_independent_call_anchors
- 2. [`00bdac18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdac18.md) · スコア 0.0 · 採用条件未達 · 順位差 -30.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bdac48",
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
        "margin": -30.0,
        "reverse_margin": -80.0
      },
      "new": "00bdac18",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-45c9bbd04f73560cdf633855c26f36a4"></a>

### v15.7.3 [`00bdae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae44.md) FUN_00bdae44

`competing_candidates` 

呼出元 1件 [`0092e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092e/0092e43c.md) · 呼出先 1件 [`00932008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/00932008.md)

- 1. [`00bdad84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad84.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00bdad84",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-175c2fa2f10fab1dcb812a139aaab283"></a>

### v15.7.3 [`00bdaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf60.md) FUN_00bdaf60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd020.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf020.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1020.md) · スコア 68.0 · 採用条件未達 · 順位差 68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdaed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaed0.md) · スコア 56.0 · 採用条件未達 · 順位差 -24.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bdaeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaeb0.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.0 / -68.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bdb020",
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
      "new": "00bdd020",
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
      "new": "00bdf020",
      "score": 68.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-af551ffdc9bcfc523b7f8ea71b92e6b3"></a>

### v15.7.3 [`00bdaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf80.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`004182d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004182d0.md) · 呼出先 1件 [`010a5000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5000.md)

- 1. [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd030.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf030.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1030.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdaed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaed0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdaeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaeb0.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bdb030",
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
      "new": "00bdd030",
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
      "new": "00bdf030",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-493bc7c0cafd7a3fdce721e482be366b"></a>

### v15.7.3 [`00bdca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca40.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`004d9b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9b40.md) · 呼出先 1件 [`010a5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5188.md)

- 1. [`00bdcaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcaf0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdeaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeaf0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0af0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bdc990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc990.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdcaf0",
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
      "new": "00bdeaf0",
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
      "new": "00be0af0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-369e773b5968a4aa81960f08a71081dc"></a>

### v15.7.3 [`00bdd2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2f0.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`0055a228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a228.md) · 呼出先 1件 [`010a5280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5280.md)

- 1. [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be13a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd240.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd250.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb3a0",
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
      "new": "00bdd3a0",
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
      "new": "00bdf3a0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-20610acd66505e1b70775e210e643544"></a>

### v15.7.3 [`00bdd300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd300.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 2件 [`0055a2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a2b8.md) [`0055a2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a2cc.md) · 呼出先 1件 [`010a5288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5288.md)

- 1. [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be13b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd240.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd250.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb3b0",
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
      "new": "00bdd3b0",
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
      "new": "00bdf3b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-baa086e88b81970aa4237a49f10a2711"></a>

### v15.7.3 [`00bdd350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd350.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`0055a44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a44c.md) · 呼出先 1件 [`010a52b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a52b0.md)

- 1. [`00bdb400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb400.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd400.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf400.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1400.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2a0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb400",
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
      "new": "00bdd400",
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
      "new": "00bdf400",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2942390f31c43d78893597158e4f541b"></a>

### v15.7.3 [`00bdd590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd590.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`0056e928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e928.md) · 呼出先 1件 [`010a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c0.md)

- 1. [`00bdb640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4e0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4f0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb640",
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
      "new": "00bdd640",
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
      "new": "00bdf640",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6f14d1dd92774579950f09743cbc08d6"></a>

### v15.7.3 [`00bdd5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd5a0.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`0056e930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e930.md) · 呼出先 1件 [`010a53c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c8.md)

- 1. [`00bdd4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bdd4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4f0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -80.0,
        "reverse_margin": 0.0
      },
      "new": "00bdd4e0",
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
      "new": "00bdd4f0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0cd38fc8b22d522a4846f70741169c47"></a>

### v15.7.3 [`00bdd600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd600.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`0056ec30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056ec30.md) · 呼出先 1件 [`010a53f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53f8.md)

- 1. [`00bdb6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd6b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf6b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be16b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be16b0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd550.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb6b0",
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
      "new": "00bdd6b0",
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
      "new": "00bdf6b0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0d1a8fa252faeeb032973136a0e1c8f"></a>

### v15.7.3 [`00bdda80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda80.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) · 呼出先 1件 [`010a5558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5558.md)

- 1. [`00bdbb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdfb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb30.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b30.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9d0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdbb30",
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
      "new": "00bddb30",
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
      "new": "00bdfb30",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-98397d2e5ac546207808044b8e37d5c4"></a>

### v15.7.3 [`010a5000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5000.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`00bdaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf80.md) · 呼出先 0件 

- 1. [`010a5000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5000.md) · スコア 79.0 · 採用条件未達 · 順位差 79.0 / 79.0 · 

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

<a id="review-778aa28f96e4290b5ede4589eed899eb"></a>

### v15.7.3 [`010a5148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5148.md) &lt;EXTERNAL&gt;::closedir

`competing_candidates` 

呼出元 1件 [`004d9024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d9/004d9024.md) · 呼出先 0件 

- 1. [`010a5148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5148.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-454ea1b4998b65b3c44cb4f31070f170"></a>

### v15.7.3 [`010a5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5188.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`00bdca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca40.md) · 呼出先 0件 

- 1. [`010a5188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5188.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-7116aa8a9f15e64a4138582671617467"></a>

### v15.7.3 [`010a5280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5280.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`00bdd2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2f0.md) · 呼出先 0件 

- 1. [`010a5280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5280.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5288.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-4b53a61a8a5d63727eb30d71a18ff9ab"></a>

### v15.7.3 [`010a5288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5288.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 1件 [`00bdd300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd300.md) · 呼出先 0件 

- 1. [`010a5288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5288.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5280.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-f32619cf0e26ba5a06f511443e783d6c"></a>

### v15.7.3 [`010a52b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a52b0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`00bdd350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd350.md) · 呼出先 0件 

- 1. [`010a52b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a52b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-abca668f54c183afe897923895035538"></a>

### v15.7.3 [`010a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c0.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`00bdd590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd590.md) · 呼出先 0件 

- 1. [`010a53c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53c0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-d85338e9dff75fd35ad5a07a317a7416"></a>

### v15.7.3 [`010a53c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c8.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`00bdd5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd5a0.md) · 呼出先 0件 

- 1. [`010a53c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53c8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53c0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-4763af9b4498a73f118da82552a578b8"></a>

### v15.7.3 [`010a53f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53f8.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`00bdd600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd600.md) · 呼出先 0件 

- 1. [`010a53f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-94465394a1bee199693c143fcb45422d"></a>

### v15.7.3 [`010a5558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5558.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`00bdda80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda80.md) · 呼出先 0件 

- 1. [`010a5558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5558.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

### v15.7.2 [`00421b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b38.md) FUN_00421b38

`initial_match_conflict` [`00421b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b38.md)

呼出元 1件 [`0081f58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f58c.md) · 呼出先 0件 


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
    "00421ad4",
    "00421b40",
    "00421ad4",
    "00421b40"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00444fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444fc4.md) FUN_00444fc4

`initial_match_conflict` [`00444fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fc4.md)

呼出元 6件 [`006369bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00637/00637320.md) [`00665a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00665/00665a98.md) [`006abca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ab/006abca0.md) [`008308f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00830/008308f0.md) · 呼出先 0件 


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
    "00444ee4",
    "00444fd4",
    "00444ee4",
    "00444fd4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0044d24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d24c.md) FUN_0044d24c

`initial_match_conflict` [`0044d24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d24c.md)

呼出元 2件 [`0078cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0078c/0078cd14.md) [`008e68f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e6/008e68f8.md) · 呼出先 0件 


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
    "0044d208",
    "0044d254"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00456ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00456/00456ee0.md) FUN_00456ee0

`initial_match_conflict` [`00456ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ee0.md)

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
    "00456ed4",
    "00456ef0"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0045becc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045becc.md) FUN_0045becc

`initial_match_conflict` [`0045becc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045becc.md)

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
    "0045bec4",
    "0045bedc"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0045bed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bed4.md) FUN_0045bed4

`initial_match_conflict` [`0045bed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bed4.md)

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
    "0045bec4",
    "0045bedc"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00470aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470aa0.md) FUN_00470aa0

`initial_match_conflict` [`00470aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470aa0.md)

呼出元 1件 [`00467098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467098.md) · 呼出先 0件 


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
    "004709fc",
    "00470aa8",
    "004709fc",
    "00470aa8"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`004ac5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ac/004ac5e0.md) FUN_004ac5e0

`initial_match_conflict` [`004ac5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac5e0.md)

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
    "004abba0",
    "004ac5ec"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`004ac614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ac/004ac614.md) FUN_004ac614

`initial_match_conflict` [`004ac614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac614.md)

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
    "004ac5ec",
    "004ac61c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`004d3a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d3/004d3a7c.md) FUN_004d3a7c

`initial_match_conflict` [`004d3a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3a7c.md)

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
    "004d3a38",
    "004d3a84"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050c240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c240.md) FUN_0050c240

`initial_match_conflict` [`0050c240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c240.md)

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
    "0050c218",
    "0050c390"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050c52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c52c.md) FUN_0050c52c

`initial_match_conflict` [`0050c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c52c.md)

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
    "0050c504",
    "0050c67c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050c818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c818.md) FUN_0050c818

`initial_match_conflict` [`0050c818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c818.md)

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
    "0050c7f0",
    "0050c968"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050c9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c9b4.md) FUN_0050c9b4

`initial_match_conflict` [`0050c9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9b4.md)

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
    "0050c968",
    "0050c9c4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050c9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050c9bc.md) FUN_0050c9bc

`initial_match_conflict` [`0050c9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9bc.md)

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
    "0050c968",
    "0050c9c4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050ca2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050c/0050ca2c.md) FUN_0050ca2c

`initial_match_conflict` [`0050ca2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca2c.md)

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
    "0050c9c4",
    "0050ca48"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050d21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d21c.md) FUN_0050d21c

`initial_match_conflict` [`0050d21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d21c.md)

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
    "0050d18c",
    "0050d248"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050d3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d3f4.md) FUN_0050d3f4

`initial_match_conflict` [`0050d3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d3f4.md)

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
    "0050d38c",
    "0050d410"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050d77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d77c.md) FUN_0050d77c

`initial_match_conflict` [`0050d77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d77c.md)

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
    "0050d738",
    "0050d78c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050d784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d784.md) FUN_0050d784

`initial_match_conflict` [`0050d784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d784.md)

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
    "0050d738",
    "0050d78c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050d8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050d8ec.md) FUN_0050d8ec

`initial_match_conflict` [`0050d8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8ec.md)

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
    "0050d8cc",
    "0050d8f4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050dfcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050d/0050dfcc.md) FUN_0050dfcc

`initial_match_conflict` [`0050dfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfcc.md)

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
    "0050df4c",
    "0050dfd4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050e224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e224.md) FUN_0050e224

`initial_match_conflict` [`0050e224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e224.md)

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
    "0050e1e4",
    "0050e234"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050e42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e42c.md) FUN_0050e42c

`initial_match_conflict` [`0050e42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e42c.md)

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
    "0050e32c",
    "0050e43c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050e634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e634.md) FUN_0050e634

`initial_match_conflict` [`0050e634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e634.md)

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
    "0050e534",
    "0050e67c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050e834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050e834.md) FUN_0050e834

`initial_match_conflict` [`0050e834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e834.md)

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
    "0050e774",
    "0050e84c",
    "0050e774",
    "0050e84c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050ea04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ea04.md) FUN_0050ea04

`initial_match_conflict` [`0050ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea04.md)

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
    "0050e9cc",
    "0050ea1c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050ed1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ed1c.md) FUN_0050ed1c

`initial_match_conflict` [`0050ed1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ed1c.md)

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
    "0050ecac",
    "0050edd4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050ee84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050e/0050ee84.md) FUN_0050ee84

`initial_match_conflict` [`0050ee84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee84.md)

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
    "0050ee5c",
    "0050ee8c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050f18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050f/0050f18c.md) FUN_0050f18c

`initial_match_conflict` [`0050f18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f18c.md)

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
    "0050f244",
    "0050ef84",
    "0050f244"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050f670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050f/0050f670.md) FUN_0050f670

`initial_match_conflict` [`0050f670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f670.md)

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
    "0050f728",
    "0050f62c",
    "0050f728"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050fbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050f/0050fbb0.md) FUN_0050fbb0

`initial_match_conflict` [`0050fbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fbb0.md)

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
    "0050fa98",
    "0050fbb8",
    "0050fa98",
    "0050fbb8"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050fc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050f/0050fc54.md) FUN_0050fc54

`initial_match_conflict` [`0050fc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fc54.md)

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
    "0050fbb8",
    "0050fc5c"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0050fea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050f/0050fea0.md) FUN_0050fea0

`initial_match_conflict` [`0050fea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fea0.md)

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
    "0050fea8",
    "0050fe60",
    "0050fea8"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00510c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00510/00510c68.md) FUN_00510c68

`initial_match_conflict` [`00510c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c68.md)

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
    "00510c3c",
    "00510c70"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00510ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00510/00510ef8.md) FUN_00510ef8

`initial_match_conflict` [`00510ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510ef8.md)

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
    "00510dc0",
    "00510f14"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`005110a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/005110a8.md) FUN_005110a8

`initial_match_conflict` [`005110a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005110a8.md)

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
    "005110a4",
    "005110e0"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`005110e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/005110e4.md) FUN_005110e4

`initial_match_conflict` [`005110e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005110e4.md)

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
    "005110e0",
    "005110f4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`00511118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/00511118.md) FUN_00511118

`initial_match_conflict` [`00511118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511118.md)

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
    "005110f4",
    "00511124"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`005111c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/005111c0.md) FUN_005111c0

`initial_match_conflict` [`005111c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005111c0.md)

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
    "00511164",
    "005111c8"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`005112ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/005112ec.md) FUN_005112ec

`initial_match_conflict` [`005112ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005112ec.md)

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
    "005111c8",
    "005112f4"
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
  "pseudocode_state": "text_equal",
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

### v15.7.2 [`0051178c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00511/0051178c.md) FUN_0051178c

`initial_match_conflict` [`0051178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/0051178c.md)

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
    "0051175c",
    "0051179c"
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
  "pseudocode_state": "text_equal",
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

