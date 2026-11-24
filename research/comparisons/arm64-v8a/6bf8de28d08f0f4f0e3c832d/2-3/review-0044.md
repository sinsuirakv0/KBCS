# v16.0.2 → v16.0.3 · 追加調査 (44)

[一覧の目次](README.md)

<a id="review-a1d8b05e4d24570364eadc9e45bbe3b0"></a>

### v16.0.2 [`00b342ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b342ec.md) FUN_00b342ec

`competing_candidates` 

呼出元 2件 [`00b356a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b356a4.md) [`00b36f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36f10.md) · 呼出先 0件 

- 1. [`00561344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561344.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00571b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b28.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00575718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00575748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575748.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`0058367c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058367c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`0058cfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cfe0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00b352e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b352e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`005836ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836ac.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00561344",
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
      "new": "00571b28",
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
      "new": "00575718",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9d43512b91a71b3fa7562faa9a582374"></a>

### v16.0.2 [`00b34efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34efc.md) FUN_00b34efc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b35ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35ef0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00b35ef0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3191e62a2a25a6cede0ba45bd817d198"></a>

### v16.0.2 [`00b34f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34f40.md) FUN_00b34f40

`competing_candidates` 

呼出元 0件  · 呼出先 15件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00b35450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35450.md)

- 1. [`00b35f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35f34.md) · スコア 62.246914 · 採用条件未達 · 順位差 56.355846 / 56.228395 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0087bc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087bc5c.md) · スコア 5.891068 · 採用条件未達 · 順位差 -56.355846 / -43.157952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00745e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745e2c.md) · スコア 2.509478 · 採用条件未達 · 順位差 -59.737435999999995 / 2.509478 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0089b55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089b/0089b55c.md) · スコア 2.0 · 採用条件未達 · 順位差 -60.246914 / -9.658915 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0087cc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cc48.md) · スコア 1.234568 · 採用条件未達 · 順位差 -61.012345999999994 / 1.234568 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) · スコア 0.818082 · 採用条件未達 · 順位差 -61.428832 / -73.234434 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0087b30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b30c.md) · スコア 0.740741 · 採用条件未達 · 順位差 -61.506173 / 0.740741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0087ba14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087ba14.md) · スコア 0.740741 · 採用条件未達 · 順位差 -61.506173 / 0.740741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6707818930041153,
          0.6707818930041153
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
        "margin": 56.355846,
        "reverse_margin": 56.228395
      },
      "new": "00b35f34",
      "score": 62.246914
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08641975308641975,
          0.09722222222222222
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.03529411764705882
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -56.355846,
        "reverse_margin": -43.157952
      },
      "new": "0087bc5c",
      "score": 5.891068
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03292181069958848,
          0.03162055335968379
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.030612244897959183
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -59.737435999999995,
        "reverse_margin": 2.509478
      },
      "new": "00745e2c",
      "score": 2.509478
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5bd1b274450c8ab350adf0aa6fc25797"></a>

### v16.0.2 [`00b353ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b353ec.md) FUN_00b353ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b363e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b363e0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b363e0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0d25a8dc385dcef6ec057ee8fc4e3278"></a>

### v16.0.2 [`00b35408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35408.md) FUN_00b35408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b363fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b363fc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00b363e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b363e0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00b36408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36408.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 4. [`00b35f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35f34.md) · スコア 0.0494 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b363fc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b363e0",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b36408",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-54ff5ee099a6c30f5ac69fc6ecd06e65"></a>

### v16.0.2 [`00b35414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35414.md) FUN_00b35414

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b36408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36408.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`00b363fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b363fc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 3. [`00b363e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b363e0.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 4. [`00b35f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35f34.md) · スコア 0.0165 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b36408",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b363fc",
      "score": 1.3333
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b363e0",
      "score": 0.5714
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4080c309fb90d722fbfe7c7547d37351"></a>

### v16.0.2 [`00b35440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35440.md) FUN_00b35440

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b36434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36434.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 50.0
      },
      "new": "00b36434",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-30499cea06c2a0064ea1bd519046ba77"></a>

### v16.0.2 [`00b35450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35450.md) FUN_00b35450

`competing_candidates` 

呼出元 1件 [`00b34f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34f40.md) · 呼出先 0件 

- 1. [`00b36444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36444.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`00b36434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36434.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b36444",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b36434",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-240bf07c5bfb195f8afa87aa89566e17"></a>

### v16.0.2 [`00b3567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b3567c.md) FUN_00b3567c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b36670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36670.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b36670",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e72507ca26dac5848ded6168e57df5f4"></a>

### v16.0.2 [`00b35698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35698.md) FUN_00b35698

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b3668c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b3668c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00b36670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36670.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b3668c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b36670",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ca0c500901bf90828798ed493d80bce0"></a>

### v16.0.2 [`00b372e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b372e0.md) FUN_00b372e0

`competing_candidates` 

呼出元 1件 [`00b38f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38f24.md) · 呼出先 0件 

- 1. [`00561344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561344.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00571b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b28.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00575718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575718.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00575748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575748.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`0058367c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058367c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`0058cfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cfe0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00b382d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b382d4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`005836ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836ac.md) · スコア 71.428571 · 採用条件未達 · 順位差 -8.571428999999995 / -8.571428999999995 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00561344",
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
      "new": "00571b28",
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
      "new": "00575718",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca7abab7174eaea9e1b03d29adc5189e"></a>

### v16.0.2 [`00b37310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37310.md) FUN_00b37310

`competing_candidates` 

呼出元 1件 [`00b38f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38f24.md) · 呼出先 0件 

- 1. [`00579800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579800.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`0087c33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c33c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00b38304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38304.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 4. [`0079ced8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079ced8.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -2.4675320000000056 · cfg_coverage, insufficient_independent_call_anchors
- 5. [`0079cdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cdf0.md) · スコア 73.896104 · 採用条件未達 · 順位差 -6.103896000000006 / 0.0 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 6. [`0079cfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cfc0.md) · スコア 72.077922 · 採用条件未達 · 順位差 -7.922077999999999 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009a71d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a71d4.md) · スコア 70.25974 · 採用条件未達 · 順位差 -9.740260000000006 / -9.740260000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009a72bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a72bc.md) · スコア 57.159091 · 採用条件未達 · 順位差 -22.840909000000003 / -22.840909000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00579800",
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
      "new": "0087c33c",
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
      "new": "00b38304",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0dd4d5660f1cc5b90845551b36336d3"></a>

### v16.0.2 [`00b39f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39f3c.md) FUN_00b39f3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b3af30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3af30.md) · スコア 80.0 · 採用条件未達 · 順位差 36.115942 / 36.115942 · insufficient_independent_call_anchors
- 2. [`00584be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584be4.md) · スコア 43.884058 · 採用条件未達 · 順位差 -36.115942 / -36.115942 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b38388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38388.md) · スコア 40.233918 · 採用条件未達 · 順位差 -39.766082 / 40.233918 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008b83d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b83d0.md) · スコア 8.076923 · 採用条件未達 · 順位差 -71.923077 / 8.076923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00586eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586eac.md) · スコア 4.615385 · 採用条件未達 · 順位差 -75.384615 / 4.615385 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 36.115942,
        "reverse_margin": 36.115942
      },
      "new": "00b3af30",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6444444444444445,
          0.6444444444444445
        ],
        "cfg_coverage": [
          0.3,
          0.2608695652173913
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -36.115942,
        "reverse_margin": -36.115942
      },
      "new": "00584be4",
      "score": 43.884058
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7555555555555555,
          0.5964912280701754
        ],
        "cfg_coverage": [
          0.3,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -39.766082,
        "reverse_margin": 40.233918
      },
      "new": "00b38388",
      "score": 40.233918
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ef7742c3ccd4cc8e9f4a1b2a6ecf5144"></a>

### v16.0.2 [`00b3a408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3a408.md) FUN_00b3a408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00579800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579800.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`0087c33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c33c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00b3b3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3b3fc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · insufficient_independent_call_anchors
- 4. [`0079ced8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079ced8.md) · スコア 75.714286 · 採用条件未達 · 順位差 -4.285713999999999 / -2.4675320000000056 · cfg_coverage, insufficient_independent_call_anchors
- 5. [`0079cdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cdf0.md) · スコア 73.896104 · 採用条件未達 · 順位差 -6.103896000000006 / 0.0 · instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 6. [`0079cfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cfc0.md) · スコア 72.077922 · 採用条件未達 · 順位差 -7.922077999999999 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009a71d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a71d4.md) · スコア 70.25974 · 採用条件未達 · 順位差 -9.740260000000006 / -9.740260000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009a72bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a72bc.md) · スコア 57.159091 · 採用条件未達 · 順位差 -22.840909000000003 / -22.840909000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00579800",
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
      "new": "0087c33c",
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
        "reverse_margin": 80.0
      },
      "new": "00b3b3fc",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6b67cdd675951d07087fb0e62690bae8"></a>

