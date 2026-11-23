# v15.7.3 → v15.7.4 · 追加調査 (24)

[一覧の目次](README.md)

<a id="review-c45bf513cf0a407121f4b534c6f5e119"></a>

### v15.7.4 [`0052dd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd0c.md) FUN_0052dd0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0052dd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd0c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052dcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dcf4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0052dd0c",
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
        "margin": -80.0,
        "reverse_margin": -54.285714
      },
      "new": "0052dcf4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d67d3d0d86b482f57d565d8d743d56d9"></a>

### v15.7.4 [`0052de58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de58.md) thunk_FUN_0055bd48

`competing_candidates` 

呼出元 1件 [`0045fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) · 呼出先 1件 [`0055bd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd48.md)

- 1. [`0052de58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052de58.md) · スコア 84.0 · 採用条件未達 · 順位差 18.7333 / 18.7333 · 
- 2. [`0055bd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055bd48.md) · スコア 65.2667 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 18.7333,
        "reverse_margin": 18.7333
      },
      "new": "0052de58",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0055bd48",
      "score": 65.2667
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-09f211aaf7f4127c299368f223c74dac"></a>

### v15.7.4 [`0052e5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e5b0.md) FUN_0052e5b0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 76.756757 · 採用条件未達 · 順位差 52.019915 / 52.019915 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 24.736842 · 採用条件未達 · 順位差 -48.94736900000001 / -52.019915 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -76.756757 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -76.756757 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -76.756757 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9459459459459459,
          0.9459459459459459
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
        "margin": 52.019915,
        "reverse_margin": 52.019915
      },
      "new": "0052e5b0",
      "score": 76.756757
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07894736842105263,
          0.08108108108108109
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
        "margin": -48.94736900000001,
        "reverse_margin": -52.019915
      },
      "new": "0052ea94",
      "score": 24.736842
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
        "margin": -68.648649,
        "reverse_margin": -76.756757
      },
      "new": "0052e644",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f3edaa2530451a05e25f02cd6e67859a"></a>

### v15.7.4 [`0052e644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e644.md) FUN_0052e644

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 68.648649 · 採用条件未達 · 順位差 68.648649 / 68.648649 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -68.648649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.684211 / -68.648649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -68.648649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -68.648649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8108108108108109,
          0.8108108108108109
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
        "margin": 68.648649,
        "reverse_margin": 68.648649
      },
      "new": "0052e644",
      "score": 68.648649
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
        "margin": -76.756757,
        "reverse_margin": -68.648649
      },
      "new": "0052e5b0",
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
        "margin": -73.684211,
        "reverse_margin": -68.648649
      },
      "new": "0052ea94",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0268b965988abc9dd38ba36ddca28e2e"></a>

### v15.7.4 [`0052e6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e6d8.md) FUN_0052e6d8

`competing_candidates` 

呼出元 1件 [`0052e91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e91c.md) · 呼出先 2件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md) [`00bdb540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb540.md)

- 1. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 78.344828 · 採用条件未達 · 順位差 71.02775500000001 / 71.02775500000001 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00538fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fd0.md) · スコア 7.317073 · 採用条件未達 · 順位差 -63.53658599999999 / -71.02775500000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0044881c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/0044881c.md) · スコア 2.068966 · 採用条件未達 · 順位差 2.068966 / -76.275862 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00448aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448aac.md) · スコア 2.068966 · 採用条件未達 · 順位差 2.068966 / -76.275862 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00448d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448d80.md) · スコア 2.068966 · 採用条件未達 · 順位差 2.068966 / -76.275862 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) · スコア 1.655172 · 採用条件未達 · 順位差 1.655172 / -76.68965600000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -78.344828 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.2 / -78.344828 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9724137931034482,
          0.9724137931034482
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
        "margin": 71.02775500000001,
        "reverse_margin": 71.02775500000001
      },
      "new": "0052e6d8",
      "score": 78.344828
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12195121951219512,
          0.13793103448275862
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
        "margin": -63.53658599999999,
        "reverse_margin": -71.02775500000001
      },
      "new": "00538fd0",
      "score": 7.317073
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.050505050505050504,
          0.034482758620689655
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
        "margin": 2.068966,
        "reverse_margin": -76.275862
      },
      "new": "0044881c",
      "score": 2.068966
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8ca00ddebc21be9bbee5d2c6ed1a607c"></a>

### v15.7.4 [`0052e91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e91c.md) FUN_0052e91c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0052e6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e6d8.md)

- 1. [`0052e91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e91c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0052ea8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea8c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0052e91c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0052ea8c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-10686bf877d58e928f12b0676c92b4ad"></a>

### v15.7.4 [`0052e924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e924.md) FUN_0052e924

`competing_candidates` 

呼出元 1件 [`0052ea8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052ea8c.md) · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 78.666667 · 採用条件未達 · 順位差 78.666667 / 78.666667 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.684211 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.2 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052ed84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ed84.md) · スコア 0.0 · 採用条件未達 · 順位差 -72.58427 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00538acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538acc.md) · スコア 0.0 · 採用条件未達 · 順位差 -77.073171 / -78.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9777777777777777,
          0.9777777777777777
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
        "margin": 78.666667,
        "reverse_margin": 78.666667
      },
      "new": "0052e924",
      "score": 78.666667
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
        "margin": -76.756757,
        "reverse_margin": -78.666667
      },
      "new": "0052e5b0",
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
        "margin": -68.648649,
        "reverse_margin": -78.666667
      },
      "new": "0052e644",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-335899fa3bbd5b2b89f00b862524671f"></a>

### v15.7.4 [`0052ea8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052ea8c.md) FUN_0052ea8c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0052e924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e924.md)

