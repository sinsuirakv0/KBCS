# v16.0.0 → v16.0.1 · 追加調査 (36)

[一覧の目次](README.md)

<a id="review-de5e2a7de68db7cdaa97b44bde214f61"></a>

### v16.0.0 [`00930f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930f3c.md) FUN_00930f3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009310d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009310d8.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`009310c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009310c8.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009310d8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009310c8",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c4238950c055edcb900e39488ef4f191"></a>

### v16.0.0 [`00930fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930fc0.md) FUN_00930fc0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093115c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093115c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0093115c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bdd145f0d93fe7afd0fa3fa815f67bc4"></a>

### v16.0.0 [`00930fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930fdc.md) FUN_00930fdc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931178.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 0.0 · 
- 2. [`0093115c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093115c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 0.0
      },
      "new": "00931178",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0093115c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f96d0011ba72bc52e454052de7f9b6dd"></a>

### v16.0.0 [`00931010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931010.md) FUN_00931010

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009311ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009311ac.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "competing_old_functions",
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
      "new": "009311ac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-43d8da8d671084207833287ffc1d74e1"></a>

### v16.0.0 [`009312b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009312b0.md) FUN_009312b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093144c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093144c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0093144c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8889dc009feb33f93973b2342647fc76"></a>

### v16.0.0 [`009312cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009312cc.md) FUN_009312cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931468.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0093144c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093144c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931468",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0093144c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a6b8a6eb5fe7b18191228140d2d99431"></a>

### v16.0.0 [`00931344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931344.md) FUN_00931344

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f7624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f7624.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`009314e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 25.714286
      },
      "new": "007f7624",
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
        "reverse_margin": 0.0
      },
      "new": "009314e0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-67d523287d397245f49f96095dc9d028"></a>

### v16.0.0 [`00931360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931360.md) FUN_00931360

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009314fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314fc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009314e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009314e0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009314fc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009314e0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-683a596789c4c1992ed7faeec3855a0e"></a>

### v16.0.0 [`00931728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931728.md) FUN_00931728

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009318c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009318c4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009318c4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6443d744750920854af325f12a29d7e8"></a>

### v16.0.0 [`00931744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931744.md) FUN_00931744

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009318e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009318e0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009318c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009318c4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009318e0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009318c4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eb14758091d102c00e347f2775bb7265"></a>

### v16.0.0 [`0093180c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/0093180c.md) FUN_0093180c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00b3fab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fab8.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`009319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009319a8.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00b3fab8",
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
      "new": "009319a8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1b36915bcbc6e56157908d8d037727e1"></a>

### v16.0.0 [`00931828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931828.md) FUN_00931828

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009319c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009319c4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009319a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009319a8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009319c4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009319a8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-68516b7df11190e0c596d87fb5b72b71"></a>

### v16.0.0 [`0093186c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/0093186c.md) FUN_0093186c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931a08.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00931a08",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b36fe58aa991fecb89de2334b9e14214"></a>

### v16.0.0 [`009318f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009318f0.md) FUN_009318f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931a8c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -5.714286000000001 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "reverse_margin": -5.714286000000001
      },
      "new": "00931a8c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d32ce60e82896eae0b13bebf1acd27b6"></a>

### v16.0.0 [`0093190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/0093190c.md) FUN_0093190c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931aa8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00931a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931a8c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931aa8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00931a8c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1e70850ecf3e795e6dbd2fd1c2f933ca"></a>

### v16.0.0 [`00931cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931cf8.md) FUN_00931cf8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931e94.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00931e94",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9541c4c0c734c7598caf3f19785df261"></a>

### v16.0.0 [`00931d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931d14.md) FUN_00931d14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931eb0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00931e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931e94.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931eb0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00931e94",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6d905a779bf6b64e087cf8054017ce9a"></a>

### v16.0.0 [`00931ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931ddc.md) FUN_00931ddc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931f78.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00931f78",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-86a5f7c71b366c1af6d187e4299c3b06"></a>

### v16.0.0 [`00931df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931df8.md) FUN_00931df8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931094.md) · スコア 84.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`00931f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931f94.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00931f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931f78.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931094",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00931f94",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00931f78",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-72d6d4cf7358b1d290f12dd5b6eba0b7"></a>

