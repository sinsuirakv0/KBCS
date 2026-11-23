# v15.7.3 → v15.7.4 · 追加調査 (27)

[一覧の目次](README.md)

<a id="review-d1f0be787507e04cff282e74c6895d18"></a>

### v15.7.4 [`005a96e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a96e4.md) FUN_005a96e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005745f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005745f4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`005a96e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a96e4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00b60684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60684.md) · スコア 63.333333 · 採用条件未達 · 順位差 0.0 / -16.666666999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0052dcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dcf4.md) · スコア 40.0 · 採用条件未達 · 順位差 -40.0 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005a96fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a96fc.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005745f4",
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
      "new": "005a96e4",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          1.0,
          0.8333333333333334
        ],
        "cfg_coverage": [
          1.0,
          0.6666666666666666
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
        "reverse_margin": -16.666666999999997
      },
      "new": "00b60684",
      "score": 63.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-064c9d1666333a988bdc242e7d7ad0c6"></a>

### v15.7.4 [`005a96fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a96fc.md) FUN_005a96fc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005a96fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a96fc.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`005a96e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a96e4.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "005a96fc",
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
      "new": "005a96e4",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a229f25f3976a9217abc2c8fac1bec4b"></a>

### v15.7.4 [`005b0488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0488.md) FUN_005b0488

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b0488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0488.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005b0488",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b05d8aa36271df1514693bea5655858f"></a>

### v15.7.4 [`005b4d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d5c.md) FUN_005b4d5c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b4d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4d5c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b4d5c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c2f3eb873863d5f91a403539d14bc825"></a>

### v15.7.4 [`005b4fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4fec.md) FUN_005b4fec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b4fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4fec.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b4fec",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8b6edcdf9a726ba0a8b94cb23f33065a"></a>

### v15.7.4 [`005b5238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5238.md) FUN_005b5238

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5238.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005b5238",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5fd3e5813f3a9ed7618987729271ae4e"></a>

### v15.7.4 [`005b586c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b586c.md) FUN_005b586c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b586c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b586c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b586c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-999056e4b85c9cddbf3a3a9b80b54bbb"></a>

### v15.7.4 [`005b631c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b631c.md) FUN_005b631c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b631c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b631c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b631c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eaf758732dc716580ed9ad01f6a71f5d"></a>

### v15.7.4 [`005b63cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b63cc.md) FUN_005b63cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b63cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b63cc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b63cc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3c9829c5b2c1e4afd25ab9645d9c2773"></a>

### v15.7.4 [`005b649c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b649c.md) FUN_005b649c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b649c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b649c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b649c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d5cea7ae239dd0321da392fbf548ca98"></a>

### v15.7.4 [`005b6718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6718.md) FUN_005b6718

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6718.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b6718",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-613c49a36571e22ca86e5d94beb60db4"></a>

### v15.7.4 [`005b6a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a84.md) FUN_005b6a84

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6a84.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b6a84",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fde928b4b89bcaa9ffb51345c74d9e60"></a>

### v15.7.4 [`005b6b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b48.md) FUN_005b6b48

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6b48.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b6b48",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5de510adc46204306814654a3aaae131"></a>

### v15.7.4 [`005b6ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ff8.md) FUN_005b6ff8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b6ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6ff8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b6ff8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0258a4bdd410227705462f7a2a005fc2"></a>

### v15.7.4 [`005b71f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b71f4.md) FUN_005b71f4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b71f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b71f4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b71f4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-28c45f989bb081dc3ca4365b0a45e362"></a>

### v15.7.4 [`005b7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7264.md) FUN_005b7264

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b7264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7264.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005b7264",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-91bd9b8c76a6806835333429b808c589"></a>

### v15.7.4 [`005b7370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7370.md) FUN_005b7370

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b7370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7370.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b7370",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ebf74913fa1025462409b8cf27f3baba"></a>

### v15.7.4 [`005b746c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b746c.md) FUN_005b746c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b746c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b746c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.6667 / 82.6667 · 
- 2. [`005b7478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7478.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.6667,
        "reverse_margin": 82.6667
      },
      "new": "005b746c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b7478",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6e748750ba679f0aaff453137a2a99aa"></a>

### v15.7.4 [`005b7478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7478.md) FUN_005b7478

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b7478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7478.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005b746c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b746c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005b7478",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005b746c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-264aa14ec02c8be9daea1723d4b3c62d"></a>