### v16.0.2 [`00b3d6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d6b4.md) FUN_00b3d6b4

`competing_candidates` 

呼出元 3件 [`00a95838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a95/00a95838.md) [`00b3e870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e870.md) [`00b3f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f8dc.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c7638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7638.md) [`005cc9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00728840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728840.md)

- 1. [`00b3e6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e6a8.md) · スコア 77.145833 · 採用条件未達 · 順位差 72.220682 / 72.220682 · instruction_coverage
- 2. [`00b40574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40574.md) · スコア 4.925151 · 採用条件未達 · 順位差 -72.220682 / 4.925151 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00605644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605644.md) · スコア 4.05231 · 採用条件未達 · 順位差 -73.09352299999999 / 4.05231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`00783e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783e1c.md) · スコア 4.0 · 採用条件未達 · 順位差 -73.145833 / 4.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 5. [`00b3f1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f1c8.md) · スコア 3.861331 · 採用条件未達 · 順位差 -73.284502 / 3.861331 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) · スコア 2.432692 · 採用条件未達 · 順位差 -74.713141 / -80.951923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005c8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c8bb0.md) · スコア 2.0 · 採用条件未達 · 順位差 -75.145833 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006d9108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9108.md) · スコア 2.0 · 採用条件未達 · 順位差 -75.145833 / -71.554252 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8524305555555556,
          0.8524305555555556
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage"
        ],
        "margin": 72.220682,
        "reverse_margin": 72.220682
      },
      "new": "00b3e6a8",
      "score": 77.145833
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03819444444444445,
          0.1527777777777778
        ],
        "cfg_coverage": [
          0.03167420814479638,
          0.12280701754385964
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -72.220682,
        "reverse_margin": 4.925151
      },
      "new": "00b40574",
      "score": 4.925151
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.001736111111111111,
          0.0008718395815170009
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
          "already_matched_elsewhere"
        ],
        "margin": -73.09352299999999,
        "reverse_margin": 4.05231
      },
      "new": "00605644",
      "score": 4.05231
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-270ee66dcfdc475f65c930b4b75febd8"></a>

### v16.0.2 [`00b3dfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3dfb4.md) FUN_00b3dfb4

`competing_candidates` 

呼出元 1件 [`00b3e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e1d4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00b3efa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3efa8.md) · スコア 63.235294 · 採用条件未達 · 順位差 60.147059000000006 / 60.147059000000006 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006c5518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5518.md) · スコア 3.088235 · 採用条件未達 · 順位差 -60.147059000000006 / 3.088235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00793b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793b80.md) · スコア 3.088235 · 採用条件未達 · 順位差 -60.147059000000006 / 3.088235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00806fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/00806fa0.md) · スコア 2.43844 · 採用条件未達 · 順位差 -60.796854 / 2.43844 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a6a58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6a58c.md) · スコア 1.764706 · 採用条件未達 · 順位差 -61.470588000000006 / 1.764706 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a6aac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6aac8.md) · スコア 1.764706 · 採用条件未達 · 順位差 -61.470588000000006 / 1.764706 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a66e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md) · スコア 0.15748 · 採用条件未達 · 順位差 -63.077814000000004 / -76.59842599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0048e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e0a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -63.235294 / -58.470588 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7205882352941176,
          0.7205882352941176
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
        "margin": 60.147059000000006,
        "reverse_margin": 60.147059000000006
      },
      "new": "00b3efa8",
      "score": 63.235294
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.051470588235294115,
          0.05737704918032787
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
        "margin": -60.147059000000006,
        "reverse_margin": 3.088235
      },
      "new": "006c5518",
      "score": 3.088235
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.051470588235294115,
          0.14285714285714285
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
        "margin": -60.147059000000006,
        "reverse_margin": 3.088235
      },
      "new": "00793b80",
      "score": 3.088235
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6c39324011915f8bb2a7bbf77c6126d8"></a>

### v16.0.2 [`00b3f9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f9f8.md) FUN_00b3f9f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b409ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b409ec.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b409ec",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d0d6dd9e65a611ba76cb46686761e459"></a>

### v16.0.2 [`00b3fa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fa14.md) FUN_00b3fa14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b40a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40a08.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00b409ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b409ec.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b40a08",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b409ec",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-56c396827594259c3020655d41229cd1"></a>

### v16.0.2 [`00b3fb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fb54.md) FUN_00b3fb54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b40b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40b48.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b40b48",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-679a1e45c3cb9e4523627a2b999fc086"></a>

### v16.0.2 [`00b3fb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fb70.md) FUN_00b3fb70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b40b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40b64.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00b40b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40b48.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00b40b64",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00b40b48",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-36160bd20ee13329674054a90b61fb27"></a>

### v16.0.2 [`00b611d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611d4.md) FUN_00b611d4

`competing_candidates` 

呼出元 1件 [`00b608c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b608c4.md) · 呼出先 0件 

- 1. [`00b621c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621c8.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00b621c8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-336900f1fb48756ba7880a1ad42ba8e8"></a>

### v16.0.2 [`00b7fed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fed8.md) FUN_00b7fed8

`competing_candidates` 

呼出元 2件 [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7fed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fed8.md) · 呼出先 2件 [`00b7fed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fed8.md) [`00baafa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baafa8.md)

- 1. [`00b80ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80ecc.md) · スコア 81.58042 · 採用条件未達 · 順位差 81.58042 / 81.58042 · insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.993006993006993,
          0.993006993006993
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "insufficient_independent_call_anchors"
        ],
        "margin": 81.58042,
        "reverse_margin": 81.58042
      },
      "new": "00b80ecc",
      "score": 81.58042
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5c88bdbd32bb6709be7e895639011b82"></a>

### v16.0.2 [`00b9913c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9913c.md) FUN_00b9913c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b9a130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a130.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "00b9a130",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-05e411ff14afdb1642487bcc90769ffc"></a>

### v16.0.2 [`00bb66f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66f8.md) FUN_00bb66f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bb76ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb76ec.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bb76ec",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-50b0710486423dea368b6924b512b0f9"></a>

### v16.0.2 [`00bc1308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1308.md) FUN_00bc1308

`competing_candidates` [`00bc22fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc22fc.md)

呼出元 1件 [`00bc13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00bc1140",
    "00bc1314",
    "00bc2134",
    "00bc2308"
  ],
  "initial_reason": ""
}
~~~

<a id="review-d1dfc6d27f1d84a9baedc49d64660e46"></a>

### v16.0.2 [`00bc1310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1310.md) FUN_00bc1310

`competing_candidates` 

呼出元 1件 [`00bc13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md) · 呼出先 0件 

- 1. [`00bc2304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2304.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bc2304",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-778ecf69f9d1dd4d91de5ae813316aa3"></a>

### v16.0.2 [`00bca0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0d0.md) FUN_00bca0d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcb0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb0c4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bcb0c4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b5ac1f485a1e3c2f47f73c531935cbbf"></a>

### v16.0.2 [`00bca0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0ec.md) FUN_00bca0ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bcb0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb0e0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00bcb0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb0c4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00bcb0e0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00bcb0c4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8a9ec3a9148cb56ce2d32d1f25779f8b"></a>

### v16.0.2 [`00bca56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca56c.md) FUN_00bca56c

`competing_candidates` [`00bcb560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb560.md)

呼出元 1件 [`00bcc1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00bca53c",
    "00bca578",
    "00bcb530",
    "00bcb56c"
  ],
  "initial_reason": ""
}
~~~

<a id="review-8fb95fb9b9cfafb097485a5c297077e4"></a>

### v16.0.2 [`00bca574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca574.md) FUN_00bca574

`competing_candidates` 