### v16.0.0 [`00931e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931e2c.md) FUN_00931e2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00655334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655334.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`009310c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009310c8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 30.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`009c143c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c1/009c143c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00931fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931fc8.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "competing_candidates",
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
        "reverse_margin": 80.0
      },
      "new": "00655334",
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
        "reverse_margin": 30.0
      },
      "new": "009310c8",
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
        "reverse_margin": 80.0
      },
      "new": "009c143c",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7c160d0f69ecdaee79f2429062ad3ca0"></a>

### v16.0.0 [`00931e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931e3c.md) FUN_00931e3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931fd8.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`00931fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931fc8.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931fd8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00931fc8",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7c515093a452e3b8e29a49670d01485c"></a>

### v16.0.0 [`00931ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931ec0.md) FUN_00931ec0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008d87a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d87a0.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0093205c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/0093205c.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008d87a0",
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
      "new": "0093205c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f91b916b008a6ed2618d6f00b53d9c4b"></a>

### v16.0.0 [`00931edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931edc.md) FUN_00931edc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00931178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931178.md) · スコア 84.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`00932078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932078.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0093205c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/0093205c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00931178",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00932078",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0093205c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b38c51de417ddfbdca0ccf06cf7118ef"></a>

### v16.0.0 [`00931f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931f10.md) FUN_00931f10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009311ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009311ac.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00934e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e9c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009320ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009320ac.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "competing_candidates",
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
        "reverse_margin": 80.0
      },
      "new": "009311ac",
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
        "reverse_margin": 80.0
      },
      "new": "00934e9c",
      "score": 80.0
    },
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
        "margin": -30.0,
        "reverse_margin": 50.0
      },
      "new": "009320ac",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-472d842791247aa6b77eb52fed4dd9a4"></a>

### v16.0.0 [`00932244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932244.md) FUN_00932244

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009323e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009323e0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009323e0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-502209b7e05bdefe4a456d2033e933c0"></a>

### v16.0.0 [`00932260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932260.md) FUN_00932260

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009323fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009323fc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009323e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009323e0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009323fc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009323e0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-56f6ce3b2d80f48781796258ef53372b"></a>

### v16.0.0 [`00932328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932328.md) FUN_00932328

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009324c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009324c4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009324c4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2448273f4533ea928615c27bca66cff3"></a>

### v16.0.0 [`00932344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932344.md) FUN_00932344

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009324e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009324e0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009324c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009324c4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009324e0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009324c4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bd566960c8692a180ee775adf1a3f2cf"></a>

### v16.0.0 [`00932388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932388.md) FUN_00932388

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932524.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00932524",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5b76bec0e4ee06c33e49298ab6232fc5"></a>

### v16.0.0 [`0093240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/0093240c.md) FUN_0093240c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009325a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325a8.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009325a8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b56841cad88db23efd0c37afb8769191"></a>

### v16.0.0 [`00932428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932428.md) FUN_00932428

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009325c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325c4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009325a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325a8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009325c4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009325a8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-49927015fc187b975afbfe912b764d8b"></a>

### v16.0.0 [`009325a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009325a4.md) FUN_009325a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932740.md) · スコア 8.571429 · 採用条件未達 · 順位差 8.571429 / 8.571429 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.14285714285714285
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
        "margin": 8.571429,
        "reverse_margin": 8.571429
      },
      "new": "00932740",
      "score": 8.571429
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-00135a5867344f490fab3405acec56d5"></a>

### v16.0.0 [`009325c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009325c0.md) FUN_009325c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/0093275c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00932740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932740.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0093275c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00932740",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c78a84542dc72a1861070c8023c89168"></a>

### v16.0.0 [`009329e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009329e8.md) FUN_009329e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932b84.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00932b84",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0c3c33c4b770bcc1df2c032950613f5f"></a>

### v16.0.0 [`00932a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a04.md) FUN_00932a04

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932ba0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00932b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932b84.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00932ba0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00932b84",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6ca15dced46ca1e2facde9835f46e97c"></a>