### v15.7.4 [`005b75e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b75e4.md) FUN_005b75e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b75e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b75e4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b75e4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-28cb226c6a76a64d1f26c993629cd290"></a>

### v15.7.4 [`005b7604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7604.md) FUN_005b7604

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b7604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7604.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005b7604",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-493ae8d32f47fa86a4abd923f0af99b4"></a>

### v15.7.4 [`005b77cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77cc.md) FUN_005b77cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b77cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b77cc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005b77cc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-79d037b4979606288cb11176cd055953"></a>

### v15.7.4 [`005b8d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d88.md) FUN_005b8d88

`competing_candidates` [`005b8d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8d88.md)

呼出元 1件 [`005c7548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c7/005c7548.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "005b8a40",
    "005b8d90",
    "005b8a40",
    "005b8d90"
  ],
  "initial_reason": ""
}
~~~

<a id="review-ba5924c70736249f05d43fa4a4226dec"></a>

### v15.7.4 [`005f0e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e24.md) FUN_005f0e24

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f0e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e24.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f0e24",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c9b5363de5b18b70d6924c49cb4f6598"></a>

### v15.7.4 [`005f1058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1058.md) FUN_005f1058

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f1058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1058.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f1058",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4be71d055e669532f611b7f30821f4af"></a>

### v15.7.4 [`005f15bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f15bc.md) FUN_005f15bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f15bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f15bc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f15bc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-39cfc6db7db8bb6a6e77539972c0a81d"></a>

### v15.7.4 [`005f1674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1674.md) FUN_005f1674

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f1674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1674.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f1674",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-428266bfa24b6e9c7c14b87d889c042d"></a>

### v15.7.4 [`005f1760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1760.md) FUN_005f1760

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f1760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1760.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f1760",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5f4ef5d188d46451bcd0084a89e08f62"></a>

### v15.7.4 [`005f17ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17ac.md) FUN_005f17ac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f17ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f17ac.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005f17ac",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c35c5cce522cfbf54af01c2d4b6fed32"></a>

### v15.7.4 [`005f17cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17cc.md) FUN_005f17cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f17cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f17cc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f17cc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-fe528929e2f0389f045cbbfdbfa2a4a2"></a>

### v15.7.4 [`005f1920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1920.md) FUN_005f1920

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f1920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1920.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f1920",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f1b19012864ade7f08907382569e50aa"></a>

### v15.7.4 [`005f28d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f28d8.md) FUN_005f28d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f28d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f28d8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f28d8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-20fe56f8d09c9ff93e1f049987138f88"></a>

### v15.7.4 [`005f2974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2974.md) FUN_005f2974

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f2974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2974.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f2974",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-34dc02f75621dd3e033d68e4accd4173"></a>

### v15.7.4 [`005f48ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f48ac.md) FUN_005f48ac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f48ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f48ac.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f48ac",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-08a57ad31751591b8cb141bec6801ac8"></a>

### v15.7.4 [`005f71ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f71ec.md) FUN_005f71ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f71ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f71ec.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f71ec",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d6d6129f443c8b6eb8f2a12ee9f49346"></a>

### v15.7.4 [`005f724c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f724c.md) FUN_005f724c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00601390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601390.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "00601390",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0fbbabb0f4a6140564ea1d9657facaa9"></a>

### v15.7.4 [`005f7280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7280.md) FUN_005f7280

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7280.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7280",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-183f9a2085b41578ebb51c3bf2d667ec"></a>

### v15.7.4 [`005f7418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7418.md) FUN_005f7418

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7418.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7418",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-72b60e58a5c0071cca8e3dade346b664"></a>

### v15.7.4 [`005f75b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f75b0.md) FUN_005f75b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f75b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f75b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f75b0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e09d02ee72859a8d896592420a610dfc"></a>

### v15.7.4 [`005f7748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7748.md) FUN_005f7748

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7748.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7748",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6ef85aa4c3fb03ab1d40bc870ebd9600"></a>

### v15.7.4 [`005f78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f78e0.md) FUN_005f78e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f78e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f78e0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f78e0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cca7ffcc0f72c7f8f40a5da1e86ed8df"></a>

### v15.7.4 [`005f7a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7a78.md) FUN_005f7a78

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7a78.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7a78",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-90651472d156a18df0d8bd9116ea7533"></a>

### v15.7.4 [`005f7d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7d10.md) FUN_005f7d10

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7d10.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7d10",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0802d1877c519eadc4c5c2c76e20f47b"></a>

