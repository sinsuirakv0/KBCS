# v16.0.2 → v16.0.3 · 追加調査 (29)

[一覧の目次](README.md)

<a id="review-3913703a4ea9dc3762db7adb85af334a"></a>

### v16.0.2 [`00806a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/00806a18.md) FUN_00806a18

`competing_candidates` 

呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`0080797c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/0080797c.md) · スコア 35.795016 · 採用条件未達 · 順位差 29.426166999999996 / 26.023705999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008063d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/008063d0.md) · スコア 6.368849 · 採用条件未達 · 順位差 -29.426166999999996 / -24.142379 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00807850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807850.md) · スコア 2.337662 · 採用条件未達 · 順位差 -33.457353999999995 / -20.754875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0048e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e0a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.795016 / -58.470588 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) · スコア 0.0 · 採用条件未達 · 順位差 -35.795016 / -57.138122 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5064935064935064,
          0.5064935064935064
        ],
        "cfg_coverage": [
          0.2777777777777778,
          0.2702702702702703
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 29.426166999999996,
        "reverse_margin": 26.023705999999997
      },
      "new": "0080797c",
      "score": 35.795016
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11688311688311688,
          0.0989010989010989
        ],
        "cfg_coverage": [
          0.027777777777777776,
          0.021739130434782608
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -29.426166999999996,
        "reverse_margin": -24.142379
      },
      "new": "008063d0",
      "score": 6.368849
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03896103896103896,
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
        "margin": -33.457353999999995,
        "reverse_margin": -20.754875
      },
      "new": "00807850",
      "score": 2.337662
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5928401ecdc5b9ac5d78091fdd655f80"></a>

### v16.0.2 [`0080715c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/0080715c.md) FUN_0080715c

`competing_candidates` 

呼出元 17件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00785a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785a14.md) [`00787570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006be9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006be9fc.md) [`00745804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745804.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00805744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805744.md)

- 1. [`008080c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/008080c0.md) · スコア 44.916346 · 採用条件未達 · 順位差 24.173160999999997 / 16.973995999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00807ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807ab0.md) · スコア 20.743185 · 採用条件未達 · 順位差 -24.173160999999997 / 20.743185 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0072c354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072c/0072c354.md) · スコア 9.025323 · 採用条件未達 · 順位差 -35.891023 / 9.025323 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008083dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/008083dc.md) · スコア 7.608434 · 採用条件未達 · 順位差 -37.307911999999995 / -25.600224 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00807184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807184.md) · スコア 4.713568 · 採用条件未達 · 順位差 -40.202777999999995 / -65.14501800000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00807260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807260.md) · スコア 4.713568 · 採用条件未達 · 順位差 -40.202777999999995 / -66.235927 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a66e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md) · スコア 3.865617 · 採用条件未達 · 順位差 -41.050729 / -72.890289 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0063d63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d63c.md) · スコア 3.139579 · 採用条件未達 · 順位差 -41.776767 / 3.139579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6231155778894473,
          0.6231155778894473
        ],
        "cfg_coverage": [
          0.17647058823529413,
          0.23684210526315788
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 24.173160999999997,
        "reverse_margin": 16.973995999999996
      },
      "new": "008080c0",
      "score": 44.916346
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2814070351758794,
          0.2731707317073171
        ],
        "cfg_coverage": [
          0.11764705882352941,
          0.1518987341772152
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -24.173160999999997,
        "reverse_margin": 20.743185
      },
      "new": "00807ab0",
      "score": 20.743185
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11055276381909548,
          0.17886178861788618
        ],
        "cfg_coverage": [
          0.0196078431372549,
          0.05128205128205128
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -35.891023,
        "reverse_margin": 9.025323
      },
      "new": "0072c354",
      "score": 9.025323
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e197529c649c764992e8c62b46026813"></a>

### v16.0.2 [`00807478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807478.md) FUN_00807478

`competing_candidates` 

呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`00807734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807734.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0074580c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074580c.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`008083dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/008083dc.md) · スコア 32.485714 · 採用条件未達 · 順位差 15.342857000000002 / -0.7229439999999983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00807de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807de4.md) · スコア 17.142857 · 採用条件未達 · 順位差 -15.342857000000002 / 17.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a668c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a668c4.md) · スコア 6.114286 · 採用条件未達 · 順位差 -26.371428 / 6.114286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00735d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00735/00735d6c.md) · スコア 4.742857 · 採用条件未達 · 順位差 -27.742857 / 4.742857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0083aa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083a/0083aa10.md) · スコア 4.657143 · 採用条件未達 · 順位差 -27.828571000000004 / 4.657143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006759a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00675/006759a8.md) · スコア 4.61206 · 採用条件未達 · 順位差 -27.873654000000002 / 4.61206 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005b3080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b3080.md) · スコア 4.057143 · 採用条件未達 · 順位差 -28.428571 / 4.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005b32d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b32d8.md) · スコア 4.057143 · 採用条件未達 · 順位差 -28.428571 / 4.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.49142857142857144,
          0.49142857142857144
        ],
        "cfg_coverage": [
          0.05,
          0.078125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.342857000000002,
        "reverse_margin": -0.7229439999999983
      },
      "new": "008083dc",
      "score": 32.485714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24571428571428572,
          0.26875
        ],
        "cfg_coverage": [
          0.02,
          0.03076923076923077
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -15.342857000000002,
        "reverse_margin": 17.142857
      },
      "new": "00807de4",
      "score": 17.142857
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06857142857142857,
          0.09375
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
        "margin": -26.371428,
        "reverse_margin": 6.114286
      },
      "new": "00a668c4",
      "score": 6.114286
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ae40dd34a8048d2ac99df011a303657c"></a>

### v16.0.2 [`00807734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807734.md) FUN_00807734

`competing_candidates` 

呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 2件 [`0080715c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/0080715c.md) [`00807478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807478.md)

- 1. [`00808064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/00808064.md) · スコア 74.782609 · 採用条件未達 · 順位差 0.0 / 74.782609 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00808698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/00808698.md) · スコア 74.782609 · 採用条件未達 · 順位差 0.0 / 19.999999999999993 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00a67c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67c98.md) · スコア 0.0 · 採用条件未達 · 順位差 -74.782609 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9130434782608695,
          0.9130434782608695
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
        "reverse_margin": 74.782609
      },
      "new": "00808064",
      "score": 74.782609
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9130434782608695,
          0.9130434782608695
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
      "new": "00808698",
      "score": 74.782609
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -74.782609,
        "reverse_margin": 0.0
      },
      "new": "00a67c98",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-37614cd2aaf21473a1eba3b7b4eb74cf"></a>

### v16.0.2 [`00807cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807cb0.md) FUN_00807cb0

`competing_candidates` 

呼出元 4件 [`00618240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md) [`006adf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf88.md) [`00820934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820934.md) [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00808c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/00808c14.md) · スコア 73.636364 · 採用条件未達 · 順位差 62.530373 / 56.542347 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00642058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642058.md) · スコア 11.105991 · 採用条件未達 · 順位差 -62.530373 / -40.046082999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00688404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00688/00688404.md) · スコア 9.82821 · 採用条件未達 · 順位差 -63.808154 / 9.82821 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008066a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/008066a8.md) · スコア 9.545455 · 採用条件未達 · 順位差 -64.090909 / 9.545455 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`004c9e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9e3c.md) · スコア 8.181818 · 採用条件未達 · 順位差 -65.454546 / 8.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00580de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580de8.md) · スコア 8.181818 · 採用条件未達 · 順位差 -65.454546 / 8.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a440a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a44/00a440a0.md) · スコア 8.181818 · 採用条件未達 · 順位差 -65.454546 / 8.181818 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a43104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md) · スコア 5.454545 · 採用条件未達 · 順位差 -68.181819 / 5.454545 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8939393939393939,
          0.8939393939393939
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
        "margin": 62.530373,
        "reverse_margin": 56.542347
      },
      "new": "00808c14",
      "score": 73.636364
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22727272727272727,
          0.16129032258064516
        ],
        "cfg_coverage": [
          0.12,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -62.530373,
        "reverse_margin": -40.046082999999996
      },
      "new": "00642058",
      "score": 11.105991
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18181818181818182,
          0.1518987341772152
        ],
        "cfg_coverage": [
          0.04,
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
        "margin": -63.808154,
        "reverse_margin": 9.82821
      },
      "new": "00688404",
      "score": 9.82821
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4a65de2bfcea1e073cf4c050b7013db1"></a>

### v16.0.2 [`0080c904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c904.md) FUN_0080c904

`competing_candidates` 

呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

- 1. [`0080d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080d/0080d868.md) · スコア 55.977273 · 採用条件未達 · 順位差 53.77618399999999 / 55.024891999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00825680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00825/00825680.md) · スコア 2.201089 · 採用条件未達 · 順位差 -53.77618399999999 / -37.351094999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008e3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e3028.md) · スコア 0.634921 · 採用条件未達 · 順位差 -55.342352 / 0.634921 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006e57dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md) · スコア 0.47619 · 採用条件未達 · 順位差 -55.501082999999994 / 0.47619 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0079a0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a0c8.md) · スコア 0.455997 · 採用条件未達 · 順位差 -55.521276 / 0.455997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007347d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00734/007347d0.md) · スコア 0.076046 · 採用条件未達 · 順位差 -55.901227 / -78.88212899999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005c20e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c20e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -55.977273 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0062c4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062c/0062c4b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -55.977273 / -27.853261 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.46745562130177515,
          0.44886363636363635
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 53.77618399999999,
        "reverse_margin": 55.024891999999994
      },
      "new": "0080d868",
      "score": 55.977273
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.010582010582010581,
          0.0033514872224549644
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
        "margin": -53.77618399999999,
        "reverse_margin": -37.351094999999994
      },
      "new": "00825680",
      "score": 2.201089
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.010582010582010581,
          0.016842105263157894
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
        "margin": -55.342352,
        "reverse_margin": 0.634921
      },
      "new": "008e3028",
      "score": 0.634921
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d6685490aeeb8ee106cd96bb61beb453"></a>

### v16.0.2 [`0080facc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080facc.md) FUN_0080facc

`competing_candidates` [`00810a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810a30.md)

呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0080f8f8",
    "0080fae4",
    "0081085c",
    "00810a48"
  ],
  "initial_reason": ""
}
~~~

<a id="review-4ccc8b212a3c59bfd50d927e22cd9883"></a>

### v16.0.2 [`0080fad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fad4.md) FUN_0080fad4

`competing_candidates` [`00810a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810a38.md)

呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0080f8f8",
    "0080fae4",
    "0081085c",
    "00810a48"
  ],
  "initial_reason": ""
}
~~~

<a id="review-7e6bee6a245b8bf49aaa93a53d16e070"></a>

### v16.0.2 [`0080fadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080fadc.md) FUN_0080fadc

`competing_candidates` [`00810a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/00810a40.md)

呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "0080f8f8",
    "0080fae4",
    "0081085c",
    "00810a48"
  ],
  "initial_reason": ""
}
~~~

<a id="review-7b3ea47a8a3f561e869d40cc32aa63b8"></a>

### v16.0.2 [`00811120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811120.md) FUN_00811120

`competing_candidates` 

呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812084.md) · スコア 25.3125 · 採用条件未達 · 順位差 15.9375 / 15.9375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0073426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00734/0073426c.md) · スコア 9.375 · 採用条件未達 · 順位差 -15.9375 / 9.375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 7.407407 · 採用条件未達 · 順位差 -17.905093 / -55.873016 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0071caf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071caf4.md) · スコア 7.228916 · 採用条件未達 · 順位差 -18.083584000000002 / 7.228916 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0071bdbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071bdbc.md) · スコア 5.454545 · 採用条件未達 · 順位差 -19.857955 / 5.454545 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 5.346535 · 採用条件未達 · 順位差 -19.965965 / -37.748827 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0071c07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c07c.md) · スコア 4.736842 · 採用条件未達 · 順位差 -20.575658 / 4.736842 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00812924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812924.md) · スコア 4.6875 · 採用条件未達 · 順位差 -20.625 / -37.524038 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.421875,
          0.421875
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
        "margin": 15.9375,
        "reverse_margin": 15.9375
      },
      "new": "00812084",
      "score": 25.3125
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15625,
          0.17857142857142858
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
        "margin": -15.9375,
        "reverse_margin": 9.375
      },
      "new": "0073426c",
      "score": 9.375
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15625,
          0.12345679012345678
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
        "margin": -17.905093,
        "reverse_margin": -55.873016
      },
      "new": "008129c0",
      "score": 7.407407
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56a354c286bf2a7a87bf012106d726d3"></a>