- 1. [`0052ea8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea8c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0052e91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e91c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0052ea8c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0052e91c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fe7ea543fca5b4a8b5550f11ca6baebe"></a>

### v15.7.4 [`0052ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052ea94.md) FUN_0052ea94

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 73.684211 · 採用条件未達 · 順位差 48.94736900000001 / 48.94736900000001 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 24.736842 · 採用条件未達 · 順位差 -52.019915 / -48.94736900000001 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 4.615385 · 採用条件未達 · 順位差 -55.76922999999999 / -69.068826 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -73.684211 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -73.684211 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8947368421052632,
          0.8947368421052632
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
        "margin": 48.94736900000001,
        "reverse_margin": 48.94736900000001
      },
      "new": "0052ea94",
      "score": 73.684211
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08108108108108109,
          0.07894736842105263
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
        "margin": -52.019915,
        "reverse_margin": -48.94736900000001
      },
      "new": "0052e5b0",
      "score": 24.736842
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.10526315789473684
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
        "margin": -55.76922999999999,
        "reverse_margin": -69.068826
      },
      "new": "005389fc",
      "score": 4.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cd50d7e0af4a7019abc03773d2cf47b0"></a>

### v15.7.4 [`0052eb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eb2c.md) FUN_0052eb2c

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md) [`00bdb540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb540.md)

- 1. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 75.2 · 採用条件未達 · 順位差 73.004878 / 73.004878 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00538fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fd0.md) · スコア 2.195122 · 採用条件未達 · 順位差 -68.658537 / -73.004878 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -75.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -75.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0052ed84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ed84.md) · スコア 0.0 · 採用条件未達 · 順位差 -72.58427 / -75.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00538acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538acc.md) · スコア 0.0 · 採用条件未達 · 順位差 -77.073171 / -75.2 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.92,
          0.92
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
        "margin": 73.004878,
        "reverse_margin": 73.004878
      },
      "new": "0052eb2c",
      "score": 75.2
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.036585365853658534,
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
        "margin": -68.658537,
        "reverse_margin": -73.004878
      },
      "new": "00538fd0",
      "score": 2.195122
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
        "margin": -78.344828,
        "reverse_margin": -75.2
      },
      "new": "0052e6d8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6cb7391b5fcae7afbbe0884fdf98e804"></a>

### v15.7.4 [`0052ed84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052ed84.md) FUN_0052ed84

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`0052ed84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ed84.md) · スコア 72.58427 · 採用条件未達 · 順位差 72.58427 / 72.58427 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.684211 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.2 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.384615 / -72.58427 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8764044943820225,
          0.8764044943820225
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
        "margin": 72.58427,
        "reverse_margin": 72.58427
      },
      "new": "0052ed84",
      "score": 72.58427
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
        "margin": -76.756757,
        "reverse_margin": -72.58427
      },
      "new": "0052e5b0",
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
        "margin": -68.648649,
        "reverse_margin": -72.58427
      },
      "new": "0052e644",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c7a38d2829b206cf263c8f4e7e57d54d"></a>

### v15.7.4 [`005377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377cc.md) thunk_FUN_0056cdd4

`competing_candidates` 

呼出元 3件 [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md) · 呼出先 1件 [`0056cdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdd4.md)

- 1. [`005377cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377cc.md) · スコア 36.0 · 採用条件未達 · 順位差 19.7368 / 19.7368 · 
- 2. [`005377d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d0.md) · スコア 16.2632 · 採用条件未達 · 順位差 — / — · 
- 3. [`005377d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d4.md) · スコア 8.2419 · 採用条件未達 · 順位差 — / — · 
- 4. [`005377d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d8.md) · スコア 8.2174 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 19.7368,
        "reverse_margin": 19.7368
      },
      "new": "005377cc",
      "score": 36.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d0",
      "score": 16.2632
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d4",
      "score": 8.2419
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-698ac75cdad2117c7de95de67217ddb3"></a>

### v15.7.4 [`005377d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d0.md) thunk_FUN_0056d008

`competing_candidates` 

呼出元 3件 [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) [`00444fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md) · 呼出先 1件 [`0056d008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d008.md)

- 1. [`005377d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d0.md) · スコア 35.0909 · 採用条件未達 · 順位差 18.8277 / 18.8277 · 
- 2. [`005377cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377cc.md) · スコア 16.2632 · 採用条件未達 · 順位差 — / — · 
- 3. [`005377d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d4.md) · スコア 11.5417 · 採用条件未達 · 順位差 — / — · 
- 4. [`005377d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d8.md) · スコア 10.3494 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 18.8277,
        "reverse_margin": 18.8277
      },
      "new": "005377d0",
      "score": 35.0909
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377cc",
      "score": 16.2632
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d4",
      "score": 11.5417
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-65812cfdee024cbdef6d2d6c0199799c"></a>

### v15.7.4 [`005377d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d4.md) thunk_FUN_0056d028

`competing_candidates` 

呼出元 1件 [`00444fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md) · 呼出先 1件 [`0056d028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d028.md)

- 1. [`005377d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d4.md) · スコア 27.8592 · 採用条件未達 · 順位差 16.3175 / 16.3175 · 
- 2. [`005377d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d0.md) · スコア 11.5417 · 採用条件未達 · 順位差 — / — · 
- 3. [`005377d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d8.md) · スコア 11.4756 · 採用条件未達 · 順位差 — / — · 
- 4. [`005377cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377cc.md) · スコア 8.2419 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 16.3175,
        "reverse_margin": 16.3175
      },
      "new": "005377d4",
      "score": 27.8592
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d0",
      "score": 11.5417
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d8",
      "score": 11.4756
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bb55c1c96cf03aabc2dd08bc78c4b45f"></a>

### v15.7.4 [`005377d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d8.md) thunk_FUN_0056d050

`competing_candidates` 

呼出元 1件 [`00444fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md) · 呼出先 1件 [`0056d050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d050.md)