呼出元 1件 [`00bcc1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md) · 呼出先 0件 

- 1. [`00bcb568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcb568.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00bcb568",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v16.0.2 [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) FUN_00be2304

`competing_candidates` 

呼出元 2件 [`00be22e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be22e8.md) [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) · 呼出先 4件 [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) [`00be90c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be90c4.md) [`00be9384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9384.md) [`00be94ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be94ac.md)

- 1. [`00be32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be32f8.md) · スコア 81.471366 · 採用条件未達 · 順位差 3.902025000000009 / 3.902025000000009 · insufficient_independent_call_anchors
- 2. [`00be4878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4878.md) · スコア 77.569341 · 採用条件未達 · 順位差 -3.902025000000009 / -3.902025000000009 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) · スコア 65.991189 · 採用条件未達 · 順位差 -15.480176999999998 / 65.991189 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3a30.md) · スコア 52.907489 · 採用条件未達 · 順位差 -28.563877000000005 / -28.554394000000002 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · スコア 30.443994 · 採用条件未達 · 順位差 -51.027372 / 30.443994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be6540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6540.md) · スコア 28.566246 · 採用条件未達 · 順位差 -52.905120000000004 / -52.895637 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be4fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) · スコア 19.028291 · 採用条件未達 · 順位差 -62.44307500000001 / 19.028291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be32f8",
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
      "new": "00be4878",
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
        "margin": -15.480176999999998,
        "reverse_margin": 65.991189
      },
      "new": "00be4144",
      "score": 65.991189
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) FUN_00be2a3c

`competing_candidates` 

呼出元 2件 [`00be2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a1c.md) [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) · 呼出先 4件 [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) [`00be97a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be97a0.md) [`00be9a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9a40.md) [`00be9b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9b68.md)

- 1. [`00be3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3a30.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.243772000000007 / 5.243772000000007 · insufficient_independent_call_anchors
- 2. [`00be6540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6540.md) · スコア 76.218111 · 採用条件未達 · 順位差 -5.243772000000007 / -5.243772000000007 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / 72.06278 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be32f8.md) · スコア 52.907489 · 採用条件未達 · 順位差 -28.554394000000002 / -28.563877000000005 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · スコア 31.287459 · 採用条件未達 · 順位差 -50.174424 / 31.287459 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be4878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4878.md) · スコア 29.282108 · 採用条件未達 · 順位差 -52.179775 / -52.189258 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) · スコア 18.951363 · 採用条件未達 · 順位差 -62.51052 / 18.951363 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 6.453533 · 採用条件未達 · 順位差 -75.00835000000001 / -73.189324 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be3a30",
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
      "new": "00be6540",
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
        "margin": -9.399102999999997,
        "reverse_margin": 72.06278
      },
      "new": "00be5e28",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) FUN_00be3884

`competing_candidates` 

呼出元 2件 [`00be3868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3868.md) [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) · 呼出先 4件 [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) [`00bea540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea540.md) [`00bea800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea800.md) [`00bea928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea928.md)

- 1. [`00be4878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4878.md) · スコア 81.471366 · 採用条件未達 · 順位差 3.902025000000009 / 3.902025000000009 · insufficient_independent_call_anchors
- 2. [`00be32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be32f8.md) · スコア 77.569341 · 採用条件未達 · 順位差 -3.902025000000009 / -3.902025000000009 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) · スコア 57.675975 · 採用条件未達 · 順位差 -23.795391000000002 / 57.675975 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3a30.md) · スコア 29.282108 · 採用条件未達 · 順位差 -52.189258 / -52.179775 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · スコア 28.920058 · 採用条件未達 · 順位差 -52.551308000000006 / 28.920058 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00be6540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6540.md) · スコア 27.0529 · 採用条件未達 · 順位差 -54.418466 / -54.408983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be4fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) · スコア 17.943418 · 採用条件未達 · 順位差 -63.527948 / 17.943418 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be4878",
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
      "new": "00be32f8",
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
          0.7296137339055794,
          0.7327586206896551
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -23.795391000000002,
        "reverse_margin": 57.675975
      },
      "new": "00be4144",
      "score": 57.675975
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) FUN_00be554c

`competing_candidates` 

呼出元 2件 [`00be552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be552c.md) [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) · 呼出先 4件 [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) [`00bec0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec0a8.md) [`00bec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec348.md) [`00bec470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec470.md)

- 1. [`00be6540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6540.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.243772000000007 / 5.243772000000007 · insufficient_independent_call_anchors
- 2. [`00be3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3a30.md) · スコア 76.218111 · 採用条件未達 · 順位差 -5.243772000000007 / -5.243772000000007 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) · スコア 68.348344 · 採用条件未達 · 順位差 -13.113539000000003 / 68.348344 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be56ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · スコア 29.053652 · 採用条件未達 · 順位差 -52.408231 / 29.053652 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00be32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be32f8.md) · スコア 28.566246 · 採用条件未達 · 順位差 -52.895637 / -52.905120000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be4878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4878.md) · スコア 27.0529 · 採用条件未達 · 順位差 -54.408983 / -54.418466 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) · スコア 18.597053 · 採用条件未達 · 順位差 -62.86483 / 18.597053 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 6.339074 · 採用条件未達 · 順位差 -75.122809 / -73.30378300000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be6540",
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
      "new": "00be3a30",
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
          0.8277310924369747,
          0.8491379310344828
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.113539000000003,
        "reverse_margin": 68.348344
      },
      "new": "00be5e28",
      "score": 68.348344
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-97f2919f4393313b21da4c64c3c446d7"></a>

### v16.0.2 [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) FUN_00be5c64

`competing_candidates` 

呼出元 2件 [`00be5c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c44.md) [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) · 呼出先 4件 [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) [`00bec76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec76c.md) [`00beca0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00beca0c.md) [`00becb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00becb34.md)

- 1. [`00be6c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6c58.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.656903 / 5.656903 · insufficient_independent_call_anchors
- 2. [`00be7a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7a88.md) · スコア 75.80498 · 採用条件未達 · 順位差 -5.656903 / -5.656903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be7370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7370.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00be81a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be81a0.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · スコア 16.643068 · 採用条件未達 · 順位差 -64.818815 / 16.643068 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be6c58",
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
      "new": "00be7a88",
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
          0.8851063829787233,
          0.896551724137931
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
      "new": "00be7370",
      "score": 68.419616
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) FUN_00be637c

`competing_candidates` 

呼出元 2件 [`00be635c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be635c.md) [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) · 呼出先 4件 [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) [`00bece30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bece30.md) [`00bed0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed0d0.md) [`00bed1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed1f8.md)

- 1. [`00be7370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7370.md) · スコア 81.461883 · 採用条件未達 · 順位差 2.0 / 2.0 · insufficient_independent_call_anchors
- 2. [`00be81a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be81a0.md) · スコア 79.461883 · 採用条件未達 · 順位差 -2.0 / -2.0 · insufficient_independent_call_anchors
- 3. [`00be7a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7a88.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be6c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6c58.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · スコア 18.449575 · 採用条件未達 · 順位差 -63.012308000000004 / 18.449575 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be7370",
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
      "new": "00be81a0",
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
      "new": "00be7a88",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) FUN_00be6a94

`competing_candidates` 

呼出元 2件 [`00be6a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a74.md) [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) · 呼出先 4件 [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) [`00bed4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed4f4.md) [`00bed794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed794.md) [`00bed8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed8bc.md)

- 1. [`00be7a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7a88.md) · スコア 81.461883 · 採用条件未達 · 順位差 5.656903 / 5.656903 · insufficient_independent_call_anchors
- 2. [`00be6c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6c58.md) · スコア 75.80498 · 採用条件未達 · 順位差 -5.656903 / -5.656903 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00be7370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7370.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be81a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be81a0.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 5. [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · スコア 18.449575 · 採用条件未達 · 順位差 -63.012308000000004 / 18.449575 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be7a88",
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
      "new": "00be6c58",
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
      "new": "00be7370",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) FUN_00be71ac

`competing_candidates` 

呼出元 2件 [`00be718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be718c.md) [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) · 呼出先 4件 [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) [`00bedbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bedbb8.md) [`00bede58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bede58.md) [`00bedf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bedf80.md)

- 1. [`00be81a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be81a0.md) · スコア 81.461883 · 採用条件未達 · 順位差 2.0 / 2.0 · insufficient_independent_call_anchors
- 2. [`00be7370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7370.md) · スコア 79.461883 · 採用条件未達 · 順位差 -2.0 / -2.0 · insufficient_independent_call_anchors
- 3. [`00be7a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be7/00be7a88.md) · スコア 72.06278 · 採用条件未達 · 順位差 -9.399102999999997 / -9.399102999999997 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00be6c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be6/00be6c58.md) · スコア 68.419616 · 採用条件未達 · 順位差 -13.042266999999995 / -13.042266999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · スコア 18.449575 · 採用条件未達 · 順位差 -63.012308000000004 / 18.449575 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00be81a0",
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
      "new": "00be7370",
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
      "new": "00be7a88",
      "score": 72.06278
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be90c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be90c4.md) FUN_00be90c4

`competing_candidates` 