### v16.0.2 [`00811220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811220.md) FUN_00811220

`competing_candidates` 

呼出元 5件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) [`00a6fdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6f/00a6fdf8.md) [`00a72604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a72/00a72604.md) [`00a735a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a73/00a735a0.md) [`00a7c564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c564.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812184.md) · スコア 73.333333 · 採用条件未達 · 順位差 73.333333 / 73.333333 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`008121a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008121a8.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -42.352941 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008122cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -38.787879 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -40.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -54.628571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812690.md) · スコア 0.0 · 採用条件未達 · 順位差 -73.333333 / -56.111111 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
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
        "margin": 73.333333,
        "reverse_margin": 73.333333
      },
      "new": "00812184",
      "score": 73.333333
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
        "margin": -73.333333,
        "reverse_margin": -42.352941
      },
      "new": "008121a8",
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
        "margin": -73.333333,
        "reverse_margin": -38.787879
      },
      "new": "008122cc",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00811244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811244.md) FUN_00811244

`competing_candidates` 

呼出元 2件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 2件 [`0081149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081149c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`008121a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008121a8.md) · スコア 42.352941 · 採用条件未達 · 順位差 20.247678 / 13.581011 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812d08.md) · スコア 22.105263 · 採用条件未達 · 順位差 -20.247678 / -46.842105 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812690.md) · スコア 20.0 · 採用条件未達 · 順位差 -22.352941 / -36.111111 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812924.md) · スコア 18.461538 · 採用条件未達 · 順位差 -23.891403 / -23.749999999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00afd0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd0e0.md) · スコア 17.647059 · 採用条件未達 · 順位差 -24.705882000000003 / 17.647059 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 12.631579 · 採用条件未達 · 順位差 -29.721362 / -61.052632 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005e491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e491c.md) · スコア 11.764706 · 採用条件未達 · 順位差 -30.588235 / 11.764706 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a43104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md) · スコア 10.0 · 採用条件未達 · 順位差 -32.352941 / 10.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 20.247678,
        "reverse_margin": 13.581011
      },
      "new": "008121a8",
      "score": 42.352941
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4117647058823529,
          0.3684210526315789
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
        "margin": -20.247678,
        "reverse_margin": -46.842105
      },
      "new": "00812d08",
      "score": 22.105263
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.35294117647058826,
          0.3333333333333333
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
        "margin": -22.352941,
        "reverse_margin": -36.111111
      },
      "new": "00812690",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`008112cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008112cc.md) FUN_008112cc

`competing_candidates` 

呼出元 1件 [`006adf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf88.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 47.115385 · 採用条件未達 · 順位差 27.115385000000003 / 27.115385000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 20.0 · 採用条件未達 · 順位差 -27.115385000000003 / -55.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 20.0 · 採用条件未達 · 順位差 -27.115385000000003 / -55.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006856d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006856d0.md) · スコア 16.923077 · 採用条件未達 · 順位差 -30.192308000000004 / 16.923077 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005233a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/005233a0.md) · スコア 16.346154 · 採用条件未達 · 順位差 -30.769231000000005 / 16.346154 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0071f108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md) · スコア 16.068376 · 採用条件未達 · 順位差 -31.047009000000003 / 16.068376 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00493fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md) · スコア 10.192308 · 採用条件未達 · 順位差 -36.923077000000006 / 10.192308 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00563fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563fc0.md) · スコア 10.192308 · 採用条件未達 · 順位差 -36.923077000000006 / 10.192308 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7435897435897436,
          0.7435897435897436
        ],
        "cfg_coverage": [
          0.125,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 27.115385000000003,
        "reverse_margin": 27.115385000000003
      },
      "new": "00812230",
      "score": 47.115385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.115385000000003,
        "reverse_margin": -55.714286
      },
      "new": "00812720",
      "score": 20.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
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
          "insufficient_independent_call_anchors"
        ],
        "margin": -27.115385000000003,
        "reverse_margin": -55.714286
      },
      "new": "00812790",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-581ef61be7ada48aa2de16a75b68d61d"></a>

### v16.0.2 [`00811368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811368.md) FUN_00811368

`competing_candidates` 

呼出元 2件 [`006a6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6614.md) [`006a7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7518.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`008122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008122cc.md) · スコア 38.787879 · 採用条件未達 · 順位差 1.0101009999999988 / 10.909090999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 37.777778 · 採用条件未達 · 順位差 -1.0101009999999988 / -2.222222000000002 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006657bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/006657bc.md) · スコア 27.878788 · 採用条件未達 · 順位差 -10.909090999999997 / 27.878788 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 16.8 · 採用条件未達 · 順位差 -21.987878999999996 / -37.828571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 15.0 · 採用条件未達 · 順位差 -23.787878999999997 / -22.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006430a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/006430a8.md) · スコア 12.933333 · 採用条件未達 · 順位差 -25.854546 / -62.266667000000005 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006852fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006852fc.md) · スコア 8.428184 · 採用条件未達 · 順位差 -30.359694999999995 / 8.428184 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md) · スコア 0.0 · 採用条件未達 · 順位差 -38.787879 / -76.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5909090909090909,
          0.5909090909090909
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.0101009999999988,
        "reverse_margin": 10.909090999999997
      },
      "new": "008122cc",
      "score": 38.787879
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36363636363636365,
          0.2962962962962963
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
        "margin": -1.0101009999999988,
        "reverse_margin": -2.222222000000002
      },
      "new": "00812324",
      "score": 37.777778
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4090909090909091,
          0.5625
        ],
        "cfg_coverage": [
          0.16666666666666666,
          0.25
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
        "margin": -10.909090999999997,
        "reverse_margin": 27.878788
      },
      "new": "006657bc",
      "score": 27.878788
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`008113c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008113c0.md) FUN_008113c0

`competing_candidates` 

呼出元 9件 [`006a6aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6aac.md) [`006a7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7518.md) [`006ab3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ab/006ab3dc.md) [`006adf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf88.md) [`006afb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006afb14.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 62.857143 · 採用条件未達 · 順位差 0.0 / -12.857143 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 62.857143 · 採用条件未達 · 順位差 0.0 / -12.857143 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 40.0 · 採用条件未達 · 順位差 -22.857143 / 2.222222000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 22.142857 · 採用条件未達 · 順位差 -40.714286 / -15.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008122cc.md) · スコア 15.555556 · 採用条件未達 · 順位差 -47.301587 / -23.232322999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 12.307692 · 採用条件未達 · 順位差 -50.549451000000005 / -34.807693 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 7.407407 · 採用条件未達 · 順位差 -55.449736 / -55.873016 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 5.940594 · 採用条件未達 · 順位差 -56.916549 / -37.154768000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7407407407407407,
          0.7142857142857143
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
        "margin": 0.0,
        "reverse_margin": -12.857143
      },
      "new": "00812720",
      "score": 62.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7407407407407407,
          0.7142857142857143
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
        "margin": 0.0,
        "reverse_margin": -12.857143
      },
      "new": "00812790",
      "score": 62.857143
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
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
        "margin": -22.857143,
        "reverse_margin": 2.222222000000002
      },
      "new": "00812324",
      "score": 40.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`0081142c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081142c.md) FUN_0081142c

`competing_candidates` 

呼出元 3件 [`00a7eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eb90.md) [`00a7eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eed0.md) [`00a7f1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7f/00a7f1d0.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 73.571429 · 採用条件未達 · 順位差 0.0 / -2.1428570000000065 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 73.571429 · 採用条件未達 · 順位差 0.0 / -2.1428570000000065 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 37.142857 · 採用条件未達 · 順位差 -36.428571999999996 / 2.1428569999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 22.619048 · 採用条件未達 · 順位差 -50.952380999999995 / -17.380952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 20.47619 · 採用条件未達 · 順位差 -53.09523899999999 / -34.152381000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 20.0 · 採用条件未達 · 順位差 -53.571428999999995 / -27.115385000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008122cc.md) · スコア 15.0 · 採用条件未達 · 順位差 -58.571428999999995 / -23.787878999999997 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 11.851852 · 採用条件未達 · 順位差 -61.719576999999994 / -51.428571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8928571428571429,
          0.8928571428571429
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
        "margin": 0.0,
        "reverse_margin": -2.1428570000000065
      },
      "new": "00812720",
      "score": 73.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8928571428571429,
          0.8928571428571429
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
        "margin": 0.0,
        "reverse_margin": -2.1428570000000065
      },
      "new": "00812790",
      "score": 73.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.5714285714285714
        ],
        "cfg_coverage": [
          0.25,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -36.428571999999996,
        "reverse_margin": 2.1428569999999993
      },
      "new": "00812390",
      "score": 37.142857
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-736ce322d1e53caa1e5e6fe94014da26"></a>

### v16.0.2 [`0081149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081149c.md) FUN_0081149c

`competing_candidates` 

呼出元 2件 [`00811244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811244.md) [`00811a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811a5c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 43.095362 · 採用条件未達 · 順位差 23.460461000000002 / 24.67952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 19.634901 · 採用条件未達 · 順位差 -23.460461000000002 / -43.645522 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 8.910891 · 採用条件未達 · 順位差 -34.184471 / -66.803395 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 8.910891 · 採用条件未達 · 順位差 -34.184471 / -66.803395 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 8.316832 · 採用条件未達 · 順位差 -34.77853 / -38.798553000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812084.md) · スコア 5.346535 · 採用条件未達 · 順位差 -37.748827 / -19.965965 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 3.564356 · 採用条件未達 · 順位差 -39.531006000000005 / -70.119855 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812800.md) · スコア 3.564356 · 採用条件未達 · 順位差 -39.531006000000005 / -33.099048999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6831683168316832,
          0.6831683168316832
        ],
        "cfg_coverage": [
          0.125,
          0.10526315789473684
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 23.460461000000002,
        "reverse_margin": 24.67952
      },
      "new": "00812400",
      "score": 43.095362
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.31683168316831684,
          0.3950617283950617
        ],
        "cfg_coverage": [
          0.03125,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.460461000000002,
        "reverse_margin": -43.645522
      },
      "new": "008129c0",
      "score": 19.634901
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1485148514851485,
          0.5357142857142857
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
        "margin": -34.184471,
        "reverse_margin": -66.803395
      },
      "new": "00812720",
      "score": 8.910891
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fbc04cdb1b4cecdcffa71bb85817e9f8"></a>

### v16.0.2 [`00811630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811630.md) FUN_00811630

`competing_candidates` 

呼出元 1件 [`006a7064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 73.684211 · 採用条件未達 · 順位差 4.7368430000000075 / 46.842106 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00812d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812d08.md) · スコア 68.947368 · 採用条件未達 · 順位差 -4.7368430000000075 / 32.631578999999995 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008121a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008121a8.md) · スコア 28.77193 · 採用条件未達 · 順位差 -44.91228100000001 / -13.581011 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812690.md) · スコア 12.631579 · 採用条件未達 · 順位差 -61.052632 / -43.479532 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812924.md) · スコア 12.307692 · 採用条件未達 · 順位差 -61.376519 / -29.903845999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005e49e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e49e8.md) · スコア 10.714286 · 採用条件未達 · 順位差 -62.969925 / 10.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 9.473684 · 採用条件未達 · 順位差 -64.210527 / -45.154887 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 8.148148 · 採用条件未達 · 順位差 -65.536063 / -55.132275 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 4.7368430000000075,
        "reverse_margin": 46.842106
      },
      "new": "00812594",
      "score": 73.684211
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8157894736842105,
          0.8157894736842105
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
        "margin": -4.7368430000000075,
        "reverse_margin": 32.631578999999995
      },
      "new": "00812d08",
      "score": 68.947368
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3684210526315789,
          0.4117647058823529
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
        "margin": -44.91228100000001,
        "reverse_margin": -13.581011
      },
      "new": "008121a8",
      "score": 28.77193
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-484646afaa1d32dd440214ce5a24df68"></a>

### v16.0.2 [`008116c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008116c8.md) FUN_008116c8