### v16.0.0 [`00932acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932acc.md) FUN_00932acc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c68.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00932c68",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ccb64f6f01cb5c49ece3c616f3cc08a4"></a>

### v16.0.0 [`00932ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932ae8.md) FUN_00932ae8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c84.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00932c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c68.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00932c84",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00932c68",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bdad7b75b8b62db1dd461eee5b708c7a"></a>

### v16.0.0 [`00932b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932b2c.md) FUN_00932b2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932cc8.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00932cc8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-652ae84354480ec9e72a19f2a43af404"></a>

### v16.0.0 [`00932bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932bb0.md) FUN_00932bb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00932d4c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bd04f39a02634b2ed090bf95dbee7530"></a>

### v16.0.0 [`00932bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932bcc.md) FUN_00932bcc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00932d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d68.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00932d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d4c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00932d68",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00932d4c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a74a7be7b98ebae4acce5f7d8162585"></a>

### v16.0.0 [`0093300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093300c.md) FUN_0093300c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009331a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331a8.md) · スコア 45.714286 · 採用条件未達 · 順位差 45.714286 / 11.428572000000003 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 45.714286,
        "reverse_margin": 11.428572000000003
      },
      "new": "009331a8",
      "score": 45.714286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ecf2273275c0cfec98b3abad6907c408"></a>

### v16.0.0 [`00933028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933028.md) FUN_00933028

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009331c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331c4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 0.0 · 
- 2. [`009331a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331a8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 0.0
      },
      "new": "009331c4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009331a8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0f132d9f44a2835afb8327762824f121"></a>

### v16.0.0 [`009330f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009330f0.md) FUN_009330f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093328c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/0093328c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 0.0
      },
      "new": "0093328c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ef3cb97cff363ce33970d780587df207"></a>

### v16.0.0 [`0093310c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093310c.md) FUN_0093310c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009332a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009332a8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0093328c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/0093328c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009332a8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0093328c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5d6081e71aef8dde6a8906134a4e6002"></a>

### v16.0.0 [`00933150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933150.md) FUN_00933150

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009332ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009332ec.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "009332ec",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b782b8e0025f13742930a3f458ba069"></a>

### v16.0.0 [`009331d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009331d4.md) FUN_009331d4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933370.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933370",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-040ca8b4ad55fea6d9e928bbb7e66559"></a>

### v16.0.0 [`009331f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009331f0.md) FUN_009331f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093338c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/0093338c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933370.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0093338c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933370",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-96df0ef7cff8fa32a6d83350694c926e"></a>

### v16.0.0 [`0093333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093333c.md) FUN_0093333c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009334d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009334d8.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009334d8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7d235bb8cada1f5276d93c08fceff6f7"></a>

### v16.0.0 [`00933358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933358.md) FUN_00933358

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009334f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009334f4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 0.0 · 
- 2. [`009334d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009334d8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.2857,
        "reverse_margin": 0.0
      },
      "new": "009334f4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009334d8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fdf87fee59495601f811ea32ad744102"></a>

### v16.0.0 [`00933464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933464.md) FUN_00933464

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933600.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933600",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8e9a6f4f5adf1ca8fe4c120d846d9bb6"></a>

### v16.0.0 [`00933480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933480.md) FUN_00933480

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0093361c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/0093361c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933600.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0093361c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933600",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-43925332f741011d6e338f88c08377c1"></a>

### v16.0.0 [`0093358c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093358c.md) FUN_0093358c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933728.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933728",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5420b756c542bae8306191ffd65c5347"></a>

### v16.0.0 [`009335a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/009335a8.md) FUN_009335a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933744.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933728.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00933744",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933728",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-373b425522517c86c14bbcdfbd91437c"></a>

### v16.0.0 [`00933874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933874.md) FUN_00933874

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933a10.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933a10",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8d411758a5af3b2ff34e109ef325ba2c"></a>

### v16.0.0 [`00933890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933890.md) FUN_00933890

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933a2c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933a10.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00933a2c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933a10",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-474042844abb64203fc3c244f33ff6ba"></a>