呼出元 1件 [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) · 呼出先 1件 [`00be9384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9384.md)

- 1. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 51.758658 · 採用条件未達 · 順位差 -27.900433000000007 / -30.241342000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -30.295454999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -27.938312000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 44.545455 · 採用条件未達 · 順位差 -35.11363600000001 / -37.454545 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.453991 / -49.437757000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) · スコア 4.558081 · 採用条件未達 · 順位差 -75.10101 / 4.558081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bea0b8",
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
      "new": "00beb534",
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
      "new": "00beae58",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d02937a670110da3304727ee0154ad89"></a>

### v16.0.2 [`00be9384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9384.md) FUN_00be9384

`competing_candidates` 

呼出元 2件 [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) [`00be90c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be90c4.md) · 呼出先 0件 

- 1. [`00bea378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea378.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00beb118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb118.md) · スコア 54.054054 · 採用条件未達 · 順位差 -25.945946 / 54.054054 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bec5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / 45.135135 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beaa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beaa34.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 0.681818 · 採用条件未達 · 順位差 -79.318182 / -78.977273 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea4a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bea378",
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
      "new": "00beb7f4",
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
        "margin": -25.945946,
        "reverse_margin": 54.054054
      },
      "new": "00beb118",
      "score": 54.054054
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c61ae479ccf93662f42558ef5c9e7c26"></a>

### v16.0.2 [`00be94ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be94ac.md) FUN_00be94ac

`competing_candidates` 

呼出元 1件 [`00be2304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2304.md) · 呼出先 0件 

- 1. [`00bea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea4a0.md) · スコア 80.0 · 採用条件未達 · 順位差 4.303351000000006 / 4.303351000000006 · insufficient_independent_call_anchors
- 2. [`00beb91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb91c.md) · スコア 75.696649 · 採用条件未達 · 順位差 -4.303351000000006 / -4.303351000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb240.md) · スコア 40.977526 · 採用条件未達 · 順位差 -39.022474 / 40.977526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00beab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beab5c.md) · スコア 14.967358 · 採用条件未達 · 順位差 -65.032642 / -65.032642 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 9.911817 · 採用条件未達 · 順位差 -70.088183 / 9.911817 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bef638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md) · スコア 7.545788 · 採用条件未達 · 順位差 -72.454212 / 7.545788 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 0.31746 · 採用条件未達 · 順位差 -79.68254 / -79.341631 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 0.31746 · 採用条件未達 · 順位差 -79.68254 / -79.32539700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 4.303351000000006,
        "reverse_margin": 4.303351000000006
      },
      "new": "00bea4a0",
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
      "new": "00beb91c",
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
          0.4567901234567901,
          0.36633663366336633
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -39.022474,
        "reverse_margin": 40.977526
      },
      "new": "00beb240",
      "score": 40.977526
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be97a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be97a0.md) FUN_00be97a0

`competing_candidates` 

呼出元 1件 [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) · 呼出先 1件 [`00be9a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9a40.md)

- 1. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 79.642857 · 採用条件未達 · 順位差 3.2665500000000094 / 3.2665500000000094 · insufficient_independent_call_anchors
- 2. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 76.376307 · 採用条件未達 · 順位差 -3.2665500000000094 / -3.2665500000000094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 56.186371 · 採用条件未達 · 順位差 -23.456486000000005 / -25.813629 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 33.907982 · 採用条件未達 · 順位差 -45.73487500000001 / -48.092018 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.437757000000005 / -49.453991 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.437757000000005 / -49.453991 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 18.754355 · 採用条件未達 · 順位差 -60.888502 / -63.245644999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 12.440476 · 採用条件未達 · 順位差 -67.202381 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bea794",
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
      "new": "00bed09c",
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
      "new": "00bec9d8",
      "score": 56.186371
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6e723bc7c734c9cc69281727ffa7df28"></a>

### v16.0.2 [`00be9a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9a40.md) FUN_00be9a40

`competing_candidates` 

呼出元 2件 [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) [`00be97a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be97a0.md) · 呼出先 0件 

- 1. [`00beaa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beaa34.md) · スコア 80.0 · 採用条件未達 · 順位差 19.836199999999998 / 19.836199999999998 · insufficient_independent_call_anchors
- 2. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 60.1638 · 採用条件未達 · 順位差 -19.836199999999998 / -19.836199999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00becc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becc78.md) · スコア 49.63145 · 採用条件未達 · 順位差 -30.36855 / 49.63145 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bea378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea378.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bec5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / 11.343161 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 0.714286 · 採用条件未達 · 順位差 -79.285714 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea4a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.836199999999998,
        "reverse_margin": 19.836199999999998
      },
      "new": "00beaa34",
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
      "new": "00bed33c",
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
          0.45454545454545453,
          0.4838709677419355
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -30.36855,
        "reverse_margin": 49.63145
      },
      "new": "00becc78",
      "score": 49.63145
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00be9b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9b68.md) FUN_00be9b68

`competing_candidates` 

呼出元 1件 [`00be2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2a3c.md) · 呼出先 0件 

- 1. [`00beab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beab5c.md) · スコア 80.0 · 採用条件未達 · 順位差 2.6282719999999955 / 2.6282719999999955 · insufficient_independent_call_anchors
- 2. [`00bed464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed464.md) · スコア 77.371728 · 採用条件未達 · 順位差 -2.6282719999999955 / -2.6282719999999955 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00becda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becda0.md) · スコア 64.01178 · 採用条件未達 · 順位差 -15.988219999999998 / 64.01178 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bec6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec6dc.md) · スコア 33.150524 · 採用条件未達 · 順位差 -46.849476 / 33.150524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bef638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md) · スコア 16.773488 · 採用条件未達 · 順位差 -63.226512 / 16.773488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea4a0.md) · スコア 14.967358 · 採用条件未達 · 順位差 -65.032642 / -65.032642 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beaa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beaa34.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 2.6282719999999955,
        "reverse_margin": 2.6282719999999955
      },
      "new": "00beab5c",
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
      "new": "00bed464",
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
        "margin": -15.988219999999998,
        "reverse_margin": 64.01178
      },
      "new": "00becda0",
      "score": 64.01178
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-febf99101664128777266572c0d30fdb"></a>

### v16.0.2 [`00be9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9e64.md) FUN_00be9e64

`competing_candidates` 

呼出元 1件 [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) · 呼出先 1件 [`00bea124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea124.md)

- 1. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 82.0 · 採用条件未達 · 順位差 30.241342000000003 / 30.241342000000003 · insufficient_independent_call_anchors
- 2. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 51.758658 · 採用条件未達 · 順位差 -30.241342000000003 / -27.900433000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 51.758658 · 採用条件未達 · 順位差 -30.241342000000003 / -27.900433000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 30.768398 · 採用条件未達 · 順位差 -51.231601999999995 / -51.231601999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 23.32419 · 採用条件未達 · 順位差 -58.67581 / -58.67581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -67.202381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) · スコア 4.558081 · 採用条件未達 · 順位差 -77.441919 / 4.558081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 30.241342000000003,
        "reverse_margin": 30.241342000000003
      },
      "new": "00beae58",
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
      "new": "00bea0b8",
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
      "new": "00beb534",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bea540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea540.md) FUN_00bea540

`competing_candidates` 

呼出元 1件 [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) · 呼出先 1件 [`00bea800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea800.md)

- 1. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 79.659091 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 51.758658 · 採用条件未達 · 順位差 -27.900433000000007 / -30.241342000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -30.295454999999997 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.954546 / -27.938312000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 44.545455 · 採用条件未達 · 順位差 -35.11363600000001 / -37.454545 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 30.2051 · 採用条件未達 · 順位差 -49.453991 / -49.437757000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`009cce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cc/009cce28.md) · スコア 4.558081 · 採用条件未達 · 順位差 -75.10101 / 4.558081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bea0b8",
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
      "new": "00beb534",
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
      "new": "00beae58",
      "score": 51.758658
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6814d252f0a568b3b2a5d02bd6f7d30b"></a>

### v16.0.2 [`00bea800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea800.md) FUN_00bea800

`competing_candidates` 

呼出元 2件 [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) [`00bea540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea540.md) · 呼出先 0件 

- 1. [`00bea378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea378.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00beb118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb118.md) · スコア 54.054054 · 採用条件未達 · 順位差 -25.945946 / 54.054054 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bec5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / 45.135135 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beaa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beaa34.md) · スコア 11.343161 · 採用条件未達 · 順位差 -68.656839 / -68.656839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 0.681818 · 採用条件未達 · 順位差 -79.318182 / -78.977273 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beb91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb91c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00bea378",
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
      "new": "00beb7f4",
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
        "margin": -25.945946,
        "reverse_margin": 54.054054
      },
      "new": "00beb118",
      "score": 54.054054
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bd8d4edf9def3086d8dd4b3c1ff0c78a"></a>