- 1. [`005377d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d8.md) · スコア 31.1429 · 採用条件未達 · 順位差 19.6673 / 19.6673 · 
- 2. [`005377d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d4.md) · スコア 11.4756 · 採用条件未達 · 順位差 — / — · 
- 3. [`005377d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377d0.md) · スコア 10.3494 · 採用条件未達 · 順位差 — / — · 
- 4. [`005377cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377cc.md) · スコア 8.2174 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 19.6673,
        "reverse_margin": 19.6673
      },
      "new": "005377d8",
      "score": 31.1429
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d4",
      "score": 11.4756
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005377d0",
      "score": 10.3494
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6ba3d1dc95c5f101b0f135a823fa8aa0"></a>

### v15.7.4 [`005389fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005389fc.md) FUN_005389fc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 60.384615 · 採用条件未達 · 順位差 15.0 / 15.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 45.384615 · 採用条件未達 · 順位差 -15.0 / -15.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 4.615385 · 採用条件未達 · 順位差 -69.068826 / -55.76922999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00538d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538d5c.md) · スコア 4.07767 · 採用条件未達 · 順位差 -69.514563 / -56.306945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00539268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539268.md) · スコア 4.07767 · 採用条件未達 · 順位差 -72.427184 / -56.306945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6730769230769231,
          0.6730769230769231
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
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "005389fc",
      "score": 60.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4230769230769231,
          0.4230769230769231
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
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "00538ef8",
      "score": 45.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.10526315789473684,
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
        "margin": -69.068826,
        "reverse_margin": -55.76922999999999
      },
      "new": "0052ea94",
      "score": 4.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a1b2b66418d74f4d46744e1f22b5ddcf"></a>

### v15.7.4 [`00538acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538acc.md) FUN_00538acc

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md) [`00bdb540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb540.md)

- 1. [`00538acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538acc.md) · スコア 77.073171 · 採用条件未達 · 順位差 75.609756 / 75.609756 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00539268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539268.md) · スコア 1.463415 · 採用条件未達 · 順位差 -75.041439 / -75.609756 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -77.073171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.2 / -77.073171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00538d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538d5c.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.592233 / -77.073171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00538fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fd0.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.853659 / -77.073171 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9512195121951219,
          0.9512195121951219
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
        "margin": 75.609756,
        "reverse_margin": 75.609756
      },
      "new": "00538acc",
      "score": 77.073171
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.038834951456310676,
          0.024390243902439025
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
        "margin": -75.041439,
        "reverse_margin": -75.609756
      },
      "new": "00539268",
      "score": 1.463415
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
        "margin": -78.344828,
        "reverse_margin": -77.073171
      },
      "new": "0052e6d8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e977fa4d485e0c70e0683a2b95b5ce41"></a>

### v15.7.4 [`00538d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538d5c.md) FUN_00538d5c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`00538d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538d5c.md) · スコア 73.592233 · 採用条件未達 · 順位差 69.514563 / 69.514563 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 4.07767 · 採用条件未達 · 順位差 -56.306945 / -69.514563 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 4.07767 · 採用条件未達 · 順位差 -56.306945 / -69.514563 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00539268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539268.md) · スコア 4.07767 · 採用条件未達 · 順位差 -72.427184 / -69.514563 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -73.592233 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -73.592233 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -73.592233 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -73.592233 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8932038834951457,
          0.8932038834951457
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
        "margin": 69.514563,
        "reverse_margin": 69.514563
      },
      "new": "00538d5c",
      "score": 73.592233
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1346153846153846,
          0.06796116504854369
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
        "margin": -56.306945,
        "reverse_margin": -69.514563
      },
      "new": "005389fc",
      "score": 4.07767
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1346153846153846,
          0.06796116504854369
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
        "margin": -56.306945,
        "reverse_margin": -69.514563
      },
      "new": "00538ef8",
      "score": 4.07767
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-51f073da595842e7e88dcfd27abfb8c4"></a>

### v15.7.4 [`00538ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538ef8.md) FUN_00538ef8

`competing_candidates` 

呼出元 1件 [`00538fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538fc8.md) · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 60.384615 · 採用条件未達 · 順位差 15.0 / 15.0 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 45.384615 · 採用条件未達 · 順位差 -15.0 / -15.0 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00538d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538d5c.md) · スコア 4.07767 · 採用条件未達 · 順位差 -69.514563 / -56.306945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00539268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539268.md) · スコア 4.07767 · 採用条件未達 · 順位差 -72.427184 / -56.306945 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0052e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e5b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -76.756757 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052e644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e644.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.648649 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.684211 / -60.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6730769230769231,
          0.6730769230769231
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
        "margin": 15.0,
        "reverse_margin": 15.0
      },
      "new": "00538ef8",
      "score": 60.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4230769230769231,
          0.4230769230769231
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
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "005389fc",
      "score": 45.384615
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06796116504854369,
          0.1346153846153846
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
        "margin": -69.514563,
        "reverse_margin": -56.306945
      },
      "new": "00538d5c",
      "score": 4.07767
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9e0b4a7a7782bba5cd2d7476be7dace2"></a>

### v15.7.4 [`00538fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538fc8.md) FUN_00538fc8

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00538ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538ef8.md)

- 1. [`00538fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fc8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00539260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539260.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539404.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00538fc8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539260",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539404",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-da7a8c3a52e4fdaf88f6f2cedad49509"></a>

### v15.7.4 [`00538fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538fd0.md) FUN_00538fd0

`competing_candidates` 

呼出元 1件 [`00539260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539260.md) · 呼出先 2件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md) [`00bdb540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb540.md)