`competing_candidates` 

呼出元 9件 [`006a6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6614.md) [`006a6e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md) [`006a7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7518.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 54.628571 · 採用条件未達 · 順位差 33.99365 / 24.628571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 20.634921 · 採用条件未達 · 順位差 -33.99365 / -19.365079 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 20.0 · 採用条件未達 · 順位差 -34.628571 / -17.142857 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 20.0 · 採用条件未達 · 順位差 -34.628571 / -55.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 20.0 · 採用条件未達 · 順位差 -34.628571 / -55.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0064303c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/0064303c.md) · スコア 18.412698 · 採用条件未達 · 順位差 -36.215873 / -46.031746000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008122cc.md) · スコア 16.8 · 採用条件未達 · 順位差 -37.828571 / -21.987878999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 9.473684 · 採用条件未達 · 順位差 -45.154887 / -64.210527 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.72,
          0.72
        ],
        "cfg_coverage": [
          0.5714285714285714,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 33.99365,
        "reverse_margin": 24.628571
      },
      "new": "0081262c",
      "score": 54.628571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32,
          0.2962962962962963
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -33.99365,
        "reverse_margin": -19.365079
      },
      "new": "00812324",
      "score": 20.634921
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.32,
          0.2857142857142857
        ],
        "cfg_coverage": [
          0.14285714285714285,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -34.628571,
        "reverse_margin": -17.142857
      },
      "new": "00812390",
      "score": 20.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3897518a69b63585fb47af6870e99266"></a>

### v16.0.2 [`0081172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081172c.md) FUN_0081172c

`competing_candidates` 

呼出元 2件 [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) [`00a79c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79c74.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812690.md) · スコア 56.111111 · 採用条件未達 · 順位差 23.974359 / 19.764957000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812924.md) · スコア 32.136752 · 採用条件未達 · 順位差 -23.974359 / -10.074785999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md) · スコア 18.888889 · 採用条件未達 · 順位差 -37.222222 / -57.111111 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00866890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866890.md) · スコア 13.356009 · 採用条件未達 · 順位差 -42.755102 / 13.356009 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0099791c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00997/0099791c.md) · スコア 13.170732 · 採用条件未達 · 順位差 -42.940379 / 13.170732 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 6.315789 · 採用条件未達 · 順位差 -49.795322 / -67.36842200000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00c53358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md) · スコア 5.263158 · 採用条件未達 · 順位差 -50.847953000000004 / 5.263158 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 0.594059 · 採用条件未達 · 順位差 -55.517052 / -42.501303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.5555555555555556,
          0.7142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 23.974359,
        "reverse_margin": 19.764957000000003
      },
      "new": "00812690",
      "score": 56.111111
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5,
          0.46153846153846156
        ],
        "cfg_coverage": [
          0.2222222222222222,
          0.2222222222222222
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -23.974359,
        "reverse_margin": -10.074785999999996
      },
      "new": "00812924",
      "score": 32.136752
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2777777777777778,
          0.3333333333333333
        ],
        "cfg_coverage": [
          0.1111111111111111,
          0.1111111111111111
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.222222,
        "reverse_margin": -57.111111
      },
      "new": "0071d53c",
      "score": 18.888889
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`008117bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008117bc.md) FUN_008117bc

`competing_candidates` 

呼出元 1件 [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 75.714286 · 採用条件未達 · 順位差 2.1428570000000065 / 2.1428570000000065 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 73.571429 · 採用条件未達 · 順位差 -2.1428570000000065 / -2.1428570000000065 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 35.0 · 採用条件未達 · 順位差 -40.714286 / -2.1428569999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 22.619048 · 採用条件未達 · 順位差 -53.095238 / -17.380952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 20.47619 · 採用条件未達 · 順位差 -55.238096 / -34.152381000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 20.0 · 採用条件未達 · 順位差 -55.714286 / -27.115385000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 11.851852 · 採用条件未達 · 順位差 -63.862434 / -51.428571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 8.910891 · 採用条件未達 · 順位差 -66.803395 / -34.184471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9285714285714286,
          0.9285714285714286
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
        "margin": 2.1428570000000065,
        "reverse_margin": 2.1428570000000065
      },
      "new": "00812720",
      "score": 75.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8928571428571429,
          0.8928571428571429
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
        "margin": -2.1428570000000065,
        "reverse_margin": -2.1428570000000065
      },
      "new": "00812790",
      "score": 73.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5357142857142857,
          0.5357142857142857
        ],
        "cfg_coverage": [
          0.25,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -40.714286,
        "reverse_margin": -2.1428569999999993
      },
      "new": "00812390",
      "score": 35.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`0081182c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081182c.md) FUN_0081182c

`competing_candidates` 

呼出元 1件 [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 75.714286 · 採用条件未達 · 順位差 2.1428570000000065 / 2.1428570000000065 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 73.571429 · 採用条件未達 · 順位差 -2.1428570000000065 / -2.1428570000000065 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 35.0 · 採用条件未達 · 順位差 -40.714286 / -2.1428569999999993 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812324.md) · スコア 22.619048 · 採用条件未達 · 順位差 -53.095238 / -17.380952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 20.47619 · 採用条件未達 · 順位差 -55.238096 / -34.152381000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 20.0 · 採用条件未達 · 順位差 -55.714286 / -27.115385000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 11.851852 · 採用条件未達 · 順位差 -63.862434 / -51.428571 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 8.910891 · 採用条件未達 · 順位差 -66.803395 / -34.184471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9285714285714286,
          0.9285714285714286
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
        "margin": 2.1428570000000065,
        "reverse_margin": 2.1428570000000065
      },
      "new": "00812790",
      "score": 75.714286
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8928571428571429,
          0.8928571428571429
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
        "margin": -2.1428570000000065,
        "reverse_margin": -2.1428570000000065
      },
      "new": "00812720",
      "score": 73.571429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5357142857142857,
          0.5357142857142857
        ],
        "cfg_coverage": [
          0.25,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -40.714286,
        "reverse_margin": -2.1428569999999993
      },
      "new": "00812390",
      "score": 35.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b153b4aa35ea93f3848fd95391948f4a"></a>

### v16.0.2 [`0081189c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081189c.md) FUN_0081189c

`competing_candidates` 

呼出元 1件 [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812800.md) · スコア 36.663405 · 採用条件未達 · 順位差 19.510762999999997 / 27.774516 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 17.152642 · 採用条件未達 · 順位差 -19.510762999999997 / -29.962743000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 15.555556 · 採用条件未達 · 順位差 -21.107848999999998 / -47.724867 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 12.475248 · 採用条件未達 · 順位差 -24.188156999999997 / -30.620114 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 12.328767 · 採用条件未達 · 順位差 -24.334637999999998 / -63.385519 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 12.328767 · 採用条件未達 · 順位差 -24.334637999999998 / -63.385519 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) · スコア 9.863014 · 採用条件未達 · 順位差 -26.800390999999998 / -44.765557 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812b04.md) · スコア 7.407407 · 採用条件未達 · 順位差 -29.255997999999998 / -53.140097000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5753424657534246,
          0.5753424657534246
        ],
        "cfg_coverage": [
          0.10714285714285714,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.510762999999997,
        "reverse_margin": 27.774516
      },
      "new": "00812800",
      "score": 36.663405
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.273972602739726,
          0.5128205128205128
        ],
        "cfg_coverage": [
          0.03571428571428571,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.510762999999997,
        "reverse_margin": -29.962743000000003
      },
      "new": "00812230",
      "score": 17.152642
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2876712328767123,
          0.25925925925925924
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
        "margin": -21.107848999999998,
        "reverse_margin": -47.724867
      },
      "new": "008129c0",
      "score": 15.555556
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5900180ebcc2377bf2ec86e2466eb898"></a>

### v16.0.2 [`008119c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008119c0.md) FUN_008119c0

`competing_candidates` 

呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0091aa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091aa74.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812924.md) · スコア 42.211538 · 採用条件未達 · 順位差 5.865383999999999 / 10.074785999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812690.md) · スコア 36.346154 · 採用条件未達 · 順位差 -5.865383999999999 / -19.764957000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008121a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008121a8.md) · スコア 12.307692 · 採用条件未達 · 順位差 -29.903845999999998 / -30.045249000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 12.307692 · 採用条件未達 · 順位差 -29.903845999999998 / -61.376519 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812d08.md) · スコア 12.307692 · 採用条件未達 · 順位差 -29.903845999999998 / -56.639675999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md) · スコア 10.480769 · 採用条件未達 · 順位差 -31.730768999999995 / -65.519231 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00812084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812084.md) · スコア 8.4375 · 採用条件未達 · 順位差 -33.774038 / -16.875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0099791c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00997/0099791c.md) · スコア 7.317073 · 採用条件未達 · 順位差 -34.894465 / 7.317073 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6410256410256411,
          0.6410256410256411
        ],
        "cfg_coverage": [
          0.1875,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.865383999999999,
        "reverse_margin": 10.074785999999996
      },
      "new": "00812924",
      "score": 42.211538
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5641025641025641,
          0.6111111111111112
        ],
        "cfg_coverage": [
          0.125,
          0.2857142857142857
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.865383999999999,
        "reverse_margin": -19.764957000000003
      },
      "new": "00812690",
      "score": 36.346154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20512820512820512,
          0.23529411764705882
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
        "margin": -29.903845999999998,
        "reverse_margin": -30.045249000000002
      },
      "new": "008121a8",
      "score": 12.307692
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-074f49eafc0c069ffdedaeb924596811"></a>

### v16.0.2 [`00811a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811a5c.md) FUN_00811a5c

`competing_candidates` 

呼出元 0件  · 呼出先 3件 [`0081149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/0081149c.md) [`00811ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811ba0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 63.280423 · 採用条件未達 · 順位差 44.864581 / 43.645522 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 18.415842 · 採用条件未達 · 順位差 -44.864581 / -24.67952 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 11.851852 · 採用条件未達 · 順位差 -51.428571 / -63.862434 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 11.851852 · 採用条件未達 · 順位差 -51.428571 / -63.862434 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 9.62963 · 採用条件未達 · 順位差 -53.650793 / -37.485755000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812800.md) · スコア 8.888889 · 採用条件未達 · 順位差 -54.391534 / -27.774516 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 8.148148 · 採用条件未達 · 順位差 -55.132275 / -65.536063 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00812d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812d08.md) · スコア 8.148148 · 採用条件未達 · 順位差 -55.132275 / -60.79922 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8641975308641975,
          0.8641975308641975
        ],
        "cfg_coverage": [
          0.6153846153846154,
          0.5714285714285714
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 44.864581,
        "reverse_margin": 43.645522
      },
      "new": "008129c0",
      "score": 63.280423
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38271604938271603,
          0.3069306930693069
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
        "margin": -44.864581,
        "reverse_margin": -24.67952
      },
      "new": "00812400",
      "score": 18.415842
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.19753086419753085,
          0.5714285714285714
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
        "margin": -51.428571,
        "reverse_margin": -63.862434
      },
      "new": "00812720",
      "score": 11.851852
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2df6e3f6eff00990681ff3297368af7a"></a>

### v16.0.2 [`00811ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811ba0.md) FUN_00811ba0

`competing_candidates` 

