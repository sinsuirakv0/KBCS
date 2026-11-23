# v15.7.3 → v15.7.4 · 追加調査 (39)

[一覧の目次](README.md)

<a id="review-084dae3626ce83ed669ca959488528a5"></a>

### v15.7.4 [`00bdae84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdae84.md) FUN_00bdae84

`competing_candidates` 

呼出元 1件 [`0092e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092e/0092e43c.md) · 呼出先 1件 [`00932008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00932/00932008.md)

- 1. [`00bdae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae44.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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
      "new": "00bdae44",
      "score": 84.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1e0cd1704641d79298a191a906c7bd3a"></a>

### v15.7.4 [`00bdafb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafb0.md) FUN_00bdafb0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00bdaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf60.md) · スコア 0.0 · 採用条件未達 · 順位差 -68.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bdaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf80.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": -68.0,
        "reverse_margin": 0.0
      },
      "new": "00bdaf60",
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
      "new": "00bdaf80",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-31c843b0b6b3aeb52e7d220fcefc4128"></a>

### v15.7.4 [`00bdafd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafd0.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`004182d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004182d0.md) · 呼出先 1件 [`010a5000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5000.md)

- 1. [`00bdb020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb020.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd020.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf020.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1020.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdaf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf80.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf60.md) · スコア 56.0 · 採用条件未達 · 順位差 -12.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00bdb020",
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
        "margin": 80.0,
        "reverse_margin": 0.0
      },
      "new": "00bdf020",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-441adce3efe5064d88d3cb4477b18046"></a>

### v15.7.4 [`00bdca90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca90.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`004d9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b40.md) · 呼出先 1件 [`010a5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5188.md)

- 1. [`00bdcae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcae0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeae0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be0ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ae0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bdca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca40.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdcae0",
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
      "new": "00bdeae0",
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
      "new": "00be0ae0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fcc9bd817ccdfa92bd9503e29731865c"></a>

### v15.7.4 [`00bdd340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd340.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`0055a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a228.md) · 呼出先 1件 [`010a5280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5280.md)