### v16.0.0 [`00933924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933924.md) FUN_00933924

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ac0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933ac0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-672c1ca157a0f1dc6bb3de9676160440"></a>

### v16.0.0 [`00933940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933940.md) FUN_00933940

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933adc.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ac0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00933adc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933ac0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c3312bf32d620f37c5931ca297ff1d44"></a>

### v16.0.0 [`00933aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933aa4.md) FUN_00933aa4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933c40.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933c40",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f67628610a4b9dcf751c89b6dcf0b2ad"></a>

### v16.0.0 [`00933ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933ac0.md) FUN_00933ac0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933c5c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933c40.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00933c5c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933c40",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-08a89f4611a8a75e2f335c74e8b1050c"></a>

### v16.0.0 [`00933c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c10.md) FUN_00933c10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933dac.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933dac",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8a5c68eca1476a2c2cf76918b22b2b9c"></a>

### v16.0.0 [`00933c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933c2c.md) FUN_00933c2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933dc8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00933dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933dac.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00933dc8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933dac",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3774cb83091d6ec3e186c6f04c9215c4"></a>

### v16.0.0 [`00933d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d38.md) FUN_00933d38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ed4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933ed4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0ed6547f83f99726f5368cd1c10d49be"></a>

### v16.0.0 [`00933d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933d54.md) FUN_00933d54

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009331c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331c4.md) · スコア 84.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`00933ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ef0.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00933ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ed4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009331c4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933ef0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933ed4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a81cdf0acfd9b5df9b65359361eee4a"></a>

### v16.0.0 [`00933e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e60.md) FUN_00933e60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00933ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ffc.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00933ffc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-42969c5376aac193e457e55563455dec"></a>

### v16.0.0 [`00933e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933e7c.md) FUN_00933e7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009334f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009334f4.md) · スコア 84.0 · 採用条件未達 · 順位差 0.0 / 0.0 · 
- 2. [`00934018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934018.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00933ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/00933ffc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009334f4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00934018",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00933ffc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c6e267bbf79068fa263cf3d215d14b41"></a>

### v16.0.0 [`009343ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009343ec.md) FUN_009343ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934588.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00934588",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6617608f8030fb295ac04c29441ffb6d"></a>

### v16.0.0 [`00934408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934408.md) FUN_00934408

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009345a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009345a4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00934588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934588.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009345a4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00934588",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d472fd40738a1c9219fa598ffd3a6ac1"></a>

### v16.0.0 [`00934530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934530.md) FUN_00934530

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009346cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009346cc.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009346cc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-616295583b81375ac120e201ce5c6174"></a>

### v16.0.0 [`0093454c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093454c.md) FUN_0093454c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009346e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009346e8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009346cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009346cc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "009346e8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009346cc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1e9b0f40f205b4ad2d145b2f96fd507f"></a>

### v16.0.0 [`009346a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346a0.md) FUN_009346a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00781d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781d14.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0093483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/0093483c.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00781d14",
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
      "new": "0093483c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3aaafe709b112fa51ff144fa7a5f427a"></a>

### v16.0.0 [`009346bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346bc.md) FUN_009346bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934858.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0093483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/0093483c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00934858",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0093483c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fbb198747d313f7938ee31815cfd0929"></a>

### v16.0.0 [`00934b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b40.md) FUN_00934b40

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008d9b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9b80.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00934cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934cdc.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008d9b80",
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
      "new": "00934cdc",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8671fd70da4338dab595acce869be6e9"></a>

### v16.0.0 [`00934b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b5c.md) FUN_00934b5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934cf8.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00934cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934cdc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00934cf8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00934cdc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4c1789f9ae0df02ba87e02db076f788b"></a>

### v16.0.0 [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) FUN_00934bbc

`competing_candidates` 

呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00726f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726f08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md)

