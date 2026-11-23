# v15.7.4 → v16.0.0 · 追加調査 (80)

[一覧の目次](README.md)

<a id="review-a2937400e97913603103ef3cc16dc05d"></a>

### v15.7.4 [`00a69074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69074.md) FUN_00a69074

`competing_candidates` 

呼出元 1件 [`00a67360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a67/00a67360.md) · 呼出先 13件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

- 1. [`00ac6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md) · スコア 47.080192 · 採用条件未達 · 順位差 5.277235999999995 / -4.566961000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ac7008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md) · スコア 41.802956 · 採用条件未達 · 順位差 -5.277235999999995 / 0.571429000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) · スコア 3.279737 · 採用条件未達 · 順位差 -43.800455 / -23.810672999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008c9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c9/008c9770.md) · スコア 3.206897 · 採用条件未達 · 順位差 -43.873295 / -28.806763999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a927b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a92/00a927b8.md) · スコア 2.689655 · 採用条件未達 · 順位差 -44.390536999999995 / 2.689655 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · スコア 2.409277 · 採用条件未達 · 順位差 -44.670914999999994 / -23.703805 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) · スコア 2.0 · 採用条件未達 · 順位差 -45.080192 / -40.000303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) · スコア 2.0 · 採用条件未達 · 順位差 -45.080192 / -38.335664 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6350574712643678,
          0.6350574712643678
        ],
        "cfg_coverage": [
          0.375,
          0.3488372093023256
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.277235999999995,
        "reverse_margin": -4.566961000000006
      },
      "new": "00ac6a98",
      "score": 47.080192
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5919540229885057,
          0.5919540229885057
        ],
        "cfg_coverage": [
          0.375,
          0.21428571428571427
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.277235999999995,
        "reverse_margin": 0.571429000000002
      },
      "new": "00ac7008",
      "score": 41.802956
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07471264367816093,
          0.02132895816242822
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
        "margin": -43.800455,
        "reverse_margin": -23.810672999999998
      },
      "new": "0060eb10",
      "score": 3.279737
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c15d6ac6ef1beb419dccc8c296ae0e52"></a>

### v15.7.4 [`00a699f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a699f8.md) FUN_00a699f8

`competing_candidates` 

呼出元 8件 [`0075f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f73c.md) [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`0089f1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f1c4.md) [`008cacc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cacc4.md) · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a69e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69e50.md)

- 1. [`00ac798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md) · スコア 28.064516 · 採用条件未達 · 順位差 27.123340000000002 / 27.123340000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0054c0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) · スコア 0.941176 · 採用条件未達 · 順位差 -27.123340000000002 / 0.941176 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · スコア 0.338983 · 採用条件未達 · 順位差 -27.725533000000002 / 0.338983 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) · スコア 0.272727 · 採用条件未達 · 順位差 -27.791789 / -22.136364 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008dde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md) · スコア 0.174927 · 採用条件未達 · 順位差 -27.889589 / -44.346725000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.3333333333333333
        ],
        "cfg_coverage": [
          0.4032258064516129,
          0.4166666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 27.123340000000002,
        "reverse_margin": 27.123340000000002
      },
      "new": "00ac798c",
      "score": 28.064516
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01568627450980392,
          0.05128205128205128
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
        "margin": -27.123340000000002,
        "reverse_margin": 0.941176
      },
      "new": "0054c0ac",
      "score": 0.941176
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01568627450980392,
          0.005649717514124294
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
        "margin": -27.725533000000002,
        "reverse_margin": 0.338983
      },
      "new": "00528364",
      "score": 0.338983
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-94ba5ce9e5d73fa765269417277fc685"></a>

### v15.7.4 [`00a6a2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a2d4.md) FUN_00a6a2d4

`competing_candidates` 

呼出元 6件 [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) [`008c9490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9490.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00ac8268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8268.md) · スコア 48.695652 · 採用条件未達 · 順位差 10.434782000000006 / 10.434782000000006 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`006eca88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ec/006eca88.md) · スコア 38.26087 · 採用条件未達 · 順位差 -10.434782000000006 / -15.652173000000005 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0071bbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bbec.md) · スコア 10.434783 · 採用条件未達 · 順位差 -38.260869 / -52.89855 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0071bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071bdfc.md) · スコア 8.275862 · 採用条件未達 · 順位差 -40.419790000000006 / -45.103448 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md) · スコア 7.5 · 採用条件未達 · 順位差 -41.195652 / 7.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4782608695652174,
          0.4782608695652174
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
        "margin": 10.434782000000006,
        "reverse_margin": 10.434782000000006
      },
      "new": "00ac8268",
      "score": 48.695652
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.30434782608695654,
          0.30434782608695654
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
        "margin": -10.434782000000006,
        "reverse_margin": -15.652173000000005
      },
      "new": "006eca88",
      "score": 38.26087
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.17391304347826086,
          0.2222222222222222
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
        "margin": -38.260869,
        "reverse_margin": -52.89855
      },
      "new": "0071bbec",
      "score": 10.434783
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-30c672f98817d8f677ae541671981371"></a>

### v15.7.4 [`00a6a4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4a8.md) thunk_FUN_00a6a4ac

`competing_candidates` 

呼出元 1件 [`0068c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c620.md) · 呼出先 1件 [`00a6a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md)

- 1. [`00ac843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac843c.md) · スコア 36.6813 · 採用条件未達 · 順位差 30.2557 / 36.6813 · 
- 2. [`00830af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830af0.md) · スコア 6.4256 · 採用条件未達 · 順位差 — / — · 
- 3. [`00830bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830bac.md) · スコア 5.4181 · 採用条件未達 · 順位差 — / — · 
- 4. [`0082ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccbc.md) · スコア 5.2926 · 採用条件未達 · 順位差 — / — · 
- 5. [`008d06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d06c4.md) · スコア 5.075 · 採用条件未達 · 順位差 — / — · 
- 6. [`00838cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc8.md) · スコア 4.5106 · 採用条件未達 · 順位差 — / — · 
- 7. [`008d83dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md) · スコア 4.4187 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 30.2557,
        "reverse_margin": 36.6813
      },
      "new": "00ac843c",
      "score": 36.6813
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00830af0",
      "score": 6.4256
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00830bac",
      "score": 5.4181
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-7d35ab6ed59a2a2409493f03d4fe8846"></a>

### v15.7.4 [`00a6a584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a584.md) FUN_00a6a584

`competing_candidates` [`00ac8518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8518.md)

呼出元 2件 [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) [`00895e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/00895e64.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6a4ac",
    "00a6a58c",
    "00ac8440",
    "00ac8520"
  ],
  "initial_reason": ""
}
~~~

<a id="review-f584e0f3536bcd7d893ed98938b9508c"></a>

### v15.7.4 [`00a6ac4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6ac4c.md) FUN_00a6ac4c

`competing_candidates` [`00ac8be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8be0.md)

呼出元 14件 [`0075f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f73c.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6ac1c",
    "00a6ac6c",
    "00ac8bb0",
    "00ac8c00"
  ],
  "initial_reason": ""
}
~~~

<a id="review-e6373c9381ef411fe28e5ad2fcaa93b2"></a>

### v15.7.4 [`00a6ac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6ac54.md) FUN_00a6ac54

`competing_candidates` [`00ac8be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8be8.md)

呼出元 9件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) [`00894b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894b58.md) [`00894d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894d08.md) [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6ac1c",
    "00a6ac6c",
    "00ac8bb0",
    "00ac8c00"
  ],
  "initial_reason": ""
}
~~~

<a id="review-118297306ddf846b4304fdee29b32db1"></a>

### v15.7.4 [`00a6ac5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6ac5c.md) FUN_00a6ac5c

`competing_candidates` [`00ac8bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8bf0.md)

呼出元 9件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`007f5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f5/007f5814.md) [`00894b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894b58.md) [`00894d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00894/00894d08.md) [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6ac1c",
    "00a6ac6c",
    "00ac8bb0",
    "00ac8c00"
  ],
  "initial_reason": ""
}
~~~

<a id="review-0706cb6502fea15662326211539fcc14"></a>

### v15.7.4 [`00a6ac64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6ac64.md) FUN_00a6ac64

`competing_candidates` [`00ac8bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8bf8.md)

呼出元 2件 [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`008959c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00895/008959c8.md) · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6ac1c",
    "00a6ac6c",
    "00ac8bb0",
    "00ac8c00"
  ],
  "initial_reason": ""
}
~~~

<a id="review-371f42c885dabc710d7daa4b9383e285"></a>

### v15.7.4 [`00a6b1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b1dc.md) FUN_00a6b1dc

`competing_candidates` 

呼出元 1件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) · 呼出先 2件 [`00a6d0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d0b0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

- 1. [`006c3c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3c44.md) · スコア 76.470588 · 採用条件未達 · 順位差 0.0 / 76.470588 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00788020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788020.md) · スコア 76.470588 · 採用条件未達 · 順位差 0.0 / 76.470588 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00935ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935ca0.md) · スコア 76.470588 · 採用条件未達 · 順位差 0.0 / 76.470588 · instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) · スコア 67.51634 · 採用条件未達 · 順位差 -8.954248000000007 / 67.51634 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0089777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md) · スコア 66.27451 · 採用条件未達 · 順位差 -10.196078 / 66.27451 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`007880ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007880ec.md) · スコア 64.767802 · 採用条件未達 · 順位差 -11.702786000000003 / -1.1764699999999948 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) · スコア 61.362229 · 採用条件未達 · 順位差 -15.108359000000007 / 61.362229 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005ad378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md) · スコア 57.326203 · 採用条件未達 · 順位差 -19.144385000000007 / 57.326203 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9411764705882353,
          0.9411764705882353
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
        "reverse_margin": 76.470588
      },
      "new": "006c3c44",
      "score": 76.470588
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9411764705882353,
          0.9411764705882353
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
        "reverse_margin": 76.470588
      },
      "new": "00788020",
      "score": 76.470588
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9411764705882353,
          0.9411764705882353
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
        "reverse_margin": 76.470588
      },
      "new": "00935ca0",
      "score": 76.470588
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-346c1356bc4e846b0f19040d4dc31776"></a>

### v15.7.4 [`00a6c0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c0e0.md) FUN_00a6c0e0

`competing_candidates` 

呼出元 7件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) [`00897610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897610.md) [`0089f868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f868.md) [`008cafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cafd4.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

- 1. [`00aca074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca074.md) · スコア 33.882353 · 採用条件未達 · 順位差 24.705882000000003 / 24.705882000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00861470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/00861470.md) · スコア 9.176471 · 採用条件未達 · 順位差 -24.705882000000003 / 9.176471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00511dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511dbc.md) · スコア 7.058824 · 採用条件未達 · 順位差 -26.823529 / 7.058824 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a66a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66a3c.md) · スコア 7.058824 · 採用条件未達 · 順位差 -26.823529 / -39.341176 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0090da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090da6c.md) · スコア 6.352941 · 採用条件未達 · 順位差 -27.529412 / -54.379942 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`009dcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md) · スコア 4.235294 · 採用条件未達 · 順位差 -29.647059000000002 / 4.235294 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0051ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ea80.md) · スコア 3.529412 · 採用条件未達 · 順位差 -30.352941 / 3.529412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0074b878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074b878.md) · スコア 2.941176 · 採用条件未達 · 順位差 -30.941177000000003 / 2.941176 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5647058823529412,
          0.5647058823529412
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
        "margin": 24.705882000000003,
        "reverse_margin": 24.705882000000003
      },
      "new": "00aca074",
      "score": 33.882353
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15294117647058825,
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
        "margin": -24.705882000000003,
        "reverse_margin": 9.176471
      },
      "new": "00861470",
      "score": 9.176471
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11764705882352941,
          0.4166666666666667
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
        "margin": -26.823529,
        "reverse_margin": 7.058824
      },
      "new": "00511dbc",
      "score": 7.058824
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-76b656df40ca4c9d46c24fd00b911441"></a>

### v15.7.4 [`00a6c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c818.md) FUN_00a6c818

`competing_candidates` 

呼出元 5件 [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) [`008cafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cafd4.md) [`009e1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1430.md) [`00a628e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a628e8.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

- 1. [`00aca7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md) · スコア 47.0 · 採用条件未達 · 順位差 15.384615 / -5.769230999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aca83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md) · スコア 31.615385 · 採用条件未達 · 順位差 -15.384615 / -35.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0062f7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md) · スコア 13.428571 · 採用条件未達 · 順位差 -33.571429 / -19.142858000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) · スコア 9.538462 · 採用条件未達 · 順位差 -37.461538 / 9.538462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) · スコア 8.333333 · 採用条件未達 · 順位差 -38.666667000000004 / 8.333333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008609ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00860/008609ac.md) · スコア 7.317073 · 採用条件未達 · 順位差 -39.682927 / -27.154472 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008274b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008274b4.md) · スコア 4.695652 · 採用条件未達 · 順位差 -42.304348 / -63.217391 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · スコア 2.0 · 採用条件未達 · 順位差 -45.0 / -26.145221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.25,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.384615,
        "reverse_margin": -5.769230999999998
      },
      "new": "00aca7ac",
      "score": 47.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.41025641025641024
        ],
        "cfg_coverage": [
          0.25,
          0.5
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.384615,
        "reverse_margin": -35.0
      },
      "new": "00aca83c",
      "score": 31.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.19047619047619047
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
        "margin": -33.571429,
        "reverse_margin": -19.142858000000004
      },
      "new": "0062f7a4",
      "score": 13.428571
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-343dcb6c6799c8797b5ebc192a0c911d"></a>