- 1. [`00538fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fd0.md) · スコア 70.853659 · 採用条件未達 · 順位差 63.53658599999999 / 63.53658599999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 7.317073 · 採用条件未達 · 順位差 -71.02775500000001 / -63.53658599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0052eb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eb2c.md) · スコア 2.195122 · 採用条件未達 · 順位差 -73.004878 / -68.658537 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) · スコア 0.0 · 採用条件未達 · 順位差 -1.655172 / -70.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0044881c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/0044881c.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.068966 / -70.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00448aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448aac.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.068966 / -70.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00448d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448d80.md) · スコア 0.0 · 採用条件未達 · 順位差 -2.068966 / -70.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00538acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538acc.md) · スコア 0.0 · 採用条件未達 · 順位差 -77.073171 / -70.853659 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8475609756097561,
          0.8475609756097561
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
        "margin": 63.53658599999999,
        "reverse_margin": 63.53658599999999
      },
      "new": "00538fd0",
      "score": 70.853659
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13793103448275862,
          0.12195121951219512
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
        "margin": -71.02775500000001,
        "reverse_margin": -63.53658599999999
      },
      "new": "0052e6d8",
      "score": 7.317073
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04,
          0.036585365853658534
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
        "margin": -73.004878,
        "reverse_margin": -68.658537
      },
      "new": "0052eb2c",
      "score": 2.195122
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7fd20e33eeb2ddddbc9fe756472a48d1"></a>

### v15.7.4 [`00539260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539260.md) FUN_00539260

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00538fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538fd0.md)

- 1. [`00539260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539260.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00538fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fc8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539404.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00539260",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00538fc8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539404",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

### v15.7.4 [`00539268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539268.md) FUN_00539268

`competing_candidates` 

呼出元 1件 [`00539404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539404.md) · 呼出先 1件 [`0056d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d180.md)

- 1. [`00539268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539268.md) · スコア 76.504854 · 採用条件未達 · 順位差 72.427184 / 72.427184 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`005389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005389fc.md) · スコア 4.07767 · 採用条件未達 · 順位差 -56.306945 / -72.427184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00538d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538d5c.md) · スコア 4.07767 · 採用条件未達 · 順位差 -69.514563 / -72.427184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00538ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538ef8.md) · スコア 4.07767 · 採用条件未達 · 順位差 -56.306945 / -72.427184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00538acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538acc.md) · スコア 1.463415 · 採用条件未達 · 順位差 -75.609756 / -75.041439 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0052e6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e6d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.344828 / -76.504854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0052e924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e924.md) · スコア 0.0 · 採用条件未達 · 順位差 -78.666667 / -76.504854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0052ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052ea94.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.684211 / -76.504854 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.941747572815534,
          0.941747572815534
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
        "margin": 72.427184,
        "reverse_margin": 72.427184
      },
      "new": "00539268",
      "score": 76.504854
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1346153846153846,
          0.06796116504854369
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
        "margin": -56.306945,
        "reverse_margin": -72.427184
      },
      "new": "005389fc",
      "score": 4.07767
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06796116504854369,
          0.06796116504854369
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
        "margin": -69.514563,
        "reverse_margin": -72.427184
      },
      "new": "00538d5c",
      "score": 4.07767
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d1b25b261c7acd3748313cff481de362"></a>

### v15.7.4 [`00539404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539404.md) FUN_00539404

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00539268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539268.md)

- 1. [`00539404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539404.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00538fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538fc8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539260.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00539404",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00538fc8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539260",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab27441881fa584731e7a7ee2d40a1ad"></a>

### v15.7.4 [`005397cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397cc.md) FUN_005397cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005397cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397cc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005397cc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bfbe24df32178ce447b4cc19797393b0"></a>

### v15.7.4 [`005397dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397dc.md) FUN_005397dc

`competing_candidates` [`005397dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397dc.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
  ],
  "initial_reason": ""
}
~~~

<a id="review-a0ed6100d9d70124173818edbfea446a"></a>

### v15.7.4 [`005397e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397e4.md) FUN_005397e4

`competing_candidates` [`005397e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397e4.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
  ],
  "initial_reason": ""
}
~~~

<a id="review-905fffe7aa8537d7b4a98b9c137bb703"></a>

### v15.7.4 [`005397f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397f0.md) FUN_005397f0

`competing_candidates` [`005397f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397f0.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
  ],
  "initial_reason": ""
}
~~~

<a id="review-e0c7fc983ec3592067d5a89f145d5f35"></a>

### v15.7.4 [`00539b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b1c.md) FUN_00539b1c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00539b1c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0053c5d8",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-dbe6cc1b9a334c6ccc3ed8d7cfda94d3"></a>

### v15.7.4 [`0053b730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b730.md) FUN_0053b730

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053b730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b730.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0053b730",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3ddf61a5d564616f21976b50e0ae2b55"></a>

### v15.7.4 [`0053bdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdb4.md) FUN_0053bdb4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053bdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdb4.md) · スコア 80.0 · 採用条件未達 · 順位差 15.0 / 15.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`004cc408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc408.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0050d718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d718.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00510684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510684.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0053bdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdcc.md) · スコア 60.0 · 採用条件未達 · 順位差 -20.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`0055fa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fa98.md) · スコア 56.0 · 採用条件未達 · 順位差 -6.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00560124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560124.md) · スコア 56.0 · 採用条件未達 · 順位差 -6.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005659c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005659c0.md) · スコア 36.666667 · 採用条件未達 · 順位差 -43.333333 / -43.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0053bdb4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
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
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "004cc408",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
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
        "margin": -15.0,
        "reverse_margin": -15.0
      },
      "new": "0050d718",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-36bbf75cc8f32815c3f0d1e36e276ff1"></a>

### v15.7.4 [`0053bdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdcc.md) FUN_0053bdcc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053bdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdcc.md) · スコア 80.0 · 採用条件未達 · 順位差 15.0 / 15.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`004cc044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004cc044.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0053bdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdb4.md) · スコア 60.0 · 採用条件未達 · 順位差 -20.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`004ccf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf1c.md) · スコア 50.0 · 採用条件未達 · 順位差 -15.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004cd6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cd6ec.md) · スコア 50.0 · 採用条件未達 · 順位差 -15.0 / -30.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005659d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005659d8.md) · スコア 40.0 · 採用条件未達 · 順位差 -40.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0053bde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bde4.md) · スコア 17.142857 · 採用条件未達 · 順位差 -62.857143 / -62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "0053bdcc",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.75,
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
        "reverse_margin": -15.0
      },
      "new": "004cc044",
      "score": 65.0
    },
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
        "margin": -20.0,
        "reverse_margin": -20.0
      },
      "new": "0053bdb4",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8ddd7f7e74594716bd3d38137a4bd7be"></a>