### v16.0.2 [`00bea928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea928.md) FUN_00bea928

`competing_candidates` 

呼出元 1件 [`00be3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3884.md) · 呼出先 0件 

- 1. [`00beb91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb91c.md) · スコア 80.0 · 採用条件未達 · 順位差 4.303351000000006 / 4.303351000000006 · insufficient_independent_call_anchors
- 2. [`00bea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea4a0.md) · スコア 75.696649 · 採用条件未達 · 順位差 -4.303351000000006 / -4.303351000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beb240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb240.md) · スコア 43.158887 · 採用条件未達 · 順位差 -36.841113 / 43.158887 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 9.911817 · 採用条件未達 · 順位差 -70.088183 / 9.911817 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bef638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md) · スコア 7.545788 · 採用条件未達 · 順位差 -72.454212 / 7.545788 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.659091 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -82.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 4.303351000000006,
        "reverse_margin": 4.303351000000006
      },
      "new": "00beb91c",
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
      "new": "00bea4a0",
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
          0.5128205128205128,
          0.39603960396039606
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -36.841113,
        "reverse_margin": 43.158887
      },
      "new": "00beb240",
      "score": 43.158887
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00beac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beac1c.md) FUN_00beac1c

`competing_candidates` 

呼出元 1件 [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) · 呼出先 1件 [`00beaedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beaedc.md)

- 1. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 82.0 · 採用条件未達 · 順位差 18.022727000000003 / 18.022727000000003 · insufficient_independent_call_anchors
- 2. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 63.977273 · 採用条件未達 · 順位差 -18.022727000000003 / -18.022727000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 44.545455 · 採用条件未達 · 順位差 -37.454545 / -35.11363600000001 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 44.545455 · 採用条件未達 · 順位差 -37.454545 / -35.11363600000001 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 30.768398 · 採用条件未達 · 順位差 -51.231601999999995 / -51.231601999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 28.112591 · 採用条件未達 · 順位差 -53.887409000000005 / -53.887409000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 0.0 · 採用条件未達 · 順位差 -82.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beb91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb91c.md) · スコア 0.0 · 採用条件未達 · 順位差 -82.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 18.022727000000003,
        "reverse_margin": 18.022727000000003
      },
      "new": "00bebc10",
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
      "new": "00bec2f4",
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
        "margin": -37.454545,
        "reverse_margin": -35.11363600000001
      },
      "new": "00bea0b8",
      "score": 44.545455
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00beb300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb300.md) FUN_00beb300

`competing_candidates` 

呼出元 1件 [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) · 呼出先 1件 [`00beb5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb5c0.md)

- 1. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 82.0 · 採用条件未達 · 順位差 18.022727000000003 / 18.022727000000003 · insufficient_independent_call_anchors
- 2. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 63.977273 · 採用条件未達 · 順位差 -18.022727000000003 / -18.022727000000003 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 53.75 · 採用条件未達 · 順位差 -28.25 / -25.892857000000006 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 51.704545 · 採用条件未達 · 順位差 -30.295454999999997 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 51.704545 · 採用条件未達 · 順位差 -30.295454999999997 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 33.907982 · 採用条件未達 · 順位差 -48.092018 / -45.73487500000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 12.440476 · 採用条件未達 · 順位差 -69.559524 / -69.559524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 18.022727000000003,
        "reverse_margin": 18.022727000000003
      },
      "new": "00bec2f4",
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
      "new": "00bebc10",
      "score": 63.977273
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5625,
          0.5892857142857143
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
        "margin": -28.25,
        "reverse_margin": -25.892857000000006
      },
      "new": "00bed09c",
      "score": 53.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00beb9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb9e4.md) FUN_00beb9e4

`competing_candidates` 

呼出元 1件 [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) · 呼出先 1件 [`00bebc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebc84.md)

- 1. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 82.0 · 採用条件未達 · 順位差 23.133004999999997 / 23.133004999999997 · insufficient_independent_call_anchors
- 2. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 58.866995 · 採用条件未達 · 順位差 -23.133004999999997 / -20.775862000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 56.186371 · 採用条件未達 · 順位差 -25.813629 / -23.456486000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bebc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) · スコア 28.112591 · 採用条件未達 · 順位差 -53.887409000000005 / -53.887409000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) · スコア 23.32419 · 採用条件未達 · 順位差 -58.67581 / -58.67581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 21.178161 · 採用条件未達 · 順位差 -60.821839 / -60.821839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00be5e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) · スコア 5.88047 · 採用条件未達 · 順位差 -76.11953 / 5.88047 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 23.133004999999997,
        "reverse_margin": 23.133004999999997
      },
      "new": "00bec9d8",
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
      "new": "00bed09c",
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
      "new": "00bea794",
      "score": 56.186371
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bec0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec0a8.md) FUN_00bec0a8

`competing_candidates` 

呼出元 1件 [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) · 呼出先 1件 [`00bec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec348.md)

- 1. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 79.642857 · 採用条件未達 · 順位差 3.2665500000000094 / 3.2665500000000094 · insufficient_independent_call_anchors
- 2. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 76.376307 · 採用条件未達 · 順位差 -3.2665500000000094 / -3.2665500000000094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 58.866995 · 採用条件未達 · 順位差 -20.775862000000004 / -23.133004999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bec2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) · スコア 53.75 · 採用条件未達 · 順位差 -25.892857000000006 / -28.25 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bea0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea0b8.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.938312000000003 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beb534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb534.md) · スコア 51.704545 · 採用条件未達 · 順位差 -27.938312000000003 / -27.954546 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 38.571429 · 採用条件未達 · 順位差 -41.071428000000004 / -41.071428000000004 · instruction_coverage, insufficient_independent_call_anchors
- 8. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 21.450617 · 採用条件未達 · 順位差 -58.192240000000005 / -60.549383 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bed09c",
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
      "new": "00bea794",
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
      "new": "00bec9d8",
      "score": 58.866995
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec348.md) FUN_00bec348

`competing_candidates` 

呼出元 2件 [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) [`00bec0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec0a8.md) · 呼出先 0件 

- 1. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 80.0 · 採用条件未達 · 順位差 9.729730000000004 / 9.729730000000004 · insufficient_independent_call_anchors
- 2. [`00becc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becc78.md) · スコア 70.27027 · 採用条件未達 · 順位差 -9.729730000000004 / 70.27027 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00beaa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beaa34.md) · スコア 60.1638 · 採用条件未達 · 順位差 -19.836199999999998 / -19.836199999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea378.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beb7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb7f4.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / -34.864865 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bec5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) · スコア 45.135135 · 採用条件未達 · 順位差 -34.864865 / 45.135135 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 24.054054 · 採用条件未達 · 順位差 -55.945946 / -55.945946 · instruction_coverage, insufficient_independent_call_anchors
- 8. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 0.714286 · 採用条件未達 · 順位差 -79.285714 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 9.729730000000004,
        "reverse_margin": 9.729730000000004
      },
      "new": "00bed33c",
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
        "margin": -9.729730000000004,
        "reverse_margin": 70.27027
      },
      "new": "00becc78",
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
      "new": "00beaa34",
      "score": 60.1638
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bec470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec470.md) FUN_00bec470

`competing_candidates` 

呼出元 1件 [`00be554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be554c.md) · 呼出先 0件 

- 1. [`00bed464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed464.md) · スコア 80.0 · 採用条件未達 · 順位差 2.6282719999999955 / 2.6282719999999955 · insufficient_independent_call_anchors
- 2. [`00beab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beab5c.md) · スコア 77.371728 · 採用条件未達 · 順位差 -2.6282719999999955 / -2.6282719999999955 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00becda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becda0.md) · スコア 64.01178 · 採用条件未達 · 順位差 -15.988219999999998 / 64.01178 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bec6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec6dc.md) · スコア 58.638743 · 採用条件未達 · 順位差 -21.361257000000002 / 58.638743 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 47.643979 · 採用条件未達 · 順位差 -32.356021 / -32.356021 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bef638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md) · スコア 16.773488 · 採用条件未達 · 順位差 -63.226512 / 16.773488 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 2.6282719999999955,
        "reverse_margin": 2.6282719999999955
      },
      "new": "00bed464",
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
      "new": "00beab5c",
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
          0.7051282051282052,
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
        "margin": -15.988219999999998,
        "reverse_margin": 64.01178
      },
      "new": "00becda0",
      "score": 64.01178
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bec76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec76c.md) FUN_00bec76c