- 1. [`00934d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d58.md) · スコア 67.213115 · 採用条件未達 · 順位差 50.046839000000006 / 50.046839000000006 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006170ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md) · スコア 17.166276 · 採用条件未達 · 順位差 -50.046839000000006 / 17.166276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00aed650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed650.md) · スコア 12.786885 · 採用条件未達 · 順位差 -54.426230000000004 / 12.786885 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00aed778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed778.md) · スコア 11.803714 · 採用条件未達 · 順位差 -55.409401 / 11.803714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a7e564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e564.md) · スコア 9.297424 · 採用条件未達 · 順位差 -57.915691 / 9.297424 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00793810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793810.md) · スコア 8.709677 · 採用条件未達 · 順位差 -58.503438 / 8.709677 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00785578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785578.md) · スコア 6.666667 · 採用条件未達 · 順位差 -60.546448 / 6.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005e7c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c40.md) · スコア 3.934426 · 採用条件未達 · 順位差 -63.278689 / 3.934426 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7868852459016393,
          0.7868852459016393
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
        "margin": 50.046839000000006,
        "reverse_margin": 50.046839000000006
      },
      "new": "00934d58",
      "score": 67.213115
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.26229508196721313,
          0.2962962962962963
        ],
        "cfg_coverage": [
          0.07142857142857142,
          0.125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -50.046839000000006,
        "reverse_margin": 17.166276
      },
      "new": "006170ac",
      "score": 17.166276
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21311475409836064,
          0.3023255813953488
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
        "margin": -54.426230000000004,
        "reverse_margin": 12.786885
      },
      "new": "00aed650",
      "score": 12.786885
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2df11fb405a83a77c3a9671a445ad08b"></a>

### v16.0.0 [`00934cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cb0.md) FUN_00934cb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e4c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00934e4c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-364d5815c233c68ad8fedae1e808f1e5"></a>

### v16.0.0 [`00934ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ccc.md) FUN_00934ccc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00934e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e68.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00934e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e4c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00934d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d58.md) · スコア 0.1967 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00934e68",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00934e4c",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00934d58",
      "score": 0.1967
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c30d70d98f4404ada7134cd9f6ea9db8"></a>

### v16.0.0 [`00934f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934f98.md) FUN_00934f98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00935134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935134.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00935134",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e53fc9e0c1b0c7967678bab39ea2bd41"></a>

### v16.0.0 [`00934fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fb4.md) FUN_00934fb4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00935150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935150.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00935134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935134.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00935150",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00935134",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8f7e2ed2a6c4027d46732b72ab10a4c6"></a>

### v16.0.0 [`00935048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935048.md) FUN_00935048

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`009351e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009351e4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "009351e4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f8d26a4c14f1f7fcd62ce7e9c978bbb6"></a>

### v16.0.0 [`00935064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935064.md) FUN_00935064

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00935200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935200.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`009351e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009351e4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00935200",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "009351e4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1c2c729119ad02334972ba180d5d982e"></a>

### v16.0.0 [`00935400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935400.md) FUN_00935400

`competing_candidates` 

呼出元 1件 [`009b873c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md) · 呼出先 3件 [`00935514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md) [`00acb85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb85c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

- 1. [`0093559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093559c.md) · スコア 31.836735 · 採用条件未達 · 順位差 18.367347000000002 / 17.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`004e4654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4654.md) · スコア 13.469388 · 採用条件未達 · 順位差 -18.367347000000002 / 13.469388 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008ff67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff67c.md) · スコア 12.244898 · 採用条件未達 · 順位差 -19.591837 / 12.244898 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md) · スコア 11.37931 · 採用条件未達 · 順位差 -20.457425 / 11.37931 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a3ec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md) · スコア 7.346939 · 採用条件未達 · 順位差 -24.489796000000002 / 7.346939 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) · スコア 5.882353 · 採用条件未達 · 順位差 -25.954382000000003 / 5.882353 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0072ba9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072ba9c.md) · スコア 5.333333 · 採用条件未達 · 順位差 -26.503402 / 5.333333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) · スコア 4.054054 · 採用条件未達 · 順位差 -27.782681 / 4.054054 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5306122448979592,
          0.5306122448979592
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
        "margin": 18.367347000000002,
        "reverse_margin": 17.142857
      },
      "new": "0093559c",
      "score": 31.836735
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22448979591836735,
          0.3793103448275862
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
        "margin": -18.367347000000002,
        "reverse_margin": 13.469388
      },
      "new": "004e4654",
      "score": 13.469388
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20408163265306123,
          0.21739130434782608
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
        "margin": -19.591837,
        "reverse_margin": 12.244898
      },
      "new": "008ff67c",
      "score": 12.244898
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd1c6176a2f99fde1ca1518ee48af3e6"></a>

### v16.0.0 [`009385d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d0.md) FUN_009385d0