### v15.7.4 [`00a6c8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c8a8.md) FUN_00a6c8a8

`competing_candidates` 

呼出元 2件 [`007fa718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fa718.md) [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

- 1. [`00aca83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md) · スコア 66.615385 · 採用条件未達 · 順位差 13.846154000000006 / 34.307693 · instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aca7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md) · スコア 52.769231 · 採用条件未達 · 順位差 -13.846154000000006 / 5.769230999999998 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0058b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b0f0.md) · スコア 32.307692 · 採用条件未達 · 順位差 -34.307693 / 32.307692 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008609ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00860/008609ac.md) · スコア 31.707317 · 採用条件未達 · 順位差 -34.908068 / -2.7642279999999992 · instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0062f7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md) · スコア 9.619048 · 採用条件未達 · 順位差 -56.996337000000004 / -22.952381000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) · スコア 9.538462 · 採用条件未達 · 順位差 -57.076923 / 9.538462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008274b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008274b4.md) · スコア 4.695652 · 採用条件未達 · 順位差 -61.919733 / -63.217391 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · スコア 2.0 · 採用条件未達 · 順位差 -64.615385 / -26.145221 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          1.0,
          1.0
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.846154000000006,
        "reverse_margin": 34.307693
      },
      "new": "00aca83c",
      "score": 66.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5128205128205128,
          0.5555555555555556
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
        "margin": -13.846154000000006,
        "reverse_margin": 5.769230999999998
      },
      "new": "00aca7ac",
      "score": 52.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.20512820512820512,
          0.25
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
        "margin": -34.307693,
        "reverse_margin": 32.307692
      },
      "new": "0058b0f0",
      "score": 32.307692
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e323d57b5680be700bbb3b54e8ec66ac"></a>

### v15.7.4 [`00a6c944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c944.md) FUN_00a6c944

`competing_candidates` 

呼出元 8件 [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`0089dc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089dc0c.md) [`008ca974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008ca974.md) · 呼出先 3件 [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

- 1. [`00aca8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca8d8.md) · スコア 57.0 · 採用条件未達 · 順位差 11.6875 / 15.375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) · スコア 45.3125 · 採用条件未達 · 順位差 -11.6875 / -7.146515999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00acaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaacc.md) · スコア 27.375 · 採用条件未達 · 順位差 -29.625 / 27.375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) · スコア 25.625 · 採用条件未達 · 順位差 -31.375 / 25.625 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) · スコア 21.636905 · 採用条件未達 · 順位差 -35.363095 / 21.636905 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md) · スコア 19.463918 · 採用条件未達 · 順位差 -37.536082 / 19.463918 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00ac8a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md) · スコア 17.1875 · 採用条件未達 · 順位差 -39.8125 / 17.1875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`004a8d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md) · スコア 15.9375 · 採用条件未達 · 順位差 -41.0625 / 15.9375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

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
          0.6,
          0.75
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 11.6875,
        "reverse_margin": 15.375
      },
      "new": "00aca8d8",
      "score": 57.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.671875,
          0.7049180327868853
        ],
        "cfg_coverage": [
          0.25,
          0.3125
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -11.6875,
        "reverse_margin": -7.146515999999998
      },
      "new": "00aca9d8",
      "score": 45.3125
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.40625,
          0.45614035087719296
        ],
        "cfg_coverage": [
          0.15,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -29.625,
        "reverse_margin": 27.375
      },
      "new": "00acaacc",
      "score": 27.375
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-883055ceecef0d795b0e542e33db1c2b"></a>

### v15.7.4 [`00a6ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ca44.md) FUN_00a6ca44

`competing_candidates` 

呼出元 18件 [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) [`00761ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761ab0.md) [`00763a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763a24.md) [`00764190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764190.md) [`00764408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00764/00764408.md) · 呼出先 4件 [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a6b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

- 1. [`00aca8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca8d8.md) · スコア 41.625 · 採用条件未達 · 順位差 1.2315570000000022 / -15.375 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) · スコア 40.393443 · 採用条件未達 · 順位差 -1.2315570000000022 / -12.065573 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00acaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaacc.md) · スコア 28.57377 · 採用条件未達 · 順位差 -13.05123 / 28.57377 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`008b9660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md) · スコア 24.639344 · 採用条件未達 · 順位差 -16.985656 / 24.639344 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`008b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md) · スコア 17.426804 · 採用条件未達 · 順位差 -24.198196 / 17.426804 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00ac894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md) · スコア 16.913043 · 採用条件未達 · 順位差 -24.711957 / 16.913043 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) · スコア 15.644028 · 採用条件未達 · 順位差 -25.980972 / 15.644028 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) · スコア 10.559701 · 採用条件未達 · 順位差 -31.065299 / 10.559701 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6229508196721312,
          0.59375
        ],
        "cfg_coverage": [
          0.3,
          0.375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 1.2315570000000022,
        "reverse_margin": -15.375
      },
      "new": "00aca8d8",
      "score": 41.625
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6065573770491803,
          0.6065573770491803
        ],
        "cfg_coverage": [
          0.2,
          0.25
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.2315570000000022,
        "reverse_margin": -12.065573
      },
      "new": "00aca9d8",
      "score": 40.393443
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4262295081967213,
          0.45614035087719296
        ],
        "cfg_coverage": [
          0.15,
          0.1875
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.05123,
        "reverse_margin": 28.57377
      },
      "new": "00acaacc",
      "score": 28.57377
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-13d65b2c43e744fa9782a47a81d5df47"></a>

### v15.7.4 [`00a6cc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6cc1c.md) FUN_00a6cc1c

`competing_candidates` 

呼出元 19件 [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) [`00714cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00714/00714cf0.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) · 呼出先 5件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00acabb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md) · スコア 25.846154 · 採用条件未達 · 順位差 25.846154 / 25.846154 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00646040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / -50.826162 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / -38.787879 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006acf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acf1c.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / -37.030648 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006e9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / -42.338624 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008f30c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f30c4.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / -25.333333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) · スコア 0.0 · 採用条件未達 · 順位差 -25.846154 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4307692307692308,
          0.4307692307692308
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
          "insufficient_independent_call_anchors"
        ],
        "margin": 25.846154,
        "reverse_margin": 25.846154
      },
      "new": "00acabb0",
      "score": 25.846154
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
        "margin": -25.846154,
        "reverse_margin": -50.826162
      },
      "new": "00646040",
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
        "margin": -25.846154,
        "reverse_margin": -38.787879
      },
      "new": "00697f94",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2dbac617b3ad6ac62262a1f078175b22"></a>

### v15.7.4 [`00a6d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d080.md) FUN_00a6d080

`competing_candidates` [`00acb014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb014.md)

呼出元 0件  · 呼出先 0件 


~~~json
{
  "bounds": [
    "00a6d07c",
    "00a6d0b0",
    "00acb010",
    "00acb044"
  ],
  "initial_reason": ""
}
~~~

<a id="review-81a73e3fc54a94284048819e1494d868"></a>

### v15.7.4 [`00a6d088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d088.md) FUN_00a6d088

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb01c.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00acb01c",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-1ac2cc366153b2b2cc372d96bba16458"></a>

### v15.7.4 [`00a6d0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d0a4.md) FUN_00a6d0a4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb038.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00acb01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb01c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00acb038",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00acb01c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1e0eae20c6a678128231c3dfdaeca66f"></a>

### v15.7.4 [`00a6d258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d258.md) FUN_00a6d258

`competing_candidates` 

呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)

- 1. [`00acb1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md) · スコア 44.761905 · 採用条件未達 · 順位差 8.095238000000002 / -7.619047000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00636760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636760.md) · スコア 36.666667 · 採用条件未達 · 順位差 -8.095238000000002 / 5.333333999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00655840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655840.md) · スコア 30.0 · 採用条件未達 · 順位差 -14.761904999999999 / -9.167718 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00630c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c1c.md) · スコア 29.017544 · 採用条件未達 · 順位差 -15.744360999999998 / 2.701755000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006973cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006973cc.md) · スコア 26.666667 · 採用条件未達 · 順位差 -18.095238 / 26.666667 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00a01064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a01/00a01064.md) · スコア 26.666667 · 採用条件未達 · 順位差 -18.095238 / -41.333332999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a02568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02568.md) · スコア 26.666667 · 採用条件未達 · 順位差 -18.095238 / -41.333332999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00698f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698f18.md) · スコア 23.809524 · 採用条件未達 · 順位差 -20.952381 / 23.809524 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5555555555555556,
          0.5555555555555556
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
        "margin": 8.095238000000002,
        "reverse_margin": -7.619047000000002
      },
      "new": "00acb1ec",
      "score": 44.761905
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4444444444444444,
          0.4666666666666667
        ],
        "cfg_coverage": [
          0.5,
          0.5384615384615384
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.095238000000002,
        "reverse_margin": 5.333333999999997
      },
      "new": "00636760",
      "score": 36.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3333333333333333,
          0.3442622950819672
        ],
        "cfg_coverage": [
          0.5,
          0.5833333333333334
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -14.761904999999999,
        "reverse_margin": -9.167718
      },
      "new": "00655840",
      "score": 30.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-77cab1698852b70c4b1e390a5039a11f"></a>

### v15.7.4 [`00a6d354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d354.md) FUN_00a6d354

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb2e8.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / -25.714286 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00acb2e8",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-32474862f56acffeea371eebc6bcc9f7"></a>

### v15.7.4 [`00a6d370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d370.md) FUN_00a6d370

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb304.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00acb2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb2e8.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00acb1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md) · スコア 0.1905 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00acb304",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00acb2e8",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00acb1ec",
      "score": 0.1905
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-238241da8d0bbecbacc5825ad04219b9"></a>

### v15.7.4 [`00a6d3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d3bc.md) FUN_00a6d3bc

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a2e4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

- 1. [`00acb350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md) · スコア 33.71517 · 採用条件未達 · 順位差 13.640867 / 11.009288000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0065e1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e1bc.md) · スコア 20.074303 · 採用条件未達 · 順位差 -13.640867 / 20.074303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0065eec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eec4.md) · スコア 20.074303 · 採用条件未達 · 順位差 -13.640867 / 20.074303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00831ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00831/00831ea4.md) · スコア 20.074303 · 採用条件未達 · 順位差 -13.640867 / 20.074303 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a9b028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b028.md) · スコア 20.074303 · 採用条件未達 · 順位差 -13.640867 / -46.211411 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00a9b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b130.md) · スコア 20.074303 · 採用条件未達 · 順位差 -13.640867 / -46.377309999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006d997c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md) · スコア 9.176471 · 採用条件未達 · 順位差 -24.538699 / 9.176471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`006d9844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md) · スコア 6.352941 · 採用条件未達 · 順位差 -27.362229 / 6.352941 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38823529411764707,
          0.38823529411764707
        ],
        "cfg_coverage": [
          0.42105263157894735,
          0.5714285714285714
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 13.640867,
        "reverse_margin": 11.009288000000002
      },
      "new": "00acb350",
      "score": 33.71517
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21176470588235294,
          0.5454545454545454
        ],
        "cfg_coverage": [
          0.3684210526315789,
          0.7
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.640867,
        "reverse_margin": 20.074303
      },
      "new": "0065e1bc",
      "score": 20.074303
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.21176470588235294,
          0.5454545454545454
        ],
        "cfg_coverage": [
          0.3684210526315789,
          0.7
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.640867,
        "reverse_margin": 20.074303
      },
      "new": "0065eec4",
      "score": 20.074303
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c02d26346b9f7a513480b4468af579c3"></a>

### v15.7.4 [`00a6d510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d510.md) FUN_00a6d510

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4a4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00acb4a4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0cd87a5ebbcc41cc8742324cf500cfea"></a>

### v15.7.4 [`00a6d52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d52c.md) FUN_00a6d52c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acb4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4c0.md) · スコア 84.0 · 採用条件未達 · 順位差 82.2857 / 82.2857 · 
- 2. [`00acb4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4a4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00acb350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md) · スコア 0.1412 · 採用条件未達 · 順位差 — / — · 

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
      "new": "00acb4c0",
      "score": 84.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00acb4a4",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00acb350",
      "score": 0.1412
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f82efd07634996ace49475544f1928d9"></a>

### v15.7.4 [`00a6dec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dec4.md) FUN_00a6dec4

`competing_candidates` 

呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00acbe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe58.md) · スコア 66.666667 · 採用条件未達 · 順位差 11.666667000000004 / 66.666667 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 55.0 · 採用条件未達 · 順位差 -11.666667000000004 / -5.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7777777777777778,
          0.7777777777777778
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
        "margin": 11.666667000000004,
        "reverse_margin": 66.666667
      },
      "new": "00acbe58",
      "score": 66.666667
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7777777777777778,
          0.5833333333333334
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
        "margin": -11.666667000000004,
        "reverse_margin": -5.0
      },
      "new": "0043bd58",
      "score": 55.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3b0333cbe9976e67238a6e591a2c948d"></a>