### v15.7.4 [`0053bde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bde4.md) FUN_0053bde4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053bde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bde4.md) · スコア 80.0 · 採用条件未達 · 順位差 21.904761999999998 / 21.904761999999998 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005659f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005659f0.md) · スコア 58.095238 · 採用条件未達 · 順位差 -21.904761999999998 / -21.904761999999998 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 3. [`0053bdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdb4.md) · スコア 17.142857 · 採用条件未達 · 順位差 -62.857143 / -62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0053bdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdcc.md) · スコア 17.142857 · 採用条件未達 · 順位差 -62.857143 / -62.857143 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 21.904761999999998,
        "reverse_margin": 21.904761999999998
      },
      "new": "0053bde4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8571428571428571,
          0.8571428571428571
        ],
        "cfg_coverage": [
          0.5,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -21.904761999999998,
        "reverse_margin": -21.904761999999998
      },
      "new": "005659f0",
      "score": 58.095238
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.2857142857142857
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
        "margin": -62.857143,
        "reverse_margin": -62.857143
      },
      "new": "0053bdb4",
      "score": 17.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-388c881df87f0ed7cda8456448e4e8db"></a>

### v15.7.4 [`0053be00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be00.md) FUN_0053be00

`competing_candidates` [`0053be00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be00.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "0053bdb0",
    "0053be08",
    "0053bdb0",
    "0053be08"
  ],
  "initial_reason": ""
}
~~~

<a id="review-d72016f439508d1db7b7684fbbb369a3"></a>

### v15.7.4 [`0053c5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5d8.md) FUN_0053c5d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0053c5d8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a58be401c016eb37b09f461a126b69b5"></a>

### v15.7.4 [`0053d8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8ac.md) FUN_0053d8ac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053d8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8ac.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0053d8ac",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8ba65ce67cbb8382b95a260ca07fdb9b"></a>

### v15.7.4 [`0053dc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc2c.md) FUN_0053dc2c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc2c.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0053dc2c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-378452e7724abfb1e739c4de3d5143a0"></a>

### v15.7.4 [`0053dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd2c.md) FUN_0053dd2c

`competing_candidates` [`0053dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd2c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "0053dce0",
    "0053dd34",
    "0053dce0",
    "0053dd34"
  ],
  "initial_reason": ""
}
~~~

<a id="review-069e9d21c84644ee156877b0841b8b63"></a>

### v15.7.4 [`0053dd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd74.md) FUN_0053dd74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0053dd74",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4455aff322740d4dd337a07c43428d51"></a>

### v15.7.4 [`0053dd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd84.md) FUN_0053dd84

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd84.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0053dd84",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c5f38f1b3f5c8bce59ec0b9c20f4aa46"></a>

### v15.7.4 [`0053dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd8c.md) FUN_0053dd8c

`competing_candidates` [`0053dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd8c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "0053dd88",
    "0053dd9c",
    "0053dd88",
    "0053dd9c"
  ],
  "initial_reason": ""
}
~~~

<a id="review-6af49b55eee1743fe5cadf70111ee907"></a>

### v15.7.4 [`0053dd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd94.md) FUN_0053dd94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd94.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0053dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd98.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0053dd94",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0053dd98",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d2df06477387daa82d2e1247a4c505e8"></a>

### v15.7.4 [`0053dd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd98.md) FUN_0053dd98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd98.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0053dd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd94.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0053dd98",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0053dd94",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ed14ca668989b96b51dd404aa4120b49"></a>

### v15.7.4 [`0053df38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053df38.md) FUN_0053df38

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053df38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053df38.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "0053df38",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c89109c1a217a8d4608a853cd9383171"></a>

### v15.7.4 [`0053dffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dffc.md) FUN_0053dffc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053dffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dffc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0053dffc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5f5da5bb7576de8b849929a1a84d9d89"></a>

### v15.7.4 [`0053e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e0fc.md) FUN_0053e0fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0053e0fc",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-745fe221c0a35fc6fba98af63fd71c15"></a>

### v15.7.4 [`0053e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e10c.md) FUN_0053e10c

`competing_candidates` 

呼出元 1件 [`005425e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005425e4.md) · 呼出先 0件 

- 1. [`0053e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e10c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0054e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e8f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005524e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005524e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00552510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552510.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "0053e10c",
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
      "new": "0054e8f0",
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
      "new": "005524e0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6bd218a9df328ef2c5b445b9974807ca"></a>

### v15.7.4 [`00540958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540958.md) FUN_00540958

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00540958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540958.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00540958",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f7f5a7fe566afaa4d8f9f4da3ebdffd7"></a>

### v15.7.4 [`00540f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f0c.md) FUN_00540f0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00540f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540f0c.md) · スコア 80.0 · 採用条件未達 · 順位差 20.0 / 20.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`004cea84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004cea84.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) · スコア 13.548387 · 採用条件未達 · 順位差 13.548387 / -66.451613 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b77840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md) · スコア 11.666667 · 採用条件未達 · 順位差 11.666667 / -68.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b47ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md) · スコア 8.571429 · 採用条件未達 · 順位差 8.571429 / -71.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 20.0,
        "reverse_margin": 20.0
      },
      "new": "00540f0c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6666666666666666,
          0.7368421052631579
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
        "margin": 60.0,
        "reverse_margin": -20.0
      },
      "new": "004cea84",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22580645161290322,
          0.3684210526315789
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
        "margin": 13.548387,
        "reverse_margin": -66.451613
      },
      "new": "00bd7398",
      "score": 13.548387
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a25879a63e04141d55e5d9decb520004"></a>

### v15.7.4 [`00548154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548154.md) FUN_00548154

`competing_candidates` 