### v15.7.4 [`005f7ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f7/005f7ea8.md) FUN_005f7ea8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f7ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f7ea8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f7ea8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-39455064369eb2aea20c7c99a304731a"></a>

### v15.7.4 [`005f8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8040.md) FUN_005f8040

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8040.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f8040",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0fa02d309869ea204abebc05173b1991"></a>

### v15.7.4 [`005f81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f81d8.md) FUN_005f81d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f81d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f81d8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f81d8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-eaa9b44c3e45ff57b7b4b2213d4e07e2"></a>

### v15.7.4 [`005f8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8370.md) FUN_005f8370

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8370.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f8370",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6c5e10f7c6613e3375106f290e960013"></a>

### v15.7.4 [`005f8510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8510.md) FUN_005f8510

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8510.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f8510",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f3b819e844c1555afaf990dd9c31efa1"></a>

### v15.7.4 [`005f86a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f86a8.md) FUN_005f86a8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f86a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f86a8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f86a8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c2c2b1fbd564064b75925ba25bc60f8c"></a>

### v15.7.4 [`005f8840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8840.md) FUN_005f8840

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8840.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f8840",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f8cf9a8c42c4351dbc6a1e4f603d1973"></a>

### v15.7.4 [`005f89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f89d8.md) FUN_005f89d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f89d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f89d8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f89d8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6cdb82083f0da7c6d886c6c0333a4910"></a>

### v15.7.4 [`005f8af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8af4.md) FUN_005f8af4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8af4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f8af4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-67c4d94a94a014c2fcc79ddc9b7bfb9e"></a>

### v15.7.4 [`005f8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c14.md) FUN_005f8c14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c14.md) · スコア 84.0 · 採用条件未達 · 順位差 82.6667 / 82.6667 · 
- 2. [`005f8c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c20.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.6667,
        "reverse_margin": 82.6667
      },
      "new": "005f8c14",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c20",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6fed7a87cc6bea8de4734162eafe01c5"></a>

### v15.7.4 [`005f8c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f8/005f8c20.md) FUN_005f8c20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f8c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c20.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`005f8c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f8/005f8c14.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "005f8c20",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "005f8c14",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0f55b1aa2f90c89a4e8ad763b69a6295"></a>

### v15.7.4 [`005f9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9094.md) FUN_005f9094

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f9094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9094.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f9094",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6a03bd4e7e94a686f468eabaed37b15a"></a>

### v15.7.4 [`005f9154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f9154.md) FUN_005f9154

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f9154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f9154.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f9154",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9e4b591cf3379735def56627b6cb1162"></a>

### v15.7.4 [`005f91a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91a0.md) FUN_005f91a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f91a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f91a0.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "005f91a0",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2936c90c8ac3f3109e485e5335827943"></a>

### v15.7.4 [`005f91c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f9/005f91c0.md) FUN_005f91c0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f91c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f9/005f91c0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005f91c0",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c244d7c4bf4f5738235757a2af39a9c0"></a>

### v15.7.4 [`005ff110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ff/005ff110.md) FUN_005ff110

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005ff110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ff/005ff110.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "005ff110",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0937613549b5faf29ab240014b8d1e2d"></a>

### v15.7.4 [`00600a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600a14.md) FUN_00600a14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00600a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600a14.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00600a14",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9345f315e712f8da36f0855ce4383623"></a>

### v15.7.4 [`00600d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600d0c.md) FUN_00600d0c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00600d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600d0c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00600d0c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f95c8e4dee2fca45113604bb0be427b0"></a>

### v15.7.4 [`00600dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600dfc.md) FUN_00600dfc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00600dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600dfc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00600dfc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-17fc2d74eaf26ec8823081cc12dc5a19"></a>

### v15.7.4 [`00600eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600eac.md) FUN_00600eac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00600eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600eac.md) · スコア 84.0 · 採用条件未達 · 順位差 82.6667 / 82.6667 · 
- 2. [`00600eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600eb8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.6667,
        "reverse_margin": 82.6667
      },
      "new": "00600eac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00600eb8",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8be7efe62fa33a45ed6c453ca349e8b7"></a>

### v15.7.4 [`00600eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/00600eb8.md) FUN_00600eb8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00600eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600eb8.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`00600eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/00600eac.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00600eb8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00600eac",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-23d0540505685079f8a91e508df40542"></a>

### v15.7.4 [`00601128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601128.md) FUN_00601128

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00601128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601128.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00601128",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-db11d628b7fcbafac5c96c0d1c86903e"></a>