呼出元 1件 [`00811a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811a5c.md) · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812b04.md) · スコア 60.547504 · 採用条件未達 · 順位差 56.103060000000006 / 53.140097000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812800.md) · スコア 4.444444 · 採用条件未達 · 順位差 -56.103060000000006 / -32.218961 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 3.703704 · 採用条件未達 · 順位差 -56.8438 / -59.576719 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 2.962963 · 採用条件未達 · 順位差 -57.584541 / -44.152422 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00812390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812390.md) · スコア 2.962963 · 採用条件未達 · 順位差 -57.584541 / -34.179894 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 2.962963 · 採用条件未達 · 順位差 -57.584541 / -72.751323 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 2.962963 · 採用条件未達 · 順位差 -57.584541 / -72.751323 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006dec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006dec20.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.547504 / -75.36 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8641975308641975,
          0.8641975308641975
        ],
        "cfg_coverage": [
          0.43478260869565216,
          0.45454545454545453
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 56.103060000000006,
        "reverse_margin": 53.140097000000004
      },
      "new": "00812b04",
      "score": 60.547504
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07407407407407407,
          0.0821917808219178
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
        "margin": -56.103060000000006,
        "reverse_margin": -32.218961
      },
      "new": "00812800",
      "score": 4.444444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06172839506172839,
          0.06172839506172839
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
        "margin": -56.8438,
        "reverse_margin": -59.576719
      },
      "new": "008129c0",
      "score": 3.703704
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00811ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811ce4.md) FUN_00811ce4

`competing_candidates` 

呼出元 1件 [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812c48.md) · スコア 47.5 · 採用条件未達 · 順位差 30.0 / 37.5 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812230.md) · スコア 17.5 · 採用条件未達 · 順位差 -30.0 / -29.615385000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00812720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812720.md) · スコア 10.0 · 採用条件未達 · 順位差 -37.5 / -65.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00812790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812790.md) · スコア 10.0 · 採用条件未達 · 順位差 -37.5 / -65.714286 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008129c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/008129c0.md) · スコア 5.925926 · 採用条件未達 · 順位差 -41.574074 / -57.354497 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007291f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/007291f4.md) · スコア 5.0 · 採用条件未達 · 順位差 -42.5 / -69.782609 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00729250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/00729250.md) · スコア 5.0 · 採用条件未達 · 順位差 -42.5 / 5.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00812400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812400.md) · スコア 4.752475 · 採用条件未達 · 順位差 -42.747525 / -38.342887000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7916666666666666,
          0.7916666666666666
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
        "margin": 30.0,
        "reverse_margin": 37.5
      },
      "new": "00812c48",
      "score": 47.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2916666666666667,
          0.358974358974359
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
        "margin": -30.0,
        "reverse_margin": -29.615385000000003
      },
      "new": "00812230",
      "score": 17.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16666666666666666,
          0.2857142857142857
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
        "margin": -37.5,
        "reverse_margin": -65.714286
      },
      "new": "00812720",
      "score": 10.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1db5860a4e1b6ba33d48d8ebc0963724"></a>

### v16.0.2 [`00811da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811da4.md) FUN_00811da4

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`00812d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812d08.md) · スコア 36.315789 · 採用条件未達 · 順位差 9.473684000000002 / -32.631578999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md) · スコア 26.842105 · 採用条件未達 · 順位差 -9.473684000000002 / -46.842106 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00afd0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd0e0.md) · スコア 15.789474 · 採用条件未達 · 順位差 -20.526315000000004 / 15.789474 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00b309bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b309bc.md) · スコア 14.210526 · 採用条件未達 · 順位差 -22.105263 / 14.210526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005e491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e491c.md) · スコア 11.764706 · 採用条件未達 · 順位差 -24.551083000000002 / 11.764706 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a43104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md) · スコア 10.0 · 採用条件未達 · 順位差 -26.315789000000002 / 10.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00af8b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af8/00af8b30.md) · スコア 8.955224 · 採用条件未達 · 順位差 -27.360565 / 8.955224 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005e4e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e4e84.md) · スコア 6.315789 · 採用条件未達 · 順位差 -30.000000000000004 / 6.315789 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6052631578947368,
          0.6052631578947368
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
        "margin": 9.473684000000002,
        "reverse_margin": -32.631578999999995
      },
      "new": "00812d08",
      "score": 36.315789
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4473684210526316,
          0.4473684210526316
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
        "margin": -9.473684000000002,
        "reverse_margin": -46.842106
      },
      "new": "00812594",
      "score": 26.842105
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2631578947368421,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -20.526315000000004,
        "reverse_margin": 15.789474
      },
      "new": "00afd0e0",
      "score": 15.789474
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`00815d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00815/00815d80.md) FUN_00815d80

`competing_candidates` 

呼出元 1件 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

- 1. [`00816ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00816/00816ce4.md) · スコア 64.185771 · 採用条件未達 · 順位差 53.249101 / 51.936759 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005c6340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6340.md) · スコア 10.93667 · 採用条件未達 · 順位差 -53.249101 / 10.93667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`005c1740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1740.md) · スコア 9.544886 · 採用条件未達 · 順位差 -54.640885000000004 / 9.544886 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009c87cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c8/009c87cc.md) · スコア 8.560679 · 採用条件未達 · 順位差 -55.625092 / 8.560679 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a33fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a33/00a33fdc.md) · スコア 8.173696 · 採用条件未達 · 順位差 -56.012075 / 8.173696 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007c8934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007c8/007c8934.md) · スコア 7.807967 · 採用条件未達 · 順位差 -56.377804000000005 / 7.807967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00663f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00663/00663f80.md) · スコア 7.297796 · 採用条件未達 · 順位差 -56.887975000000004 / 7.297796 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005c7aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c7aac.md) · スコア 7.220485 · 採用条件未達 · 順位差 -56.965286000000006 / 7.220485 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8045454545454546,
          0.8045454545454546
        ],
        "cfg_coverage": [
          0.7191011235955056,
          0.6956521739130435
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 53.249101,
        "reverse_margin": 51.936759
      },
      "new": "00816ce4",
      "score": 64.185771
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12272727272727273,
          0.20930232558139536
        ],
        "cfg_coverage": [
          0.07865168539325842,
          0.1206896551724138
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -53.249101,
        "reverse_margin": 10.93667
      },
      "new": "005c6340",
      "score": 10.93667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1409090909090909,
          0.11272727272727273
        ],
        "cfg_coverage": [
          0.056179775280898875,
          0.0390625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -54.640885000000004,
        "reverse_margin": 9.544886
      },
      "new": "005c1740",
      "score": 9.544886
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

### v16.0.2 [`008160f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/008160f0.md) FUN_008160f0

`competing_candidates` 

呼出元 2件 [`0082010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/0082010c.md) [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005c1884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1884.md)

- 1. [`00817054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00817/00817054.md) · スコア 60.705611 · 採用条件未達 · 順位差 56.802755 / 56.717856 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0091b294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0091b/0091b294.md) · スコア 3.902856 · 採用条件未達 · 順位差 -56.802755 / 3.902856 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00861a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00861/00861a94.md) · スコア 3.744007 · 採用条件未達 · 順位差 -56.961603999999994 / 3.744007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0093b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093b/0093b208.md) · スコア 3.731916 · 採用条件未達 · 順位差 -56.973695 / 3.731916 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b0d2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0d/00b0d2e4.md) · スコア 3.598082 · 採用条件未達 · 順位差 -57.107529 / 3.598082 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a67518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67518.md) · スコア 3.585991 · 採用条件未達 · 順位差 -57.11962 / -51.424974 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006ccf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cc/006ccf80.md) · スコア 3.177254 · 採用条件未達 · 順位差 -57.528357 / -74.468869 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006cbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbe7c.md) · スコア 3.061394 · 採用条件未達 · 順位差 -57.644217 / -74.571707 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.791869918699187,
          0.791869918699187
        ],
        "cfg_coverage": [
          0.5811965811965812,
          0.5596707818930041
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 56.802755,
        "reverse_margin": 56.717856
      },
      "new": "00817054",
      "score": 60.705611
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.026016260162601626,
          0.03902439024390244
        ],
        "cfg_coverage": [
          0.017094017094017096,
          0.026490066225165563
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -56.802755,
        "reverse_margin": 3.902856
      },
      "new": "0091b294",
      "score": 3.902856
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.027642276422764227,
          0.038202247191011236
        ],
        "cfg_coverage": [
          0.004273504273504274,
          0.005681818181818182
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -56.961603999999994,
        "reverse_margin": 3.744007
      },
      "new": "00861a94",
      "score": 3.744007
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2be299bc9555ba4cc4739438da8baee1"></a>

### v16.0.2 [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) FUN_00816b88

`competing_candidates` 

呼出元 6件 [`008160f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/008160f0.md) [`0081ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081ded8.md) [`0082010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/0082010c.md) [`0082250c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/0082250c.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00604dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00604/00604dd0.md) [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) [`0081a4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a4e8.md) [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md)

- 1. [`00817b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00817/00817b34.md) · スコア 53.263421 · 採用条件未達 · 順位差 49.15231 / 49.374532 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0062f670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062f/0062f670.md) · スコア 4.111111 · 採用条件未達 · 順位差 -49.15231 / 4.111111 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a43aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43aec.md) · スコア 3.412385 · 採用条件未達 · 順位差 -49.851036 / 3.412385 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006a4d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a4/006a4d04.md) · スコア 3.0 · 採用条件未達 · 順位差 -50.263421 / 3.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00737024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00737/00737024.md) · スコア 2.444444 · 採用条件未達 · 順位差 -50.818977000000004 / 2.444444 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00817054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00817/00817054.md) · スコア 2.097561 · 採用条件未達 · 順位差 -51.16586 / -58.60805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007f900c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f9/007f900c.md) · スコア 2.0 · 採用条件未達 · 順位差 -51.263421 / -44.179487 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a66e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md) · スコア 2.0 · 採用条件未達 · 順位差 -51.263421 / -74.755906 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.737037037037037,
          0.737037037037037
        ],
        "cfg_coverage": [
          0.3715415019762846,
          0.352059925093633
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.15231,
        "reverse_margin": 49.374532
      },
      "new": "00817b34",
      "score": 53.263421
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03518518518518519,
          0.05507246376811594
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
        "margin": -49.15231,
        "reverse_margin": 4.111111
      },
      "new": "0062f670",
      "score": 4.111111
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.022222222222222223,
          0.03418803418803419
        ],
        "cfg_coverage": [
          0.003952569169960474,
          0.006024096385542169
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -49.851036,
        "reverse_margin": 3.412385
      },
      "new": "00a43aec",
      "score": 3.412385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a1d80e72e87c851f644a6f7d09ec95de"></a>

### v16.0.2 [`0081a4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a4e8.md) FUN_0081a4e8

`competing_candidates` 