- 1. [`00bdb390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb390.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd390.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf390.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1390.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2f0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd300.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb390",
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
      "new": "00bdd390",
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
      "new": "00bdf390",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ed524b8b1eff629391af7de1bac7be81"></a>

### v15.7.4 [`00bdd350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd350.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 2件 [`0055a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a2b8.md) [`0055a2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a2cc.md) · 呼出先 1件 [`010a5288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5288.md)

- 1. [`00bdb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2f0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd300.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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

<a id="review-7fc7e4d08d3ad7c676c98d9a5224d919"></a>

### v15.7.4 [`00bdd3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3a0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`0055a44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a44c.md) · 呼出先 1件 [`010a52b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52b0.md)

- 1. [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3f0.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00bdf3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13f0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd350.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb3f0",
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
      "new": "00bdd3f0",
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
      "new": "00bdf3f0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c639a009934e90f04edadd6269bd6cd7"></a>

### v15.7.4 [`00bdd440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd440.md) &lt;EXTERNAL&gt;::rename

`competing_candidates` 

呼出元 1件 [`0055bd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd48.md) · 呼出先 1件 [`010a52f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52f8.md)

- 1. [`00bdb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb490.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd490.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00be1490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1490.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00bdd3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3f0.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb490",
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
      "new": "00bdd490",
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
      "new": "00be1490",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4c778e7899192ee2f204585eece172c7"></a>

### v15.7.4 [`00bdd5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5e0.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`0056e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e928.md) · 呼出先 1件 [`010a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c0.md)

- 1. [`00bdd5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd5a0.md) · スコア 35.0 · 採用条件未達 · 順位差 35.0 / 35.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00bdd590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd590.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -35.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "candidate_for_unmatched_old_function",
  "order": "score_descending_then_address",
  "ranked_candidates": [
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
        "margin": 35.0,
        "reverse_margin": 35.0
      },
      "new": "00bdd5a0",
      "score": 35.0
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
        "reverse_margin": -35.0
      },
      "new": "00bdd590",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca652a55787866ed7af591b873b329ee"></a>

### v15.7.4 [`00bdd5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5f0.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`0056e930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056e930.md) · 呼出先 1件 [`010a53c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c8.md)

- 1. [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1640.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd590.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 6. [`00bdd5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd5a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.0 / -80.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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

<a id="review-fe08df27d81dbc33d6b1b6bc654aefeb"></a>

### v15.7.4 [`00bdd650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd650.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`0056ec30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056e/0056ec30.md) · 呼出先 1件 [`010a53f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53f8.md)

- 1. [`00bdb6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bdd6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd6a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be16a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16a0.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdd600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd600.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdb6a0",
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
      "new": "00bdd6a0",
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
      "new": "00bdf6a0",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0c0dfa8ab26f9a1689b94d2566e333ff"></a>

### v15.7.4 [`00bddad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddad0.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`010a5558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5558.md)

- 1. [`00bdbb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00bddb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00bdfb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00be1b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b20.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00bdda80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda80.md) · スコア 65.0 · 採用条件未達 · 順位差 -15.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00bdbb20",
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
      "new": "00bddb20",
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
      "new": "00bdfb20",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9db005bc57c327529e024d510e88deb2"></a>

### v15.7.4 [`010a5000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5000.md) &lt;EXTERNAL&gt;::__cxa_finalize

`competing_candidates` 

呼出元 1件 [`00bdafd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafd0.md) · 呼出先 0件 

- 1. [`010a5000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5000.md) · スコア 79.0 · 採用条件未達 · 順位差 79.0 / 79.0 · 

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

<a id="review-69b616f6dd45d4e900005028acf83d86"></a>

### v15.7.4 [`010a5148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5148.md) &lt;EXTERNAL&gt;::closedir

`competing_candidates` 

呼出元 1件 [`004d9024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) · 呼出先 0件 

- 1. [`010a5148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5148.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-fddee6b09b5211d725bdda507baa55f7"></a>

### v15.7.4 [`010a5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5188.md) &lt;EXTERNAL&gt;::siglongjmp

`competing_candidates` 

呼出元 1件 [`00bdca90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca90.md) · 呼出先 0件 

- 1. [`010a5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5188.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-d8a2bc8407eded78edb9dc7790bb3aa3"></a>

### v15.7.4 [`010a5280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5280.md) &lt;EXTERNAL&gt;::AAsset_seek

`competing_candidates` 

呼出元 1件 [`00bdd340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd340.md) · 呼出先 0件 

- 1. [`010a5280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5280.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5288.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-d77b121edd27c430592c2a6d3512faa9"></a>

### v15.7.4 [`010a5288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5288.md) &lt;EXTERNAL&gt;::AAsset_openFileDescriptor64

`competing_candidates` 

呼出元 1件 [`00bdd350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd350.md) · 呼出先 0件 

- 1. [`010a5288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5288.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a5280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5280.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-f98f23d3b44e5e3cc243e5f67658e14e"></a>

### v15.7.4 [`010a52b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52b0.md) &lt;EXTERNAL&gt;::feof

`competing_candidates` 

呼出元 1件 [`00bdd3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3a0.md) · 呼出先 0件 

- 1. [`010a52b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a52b0.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-a89a7b08abc179a8bf0b9887430746e3"></a>

### v15.7.4 [`010a52f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a52f8.md) &lt;EXTERNAL&gt;::rename

`competing_candidates` 

呼出元 1件 [`00bdd440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd440.md) · 呼出先 0件 

- 1. [`010a52f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a52f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-a68757096eb2e54fac3b310818992a3e"></a>

### v15.7.4 [`010a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c0.md) &lt;EXTERNAL&gt;::glFrontFace

`competing_candidates` 

呼出元 1件 [`00bdd5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5e0.md) · 呼出先 0件 

- 1. [`010a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c0.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c8.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-b1921ef8e665a8560812bcf0420fbdcf"></a>

### v15.7.4 [`010a53c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53c8.md) &lt;EXTERNAL&gt;::glLineWidth

`competing_candidates` 

呼出元 1件 [`00bdd5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd5f0.md) · 呼出先 0件 

- 1. [`010a53c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c8.md) · スコア 84.0 · 採用条件未達 · 順位差 15.0 / 15.0 · 
- 2. [`010a53c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53c0.md) · スコア 69.0 · 採用条件未達 · 順位差 — / — · 

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

<a id="review-2b508a5a201d232cb4a96067fd9be5ab"></a>

### v15.7.4 [`010a53f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a53f8.md) &lt;EXTERNAL&gt;::glViewport

`competing_candidates` 

呼出元 1件 [`00bdd650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd650.md) · 呼出先 0件 

- 1. [`010a53f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53f8.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

<a id="review-7f4754cf068ba116277d7f6f9e2bc94b"></a>

### v15.7.4 [`010a5558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5558.md) &lt;EXTERNAL&gt;::cosf

`competing_candidates` 

呼出元 1件 [`00bddad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddad0.md) · 呼出先 0件 

- 1. [`010a5558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5558.md) · スコア 84.0 · 採用条件未達 · 順位差 84.0 / 84.0 · 

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

### v15.7.3 [`00421b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b38.md) FUN_00421b38

`initial_match_conflict` [`00421b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b38.md)

呼出元 1件 [`0081f58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) · 呼出先 0件 


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

### v15.7.3 [`00444fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fc4.md) FUN_00444fc4

`initial_match_conflict` [`00444fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fc4.md)

呼出元 6件 [`006369bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md) [`00665a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665a98.md) [`006abca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ab/006abca0.md) [`008308f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008308f0.md) · 呼出先 0件 


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

### v15.7.3 [`00444fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fcc.md) FUN_00444fcc

`initial_match_conflict` [`00444fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fcc.md)

呼出元 9件 [`006369bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md) [`006534e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md) [`00665a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665a98.md) [`006abca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ab/006abca0.md) · 呼出先 0件 


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

### v15.7.3 [`0044d24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d24c.md) FUN_0044d24c

`initial_match_conflict` [`0044d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d24c.md)

呼出元 2件 [`0078cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078c/0078cd14.md) [`008e68f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e6/008e68f8.md) · 呼出先 0件 


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

### v15.7.3 [`00456ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00456/00456ee0.md) FUN_00456ee0

`initial_match_conflict` [`00456ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456ee0.md)

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

### v15.7.3 [`0045becc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045becc.md) FUN_0045becc

`initial_match_conflict` [`0045becc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045becc.md)

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

### v15.7.3 [`0045bed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bed4.md) FUN_0045bed4

`initial_match_conflict` [`0045bed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bed4.md)

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

### v15.7.3 [`00470aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470aa0.md) FUN_00470aa0

`initial_match_conflict` [`00470aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470aa0.md)

呼出元 1件 [`00467098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467098.md) · 呼出先 0件 


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

### v15.7.3 [`004ac5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac5e0.md) FUN_004ac5e0

`initial_match_conflict` [`004ac5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac5e0.md)

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

### v15.7.3 [`004ac614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ac/004ac614.md) FUN_004ac614

`initial_match_conflict` [`004ac614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac614.md)

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

### v15.7.3 [`004d3a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3a7c.md) FUN_004d3a7c

`initial_match_conflict` [`004d3a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a7c.md)

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

### v15.7.3 [`0050c240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c240.md) FUN_0050c240

`initial_match_conflict` [`0050c240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c240.md)

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

### v15.7.3 [`0050c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c52c.md) FUN_0050c52c

`initial_match_conflict` [`0050c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c52c.md)

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

### v15.7.3 [`0050c818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c818.md) FUN_0050c818

`initial_match_conflict` [`0050c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c818.md)

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

### v15.7.3 [`0050c9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9b4.md) FUN_0050c9b4

`initial_match_conflict` [`0050c9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c9b4.md)

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

### v15.7.3 [`0050c9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9bc.md) FUN_0050c9bc

`initial_match_conflict` [`0050c9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c9bc.md)

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

### v15.7.3 [`0050ca2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca2c.md) FUN_0050ca2c

`initial_match_conflict` [`0050ca2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050ca2c.md)

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

### v15.7.3 [`0050d21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d21c.md) FUN_0050d21c

`initial_match_conflict` [`0050d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d21c.md)

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

### v15.7.3 [`0050d3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d3f4.md) FUN_0050d3f4

`initial_match_conflict` [`0050d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d3f4.md)

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

### v15.7.3 [`0050d77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d77c.md) FUN_0050d77c

`initial_match_conflict` [`0050d77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d77c.md)

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

### v15.7.3 [`0050d784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d784.md) FUN_0050d784

`initial_match_conflict` [`0050d784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d784.md)

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

### v15.7.3 [`0050d8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8ec.md) FUN_0050d8ec

`initial_match_conflict` [`0050d8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8ec.md)

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

### v15.7.3 [`0050dfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfcc.md) FUN_0050dfcc

`initial_match_conflict` [`0050dfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfcc.md)

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

### v15.7.3 [`0050e224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e224.md) FUN_0050e224

`initial_match_conflict` [`0050e224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e224.md)

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

### v15.7.3 [`0050e42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e42c.md) FUN_0050e42c

`initial_match_conflict` [`0050e42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e42c.md)

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

### v15.7.3 [`0050e634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e634.md) FUN_0050e634

`initial_match_conflict` [`0050e634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e634.md)

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

### v15.7.3 [`0050e834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e834.md) FUN_0050e834

`initial_match_conflict` [`0050e834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e834.md)

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

### v15.7.3 [`0050ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea04.md) FUN_0050ea04

`initial_match_conflict` [`0050ea04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea04.md)

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

### v15.7.3 [`0050ed1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ed1c.md) FUN_0050ed1c

`initial_match_conflict` [`0050ed1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed1c.md)

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

### v15.7.3 [`0050ee84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee84.md) FUN_0050ee84

`initial_match_conflict` [`0050ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee84.md)

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

### v15.7.3 [`0050f18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f18c.md) FUN_0050f18c

`initial_match_conflict` [`0050f18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f18c.md)

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

### v15.7.3 [`0050f670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f670.md) FUN_0050f670

`initial_match_conflict` [`0050f670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f670.md)

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

### v15.7.3 [`0050fbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fbb0.md) FUN_0050fbb0

`initial_match_conflict` [`0050fbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fbb0.md)

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

### v15.7.3 [`0050fc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fc54.md) FUN_0050fc54

`initial_match_conflict` [`0050fc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc54.md)

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

### v15.7.3 [`0050fea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fea0.md) FUN_0050fea0

`initial_match_conflict` [`0050fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fea0.md)

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

### v15.7.3 [`00510c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c68.md) FUN_00510c68

`initial_match_conflict` [`00510c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c68.md)

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

### v15.7.3 [`00510ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510ef8.md) FUN_00510ef8

`initial_match_conflict` [`00510ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510ef8.md)

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

### v15.7.3 [`005110a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005110a8.md) FUN_005110a8

`initial_match_conflict` [`005110a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005110a8.md)

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
    "00511084",
    "005110b4",
    "00511084",
    "005110b4"
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

### v15.7.3 [`005110e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005110e4.md) FUN_005110e4

`initial_match_conflict` [`005110e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005110e4.md)

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
    "005110b4",
    "005110f4",
    "005110b4",
    "005110f4"
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

### v15.7.3 [`00511118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511118.md) FUN_00511118

`initial_match_conflict` [`00511118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511118.md)

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

### v15.7.3 [`005111c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005111c0.md) FUN_005111c0

`initial_match_conflict` [`005111c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c0.md)

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

### v15.7.3 [`005112ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005112ec.md) FUN_005112ec

`initial_match_conflict` [`005112ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112ec.md)

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

### v15.7.3 [`0051178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/0051178c.md) FUN_0051178c

`initial_match_conflict` [`0051178c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051178c.md)

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

### v15.7.3 [`00511a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511a5c.md) FUN_00511a5c

`initial_match_conflict` [`00511a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511a5c.md)

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
    "0050b45c",
    "0054fd90",
    "0050b45c",
    "0054fd90"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 1346,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": false,
  "local_unique_shape": false,
  "margin": 30.0,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "text_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 30.0,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": true,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`0051347c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051347c.md) FUN_0051347c

`initial_match_conflict` [`0051347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051347c.md)

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
    "00513474",
    "00513484",
    "00513474",
    "00513484"
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

### v15.7.3 [`005139fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005139fc.md) FUN_005139fc

`initial_match_conflict` [`005139fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005139fc.md)

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
    "005139d4",
    "00513a04",
    "005139d4",
    "00513a04"
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

### v15.7.3 [`00514678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514678.md) FUN_00514678

`initial_match_conflict` [`00514678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514678.md)

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
    "00514580",
    "00514680",
    "00514580",
    "00514680"
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

### v15.7.3 [`00516f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516f40.md) FUN_00516f40

`initial_match_conflict` [`00516f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516f40.md)

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
    "00516d78",
    "00516f48",
    "00516d78",
    "00516f48"
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

### v15.7.3 [`005397dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397dc.md) FUN_005397dc

`initial_match_conflict` [`005397dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397dc.md)

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
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
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

### v15.7.3 [`005397e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397e4.md) FUN_005397e4

`initial_match_conflict` [`005397e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397e4.md)

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
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
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
  "margin": 91.8333,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "text_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 91.8333,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`005397f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397f0.md) FUN_005397f0

`initial_match_conflict` [`005397f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397f0.md)

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
    "005397d8",
    "005397f8",
    "005397d8",
    "005397f8"
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

### v15.7.3 [`0053be00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be00.md) FUN_0053be00

`initial_match_conflict` [`0053be00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be00.md)

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
    "0053bdb0",
    "0053be08",
    "0053bdb0",
    "0053be08"
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

### v15.7.3 [`0053dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd2c.md) FUN_0053dd2c

`initial_match_conflict` [`0053dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd2c.md)

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
    "0053dce0",
    "0053dd34",
    "0053dce0",
    "0053dd34"
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

### v15.7.3 [`0053dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd8c.md) FUN_0053dd8c

`initial_match_conflict` [`0053dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd8c.md)

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
    "0053dd88",
    "0053dde0",
    "0053dd88",
    "0053dde0"
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

### v15.7.3 [`00549064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549064.md) FUN_00549064

`initial_match_conflict` [`00549064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549064.md)

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
    "00548e1c",
    "0054906c",
    "00548e1c",
    "0054906c"
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

### v15.7.3 [`00549118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549118.md) FUN_00549118

`initial_match_conflict` [`00549118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549118.md)

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
    "00549108",
    "00549128",
    "00549108",
    "00549128"
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

### v15.7.3 [`0054923c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/0054923c.md) FUN_0054923c

`initial_match_conflict` [`0054923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/0054923c.md)

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
    "005491c4",
    "00549268",
    "005491c4",
    "00549268"
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
  "margin": 98.1111,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "text_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.1111,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`00551b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551b18.md) FUN_00551b18

`initial_match_conflict` [`00551b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551b18.md)

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
    "00551984",
    "00551b20",
    "00551984",
    "00551b20"
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

### v15.7.3 [`00553974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553974.md) FUN_00553974

`initial_match_conflict` [`00553974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553974.md)

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
    "00553828",
    "0055397c",
    "00553828",
    "0055397c"
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
  "margin": 98.1111,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "text_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.1111,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`0055397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/0055397c.md) FUN_0055397c

`initial_match_conflict` [`0055397c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055397c.md)

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
    "00551208",
    "00558640",
    "00551208",
    "00558640"
  ],
  "call_examples": [],
  "code_sketch": 1.0,
  "data_examples": [],
  "delta": true,
  "exported_bytes": false,
  "initial_reason": "",
  "interval_count": 124,
  "leaf_bytes": true,
  "local_unique_leaf_bytes": false,
  "local_unique_shape": false,
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
  "unique_leaf": true,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`00559e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559e30.md) FUN_00559e30

`initial_match_conflict` [`00559e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e30.md)

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
    "00559da0",
    "00559e38",
    "00559da0",
    "00559e38"
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

### v15.7.3 [`00559e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559e70.md) FUN_00559e70

`initial_match_conflict` [`00559e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559e70.md)

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
    "00559e38",
    "00559e88",
    "00559e38",
    "00559e88"
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

### v15.7.3 [`00559edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559edc.md) FUN_00559edc

`initial_match_conflict` [`00559edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559edc.md)

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
    "00559e88",
    "00559ef4",
    "00559e88",
    "00559ef4"
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

### v15.7.3 [`0055a24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a24c.md) FUN_0055a24c

`initial_match_conflict` [`0055a24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a24c.md)

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
    "00559fe0",
    "0055a254",
    "00559fe0",
    "0055a254"
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
  "margin": 98.1111,
  "matched_data": 0,
  "matched_edges": 0,
  "order": true,
  "pseudocode_state": "text_equal",
  "rare_strings": 0,
  "reciprocal_best": true,
  "relaxed": true,
  "reverse_margin": 98.1111,
  "shape": true,
  "size_ratio": 1.0,
  "string_examples": [],
  "tail_call_examples": [],
  "unique_leaf": false,
  "unique_neighborhood": false,
  "unique_shape": false
}
~~~

### v15.7.3 [`0055a3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a3ec.md) FUN_0055a3ec

`initial_match_conflict` [`0055a3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a3ec.md)

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
    "0055a35c",
    "0055a3f4",
    "0055a35c",
    "0055a3f4"
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

### v15.7.3 [`0055a470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a470.md) FUN_0055a470

`initial_match_conflict` [`0055a470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a470.md)

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
    "0055a3f4",
    "0055a488",
    "0055a3f4",
    "0055a488"
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

### v15.7.3 [`0055b5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b5fc.md) FUN_0055b5fc

`initial_match_conflict` [`0055b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b5fc.md)

呼出元 1件 [`0052dd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd4c.md) · 呼出先 0件 


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
    "0055b540",
    "0055b604",
    "0055b540",
    "0055b604"
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

### v15.7.3 [`0055c974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c974.md) FUN_0055c974

`initial_match_conflict` [`0055c974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c974.md)

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
    "0055c754",
    "0055c994",
    "0055c754",
    "0055c994"
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

### v15.7.3 [`0055cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc24.md) FUN_0055cc24

`initial_match_conflict` [`0055cc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc24.md)

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
    "0055c994",
    "0055cc2c",
    "0055c994",
    "0055cc2c"
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

### v15.7.3 [`0055f054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f054.md) FUN_0055f054

`initial_match_conflict` [`0055f054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f054.md)

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
    "0055f050",
    "0055f05c",
    "0055f050",
    "0055f05c"
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

### v15.7.3 [`0055f08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f08c.md) FUN_0055f08c

`initial_match_conflict` [`0055f08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f08c.md)

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
    "0055f05c",
    "0055f094",
    "0055f05c",
    "0055f094"
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

### v15.7.3 [`005604b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604b4.md) FUN_005604b4

`initial_match_conflict` [`005604b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604b4.md)

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
    "005604ac",
    "005604c4",
    "005604ac",
    "005604c4"
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

### v15.7.3 [`005604bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604bc.md) FUN_005604bc

`initial_match_conflict` [`005604bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604bc.md)

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
    "005604ac",
    "005604c4",
    "005604ac",
    "005604c4"
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

### v15.7.3 [`00560998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560998.md) FUN_00560998

`initial_match_conflict` [`00560998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560998.md)

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
    "0056096c",
    "005609a0",
    "0056096c",
    "005609a0"
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

### v15.7.3 [`00562444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562444.md) FUN_00562444

`initial_match_conflict` [`00562444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562444.md)

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
    "0056233c",
    "0056244c",
    "0056233c",
    "0056244c"
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

### v15.7.3 [`00565b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565b68.md) FUN_00565b68

`initial_match_conflict` [`00565b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565b68.md)

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
    "00565b20",
    "00565b70",
    "00565b20",
    "00565b70"
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

### v15.7.3 [`00567de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567de4.md) FUN_00567de4

`initial_match_conflict` [`00567de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567de4.md)

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
    "00567d4c",
    "00567e94",
    "00567d4c",
    "00567e94"
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