### v15.7.4 [`006011e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006011e8.md) FUN_006011e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006011e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006011e8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "006011e8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-07abb57850e29c076743d5d099b50ed6"></a>

### v15.7.4 [`0060127c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060127c.md) FUN_0060127c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060127c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060127c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060127c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-c128a79f8ff6ed6c48f06e900dff31f6"></a>

### v15.7.4 [`0060132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060132c.md) FUN_0060132c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060132c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.6667 / 82.6667 · 
- 2. [`00601338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601338.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.6667,
        "reverse_margin": 82.6667
      },
      "new": "0060132c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00601338",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-13eb6e7c8a0f7a2b55e2fe433a9690af"></a>

### v15.7.4 [`00601338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601338.md) FUN_00601338

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00601338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601338.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`0060132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060132c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00601338",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0060132c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d488c3b0bc1db9446df253478c18fb4c"></a>

### v15.7.4 [`00601390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601390.md) FUN_00601390

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005f724c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f7/005f724c.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "005f724c",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-bda32e65ceabca4f0650d129314614e0"></a>

### v15.7.4 [`006013c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013c4.md) FUN_006013c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006013c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/006013c4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "006013c4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0e78319b16fdc2d832d58928161f07ef"></a>

### v15.7.4 [`0060155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060155c.md) FUN_0060155c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060155c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/0060155c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060155c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3043268079cb1011eace5790221f2d24"></a>

### v15.7.4 [`00601c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601c94.md) FUN_00601c94

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00601c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00601/00601c94.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00601c94",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4154ccc0a88fb7ced874d17010aa58fc"></a>

### v15.7.4 [`0060212c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/0060212c.md) FUN_0060212c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060212c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060212c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.6667 / 82.6667 · 
- 2. [`00602138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602138.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 82.6667,
        "reverse_margin": 82.6667
      },
      "new": "0060212c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00602138",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-12b6dc9c75fea2c3d2ef0cacc9c6f8d3"></a>

### v15.7.4 [`00602138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602138.md) FUN_00602138

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00602138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602138.md) · スコア 69.0 · 採用条件未達 · 順位差 67.6667 / 67.6667 · 
- 2. [`0060212c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/0060212c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00602138",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0060212c",
      "score": 1.3333
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ea9439df269a545c02bc25e03fafe7a5"></a>

### v15.7.4 [`00602370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602370.md) FUN_00602370

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00602370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602370.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00602370",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d8be3ec624ed1b3d2d83aa3dafc27d60"></a>

### v15.7.4 [`00602450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602450.md) FUN_00602450

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00602450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00602/00602450.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00602450",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e90a452dad10d901a0367fb52286ed9e"></a>

### v15.7.4 [`0060b060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b060.md) FUN_0060b060

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060b060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b060.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060b060",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2976951b41ae0094397f954aa8f59ac6"></a>

### v15.7.4 [`0060b270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b270.md) FUN_0060b270

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060b270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b270.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060b270",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-68800136ce66de9f8f602c1d1de7b7fa"></a>

### v15.7.4 [`0060b348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b348.md) FUN_0060b348

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060b348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b348.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060b348",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a9e7c8f3d717cee992c1542622d7e795"></a>

### v15.7.4 [`0060fb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb44.md) FUN_0060fb44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb44.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0060fb44",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5629fb5f68b4dcb392ead77d2d8cf164"></a>

### v15.7.4 [`0060fb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb88.md) FUN_0060fb88

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060fb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb88.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0060fb88",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9a9b41f67665d8072138fda56bc0bfed"></a>

### v15.7.4 [`0060fba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fba8.md) FUN_0060fba8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060fba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fba8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060fba8",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-785f883be17135cbe2921f467b0206d4"></a>

### v15.7.4 [`0060fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fddc.md) FUN_0060fddc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0060fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fddc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0060fddc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ca40d67cb383fde87432fa39310bcb57"></a>

### v15.7.4 [`00610374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610374.md) FUN_00610374

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00610374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610374.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00610374",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ea8d7c5f9b919c8cc1c7502ca0113d97"></a>

### v15.7.4 [`00610d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610d74.md) FUN_00610d74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00610d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610d74.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00610d74",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-34cdef90de7e0f254d51cf6a3eedabd1"></a>