### v15.7.4 [`00a6df20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6df20.md) FUN_00a6df20

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00acbeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbeb4.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors

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
      "new": "00acbeb4",
      "score": 54.285714
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-52857521a79bebd364a5e98ac8d7e21b"></a>

### v15.7.4 [`00a6e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6e/00a6e440.md) FUN_00a6e440

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

- 1. [`00acc3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc3d4.md) · スコア 25.856139 · 採用条件未達 · 順位差 17.559243 / 17.256087 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) · スコア 8.296896 · 採用条件未達 · 順位差 -17.559243 / -13.423953000000001 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · スコア 6.208636 · 採用条件未達 · 順位差 -19.647503 / -24.976066000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00908178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00908/00908178.md) · スコア 6.107962 · 採用条件未達 · 順位差 -19.748177 / 0.10796199999999967 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) · スコア 6.025873 · 採用条件未達 · 順位差 -19.830265999999998 / -19.587825 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00912918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00912/00912918.md) · スコア 4.461304 · 採用条件未達 · 順位差 -21.394835 / -18.048529000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`006f0614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md) · スコア 4.269906 · 採用条件未達 · 順位差 -21.586233 / 4.269906 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00668db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md) · スコア 4.188934 · 採用条件未達 · 順位差 -21.667205 / 4.188934 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2676563202878992,
          0.2676563202878992
        ],
        "cfg_coverage": [
          0.0898379970544919,
          0.09186746987951808
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.559243,
        "reverse_margin": 17.256087
      },
      "new": "00acc3d4",
      "score": 25.856139
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.004948268106162843,
          0.005780346820809248
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
        "margin": -17.559243,
        "reverse_margin": -13.423953000000001
      },
      "new": "006b01f8",
      "score": 8.296896
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.003148897885739991,
          0.0029863481228668944
        ],
        "cfg_coverage": [
          0.0014727540500736377,
          0.0016806722689075631
        ],
        "mapped_data": 3,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -19.647503,
        "reverse_margin": -24.976066000000003
      },
      "new": "00a73338",
      "score": 6.208636
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e69e597af54bcd2f68c956fae599ba1b"></a>

### v15.7.4 [`00a709cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a709cc.md) FUN_00a709cc

`competing_candidates` 

呼出元 16件 [`005bc594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc594.md) [`005bc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc910.md) [`005bca40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bca40.md) [`0063c0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c178.md) · 呼出先 11件 [`0065042c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/0065042c.md) [`0078b018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078b/0078b018.md) [`007cd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd120.md) [`007cf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf4b0.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md)

- 1. [`00ace960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md) · スコア 33.903226 · 採用条件未達 · 順位差 30.032257999999995 / 30.032257999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007ef2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md) · スコア 3.870968 · 採用条件未達 · 順位差 -30.032257999999995 / -21.933228 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.903226 / -21.315789 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007efb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.903226 / -43.134921 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.903226 / -59.71831 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md) · スコア 0.0 · 採用条件未達 · 順位差 -33.903226 / 0.0 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5483870967741935,
          0.5483870967741935
        ],
        "cfg_coverage": [
          0.05,
          0.0625
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.032257999999995,
        "reverse_margin": 30.032257999999995
      },
      "new": "00ace960",
      "score": 33.903226
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06451612903225806,
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
        "margin": -30.032257999999995,
        "reverse_margin": -21.933228
      },
      "new": "007ef2e0",
      "score": 3.870968
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
        "margin": -33.903226,
        "reverse_margin": -21.315789
      },
      "new": "005e15e0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-77180844f801a9dc1f5a5a4c4e89c530"></a>

### v15.7.4 [`00a71364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71364.md) FUN_00a71364

`competing_candidates` 

呼出元 3件 [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) [`00a6e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6e/00a6e440.md) [`00a81ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81ea4.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md) [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md) [`00a251d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a251d8.md)

- 1. [`00acf2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf2f8.md) · スコア 18.03681 · 採用条件未達 · 順位差 10.53681 / 13.619632 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00767f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767f54.md) · スコア 7.5 · 採用条件未達 · 順位差 -10.53681 / -24.751235 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) · スコア 6.666667 · 採用条件未達 · 順位差 -11.370142999999999 / -28.700028 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00768564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768564.md) · スコア 6.666667 · 採用条件未達 · 順位差 -11.370142999999999 / -22.329734 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0058e8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md) · スコア 5.833333 · 採用条件未達 · 順位差 -12.203477 / 5.833333 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008ad760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad760.md) · スコア 5.177665 · 採用条件未達 · 順位差 -12.859144999999998 / 5.177665 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0078fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md) · スコア 4.785276 · 採用条件未達 · 順位差 -13.251534 / 4.785276 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0074f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074f69c.md) · スコア 4.290541 · 採用条件未達 · 順位差 -13.746268999999998 / -55.841038000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3402777777777778,
          0.3006134969325153
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
        "margin": 10.53681,
        "reverse_margin": 13.619632
      },
      "new": "00acf2f8",
      "score": 18.03681
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.125,
          0.1651376146788991
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
        "margin": -10.53681,
        "reverse_margin": -24.751235
      },
      "new": "00767f54",
      "score": 7.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1111111111111111,
          0.1322314049586777
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
        "margin": -11.370142999999999,
        "reverse_margin": -28.700028
      },
      "new": "00764ea0",
      "score": 6.666667
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e1b54b51176cb0e4b9551ae0675157d0"></a>

### v15.7.4 [`00a71618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71618.md) FUN_00a71618

`competing_candidates` 

呼出元 4件 [`00a6e440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6e/00a6e440.md) [`00a81ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81ea4.md) [`00a8d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1bc.md) [`00a8f86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f86c.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

- 1. [`00acf5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf5fc.md) · スコア 21.67435 · 採用条件未達 · 順位差 9.841046 / 12.458023 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0091a884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a884.md) · スコア 11.833304 · 採用条件未達 · 順位差 -9.841046 / -26.638457000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00582320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md) · スコア 6.47482 · 採用条件未達 · 順位差 -15.19953 / 6.47482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md) · スコア 6.47482 · 採用条件未達 · 順位差 -15.19953 / 6.47482 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a65868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md) · スコア 6.316547 · 採用条件未達 · 順位差 -15.357803 / 6.316547 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00694ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ad4.md) · スコア 5.179856 · 採用条件未達 · 順位差 -16.494494 / -32.25153 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) · スコア 4.748201 · 採用条件未達 · 順位差 -16.926149000000002 / 4.748201 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0062bd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bd9c.md) · スコア 4.748201 · 採用条件未達 · 順位差 -16.926149000000002 / -32.822548999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.28776978417266186,
          0.28776978417266186
        ],
        "cfg_coverage": [
          0.024390243902439025,
          0.02040816326530612
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 9.841046,
        "reverse_margin": 12.458023
      },
      "new": "00acf5fc",
      "score": 21.67435
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11510791366906475,
          0.18604651162790697
        ],
        "cfg_coverage": [
          0.14634146341463414,
          0.17142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.841046,
        "reverse_margin": -26.638457000000002
      },
      "new": "0091a884",
      "score": 11.833304
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1079136690647482,
          0.17647058823529413
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
        "margin": -15.19953,
        "reverse_margin": 6.47482
      },
      "new": "00582320",
      "score": 6.47482
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-f07bd331ab20c9be5c4f4cdc1e88365a"></a>

### v15.7.4 [`00a71924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71924.md) FUN_00a71924

`competing_candidates` 

呼出元 1件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

- 1. [`009a11e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a11e0.md) · スコア 41.65368 · 採用条件未達 · 順位差 1.0909090000000035 / 41.65368 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00acf908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf908.md) · スコア 40.562771 · 採用条件未達 · 順位差 -1.0909090000000035 / -22.225108 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00996dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996dc4.md) · スコア 36.952381 · 採用条件未達 · 順位差 -4.701298999999999 / 36.952381 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0098cd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cd38.md) · スコア 5.454545 · 採用条件未達 · 順位差 -36.199135 / -72.476489 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6545454545454545,
          0.6545454545454545
        ],
        "cfg_coverage": [
          0.11904761904761904,
          0.15151515151515152
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": 1.0909090000000035,
        "reverse_margin": 41.65368
      },
      "new": "009a11e0",
      "score": 41.65368
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6363636363636364,
          0.6363636363636364
        ],
        "cfg_coverage": [
          0.11904761904761904,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -1.0909090000000035,
        "reverse_margin": -22.225108
      },
      "new": "00acf908",
      "score": 40.562771
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6,
          0.6
        ],
        "cfg_coverage": [
          0.047619047619047616,
          0.06060606060606061
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -4.701298999999999,
        "reverse_margin": 36.952381
      },
      "new": "00996dc4",
      "score": 36.952381
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-29a7e056bdee01588b15003686fde9e5"></a>

### v15.7.4 [`00a71ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71ae0.md) FUN_00a71ae0

`competing_candidates` 

呼出元 3件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a8d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1bc.md) · 呼出先 14件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`00640910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md) [`0066f824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f824.md)

- 1. [`00acfac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md) · スコア 22.801201 · 採用条件未達 · 順位差 19.162045 / 19.952672 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · スコア 3.639156 · 採用条件未達 · 順位差 -19.162045 / 3.639156 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`008b806c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b8/008b806c.md) · スコア 2.911392 · 採用条件未達 · 順位差 -19.889809 / 2.911392 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00753834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753834.md) · スコア 2.630252 · 採用条件未達 · 順位差 -20.170949 / -14.866704999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) · スコア 2.606061 · 採用条件未達 · 順位差 -20.19514 / -30.330412 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`005c0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0e4c.md) · スコア 2.582278 · 採用条件未達 · 順位差 -20.218923 / 2.582278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007c970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md) · スコア 2.342205 · 採用条件未達 · 順位差 -20.458996 / -38.818463 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) · スコア 2.303797 · 採用条件未達 · 順位差 -20.497404 / -21.650226 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3367088607594937,
          0.3114754098360656
        ],
        "cfg_coverage": [
          0.1171875,
          0.1056338028169014
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 19.162045,
        "reverse_margin": 19.952672
      },
      "new": "00acfac4",
      "score": 22.801201
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05063291139240506,
          0.0477326968973747
        ],
        "cfg_coverage": [
          0.0390625,
          0.03875968992248062
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -19.162045,
        "reverse_margin": 3.639156
      },
      "new": "00887898",
      "score": 3.639156
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.015189873417721518,
          0.04285714285714286
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
        "margin": -19.889809,
        "reverse_margin": 2.911392
      },
      "new": "008b806c",
      "score": 2.911392
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-933b44253f995156ebff100bb8673e37"></a>

### v15.7.4 [`00a72140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a72140.md) FUN_00a72140

`competing_candidates` 

呼出元 2件 [`00a8e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e58c.md) [`00a91e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a91e58.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md)

- 1. [`00ad0210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md) · スコア 22.652527 · 採用条件未達 · 順位差 5.693429999999999 / -5.696896000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ad04dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md) · スコア 16.959097 · 採用条件未達 · 順位差 -5.693429999999999 / -22.073161 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00798020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md) · スコア 9.075885 · 採用条件未達 · 順位差 -13.576642 / 9.075885 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009b4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md) · スコア 7.883212 · 採用条件未達 · 順位差 -14.769314999999999 / 7.883212 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007f2a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md) · スコア 7.822614 · 採用条件未達 · 順位差 -14.829913 / -37.287723 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) · スコア 7.762016 · 採用条件未達 · 順位差 -14.890511 / 7.762016 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00746674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746674.md) · スコア 6.569343 · 採用条件未達 · 順位差 -16.083184 / 6.569343 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009e50c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e5/009e50c4.md) · スコア 5.33805 · 採用条件未達 · 順位差 -17.314477 / -8.039143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.36496350364963503,
          0.36496350364963503
        ],
        "cfg_coverage": [
          0.03773584905660377,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 5.693429999999999,
        "reverse_margin": -5.696896000000002
      },
      "new": "00ad0210",
      "score": 22.652527
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.27007299270072993,
          0.3135593220338983
        ],
        "cfg_coverage": [
          0.03773584905660377,
          0.06666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -5.693429999999999,
        "reverse_margin": -22.073161
      },
      "new": "00ad04dc",
      "score": 16.959097
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1386861313868613,
          0.2345679012345679
        ],
        "cfg_coverage": [
          0.03773584905660377,
          0.1
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.576642,
        "reverse_margin": 9.075885
      },
      "new": "00798020",
      "score": 9.075885
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-38587d50a1317a5d004258f2479fabe1"></a>

### v15.7.4 [`00a7240c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7240c.md) FUN_00a7240c

`competing_candidates` 

呼出元 1件 [`00a8e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e58c.md) · 呼出先 9件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md) [`00887e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/00887e18.md)