呼出元 1件 [`00458970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458970.md) · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)

- 1. [`00548154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548154.md) · スコア 67.777778 · 採用条件未達 · 順位差 67.777778 / 63.333334 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`004c8590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8590.md) · スコア 4.444444 · 採用条件未達 · 順位差 4.444444 / -63.333334 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00548244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548244.md) · スコア 0.0 · 採用条件未達 · 順位差 -70.0 / -67.777778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7962962962962963,
          0.7962962962962963
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
        "margin": 67.777778,
        "reverse_margin": 63.333334
      },
      "new": "00548154",
      "score": 67.777778
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12121212121212122,
          0.07407407407407407
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
        "margin": 4.444444,
        "reverse_margin": -63.333334
      },
      "new": "004c8590",
      "score": 4.444444
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
        "margin": -70.0,
        "reverse_margin": -67.777778
      },
      "new": "00548244",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cbbfc7b27f3de05fef564a53b833bdea"></a>

### v15.7.4 [`00548244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548244.md) FUN_00548244

`competing_candidates` 

呼出元 2件 [`004588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f0.md) [`0045cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cb74.md) · 呼出先 2件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)

- 1. [`00548244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/00548244.md) · スコア 70.0 · 採用条件未達 · 順位差 58.376623 / 58.376623 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`006acd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ac/006acd0c.md) · スコア 11.623377 · 採用条件未達 · 順位差 11.623377 / -58.376623 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005c322c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c322c.md) · スコア 10.909091 · 採用条件未達 · 順位差 10.909091 / -59.090908999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006aca10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ac/006aca10.md) · スコア 10.909091 · 採用条件未達 · 順位差 10.909091 / -59.090908999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00adf8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf8e0.md) · スコア 10.909091 · 採用条件未達 · 順位差 10.909091 / -59.090908999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00bbbdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) · スコア 10.0 · 採用条件未達 · 順位差 10.0 / -60.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`009e13ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e1/009e13ec.md) · スコア 6.593407 · 採用条件未達 · 順位差 6.593407 / -63.406593 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) · スコア 5.19685 · 採用条件未達 · 順位差 5.19685 / -64.80315 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 58.376623,
        "reverse_margin": 58.376623
      },
      "new": "00548244",
      "score": 70.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2926829268292683,
          0.18181818181818182
        ],
        "cfg_coverage": [
          0.09090909090909091,
          0.03571428571428571
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 11.623377,
        "reverse_margin": -58.376623
      },
      "new": "006acd0c",
      "score": 11.623377
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18461538461538463,
          0.18181818181818182
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
        "margin": 10.909091,
        "reverse_margin": -59.090908999999996
      },
      "new": "005c322c",
      "score": 10.909091
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0c9cc794a1d660803679e28ffd118543"></a>

### v15.7.4 [`00549064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549064.md) FUN_00549064

`competing_candidates` [`00549064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549064.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00548e1c",
    "0054906c",
    "00548e1c",
    "0054906c"
  ],
  "initial_reason": ""
}
~~~

<a id="review-b1763b5b8913f32e0522f28f458d145b"></a>

### v15.7.4 [`005490a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005490a0.md) FUN_005490a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00549118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549118.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005490a0",
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
      "new": "005490b0",
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
      "new": "005490f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b8fb233cf0b2bd20eb60ea6ce00a5873"></a>

### v15.7.4 [`005490b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005490b0.md) FUN_005490b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00549118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549118.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005490a0",
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
      "new": "005490b0",
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
      "new": "005490f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56933a5bc20dcfe15460c85a2c42c081"></a>

### v15.7.4 [`005490f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005490f0.md) FUN_005490f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00549118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549118.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 7. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 35.0 · 採用条件未達 · 順位差 -45.0 / -45.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005490a0",
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
      "new": "005490b0",
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
      "new": "005490f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e69d04f1420cbf7dc9d6b262dd4f5489"></a>

### v15.7.4 [`00549100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549100.md) FUN_00549100

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00549100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549100.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`004365e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365e8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 67.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 67.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 67.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 67.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 66.6 · 採用条件未達 · 順位差 — / — · 
- 8. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 66.6 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00549100",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "004365e8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005490a0",
      "score": 67.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eba5eb3b7bd5ff4f7b7cafad83a78a21"></a>

### v15.7.4 [`00549118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549118.md) FUN_00549118

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "",
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
      "new": "005490a0",
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
      "new": "005490b0",
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
      "new": "005490f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-47c6b93cd4ab0cef3eec3a06fc6a5283"></a>

### v15.7.4 [`0054923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/0054923c.md) FUN_0054923c

`competing_candidates` [`0054923c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/0054923c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "005491c4",
    "00549268",
    "005491c4",
    "00549268"
  ],
  "initial_reason": ""
}
~~~

<a id="review-4fa874faddb7aa787a477a85937624f9"></a>

### v15.7.4 [`00549244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549244.md) FUN_00549244

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00549244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549244.md) · スコア 80.0 · 採用条件未達 · 順位差 20.0 / 20.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00482414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482414.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`004925cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/004925cc.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004e0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e0/004e0718.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004e68c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e68c8.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a5c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5c524.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
        "margin": 20.0,
        "reverse_margin": 20.0
      },
      "new": "00549244",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8571428571428571,
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 60.0,
        "reverse_margin": -20.0
      },
      "new": "00482414",
      "score": 60.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8571428571428571,
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 60.0,
        "reverse_margin": -20.0
      },
      "new": "004925cc",
      "score": 60.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2e98c612491230d03bc97c3437809be9"></a>

### v15.7.4 [`005494d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494d8.md) FUN_005494d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494d8.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494dc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494e0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494d8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494dc",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494e0",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-108f7a8e44134eade21fd9c4877f06e4"></a>

### v15.7.4 [`005494dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494dc.md) FUN_005494dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494dc.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494d8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494e0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494dc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494d8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494e0",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-304925bbb32fe7d186c01b7b2cd08391"></a>