`competing_candidates` [`0093876c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/0093876c.md)

呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00938364",
    "009385d8",
    "00938500",
    "00938774"
  ],
  "initial_reason": ""
}
~~~

<a id="review-039556db291261e5ad701faaa4a86a37"></a>

### v16.0.0 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) FUN_009470d0

`competing_candidates` 

呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 112件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)

- 1. [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · スコア 53.623305 · 採用条件未達 · 順位差 41.525098 / 41.479896000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · スコア 12.098207 · 採用条件未達 · 順位差 -41.525098 / -49.526734 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · スコア 10.169837 · 採用条件未達 · 順位差 -43.453468 / 10.169837 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere
- 4. [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · スコア 10.124517 · 採用条件未達 · 順位差 -43.498788000000005 / -74.989581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · スコア 10.103758 · 採用条件未達 · 順位差 -43.519547 / -37.770516 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · スコア 10.073539 · 採用条件未達 · 順位差 -43.549766000000005 / -44.162302 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · スコア 10.043444 · 採用条件未達 · 順位差 -43.579861 / -37.413455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · スコア 10.008171 · 採用条件未達 · 順位差 -43.615134 / -30.948542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.49720822552090427,
          0.49720822552090427
        ],
        "cfg_coverage": [
          0.3895405669599218,
          0.39632023868722027
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 41.525098,
        "reverse_margin": 41.479896000000004
      },
      "new": "0094726c",
      "score": 53.623305
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0016342094511779927,
          0.0015103838892385148
        ],
        "cfg_coverage": [
          0.0004887585532746823,
          0.0003792188092529389
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -41.525098,
        "reverse_margin": -49.526734
      },
      "new": "00ad6f4c",
      "score": 12.098207
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.00217894593490399,
          0.0043091839482897925
        ],
        "cfg_coverage": [
          0.0019550342130987292,
          0.0028169014084507044
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "already_matched_elsewhere"
        ],
        "margin": -43.453468,
        "reverse_margin": 10.169837
      },
      "new": "00a75dac",
      "score": 10.169837
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bc1dcb013e832615f10c7a15b14cd26a"></a>

### v16.0.0 [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) FUN_00963e3c

`competing_candidates` 

呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 82件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md)

- 1. [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · スコア 47.456899 · 採用条件未達 · 順位差 35.359223 / 35.365142 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · スコア 12.097676 · 採用条件未達 · 順位差 -35.359223 / -45.539776 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · スコア 10.147995 · 採用条件未達 · 順位差 -37.308904 / -79.121353 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · スコア 10.080077 · 採用条件未達 · 順位差 -37.376822000000004 / -43.543228 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · スコア 10.073997 · 採用条件未達 · 順位差 -37.382902 / -37.800277 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · スコア 10.053278 · 採用条件未達 · 順位差 -37.403621 / -51.571663 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · スコア 10.017759 · 採用条件未達 · 順位差 -37.43914 / -21.46096 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`0091ab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091ab78.md) · スコア 8.17074 · 採用条件未達 · 順位差 -39.286159 / 8.17074 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.46031276207389865,
          0.46031276207389865
        ],
        "cfg_coverage": [
          0.19272001994515084,
          0.19190665342601787
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 35.359223,
        "reverse_margin": 35.365142
      },
      "new": "00963fd8",
      "score": 47.456899
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.001627941394109812,
          0.0035900783289817234
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -35.359223,
        "reverse_margin": -45.539776
      },
      "new": "00ae128c",
      "score": 12.097676
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0024665778698633517,
          0.0030566083873334146
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -37.308904,
        "reverse_margin": -79.121353
      },
      "new": "007df0e8",
      "score": 10.147995
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d4093bd2dba17568c53d686ab489de57"></a>