- 1. [`00ad04dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md) · スコア 39.032258 · 採用条件未達 · 順位差 10.682834999999997 / 17.936213 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ad0210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md) · スコア 28.349423 · 採用条件未達 · 順位差 -10.682834999999997 / 5.696896000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) · スコア 20.924002 · 採用条件未達 · 順位差 -18.108255999999997 / 20.924002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`007add18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md) · スコア 15.429196 · 採用条件未達 · 順位差 -23.603062 / -10.911545000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0087a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md) · スコア 12.951147 · 採用条件未達 · 順位差 -26.081111 / -6.656695999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0087b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md) · スコア 11.204282 · 採用条件未達 · 順位差 -27.827976 / -8.093964 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0097d12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d12c.md) · スコア 9.714541 · 採用条件未達 · 順位差 -29.317717 / 9.714541 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) · スコア 9.699046 · 採用条件未達 · 順位差 -29.333212 / -31.989234 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.45161290322580644,
          0.4666666666666667
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 10.682834999999997,
        "reverse_margin": 17.936213
      },
      "new": "00ad04dc",
      "score": 39.032258
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.423728813559322,
          0.36496350364963503
        ],
        "cfg_coverage": [
          0.3225806451612903,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -10.682834999999997,
        "reverse_margin": 5.696896000000002
      },
      "new": "00ad0210",
      "score": 28.349423
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2627118644067797,
          0.2672413793103448
        ],
        "cfg_coverage": [
          0.25806451612903225,
          0.25806451612903225
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -18.108255999999997,
        "reverse_margin": 20.924002
      },
      "new": "00891b28",
      "score": 20.924002
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-dc9edd035cfdfb059cb3091577c7a04c"></a>

### v15.7.4 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) FUN_00a7268c

`competing_candidates` 

呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 94件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

- 1. [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · スコア 14.530189 · 採用条件未達 · 順位差 8.497123 / 9.275843 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) · スコア 6.033066 · 採用条件未達 · 順位差 -8.497123 / -20.704385000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · スコア 4.885576 · 採用条件未達 · 順位差 -9.644613 / -24.692934 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · スコア 4.377518 · 採用条件未達 · 順位差 -10.152671 / -29.570513999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · スコア 4.368873 · 採用条件未達 · 順位差 -10.161316 / -24.071471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · スコア 4.269085 · 採用条件未達 · 順位差 -10.261104 / -26.312965 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`008bdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bd/008bdabc.md) · スコア 4.141199 · 採用条件未達 · 順位差 -10.38899 / 4.141199 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · スコア 4.1153 · 採用条件未達 · 順位差 -10.414888999999999 / -5.703542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15842458495231368,
          0.15328092959671907
        ],
        "cfg_coverage": [
          0.06666666666666667,
          0.06990434142752024
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 8.497123,
        "reverse_margin": 9.275843
      },
      "new": "00ad075c",
      "score": 14.530189
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.039032144118685975,
          0.03022842292436055
        ],
        "cfg_coverage": [
          0.016140350877192983,
          0.010968049594659036
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -8.497123,
        "reverse_margin": -20.704385000000002
      },
      "new": "0098527c",
      "score": 6.033066
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.012186506534793359,
          0.013967611336032389
        ],
        "cfg_coverage": [
          0.0077192982456140355,
          0.007947976878612716
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -9.644613,
        "reverse_margin": -24.692934
      },
      "new": "0075eb40",
      "score": 4.885576
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-cbcc937b025d7e20c9643f6626d325c9"></a>

### v15.7.4 [`00a7840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a7840c.md) FUN_00a7840c

`competing_candidates` 

呼出元 6件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a81ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81ea4.md) [`00a8d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1bc.md) [`00a908b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) [`005f00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f00b0.md) [`0065042c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/0065042c.md) [`00719c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719c4c.md)

- 1. [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) · スコア 41.521127 · 採用条件未達 · 順位差 29.359858 / 33.364581 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0097d45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md) · スコア 12.161269 · 採用条件未達 · 順位差 -29.359858 / -40.854774000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md) · スコア 9.698254 · 採用条件未達 · 順位差 -31.822873 / 9.698254 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md) · スコア 8.911369 · 採用条件未達 · 順位差 -32.609758 / 8.911369 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0081db0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081db0c.md) · スコア 6.883913 · 採用条件未達 · 順位差 -34.637214 / 0.5160819999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00806de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806de8.md) · スコア 6.062908 · 採用条件未達 · 順位差 -35.458219 / -30.800728 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`005db1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db1c8.md) · スコア 4.719979 · 採用条件未達 · 順位差 -36.801148 / -27.091068 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0072bf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bf0c.md) · スコア 4.685859 · 採用条件未達 · 順位差 -36.835268 / -45.669363 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.2032520325203252,
          0.176056338028169
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 29.359858,
        "reverse_margin": 33.364581
      },
      "new": "00ad688c",
      "score": 41.521127
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16393442622950818,
          0.36764705882352944
        ],
        "cfg_coverage": [
          0.016260162601626018,
          0.045454545454545456
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -29.359858,
        "reverse_margin": -40.854774000000006
      },
      "new": "0097d45c",
      "score": 12.161269
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11475409836065574,
          0.21875
        ],
        "cfg_coverage": [
          0.04065040650406504,
          0.0684931506849315
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -31.822873,
        "reverse_margin": 9.698254
      },
      "new": "005c04b0",
      "score": 9.698254
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-243929ae0822ebfd534d3c8aedb97d82"></a>

### v15.7.4 [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) FUN_00a788d0

`competing_candidates` 

呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 139件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

- 1. [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · スコア 33.948032 · 採用条件未達 · 順位差 21.606015 / 21.586053999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · スコア 12.342017 · 採用条件未達 · 順位差 -21.606015 / -8.033691 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · スコア 11.019114 · 採用条件未達 · 順位差 -22.928917999999996 / -28.968241999999996 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · スコア 10.148747 · 採用条件未達 · 順位差 -23.799284999999998 / -48.112662 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · スコア 8.473 · 採用条件未達 · 順位差 -25.475032 / -33.55191 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · スコア 8.171131 · 採用条件未達 · 順位差 -25.776900999999995 / -40.915606999999994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · スコア 8.149565 · 採用条件未達 · 順位差 -25.798466999999995 / -15.836108999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · スコア 8.095366 · 採用条件未達 · 順位差 -25.852666 / -39.807033000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.33585594989561585,
          0.3239773442416614
        ],
        "cfg_coverage": [
          0.14440121054907046,
          0.12546957175056347
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 21.606015,
        "reverse_margin": 21.586053999999997
      },
      "new": "00ad6d50",
      "score": 33.948032
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01069937369519833,
          0.0056226001097092705
        ],
        "cfg_coverage": [
          0.00043233895373973193,
          0.00023304591004427873
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -21.606015,
        "reverse_margin": -8.033691
      },
      "new": "007cceac",
      "score": 12.342017
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.01865866388308977,
          0.01648605026516025
        ],
        "cfg_coverage": [
          0.0017293558149589277,
          0.001497566454511419
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -22.928917999999996,
        "reverse_margin": -28.968241999999996
      },
      "new": "0098da6c",
      "score": 11.019114
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-118ea8dc5b3d6e43b0f7bf3fdf29ee76"></a>

### v15.7.4 [`00a80570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a80570.md) FUN_00a80570

`competing_candidates` 

呼出元 3件 [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b06c.md) · 呼出先 9件 [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) [`00719c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719c4c.md) [`00719de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719de8.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md) [`009e4f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md)

- 1. [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) · スコア 45.57398 · 採用条件未達 · 順位差 36.364796 / 36.324473999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00493ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ca8.md) · スコア 9.209184 · 採用条件未達 · 順位差 -36.364796 / 9.209184 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0081a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a450.md) · スコア 8.571429 · 採用条件未達 · 順位差 -37.002551 / -40.074404 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006d5ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d5/006d5ac4.md) · スコア 5.535714 · 採用条件未達 · 順位差 -40.038266 / 5.535714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b3f2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f2fc.md) · スコア 5.535714 · 採用条件未達 · 順位差 -40.038266 / 5.535714 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006fefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md) · スコア 2.44898 · 採用条件未達 · 順位差 -43.125 / 2.44898 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00c38854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) · スコア 2.44898 · 採用条件未達 · 順位差 -43.125 / 2.44898 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`008b92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b92a8.md) · スコア 1.804511 · 採用条件未達 · 順位差 -43.769469 / 1.804511 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5408163265306123,
          0.5408163265306123
        ],
        "cfg_coverage": [
          0.65625,
          0.6774193548387096
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.364796,
        "reverse_margin": 36.324473999999995
      },
      "new": "00adee94",
      "score": 45.57398
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1326530612244898,
          0.23214285714285715
        ],
        "cfg_coverage": [
          0.0625,
          0.16666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -36.364796,
        "reverse_margin": 9.209184
      },
      "new": "00493ca8",
      "score": 9.209184
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.21875
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
        "margin": -37.002551,
        "reverse_margin": -40.074404
      },
      "new": "0081a450",
      "score": 8.571429
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3b08f58adb97c0e72420584f5d1b82ab"></a>

### v15.7.4 [`00a806f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a806f8.md) FUN_00a806f8

`competing_candidates` 

呼出元 3件 [`007c77c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c7/007c77c8.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

- 1. [`00adf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00adf/00adf01c.md) · スコア 5.181507 · 採用条件未達 · 順位差 2.353281 / 0.7815069999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) · スコア 2.828226 · 採用条件未達 · 順位差 -2.353281 / -30.08292 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00641fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md) · スコア 0.410959 · 採用条件未達 · 順位差 -4.770548 / 0.410959 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · スコア 0.256849 · 採用条件未達 · 順位差 -4.924658 / -29.890510000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · スコア 0.256849 · 採用条件未達 · 順位差 -4.924658 / -43.538163999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00aad4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aad4a0.md) · スコア 0.256849 · 採用条件未達 · 順位差 -4.924658 / 0.256849 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) · スコア 0.205479 · 採用条件未達 · 順位差 -4.9760279999999995 / 0.205479 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007548d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00754/007548d0.md) · スコア 0.205479 · 採用条件未達 · 順位差 -4.9760279999999995 / 0.205479 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.019691780821917807,
          0.020517395182872437
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
        "margin": 2.353281,
        "reverse_margin": 0.7815069999999995
      },
      "new": "00adf01c",
      "score": 5.181507
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.009417808219178082,
          0.010617760617760617
        ],
        "cfg_coverage": [
          0.013157894736842105,
          0.013157894736842105
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -2.353281,
        "reverse_margin": -30.08292
      },
      "new": "006e5d30",
      "score": 2.828226
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.00684931506849315,
          0.0121765601217656
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
        "margin": -4.770548,
        "reverse_margin": 0.410959
      },
      "new": "00641fd0",
      "score": 0.410959
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-05638be81345ab21db9def5481ea06d7"></a>

### v15.7.4 [`00a81b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81b6c.md) FUN_00a81b6c

`competing_candidates` 

呼出元 2件 [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a8df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df4c.md) · 呼出先 0件 

- 1. [`00ae0408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0408.md) · スコア 60.550162 · 採用条件未達 · 順位差 60.550162 / 60.550162 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -31.555024 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006559b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006559b0.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -30.57737 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0065f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -19.347612 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065f778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -18.509144 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -16.8 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00744238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744238.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -18.715278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) · スコア 0.0 · 採用条件未達 · 順位差 -60.550162 / -34.147465 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8980582524271845,
          0.8980582524271845
        ],
        "cfg_coverage": [
          0.375,
          0.3333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 60.550162,
        "reverse_margin": 60.550162
      },
      "new": "00ae0408",
      "score": 60.550162
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
        "margin": -60.550162,
        "reverse_margin": -31.555024
      },
      "new": "005e0f50",
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
        "margin": -60.550162,
        "reverse_margin": -30.57737
      },
      "new": "006559b0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6a72bd4daaf21f9ebd14f03217b4353f"></a>

### v15.7.4 [`00a81ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81ea4.md) FUN_00a81ea4

`competing_candidates` 

呼出元 2件 [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 17件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md) [`00883d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d5c.md)

- 1. [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) · スコア 34.147465 · 採用条件未達 · 順位差 28.065831999999997 / 27.115206999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aeb76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md) · スコア 6.081633 · 採用条件未達 · 順位差 -28.065831999999997 / -37.893542 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 5.517707 · 採用条件未達 · 順位差 -28.629757999999995 / -2.0236080000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) · スコア 4.653061 · 採用条件未達 · 順位差 -29.494403999999996 / 4.653061 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0051a73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a73c.md) · スコア 4.489796 · 採用条件未達 · 順位差 -29.657669 / 4.489796 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) · スコア 3.877551 · 採用条件未達 · 順位差 -30.269913999999996 / 3.877551 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`007640b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md) · スコア 3.836735 · 採用条件未達 · 順位差 -30.310729999999996 / -45.170636 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · スコア 3.722689 · 採用条件未達 · 順位差 -30.424775999999998 / -30.175312 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.47959183673469385,
          0.45483870967741935
        ],
        "cfg_coverage": [
          0.19117647058823528,
          0.14285714285714285
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 28.065831999999997,
        "reverse_margin": 27.115206999999998
      },
      "new": "00ae0814",
      "score": 34.147465
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06802721088435375,
          0.09174311926605505
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
        "margin": -28.065831999999997,
        "reverse_margin": -37.893542
      },
      "new": "00aeb76c",
      "score": 6.081633
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.05102040816326531,
          0.025295109612141653
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
        "margin": -28.629757999999995,
        "reverse_margin": -2.0236080000000003
      },
      "new": "00aec538",
      "score": 5.517707
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d34843165f7f02a8334d6d7309040fd5"></a>