呼出元 1件 [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`0081b494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b494.md) · スコア 54.429348 · 採用条件未達 · 順位差 40.908514999999994 / 41.753291999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00524bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524bd0.md) · スコア 13.520833 · 採用条件未達 · 順位差 -40.908514999999994 / 13.520833 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0066564c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/0066564c.md) · スコア 13.25 · 採用条件未達 · 順位差 -41.179348 / 13.25 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00668b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00668/00668b94.md) · スコア 11.324984 · 採用条件未達 · 順位差 -43.104364 / 11.324984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008f32e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f32e4.md) · スコア 8.4375 · 採用条件未達 · 順位差 -45.991848 / 8.4375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008c98e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c98e0.md) · スコア 7.605634 · 採用条件未達 · 順位差 -46.823713999999995 / 7.605634 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008f08b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f08b4.md) · スコア 7.5 · 採用条件未達 · 順位差 -46.929348 / 7.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009e4ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e4ce8.md) · スコア 5.684211 · 採用条件未達 · 順位差 -48.745137 / 5.684211 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.71875,
          0.71875
        ],
        "cfg_coverage": [
          0.65,
          0.5652173913043478
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 40.908514999999994,
        "reverse_margin": 41.753291999999995
      },
      "new": "0081b494",
      "score": 54.429348
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.203125,
          0.21311475409836064
        ],
        "cfg_coverage": [
          0.1,
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
        "margin": -40.908514999999994,
        "reverse_margin": 13.520833
      },
      "new": "00524bd0",
      "score": 13.520833
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1875,
          0.24489795918367346
        ],
        "cfg_coverage": [
          0.1,
          0.2857142857142857
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -41.179348,
        "reverse_margin": 13.25
      },
      "new": "0066564c",
      "score": 13.25
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7ec9d8804f87fe9c6c9b75cdc7f5c3a0"></a>

### v16.0.2 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) FUN_0081cbe0

`competing_candidates` 

呼出元 10件 [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) [`0081c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c95c.md) [`0081cf38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cf38.md) [`0081ff94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081f/0081ff94.md) [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00815d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00815/00815d80.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`0081db8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081d/0081db8c.md) · スコア 79.586207 · 採用条件未達 · 順位差 68.691317 / 68.691317 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0072a0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072a/0072a0fc.md) · スコア 10.89489 · 採用条件未達 · 順位差 -68.691317 / 10.89489 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a683f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a68/00a683f0.md) · スコア 9.619443 · 採用条件未達 · 順位差 -69.966764 / -60.144532 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00b0827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b08/00b0827c.md) · スコア 9.307852 · 採用条件未達 · 順位差 -70.278355 / 9.307852 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005db5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005db/005db5f8.md) · スコア 7.101786 · 採用条件未達 · 順位差 -72.484421 / -39.850334000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0097e5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0097e/0097e5f8.md) · スコア 6.378895 · 採用条件未達 · 順位差 -73.207312 / 6.378895 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00668cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00668/00668cdc.md) · スコア 5.930204 · 採用条件未達 · 順位差 -73.656003 / 5.930204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00a66cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66cd0.md) · スコア 5.930204 · 採用条件未達 · 順位差 -73.656003 / 5.930204 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9597701149425287,
          0.9597701149425287
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
        "margin": 68.691317,
        "reverse_margin": 68.691317
      },
      "new": "0081db8c",
      "score": 79.586207
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13218390804597702,
          0.23711340206185566
        ],
        "cfg_coverage": [
          0.04819277108433735,
          0.14814814814814814
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -68.691317,
        "reverse_margin": 10.89489
      },
      "new": "0072a0fc",
      "score": 10.89489
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11494252873563218,
          0.19047619047619047
        ],
        "cfg_coverage": [
          0.03614457831325301,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -69.966764,
        "reverse_margin": -60.144532
      },
      "new": "00a683f0",
      "score": 9.619443
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1925c5452ce9f30066b31cd601923b0e"></a>

### v16.0.2 [`0081d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d560.md) FUN_0081d560

`competing_candidates` 

呼出元 4件 [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) [`0083336c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083336c.md) [`0083371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/0083371c.md) [`00833a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833a94.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0081d464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d464.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`0081e50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081e50c.md) · スコア 66.827176 · 採用条件未達 · 順位差 62.992737999999996 / 63.031665 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00816ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00816/00816ce4.md) · スコア 3.834438 · 採用条件未達 · 順位差 -62.992737999999996 / -60.351333000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00817054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00817/00817054.md) · スコア 3.304828 · 採用条件未達 · 順位差 -63.522347999999994 / -57.400783 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0081eb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081eb50.md) · スコア 2.897756 · 採用条件未達 · 順位差 -63.92941999999999 / -67.853093 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005e6bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e6/005e6bb0.md) · スコア 2.598504 · 採用条件未達 · 順位差 -64.22867199999999 / 2.598504 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00805534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00805/00805534.md) · スコア 2.452489 · 採用条件未達 · 順位差 -64.374687 / -46.374706 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007347d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00734/007347d0.md) · スコア 2.304183 · 採用条件未達 · 順位差 -64.522993 / -76.653992 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006cbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbe7c.md) · スコア 2.059821 · 採用条件未達 · 順位差 -64.767355 / -75.57328 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8653366583541147,
          0.8653366583541147
        ],
        "cfg_coverage": [
          0.676829268292683,
          0.6453488372093024
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 62.992737999999996,
        "reverse_margin": 63.031665
      },
      "new": "0081e50c",
      "score": 66.827176
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.022443890274314215,
          0.04090909090909091
        ],
        "cfg_coverage": [
          0.024390243902439025,
          0.043478260869565216
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -62.992737999999996,
        "reverse_margin": -60.351333000000004
      },
      "new": "00816ce4",
      "score": 3.834438
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02493765586034913,
          0.016260162601626018
        ],
        "cfg_coverage": [
          0.024390243902439025,
          0.01646090534979424
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -63.522347999999994,
        "reverse_margin": -57.400783
      },
      "new": "00817054",
      "score": 3.304828
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-979f16b76ff4d138d81814b6efa0774d"></a>

### v16.0.2 [`0081dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081dba4.md) FUN_0081dba4

`competing_candidates` 

呼出元 1件 [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0082250c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/0082250c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

- 1. [`0081eb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081e/0081eb50.md) · スコア 70.750849 · 採用条件未達 · 順位差 65.20986500000001 / 64.10744100000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ad7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7aec.md) · スコア 5.540984 · 採用条件未達 · 順位差 -65.20986500000001 / 5.540984 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`007f6228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f6/007f6228.md) · スコア 5.501946 · 採用条件未達 · 順位差 -65.248903 / -52.96064 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a845ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a84/00a845ec.md) · スコア 5.489782 · 採用条件未達 · 順位差 -65.261067 / 5.489782 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`005c89b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c89b4.md) · スコア 5.219512 · 採用条件未達 · 順位差 -65.53133700000001 / 5.219512 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007850f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/007850f4.md) · スコア 5.088235 · 採用条件未達 · 順位差 -65.662614 / -63.637254999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0082ba7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082b/0082ba7c.md) · スコア 4.593276 · 採用条件未達 · 順位差 -66.157573 / 4.593276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0066b08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066b/0066b08c.md) · スコア 3.756098 · 採用条件未達 · 順位差 -66.99475100000001 / 3.756098 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8926829268292683,
          0.8926829268292683
        ],
        "cfg_coverage": [
          0.8108108108108109,
          0.759493670886076
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 65.20986500000001,
        "reverse_margin": 64.10744100000001
      },
      "new": "0081eb50",
      "score": 70.750849
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08780487804878048,
          0.05901639344262295
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
        "margin": -65.20986500000001,
        "reverse_margin": 5.540984
      },
      "new": "00ad7aec",
      "score": 5.540984
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07317073170731707,
          0.058365758754863814
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
        "margin": -65.248903,
        "reverse_margin": -52.96064
      },
      "new": "007f6228",
      "score": 5.501946
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-30b90189d0d6080cd7dca2e077b2875b"></a>

### v16.0.2 [`0082010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/0082010c.md) FUN_0082010c

`competing_candidates` 

呼出元 4件 [`006170ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170ec.md) [`0061e4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e4a8.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 5件 [`008160f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/008160f0.md) [`00816b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/00816b88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

- 1. [`008210b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00821/008210b8.md) · スコア 76.774194 · 採用条件未達 · 順位差 60.94413899999999 / 60.94413899999999 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00519d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519d5c.md) · スコア 15.830055 · 採用条件未達 · 順位差 -60.94413899999999 / 15.830055 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00519e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519e44.md) · スコア 15.830055 · 採用条件未達 · 順位差 -60.94413899999999 / 15.830055 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007739c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/007739c8.md) · スコア 11.455547 · 採用条件未達 · 順位差 -65.318647 / 11.455547 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00abf314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abf/00abf314.md) · スコア 11.29819 · 採用条件未達 · 順位差 -65.47600399999999 / 11.29819 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`004ff3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff3a0.md) · スコア 10.668765 · 採用条件未達 · 順位差 -66.10542899999999 / 10.668765 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00b407b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b407b4.md) · スコア 10.668765 · 採用条件未達 · 順位差 -66.10542899999999 / 10.668765 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00514418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/00514418.md) · スコア 10.126829 · 採用条件未達 · 順位差 -66.647365 / 10.126829 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.946236559139785,
          0.946236559139785
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
        "margin": 60.94413899999999,
        "reverse_margin": 60.94413899999999
      },
      "new": "008210b8",
      "score": 76.774194
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21505376344086022,
          0.4166666666666667
        ],
        "cfg_coverage": [
          0.14634146341463414,
          0.42857142857142855
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -60.94413899999999,
        "reverse_margin": 15.830055
      },
      "new": "00519d5c",
      "score": 15.830055
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21505376344086022,
          0.4166666666666667
        ],
        "cfg_coverage": [
          0.14634146341463414,
          0.42857142857142855
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -60.94413899999999,
        "reverse_margin": 15.830055
      },
      "new": "00519e44",
      "score": 15.830055
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cf69baaa40183ea84377707bf62c477c"></a>

### v16.0.2 [`00822cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00822/00822cf0.md) FUN_00822cf0

`competing_candidates` 

呼出元 2件 [`0081ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081ded8.md) [`00823068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00823/00823068.md) · 呼出先 5件 [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

- 1. [`00823c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00823/00823c9c.md) · スコア 73.023256 · 採用条件未達 · 順位差 65.348837 / 66.032965 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`0088cbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cbf0.md) · スコア 7.674419 · 採用条件未達 · 順位差 -65.348837 / 7.674419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00a9b868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a9b/00a9b868.md) · スコア 7.674419 · 採用条件未達 · 順位差 -65.348837 / 7.674419 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`004502bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/004502bc.md) · スコア 6.990291 · 採用条件未達 · 順位差 -66.032965 / 6.990291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008666ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/008666ac.md) · スコア 6.976744 · 採用条件未達 · 順位差 -66.046512 / 6.976744 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0069f31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069f/0069f31c.md) · スコア 6.804124 · 採用条件未達 · 順位差 -66.219132 / 6.804124 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004fcb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fc/004fcb78.md) · スコア 6.226415 · 採用条件未達 · 順位差 -66.796841 / 6.226415 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00667754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00667/00667754.md) · スコア 6.206897 · 採用条件未達 · 順位差 -66.816359 / 6.206897 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8837209302325582,
          0.8837209302325582
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
        "margin": 65.348837,
        "reverse_margin": 66.032965
      },
      "new": "00823c9c",
      "score": 73.023256
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12790697674418605,
          0.171875
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
        "margin": -65.348837,
        "reverse_margin": 7.674419
      },
      "new": "0088cbf0",
      "score": 7.674419
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12790697674418605,
          0.15714285714285714
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
        "margin": -65.348837,
        "reverse_margin": 7.674419
      },
      "new": "00a9b868",
      "score": 7.674419
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f0510b5c73744ec65b4788bc2e1cc48a"></a>

### v16.0.2 [`00824270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824270.md) FUN_00824270

`competing_candidates` 

呼出元 1件 [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

- 1. [`0082521c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00825/0082521c.md) · スコア 74.984127 · 採用条件未達 · 順位差 63.555556 / 63.555556 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00807184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807184.md) · スコア 11.428571 · 採用条件未達 · 順位差 -63.555556 / -58.430015000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00807260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807260.md) · スコア 11.428571 · 採用条件未達 · 順位差 -63.555556 / -59.520924 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0080733c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/0080733c.md) · スコア 11.428571 · 採用条件未達 · 順位差 -63.555556 / -56.248197 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00807418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807418.md) · スコア 11.428571 · 採用条件未達 · 順位差 -63.555556 / -66.207793 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008041a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00804/008041a0.md) · スコア 10.571429 · 採用条件未達 · 順位差 -64.412698 / -68.47775100000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008074f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/008074f4.md) · スコア 6.285714 · 採用条件未達 · 順位差 -68.698413 / -46.322982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`004a55f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a55f0.md) · スコア 3.428571 · 採用条件未達 · 順位差 -71.555556 / 3.428571 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9571428571428572,
          0.9571428571428572
        ],
        "cfg_coverage": [
          0.8076923076923077,
          0.7777777777777778
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 63.555556,
        "reverse_margin": 63.555556
      },
      "new": "0082521c",
      "score": 74.984127
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15714285714285714,
          0.2
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
        "margin": -63.555556,
        "reverse_margin": -58.430015000000004
      },
      "new": "00807184",
      "score": 11.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15714285714285714,
          0.2
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
        "margin": -63.555556,
        "reverse_margin": -59.520924
      },
      "new": "00807260",
      "score": 11.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0765e691234db56704522fcd57bb314a"></a>