### v15.7.4 [`005494e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494e0.md) FUN_005494e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494e0.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494d8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494dc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494e0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494d8",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494dc",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3cac399d3b96041613eb19db1a81f604"></a>

### v15.7.4 [`005494f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494f0.md) FUN_005494f0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f0.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f4.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005494fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494fc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494f0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f4",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f8",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-bcc2b7ce2bad012eb2ca81d00476563d"></a>

### v15.7.4 [`005494f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494f4.md) FUN_005494f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f4.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005494fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494fc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00549500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549500.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494f4",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f8",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a7e10c8f7ecf49779f644f07e5c8b254"></a>

### v15.7.4 [`005494f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494f8.md) FUN_005494f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f8.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f4.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005494fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494fc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00549500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549500.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494f8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f4",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-993eca318a997964419520281960ff1d"></a>

### v15.7.4 [`005494fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/005494fc.md) FUN_005494fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005494fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494fc.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f0.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f4.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005494f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00549500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549500.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005494fc",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f0",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f4",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c806ef043e04ca080d76cd971c6faa6b"></a>

### v15.7.4 [`00549500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549500.md) FUN_00549500

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00549500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549500.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`005494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f4.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`005494f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494f8.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`005494fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005494fc.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00549500",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f4",
      "score": 54.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005494f8",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3a6b39c9a8c4c96bcf2ea47cf0d55025"></a>

### v15.7.4 [`00549580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549580.md) FUN_00549580

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00549580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549580.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00549580",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-36004eb77f46ee9ed5f12366fd417ea8"></a>

### v15.7.4 [`0054c7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054c7d8.md) FUN_0054c7d8

`competing_candidates` 

呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 0件 

- 1. [`0054c7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054c/0054c7d8.md) · スコア 78.77551 · 採用条件未達 · 順位差 78.77551 / 78.77551 · instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9795918367346939,
          0.9795918367346939
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
        "margin": 78.77551,
        "reverse_margin": 78.77551
      },
      "new": "0054c7d8",
      "score": 78.77551
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2740b589feb01141c5447ef2b3f22b9b"></a>

### v15.7.4 [`0054e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e39c.md) FUN_0054e39c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0054e39c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-88f8914a23bdca6dc78e06e3f10ae5cc"></a>

### v15.7.4 [`0054e8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e8f0.md) FUN_0054e8f0

`competing_candidates` 

呼出元 1件 [`00552480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552480.md) · 呼出先 0件 

- 1. [`0053e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e10c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0054e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e8f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005524e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005524e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00552510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552510.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "0053e10c",
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
      "new": "0054e8f0",
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
      "new": "005524e0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7b71565c548da781a721ee62a7a4434c"></a>

### v15.7.4 [`00551b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551b18.md) FUN_00551b18

`competing_candidates` [`00551b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551b18.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00551aec",
    "00551b20",
    "00551aec",
    "00551b20"
  ],
  "initial_reason": ""
}
~~~

<a id="review-33adb92c3b97ca8c8204ecea920e7821"></a>

### v15.7.4 [`00551be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551be4.md) FUN_00551be4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00551be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551be4.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`004365f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f0.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00456ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ed8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00456ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ee8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00456f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f00.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00456f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f18.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00456f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f20.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00551bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551bec.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00551be4",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "004365f0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456ed8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ce0af57e2610dfcbe4546b073bcc14e3"></a>

### v15.7.4 [`00551bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bec.md) FUN_00551bec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00551bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551bec.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`004365f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f0.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00456ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ed8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00456ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ee8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00456f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f00.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00456f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f18.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`00456f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f20.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`00551be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551be4.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00551bec",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "004365f0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456ed8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c4e32ade9e989f0d0d27ef4135e801bc"></a>

### v15.7.4 [`005524e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005524e0.md) FUN_005524e0

`competing_candidates` 

呼出元 1件 [`0055347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md) · 呼出先 0件 

- 1. [`0053e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e10c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0054e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e8f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005524e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005524e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00552510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552510.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "0053e10c",
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
      "new": "0054e8f0",
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
      "new": "005524e0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c79c777da967d987be2f6964786487ff"></a>

### v15.7.4 [`00552510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552510.md) FUN_00552510

`competing_candidates` 

呼出元 1件 [`0055347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md) · 呼出先 0件 

- 1. [`0053e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e10c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0054e8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e8f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005524e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/005524e0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00552510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00552/00552510.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 5. [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 6. [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 7. [`00ad42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad42fc.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 8. [`00ad432c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad432c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "0053e10c",
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
      "new": "0054e8f0",
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
      "new": "005524e0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c3c83a7f8f2bf2cd4c969f949c130903"></a>

### v15.7.4 [`00553974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553974.md) FUN_00553974

`competing_candidates` [`00553974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553974.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00553950",
    "00553984",
    "00553950",
    "00553984"
  ],
  "initial_reason": ""
}
~~~

<a id="review-c10b313fb28936d8d7f9d12ba811c33f"></a>

### v15.7.4 [`0055397c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055397c.md) FUN_0055397c

`competing_candidates` [`0055397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/0055397c.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00553950",
    "00553984",
    "00553950",
    "00553984"
  ],
  "initial_reason": ""
}
~~~

<a id="review-ce500a855f5be3573a157554afb25be3"></a>

### v15.7.4 [`00553ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac0.md) FUN_00553ac0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00553ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553ac0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00553ac0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cd28f649c11ef5068afb1b9f4f022384"></a>

### v15.7.4 [`005543ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005543ec.md) FUN_005543ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005543ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00554/005543ec.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005543ec",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-afe35f8f7cfbe2c9340567ccbf631d28"></a>

### v15.7.4 [`005565c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/005565c8.md) FUN_005565c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005565c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00556/005565c8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 2. [`007724a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/007724a8.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 3. [`00772590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772590.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 4. [`00772678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00772/00772678.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 5. [`00ad7430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7430.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 6. [`00ada528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada528.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · insufficient_independent_call_anchors
- 7. [`00848ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848ab0.md) · スコア 65.113636 · 採用条件未達 · 順位差 -14.886364 / -14.886364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00970554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970554.md) · スコア 49.454545 · 採用条件未達 · 順位差 -30.545454999999997 / -30.545454999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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

<a id="review-85b3cc13bd7e8314fcb6e7ac3b18e73e"></a>

### v15.7.4 [`00557104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557104.md) FUN_00557104

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557104.md) · スコア 80.0 · 採用条件未達 · 順位差 70.0 / 70.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`0055711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/0055711c.md) · スコア 10.0 · 採用条件未達 · 順位差 -70.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 70.0,
        "reverse_margin": 70.0
      },
      "new": "00557104",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.16666666666666666
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
        "reverse_margin": -70.0
      },
      "new": "0055711c",
      "score": 10.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d0b708f58e7d4f06eec76f33438f315d"></a>

### v15.7.4 [`0055711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/0055711c.md) FUN_0055711c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0055711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/0055711c.md) · スコア 80.0 · 採用条件未達 · 順位差 70.0 / 70.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00557104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557104.md) · スコア 10.0 · 採用条件未達 · 順位差 -70.0 / -70.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 70.0,
        "reverse_margin": 70.0
      },
      "new": "0055711c",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.16666666666666666
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
        "reverse_margin": -70.0
      },
      "new": "00557104",
      "score": 10.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e33b7d0d693909c94e214b56ff583104"></a>