### v15.7.4 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) FUN_00a823d8

`competing_candidates` 

呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 104件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md)

- 1. [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · スコア 20.782593 · 採用条件未達 · 順位差 10.485490999999998 / 10.488834999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 2. [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · スコア 10.297102 · 採用条件未達 · 順位差 -10.485490999999998 / -37.605297 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 3. [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · スコア 8.924437 · 採用条件未達 · 順位差 -11.858156 / -10.150997000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 4. [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · スコア 8.159004 · 採用条件未達 · 順位差 -12.623588999999999 / -13.884615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 5. [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · スコア 6.532319 · 採用条件未達 · 順位差 -14.250273999999997 / -25.277061999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 6. [`00a92b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a92/00a92b50.md) · スコア 6.207397 · 採用条件未達 · 順位差 -14.575195999999998 / -57.591129 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 7. [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · スコア 6.088797 · 採用条件未達 · 順位差 -14.693795999999999 / -0.0266390000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position
- 8. [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) · スコア 4.0 · 採用条件未達 · 順位差 -16.782593 / -36.012405 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18020509275262128,
          0.170147954743255
        ],
        "cfg_coverage": [
          0.028685790527018012,
          0.02943189596167009
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": 10.485490999999998,
        "reverse_margin": 10.488834999999998
      },
      "new": "00ae0e64",
      "score": 20.782593
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.009332872450743173,
          0.004951705587480132
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
        "margin": -10.485490999999998,
        "reverse_margin": -37.605297
      },
      "new": "007df0a8",
      "score": 10.297102
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.014517801590044937,
          0.02671189315242739
        ],
        "cfg_coverage": [
          0.00266844563042028,
          0.0028228652081863093
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position"
        ],
        "margin": -11.858156,
        "reverse_margin": -10.150997000000002
      },
      "new": "00996ea0",
      "score": 8.924437
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-9d98c036322324d00fcdf3aa08dadd54"></a>

### v15.7.4 [`00a8ac9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8a/00a8ac9c.md) FUN_00a8ac9c

`competing_candidates` 

呼出元 3件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f8f8.md) [`00a90618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90618.md) · 呼出先 10件 [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) [`00719de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719de8.md) [`00719eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719eac.md) [`0071a054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a054.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md)

- 1. [`00ae9f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md) · スコア 39.402622 · 採用条件未達 · 順位差 36.806468 / 32.647655 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 2.596154 · 採用条件未達 · 順位差 -36.806468 / -32.089743 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) · スコア 0.794702 · 採用条件未達 · 順位差 -38.60792 / -44.779278 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00aea2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md) · スコア 0.685714 · 採用条件未達 · 順位差 -38.716908000000004 / -32.703175 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0086584c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/0086584c.md) · スコア 0.397351 · 採用条件未達 · 順位差 -39.005271 / 0.397351 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) · スコア 0.196721 · 採用条件未達 · 順位差 -39.205901000000004 / -41.324406 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00aea188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md) · スコア 0.0 · 採用条件未達 · 順位差 -39.402622 / -53.242784 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6158940397350994,
          0.6158940397350994
        ],
        "cfg_coverage": [
          0.12244897959183673,
          0.13636363636363635
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 36.806468,
        "reverse_margin": 32.647655
      },
      "new": "00ae9f2c",
      "score": 39.402622
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.059602649006622516,
          0.04326923076923077
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
        "margin": -36.806468,
        "reverse_margin": -32.089743
      },
      "new": "00aec17c",
      "score": 2.596154
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.013245033112582781,
          0.02040816326530612
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
        "margin": -38.60792,
        "reverse_margin": -44.779278
      },
      "new": "00adee94",
      "score": 0.794702
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-8981899ec606586a3b6438fea75c3242"></a>

### v15.7.4 [`00a8aef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8a/00a8aef8.md) FUN_00a8aef8

`competing_candidates` 

呼出元 3件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a8f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f8f8.md) [`00a90618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90618.md) · 呼出先 4件 [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md) [`00719de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00719/00719de8.md) [`0071a054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a054.md) [`0071a0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0c4.md)

- 1. [`00aea188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md) · スコア 53.242784 · 採用条件未達 · 順位差 49.45331 / 44.210526 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009e3b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e3/009e3b4c.md) · スコア 3.789474 · 採用条件未達 · 順位差 -49.45331 / -5.68421 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`009df750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df750.md) · スコア 3.71134 · 採用条件未達 · 順位差 -49.531444 / 0.6185559999999999 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0081a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a450.md) · スコア 3.225806 · 採用条件未達 · 順位差 -50.016978 / -45.420027000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008c8744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8744.md) · スコア 3.225806 · 採用条件未達 · 順位差 -50.016978 / -10.271847 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008f2148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2148.md) · スコア 3.225806 · 採用条件未達 · 順位差 -50.016978 / -36.894314 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00b0a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a930.md) · スコア 3.225806 · 採用条件未達 · 順位差 -50.016978 / -63.603462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) · スコア 0.983607 · 採用条件未達 · 順位差 -52.259177 / -40.53752 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8172043010752689,
          0.8172043010752689
        ],
        "cfg_coverage": [
          0.23529411764705882,
          0.21052631578947367
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 49.45331,
        "reverse_margin": 44.210526
      },
      "new": "00aea188",
      "score": 53.242784
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06451612903225806,
          0.06315789473684211
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
        "margin": -49.45331,
        "reverse_margin": -5.68421
      },
      "new": "009e3b4c",
      "score": 3.789474
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.06451612903225806,
          0.061855670103092786
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
        "margin": -49.531444,
        "reverse_margin": 0.6185559999999999
      },
      "new": "009df750",
      "score": 3.71134
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d6e867472c04742c0ea690ab403d1fff"></a>

### v15.7.4 [`00a8b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b06c.md) FUN_00a8b06c

`competing_candidates` 

呼出元 2件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) [`00a914fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a91/00a914fc.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)

- 1. [`00aea2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md) · スコア 33.388889 · 採用条件未達 · 順位差 31.21746 / 30.646031999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) · スコア 2.171429 · 採用条件未達 · 順位差 -31.21746 / -32.817775 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0080dbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080dbf4.md) · スコア 2.057143 · 採用条件未達 · 順位差 -31.331746 / 2.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0080e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080e3ac.md) · スコア 2.057143 · 採用条件未達 · 順位差 -31.331746 / 2.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00aef6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md) · スコア 2.057143 · 採用条件未達 · 順位差 -31.331746 / 2.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b0c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md) · スコア 2.057143 · 採用条件未達 · 順位差 -31.331746 / 2.057143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005e0b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0b10.md) · スコア 1.885714 · 採用条件未達 · 順位差 -31.503175 / -27.358592 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008c4530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4530.md) · スコア 1.885714 · 採用条件未達 · 順位差 -31.503175 / -33.663876 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.08064516129032258,
          0.06944444444444445
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 31.21746,
        "reverse_margin": 30.646031999999998
      },
      "new": "00aea2fc",
      "score": 33.388889
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.002857142857142857,
          0.00303951367781155
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
        "margin": -31.21746,
        "reverse_margin": -32.817775
      },
      "new": "005ed234",
      "score": 2.171429
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03428571428571429,
          0.0916030534351145
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
        "margin": -31.331746,
        "reverse_margin": 2.057143
      },
      "new": "0080dbf4",
      "score": 2.057143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-883bff572f94747bfcfc15ac81c3df3f"></a>

### v15.7.4 [`00a8b5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b5e4.md) FUN_00a8b5e4

`competing_candidates` 

呼出元 3件 [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

- 1. [`00aea874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md) · スコア 40.823529 · 採用条件未達 · 順位差 32.103529 / 32.103529 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00683a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683a7c.md) · スコア 8.72 · 採用条件未達 · 順位差 -32.103529 / 8.72 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006e7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md) · スコア 6.883721 · 採用条件未達 · 順位差 -33.939808 / -41.601073 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`009bd0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd0c4.md) · スコア 6.724409 · 採用条件未達 · 順位差 -34.09912 / 6.724409 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) · スコア 6.21875 · 採用条件未達 · 順位差 -34.604779 / -21.926471 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`006350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md) · スコア 5.6 · 採用条件未達 · 順位差 -35.223529 / 5.6 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00646040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md) · スコア 3.807229 · 採用条件未達 · 順位差 -37.0163 / -47.018933 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) · スコア 3.50365 · 採用条件未達 · 順位差 -37.319879 / -17.518248 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.6470588235294118,
          0.6470588235294118
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
        "margin": 32.103529,
        "reverse_margin": 32.103529
      },
      "new": "00aea874",
      "score": 40.823529
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16470588235294117,
          0.112
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
        "margin": -32.103529,
        "reverse_margin": 8.72
      },
      "new": "00683a7c",
      "score": 8.72
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.16470588235294117,
          0.08139534883720931
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
        "margin": -33.939808,
        "reverse_margin": -41.601073
      },
      "new": "006e7950",
      "score": 6.883721
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0ad4456bde66c7477dbed9d7742b05af"></a>

### v15.7.4 [`00a8b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b738.md) FUN_00a8b738

`competing_candidates` 

呼出元 3件 [`00a70ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70ac4.md) [`00a70c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a70/00a70c90.md) [`00a71028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71028.md) · 呼出先 6件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

- 1. [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) · スコア 62.077295 · 採用条件未達 · 順位差 40.273348999999996 / 40.631772 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00a33434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md) · スコア 21.803946 · 採用条件未達 · 順位差 -40.273348999999996 / 21.803946 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009eec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ee/009eec8c.md) · スコア 20.44335 · 採用条件未達 · 順位差 -41.633945 / -1.077961000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a6a510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a510.md) · スコア 18.237705 · 採用条件未達 · 順位差 -43.83959 / 18.237705 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`009edf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ed/009edf9c.md) · スコア 17.73661 · 採用条件未達 · 順位差 -44.340685 / -0.1256850000000007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`008e5ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5ca8.md) · スコア 13.043478 · 採用条件未達 · 順位差 -49.033817 / 13.043478 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008e4f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4f18.md) · スコア 11.73913 · 採用条件未達 · 順位差 -50.338165000000004 / 11.73913 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00519080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519080.md) · スコア 11.186441 · 採用条件未達 · 順位差 -50.890854 / 11.186441 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.8586956521739131,
          0.8586956521739131
        ],
        "cfg_coverage": [
          0.6129032258064516,
          0.5277777777777778
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 40.273348999999996,
        "reverse_margin": 40.631772
      },
      "new": "00aea9c8",
      "score": 62.077295
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.358695652173913,
          0.32038834951456313
        ],
        "cfg_coverage": [
          0.12903225806451613,
          0.13333333333333333
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -40.273348999999996,
        "reverse_margin": 21.803946
      },
      "new": "00a33434",
      "score": 21.803946
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.3695652173913043,
          0.29310344827586204
        ],
        "cfg_coverage": [
          0.1935483870967742,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -41.633945,
        "reverse_margin": -1.077961000000002
      },
      "new": "009eec8c",
      "score": 20.44335
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ef1f5e6f5a23d0d2fdcfc42460b916ef"></a>

### v15.7.4 [`00a8b8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8b/00a8b8dc.md) FUN_00a8b8dc

`competing_candidates` 

呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0063c0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c178.md)

- 1. [`00aeab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md) · スコア 20.022623 · 採用条件未達 · 順位差 12.572178999999998 / 15.91365 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`005c1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1310.md) · スコア 7.450444 · 採用条件未達 · 順位差 -12.572178999999998 / 7.450444 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0093ac54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093a/0093ac54.md) · スコア 4.724343 · 採用条件未達 · 順位差 -15.298279999999998 / 4.724343 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`009385d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md) · スコア 4.349925 · 採用条件未達 · 順位差 -15.672698 / 4.349925 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) · スコア 3.128527 · 採用条件未達 · 順位差 -16.894095999999998 / 3.128527 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`008ab274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab274.md) · スコア 3.033311 · 採用条件未達 · 順位差 -16.989311999999998 / 3.033311 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`008ac33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac33c.md) · スコア 2.939267 · 採用条件未達 · 順位差 -17.083356 / 2.939267 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`007839a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md) · スコア 2.564263 · 採用条件未達 · 順位差 -17.45836 / -25.527849 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2727272727272727,
          0.292436974789916
        ],
        "cfg_coverage": [
          0.08411214953271028,
          0.08294930875576037
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 12.572178999999998,
        "reverse_margin": 15.91365
      },
      "new": "00aeab6c",
      "score": 20.022623
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07993730407523511,
          0.18545454545454546
        ],
        "cfg_coverage": [
          0.03271028037383177,
          0.05785123966942149
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -12.572178999999998,
        "reverse_margin": 7.450444
      },
      "new": "005c1310",
      "score": 7.450444
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.03761755485893417,
          0.05825242718446602
        ],
        "cfg_coverage": [
          0.02336448598130841,
          0.029411764705882353
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -15.298279999999998,
        "reverse_margin": 4.724343
      },
      "new": "0093ac54",
      "score": 4.724343
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-16f392a961baec60cb6f0e14bbf53421"></a>