### v16.0.2 [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) FUN_008246d4

`competing_candidates` 

呼出元 1件 [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) · 呼出先 23件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md)

- 1. [`00825680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00825/00825680.md) · スコア 39.552184 · 採用条件未達 · 順位差 37.391664999999996 / 37.351094999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a48f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · スコア 2.160519 · 採用条件未達 · 順位差 -37.391664999999996 / -58.920049999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0085e4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085e/0085e4f8.md) · スコア 2.144095 · 採用条件未達 · 順位差 -37.408089 / 2.144095 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007bea00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007be/007bea00.md) · スコア 2.031652 · 採用条件未達 · 順位差 -37.520531999999996 / -54.555515 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00ab77a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ab7/00ab77a4.md) · スコア 2.0 · 採用条件未達 · 順位差 -37.552184 / -61.918055 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`009a2600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a2/009a2600.md) · スコア 0.377223 · 採用条件未達 · 順位差 -39.174960999999996 / 0.377223 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a88b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a88/00a88b34.md) · スコア 0.176314 · 採用条件未達 · 順位差 -39.37587 / -75.761196 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00660d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00660/00660d28.md) · スコア 0.100545 · 採用条件未達 · 順位差 -39.451639 / 0.100545 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5111018014243821,
          0.5111018014243821
        ],
        "cfg_coverage": [
          0.24430379746835443,
          0.24967658473479948
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 37.391664999999996,
        "reverse_margin": 37.351094999999994
      },
      "new": "00825680",
      "score": 39.552184
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006702974444909929,
          0.0022717591935254864
        ],
        "cfg_coverage": [
          0.002531645569620253,
          0.0012106537530266344
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -37.391664999999996,
        "reverse_margin": -58.920049999999996
      },
      "new": "00a48f48",
      "score": 2.160519
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0025136154168412233,
          0.002003338898163606
        ],
        "cfg_coverage": [
          0.0012658227848101266,
          0.0011947431302270011
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -37.408089,
        "reverse_margin": 2.144095
      },
      "new": "0085e4f8",
      "score": 2.144095
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d1ec30f625bf1a29a3c24ee4dc45c1bd"></a>

### v16.0.2 [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) FUN_00827970

`competing_candidates` 

呼出元 1件 [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) · 呼出先 34件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

- 1. [`0082891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00828/0082891c.md) · スコア 49.983741 · 採用条件未達 · 順位差 44.200288 / 44.789711000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006ae338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ae/006ae338.md) · スコア 5.783453 · 採用条件未達 · 順位差 -44.200288 / -67.528022 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00b1c878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b1c/00b1c878.md) · スコア 4.392413 · 採用条件未達 · 順位差 -45.591328000000004 / -38.108677 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006ab78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ab/006ab78c.md) · スコア 4.389972 · 採用条件未達 · 順位差 -45.593769 / -69.236769 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0089b55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089b/0089b55c.md) · スコア 4.0 · 採用条件未達 · 順位差 -45.983741 / -7.658915 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00808d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00808/00808d68.md) · スコア 2.776119 · 採用条件未達 · 順位差 -47.207622 / 2.776119 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00813130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00813/00813130.md) · スコア 2.595117 · 採用条件未達 · 順位差 -47.388624 / 2.595117 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007566ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00756/007566ac.md) · スコア 2.285412 · 採用条件未達 · 順位差 -47.698329 / -66.936575 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5671641791044776,
          0.5671641791044776
        ],
        "cfg_coverage": [
          0.3988439306358382,
          0.3976945244956772
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 44.200288,
        "reverse_margin": 44.789711000000004
      },
      "new": "0082891c",
      "score": 49.983741
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.025870646766169153,
          0.02841530054644809
        ],
        "cfg_coverage": [
          0.011560693641618497,
          0.012121212121212121
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -44.200288,
        "reverse_margin": -67.528022
      },
      "new": "006ae338",
      "score": 5.783453
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.009950248756218905,
          0.006540222367560497
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -45.591328000000004,
        "reverse_margin": -38.108677
      },
      "new": "00b1c878",
      "score": 4.392413
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c2064b7af16947611225c838e9ae3c19"></a>

### v16.0.2 [`0082bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bec0.md) FUN_0082bec0

`competing_candidates` 

呼出元 1件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) · 呼出先 10件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a467d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a467d8.md) [`00a4691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4691c.md)

- 1. [`0082ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082c/0082ce6c.md) · スコア 11.491215 · 採用条件未達 · 順位差 6.518839000000001 / -18.658342 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0082c904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082c/0082c904.md) · スコア 4.972376 · 採用条件未達 · 順位差 -6.518839000000001 / 4.972376 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006d1048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md) · スコア 3.680982 · 採用条件未達 · 順位差 -7.810233 / 3.680982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006d1354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md) · スコア 3.680982 · 採用条件未達 · 順位差 -7.810233 / 3.680982 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007f1530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f1/007f1530.md) · スコア 3.529412 · 採用条件未達 · 順位差 -7.961803 / 3.529412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00acafc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md) · スコア 3.292683 · 採用条件未達 · 順位差 -8.198532 / 3.292683 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0062b464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062b/0062b464.md) · スコア 0.0 · 採用条件未達 · 順位差 -11.491215 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00bc8378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc8/00bc8378.md) · スコア 0.0 · 採用条件未達 · 順位差 -11.491215 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6463414634146342,
          0.18213058419243985
        ],
        "cfg_coverage": [
          0.2857142857142857,
          0.028169014084507043
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 6.518839000000001,
        "reverse_margin": -18.658342
      },
      "new": "0082ce6c",
      "score": 11.491215
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18292682926829268,
          0.08287292817679558
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
        "margin": -6.518839000000001,
        "reverse_margin": 4.972376
      },
      "new": "0082c904",
      "score": 4.972376
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12195121951219512,
          0.06134969325153374
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
        "margin": -7.810233,
        "reverse_margin": 3.680982
      },
      "new": "006d1048",
      "score": 3.680982
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-766050793f0ce137439e0cee1588d387"></a>

### v16.0.2 [`0082c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c008.md) FUN_0082c008

`competing_candidates` 

呼出元 1件 [`00c57dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dac.md) · 呼出先 14件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) [`00832124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832124.md) [`00832128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832128.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`0082ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082c/0082ce6c.md) · スコア 30.149557 · 採用条件未達 · 順位差 10.209140000000001 / 15.655583000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006d1048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md) · スコア 19.940417 · 採用条件未達 · 順位差 -10.209140000000001 / 19.940417 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006d1354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md) · スコア 18.792092 · 採用条件未達 · 順位差 -11.357465000000001 / 18.792092 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00acafc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md) · スコア 16.421414 · 採用条件未達 · 順位差 -13.728143000000003 / 16.421414 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0082c904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082c/0082c904.md) · スコア 14.592399 · 採用条件未達 · 順位差 -15.557158000000001 / 14.592399 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`009358d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00935/009358d0.md) · スコア 11.704763 · 採用条件未達 · 順位差 -18.444794 / 11.704763 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a62770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a62/00a62770.md) · スコア 7.041847 · 採用条件未達 · 順位差 -23.10771 / 7.041847 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00acab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acab50.md) · スコア 5.783133 · 採用条件未達 · 順位差 -24.366424000000002 / 5.783133 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5885167464114832,
          0.422680412371134
        ],
        "cfg_coverage": [
          0.32075471698113206,
          0.23943661971830985
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.209140000000001,
        "reverse_margin": 15.655583000000002
      },
      "new": "0082ce6c",
      "score": 30.149557
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2631578947368421,
          0.3374233128834356
        ],
        "cfg_coverage": [
          0.20754716981132076,
          0.34375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -10.209140000000001,
        "reverse_margin": 19.940417
      },
      "new": "006d1048",
      "score": 19.940417
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24401913875598086,
          0.3128834355828221
        ],
        "cfg_coverage": [
          0.20754716981132076,
          0.3055555555555556
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -11.357465000000001,
        "reverse_margin": 18.792092
      },
      "new": "006d1354",
      "score": 18.792092
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1d1b03a04b6c9fbfb6f705a5ae140460"></a>

### v16.0.2 [`0082c638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c638.md) FUN_0082c638

`competing_candidates` 

呼出元 1件 [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

- 1. [`0082d5e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d5e4.md) · スコア 76.190476 · 採用条件未達 · 順位差 66.209997 / 65.982185 · cfg_coverage, insufficient_independent_call_anchors
- 2. [`008284f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00828/008284f8.md) · スコア 9.980479 · 採用条件未達 · 順位差 -66.209997 / 9.980479 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006acd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ac/006acd20.md) · スコア 7.619048 · 採用条件未達 · 順位差 -68.571428 / 7.619048 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0082a398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082a/0082a398.md) · スコア 7.450395 · 採用条件未達 · 順位差 -68.740081 / 7.450395 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0082b7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082b/0082b7a4.md) · スコア 6.363889 · 採用条件未達 · 順位差 -69.826587 / 6.363889 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`0082817c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00828/0082817c.md) · スコア 6.200181 · 採用条件未達 · 順位差 -69.990295 / 6.200181 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008286c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00828/008286c4.md) · スコア 5.812658 · 採用条件未達 · 順位差 -70.377818 / 5.812658 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0082bb7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082b/0082bb7c.md) · スコア 2.857143 · 採用条件未達 · 順位差 -73.33333300000001 / 2.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9841269841269841,
          0.9841269841269841
        ],
        "cfg_coverage": [
          0.9,
          0.8571428571428571
        ],
        "mapped_data": 0,
        "held": [
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 66.209997,
        "reverse_margin": 65.982185
      },
      "new": "0082d5e4",
      "score": 76.190476
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.25396825396825395,
          0.1391304347826087
        ],
        "cfg_coverage": [
          0.1,
          0.08163265306122448
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -66.209997,
        "reverse_margin": 9.980479
      },
      "new": "008284f8",
      "score": 9.980479
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20634920634920634,
          0.1111111111111111
        ],
        "cfg_coverage": [
          0.05,
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
        "margin": -68.571428,
        "reverse_margin": 7.619048
      },
      "new": "006acd20",
      "score": 7.619048
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-eeafb4234b0e891b4ab60d360510749c"></a>

### v16.0.2 [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) FUN_0082cd70

`competing_candidates` 

呼出元 1件 [`0082f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082f180.md) · 呼出先 21件 [`008160f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00816/008160f0.md) [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) [`0082abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082abd0.md) [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`0082d538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d538.md)

- 1. [`0082dd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082dd1c.md) · スコア 46.215835 · 採用条件未達 · 順位差 41.542938 / 41.541174 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0082d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d868.md) · スコア 4.672897 · 採用条件未達 · 順位差 -41.542938 / 4.672897 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0082e7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082e/0082e7ac.md) · スコア 3.46634 · 採用条件未達 · 順位差 -42.749494999999996 / 3.46634 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008ac2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ac/008ac2bc.md) · スコア 2.33387 · 採用条件未達 · 順位差 -43.881965 / 2.33387 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006e01d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e01d0.md) · スコア 1.392118 · 採用条件未達 · 順位差 -44.823717 / 1.392118 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008210b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00821/008210b8.md) · スコア 1.308411 · 採用条件未達 · 順位差 -44.907424 / -75.46578299999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0082398c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00823/0082398c.md) · スコア 1.121495 · 採用条件未達 · 順位差 -45.094339999999995 / 1.121495 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md) · スコア 0.934579 · 採用条件未達 · 順位差 -45.281256 / 0.934579 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6853582554517134,
          0.6853582554517134
        ],
        "cfg_coverage": [
          0.25471698113207547,
          0.25471698113207547
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 41.542938,
        "reverse_margin": 41.541174
      },
      "new": "0082dd1c",
      "score": 46.215835
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0778816199376947,
          0.09398496240601503
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
        "margin": -41.542938,
        "reverse_margin": 4.672897
      },
      "new": "0082d868",
      "score": 4.672897
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.04984423676012461,
          0.04833836858006042
        ],
        "cfg_coverage": [
          0.02830188679245283,
          0.0297029702970297
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -42.749494999999996,
        "reverse_margin": 3.46634
      },
      "new": "0082e7ac",
      "score": 3.46634
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3d46a2afe2cba3a3c1747f67892231d"></a>