### v15.7.4 [`00610e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610e24.md) FUN_00610e24

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00610e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610e24.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00610e24",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1fa96e9c07e24e87b06e13e0d426eca5"></a>

### v15.7.4 [`006111c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/006111c4.md) FUN_006111c4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006111c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00611/006111c4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "006111c4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0410e039b6246ae4cdf858df108d5a7f"></a>

### v15.7.4 [`00614100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614100.md) FUN_00614100

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00614100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614100.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00614100",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-d12c87de4a1b0b9b798655af53b67fed"></a>

### v15.7.4 [`00614120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614120.md) FUN_00614120

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00614120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614120.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00614120",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cb0bca44c4ac0f9f831e14f069d4f822"></a>

### v15.7.4 [`006143ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006143ec.md) FUN_006143ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006143ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006143ec.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "006143ec",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9de07e9e7503f31ca0cc358c7cc10dfd"></a>

### v15.7.4 [`00614894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614894.md) FUN_00614894

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00614894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614894.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00614894",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-91244ee6ab636bd9eb54d36c878b4112"></a>

### v15.7.4 [`0062714c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/0062714c.md) _INIT_79

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00626ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00626/00626ee4.md) [`00627030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627030.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

- 1. [`0062714c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00627/0062714c.md) · スコア 48.425993 · 採用条件未達 · 順位差 36.921094 / 36.921094 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00973254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973254.md) · スコア 11.504899 · 採用条件未達 · 順位差 11.504899 / -36.921094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006b6c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6c84.md) · スコア 5.399694 · 採用条件未達 · 順位差 -52.116386000000006 / -43.026298999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a0d278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0d/00a0d278.md) · スコア 4.599278 · 採用条件未達 · 順位差 4.599278 / -43.826715 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b1ed64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md) · スコア 3.06057 · 採用条件未達 · 順位差 3.06057 / -45.365423 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) · スコア 2.541516 · 採用条件未達 · 順位差 2.541516 / -45.884477 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00615c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00615/00615c9c.md) · スコア 2.433213 · 採用条件未達 · 順位差 -0.593013 / -45.992779999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007f8ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f8/007f8ecc.md) · スコア 2.433213 · 採用条件未達 · 順位差 2.433213 / -45.992779999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4404332129963899,
          0.4404332129963899
        ],
        "cfg_coverage": [
          1.0,
          1.0
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.921094,
        "reverse_margin": 36.921094
      },
      "new": "0062714c",
      "score": 48.425993
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16203703703703703,
          0.0631768953068592
        ],
        "cfg_coverage": [
          0.2926829268292683,
          0.2857142857142857
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 11.504899,
        "reverse_margin": -36.921094
      },
      "new": "00973254",
      "score": 11.504899
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05666156202143951,
          0.06678700361010831
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
        "margin": -52.116386000000006,
        "reverse_margin": -43.026298999999995
      },
      "new": "006b6c84",
      "score": 5.399694
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-432c3ea882213110afae9eec184f4c39"></a>

### v15.7.4 [`0062d97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d97c.md) FUN_0062d97c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062d97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d97c.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0062d97c",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e03d9991bfb4ebb024977357a7bc8037"></a>

### v15.7.4 [`0062d9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9c0.md) FUN_0062d9c0

`competing_candidates` [`0062d9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9c0.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "0062d9bc",
    "0062d9c8",
    "0062d9bc",
    "0062d9c8"
  ],
  "initial_reason": ""
}
~~~

<a id="review-13776f73f341b93322bd18ff59cc35e6"></a>

### v15.7.4 [`0062d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9e4.md) FUN_0062d9e4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9e4.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0062d9e4",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5dc0ad570f33e65d7931ba70606c0ae6"></a>

### v15.7.4 [`0062da70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da70.md) FUN_0062da70

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062da70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da70.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0062da70",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-50d7fee5b0988eec24f530fa01602290"></a>

### v15.7.4 [`0062f64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f64c.md) FUN_0062f64c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f64c.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0062f64c",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5d18e5f317741fb53882faa539caf7f5"></a>

### v15.7.4 [`0062f714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f714.md) FUN_0062f714

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062f714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f714.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0062f714",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1064633f6e287f387620ba4c634c9ee5"></a>

### v15.7.4 [`0062f7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f7dc.md) FUN_0062f7dc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0062f7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f7dc.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "0062f7dc",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