### v15.7.4 [`00a8c2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c2d4.md) FUN_00a8c2d4

`competing_candidates` 

呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 11件 [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md)

- 1. [`00aeb584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md) · スコア 30.769231 · 採用条件未達 · 順位差 7.3282370000000014 / -1.164835 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`0064d7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d7f4.md) · スコア 23.440994 · 採用条件未達 · 順位差 -7.3282370000000014 / 23.440994 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`006dad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md) · スコア 16.857143 · 採用条件未達 · 順位差 -13.912088 / 16.857143 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`0068452c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/0068452c.md) · スコア 14.503937 · 採用条件未達 · 順位差 -16.265294 / 14.503937 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`006e29b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md) · スコア 14.265635 · 採用条件未達 · 順位差 -16.503596 / 14.265635 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`00b0f1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md) · スコア 12.357616 · 採用条件未達 · 順位差 -18.411615 / 12.357616 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md) · スコア 11.806452 · 採用条件未達 · 順位差 -18.962779 / 11.806452 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`009cfe60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cf/009cfe60.md) · スコア 10.972376 · 採用条件未達 · 順位差 -19.796855 / -17.443094 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.4,
          0.4
        ],
        "cfg_coverage": [
          0.043478260869565216,
          0.038461538461538464
        ],
        "mapped_data": 5,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 7.3282370000000014,
        "reverse_margin": -1.164835
      },
      "new": "00aeb584",
      "score": 30.769231
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2761904761904762,
          0.32222222222222224
        ],
        "cfg_coverage": [
          0.043478260869565216,
          0.058823529411764705
        ],
        "mapped_data": 4,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -7.3282370000000014,
        "reverse_margin": 23.440994
      },
      "new": "0064d7f4",
      "score": 23.440994
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.18095238095238095,
          0.19
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -13.912088,
        "reverse_margin": 16.857143
      },
      "new": "006dad34",
      "score": 16.857143
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a2cc6278992bd9c9f7e8a788b81aad45"></a>

### v15.7.4 [`00a8c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c4bc.md) FUN_00a8c4bc

`competing_candidates` 

呼出元 2件 [`00a908b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) [`00a90e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90e6c.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

- 1. [`00aeb76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md) · スコア 43.975175 · 採用条件未達 · 順位差 35.495175 / 35.255175 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) · スコア 8.48 · 採用条件未達 · 順位差 -35.495175 / 8.48 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · スコア 4.615385 · 採用条件未達 · 順位差 -39.359790000000004 / 4.615385 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) · スコア 4.322581 · 採用条件未達 · 順位差 -39.652594 / -29.824883999999997 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) · スコア 3.964382 · 採用条件未達 · 順位差 -40.010793 / -29.933619 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00b0b8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md) · スコア 3.85567 · 採用条件未達 · 順位差 -40.119505000000004 / 3.85567 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`0063b784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md) · スコア 3.742739 · 採用条件未達 · 順位差 -40.232436 / 3.742739 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) · スコア 3.100917 · 採用条件未達 · 順位差 -40.874258 / -20.853106 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.591743119266055,
          0.591743119266055
        ],
        "cfg_coverage": [
          0.4230769230769231,
          0.3235294117647059
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 35.495175,
        "reverse_margin": 35.255175
      },
      "new": "00aeb76c",
      "score": 43.975175
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.12385321100917432,
          0.108
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
        "margin": -35.495175,
        "reverse_margin": 8.48
      },
      "new": "008eb380",
      "score": 8.48
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.11009174311926606,
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
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -39.359790000000004,
        "reverse_margin": 4.615385
      },
      "new": "00527de8",
      "score": 4.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2ebcd9b8652c01e301a6b58be6aee689"></a>

### v15.7.4 [`00a8c898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8c898.md) FUN_00a8c898

`competing_candidates` 

呼出元 3件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006dd65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006dd65c.md) [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0063eaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063eaf8.md) [`00aa3f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3f64.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

- 1. [`00aebb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md) · スコア 36.431438 · 採用条件未達 · 順位差 26.795074 / 31.118938 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`007640b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md) · スコア 9.636364 · 採用条件未達 · 順位差 -26.795074 / -39.371007 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`006e3e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3e10.md) · スコア 5.384615 · 採用条件未達 · 順位差 -31.046823 / -36.898213 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0077acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md) · スコア 5.384615 · 採用条件未達 · 順位差 -31.046823 / 5.384615 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a35c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35c68.md) · スコア 5.153374 · 採用条件未達 · 順位差 -31.278064 / 5.153374 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`005f3a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3a30.md) · スコア 5.0 · 採用条件未達 · 順位差 -31.431438 / -36.8198 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00763d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763d18.md) · スコア 4.898551 · 採用条件未達 · 順位差 -31.532887 / -65.797101 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) · スコア 4.714932 · 採用条件未達 · 順位差 -31.716506 / -15.905373999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5448717948717948,
          0.5448717948717948
        ],
        "cfg_coverage": [
          0.11764705882352941,
          0.08695652173913043
        ],
        "mapped_data": 1,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 26.795074,
        "reverse_margin": 31.118938
      },
      "new": "00aebb48",
      "score": 36.431438
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.1346153846153846,
          0.12727272727272726
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
        "margin": -26.795074,
        "reverse_margin": -39.371007
      },
      "new": "007640b0",
      "score": 9.636364
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.08974358974358974,
          0.1037037037037037
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
        "margin": -31.046823,
        "reverse_margin": -36.898213
      },
      "new": "006e3e10",
      "score": 5.384615
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e7928f3a43d24bccb3233b0a2f38e351"></a>

### v15.7.4 [`00a8cdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cdac.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aec128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec128.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec174.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec160.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aec128",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec174",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-84501effd187a8552e559258271284ca"></a>

### v15.7.4 [`00a8cdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cdb0.md) FUN_00a8cdb0

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`0047d694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md) · スコア 75.384615 · 採用条件未達 · 順位差 75.384615 / 75.384615 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.384615 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aec160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec160.md) · スコア 0.0 · 採用条件未達 · 順位差 -75.384615 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.9230769230769231,
          0.9230769230769231
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
        "margin": 75.384615,
        "reverse_margin": 75.384615
      },
      "new": "0047d694",
      "score": 75.384615
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
        "margin": -75.384615,
        "reverse_margin": 0.0
      },
      "new": "00aec12c",
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
        "margin": -75.384615,
        "reverse_margin": 0.0
      },
      "new": "00aec160",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-d2e67e815e0cd1a264e5ffd4461354d4"></a>

### v15.7.4 [`00a8cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cde4.md) FUN_00a8cde4

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0047d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md) · スコア 80.0 · 採用条件未達 · 順位差 80.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors, already_matched_elsewhere
- 2. [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aec160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec160.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 80.0,
        "reverse_margin": 80.0
      },
      "new": "0047d6c8",
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
      "new": "00aec12c",
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
      "new": "00aec160",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c4986ac8f6cb7b5987f51aac3a7b4f46"></a>

### v15.7.4 [`00a8cdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cdf8.md) FUN_00a8cdf8

`competing_candidates` 

呼出元 1件 [`00a72140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a72140.md) · 呼出先 0件 

- 1. [`00aec174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec174.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aec128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec128.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec178.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec160.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 0.0192 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aec174",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec128",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec178",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-cd78934fb6e962bc15095401a7c94c85"></a>

### v15.7.4 [`00a8cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8cdfc.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a72140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a72140.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aec178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec178.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 78.9808 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 4.0192 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec174.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aec4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec160.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 78.9808
      },
      "new": "00aec178",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec17c",
      "score": 4.0192
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-74582b96e0219e39d8b87b6bde27133a"></a>

### v15.7.4 [`00a8ce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8ce00.md) FUN_00a8ce00

`competing_candidates` 

呼出元 0件  · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0059be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059b/0059be80.md)

- 1. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 34.685897 · 採用条件未達 · 順位差 30.070511999999997 / 29.058806999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ae9f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md) · スコア 4.615385 · 採用条件未達 · 順位差 -30.070511999999997 / -34.787237000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0072b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b264.md) · スコア 4.038462 · 採用条件未達 · 順位差 -30.647434999999998 / 4.038462 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00a600b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a600b8.md) · スコア 3.461538 · 採用条件未達 · 順位差 -31.224358999999996 / 3.461538 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`007f0394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0394.md) · スコア 3.173077 · 採用条件未達 · 順位差 -31.512819999999998 / 3.173077 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006e3e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3e10.md) · スコア 2.913753 · 採用条件未達 · 順位差 -31.772143999999997 / -39.369075 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0077af28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077af28.md) · スコア 2.019231 · 採用条件未達 · 順位差 -32.666666 / -41.837912 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008c8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8c70.md) · スコア 0.8 · 採用条件未達 · 順位差 -33.885897 / -7.3111109999999995 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5336538461538461,
          0.5336538461538461
        ],
        "cfg_coverage": [
          0.13333333333333333,
          0.14285714285714285
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 30.070511999999997,
        "reverse_margin": 29.058806999999998
      },
      "new": "00aec17c",
      "score": 34.685897
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.10596026490066225
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
        "margin": -30.070511999999997,
        "reverse_margin": -34.787237000000005
      },
      "new": "00ae9f2c",
      "score": 4.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0673076923076923,
          0.1
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
        "margin": -30.647434999999998,
        "reverse_margin": 4.038462
      },
      "new": "0072b264",
      "score": 4.038462
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-56d62b861af3f3661ab8cb9444047eb5"></a>

### v15.7.4 [`00a8d140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d140.md) FUN_00a8d140

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -34.285714 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -75.384615 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": -34.285714
      },
      "new": "00aec4bc",
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
        "reverse_margin": -75.384615
      },
      "new": "00aec4e8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c3b15e27ac3c318d39da68248b0700d8"></a>

### v15.7.4 [`00a8d15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d15c.md) FUN_00a8d15c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aec4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4d8.md) · スコア 79.0 · 採用条件未達 · 順位差 76.6 / 76.6 · 
- 2. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec178.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aec4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 0.0577 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 76.6,
        "reverse_margin": 76.6
      },
      "new": "00aec4d8",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec51c",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec4bc",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-e4f54f5d4725dffdf557e63e99e8331b"></a>

### v15.7.4 [`00a8d168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d168.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aec4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e4.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 78.9808 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) · スコア 4.0192 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec530.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aec4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4d8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 78.9808
      },
      "new": "00aec4e4",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec17c",
      "score": 4.0192
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5f62629d935baafafef3a030e7794037"></a>

### v15.7.4 [`00a8d16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d16c.md) FUN_00a8d16c

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 66.153846 · 採用条件未達 · 順位差 41.538461 / -9.230768999999995 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aec4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4bc.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -9.670328999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7692307692307693,
          0.7692307692307693
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
        "margin": 41.538461,
        "reverse_margin": -9.230768999999995
      },
      "new": "00aec4e8",
      "score": 66.153846
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.14285714285714285
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
        "margin": -41.538461,
        "reverse_margin": -9.670328999999999
      },
      "new": "00aec4bc",
      "score": 24.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.2
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
        "margin": -41.538461,
        "reverse_margin": -55.384615
      },
      "new": "00aec51c",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-3fdabff2098bc41aec0dc4aa9adb5ec5"></a>

### v15.7.4 [`00a8d1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1a0.md) FUN_00a8d1a0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 56.0 · 採用条件未達 · 順位差 31.384615 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 31.384615,
        "reverse_margin": -24.0
      },
      "new": "00aec51c",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.07692307692307693
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
        "margin": -31.384615,
        "reverse_margin": -50.76922999999999
      },
      "new": "00aec4e8",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-4ea897ff6b6a65f841d7a5532b33e908"></a>

### v15.7.4 [`00a8d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1b4.md) FUN_00a8d1b4

`competing_candidates` 

呼出元 1件 [`00a7240c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7240c.md) · 呼出先 0件 

- 1. [`00aec530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec530.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aec4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec534.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 0.0067 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aec530",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec4e4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec534",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-5c1fe3a24714abd1931f738f9e42c8cc"></a>

### v15.7.4 [`00a8d1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1b8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a7240c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7240c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aec534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec534.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 78.9928 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 4.0067 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec530.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aecf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf34.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 78.9928
      },
      "new": "00aec534",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec538",
      "score": 4.0067
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1375d2f1abcf4cfd959e1a30048d7b33"></a>

### v15.7.4 [`00a8d1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8d1bc.md) FUN_00a8d1bc

`competing_candidates` 

呼出元 0件  · 呼出先 26件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