### v16.0.2 [`0082ee74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee74.md) FUN_0082ee74

`competing_candidates` 

呼出元 1件 [`009ccbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccbd0.md) · 呼出先 0件 

- 1. [`0082fe20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fe20.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "0082fe20",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8c43c61f32f0598376dcb385e68c32d9"></a>

### v16.0.2 [`0083065c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083065c.md) FUN_0083065c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831608.md) · スコア 69.0 · 採用条件未達 · 順位差 69.0 / 69.0 · 

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
      "new": "00831608",
      "score": 69.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-08cbbf9e04f5e06ed2b14f4cdf69e6a6"></a>

### v16.0.2 [`00830b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b60.md) FUN_00830b60

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006274d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00627/006274d4.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006fde0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde0c.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00784860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00784/00784860.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 4. [`00831b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b0c.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 5. [`00aee6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee6b8.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "006274d4",
      "score": 65.0
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "006fde0c",
      "score": 65.0
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "00784860",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-037f47c33fb0aba122cb6243e7f11376"></a>

### v16.0.2 [`00830b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b80.md) FUN_00830b80

`competing_candidates` 

呼出元 1件 [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) · 呼出先 0件 

- 1. [`00831b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b2c.md) · スコア 69.0 · 採用条件未達 · 順位差 68.5 / 68.5 · 
- 2. [`00831b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b0c.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.5,
        "reverse_margin": 68.5
      },
      "new": "00831b2c",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831b0c",
      "score": 0.5
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-9d9639fe78d6bcccd6764aa28edc369e"></a>

### v16.0.2 [`00830bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bc8.md) FUN_00830bc8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005d9e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d9/005d9e3c.md) · スコア 71.428571 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f7a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f7/007f7a5c.md) · スコア 71.428571 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00893ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893ae4.md) · スコア 58.095238 · 採用条件未達 · 順位差 -13.333333000000003 / -13.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 4. [`009a4658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a4/009a4658.md) · スコア 58.095238 · 採用条件未達 · 順位差 -13.333333000000003 / -13.333333000000003 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 5. [`00628038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00628/00628038.md) · スコア 46.190476 · 採用条件未達 · 順位差 -25.23809500000001 / -15.238095000000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 6. [`00ac42a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac4/00ac42a0.md) · スコア 46.190476 · 採用条件未達 · 順位差 -25.23809500000001 / -10.238095000000001 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, insufficient_independent_call_anchors
- 7. [`0078387c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/0078387c.md) · スコア 44.285714 · 採用条件未達 · 順位差 -27.142857000000006 / -17.142857 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00831b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b74.md) · スコア 0.0 · 採用条件未達 · 順位差 -71.428571 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "005d9e3c",
      "score": 71.428571
    },
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
        "margin": 0.0,
        "reverse_margin": 0.0
      },
      "new": "007f7a5c",
      "score": 71.428571
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8571428571428571,
          0.8571428571428571
        ],
        "cfg_coverage": [
          0.3333333333333333,
          0.4
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.333333000000003,
        "reverse_margin": -13.333333000000003
      },
      "new": "00893ae4",
      "score": 58.095238
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-625aa8434f9689541b44017e3648edbd"></a>

### v16.0.2 [`00830be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830be4.md) FUN_00830be4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b90.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831b74.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831b90",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831b74",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ba2bf3db8dc75656093a61e030868e61"></a>

### v16.0.2 [`00830c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830c28.md) FUN_00830c28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831bd4.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.6
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
        "margin": 56.0,
        "reverse_margin": -24.0
      },
      "new": "00831bd4",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b5a009862e897882d855e2426b887c27"></a>

### v16.0.2 [`00830c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830c3c.md) FUN_00830c3c

`competing_candidates` 

呼出元 1件 [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) · 呼出先 0件 

- 1. [`00831be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831be8.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`00831bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831bd4.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.2,
        "reverse_margin": 68.2
      },
      "new": "00831be8",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831bd4",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-177793812404497bfd2e4132a7fa5bcc"></a>

### v16.0.2 [`00830ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ca8.md) FUN_00830ca8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c54.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831c54",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56af708e8f623f9e7516df1dea42e38c"></a>

### v16.0.2 [`00830cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830cc4.md) FUN_00830cc4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c70.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831c54.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831c70",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831c54",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1b23967503c2ec2e32ba5ae71fba4067"></a>

### v16.0.2 [`00830e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830e6c.md) FUN_00830e6c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`005b8644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b8644.md) · スコア 69.411765 · 採用条件未達 · 順位差 19.411765000000003 / 69.411765 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00831e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831e18.md) · スコア 50.0 · 採用条件未達 · 順位差 -19.411765000000003 / 50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009b8b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b8/009b8b78.md) · スコア 32.679739 · 採用条件未達 · 順位差 -36.732026000000005 / 32.679739 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.8235294117647058
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
        "margin": 19.411765000000003,
        "reverse_margin": 69.411765
      },
      "new": "005b8644",
      "score": 69.411765
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6428571428571429,
          0.6428571428571429
        ],
        "cfg_coverage": [
          0.5714285714285714,
          0.6666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.411765000000003,
        "reverse_margin": 50.0
      },
      "new": "00831e18",
      "score": 50.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5714285714285714,
          0.47058823529411764
        ],
        "cfg_coverage": [
          0.2857142857142857,
          0.2222222222222222
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
        "margin": -36.732026000000005,
        "reverse_margin": 32.679739
      },
      "new": "009b8b78",
      "score": 32.679739
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ca1fe5f098bf6097ef0d719d841abbab"></a>

### v16.0.2 [`00830f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f74.md) FUN_00830f74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f20.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00831f20",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c180f92f01438b340c9b41cab0262d62"></a>

### v16.0.2 [`00830f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f90.md) FUN_00830f90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00831f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f3c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00831f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00831/00831f20.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00831f3c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00831f20",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7d5a64f6a4e4cf0cd24ad6b2d9995482"></a>

### v16.0.2 [`00831138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831138.md) FUN_00831138

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008320e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008320e4.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors

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
      "new": "008320e4",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11ffa968ac4cd46bc530792925bed4ca"></a>

### v16.0.2 [`0083120c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083120c.md) FUN_0083120c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008321b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008321b8.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008321b8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c5d59313107103eb7a203bf27f1c98d5"></a>

### v16.0.2 [`00831228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831228.md) FUN_00831228

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008321d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008321d4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008321b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008321b8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008321d4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008321b8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2a49476c5f647e9dee8c0ca9b53249a2"></a>

### v16.0.2 [`008312d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312d0.md) FUN_008312d0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0083227c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/0083227c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0083227c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9a0b3698bcd6be88c9280c0fb1864c5d"></a>

### v16.0.2 [`008312ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312ec.md) FUN_008312ec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832298.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0083227c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/0083227c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832298",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0083227c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-55dfd5f29b3b262940eb4e285d3fd3eb"></a>

### v16.0.2 [`008316f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008316f8.md) FUN_008316f8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008326a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008326a4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b0b42148f099d0731bed6d54004f34f7"></a>

### v16.0.2 [`00831714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831714.md) FUN_00831714

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008326c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326c0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008326a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/008326a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "008326c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008326a4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f5c6f03cfd6ed8f7e452d2b7cb78034f"></a>

### v16.0.2 [`008317bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317bc.md) FUN_008317bc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832768.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00832768",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-aba172e196903103146b6b167427baf8"></a>

### v16.0.2 [`008317d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317d8.md) FUN_008317d8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832784.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00832768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832768.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832784",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00832768",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3765c1c121108a7dfcbb6ad830a259f6"></a>

### v16.0.2 [`00831b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831b28.md) FUN_00831b28

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ad4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00832ad4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9a87ef0bf8a9da49d86357ebe2634260"></a>

### v16.0.2 [`00831b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831b44.md) FUN_00831b44

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832af0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00832ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832ad4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832af0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00832ad4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-23bb1c4a4f8baa64684f7edacd0031c7"></a>

### v16.0.2 [`00831ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ec0.md) FUN_00831ec0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832e6c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00832e6c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-442ba44a9a65bb249b5e3494c96a5341"></a>

### v16.0.2 [`00831edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831edc.md) FUN_00831edc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832e88.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00832e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832e6c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832e88",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00832e6c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-a03f87ace49b372474b9059962a01b1f"></a>

### v16.0.2 [`00831fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831fd0.md) FUN_00831fd0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832f7c.md) · スコア 54.285714 · 採用条件未達 · 順位差 11.428570999999998 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`009de0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009de/009de0c8.md) · スコア 42.857143 · 採用条件未達 · 順位差 -11.428570999999998 / -20.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 11.428570999999998,
        "reverse_margin": 54.285714
      },
      "new": "00832f7c",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7142857142857143,
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
        "margin": -11.428570999999998,
        "reverse_margin": -20.0
      },
      "new": "009de0c8",
      "score": 42.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4c2a55aa7ecfc8e3d87bbe22132d1974"></a>

### v16.0.2 [`00831fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831fec.md) FUN_00831fec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00832f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832f98.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00832f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00832/00832f7c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00832f98",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00832f7c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-0fb40889014059a27b0970d5cac2e03d"></a>

### v16.0.2 [`008320b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320b0.md) FUN_008320b0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0083305c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/0083305c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "0083305c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2672e616a3101237063560104acf46c1"></a>

### v16.0.2 [`008320cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320cc.md) FUN_008320cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00833078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/00833078.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`0083305c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/0083305c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00833078",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0083305c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b0d66a9e050f447a44cffa3aa053fe39"></a>

### v16.0.2 [`00832110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832110.md) FUN_00832110

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0078f154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f154.md) · スコア 80.0 · 採用条件未達 · 順位差 24.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`008330bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330bc.md) · スコア 56.0 · 採用条件未達 · 順位差 -24.0 / 56.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
        "margin": 24.0,
        "reverse_margin": 80.0
      },
      "new": "0078f154",
      "score": 80.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.6
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
        "margin": -24.0,
        "reverse_margin": 56.0
      },
      "new": "008330bc",
      "score": 56.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fc894b9d673b9062e470aba5fd6081c4"></a>

### v16.0.2 [`00832124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832124.md) FUN_00832124

`competing_candidates` 

呼出元 1件 [`0082c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c008.md) · 呼出先 0件 

- 1. [`008330d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330d0.md) · スコア 69.0 · 採用条件未達 · 順位差 68.2 / 68.2 · 
- 2. [`008330bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00833/008330bc.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 68.2,
        "reverse_margin": 68.2
      },
      "new": "008330d0",
      "score": 69.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008330bc",
      "score": 0.8
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e83ae616e5b9b2fc460f0ee76447cd24"></a>

### v16.0.2 [`00833344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833344.md) FUN_00833344

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008342f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008342f0.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008342f0",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-79b0e258ab52946abde9416ed8cbd5cd"></a>

### v16.0.2 [`00833360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00833/00833360.md) FUN_00833360

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0083430c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/0083430c.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008342f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00834/008342f0.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "0083430c",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008342f0",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-25134edf90a35616c84e666c37a55b07"></a>

### v16.0.2 [`00834990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834990.md) FUN_00834990

`competing_candidates` 

呼出元 2件 [`008341a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/008341a0.md) [`00834990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834990.md) · 呼出先 2件 [`00834990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834990.md) [`00834fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/00834fec.md)