`competing_candidates` 

呼出元 1件 [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) · 呼出先 1件 [`00beca0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00beca0c.md)

- 1. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 79.642857 · 採用条件未達 · 順位差 1.3447969999999998 / 1.3447969999999998 · insufficient_independent_call_anchors
- 2. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 78.29806 · 採用条件未達 · 順位差 -1.3447969999999998 / -1.3447969999999998 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 72.142857 · 採用条件未達 · 順位差 -7.5 / -7.5 · instruction_coverage, insufficient_independent_call_anchors
- 4. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 38.571429 · 採用条件未達 · 順位差 -41.071428000000004 / -41.071428000000004 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 0.0 · 採用条件未達 · 順位差 -79.642857 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bed760",
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
      "new": "00bee4e8",
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
      "new": "00bede24",
      "score": 72.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d7bacce714309f5374539685658c68af"></a>

### v16.0.2 [`00beca0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00beca0c.md) FUN_00beca0c

`competing_candidates` 

呼出元 2件 [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) [`00bec76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bec76c.md) · 呼出先 0件 

- 1. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed33c.md) · スコア 24.054054 · 採用条件未達 · 順位差 -55.945946 / -55.945946 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bed464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed464.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00beda00",
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
      "new": "00bee788",
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
      "new": "00bee0c4",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00becb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00becb34.md) FUN_00becb34

`competing_candidates` 

呼出元 1件 [`00be5c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be5/00be5c64.md) · 呼出先 0件 

- 1. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 80.0 · 採用条件未達 · 順位差 5.476051999999996 / 5.476051999999996 · insufficient_independent_call_anchors
- 2. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 74.523948 · 採用条件未達 · 順位差 -5.476051999999996 / -5.476051999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 58.058996 · 採用条件未達 · 順位差 -21.941004 / -21.941004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 55.434796 · 採用条件未達 · 順位差 -24.565204 / -24.565204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bed464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed464.md) · スコア 47.643979 · 採用条件未達 · 順位差 -32.356021 / -32.356021 · instruction_coverage, insufficient_independent_call_anchors
- 6. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 22.484649 · 採用条件未達 · 順位差 -57.515350999999995 / 22.484649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 5.476051999999996,
        "reverse_margin": 5.476051999999996
      },
      "new": "00bedb28",
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
      "new": "00bee8b0",
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
      "new": "00bee1ec",
      "score": 58.058996
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bece30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bece30.md) FUN_00bece30

`competing_candidates` 

呼出元 1件 [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) · 呼出先 1件 [`00bed0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed0d0.md)

- 1. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 79.642857 · 採用条件未達 · 順位差 7.5 / 7.5 · insufficient_independent_call_anchors
- 2. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 72.142857 · 採用条件未達 · 順位差 -7.5 / -7.5 · instruction_coverage, insufficient_independent_call_anchors
- 3. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 71.731092 · 採用条件未達 · 順位差 -7.911765000000003 / -7.911765000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 66.653439 · 採用条件未達 · 順位差 -12.989418 / -12.989418 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.328721 / -79.685864 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bede24",
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
      "new": "00bed760",
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
      "new": "00beebac",
      "score": 71.731092
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-da4c7f1fb1c149ce6a45078a6c173d5c"></a>

### v16.0.2 [`00bed0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed0d0.md) FUN_00bed0d0

`competing_candidates` 

呼出元 2件 [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) [`00bece30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bec/00bece30.md) · 呼出先 0件 

- 1. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 80.0 · 採用条件未達 · 順位差 14.818533000000002 / 14.818533000000002 · insufficient_independent_call_anchors
- 2. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 65.181467 · 採用条件未達 · 順位差 -14.818533000000002 / -14.818533000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 14.818533000000002,
        "reverse_margin": 14.818533000000002
      },
      "new": "00bee0c4",
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
      "new": "00beee4c",
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
      "new": "00beda00",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bed1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed1f8.md) FUN_00bed1f8

`competing_candidates` 

呼出元 1件 [`00be637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be637c.md) · 呼出先 0件 

- 1. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 80.0 · 採用条件未達 · 順位差 19.791780000000003 / 19.791780000000003 · insufficient_independent_call_anchors
- 2. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 60.20822 · 採用条件未達 · 順位差 -19.791780000000003 / -19.791780000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 58.058996 · 採用条件未達 · 順位差 -21.941004 / -21.941004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 54.640531 · 採用条件未達 · 順位差 -25.359468999999997 / -25.359468999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 22.43647 · 採用条件未達 · 順位差 -57.56353 / 22.43647 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.685864 / -79.328721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.685864 / -79.328721 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.791780000000003,
        "reverse_margin": 19.791780000000003
      },
      "new": "00bee1ec",
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
      "new": "00beef74",
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
      "new": "00bedb28",
      "score": 58.058996
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fdd42a1af29ee530188080668f92d747"></a>

### v16.0.2 [`00bed4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed4f4.md) FUN_00bed4f4

`competing_candidates` 

呼出元 1件 [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) · 呼出先 1件 [`00bed794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed794.md)

- 1. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 79.642857 · 採用条件未達 · 順位差 1.3447969999999998 / 1.3447969999999998 · insufficient_independent_call_anchors
- 2. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 78.29806 · 採用条件未達 · 順位差 -1.3447969999999998 / -1.3447969999999998 · cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 66.653439 · 採用条件未達 · 順位差 -12.989418 / -12.989418 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) · スコア 21.355422 · 採用条件未達 · 順位差 -58.287435 / -60.644577999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 0.314136 · 採用条件未達 · 順位差 -79.328721 / -79.685864 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bee4e8",
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
      "new": "00bed760",
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
          0.8148148148148148,
          0.825
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
      "new": "00bede24",
      "score": 66.653439
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bdd6f2eec63cc7815d74fa29b6070d09"></a>

### v16.0.2 [`00bed794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed794.md) FUN_00bed794

`competing_candidates` 

呼出元 2件 [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) [`00bed4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed4f4.md) · 呼出先 0件 

- 1. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 47.397683 · 採用条件未達 · 順位差 -32.602317 / -32.602317 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.928571 / -78.57142800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00beda00",
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
      "new": "00bee788",
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
      "new": "00bee0c4",
      "score": 47.397683
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bed8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bed8bc.md) FUN_00bed8bc

`competing_candidates` 

呼出元 1件 [`00be6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be6/00be6a94.md) · 呼出先 0件 

- 1. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 80.0 · 採用条件未達 · 順位差 5.476051999999996 / 5.476051999999996 · insufficient_independent_call_anchors
- 2. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 74.523948 · 採用条件未達 · 順位差 -5.476051999999996 / -5.476051999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 54.640531 · 採用条件未達 · 順位差 -25.359468999999997 / -25.359468999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 53.741349 · 採用条件未達 · 順位差 -26.258651 / -26.258651 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 22.484649 · 採用条件未達 · 順位差 -57.515350999999995 / 22.484649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 5.476051999999996,
        "reverse_margin": 5.476051999999996
      },
      "new": "00bee8b0",
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
      "new": "00bedb28",
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
          0.5555555555555556,
          0.5487804878048781
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
      "new": "00bee1ec",
      "score": 54.640531
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2f620d5d89229bc05ded7a14d4e124c2"></a>

### v16.0.2 [`00bedbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bedbb8.md) FUN_00bedbb8

`competing_candidates` 

呼出元 1件 [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) · 呼出先 1件 [`00bede58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bede58.md)

- 1. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 79.642857 · 採用条件未達 · 順位差 7.911765000000003 / 7.911765000000003 · insufficient_independent_call_anchors
- 2. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 71.731092 · 採用条件未達 · 順位差 -7.911765000000003 / -7.911765000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 59.273109 · 採用条件未達 · 順位差 -20.36974800000001 / -20.36974800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) · スコア 18.659664 · 採用条件未達 · 順位差 -60.98319300000001 / -63.340336 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 9.147059 · 採用条件未達 · 順位差 -70.49579800000001 / -72.852941 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 1.071429 · 採用条件未達 · 順位差 -78.57142800000001 / -78.928571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.28571400000001 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00beebac",
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
      "new": "00bede24",
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
          0.5529411764705883,
          0.5875
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
      "new": "00bed760",
      "score": 59.273109
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b5ee302d3e44ac890250482ca2f0e9bd"></a>

### v16.0.2 [`00bede58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bede58.md) FUN_00bede58

`competing_candidates` 