- 1. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 7.541315 · 採用条件未達 · 順位差 1.823963 / 2.0236080000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) · スコア 5.717352 · 採用条件未達 · 順位差 -1.823963 / -28.430113 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · スコア 4.358744 · 採用条件未達 · 順位差 -3.1825710000000003 / -38.392341 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) · スコア 4.039356 · 採用条件未達 · 順位差 -3.5019590000000003 / -61.657892000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0066f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md) · スコア 2.429338 · 採用条件未達 · 順位差 -5.1119769999999995 / 2.429338 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 6. [`006e8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md) · スコア 2.214669 · 採用条件未達 · 順位差 -5.326646 / -32.947291 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`00a7c2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c2fc.md) · スコア 2.188531 · 採用条件未達 · 順位差 -5.352784 / 2.188531 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`0067f004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067f004.md) · スコア 2.16129 · 採用条件未達 · 順位差 -5.380025 / -32.392284 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.0626118067978533,
          0.05902192242833052
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
        "margin": 1.823963,
        "reverse_margin": 2.0236080000000003
      },
      "new": "00aec538",
      "score": 7.541315
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.028622540250447227,
          0.05161290322580645
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
        "margin": -1.823963,
        "reverse_margin": -28.430113
      },
      "new": "00ae0814",
      "score": 5.717352
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.007155635062611807,
          0.005979073243647235
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
        "margin": -3.1825710000000003,
        "reverse_margin": -38.392341
      },
      "new": "0061300c",
      "score": 4.358744
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e6510e3a7375115d38e2ec312d0a0e4c"></a>

### v15.7.4 [`00a8db14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db14.md) FUN_00a8db14

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`008da19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da19c.md) · スコア 80.0 · 採用条件未達 · 順位差 25.714286 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 54.285714 · 採用条件未達 · 順位差 -25.714286 / 29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 3. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 24.615385 · 採用条件未達 · 順位差 -55.384615 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "008da19c",
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
        "reverse_margin": 29.670329
      },
      "new": "00aecf18",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
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
        "margin": -55.384615,
        "reverse_margin": -50.76922999999999
      },
      "new": "00aecf44",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-377b8063618aed3aba92a6ecccb5db56"></a>

### v15.7.4 [`00a8db30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db30.md) FUN_00a8db30

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aecf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf34.md) · スコア 79.0 · 採用条件未達 · 順位差 76.6 / 76.6 · 
- 2. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aec534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec534.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aecf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf40.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 0.0202 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 76.6,
        "reverse_margin": 76.6
      },
      "new": "00aecf34",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aecf78",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aecf18",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-19890d61cf0c20c37ee05c003fa81446"></a>

### v15.7.4 [`00a8db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db3c.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aecf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf40.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 78.9928 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · スコア 4.0067 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aecf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aecf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf34.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 78.9928
      },
      "new": "00aecf40",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aec538",
      "score": 4.0067
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b927e961d203102c5bf6de0963bb2e58"></a>

### v15.7.4 [`00a8db40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db40.md) FUN_00a8db40

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 66.153846 · 採用条件未達 · 順位差 41.538461 / -9.230768999999995 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aecf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf18.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 0.0 · 採用条件未達 · 順位差 -66.153846 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7692307692307693,
          0.7692307692307693
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
        "margin": 41.538461,
        "reverse_margin": -9.230768999999995
      },
      "new": "00aecf44",
      "score": 66.153846
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.14285714285714285
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
        "margin": -41.538461,
        "reverse_margin": -29.670329
      },
      "new": "00aecf18",
      "score": 24.615385
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
        "margin": -66.153846,
        "reverse_margin": 0.0
      },
      "new": "00aecf78",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-64441e686b2e821c837bdf7bf9439fdc"></a>

### v15.7.4 [`00a8db74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db74.md) FUN_00a8db74

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 24.615385 · 採用条件未達 · 順位差 24.615385 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.615385 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.07692307692307693
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
        "margin": 24.615385,
        "reverse_margin": -50.76922999999999
      },
      "new": "00aecf44",
      "score": 24.615385
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
        "margin": -24.615385,
        "reverse_margin": 0.0
      },
      "new": "00aecf78",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2e875380a42e2707a9af0ca3b1d3a118"></a>

### v15.7.4 [`00a8db88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db88.md) FUN_00a8db88

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 0件 

- 1. [`00aecf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf8c.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aecf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf40.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aecf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf90.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed194.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aecf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf94.md) · スコア 0.0336 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aecf8c",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aecf40",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aecf90",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2cc4892c35f6d63b333140244d831ad5"></a>

### v15.7.4 [`00a8db8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db8c.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aecf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf90.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aecf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf8c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1b0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aecf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf78.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed194.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aecf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf94.md) · スコア 0.0336 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aecf90",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aecf8c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8cbe10a93d732cfa54de94534e3dbcfe"></a>

### v15.7.4 [`00a8db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db90.md) FUN_00a8db90

`competing_candidates` 

呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

- 1. [`00aecf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf94.md) · スコア 32.401592 · 採用条件未達 · 順位差 17.253427000000002 / 17.645289 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`006d9aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9aa8.md) · スコア 15.148165 · 採用条件未達 · 順位差 -17.253427000000002 / 15.148165 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009a319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a319c.md) · スコア 9.777385 · 採用条件未達 · 順位差 -22.624207 / -17.191341 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00a87414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87414.md) · スコア 9.579832 · 採用条件未達 · 順位差 -22.82176 / 9.579832 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 5. [`00a7c174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c174.md) · スコア 8.571429 · 採用条件未達 · 順位差 -23.830163 / -21.668641 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0057e214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md) · スコア 7.058824 · 採用条件未達 · 順位差 -25.342768 / 7.058824 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00a7e4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e4b4.md) · スコア 7.058824 · 採用条件未達 · 順位差 -25.342768 / -23.812359999999998 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00693418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693418.md) · スコア 4.635905 · 採用条件未達 · 順位差 -27.765687 / 4.635905 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.48739495798319327,
          0.48739495798319327
        ],
        "cfg_coverage": [
          0.15789473684210525,
          0.17142857142857143
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 17.253427000000002,
        "reverse_margin": 17.645289
      },
      "new": "00aecf94",
      "score": 32.401592
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.24369747899159663,
          0.38666666666666666
        ],
        "cfg_coverage": [
          0.02631578947368421,
          0.04
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -17.253427000000002,
        "reverse_margin": 15.148165
      },
      "new": "006d9aa8",
      "score": 15.148165
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.15126050420168066,
          0.1565217391304348
        ],
        "cfg_coverage": [
          0.05263157894736842,
          0.03508771929824561
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.624207,
        "reverse_margin": -17.191341
      },
      "new": "009a319c",
      "score": 9.777385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-70c20a89288facd7934b860f9e26dad1"></a>

### v15.7.4 [`00a8dd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8dd90.md) FUN_00a8dd90

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed194.md) · スコア 54.285714 · 採用条件未達 · 順位差 54.285714 / 54.285714 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 0.0 · 採用条件未達 · 順位差 -54.285714 / -37.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00aed194",
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
        "margin": -54.285714,
        "reverse_margin": -37.5
      },
      "new": "00aed1c0",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-428858c3d4f87aec2c3d0206689c5f4a"></a>

### v15.7.4 [`00a8ddac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8ddac.md) FUN_00a8ddac

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1b0.md) · スコア 79.0 · 採用条件未達 · 順位差 77.2857 / 77.2857 · 
- 2. [`00aed194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed194.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed200.md) · スコア 1.5 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aecf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf90.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1bc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 0.75 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aecf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf94.md) · スコア 0.1008 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.2857,
        "reverse_margin": 77.2857
      },
      "new": "00aed1b0",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed194",
      "score": 1.7143
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed200",
      "score": 1.5
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-81252cd329ce0c79ed54200170882592"></a>

### v15.7.4 [`00a8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8ddb8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1bc.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed220.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1b0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed200.md) · スコア 0.7308 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed194.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 0.4224 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aecf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf94.md) · スコア 0.0336 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aed1bc",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed220",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-382f44bb7e20c2f1af2be309c8061d8f"></a>

### v15.7.4 [`00a8ddbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8ddbc.md) FUN_00a8ddbc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`007fd0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd0e4.md) · スコア 68.75 · 採用条件未達 · 順位差 31.25 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 37.5 · 採用条件未達 · 順位差 -31.25 / 37.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`0065f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f03c.md) · スコア 33.75 · 採用条件未達 · 順位差 -35.0 / -23.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00618128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618128.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -38.75 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f598.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0065f6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f6d8.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`007fb188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb188.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -50.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`00830a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830a88.md) · スコア 18.75 · 採用条件未達 · 順位差 -50.0 / -15.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
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
          "short_function_requires_other_identity_evidence",
          "instruction_coverage",
          "insufficient_independent_call_anchors"
        ],
        "margin": 31.25,
        "reverse_margin": 0.0
      },
      "new": "007fd0e4",
      "score": 68.75
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "margin": -31.25,
        "reverse_margin": 37.5
      },
      "new": "00aed1c0",
      "score": 37.5
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5625,
          0.5625
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
        "margin": -35.0,
        "reverse_margin": -23.75
      },
      "new": "0065f03c",
      "score": 33.75
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-fd7252f5b5b2ff64fd66a3308aaf6b1a"></a>

### v15.7.4 [`00a8ddfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8ddfc.md) FUN_00a8ddfc

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`0065f718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f718.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 27.5 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aed200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed200.md) · スコア 65.0 · 採用条件未達 · 順位差 0.0 / 65.0 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00618168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618168.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`006270a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270a4.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`0065eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eb60.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0065f07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f07c.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`0065f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f5d8.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`006fb18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb18c.md) · スコア 37.5 · 採用条件未達 · 順位差 -27.5 / -27.5 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 27.5
      },
      "new": "0065f718",
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
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 0.0,
        "reverse_margin": 65.0
      },
      "new": "00aed200",
      "score": 65.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.625,
          0.625
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
        "margin": -27.5,
        "reverse_margin": -27.5
      },
      "new": "00618168",
      "score": 37.5
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-a3cacfc0f35c109545984763fdf40719"></a>

### v15.7.4 [`00a8de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8de1c.md) FUN_00a8de1c

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 0件 

- 1. [`00aed220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed220.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aed1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1bc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed224.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed200.md) · スコア 0.5 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 0.25 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 0.093 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aed220",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed1bc",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed224",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ebfa7b145930c2e06cb25303f0d3e265"></a>

### v15.7.4 [`00a8de20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8de20.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed224.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed220.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2f0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed200.md) · スコア 0.7308 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) · スコア 0.4224 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 0.2017 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aed224",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed220",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-8fc7550d44def2155338e2ba161ccd90"></a>

### v15.7.4 [`00a8de24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8de24.md) FUN_00a8de24

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e97fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97fc.md) [`009e9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md)

- 1. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 46.093023 · 採用条件未達 · 順位差 26.038303000000003 / 17.038759000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`009a3410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3410.md) · スコア 20.05472 · 採用条件未達 · 順位差 -26.038303000000003 / 20.05472 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`0061706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md) · スコア 19.333333 · 採用条件未達 · 順位差 -26.759690000000003 / -43.777778 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 18.436782 · 採用条件未達 · 順位差 -27.656241 / -17.241379000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) · スコア 17.166276 · 採用条件未達 · 順位差 -28.926747000000002 / -31.358314000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`00aee628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee628.md) · スコア 13.162791 · 採用条件未達 · 順位差 -32.930232000000004 / 13.162791 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`00926f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926f80.md) · スコア 12.591362 · 採用条件未達 · 順位差 -33.501661 / -33.790991000000005 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`0093323c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093323c.md) · スコア 10.5625 · 採用条件未達 · 順位差 -35.530523 / -31.1875 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5348837209302325,
          0.5348837209302325
        ],
        "cfg_coverage": [
          0.7,
          0.7777777777777778
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 26.038303000000003,
        "reverse_margin": 17.038759000000002
      },
      "new": "00aed228",
      "score": 46.093023
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2558139534883721,
          0.2558139534883721
        ],
        "cfg_coverage": [
          0.4,
          0.23529411764705882
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -26.038303000000003,
        "reverse_margin": 20.05472
      },
      "new": "009a3410",
      "score": 20.05472
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.27906976744186046,
          0.2222222222222222
        ],
        "cfg_coverage": [
          0.3,
          0.375
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -26.759690000000003,
        "reverse_margin": -43.777778
      },
      "new": "0061706c",
      "score": 19.333333
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-7b87717c3de22860eb7242f326130424"></a>

### v15.7.4 [`00a8ded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8ded0.md) FUN_00a8ded0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 54.285714 · 採用条件未達 · 順位差 29.670329 / 29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 24.615385 · 採用条件未達 · 順位差 -29.670329 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 29.670329,
        "reverse_margin": 29.670329
      },
      "new": "00aed2d4",
      "score": 54.285714
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.14285714285714285,
          0.07692307692307693
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
        "margin": -29.670329,
        "reverse_margin": -50.76922999999999
      },
      "new": "00aed300",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-912cff9b1d6ed1823181bd263cf25449"></a>

### v15.7.4 [`00a8deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8deec.md) FUN_00a8deec

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2f0.md) · スコア 79.0 · 採用条件未達 · 順位差 76.6 / 76.6 · 
- 2. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed224.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2fc.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 0.2791 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 76.6,
        "reverse_margin": 76.6
      },
      "new": "00aed2f0",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed334",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed2d4",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-1f1d6bc40793e38a94bf010e7434185a"></a>