### v15.7.4 [`00557a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a68.md) FUN_00557a68

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a68.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00557a68",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1cbf9c6b32d49526a291c90a4b3bdf7c"></a>

### v15.7.4 [`00557a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a70.md) FUN_00557a70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a70.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00557a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a74.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00557a70",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00557a74",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-383869b6a385c57daf60663d073ef611"></a>

### v15.7.4 [`00557a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a74.md) FUN_00557a74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a74.md) · スコア 69.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00557a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a70.md) · スコア 54.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00557a74",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00557a70",
      "score": 54.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e850b1992b2fac94db2bbbab949f85ad"></a>

### v15.7.4 [`00557a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a88.md) FUN_00557a88

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a88.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00557a88",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-60e3e05743bbd5b69786fa0cbf56f0f7"></a>

### v15.7.4 [`00557f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f58.md) FUN_00557f58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00557f58",
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
      "new": "00557f6c",
      "score": 80.0
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.0,
        "reverse_margin": -12.0
      },
      "new": "005490a0",
      "score": 68.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1eac2c9296fe9b78b1d067816e619868"></a>

### v15.7.4 [`00557f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f6c.md) FUN_00557f6c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f58.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00557f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f6c.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`005490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490a0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`005490b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490b0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`005490f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/005490f0.md) · スコア 68.0 · 採用条件未達 · 順位差 -12.0 / -12.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bc0f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f64.md) · スコア 32.0 · 採用条件未達 · 順位差 -48.0 / -48.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00557f58",
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
      "new": "00557f6c",
      "score": 80.0
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -12.0,
        "reverse_margin": -12.0
      },
      "new": "005490a0",
      "score": 68.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3f4179e8e871db8449f539277ac72c77"></a>

### v15.7.4 [`00557f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f80.md) FUN_00557f80

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00557f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557f80.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 

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
      "new": "00557f80",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-abc7e6801987aaab623e2645c3cdb955"></a>

### v15.7.4 [`00558c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558c8c.md) FUN_00558c8c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00558c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c8c.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00456ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ef8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00456f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f08.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00456f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f10.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00558c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c94.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00558c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c9c.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00558c8c",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456ef8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456f08",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-850ce4e7ff6257ae3528641eb36a3614"></a>

### v15.7.4 [`00558c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558c94.md) FUN_00558c94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00558c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c94.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00456ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ef8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00456f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f08.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00456f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f10.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00558c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c8c.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00558c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c9c.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00558c94",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456ef8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456f08",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c6b65a5083d1308edaf29a0f93a37faf"></a>

### v15.7.4 [`00558c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558c9c.md) FUN_00558c9c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00558c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c9c.md) · スコア 99.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`00456ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ef8.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00456f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f08.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00456f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456f10.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00558c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c8c.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`00558c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558c94.md) · スコア 84.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00558c9c",
      "score": 99.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456ef8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00456f08",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0fe2bba375697a1116ead14d81ecd9e2"></a>

### v15.7.4 [`00559178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559178.md) FUN_00559178

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00559178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559178.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00559178",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-36497894e188a32d9d76c7b7ea987a7e"></a>

### v15.7.4 [`005591c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591c8.md) FUN_005591c8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005591c8",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8e11c7cd9f4e881f2ba914d6fb65e011"></a>

### v15.7.4 [`005595f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005595f4.md) FUN_005595f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005595f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595f4.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`0045b324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b324.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00539b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b1c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`0053c5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5d8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`0053dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd74.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 6. [`0053e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0fc.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 7. [`0054e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e39c.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 
- 8. [`005591c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005595f4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0045b324",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00539b1c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-babfa44116e854fea0c000a4e1e2bb36"></a>

### v15.7.4 [`00559644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559644.md) FUN_00559644

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00559644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559644.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 

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
      "new": "00559644",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-80eeee1014810e4b49b3ced671148d86"></a>

### v15.7.4 [`00559774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559774.md) FUN_00559774

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00559774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559774.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00559774",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-16dea6cdd089f995438ea56cf9d41110"></a>

### v15.7.4 [`00559e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e30.md) FUN_00559e30

`competing_candidates` [`00559e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559e30.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00559dfc",
    "00559e38",
    "00559dfc",
    "00559e38"
  ],
  "initial_reason": ""
}
~~~

<a id="review-3e5caa726de8878937ce1579e83271b9"></a>

### v15.7.4 [`00559e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e70.md) FUN_00559e70

`competing_candidates` [`00559e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559e70.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00559e44",
    "00559e78",
    "00559e44",
    "00559e78"
  ],
  "initial_reason": ""
}
~~~