呼出元 2件 [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) [`00bedbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bedbb8.md) · 呼出先 0件 

- 1. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 80.0 · 採用条件未達 · 順位差 14.818533000000002 / 14.818533000000002 · insufficient_independent_call_anchors
- 2. [`00bee0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee0c4.md) · スコア 65.181467 · 採用条件未達 · 順位差 -14.818533000000002 / -14.818533000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00beda00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00beda00.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee788.md) · スコア 47.043919 · 採用条件未達 · 順位差 -32.956081 / -32.956081 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.642857 / -79.28571400000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 0.357143 · 採用条件未達 · 順位差 -79.642857 / -81.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 14.818533000000002,
        "reverse_margin": 14.818533000000002
      },
      "new": "00beee4c",
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
      "new": "00bee0c4",
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
          0.40625,
          0.41935483870967744
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
      "new": "00beda00",
      "score": 47.043919
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00bedf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bed/00bedf80.md) FUN_00bedf80

`competing_candidates` 

呼出元 1件 [`00be71ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be71ac.md) · 呼出先 0件 

- 1. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 80.0 · 採用条件未達 · 順位差 19.791780000000003 / 19.791780000000003 · insufficient_independent_call_anchors
- 2. [`00bee1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee1ec.md) · スコア 60.20822 · 採用条件未達 · 順位差 -19.791780000000003 / -19.791780000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bedb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bedb28.md) · スコア 55.434796 · 採用条件未達 · 順位差 -24.565204 / -24.565204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee8b0.md) · スコア 53.741349 · 採用条件未達 · 順位差 -26.258651 / -26.258651 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00befcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · スコア 21.208401 · 採用条件未達 · 順位差 -58.791599000000005 / 21.208401 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -82.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 19.791780000000003,
        "reverse_margin": 19.791780000000003
      },
      "new": "00beef74",
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
      "new": "00bee1ec",
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
          0.4942528735632184,
          0.5512820512820513
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
      "new": "00bedb28",
      "score": 55.434796
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-89ca18545c19f1d9006d35df14fa9d35"></a>

### v16.0.2 [`00bee27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee27c.md) FUN_00bee27c

`competing_candidates` 

呼出元 1件 [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) · 呼出先 1件 [`00bee51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee51c.md)

- 1. [`00bef270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) · スコア 82.0 · 採用条件未達 · 順位差 60.549383 / 60.549383 · insufficient_independent_call_anchors
- 2. [`00bed09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed09c.md) · スコア 21.450617 · 採用条件未達 · 順位差 -60.549383 / -58.192240000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bec9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) · スコア 21.178161 · 採用条件未達 · 順位差 -60.821839 / -60.821839 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bea794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00bea794.md) · スコア 18.754355 · 採用条件未達 · 順位差 -63.245644999999996 / -60.888502 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 9.147059 · 採用条件未達 · 順位差 -72.852941 / -70.49579800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) · スコア 6.072285 · 採用条件未達 · 順位差 -75.927715 / 6.072285 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00beee4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beee4c.md) · スコア 0.357143 · 採用条件未達 · 順位差 -81.642857 / -79.642857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00beef74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beef74.md) · スコア 0.0 · 採用条件未達 · 順位差 -82.0 / -80.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 60.549383,
        "reverse_margin": 60.549383
      },
      "new": "00bef270",
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
          0.19753086419753085,
          0.2
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.549383,
        "reverse_margin": -58.192240000000005
      },
      "new": "00bed09c",
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
          0.19753086419753085,
          0.1839080459770115
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
      "new": "00bec9d8",
      "score": 21.178161
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b10dcaf923376a434a3fec76b7155835"></a>

### v16.0.2 [`00bee91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee91c.md) FUN_00bee91c

`competing_candidates` 

呼出元 1件 [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) · 呼出先 1件 [`00beebbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beebbc.md)

- 1. [`00bef910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef910.md) · スコア 82.0 · 採用条件未達 · 順位差 60.644577999999996 / 60.644577999999996 · insufficient_independent_call_anchors
- 2. [`00bed760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bed760.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bede24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bed/00bede24.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00bee4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00bee4e8.md) · スコア 21.355422 · 採用条件未達 · 順位差 -60.644577999999996 / -58.287435 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00beebac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bee/00beebac.md) · スコア 18.659664 · 採用条件未達 · 順位差 -63.340336 / -60.98319300000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00be8fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8fd0.md) · スコア 6.206087 · 採用条件未達 · 順位差 -75.793913 / 6.206087 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 60.644577999999996,
        "reverse_margin": 60.644577999999996
      },
      "new": "00bef910",
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
          0.1927710843373494,
          0.2
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.644577999999996,
        "reverse_margin": -58.287435
      },
      "new": "00bed760",
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
          0.1927710843373494,
          0.2
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.644577999999996,
        "reverse_margin": -58.287435
      },
      "new": "00bede24",
      "score": 21.355422
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e53aec60254ed9cda6771ed1087bf164"></a>

### v16.0.2 [`00bf87d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf87d0.md) FUN_00bf87d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf97c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf97c4.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 65.0
      },
      "new": "00bf97c4",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3b3a26c58416806c7bf1087d595bb0e5"></a>

### v16.0.2 [`00bf87e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf87e0.md) FUN_00bf87e0

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`00bf97d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf97d4.md) · スコア 61.538462 · 採用条件未達 · 順位差 6.923076999999999 / 6.923076999999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf989c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf989c.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.923076999999999 / -6.184614999999994 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bfbf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf08.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.84880700000001 / -42.758621000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00532cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532cd0.md) · スコア 11.538462 · 採用条件未達 · 順位差 -50.0 / -47.461538 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0074e6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e6ec.md) · スコア 11.538462 · 採用条件未達 · 順位差 -50.0 / -47.461538 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bf97d4",
      "score": 61.538462
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
      "new": "00bf989c",
      "score": 54.615385
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
      "new": "00bfbf08",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-70f2b2162f8f4fe8928cab448c204934"></a>

### v16.0.2 [`00bf8898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8898.md) FUN_00bf8898

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf988c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf988c.md) · スコア 65.0 · 採用条件未達 · 順位差 31.666666999999997 / 31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf9900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9900.md) · スコア 33.333333 · 採用条件未達 · 順位差 -31.666666999999997 / -46.666667 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 31.666666999999997,
        "reverse_margin": 31.666666999999997
      },
      "new": "00bf988c",
      "score": 65.0
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
      "new": "00bf9900",
      "score": 33.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-134e0e7c158ee2e063d7b1cb16634254"></a>

### v16.0.2 [`00bf88a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf88a8.md) FUN_00bf88a8

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`00bf989c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf989c.md) · スコア 60.8 · 採用条件未達 · 順位差 6.184614999999994 / 6.184614999999994 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf97d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf97d4.md) · スコア 54.615385 · 採用条件未達 · 順位差 -6.184614999999994 / -6.923076999999999 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bfbf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf08.md) · スコア 20.689655 · 採用条件未達 · 順位差 -40.110344999999995 / -42.758621000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bf989c",
      "score": 60.8
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
      "new": "00bf97d4",
      "score": 54.615385
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
      "new": "00bfbf08",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7a53f496fb01511def09e40359b237a"></a>

### v16.0.2 [`00bf890c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf890c.md) FUN_00bf890c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bf9900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf9900.md) · スコア 80.0 · 採用条件未達 · 順位差 46.666667 / 46.666667 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00bf988c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf988c.md) · スコア 33.333333 · 採用条件未達 · 順位差 -46.666667 / -31.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bf989c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf989c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -60.8 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 46.666667,
        "reverse_margin": 46.666667
      },
      "new": "00bf9900",
      "score": 80.0
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
      "new": "00bf988c",
      "score": 33.333333
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
        "reverse_margin": -60.8
      },
      "new": "00bf989c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8cab44de123582312481ae3ec03757d2"></a>

### v16.0.2 [`00bf945c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf945c.md) FUN_00bf945c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bfa450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa450.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 65.0
      },
      "new": "00bfa450",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-20391c622f58da6455ae99aaf7d4a610"></a>