### v15.7.4 [`00a8def8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8def8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2fc.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed348.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2f0.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 0.2017 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aed2fc",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed348",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-2a23de51a779dc99eece0d34151e3405"></a>

### v15.7.4 [`00a8defc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8defc.md) FUN_00a8defc

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 66.153846 · 採用条件未達 · 順位差 41.538461 / -9.230768999999995 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2d4.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -29.670329 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 24.615385 · 採用条件未達 · 順位差 -41.538461 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.7692307692307693,
          0.7692307692307693
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
        "margin": 41.538461,
        "reverse_margin": -9.230768999999995
      },
      "new": "00aed300",
      "score": 66.153846
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.14285714285714285
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
        "margin": -41.538461,
        "reverse_margin": -29.670329
      },
      "new": "00aed2d4",
      "score": 24.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.2
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
        "margin": -41.538461,
        "reverse_margin": -55.384615
      },
      "new": "00aed334",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-e5fbd57d0717c5c4e254be601aaa3eab"></a>

### v15.7.4 [`00a8df30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df30.md) FUN_00a8df30

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 56.0 · 採用条件未達 · 順位差 31.384615 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 24.615385 · 採用条件未達 · 順位差 -31.384615 / -50.76922999999999 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "margin": 31.384615,
        "reverse_margin": -24.0
      },
      "new": "00aed334",
      "score": 56.0
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2,
          0.07692307692307693
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
        "margin": -31.384615,
        "reverse_margin": -50.76922999999999
      },
      "new": "00aed300",
      "score": 24.615385
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-37476a1eb8920333d0fa16df8efd4a03"></a>

### v15.7.4 [`00a8df44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df44.md) FUN_00a8df44

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 0件 

- 1. [`00aed348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed348.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aed2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed2fc.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed34c.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 0.046 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aed348",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed2fc",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed34c",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4b8f212088e2e7d072e0727567a9517b"></a>

### v15.7.4 [`00a8df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df48.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed34c.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed348.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4c8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed334.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 0.046 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aed34c",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed348",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-f46991ef67ca039e0344cf470fe85494"></a>

### v15.7.4 [`00a8df4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8df4c.md) FUN_00a8df4c

`competing_candidates` 

呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00a81b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a81/00a81b6c.md) [`00aa97bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa97bc.md) [`00aaa93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa93c.md)

- 1. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 35.678161 · 採用条件未達 · 順位差 15.565230000000003 / 17.241379000000002 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) · スコア 20.112931 · 採用条件未達 · 順位差 -15.565230000000003 / -25.980092000000003 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00934bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934bbc.md) · スコア 13.337098 · 採用条件未達 · 順位差 -22.341063000000005 / -35.187492000000006 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 4. [`0061706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md) · スコア 11.959345 · 採用条件未達 · 順位差 -23.718816000000004 / -51.151766 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`008f2148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2148.md) · スコア 10.12987 · 採用条件未達 · 順位差 -25.548291000000003 / -29.99025 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`0081a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a450.md) · スコア 3.896104 · 採用条件未達 · 順位差 -31.782057000000002 / -44.749729 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 7. [`009a3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3538.md) · スコア 3.488636 · 採用条件未達 · 順位差 -32.189525 / -28.977273000000004 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 8. [`008ef718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef718.md) · スコア 3.116883 · 採用条件未達 · 順位差 -32.561278 / -51.168831 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
          0.5057471264367817
        ],
        "cfg_coverage": [
          0.34782608695652173,
          0.26666666666666666
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 15.565230000000003,
        "reverse_margin": 17.241379000000002
      },
      "new": "00aed350",
      "score": 35.678161
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.23376623376623376,
          0.4186046511627907
        ],
        "cfg_coverage": [
          0.30434782608695654,
          0.7777777777777778
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -15.565230000000003,
        "reverse_margin": -25.980092000000003
      },
      "new": "00aed228",
      "score": 20.112931
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.2077922077922078,
          0.26229508196721313
        ],
        "cfg_coverage": [
          0.043478260869565216,
          0.07142857142857142
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": -22.341063000000005,
        "reverse_margin": -35.187492000000006
      },
      "new": "00934bbc",
      "score": 13.337098
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-de2541236ca461837912986b6fd1ec76"></a>

### v15.7.4 [`00a8e080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e080.md) FUN_00a8e080

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`004433d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004433d4.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 2. [`00933924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933924.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 25.714286 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 3. [`00a024ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a024ec.md) · スコア 80.0 · 採用条件未達 · 順位差 0.0 / 80.0 · short_function_requires_other_identity_evidence, insufficient_independent_call_anchors
- 4. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -80.0 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
        "reverse_margin": 25.714286
      },
      "new": "004433d4",
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
        "reverse_margin": 25.714286
      },
      "new": "00933924",
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
        "reverse_margin": 80.0
      },
      "new": "00a024ec",
      "score": 80.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-6c90e0f1aec4333d55ba9bf555cdb198"></a>

### v15.7.4 [`00a8e09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e09c.md) FUN_00a8e09c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4c8.md) · スコア 79.0 · 採用条件未達 · 順位差 76.6 / 76.6 · 
- 2. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed34c.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d4.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 0.1379 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 76.6,
        "reverse_margin": 76.6
      },
      "new": "00aed4c8",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed50c",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed4ac",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-ab56c0744405bb34a7ae2492a60f42e9"></a>

### v15.7.4 [`00a8e0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0a8.md) _ZdlPv

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d4.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 79.0 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed520.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4c8.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · スコア 0.046 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 79.0
      },
      "new": "00aed4d4",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed520",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b249d54301668f347759c2ce9323a038"></a>

### v15.7.4 [`00a8e0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0ac.md) FUN_00a8e0ac

`competing_candidates` 

呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

- 1. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 24.615385 · 採用条件未達 · 順位差 1.538461999999999 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 23.076923 · 採用条件未達 · 順位差 -1.538461999999999 / -32.307691999999996 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 3. [`00aed4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4ac.md) · スコア 0.0 · 採用条件未達 · 順位差 -24.615385 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.07692307692307693,
          0.2
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
        "margin": 1.538461999999999,
        "reverse_margin": -55.384615
      },
      "new": "00aed50c",
      "score": 24.615385
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.38461538461538464,
          0.38461538461538464
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
        "margin": -1.538461999999999,
        "reverse_margin": -32.307691999999996
      },
      "new": "00aed4d8",
      "score": 23.076923
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
        "margin": -24.615385,
        "reverse_margin": 0.0
      },
      "new": "00aed4ac",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-0aa9c84de3da10e9d7ef8469ae15ded7"></a>

### v15.7.4 [`00a8e0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0e0.md) FUN_00a8e0e0

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 56.0 · 採用条件未達 · 順位差 56.0 / -24.0 · short_function_requires_other_identity_evidence, instruction_coverage, insufficient_independent_call_anchors
- 2. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.0 · 採用条件未達 · 順位差 -56.0 / -55.384615 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00aed50c",
      "score": 56.0
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
        "margin": -56.0,
        "reverse_margin": -55.384615
      },
      "new": "00aed4d8",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-c385575740e5bb0cb745ddd5e1a87822"></a>

### v15.7.4 [`00a8e0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0f4.md) FUN_00a8e0f4

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 0件 

- 1. [`00aed520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed520.md) · スコア 64.0 · 採用条件未達 · 順位差 60.0 / 60.0 · 
- 2. [`00aed4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d4.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed524.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 0.8 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed93c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.3077 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) · スコア 0.0199 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 60.0,
        "reverse_margin": 60.0
      },
      "new": "00aed520",
      "score": 64.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed4d4",
      "score": 4.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed524",
      "score": 4.0
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-4f2e03838a70bebd435a706541670dd4"></a>

### v15.7.4 [`00a8e0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0f8.md) _ZdlPv

`competing_candidates` 

呼出元 1件 [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

- 1. [`00aed524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed524.md) · スコア 83.0 · 採用条件未達 · 順位差 77.4167 / 78.9801 · 
- 2. [`0043bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd58.md) · スコア 5.5833 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) · スコア 4.0199 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed520.md) · スコア 4.0 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed958.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed50c.md) · スコア 1.1846 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) · スコア 0.5907 · 採用条件未達 · 順位差 — / — · 
- 8. [`00aed93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed93c.md) · スコア 0.5714 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 77.4167,
        "reverse_margin": 78.9801
      },
      "new": "00aed524",
      "score": 83.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "0043bd58",
      "score": 5.5833
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed528",
      "score": 4.0199
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

<a id="review-b056d04896aba04e531ee8b4fd9ef948"></a>

### v15.7.4 [`00a8e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e0fc.md) FUN_00a8e0fc

`competing_candidates` 

呼出元 0件  · 呼出先 19件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

- 1. [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) · スコア 41.68828 · 採用条件未達 · 順位差 24.526631 / 24.648887 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00921cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921cc4.md) · スコア 17.161649 · 採用条件未達 · 順位差 -24.526631 / 17.161649 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 3. [`009ba7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md) · スコア 10.771566 · 採用条件未達 · 順位差 -30.916714 / 10.771566 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 4. [`00ad04dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md) · スコア 9.754617 · 採用条件未達 · 順位差 -31.933663 / -29.277641 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 5. [`006559b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006559b0.md) · スコア 8.221604 · 採用条件未達 · 順位差 -33.466676 / -22.355766 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 6. [`007f7cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f7/007f7cac.md) · スコア 8.181128 · 採用条件未達 · 順位差 -33.507152 / 8.181128 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 7. [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · スコア 8.004048 · 採用条件未達 · 順位差 -33.684232 / 8.004048 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere
- 8. [`00b9720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b97/00b9720c.md) · スコア 4.260056 · 採用条件未達 · 順位差 -37.428224 / 4.260056 · instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors, already_matched_elsewhere

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.5472636815920398,
          0.5472636815920398
        ],
        "cfg_coverage": [
          0.4576271186440678,
          0.4426229508196721
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors"
        ],
        "margin": 24.526631,
        "reverse_margin": 24.648887
      },
      "new": "00aed528",
      "score": 41.68828
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.22388059701492538,
          0.24725274725274726
        ],
        "cfg_coverage": [
          0.1864406779661017,
          0.24444444444444444
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -24.526631,
        "reverse_margin": 17.161649
      },
      "new": "00921cc4",
      "score": 17.161649
    },
    {
      "eligible": false,
      "evidence": {
        "coverage": [
          0.13432835820895522,
          0.1534090909090909
        ],
        "cfg_coverage": [
          0.13559322033898305,
          0.13559322033898305
        ],
        "mapped_data": 0,
        "held": [
          "instruction_coverage",
          "cfg_coverage",
          "unexplained_entry_return_or_effect_position",
          "insufficient_independent_call_anchors",
          "already_matched_elsewhere"
        ],
        "margin": -30.916714,
        "reverse_margin": 10.771566
      },
      "new": "009ba7c0",
      "score": 10.771566
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-2f587424cf193cfa3ee51844e209c666"></a>

### v15.7.4 [`00a8e510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e510.md) FUN_00a8e510

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed93c.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / 0.0 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors
- 2. [`00aed968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed968.md) · スコア 0.0 · 採用条件未達 · 順位差 0.0 / -47.692308 · short_function_requires_other_identity_evidence, instruction_coverage, cfg_coverage, unexplained_entry_return_or_effect_position, insufficient_independent_call_anchors

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
      "new": "00aed93c",
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
        "margin": 0.0,
        "reverse_margin": -47.692308
      },
      "new": "00aed968",
      "score": 0.0
    }
  ],
  "ranking_method": "instruction_blocks"
}
~~~

<a id="review-ae84f5546a85710ac010d1bfede88829"></a>

### v15.7.4 [`00a8e52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8e/00a8e52c.md) FUN_00a8e52c

`competing_candidates` 

呼出元 0件  · 呼出先 0件 

- 1. [`00aed958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed958.md) · スコア 79.0 · 採用条件未達 · 順位差 76.6 / 76.6 · 
- 2. [`00aed99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed99c.md) · スコア 2.4 · 採用条件未達 · 順位差 — / — · 
- 3. [`00aed93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed93c.md) · スコア 1.7143 · 採用条件未達 · 順位差 — / — · 
- 4. [`00aed524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed524.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 5. [`00aed964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed964.md) · スコア 1.3333 · 採用条件未達 · 順位差 — / — · 
- 6. [`00aed968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed968.md) · スコア 0.9231 · 採用条件未達 · 順位差 — / — · 
- 7. [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) · スコア 0.0597 · 採用条件未達 · 順位差 — / — · 

~~~json
{
  "initial_reason": "insufficient_independent_evidence",
  "order": "score_descending_then_address",
  "ranked_candidates": [
    {
      "eligible": "",
      "evidence": {
        "margin": 76.6,
        "reverse_margin": 76.6
      },
      "new": "00aed958",
      "score": 79.0
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed99c",
      "score": 2.4
    },
    {
      "eligible": "",
      "evidence": {},
      "new": "00aed93c",
      "score": 1.7143
    }
  ],
  "ranking_method": "initial_matcher"
}
~~~