### v16.0.0 [`0097d048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d048.md) FUN_0097d048

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00a99fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a99fe4.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0097d1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d1e4.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 30.0,
        "reverse_margin": 0.0
      },
      "new": "00a99fe4",
      "score": 80.0
    },
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
        "margin": -30.0,
        "reverse_margin": 50.0
      },
      "new": "0097d1e4",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1297d64f9e507a7a478518e3b9e78d5b"></a>

### v16.0.0 [`0097d058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d058.md) FUN_0097d058

`competing_candidates` 

呼出元 1件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 0件 

- 1. [`0097d1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d1f4.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`0097d1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d1e4.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d1f4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d1e4",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-019dd041678a312f6cc0a489a4d04b12"></a>

### v16.0.0 [`0097d0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d0a8.md) FUN_0097d0a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d244.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0097d244",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-453cb6c1c719cf5f7356af81c81c8b1b"></a>

### v16.0.0 [`0097d0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d0c4.md) FUN_0097d0c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d260.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0097d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d244.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d260",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d244",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-aed54d43e85b82490cccf1ff33c0476a"></a>

### v16.0.0 [`0097d10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d10c.md) FUN_0097d10c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d2a8.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 60.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "0097d2a8",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a67c271be68bb6459ed7cff46c164be4"></a>

### v16.0.0 [`0097d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d124.md) FUN_0097d124

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d2c0.md) · スコア 69.0 · 採用条件未達 · 順位差 68.3333 / 68.3333 · 
- 2. [`0097d2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d2a8.md) · スコア 0.6667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.3333,
        "reverse_margin": 68.3333
      },
      "new": "0097d2c0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d2a8",
      "score": 0.6667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fe67d6c25ec1f755b4e3225e294c3e84"></a>

### v16.0.0 [`0097d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d3e0.md) FUN_0097d3e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d57c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0097d57c",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-803fcfe15302b75a4e149d99303759ef"></a>

### v16.0.0 [`0097d3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d3fc.md) FUN_0097d3fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d598.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0097d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d57c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d598",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d57c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4f4515e3135c5765ddb8e07b9ef1a40e"></a>

### v16.0.0 [`0097d67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d67c.md) FUN_0097d67c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d818.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0097d818",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-376afb4b0d94e2867b1fc01ed2569570"></a>

### v16.0.0 [`0097d698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d698.md) FUN_0097d698

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d834.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0097d818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d818.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d834",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d818",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8e963c1fed0e3594528712e31826ff0f"></a>

### v16.0.0 [`0097d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6cc.md) FUN_0097d6cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008fade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fade4.md) · スコア 80.0 · 採用条件未達 · 順位差 30.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`0097d868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d868.md) · スコア 50.0 · 採用条件未達 · 順位差 -30.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 30.0,
        "reverse_margin": 80.0
      },
      "new": "008fade4",
      "score": 80.0
    },
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
        "margin": -30.0,
        "reverse_margin": -30.0
      },
      "new": "0097d868",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-103e5bdc5f523124281579bd1ea7c41b"></a>

### v16.0.0 [`0097d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6dc.md) FUN_0097d6dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d878.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`0097d868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d868.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d878",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d868",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7decce44b3638166d3950bb3d019f959"></a>

### v16.0.0 [`0097d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7b0.md) FUN_0097d7b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d94c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0097d94c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5157822fed6fc2f31983bc3f3fa8ceeb"></a>

### v16.0.0 [`0097d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7cc.md) FUN_0097d7cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d968.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0097d94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d94c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d968",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d94c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3c8bc1fcc3baf057a208579d3f27b97f"></a>

### v16.0.0 [`0097d800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d800.md) FUN_0097d800

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d99c.md) · スコア 50.0 · 採用条件未達 · 順位差 50.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0097d99c",
      "score": 50.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6531f85358a821f07ef55990605ce68f"></a>

### v16.0.0 [`0097d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d810.md) FUN_0097d810

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0097d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d9ac.md) · スコア 69.0 · 採用条件未達 · 順位差 68.0 / 68.0 · 
- 2. [`0097d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d99c.md) · スコア 1.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0097d9ac",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0097d99c",
      "score": 1.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