- 1. [`0083593c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00835/0083593c.md) · スコア 70.49009 · 採用条件未達 · 順位差 67.56450199999999 / 67.46470099999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009ff20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ff/009ff20c.md) · スコア 2.925588 · 採用条件未達 · 順位差 -67.56450199999999 / 2.925588 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009ffd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ff/009ffd94.md) · スコア 2.335907 · 採用条件未達 · 順位差 -68.15418299999999 / 2.335907 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          0.7357142857142858,
          0.6866666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 67.56450199999999,
        "reverse_margin": 67.46470099999999
      },
      "new": "0083593c",
      "score": 70.49009
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.036855036855036855,
          0.05660377358490566
        ],
        "cfg_coverage": [
          0.03571428571428571,
          0.05555555555555555
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -67.56450199999999,
        "reverse_margin": 2.925588
      },
      "new": "009ff20c",
      "score": 2.925588
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.02702702702702703,
          0.04150943396226415
        ],
        "cfg_coverage": [
          0.03571428571428571,
          0.058823529411764705
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -68.15418299999999,
        "reverse_margin": 2.335907
      },
      "new": "009ffd94",
      "score": 2.335907
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2741d76d69481be34203634fc1016543"></a>

### v16.0.2 [`008354cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354cc.md) FUN_008354cc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836478.md) · スコア 54.285714 · 採用条件未達 · 順位差 20.0 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`007f6970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f6/007f6970.md) · スコア 34.285714 · 採用条件未達 · 順位差 -20.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 20.0,
        "reverse_margin": 54.285714
      },
      "new": "00836478",
      "score": 54.285714
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
      "new": "007f6970",
      "score": 34.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-542df5573b58092589534ad5245e95d6"></a>

### v16.0.2 [`008354e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354e8.md) FUN_008354e8

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836494.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00836478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836478.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00836494",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00836478",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6283acc15ff49b199d76268e7dca93be"></a>

### v16.0.2 [`00835948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835948.md) FUN_00835948

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008368f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008368f4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "008368f4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-39a13a2d0514b8e740cbef5577065a76"></a>

### v16.0.2 [`00835964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835964.md) FUN_00835964

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836910.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`008368f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/008368f4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00836910",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "008368f4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-69194481376fde74c63243d1e4fd3e3e"></a>

### v16.0.2 [`00835d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835d98.md) FUN_00835d98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d44.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 20.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00836d44",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b7076657ff7d9fded6ed71fe8bcc3aed"></a>

### v16.0.2 [`00835db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835db4.md) FUN_00835db4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d60.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00836d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836d44.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00836d60",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00836d44",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f9eae9ae309f75ebab5361376a238c08"></a>

### v16.0.2 [`00835e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e48.md) FUN_00835e48

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`007f940c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f9/007f940c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 0.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00836df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836df4.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "007f940c",
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
      "new": "00836df4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-b1e02f9e6c4dbc89c1477e2912d3304b"></a>

### v16.0.2 [`00835e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e64.md) FUN_00835e64

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00836e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836e10.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00836df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00836/00836df4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00836e10",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00836df4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-6bc1d991030b51a664908e23465bf652"></a>

### v16.0.2 [`00838aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838aec.md) FUN_00838aec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a98.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00839a98",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6eda36d016fdaeb885c8ab4c8bcf4e6b"></a>

### v16.0.2 [`00838b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b08.md) FUN_00838b08

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839ab4.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00839a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a98.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00839ab4",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00839a98",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-98ac60790e55817e68380b737fdd1156"></a>

### v16.0.2 [`00838b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b7c.md) FUN_00838b7c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b28.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00839b28",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1a0df9ee767ecb09ff53805955703e2b"></a>

### v16.0.2 [`00838b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b98.md) FUN_00838b98

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b44.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00839b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839b28.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00839b44",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00839b28",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-3ae7f536362786442de8573193cdc507"></a>

### v16.0.2 [`00838ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ce4.md) FUN_00838ce4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839c90.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00839c90",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-11d15db6c7155e1f590611d972d86b3e"></a>

### v16.0.2 [`00838d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d00.md) FUN_00838d00

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839cac.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00839c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839c90.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00839cac",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00839c90",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b9323111047c4ea2e8dbac07999ac2d4"></a>

### v16.0.2 [`00838e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e3c.md) FUN_00838e3c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`006993d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00699/006993d8.md) · スコア 60.0 · 採用条件未達 · 順位差 60.0 / 5.714286000000001 · short_function_requires_other_identity_evidence, cfg_coverage, insufficient_independent_call_anchors
- 2. [`00839de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839de8.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "cfg_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.0,
        "reverse_margin": 5.714286000000001
      },
      "new": "006993d8",
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
        "reverse_margin": 0.0
      },
      "new": "00839de8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-5be578d2e015448b30e08fd92782acbe"></a>

### v16.0.2 [`00838e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e58.md) FUN_00838e58

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00839e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839e04.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00839de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839de8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00839e04",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00839de8",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ebad72c1a043caf597b3b8dbb864ef81"></a>

### v16.0.2 [`00849d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849d2c.md) FUN_00849d2c

`competing_candidates` 

呼出元 1件 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

- 1. [`0084acd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084acd8.md) · スコア 9.63361 · 採用条件未達 · 順位差 9.63361 / 9.63361 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14606741573033707,
          0.14606741573033707
        ],
        "cfg_coverage": [
          0.043478260869565216,
          0.047619047619047616
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 9.63361,
        "reverse_margin": 9.63361
      },
      "new": "0084acd8",
      "score": 9.63361
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7425500d4e737bf79313ac307a587c0b"></a>

### v16.0.2 [`0084a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a050.md) FUN_0084a050

`competing_candidates` 

呼出元 1件 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

- 1. [`0084affc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084affc.md) · スコア 73.333333 · 採用条件未達 · 順位差 3.333332999999996 / 3.333332999999996 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0066c444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066c/0066c444.md) · スコア 70.0 · 採用条件未達 · 順位差 -3.333332999999996 / 70.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00c36f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36f10.md) · スコア 65.0 · 採用条件未達 · 順位差 -8.333332999999996 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00c36f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36f60.md) · スコア 65.0 · 採用条件未達 · 順位差 -8.333332999999996 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0084ae3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ae3c.md) · スコア 26.666667 · 採用条件未達 · 順位差 -46.66666599999999 / 26.666667 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00aa447c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa4/00aa447c.md) · スコア 13.333333 · 採用条件未達 · 順位差 -60.0 / 13.333333 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00479a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00479/00479a10.md) · スコア 10.0 · 採用条件未達 · 順位差 -63.333332999999996 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005a1e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a1/005a1e80.md) · スコア 10.0 · 採用条件未達 · 順位差 -63.333332999999996 / 10.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8888888888888888,
          0.8888888888888888
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
        "margin": 3.333332999999996,
        "reverse_margin": 3.333332999999996
      },
      "new": "0084affc",
      "score": 73.333333
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
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -3.333332999999996,
        "reverse_margin": 70.0
      },
      "new": "0066c444",
      "score": 70.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8333333333333334,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -8.333332999999996,
        "reverse_margin": 65.0
      },
      "new": "00c36f10",
      "score": 65.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f73e9551d0a08fe98aa0d94c5b3a16d5"></a>

### v16.0.2 [`0084a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) _INIT_156

`competing_candidates` 

呼出元 0件  · 呼出先 20件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md)

- 1. [`0084b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084b/0084b044.md) · スコア 19.513007 · 採用条件未達 · 順位差 13.144060000000001 / 13.144060000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aaf5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aaf/00aaf5a8.md) · スコア 6.368947 · 採用条件未達 · 順位差 -13.144060000000001 / -20.110075000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a53e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a53/00a53e94.md) · スコア 6.075251 · 採用条件未達 · 順位差 -13.437756000000002 / -19.085445 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006ab78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ab/006ab78c.md) · スコア 6.0 · 採用条件未達 · 順位差 -13.513007000000002 / -67.626741 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00b1c878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b1c/00b1c878.md) · スコア 6.0 · 採用条件未達 · 順位差 -13.513007000000002 / -36.50109 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a48f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · スコア 4.034076 · 採用条件未達 · 順位差 -15.478931000000003 / -57.046493 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006a78c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a78c8.md) · スコア 2.573837 · 採用条件未達 · 順位差 -16.93917 / 2.573837 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · スコア 2.287699 · 採用条件未達 · 順位差 -17.225308000000002 / 2.287699 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15244683576735843,
          0.15244683576735843
        ],
        "cfg_coverage": [
          0.21830985915492956,
          0.22682926829268293
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.144060000000001,
        "reverse_margin": 13.144060000000001
      },
      "new": "0084b044",
      "score": 19.513007
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.006149116064565719,
          0.018794048551292093
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.144060000000001,
        "reverse_margin": -20.110075000000002
      },
      "new": "00aaf5a8",
      "score": 6.368947
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0030745580322828594,
          0.001254180602006689
        ],
        "cfg_coverage": [
          0.0,
          0.0
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -13.437756000000002,
        "reverse_margin": -19.085445
      },
      "new": "00a53e94",
      "score": 6.075251
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2171c42f2264057377274cc6dd96e199"></a>

### v16.0.2 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) FUN_0084e5f4

`competing_candidates` 

呼出元 4件 [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) [`009ccb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md) [`00a95838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a95/00a95838.md) · 呼出先 80件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0044e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md)

- 1. [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · スコア 46.333026 · 採用条件未達 · 順位差 44.265401 / 42.333026 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`00a233d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a23/00a233d0.md) · スコア 2.067625 · 採用条件未達 · 順位差 -44.265401 / -52.617075 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · スコア 2.060582 · 採用条件未達 · 順位差 -44.27244399999999 / -51.123487999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009da92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da92c.md) · スコア 2.0 · 採用条件未達 · 順位差 -44.333026 / -80.555556 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008517dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00851/008517dc.md) · スコア 0.247593 · 採用条件未達 · 順位差 -46.085432999999995 / -48.946213 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a88b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a88/00a88b34.md) · スコア 0.082531 · 採用条件未達 · 順位差 -46.250494999999994 / -75.854979 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009d1320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d1/009d1320.md) · スコア 0.039461 · 採用条件未達 · 順位差 -46.293564999999994 / -80.25320599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00a15d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a15/00a15d8c.md) · スコア 0.010971 · 採用条件未達 · 順位差 -46.322055 / -69.781678 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5758826226501604,
          0.5758826226501604
        ],
        "cfg_coverage": [
          0.1950354609929078,
          0.18900343642611683
        ],
        "mapped_data": 2,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 44.265401,
        "reverse_margin": 42.333026
      },
      "new": "0084f5a0",
      "score": 46.333026
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0018340210912425492,
          0.0011270780501549732
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
        "margin": -44.265401,
        "reverse_margin": -52.617075
      },
      "new": "00a233d0",
      "score": 2.067625
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0022925263640531865,
          0.0010096930533117932
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
        "margin": -44.27244399999999,
        "reverse_margin": -51.123487999999995
      },
      "new": "0075ef88",
      "score": 2.060582
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7aaa21ee32628cafa8011d1e4b97a12b"></a>

### v16.0.2 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) FUN_00850830

`competing_candidates` 

呼出元 2件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 8件 [`005b9a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a38.md) [`00798e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e2c.md) [`00798e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md) [`0080c4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c4b0.md) [`0080c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080c/0080c8d0.md)

- 1. [`008517dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00851/008517dc.md) · スコア 49.193806 · 採用条件未達 · 順位差 49.077165 / 48.336663 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · スコア 0.116641 · 採用条件未達 · 順位差 -49.077165 / -31.403710999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009d1320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d1/009d1320.md) · スコア 0.039461 · 採用条件未達 · 順位差 -49.154345 / -80.25320599999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · スコア 0.0 · 採用条件未達 · 順位差 -49.193806 / -46.333026 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6928571428571428,
          0.6928571428571428
        ],
        "cfg_coverage": [
          0.3811188811188811,
          0.3978102189781022
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.077165,
        "reverse_margin": 48.336663
      },
      "new": "008517dc",
      "score": 49.193806
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.005952380952380952,
          0.0019440124416796269
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
        "margin": -49.077165,
        "reverse_margin": -31.403710999999998
      },
      "new": "00a2c310",
      "score": 0.116641
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.002380952380952381,
          0.0006576783952647156
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
        "margin": -49.154345,
        "reverse_margin": -80.25320599999999
      },
      "new": "009d1320",
      "score": 0.039461
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