### v16.0.2 [`00bf946c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf946c.md) FUN_00bf946c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`00bfa460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfa/00bfa460.md) · スコア 48.484848 · 採用条件未達 · 順位差 43.222922 / 43.222922 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00522ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522ec0.md) · スコア 5.261926 · 採用条件未達 · 順位差 -43.222922 / 5.261926 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00abe074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abe/00abe074.md) · スコア 3.576577 · 採用条件未達 · 順位差 -44.908271 / 3.576577 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) · スコア 1.401869 · 採用条件未達 · 順位差 -47.082979 / 1.401869 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0045e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.484848 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005d1434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1434.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.484848 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0065f50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065f/0065f50c.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.484848 / -38.768258 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0065fba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065f/0065fba8.md) · スコア 0.0 · 採用条件未達 · 順位差 -48.484848 / -30.014295 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bfa460",
      "score": 48.484848
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10101010101010101,
          0.07462686567164178
        ],
        "cfg_coverage": [
          0.10526315789473684,
          0.0392156862745098
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -43.222922,
        "reverse_margin": 5.261926
      },
      "new": "00522ec0",
      "score": 5.261926
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08080808080808081,
          0.05405405405405406
        ],
        "cfg_coverage": [
          0.05263157894736842,
          0.016666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -44.908271,
        "reverse_margin": 3.576577
      },
      "new": "00abe074",
      "score": 3.576577
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-08921b94deb50ff83beb0880a9ff5247"></a>

### v16.0.2 [`00bfaf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf04.md) FUN_00bfaf04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bfbef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbef8.md) · スコア 65.0 · 採用条件未達 · 順位差 65.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": 65.0
      },
      "new": "00bfbef8",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-507f34e1685c630e14cbd61cdffdcaf2"></a>

### v16.0.2 [`00bfaf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf14.md) FUN_00bfaf14

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bf86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`00bfbf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbf08.md) · スコア 63.448276 · 採用条件未達 · 順位差 42.758621000000005 / 42.758621000000005 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00bf97d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf97d4.md) · スコア 20.689655 · 採用条件未達 · 順位差 -42.758621000000005 / -40.84880700000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00bf989c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf989c.md) · スコア 20.689655 · 採用条件未達 · 順位差 -42.758621000000005 / -40.110344999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
      "new": "00bfbf08",
      "score": 63.448276
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
      "new": "00bf97d4",
      "score": 20.689655
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
      "new": "00bf989c",
      "score": 20.689655
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0dc76c5758a8ef416cda9bc985fe0f90"></a>

### v16.0.2 [`00c2d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d030.md) FUN_00c2d030

`competing_candidates` 

呼出元 1件 [`00c2cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md) · 呼出先 5件 [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) [`00c35dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35dac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

- 1. [`00c2e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e024.md) · スコア 59.801105 · 採用条件未達 · 順位差 55.982923 / 55.982923 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c2eab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2eab8.md) · スコア 3.818182 · 採用条件未達 · 順位差 -55.982923 / -58.363636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0047fdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047fdac.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.801105 / -62.794118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00c2db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.801105 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c2e364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.801105 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00c2f04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.801105 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00c2f198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md) · スコア 2.0 · 採用条件未達 · 順位差 -57.801105 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0048a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md) · スコア 0.0 · 採用条件未達 · 順位差 -59.801105 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "reverse_margin": 55.982923
      },
      "new": "00c2e024",
      "score": 59.801105
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
      "new": "00c2eab8",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -57.801105,
        "reverse_margin": -62.794118
      },
      "new": "0047fdac",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-85be5e79b8713ea1763849a3f49b8c28"></a>

### v16.0.2 [`00c2dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dac4.md) FUN_00c2dac4

`competing_candidates` 

呼出元 1件 [`00c2da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md) · 呼出先 5件 [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) [`00c35f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35f6c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

- 1. [`00c2eab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2eab8.md) · スコア 62.181818 · 採用条件未達 · 順位差 58.363636 / 58.363636 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00c2e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e024.md) · スコア 3.818182 · 採用条件未達 · 順位差 -58.363636 / -55.982923 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0047fdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047fdac.md) · スコア 2.0 · 採用条件未達 · 順位差 -60.181818 / -62.794118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00c2db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md) · スコア 2.0 · 採用条件未達 · 順位差 -60.181818 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00c2e364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md) · スコア 2.0 · 採用条件未達 · 順位差 -60.181818 / 2.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0048a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md) · スコア 0.0 · 採用条件未達 · 順位差 -62.181818 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 58.363636,
        "reverse_margin": 58.363636
      },
      "new": "00c2eab8",
      "score": 62.181818
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
        "margin": -58.363636,
        "reverse_margin": -55.982923
      },
      "new": "00c2e024",
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -60.181818,
        "reverse_margin": -62.794118
      },
      "new": "0047fdac",
      "score": 2.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-df9381828f933945b5d300b9e11170a5"></a>

### v16.0.2 [`00c35128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35128.md) FUN_00c35128

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3611c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3611c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36238.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c3611c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36238",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36128",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bb5fe8f66b7944509b8c246eb41f1f92"></a>

### v16.0.2 [`00c35134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35134.md) FUN_00c35134

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3611c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3611c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36128",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36244",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3611c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-225c8f952336d2cf222cb4155e9cb8ea"></a>

### v16.0.2 [`00c35140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35140.md) FUN_00c35140

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3611c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3611c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36134",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36250",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3611c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a56f2f1cfc85d14adc1c8a3c08474bc1"></a>

### v16.0.2 [`00c3514c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3514c.md) FUN_00c3514c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3611c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3611c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36140",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3625c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3611c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cc768c3d6b48fe3f8a82b16d93da6b0f"></a>

### v16.0.2 [`00c35158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35158.md) FUN_00c35158

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c3614c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36268",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36128",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bfc29bb58adb61f029be7679befb3a64"></a>

### v16.0.2 [`00c35164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35164.md) FUN_00c35164

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36158",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36274",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36134",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-969da629dc7b2dd9ae4c0eec66567945"></a>

### v16.0.2 [`00c35170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35170.md) FUN_00c35170

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36280.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36164",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36280",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36140",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b87593f39e52227223af836868fc683c"></a>

### v16.0.2 [`00c3517c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3517c.md) FUN_00c3517c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3628c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36170",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3628c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3614c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-77df0d276201390339bb4677e4c413d6"></a>

### v16.0.2 [`00c35188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35188.md) FUN_00c35188

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36298.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c3617c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36298",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36158",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-80831a6f2519a45d35e8b49fdd02f7bc"></a>

### v16.0.2 [`00c35194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35194.md) FUN_00c35194

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c362a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362a4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c361ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36188",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c362a4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36164",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cb707919dbfdcd93251000effce1706a"></a>

### v16.0.2 [`00c351a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351a0.md) FUN_00c351a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c362b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362b0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36170.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c361ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c361b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361b8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36194",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c362b0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36170",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b7a643cc7f8a44ece34fd4608a6f5517"></a>

### v16.0.2 [`00c351ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351ac.md) FUN_00c351ac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c362bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362bc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3617c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3617c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c361ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c361b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361b8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c361a0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c362bc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3617c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eebe17e63987501feb41fbbefe589350"></a>

### v16.0.2 [`00c351b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351b8.md) FUN_00c351b8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c361ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361ac.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c362c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36188.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c361b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361b8.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c361ac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c362c8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36188",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6654d4cf38ec2a9b98838ab0f066a5ce"></a>

### v16.0.2 [`00c351c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351c4.md) FUN_00c351c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c361b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361b8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c362d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362d4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36194.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c361a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361a0.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c361ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c361ac.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c361b8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c362d4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36194",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a2c4007e39145c5118f50b0a963a1f8b"></a>

### v16.0.2 [`00c35244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35244.md) FUN_00c35244

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36238.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3611c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3611c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36238",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3611c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36244",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-20904cb9df130678b10e18b83d30e29d"></a>

### v16.0.2 [`00c35250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35250.md) FUN_00c35250

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36128.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36238.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36244",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36128",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36238",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d879055ae225aa31055d02b3d4d7e6b9"></a>

### v16.0.2 [`00c3525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3525c.md) FUN_00c3525c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36134.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36238.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36250",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36134",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36238",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d938f6df9c2dcdb1ad31ed6a30202c38"></a>

### v16.0.2 [`00c35268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35268.md) FUN_00c35268

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36140.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36238.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36280.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c3625c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36140",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36238",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-103ab36446ca363828447f754926a92b"></a>

### v16.0.2 [`00c35274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35274.md) FUN_00c35274

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c3614c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3614c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36244.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36280.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c3628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3628c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36268",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3614c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36244",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d60db27677aa679118e98b66c8172206"></a>

### v16.0.2 [`00c35280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35280.md) FUN_00c35280

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36158.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c36250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36250.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c36280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36280.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c3628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3628c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c36298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36298.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36274",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36158",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36250",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e7c8414029d75dbd57f98dac8dd63e83"></a>

### v16.0.2 [`00c3528c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3528c.md) FUN_00c3528c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00c36280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36280.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00c36164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36164.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00c3625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3625c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00c36268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36268.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00c36274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36274.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00c3628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c3628c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00c36298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36298.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00c362a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c362a4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00c36280",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c36164",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00c3625c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

