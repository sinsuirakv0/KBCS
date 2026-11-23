# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (12)

[一覧の目次](README.md)

<a id="compare-5579bed3bfbf2e905d41011902ce4d49"></a>

### [`0097648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/0097648c.md) → [`009abf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md) FUN_009abf70

採用 · 移動量 `+0x35ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`009764c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009764c4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`009abfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abfa8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009764b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009abf98"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009764b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "009abfa8"
      ]
    ]
  ],
  "added": [
    [
      "009abf98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "009abfa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009764b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/0097648c.md#insn-009764b4) · [`00976498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/0097648c.md#insn-00976498)
- 新版 [`009abf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md#insn-009abf98) · [`009abf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md#insn-009abf7c)

~~~diff
- 009764b4 ["INT_ADD", "register:40f0:8", ["const:9764b4:8", "const:4:8"]]
- 009764b4 ["CALL", null, ["callee:009abfa8:8"]]
- 009764b4 bytes 04000094
+ 009abf98 ["INT_ADD", "register:40f0:8", ["const:9abf98:8", "const:4:8"]]
+ 009abf98 ["CALL", null, ["callee:009abfa8:8"]]
+ 009abf98 bytes 04000094
- 00976498 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00976498 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00976498 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00976498 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 009abf7c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 009abf7c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 009abf7c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 009abf7c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00976498 bytes 08010037
+ 009abf7c bytes 08010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2053c19cd1d2e60861d9f6a8c092c24"></a>

### [`009764c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009764c4.md) → [`009abfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abfa8.md) FUN_009abfa8

採用 · 移動量 `+0x35ae4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/0097648c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009abf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abf70.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 53.85% / 新版 48.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00976508"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097651c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009abfec"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00976508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac01c"
      ]
    ],
    [
      "unmatched:0097651c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac018"
      ]
    ]
  ],
  "added": [
    [
      "009abfec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac01c"
      ]
    ],
    [
      "009ac000",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac018"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00976508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009764c4.md#insn-00976508) · [`0097651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009764c4.md#insn-0097651c)
- 新版 [`009abfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ab/009abfa8.md#insn-009abfec)

~~~diff
- 00976508 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00976508 bytes 80010054
- 0097651c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0097651c bytes c0000054
+ 009abfec ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 009abfec bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7bbb0cafb2a034a24cdd7734756250"></a>

### [`00976b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976b78.md) → [`009ac65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md) FUN_009ac65c

採用 · 移動量 `+0x35ae4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083af18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083af18.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0086d204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d204.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 53.33% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00976ba0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ac684"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00976ba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac698"
      ]
    ]
  ],
  "added": [
    [
      "009ac684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac698"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00976ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976b78.md#insn-00976ba0) · [`00976b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976b78.md#insn-00976b8c)
- 新版 [`009ac684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md#insn-009ac684) · [`009ac670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac65c.md#insn-009ac670)

~~~diff
- 00976ba0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00976ba0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00976ba0 bytes a1000054
+ 009ac684 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009ac684 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 009ac684 bytes a1000054
- 00976b8c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00976b8c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 009ac670 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 009ac670 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00976b8c bytes b50300b4
+ 009ac670 bytes b50300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9fe75d4511abb085d03ae70a2765838"></a>

### [`00976c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976c10.md) → [`009ac6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac6f4.md) FUN_009ac6f4

採用 · 移動量 `+0x35ae4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 31.25% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00976c48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00976c50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ac72c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ac71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00976c4c"
      ]
    ],
    [
      "unmatched:00976c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac764"
      ]
    ],
    [
      "unmatched:00976c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac724"
      ]
    ]
  ],
  "added": [
    [
      "009ac71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac730"
      ]
    ],
    [
      "009ac72c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac764"
      ]
    ],
    [
      "009ac734",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac724"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00976c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976c10.md#insn-00976c48) · [`00976c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976c10.md#insn-00976c50)
- 新版 [`009ac72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac6f4.md#insn-009ac72c)

~~~diff
- 00976c48 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00976c48 bytes c0010054
- 00976c50 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00976c50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00976c50 bytes 94ffffb4
+ 009ac72c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 009ac72c bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e49dfa9f6f72f7ea3e76f915c575d2"></a>

### [`00976ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976ca8.md) → [`009ac78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac78c.md) FUN_009ac78c

採用 · 移動量 `+0x35ae4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 6件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0097fefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fefc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 6件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`009b59dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b59dc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 26.32% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00976cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009ac7b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00976d08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00976cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00976d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac7fc"
      ]
    ],
    [
      "unmatched:00976d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac884"
      ]
    ]
  ],
  "added": [
    [
      "009ac7b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009ac7ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac7fc"
      ]
    ],
    [
      "009ac844",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ac884"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00976cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976ca8.md#insn-00976cd0) · [`00976d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976ca8.md#insn-00976d08) · [`00976d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976ca8.md#insn-00976d44)

~~~diff
- 00976cd0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00976cd0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00976cd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00976cd0 bytes a8831ff8
- 00976d08 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00976d08 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00976d08 bytes 940000b4
- 00976d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00976d44 ["INT_ADD", "register:40f0:8", ["const:976d44:8", "const:4:8"]]
- 00976d44 ["CALLIND", null, ["register:0:8"]]
- 00976d44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f4f60f74cd1c2b1fc2150a16c88f09"></a>

### [`00977ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977ad4.md) → [`009ad5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad5b4.md) FUN_009ad5b4

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a198.md) · 呼出先 3件 [`0097e4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4d8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`007644a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md) · 呼出先 3件 [`009b3fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fb8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.67% / 新版 90.67%

CFGの説明率　旧版 77.42% / 新版 82.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00977b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00977b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ad5f0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00977b10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad610"
      ]
    ],
    [
      "unmatched:00977b28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad5e4"
      ]
    ]
  ],
  "added": [
    [
      "009ad5f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad610"
      ]
    ],
    [
      "009ad608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad5e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00977b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977ad4.md#insn-00977b10) · [`00977b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977ad4.md#insn-00977b28)
- 新版 [`009ad5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad5b4.md#insn-009ad5f0)

~~~diff
- 00977b10 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00977b10 bytes 00010054
- 00977b28 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00977b28 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00977b28 bytes e3feff54
+ 009ad5f0 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 009ad5f0 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-177972386ab784fd1497f0a688839c52"></a>

### [`00977c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md) → [`009ad6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad6e0.md) FUN_009ad6e0

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) · 呼出先 7件 [`0097ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ea24.md) [`00980028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980028.md) [`009800d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009800d8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) · 呼出先 7件 [`009b4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md) [`009b5b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b08.md) [`009b5bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5bb8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 45.83% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977c08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00977c04",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00977c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00977c0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ad6e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009ad6e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009ad6ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00977c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md#insn-00977c04) · [`00977c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md#insn-00977c08) · [`00977c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md#insn-00977c0c)

~~~diff
- 00977c04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00977c04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00977c04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00977c04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00977c04 bytes fd7b02a9
- 00977c08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00977c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00977c08 bytes f71b00f9
- 00977c0c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00977c0c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00977c0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00977c0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00977c0c bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9262523eaece56e4f47fc39724648f19"></a>

### [`00977d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md) → [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) FUN_009ad7e4

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 11件 [`0073a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a198.md) [`007684b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/007684b4.md) [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) [`0097a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a22c.md) [`00982ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982ed4.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0097c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c214.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 11件 [`007644a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md) [`00792988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792988.md) [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) [`009afd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afd0c.md) [`009b89b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`009b1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1cf4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.83% / 新版 73.83%

CFGの説明率　旧版 23.68% / 新版 22.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00977d3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00977d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009ad828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00977d8c"
      ]
    ],
    [
      "unmatched:00977d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad82c"
      ]
    ]
  ],
  "added": [
    [
      "009ad814",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009ad828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad86c"
      ]
    ],
    [
      "009ad868",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ad82c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00977d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md#insn-00977d34) · [`00977d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md#insn-00977d3c) · [`00977d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md#insn-00977d40)

~~~diff
- 00977d34 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00977d34 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00977d34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00977d34 bytes a8831ff8
- 00977d3c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00977d3c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00977d3c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00977d3c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00977d3c bytes 7f7e00a9
- 00977d40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00977d40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00977d40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00977d40 bytes 7f0a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4cdce9453d8c5681f7c28ed9dff3f60"></a>

### [`00978390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978390.md) → [`009ade70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ade70.md) FUN_009ade70

採用 · 移動量 `+0x35ae0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) · 呼出先 6件 [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) [`00980028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980028.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · 呼出先 6件 [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) [`009b5b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b08.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 85.00% / 新版 89.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0097840c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009adeec"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097840c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009adeec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978390.md#insn-0097840c) · [`009783c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978390.md#insn-009783c0)
- 新版 [`009adeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ade70.md#insn-009adeec) · [`009adea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ade70.md#insn-009adea0)

~~~diff
- 0097840c ["COPY", "register:0:8", ["register:4040:8"]]
- 0097840c ["INT_ADD", "register:40f0:8", ["const:97840c:8", "const:4:8"]]
- 0097840c ["CALLIND", null, ["register:0:8"]]
- 0097840c bytes 00013fd6
+ 009adeec ["COPY", "register:0:8", ["register:4040:8"]]
+ 009adeec ["INT_ADD", "register:40f0:8", ["const:9adeec:8", "const:4:8"]]
+ 009adeec ["CALLIND", null, ["register:0:8"]]
+ 009adeec bytes 00013fd6
- 009783c0 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 009adea0 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 009783c0 bytes 60030054
+ 009adea0 bytes 60030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4bcb9a147f8a5f812545c9b2365375"></a>

### [`009784b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009784b4.md) → [`009adf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adf94.md) FUN_009adf94

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005edb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ed/005edb40.md) · 呼出先 6件 [`0097deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097deec.md) [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) · 呼出先 6件 [`009b39cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md) [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 63.16% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00978598"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ae078"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00978598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ae0cc"
      ]
    ],
    [
      "unmatched:009785b4",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ae078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ae0cc"
      ]
    ],
    [
      "009ae094",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00978598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009784b4.md#insn-00978598) · [`009784e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009784b4.md#insn-009784e8)
- 新版 [`009ae078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adf94.md#insn-009ae078) · [`009adfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adf94.md#insn-009adfc8)

~~~diff
- 00978598 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00978598 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00978598 bytes a1020054
+ 009ae078 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009ae078 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 009ae078 bytes a1020054
- 009784e8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 009adfc8 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 009784e8 bytes a0030054
+ 009adfc8 bytes a0030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35ccf218d2c00f8aff298a1ba30c52ab"></a>

### [`00978c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978c88.md) → [`009ae768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae768.md) FUN_009ae768

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00978cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ae7b4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00978cd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ae7c4"
      ]
    ]
  ],
  "added": [
    [
      "009ae7b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ae7c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00978cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978c88.md#insn-00978cd4) · [`00978ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978c88.md#insn-00978ca8)
- 新版 [`009ae7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae768.md#insn-009ae7b4) · [`009ae788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae768.md#insn-009ae788)

~~~diff
- 00978cd4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00978cd4 bytes 80000054
+ 009ae7b4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 009ae7b4 bytes 80000054
- 00978ca8 ["INT_ADD", "register:40f0:8", ["const:978ca8:8", "const:4:8"]]
- 00978ca8 ["CALL", null, ["callee:00c538e0:8"]]
+ 009ae788 ["INT_ADD", "register:40f0:8", ["const:9ae788:8", "const:4:8"]]
+ 009ae788 ["CALL", null, ["callee:00c538e0:8"]]
- 00978ca8 bytes 7a780994
+ 009ae788 bytes 56940a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9771a75a0a422e722e5600fe52d01955"></a>

### [`00978d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md) → [`009ae7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae7ec.md) FUN_009ae7ec

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 10件 [`0097ca5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca5c.md) [`0097ca60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca60.md) [`0097deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097deec.md) [`00980028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980028.md) [`00980038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980038.md)
- 新版 呼出元 1件 [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 10件 [`009b253c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b253c.md) [`009b2540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2540.md) [`009b39cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md) [`009b5b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b08.md) [`009b5b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b18.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.75% / 新版 83.75%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978d14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00978d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00978d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00978d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ae7f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009ae7f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009ae7f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00978d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md#insn-00978d10) · [`00978d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md#insn-00978d14) · [`00978d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md#insn-00978d18)

~~~diff
- 00978d10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00978d10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00978d10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00978d10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00978d10 bytes fd7b05a9
- 00978d14 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00978d14 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00978d14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00978d14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00978d14 bytes fa6706a9
- 00978d18 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00978d18 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00978d18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00978d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00978d18 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941bbb1141e6490c0cd71ebc0915b7c0"></a>

### [`00979848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979848.md) → [`009af328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af328.md) FUN_009af328

採用 · 移動量 `+0x35ae0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 6件 [`009750ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009750ec.md) [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 6件 [`009aabd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aabd0.md) [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 83.33% / 新版 74.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009798d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009af3b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00979954"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00979948",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097994c",
      "DATA",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009798d4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009af428",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009af42c",
      "DATA",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009af3b4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009798d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979848.md#insn-009798d4) · [`00979954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979848.md#insn-00979954)
- 新版 [`009af3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af328.md#insn-009af3b4)

~~~diff
- 009798d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009798d4 ["INT_ADD", "register:40f0:8", ["const:9798d4:8", "const:4:8"]]
- 009798d4 ["CALLIND", null, ["register:0:8"]]
- 009798d4 bytes 00013fd6
- 00979954 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00979954 ["RETURN", null, ["register:0:8"]]
- 00979954 bytes c0035fd6
+ 009af3b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009af3b4 ["INT_ADD", "register:40f0:8", ["const:9af3b4:8", "const:4:8"]]
+ 009af3b4 ["CALLIND", null, ["register:0:8"]]
+ 009af3b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed705b8322601f118e770a9f6f4b7d8"></a>

### [`00979980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979980.md) → [`009af460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af460.md) FUN_009af460

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 2件 [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) [`009800a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009800a0.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 2件 [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) [`009b5b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009799bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009af49c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009799bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009af484"
      ]
    ]
  ],
  "added": [
    [
      "009af49c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009af484"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009799bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979980.md#insn-009799bc) · [`00979998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979980.md#insn-00979998)
- 新版 [`009af49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af460.md#insn-009af49c) · [`009af478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af460.md#insn-009af478)

~~~diff
- 009799bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009799bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 009799bc bytes 41ffff54
+ 009af49c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009af49c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 009af49c bytes 41ffff54
- 00979998 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 009af478 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00979998 bytes 40010054
+ 009af478 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c357203de0fc54ba77fb506fc88b84c"></a>

### [`0097a1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a1a8.md) → [`009afc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afc88.md) FUN_009afc88

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 33.33% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a1f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009afcd0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097a1f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009afce4"
      ]
    ]
  ],
  "added": [
    [
      "009afcd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009afce4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097a1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a1a8.md#insn-0097a1f0) · [`0097a1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a1a8.md#insn-0097a1c4)
- 新版 [`009afcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afc88.md#insn-009afcd0) · [`009afca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009afc88.md#insn-009afca4)

~~~diff
- 0097a1f0 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0097a1f0 bytes a0000054
+ 009afcd0 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 009afcd0 bytes a0000054
- 0097a1c4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 009afca4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0097a1c4 bytes 80000054
+ 009afca4 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f76affb4f6e2b84397e332bfc4a5861"></a>

### [`0097a858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a858.md) → [`009b0338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b0/009b0338.md) FUN_009b0338

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00837f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837f3c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a864"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097a860",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097a864",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b0340",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b0344",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097a860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a858.md#insn-0097a860) · [`0097a864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a858.md#insn-0097a864)
- 新版 [`009b0340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b0/009b0338.md#insn-009b0340)

~~~diff
- 0097a860 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097a860 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097a860 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0097a860 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0097a860 bytes fd7bbea9
- 0097a864 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0097a864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0097a864 bytes f30b00f9
+ 009b0340 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009b0340 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009b0340 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 009b0340 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009b0340 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375c2debdca2dce4bdf26f311cbcdb56"></a>

### [`0097c160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c160.md) → [`009b1c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1c40.md) FUN_009b1c40

採用 · 移動量 `+0x35ae0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009772ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/009772ec.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009acdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acdcc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c1bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b1c9c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1cd4"
      ]
    ]
  ],
  "added": [
    [
      "009b1c9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1cd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c160.md#insn-0097c1bc) · [`0097c1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c160.md#insn-0097c1ac)
- 新版 [`009b1c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1c40.md#insn-009b1c9c) · [`009b1c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1c40.md#insn-009b1c8c)

~~~diff
- 0097c1bc ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0097c1bc bytes c0010054
+ 009b1c9c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 009b1c9c bytes c0010054
- 0097c1ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097c1ac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 009b1c8c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009b1c8c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0097c1ac bytes a1000054
+ 009b1c8c bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0024ccb7b72f4f8e51b97dbe7fdc58"></a>

### [`0097c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c214.md) → [`009b1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1cf4.md) FUN_009b1cf4

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00977d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md) [`00a40cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a40/00a40cf4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md) [`00a9ebf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ebf0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b1cf4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c214",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c220",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0097c224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "009b1cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b1d00",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "009b1d04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c214.md#insn-0097c214) · [`0097c224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c214.md#insn-0097c224)
- 新版 [`009b1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1cf4.md#insn-009b1cf4)

~~~diff
- 0097c214 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097c214 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097c214 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0097c214 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0097c214 bytes fd7bbfa9
- 0097c224 ["INT_ADD", "register:40f0:8", ["const:97c224:8", "const:4:8"]]
- 0097c224 ["CALL", null, ["ram:418c38:8"]]
- 0097c224 bytes 8572ea97
+ 009b1cf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009b1cf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009b1cf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 009b1cf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009b1cf4 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ba4bbfaff0d20fb88232ce0355b778"></a>

### [`0097c490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c490.md) → [`009b1f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1f70.md) FUN_009b1f70

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0097c4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c490.md#insn-0097c4b0) · [`0097c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c490.md#insn-0097c4c4) · [`0097c4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c490.md#insn-0097c4cc)
- 新版 [`009b1f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1f70.md#insn-009b1f90) · [`009b1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1f70.md#insn-009b1fa4) · [`009b1fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1f70.md#insn-009b1fac)

~~~diff
- 0097c4b0 ["INT_ADD", "register:40f0:8", ["const:97c4b0:8", "const:4:8"]]
- 0097c4b0 ["CALL", null, ["callee:00c538e0:8"]]
+ 009b1f90 ["INT_ADD", "register:40f0:8", ["const:9b1f90:8", "const:4:8"]]
+ 009b1f90 ["CALL", null, ["callee:00c538e0:8"]]
- 0097c4b0 bytes 786a0994
+ 009b1f90 bytes 54860a94
- 0097c4c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0097c4c4 ["INT_ADD", "register:40f0:8", ["const:97c4c4:8", "const:4:8"]]
- 0097c4c4 ["CALLIND", null, ["register:0:8"]]
+ 009b1fa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b1fa4 ["INT_ADD", "register:40f0:8", ["const:9b1fa4:8", "const:4:8"]]
+ 009b1fa4 ["CALLIND", null, ["register:0:8"]]
- 0097c4c4 bytes 00013fd6
+ 009b1fa4 bytes 00013fd6
- 0097c4cc ["INT_ADD", "register:40f0:8", ["const:97c4cc:8", "const:4:8"]]
- 0097c4cc ["CALL", null, ["callee:00c57a80:8"]]
+ 009b1fac ["INT_ADD", "register:40f0:8", ["const:9b1fac:8", "const:4:8"]]
+ 009b1fac ["CALL", null, ["callee:00c57a80:8"]]
- 0097c4cc bytes d97a0994
+ 009b1fac bytes b5960a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73846b0e3be8d89388484881d3e0e8db"></a>

### [`0097c514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c514.md) → [`009b1ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1ff4.md) FUN_009b1ff4

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009ae0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae0d0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c548"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009b2028"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c548",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009b2028",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c514.md#insn-0097c548) · [`0097c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c514.md#insn-0097c528)
- 新版 [`009b2028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1ff4.md#insn-009b2028) · [`009b2008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1ff4.md#insn-009b2008)

~~~diff
- 0097c548 ["COPY", "register:0:8", ["register:4040:8"]]
- 0097c548 ["INT_ADD", "register:40f0:8", ["const:97c548:8", "const:4:8"]]
- 0097c548 ["CALLIND", null, ["register:0:8"]]
- 0097c548 bytes 00013fd6
+ 009b2028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b2028 ["INT_ADD", "register:40f0:8", ["const:9b2028:8", "const:4:8"]]
+ 009b2028 ["CALLIND", null, ["register:0:8"]]
+ 009b2028 bytes 00013fd6
- 0097c528 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0097c528 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 009b2008 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 009b2008 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0097c528 bytes 740100b4
+ 009b2008 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-129ce01a935d5f81b8be2ec5d7d81921"></a>

### [`0097c764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c764.md) → [`009b2244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2244.md) FUN_009b2244

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c77c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b225c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c77c",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097c780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2270"
      ]
    ]
  ],
  "added": [
    [
      "009b225c",
      "DATA",
      [
        "storage",
        "00c88780",
        null,
        "undefined *"
      ]
    ],
    [
      "009b2260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c764.md#insn-0097c77c) · [`0097c780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c764.md#insn-0097c780)
- 新版 [`009b225c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2244.md#insn-009b225c)

~~~diff
- 0097c77c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0097c77c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0097c77c bytes 0a0100f9
- 0097c780 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0097c780 bytes 80000054
+ 009b225c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b225c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b225c bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de6c5bff87b4afdb8fb7b32166a1dedd"></a>

### [`0097c7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c7a8.md) → [`009b2288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2288.md) FUN_009b2288

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c7cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b22ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c7d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c7cc",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097c7d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b22c0"
      ]
    ]
  ],
  "added": [
    [
      "009b22ac",
      "DATA",
      [
        "storage",
        "00c88780",
        null,
        "undefined *"
      ]
    ],
    [
      "009b22b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b22c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c7a8.md#insn-0097c7cc) · [`0097c7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c7a8.md#insn-0097c7d0)
- 新版 [`009b22ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2288.md#insn-009b22ac)

~~~diff
- 0097c7cc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0097c7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097c7cc bytes 680200f9
- 0097c7d0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0097c7d0 bytes 80000054
+ 009b22ac ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 009b22ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b22ac bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe8a6e754fda340688844cd0e5c6013"></a>

### [`0097c804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c804.md) → [`009b22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b22e4.md) FUN_009b22e4

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c804",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c808",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c830",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b22e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b22e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b2310",
      "DATA",
      [
        "storage",
        "00c88780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c804.md#insn-0097c804) · [`0097c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c804.md#insn-0097c808) · [`0097c830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c804.md#insn-0097c830)

~~~diff
- 0097c804 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097c804 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097c804 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0097c804 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0097c804 bytes fd7bbea9
- 0097c808 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097c808 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097c808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097c808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097c808 bytes f44f01a9
- 0097c830 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0097c830 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0097c830 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0097c830 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0097c830 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b5860d2edbe37fcbd1ae16aa1efaec"></a>

### [`0097c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c938.md) → [`009b2418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2418.md) FUN_009b2418

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009ae0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae0d0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c93c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c938",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c93c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2444"
      ]
    ]
  ],
  "added": [
    [
      "009b2418",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b241c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b2434",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c938.md#insn-0097c938) · [`0097c93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c938.md#insn-0097c93c) · [`0097c954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c938.md#insn-0097c954)

~~~diff
- 0097c938 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097c938 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097c938 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0097c938 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0097c938 bytes fd7bbea9
- 0097c93c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0097c93c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0097c93c bytes f30b00f9
- 0097c954 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0097c954 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be0e6f66553b7f8563ea2d2e3a3447e"></a>

### [`0097c988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c988.md) → [`009b2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2468.md) FUN_009b2468

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 75.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c98c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c98c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c990"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c98c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097c990",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b246c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b2470",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c988.md#insn-0097c98c) · [`0097c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c988.md#insn-0097c990)
- 新版 [`009b246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2468.md#insn-009b246c)

~~~diff
- 0097c98c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097c98c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097c98c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097c98c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097c98c bytes fd7b01a9
- 0097c990 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 0097c990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0097c990 bytes f31300f9
+ 009b246c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009b246c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009b246c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 009b246c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009b246c bytes fd7b01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f0d476390dbeb1af3042b9db3252e3"></a>

### [`0097ca94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca94.md) → [`009b2574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2574.md) FUN_009b2574

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097caac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b258c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097caac",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097cab0",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b258c",
      "DATA",
      [
        "storage",
        "00c88880",
        null,
        "undefined *"
      ]
    ],
    [
      "009b2590",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097caac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca94.md#insn-0097caac) · [`0097cab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca94.md#insn-0097cab4)
- 新版 [`009b258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2574.md#insn-009b258c)

~~~diff
- 0097caac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0097caac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097caac bytes 080000f9
- 0097cab4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0097cab4 ["RETURN", null, ["register:0:8"]]
- 0097cab4 bytes c0035fd6
+ 009b258c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009b258c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b258c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08aa8af7d803b4d950f437ab1d180b58"></a>

### [`0097cad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cad0.md) → [`009b25b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b25b0.md) FUN_009b25b0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0097caf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009b25d4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097caf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "009b25d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097caf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cad0.md#insn-0097caf4) · [`0097cad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cad0.md#insn-0097cad8)
- 新版 [`009b25d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b25b0.md#insn-009b25d4) · [`009b25b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b25b0.md#insn-009b25b8)

~~~diff
- 0097caf4 ["INT_ADD", "register:40f0:8", ["const:97caf4:8", "const:4:8"]]
- 0097caf4 ["CALL", null, ["ram:457e1c:8"]]
- 0097caf4 bytes ca6ceb97
+ 009b25d4 ["INT_ADD", "register:40f0:8", ["const:9b25d4:8", "const:4:8"]]
+ 009b25d4 ["CALL", null, ["ram:47acb4:8"]]
+ 009b25d4 bytes b821eb97
- 0097cad8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097cad8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 009b25b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009b25b8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0097cad8 bytes e1010054
+ 009b25b8 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4f30badafd774f7690594bc33b8d33"></a>

### [`0097cb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb44.md) → [`009b2624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2624.md) FUN_009b2624

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cb5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b263c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cb64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097cb5c",
      "DATA",
      [
        "storage",
        "00c0aa28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097cb60",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b263c",
      "DATA",
      [
        "storage",
        "00c88900",
        null,
        "undefined *"
      ]
    ],
    [
      "009b2640",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb44.md#insn-0097cb5c) · [`0097cb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb44.md#insn-0097cb64)
- 新版 [`009b263c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2624.md#insn-009b263c)

~~~diff
- 0097cb5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0097cb5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097cb5c bytes 080000f9
- 0097cb64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0097cb64 ["RETURN", null, ["register:0:8"]]
- 0097cb64 bytes c0035fd6
+ 009b263c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009b263c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b263c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40c2b40d3f417214478782266312c2eb"></a>

### [`0097cc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cc18.md) → [`009b26f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b26f8.md) FUN_009b26f8

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cc1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cc1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097cc40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097cc1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097cc40",
      "DATA",
      [
        "storage",
        "00c0aaa8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097cc44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2734"
      ]
    ]
  ],
  "added": [
    [
      "009b26fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b2720",
      "DATA",
      [
        "storage",
        "00c88980",
        null,
        "undefined *"
      ]
    ],
    [
      "009b2724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2734"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cc18.md#insn-0097cc1c) · [`0097cc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cc18.md#insn-0097cc40) · [`0097cc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cc18.md#insn-0097cc44)

~~~diff
- 0097cc1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097cc1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097cc1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097cc1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097cc1c bytes f44f01a9
- 0097cc40 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0097cc40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097cc40 bytes 680200f9
- 0097cc44 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0097cc44 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6188b1f3294d2aafdbbba6f211f92fb5"></a>

### [`0097fe14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fe14.md) → [`009b58f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md) FUN_009b58f4

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097fe4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b592c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097fe28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097fe28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b595c"
      ]
    ],
    [
      "unmatched:0097fe4c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b595c"
      ]
    ],
    [
      "009b592c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097fe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fe14.md#insn-0097fe28) · [`0097fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fe14.md#insn-0097fe4c)
- 新版 [`009b5908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md#insn-009b5908)

~~~diff
- 0097fe28 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0097fe28 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0097fe28 bytes b30200b4
- 0097fe4c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0097fe4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097fe4c bytes 680200f9
+ 009b5908 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 009b5908 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 009b5908 bytes b30200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d920a1ddc2a0137385b96e20d1afc0"></a>

### [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md) → [`009b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md) FUN_009b5af8

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`009772ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/009772ec.md) [`00977efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977efc.md) [`00978008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978008.md) [`00978140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978140.md) [`0097826c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/0097826c.md) · 呼出先 1件 [`00973ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973ae0.md)
- 新版 呼出元 10件 [`009acdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009acdcc.md) [`009ad9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9dc.md) [`009adae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adae8.md) [`009adc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md) [`009add4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009add4c.md) · 呼出先 1件 [`009a95c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95c4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098001c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5afc"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098001c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b04"
      ]
    ]
  ],
  "added": [
    [
      "009b5afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098001c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md#insn-0098001c) · [`00980018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980018.md#insn-00980018)
- 新版 [`009b5afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5af8.md#insn-009b5afc)

~~~diff
- 0098001c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0098001c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0098001c bytes 400000b4
+ 009b5afc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5afc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009b5afc bytes 400000b4
- 00980018 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00980018 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00980018 bytes 000040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eafb53207e5a9b341308c7d63c8c39d8"></a>

### [`00980038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980038.md) → [`009b5b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b18.md) FUN_009b5b18

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0097826c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/0097826c.md) [`00978d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md) · 呼出先 1件 [`00975098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975098.md)
- 新版 呼出元 2件 [`009add4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009add4c.md) [`009ae7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae7ec.md) · 呼出先 1件 [`009aab7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aab7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098003c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5b1c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098003c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b24"
      ]
    ]
  ],
  "added": [
    [
      "009b5b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098003c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980038.md#insn-0098003c) · [`00980038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980038.md#insn-00980038)
- 新版 [`009b5b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b18.md#insn-009b5b1c)

~~~diff
- 0098003c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0098003c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0098003c bytes 400000b4
+ 009b5b1c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5b1c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009b5b1c bytes 400000b4
- 00980038 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00980038 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00980038 bytes 000040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80da71f0841b616a76a92cf366384b6e"></a>

### [`00980048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980048.md) → [`009b5b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b28.md) FUN_009b5b28

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00979584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979584.md) · 呼出先 1件 [`009750a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009750a0.md)
- 新版 呼出元 1件 [`009af064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af064.md) · 呼出先 1件 [`009aab84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aab84.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098004c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5b2c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098004c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b34"
      ]
    ]
  ],
  "added": [
    [
      "009b5b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980048.md#insn-0098004c) · [`00980048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980048.md#insn-00980048)
- 新版 [`009b5b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b28.md#insn-009b5b2c)

~~~diff
- 0098004c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0098004c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0098004c bytes 400000b4
+ 009b5b2c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5b2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 009b5b2c bytes 400000b4
- 00980048 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00980048 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00980048 bytes 000040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1edfa09c00c159aa07cdc9f6e291787"></a>

### [`0098006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098006c.md) → [`009b5b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b4c.md) FUN_009b5b4c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00979350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979350.md) · 呼出先 1件 [`009750d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009750d4.md)
- 新版 呼出元 1件 [`009aee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009aee30.md) · 呼出先 1件 [`009aabb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aabb8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00980070"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5b50"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b58"
      ]
    ]
  ],
  "added": [
    [
      "009b5b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098006c.md#insn-00980070) · [`0098006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098006c.md#insn-0098006c)
- 新版 [`009b5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b4c.md#insn-009b5b50)

~~~diff
- 00980070 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00980070 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00980070 bytes 400000b4
+ 009b5b50 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5b50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009b5b50 bytes 400000b4
- 0098006c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0098006c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0098006c bytes 000040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af30e8ddc95b377f2c66dc7e875d37e7"></a>

### [`0098007c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098007c.md) → [`009b5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b5c.md) FUN_009b5b5c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009794a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/009794a8.md) · 呼出先 1件 [`009750dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009750dc.md)
- 新版 呼出元 1件 [`009aef88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009aef88.md) · 呼出先 1件 [`009aabc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aabc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00980080"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5b60"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b6c"
      ]
    ]
  ],
  "added": [
    [
      "009b5b60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098007c.md#insn-00980080) · [`0098007c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098007c.md#insn-0098007c)
- 新版 [`009b5b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5b5c.md#insn-009b5b60)

~~~diff
- 00980080 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00980080 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00980080 bytes 600000b4
+ 009b5b60 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5b60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009b5b60 bytes 600000b4
- 0098007c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0098007c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0098007c bytes 000040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-343ac8298c1c8bcd58ddecab9d1af1ac"></a>

### [`00980108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980108.md) → [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) FUN_009b5be8

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097d4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097d4b8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0058574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058574c.md) [`005857bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005857bc.md) [`005859ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md) [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 76.67% / 新版 88.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098027c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b5d5c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0098027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980108.md#insn-0098027c) · [`00980280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980108.md#insn-00980280)
- 新版 [`009b5d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md#insn-009b5d5c)

~~~diff
- 0098027c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 0098027c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0098027c bytes 0a4100f9
- 00980280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
- 00980280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00980280 bytes 001d803d
+ 009b5d5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 009b5d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b5d5c bytes 0a4100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f8def3b134264f17a1e0e0effd020c"></a>

### [`009803f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009803f0.md) → [`009b5ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5ed0.md) FUN_009b5ed0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009803f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009803f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009803f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009803f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009803f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980414",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b5ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b5ef4",
      "DATA",
      [
        "storage",
        "00c88a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009803f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009803f0.md#insn-009803f0) · [`009803f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009803f0.md#insn-009803f4) · [`00980414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009803f0.md#insn-00980414)

~~~diff
- 009803f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009803f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009803f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009803f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009803f0 bytes fd7bbea9
- 009803f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009803f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009803f4 bytes f30b00f9
- 00980414 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00980414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00980414 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86439eb4ff54414b9ec34242883f595"></a>

### [`0098044c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098044c.md) → [`009b5f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5f2c.md) FUN_009b5f2c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098044c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098044c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980450"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098044c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980450",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980478",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b5f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b5f58",
      "DATA",
      [
        "storage",
        "00c88a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098044c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098044c.md#insn-0098044c) · [`00980450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098044c.md#insn-00980450) · [`00980478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098044c.md#insn-00980478)

~~~diff
- 0098044c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098044c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098044c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0098044c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098044c bytes fd7bbea9
- 00980450 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00980450 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00980450 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00980450 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980450 bytes f44f01a9
- 00980478 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00980478 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00980478 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1915635471cf639ca28451241d8bfce2"></a>

### [`00980800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980800.md) → [`009b62e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b62e0.md) FUN_009b62e0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b62f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098081c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980818",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0098081c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b630c"
      ]
    ]
  ],
  "added": [
    [
      "009b62f8",
      "DATA",
      [
        "storage",
        "00c88a90",
        null,
        "undefined *"
      ]
    ],
    [
      "009b62fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b630c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980800.md#insn-00980818) · [`0098081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980800.md#insn-0098081c)
- 新版 [`009b62f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b62e0.md#insn-009b62f8)

~~~diff
- 00980818 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00980818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00980818 bytes 0a0100f9
- 0098081c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 0098081c bytes 80000054
+ 009b62f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b62f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b62f8 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b974a2fc2311dc2ad962291a70acf08e"></a>

### [`009808a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009808a0.md) → [`009b6380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6380.md) FUN_009b6380

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 24.24% / 新版 24.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009808a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009808a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009808a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009808a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009808a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009808cc",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6380",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b6384",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b63ac",
      "DATA",
      [
        "storage",
        "00c88a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009808a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009808a0.md#insn-009808a0) · [`009808a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009808a0.md#insn-009808a4) · [`009808cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009808a0.md#insn-009808cc)

~~~diff
- 009808a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009808a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009808a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009808a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009808a0 bytes fd7bbea9
- 009808a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009808a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009808a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009808a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009808a4 bytes f44f01a9
- 009808cc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009808cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009808cc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b40c6d836b51e5b7fe8b7cf2029ac32"></a>

### [`00980938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980938.md) → [`009b6418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6418.md) FUN_009b6418

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 50.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098093c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980938",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098093c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980950",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6418",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b641c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b6430",
      "DATA",
      [
        "storage",
        "00c88a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980938.md#insn-00980938) · [`0098093c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980938.md#insn-0098093c) · [`00980950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980938.md#insn-00980950)

~~~diff
- 00980938 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980938 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980938 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00980938 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00980938 bytes fd7bbea9
- 0098093c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0098093c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0098093c bytes f30b00f9
- 00980950 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00980950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00980950 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a481e7f97b7481dd3490c4f112d772"></a>

### [`00980a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980a48.md) → [`009b6528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6528.md) FUN_009b6528

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`009743e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/009743e4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`009a9ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9ec8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 22.22% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980a50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b652c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009b6530",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b6534",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980a48.md#insn-00980a4c) · [`00980a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980a48.md#insn-00980a50) · [`00980a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980a48.md#insn-00980a54)

~~~diff
- 00980a4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980a4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980a4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00980a4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980a4c bytes fd7b02a9
- 00980a50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00980a50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00980a50 bytes f51b00f9
- 00980a54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00980a54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00980a54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00980a54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980a54 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653cb507ee19c4351aafc8caf7ed2761"></a>

### [`00980b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b7c.md) → [`009b665c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b665c.md) FUN_009b665c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980b80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980ba0",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b665c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b6660",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b6680",
      "DATA",
      [
        "storage",
        "00c88b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b7c.md#insn-00980b7c) · [`00980b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b7c.md#insn-00980b80) · [`00980ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b7c.md#insn-00980ba0)

~~~diff
- 00980b7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980b7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980b7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00980b7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00980b7c bytes fd7bbea9
- 00980b80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00980b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00980b80 bytes f30b00f9
- 00980ba0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00980ba0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00980ba0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00980ba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980ba0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b25b231aea34c590807dcbed6c2f28"></a>

### [`00980d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980d44.md) → [`009b6824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md) FUN_009b6824

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b683c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00980d64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980d5c",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00980d60",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b683c",
      "DATA",
      [
        "storage",
        "00c88c10",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6840",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980d44.md#insn-00980d5c) · [`00980d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980d44.md#insn-00980d64)
- 新版 [`009b683c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md#insn-009b683c)

~~~diff
- 00980d5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00980d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00980d5c bytes 080000f9
- 00980d64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00980d64 ["RETURN", null, ["register:0:8"]]
- 00980d64 bytes c0035fd6
+ 009b683c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009b683c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b683c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e8b4788c897f36732a37a6a9b776a28"></a>

### [`00980dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980dac.md) → [`009b688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b688c.md) FUN_009b688c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b68a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00980dc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980dc4",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00980dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b68b8"
      ]
    ]
  ],
  "added": [
    [
      "009b68a4",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ],
    [
      "009b68a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b68b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980dac.md#insn-00980dc4) · [`00980dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980dac.md#insn-00980dc8)
- 新版 [`009b68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b688c.md#insn-009b68a4)

~~~diff
- 00980dc4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00980dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00980dc4 bytes 0a0100f9
- 00980dc8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00980dc8 bytes 80000054
+ 009b68a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b68a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b68a4 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfa56c4de59058f4f4669bff052d903c"></a>

### [`00980df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980df0.md) → [`009b68d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b68d0.md) FUN_009b68d0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980df0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980df4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980e14",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b68d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b68d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b68f4",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980df0.md#insn-00980df0) · [`00980df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980df0.md#insn-00980df4) · [`00980e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980df0.md#insn-00980e14)

~~~diff
- 00980df0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980df0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980df0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00980df0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00980df0 bytes fd7bbea9
- 00980df4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00980df4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00980df4 bytes f30b00f9
- 00980e14 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00980e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00980e14 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79eda2fdd7891b3197871501f68255a5"></a>

### [`00980f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980f8c.md) → [`009b6a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6a6c.md) FUN_009b6a6c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f1b0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 9.09% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00980fa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b6a88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00980fc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b6a98"
      ]
    ],
    [
      "unmatched:00980fc8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009b6a88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b6a98"
      ]
    ],
    [
      "009b6aa8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980f8c.md#insn-00980fa8) · [`00980fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980f8c.md#insn-00980fc8)
- 新版 [`009b6a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6a6c.md#insn-009b6a88)

~~~diff
- 00980fa8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00980fa8 bytes 80000054
- 00980fc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00980fc8 ["INT_ADD", "register:40f0:8", ["const:980fc8:8", "const:4:8"]]
- 00980fc8 ["CALLIND", null, ["register:0:8"]]
- 00980fc8 bytes 00013fd6
+ 009b6a88 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 009b6a88 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db5efdf727a167cb4b37e9165f304c47"></a>

### [`009811f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009811f8.md) → [`009b6cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6cd8.md) FUN_009b6cd8

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009811fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009811f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009811fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981224",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b6cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b6d04",
      "DATA",
      [
        "storage",
        "00c88d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009811f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009811f8.md#insn-009811f8) · [`009811fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009811f8.md#insn-009811fc) · [`00981224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009811f8.md#insn-00981224)

~~~diff
- 009811f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009811f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009811f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009811f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009811f8 bytes fd7bbea9
- 009811fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009811fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009811fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009811fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009811fc bytes f44f01a9
- 00981224 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00981224 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00981224 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00981224 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00981224 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e765aecce142570be40e335a1238338d"></a>

### [`0098137c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098137c.md) → [`009b6e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e5c.md) FUN_009b6e5c

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 22.22% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009813a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009813a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b6e80"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009813a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c]",
        null,
        null
      ]
    ],
    [
      "unmatched:009813a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009813c4",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b6e80",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c]",
        null,
        null
      ]
    ],
    [
      "009b6e84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009b6ea4",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009813a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098137c.md#insn-009813a0) · [`009813a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098137c.md#insn-009813a4) · [`009813bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098137c.md#insn-009813bc)

~~~diff
- 009813a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:4:8"]]
- 009813a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 009813a0 bytes e80700b9
- 009813a4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 009813a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 009813a4 ["COPY", "tmp:2:8", ["register:8:8"]]
- 009813a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 009813a4 bytes ff030039
- 009813bc ["COPY", "register:0:8", ["register:4040:8"]]
- 009813bc ["INT_ADD", "register:40f0:8", ["const:9813bc:8", "const:4:8"]]
- 009813bc ["CALLIND", null, ["register:0:8"]]
- 009813bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad22c313c1ddee5b178e5994b5ef5b9"></a>

### [`00981420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981420.md) → [`009b6f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6f00.md) FUN_009b6f00

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 26.32% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098144c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b6f2c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098144c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981450",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:00981460",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009b6f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b6f30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "009b6f40",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981420.md#insn-0098144c) · [`00981450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981420.md#insn-00981450) · [`00981460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981420.md#insn-00981460)

~~~diff
- 0098144c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0098144c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0098144c bytes e80700f9
- 00981450 ["INT_ADD", "register:40f0:8", ["const:981450:8", "const:4:8"]]
- 00981450 ["CALL", null, ["callee:00c57a90:8"]]
- 00981450 bytes fc660994
- 00981460 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00981460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981460 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed91ce1996dfed69e8ea6c2096dcb866"></a>

### [`009815dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009815dc.md) → [`009b70bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b70bc.md) FUN_009b70bc

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009815dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009815dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009815e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009815dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009815e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981600",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b70bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b70c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b70e0",
      "DATA",
      [
        "storage",
        "00c88d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009815dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009815dc.md#insn-009815dc) · [`009815e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009815dc.md#insn-009815e0) · [`00981600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009815dc.md#insn-00981600)

~~~diff
- 009815dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009815dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009815dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009815dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009815dc bytes fd7bbea9
- 009815e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009815e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009815e0 bytes f30b00f9
- 00981600 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00981600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981600 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7130c23275994577fd15313bd806f784"></a>

### [`00981638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981638.md) → [`009b7118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7118.md) FUN_009b7118

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b7144"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981664",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7164"
      ]
    ]
  ],
  "added": [
    [
      "009b7144",
      "DATA",
      [
        "storage",
        "00c88d90",
        null,
        "undefined *"
      ]
    ],
    [
      "009b7148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7164"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981638.md#insn-00981664) · [`00981668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981638.md#insn-00981668) · [`009816a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981638.md#insn-009816a8)

~~~diff
- 00981664 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00981664 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00981664 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00981664 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00981664 bytes 280401f8
- 00981668 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00981668 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00981668 bytes e00000b4
- 009816a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009816a8 ["RETURN", null, ["register:0:8"]]
- 009816a8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304193190c9e3a5ba2ff5d327a361a88"></a>

### [`009817bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009817bc.md) → [`009b729c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b729c.md) FUN_009b729c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 24.14% / 新版 24.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009817d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009817e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b72b4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009817d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:009817e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009817e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00981818"
      ]
    ]
  ],
  "added": [
    [
      "009b72b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "009b72c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009b72c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b72f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009817d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009817bc.md#insn-009817d4) · [`009817e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009817bc.md#insn-009817e0) · [`009817e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009817bc.md#insn-009817e4)

~~~diff
- 009817d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 009817d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009817d4 bytes e80700f9
- 009817e0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 009817e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009817e0 bytes e80300f9
- 009817e4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009817e4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 009817e4 bytes a00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a05241f817cc02b0264888400cca8d4"></a>

### [`0098189c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098189c.md) → [`009b737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md) FUN_009b737c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009818c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b73a0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009818c0",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b73a0",
      "DATA",
      [
        "storage",
        "00c88e10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009818c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098189c.md#insn-009818c0) · [`009818b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098189c.md#insn-009818b0)
- 新版 [`009b73a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md#insn-009b73a0) · [`009b7390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md#insn-009b7390)

~~~diff
- 009818c0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 009818c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009818c0 bytes 680200f9
+ 009b73a0 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 009b73a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b73a0 bytes 680200f9
- 009818b0 ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 009b7390 ["COPY", "register:4040:8", ["const:c88000:8"]]
- 009818b0 bytes 481400b0
+ 009b7390 bytes 881600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ee471a7817a6101a5fd439f56c71ac0"></a>

### [`00981c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c3c.md) → [`009b771c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b771c.md) FUN_009b771c

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b7734"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981c58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981c54",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7748"
      ]
    ]
  ],
  "added": [
    [
      "009b7734",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ],
    [
      "009b7738",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7748"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c3c.md#insn-00981c54) · [`00981c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c3c.md#insn-00981c58)
- 新版 [`009b7734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b771c.md#insn-009b7734)

~~~diff
- 00981c54 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00981c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00981c54 bytes 0a0100f9
- 00981c58 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00981c58 bytes 80000054
+ 009b7734 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b7734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b7734 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e6afd61a680334e3a73b4abdbf3893e"></a>

### [`00981c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c80.md) → [`009b7760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md) FUN_009b7760

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b7784"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981ca8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981ca4",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981ca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7798"
      ]
    ]
  ],
  "added": [
    [
      "009b7784",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ],
    [
      "009b7788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7798"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c80.md#insn-00981ca4) · [`00981ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c80.md#insn-00981ca8)
- 新版 [`009b7784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md#insn-009b7784)

~~~diff
- 00981ca4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00981ca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981ca4 bytes 680200f9
- 00981ca8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00981ca8 bytes 80000054
+ 009b7784 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 009b7784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b7784 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bed931ac71187a09f4199220c874f3f7"></a>

### [`00981e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e10.md) → [`009b78f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b78f0.md) FUN_009b78f0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b78f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b78f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e10.md#insn-00981e10) · [`00981e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e10.md#insn-00981e14)
- 新版 [`009b78f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b78f0.md#insn-009b78f0)

~~~diff
- 00981e10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981e10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981e10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00981e10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981e10 bytes fd7bbea9
- 00981e14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00981e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00981e14 bytes f30b00f9
+ 009b78f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009b78f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009b78f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 009b78f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009b78f0 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fa5b72493761b547129568e909d77e"></a>

### [`00981e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e60.md) → [`009b7940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7940.md) FUN_009b7940

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.03% / 新版 31.03%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981e78",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b7944",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b7948",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b7958",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e60.md#insn-00981e64) · [`00981e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e60.md#insn-00981e68) · [`00981e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981e60.md#insn-00981e78)

~~~diff
- 00981e64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981e64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981e64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00981e64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981e64 bytes fd7b01a9
- 00981e68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00981e68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00981e68 bytes f31300f9
- 00981e78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00981e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981e78 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7abea18024af6d02923b843bf2daed8"></a>

### [`00981efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981efc.md) → [`009b79dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b79dc.md) FUN_009b79dc

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b79f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981f14",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981f18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a08"
      ]
    ]
  ],
  "added": [
    [
      "009b79f4",
      "DATA",
      [
        "storage",
        "00c88f10",
        null,
        "undefined *"
      ]
    ],
    [
      "009b79f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981efc.md#insn-00981f14) · [`00981f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981efc.md#insn-00981f18)
- 新版 [`009b79f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b79dc.md#insn-009b79f4)

~~~diff
- 00981f14 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00981f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00981f14 bytes 0a0100f9
- 00981f18 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00981f18 bytes 80000054
+ 009b79f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b79f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009b79f4 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c85ead1bf6dd43231d0faff7bfa079"></a>

### [`00981f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981f40.md) → [`009b7a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7a20.md) FUN_009b7a20

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b7a44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981f64",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00981f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a58"
      ]
    ]
  ],
  "added": [
    [
      "009b7a44",
      "DATA",
      [
        "storage",
        "00c88f10",
        null,
        "undefined *"
      ]
    ],
    [
      "009b7a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981f40.md#insn-00981f64) · [`00981f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981f40.md#insn-00981f68)
- 新版 [`009b7a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7a20.md#insn-009b7a44)

~~~diff
- 00981f64 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00981f64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981f64 bytes 680200f9
- 00981f68 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00981f68 bytes 80000054
+ 009b7a44 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 009b7a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009b7a44 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bee91edd8922a8ac228fc419f1e0d533"></a>

### [`009820d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009820d0.md) → [`009b7bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7bb0.md) FUN_009b7bb0

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 71.43% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009820ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b7bcc"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009820ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7bdc"
      ]
    ]
  ],
  "added": [
    [
      "009b7bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7bdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009820ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009820d0.md#insn-009820ec) · [`009820e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009820d0.md#insn-009820e8)
- 新版 [`009b7bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7bb0.md#insn-009b7bcc)

~~~diff
- 009820ec ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 009820ec bytes 80000054
+ 009b7bcc ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 009b7bcc bytes 80000054
- 009820e8 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4000:8"]]
- 009820e8 ["INT_SBORROW", "register:106:1", ["register:4000:8", "register:4048:8"]]
- 009820e8 ["INT_SUB", "tmp:0:8", ["register:4000:8", "register:4048:8"]]
- 009820e8 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 009820e8 bytes 1f0009eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b9d2ac7c593b28bc0351c926bc67a5"></a>

### [`009824b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009824b4.md) → [`009b7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7f94.md) FUN_009b7f94

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4e8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009824b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009824b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009824b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009824b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009824b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b7f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b7f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009824b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009824b4.md#insn-009824b4) · [`009824b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009824b4.md#insn-009824b8)
- 新版 [`009b7f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7f94.md#insn-009b7f94)

~~~diff
- 009824b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009824b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009824b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009824b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009824b4 bytes fd7bbea9
- 009824b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009824b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009824b8 bytes f30b00f9
+ 009b7f94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009b7f94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009b7f94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 009b7f94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009b7f94 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59214132d9a540e14669550632789d3"></a>

### [`00982504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982504.md) → [`009b7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md) FUN_009b7fe4

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 37.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0098253c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009b801c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0098255c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098253c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009b801c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098253c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982504.md#insn-0098253c) · [`0098255c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982504.md#insn-0098255c)
- 新版 [`009b801c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7fe4.md#insn-009b801c)

~~~diff
- 0098253c ["COPY", "register:0:8", ["register:4040:8"]]
- 0098253c ["INT_ADD", "register:40f0:8", ["const:98253c:8", "const:4:8"]]
- 0098253c ["CALLIND", null, ["register:0:8"]]
- 0098253c bytes 00013fd6
- 0098255c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0098255c ["RETURN", null, ["register:0:8"]]
- 0098255c bytes c0035fd6
+ 009b801c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b801c ["INT_ADD", "register:40f0:8", ["const:9b801c:8", "const:4:8"]]
+ 009b801c ["CALLIND", null, ["register:0:8"]]
+ 009b801c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f85239a0edbded3907f7cd69451e177"></a>

### [`009843fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843fc.md) → [`009b9edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9edc.md) FUN_009b9edc

採用 · 移動量 `+0x35ae0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b9f00"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00984420",
      "DATA",
      [
        "storage",
        "00c0b1b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00984424",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00984428",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b9f00",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ],
    [
      "009b9f04",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b9f08",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843fc.md#insn-00984420) · [`0098442c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009843fc.md#insn-0098442c)
- 新版 [`009b9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9edc.md#insn-009b9f00)

~~~diff
- 00984420 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00984420 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00984420 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00984420 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00984420 bytes 082400a9
- 0098442c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0098442c ["RETURN", null, ["register:0:8"]]
- 0098442c bytes c0035fd6
+ 009b9f00 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009b9f00 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009b9f00 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009b9f00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009b9f00 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6729e9ac356ee9dca12b2fad644f1d3"></a>

### [`00984700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984700.md) → [`009ba1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1e0.md) FUN_009ba1e0

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00983810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983810.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009b92f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b92f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00984718"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009ba1f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00984720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00984718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0098472c"
      ]
    ],
    [
      "unmatched:00984720",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:00984728",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009ba214"
      ]
    ]
  ],
  "added": [
    [
      "009ba1f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ba20c"
      ]
    ],
    [
      "009ba200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009ba208",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009ba214"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984700.md#insn-00984718) · [`00984720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984700.md#insn-00984720) · [`0098472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984700.md#insn-0098472c)

~~~diff
- 00984718 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00984718 bytes a0000054
- 00984720 ["INT_ADD", "register:40f0:8", ["const:984720:8", "const:4:8"]]
- 00984720 ["CALL", null, ["ram:457e1c:8"]]
- 00984720 bytes bf4deb97
- 0098472c ["INT_ADD", "register:40f0:8", ["const:98472c:8", "const:4:8"]]
- 0098472c ["CALL", null, ["ram:457e1c:8"]]
- 0098472c bytes bc4deb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4dd5978ccc0418b91932dfa408e293c"></a>

### [`00984c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984c24.md) → [`009ba704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba704.md) FUN_009ba704

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00985084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00985/00985084.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`009bab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 7.69% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009ba7ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00984c6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00984ca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ba794"
      ]
    ]
  ],
  "added": [
    [
      "009ba788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009ba794"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984c24.md#insn-00984c6c) · [`00984c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984c24.md#insn-00984c94) · [`00984ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984c24.md#insn-00984ca8)

~~~diff
- 00984c6c ["COPY", "tmp:0:1", ["register:101:1"]]
- 00984c6c ["COPY", "tmp:1:1", ["const:0:1"]]
- 00984c6c ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 00984c6c ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 00984c6c bytes 20014a7a
- 00984c94 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00984c94 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00984c94 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00984c94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00984c94 bytes 4915819a
- 00984ca8 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00984ca8 bytes 60000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f7ad2c0040e14315edc5d459c667638"></a>

### [`009870dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md) → [`009bcbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md) FUN_009bcbbc

採用 · 移動量 `+0x35ae0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00987ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/00987ebc.md) [`00988004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988004.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`009bd99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md) [`009bdae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 56.00% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009870f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00987104"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098716c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009870f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcc00"
      ]
    ],
    [
      "unmatched:00987100",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ],
    [
      "unmatched:00987104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcc00"
      ]
    ]
  ],
  "added": [
    [
      "009bcbd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcc00"
      ]
    ],
    [
      "009bcbe0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ],
    [
      "009bcbe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcc00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009870f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md#insn-009870f4) · [`00987100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md#insn-00987100) · [`00987104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md#insn-00987104)

~~~diff
- 009870f4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 009870f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009870f4 bytes 740100b4
- 00987100 ["INT_ADD", "register:40f0:8", ["const:987100:8", "const:4:8"]]
- 00987100 ["CALL", null, ["callee:00c538e0:8"]]
- 00987100 bytes 643f0994
- 00987104 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00987104 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00987104 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b1c276f71926100d80faa531139b83"></a>

### [`00988004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988004.md) → [`009bdae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md) FUN_009bdae4

採用 · 移動量 `+0x35ae0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00988b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988b6c.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009870dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md) [`00a251d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a251d8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`009be660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be660.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009bcbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md) [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00988004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00988004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00988008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00988004",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00988008",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098800c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009bdae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009bdae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009bdaec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00988004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988004.md#insn-00988004) · [`00988008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988004.md#insn-00988008) · [`0098800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988004.md#insn-0098800c)

~~~diff
- 00988004 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00988004 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00988004 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00988004 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00988004 bytes fd7bbda9
- 00988008 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00988008 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00988008 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00988008 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00988008 bytes f65701a9
- 0098800c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0098800c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0098800c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0098800c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098800c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b448ee369a7f978d13e47c524985ed41"></a>

### [`009898dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/009898dc.md) → [`009bf3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf3d0.md) FUN_009bf3d0

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009898dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009898dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009898f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009898dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009898e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:009898f4",
      "DATA",
      [
        "storage",
        "00c0b2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf3d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009bf3dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "009bf3e8",
      "DATA",
      [
        "storage",
        "00c89190",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009898dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/009898dc.md#insn-009898dc) · [`009898e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/009898dc.md#insn-009898e8) · [`009898f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/009898dc.md#insn-009898f4)

~~~diff
- 009898dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009898dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009898dc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009898dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009898dc bytes fd7bbfa9
- 009898e8 ["INT_ADD", "register:40f0:8", ["const:9898e8:8", "const:4:8"]]
- 009898e8 ["CALL", null, ["callee:00c57a90:8"]]
- 009898e8 bytes d6450994
- 009898f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009898f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009898f4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eefbae316aa5c8119b8c5e251f9eeeb"></a>

### [`00989900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989900.md) → [`009bf3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf3f4.md) FUN_009bf3f4

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00989908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009bf3fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0098990c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00989908",
      "DATA",
      [
        "storage",
        "00c0b2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf3fc",
      "DATA",
      [
        "storage",
        "00c89190",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989900.md#insn-00989908) · [`0098990c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989900.md#insn-0098990c)
- 新版 [`009bf3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf3f4.md#insn-009bf3fc)

~~~diff
- 00989908 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00989908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00989908 bytes 280000f9
- 0098990c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0098990c ["RETURN", null, ["register:0:8"]]
- 0098990c bytes c0035fd6
+ 009bf3fc ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 009bf3fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009bf3fc bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e982e3b16a70c0c30eef3adb6e3f4839"></a>

### [`00989918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989918.md) → [`009bf40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf40c.md) FUN_009bf40c

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0098993c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009bf430"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098993c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "009bf430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098993c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989918.md#insn-0098993c) · [`00989920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989918.md#insn-00989920)
- 新版 [`009bf430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf40c.md#insn-009bf430) · [`009bf414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf40c.md#insn-009bf414)

~~~diff
- 0098993c ["INT_ADD", "register:40f0:8", ["const:98993c:8", "const:4:8"]]
- 0098993c ["CALL", null, ["ram:457e1c:8"]]
- 0098993c bytes 3839eb97
+ 009bf430 ["INT_ADD", "register:40f0:8", ["const:9bf430:8", "const:4:8"]]
+ 009bf430 ["CALL", null, ["ram:47acb4:8"]]
+ 009bf430 bytes 21eeea97
- 00989920 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00989920 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 009bf414 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009bf414 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00989920 bytes e1010054
+ 009bf414 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7692b3042c8ca2c6f3927eb4298dd9b1"></a>

### [`0098998c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/0098998c.md) → [`009bf480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf480.md) FUN_009bf480

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009899a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009bf498"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009899ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009899a4",
      "DATA",
      [
        "storage",
        "00c0b338",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009899a8",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009bf498",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ],
    [
      "009bf49c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009899a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/0098998c.md#insn-009899a4) · [`009899ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/0098998c.md#insn-009899ac)
- 新版 [`009bf498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf480.md#insn-009bf498)

~~~diff
- 009899a4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009899a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009899a4 bytes 080000f9
- 009899ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 009899ac ["RETURN", null, ["register:0:8"]]
- 009899ac bytes c0035fd6
+ 009bf498 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009bf498 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009bf498 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b89113cd000d81ce3b654095a3c69e1e"></a>

### [`00989a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a2c.md) → [`009bf520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf520.md) FUN_009bf520

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00989a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00989a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009bf52c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00989a38",
      "DATA",
      [
        "storage",
        "00c0b3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf52c",
      "DATA",
      [
        "storage",
        "00c892a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00989a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a2c.md#insn-00989a38) · [`00989a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a2c.md#insn-00989a3c)
- 新版 [`009bf52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf520.md#insn-009bf52c)

~~~diff
- 00989a38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00989a38 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00989a38 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00989a38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00989a38 bytes 292000a9
- 00989a3c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00989a3c ["RETURN", null, ["register:0:8"]]
- 00989a3c bytes c0035fd6
+ 009bf52c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009bf52c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 009bf52c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 009bf52c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009bf52c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5439aa061a4202dfe41200ece0e4f448"></a>

### [`0098a780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a780.md) → [`009c0274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0274.md) FUN_009c0274

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098a780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098a780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098a798"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098a780",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098a78c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:0098a798",
      "DATA",
      [
        "storage",
        "00c0b4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009c0274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009c0280",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "009c028c",
      "DATA",
      [
        "storage",
        "00c893a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a780.md#insn-0098a780) · [`0098a78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a780.md#insn-0098a78c) · [`0098a798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a780.md#insn-0098a798)

~~~diff
- 0098a780 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098a780 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098a780 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0098a780 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098a780 bytes fd7bbfa9
- 0098a78c ["INT_ADD", "register:40f0:8", ["const:98a78c:8", "const:4:8"]]
- 0098a78c ["CALL", null, ["callee:00c57a90:8"]]
- 0098a78c bytes 2d420994
- 0098a798 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0098a798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0098a798 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1233773b60ca9f2674e6341a86f1e2e8"></a>

### [`0098a8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a8ac.md) → [`009c03a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03a0.md) FUN_009c03a0

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098a8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098a8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009c03c4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098a8d0",
      "DATA",
      [
        "storage",
        "00c0b5d0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0098a8d4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098a8d8",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009c03c4",
      "DATA",
      [
        "storage",
        "00c894a8",
        null,
        "undefined *"
      ]
    ],
    [
      "009c03c8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009c03cc",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098a8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a8ac.md#insn-0098a8d0) · [`0098a8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a8ac.md#insn-0098a8dc)
- 新版 [`009c03c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03a0.md#insn-009c03c4)

~~~diff
- 0098a8d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0098a8d0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0098a8d0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0098a8d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098a8d0 bytes 082400a9
- 0098a8dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 0098a8dc ["RETURN", null, ["register:0:8"]]
- 0098a8dc bytes c0035fd6
+ 009c03c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009c03c4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009c03c4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009c03c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009c03c4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cab295a7ad8b5e7c92341e06319d7587"></a>

### [`0098af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098af8c.md) → [`009c0a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0a80.md) FUN_009c0a80

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098afa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009c0a98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0098afac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098afa4",
      "DATA",
      [
        "storage",
        "00c0b650",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0098afa8",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009c0a98",
      "DATA",
      [
        "storage",
        "00c89528",
        null,
        "undefined *"
      ]
    ],
    [
      "009c0a9c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098afa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098af8c.md#insn-0098afa4) · [`0098afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098af8c.md#insn-0098afac)
- 新版 [`009c0a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0a80.md#insn-009c0a98)

~~~diff
- 0098afa4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0098afa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0098afa4 bytes 080000f9
- 0098afac ["COPY", "register:0:8", ["register:40f0:8"]]
- 0098afac ["RETURN", null, ["register:0:8"]]
- 0098afac bytes c0035fd6
+ 009c0a98 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009c0a98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009c0a98 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f2ea6b562b8a38a59c79c76c51c8dc3"></a>

### [`0098b270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b270.md) → [`009c0d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md) FUN_009c0d64

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0098a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098a/0098a8fc.md) [`0098b0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b0e8.md) · 呼出先 3件 [`0043e7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e7f8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`009c03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03f0.md) [`009c0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0bdc.md) · 呼出先 3件 [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 75.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098b270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098b274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009c0d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009c0d68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b270.md#insn-0098b270) · [`0098b274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b270.md#insn-0098b274)
- 新版 [`009c0d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c0d64.md#insn-009c0d64)

~~~diff
- 0098b270 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098b270 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098b270 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0098b270 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098b270 bytes fd7bbea9
- 0098b274 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0098b274 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0098b274 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0098b274 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098b274 bytes f44f01a9
+ 009c0d64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009c0d64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009c0d64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 009c0d64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009c0d64 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1728f6513b6b663066c4285ef2194b"></a>

### [`0098b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b838.md) → [`009c132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c132c.md) FUN_009c132c

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b83c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098b838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098b83c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098b85c",
      "DATA",
      [
        "storage",
        "00c0b860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009c132c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009c1330",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009c1350",
      "DATA",
      [
        "storage",
        "00c89738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b838.md#insn-0098b838) · [`0098b83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b838.md#insn-0098b83c) · [`0098b85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b838.md#insn-0098b85c)

~~~diff
- 0098b838 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098b838 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098b838 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0098b838 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098b838 bytes fd7bbea9
- 0098b83c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0098b83c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0098b83c bytes f30b00f9
- 0098b85c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0098b85c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0098b85c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0098b85c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098b85c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ccb12142f126bbebe0e518eb4cf02d"></a>

### [`0098b888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b888.md) → [`009c137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md) FUN_009c137c

採用 · 移動量 `+0x35af4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md) [`00886014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886014.md) [`00a25500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25500.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md) [`00a83390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83390.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 77.36% / 新版 77.36%

CFGの説明率　旧版 28.57% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098b8fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009c13a8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098b8b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c13e0"
      ]
    ],
    [
      "unmatched:0098b8fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c1444"
      ]
    ]
  ],
  "added": [
    [
      "009c13a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c13e0"
      ]
    ],
    [
      "009c13f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c1444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098b8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b888.md#insn-0098b8b4) · [`0098b8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098b/0098b888.md#insn-0098b8fc)
- 新版 [`009c13a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c1/009c137c.md#insn-009c13a8)

~~~diff
- 0098b8b4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 0098b8b4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0098b8b4 bytes c90100b4
- 0098b8fc ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0098b8fc bytes a0020054
+ 009c13a8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 009c13a8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 009c13a8 bytes c90100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baac12e267644e17f690575698371e97"></a>

### [`0098c998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098c998.md) → [`009c248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c248c.md) FUN_009c248c

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098ca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098ca8c.md) · 呼出先 4件 [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`009c2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c2/009c2580.md) · 呼出先 4件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098c9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009c24a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098c9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098c9b4",
      "DATA",
      [
        "storage",
        "00c0b8e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0098c9b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c24d8"
      ]
    ],
    [
      "unmatched:0098c9c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ],
  "added": [
    [
      "009c24a8",
      "DATA",
      [
        "storage",
        "00c897b8",
        null,
        "pointer"
      ]
    ],
    [
      "009c24ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c24d8"
      ]
    ],
    [
      "009c24b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098c9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098c998.md#insn-0098c9b4) · [`0098c9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098c998.md#insn-0098c9b8) · [`0098c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098c/0098c998.md#insn-0098c9c4)

~~~diff
- 0098c9b4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0098c9b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0098c9b4 bytes 080000f9
- 0098c9b8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0098c9b8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0098c9b8 bytes 740100b4
- 0098c9c4 ["INT_ADD", "register:40f0:8", ["const:98c9c4:8", "const:4:8"]]
- 0098c9c4 ["CALL", null, ["callee:00c538e0:8"]]
- 0098c9c4 bytes 33290994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-555933079b615de1f1b882164983aa83"></a>

### [`00991af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00991/00991af4.md) → [`009c75e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e8.md) FUN_009c75e8

採用 · 移動量 `+0x35af4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`0096d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d580.md) · 呼出先 1件 [`00991b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00991/00991b3c.md)
- 新版 呼出元 2件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`009a3064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3064.md) · 呼出先 1件 [`009c7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7630.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00991b20"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009c7614"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00991b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00991/00991af4.md#insn-00991b20) · [`00991b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00991/00991af4.md#insn-00991b0c)
- 新版 [`009c7614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e8.md#insn-009c7614) · [`009c7600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e8.md#insn-009c7600)

~~~diff
- 00991b20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00991b20 ["RETURN", null, ["register:0:8"]]
- 00991b20 bytes c0035fd6
+ 009c7614 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009c7614 ["RETURN", null, ["register:0:8"]]
+ 009c7614 bytes c0035fd6
- 00991b0c ["INT_ADD", "register:40f0:8", ["const:991b0c:8", "const:4:8"]]
- 00991b0c ["CALL", null, ["callee:009c7630:8"]]
+ 009c7600 ["INT_ADD", "register:40f0:8", ["const:9c7600:8", "const:4:8"]]
+ 009c7600 ["CALL", null, ["callee:009c7630:8"]]
- 00991b0c bytes 0c000094
+ 009c7600 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2746a18c9a5f7b35634a707134d2f1"></a>

### [`00992bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992bd0.md) → [`009c86c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md) FUN_009c86c4

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 73.58% / 新版 79.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00992c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00992df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009c8770"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00992c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c87cc"
      ]
    ],
    [
      "unmatched:00992df0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c88fc"
      ]
    ]
  ],
  "added": [
    [
      "009c8770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c87cc"
      ]
    ],
    [
      "009c88e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009c88fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00992c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992bd0.md#insn-00992c7c) · [`00992df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00992/00992bd0.md#insn-00992df0)
- 新版 [`009c8770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c8/009c86c4.md#insn-009c8770)

~~~diff
- 00992c7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00992c7c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00992c7c bytes e1020054
- 00992df0 ["CBRANCH", null, ["local:b28:8", "register:101:1"]]
- 00992df0 bytes c0000054
+ 009c8770 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009c8770 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 009c8770 bytes e1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88bf0574d6b92287ca196ce236d175e0"></a>

### [`00994250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/00994250.md) → [`009c9d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md) FUN_009c9d44

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00993f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00993/00993f28.md) [`009943c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/009943c4.md) [`009946a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/009946a8.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`009c9a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9a1c.md) [`009c9eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9eb8.md) [`009ca19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca19c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 60.61% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099439c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009c9e90"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0099439c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/00994250.md#insn-0099439c) · [`009942c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/00994250.md#insn-009942c4)
- 新版 [`009c9e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md#insn-009c9e90) · [`009c9db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c9/009c9d44.md#insn-009c9db8)

~~~diff
- 0099439c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:48:8"]]
- 0099439c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0099439c bytes c82600f9
+ 009c9e90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:48:8"]]
+ 009c9e90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009c9e90 bytes c82600f9
- 009942c4 ["INT_ADD", "register:40f0:8", ["const:9942c4:8", "const:4:8"]]
- 009942c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 009c9db8 ["INT_ADD", "register:40f0:8", ["const:9c9db8:8", "const:4:8"]]
+ 009c9db8 ["CALL", null, ["callee:00c57a90:8"]]
- 009942c4 bytes 5f1b0994
+ 009c9db8 bytes 36370a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a28bd4cf21d20b9036c93f6730332a6"></a>

### [`00996198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md) → [`009cbc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md) FUN_009cbc8c

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00994d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/00994d40.md) · 呼出先 4件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00995cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00995/00995cfc.md) [`00995f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00995/00995f30.md) [`00996434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996434.md)
- 新版 呼出元 1件 [`009ca834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca834.md) · 呼出先 4件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`009cb7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cb7f0.md) [`009cba24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cba24.md) [`009cbf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbf28.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 79.80% / 新版 79.80%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009962f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009cbde8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009963ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009962f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009cbe98"
      ]
    ],
    [
      "unmatched:009963a8",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009963ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "009cbde8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009cbe98"
      ]
    ],
    [
      "009cbe9c",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "009cbea0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009962f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md#insn-009962f4) · [`009963ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md#insn-009963ac)
- 新版 [`009cbde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md#insn-009cbde8)

~~~diff
- 009962f4 ["INT_EQUAL", "tmp:0:1", ["register:4078:8", "const:0:8"]]
- 009962f4 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 009962f4 bytes 8f0500b4
- 009963ac ["INT_ADD", "register:40f0:8", ["const:9963ac:8", "const:4:8"]]
- 009963ac ["CALL", null, ["ram:41fdf0:8"]]
- 009963ac bytes 9126ea97
+ 009cbde8 ["INT_EQUAL", "tmp:0:1", ["register:4078:8", "const:0:8"]]
+ 009cbde8 ["CBRANCH", null, ["local:b49:8", "tmp:0:1"]]
+ 009cbde8 bytes 8f0500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94937f9d35c088f136f93099026c112"></a>

### [`00996434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996434.md) → [`009cbf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbf28.md) FUN_009cbf28

採用 · 移動量 `+0x35af4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00994d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00994/00994d40.md) [`00995cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00995/00995cfc.md) [`00996198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996198.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00995f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00995/00995f30.md)
- 新版 呼出元 3件 [`009ca834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ca/009ca834.md) [`009cb7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cb7f0.md) [`009cbc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cbc8c.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`009cba24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cb/009cba24.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.55% / 新版 84.55%

CFGの説明率　旧版 51.43% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00996490"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00996498"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009964f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00996490",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009964a0"
      ]
    ],
    [
      "unmatched:00996498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009cbf78"
      ]
    ],
    [
      "unmatched:0099649c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009cc0ac"
      ]
    ]
  ],
  "added": [
    [
      "009cbf84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009cbf94"
      ]
    ],
    [
      "009cbf8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009cbf78"
      ]
    ],
    [
      "009cbf90",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009cc0ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00996490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996434.md#insn-00996490) · [`00996498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996434.md#insn-00996498) · [`009964f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996434.md#insn-009964f8)

~~~diff
- 00996490 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00996490 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00996490 bytes 8a000054
- 00996498 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00996498 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00996498 bytes 6bffffb5
- 009964f8 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 009964f8 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 009964f8 bytes 0b0600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5fda6131e205dda4dace621c33b41a"></a>

### [`00996ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md) → [`009cc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc994.md) FUN_009cc994

採用 · 移動量 `+0x35af4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0084c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c134.md) [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084d464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md) [`00879b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879b70.md) · 呼出先 6件 [`0073e0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073eb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb18.md) [`0073ed78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ed78.md) [`0073ef04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef04.md)
- 新版 呼出元 4件 [`0087f0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`008803fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md) [`008acd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acd10.md) · 呼出先 6件 [`007683d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00768e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e24.md) [`00769084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769084.md) [`00769210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769210.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 47.37% / 新版 47.37%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00996eb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00996ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00996ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00996eb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081c6a0"
      ]
    ],
    [
      "unmatched:00996ebc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e6dc"
      ]
    ],
    [
      "unmatched:00996ec4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073eb18"
      ]
    ]
  ],
  "added": [
    [
      "009cc9a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084e55c"
      ]
    ],
    [
      "009cc9b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689e8"
      ]
    ],
    [
      "009cc9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00996eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md#insn-00996eb0) · [`00996ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md#insn-00996ebc) · [`00996ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md#insn-00996ec4)

~~~diff
- 00996eb0 ["INT_ADD", "register:40f0:8", ["const:996eb0:8", "const:4:8"]]
- 00996eb0 ["CALL", null, ["ram:81c6a0:8"]]
- 00996eb0 bytes fc15fa97
- 00996ebc ["INT_ADD", "register:40f0:8", ["const:996ebc:8", "const:4:8"]]
- 00996ebc ["CALL", null, ["ram:73e6dc:8"]]
- 00996ebc bytes 089ef697
- 00996ec4 ["INT_ADD", "register:40f0:8", ["const:996ec4:8", "const:4:8"]]
- 00996ec4 ["CALL", null, ["ram:73eb18:8"]]
- 00996ec4 bytes 159ff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5469011a449ddeb0d5198e053bbfb966"></a>

### [`0099d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d8b4.md) → [`009d3598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3598.md) FUN_009d3598

採用 · 移動量 `+0x35ce4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d8b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0099d8b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0099d8b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009d3598",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009d359c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0099d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d8b4.md#insn-0099d8b4) · [`0099d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d8b4.md#insn-0099d8b8) · [`0099d8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d8b4.md#insn-0099d8d4)

~~~diff
- 0099d8b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0099d8b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0099d8b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0099d8b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0099d8b4 bytes fd7bbea9
- 0099d8b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0099d8b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0099d8b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0099d8b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0099d8b8 bytes f44f01a9
- 0099d8d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0099d8d4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0099d8d4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0099d8d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 0099d8d4 bytes 4115819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c65dae3507856d4bfba9d0f7acc7062"></a>

### [`0099d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d91c.md) → [`009d3600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3600.md) FUN_009d3600

採用 · 移動量 `+0x35ce4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 63.16% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d91c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d91c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099d920"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0099d91c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0099d920",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0099d924",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009d3600",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009d3604",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009d3608",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0099d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d91c.md#insn-0099d91c) · [`0099d920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d91c.md#insn-0099d920) · [`0099d924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099d91c.md#insn-0099d924)

~~~diff
- 0099d91c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0099d91c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0099d91c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0099d91c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0099d91c bytes fd7bbca9
- 0099d920 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0099d920 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0099d920 bytes f70b00f9
- 0099d924 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0099d924 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0099d924 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0099d924 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0099d924 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f9e0dfe9a995d05b0095ecb8aa1203"></a>

### [`009a5ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5ed4.md) → [`009dbc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbc34.md) FUN_009dbc34

採用 · 移動量 `+0x35d60` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 2件 [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 2件 [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009dbc70",
      "incomplete_value": true,
      "site": "009dbc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "live",
            "register:40b8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009a5f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5ed4.md#insn-009a5f24) · [`009a5f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5ed4.md#insn-009a5f14)
- 新版 [`009dbc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbc34.md#insn-009dbc84) · [`009dbc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbc34.md#insn-009dbc74)

~~~diff
- 009a5f24 ["INT_ADD", "register:40f0:8", ["const:9a5f24:8", "const:4:8"]]
- 009a5f24 ["CALL", null, ["callee:00470074:8"]]
+ 009dbc84 ["INT_ADD", "register:40f0:8", ["const:9dbc84:8", "const:4:8"]]
+ 009dbc84 ["CALL", null, ["callee:00470074:8"]]
- 009a5f24 bytes ae9cea97
+ 009dbc84 bytes fc50ea97
- 009a5f14 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a5f14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009a5f14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009a5f14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009a5f14 bytes 2100088b
+ 009dbc74 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009dbc74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009dbc74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009dbc74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009dbc74 bytes 2100088b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-311e168786c75aa68d81b1d7854f7fbf"></a>

### [`009a61a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a61a4.md) → [`009dbf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf04.md) FUN_009dbf04

採用 · 移動量 `+0x35d60` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.79% / 新版 78.79%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a61a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a61a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a61a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a61a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a61a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a61ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009dbf04",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009dbf08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009dbf0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a61a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a61a4.md#insn-009a61a4) · [`009a61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a61a4.md#insn-009a61a8) · [`009a61ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a61a4.md#insn-009a61ac)

~~~diff
- 009a61a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a61a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a61a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 009a61a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a61a4 bytes fd7bbca9
- 009a61a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a61a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 009a61a8 bytes f70b00f9
- 009a61ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009a61ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009a61ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009a61ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a61ac bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8f1700a098606fa9498f58fb48930c"></a>

### [`009a70a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a70a0.md) → [`009dce00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dce00.md) FUN_009dce00

採用 · 移動量 `+0x35d60` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a70b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009dce18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a70c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a70b8",
      "DATA",
      [
        "storage",
        "00c0b900",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a70bc",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009dce18",
      "DATA",
      [
        "storage",
        "00c897d8",
        null,
        "undefined *"
      ]
    ],
    [
      "009dce1c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a70b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a70a0.md#insn-009a70b8) · [`009a70c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a70a0.md#insn-009a70c0)
- 新版 [`009dce18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dce00.md#insn-009dce18)

~~~diff
- 009a70b8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a70b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a70b8 bytes 080000f9
- 009a70c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a70c0 ["RETURN", null, ["register:0:8"]]
- 009a70c0 bytes c0035fd6
+ 009dce18 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009dce18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009dce18 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782878f11ed268ee7fdd68c834731626"></a>

### [`009a71f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a71f4.md) → [`009dcf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcf54.md) FUN_009dcf54

採用 · 移動量 `+0x35d60` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0099fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fe4c.md) [`009a1b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1b84.md) [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) [`009d7890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7890.md) [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a71f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a71f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009dcf54"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a71f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a7200",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009a7204",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "009dcf54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009dcf60",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "009dcf64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a71f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a71f4.md#insn-009a71f4) · [`009a7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a71f4.md#insn-009a7204)
- 新版 [`009dcf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcf54.md#insn-009dcf54)

~~~diff
- 009a71f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a71f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a71f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009a71f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a71f4 bytes fd7bbfa9
- 009a7204 ["INT_ADD", "register:40f0:8", ["const:9a7204:8", "const:4:8"]]
- 009a7204 ["CALL", null, ["ram:418c38:8"]]
- 009a7204 bytes 8dc6e997
+ 009dcf54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009dcf54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009dcf54 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 009dcf54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009dcf54 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c614ea2b99b3459155b573c0a7c9f6e5"></a>

### [`009a7a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a7a20.md) → [`009dd780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009dd780.md) FUN_009dd780

採用 · 移動量 `+0x35d60` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a2140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a2/009a2140.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`009d7e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d7e4c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a7a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a7a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009dd780"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a7a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a7a2c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009a7a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "009dd780",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009dd78c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "009dd790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a7a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a7a20.md#insn-009a7a20) · [`009a7a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a7/009a7a20.md#insn-009a7a30)
- 新版 [`009dd780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dd/009dd780.md#insn-009dd780)

~~~diff
- 009a7a20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a7a20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a7a20 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009a7a20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a7a20 bytes fd7bbfa9
- 009a7a30 ["INT_ADD", "register:40f0:8", ["const:9a7a30:8", "const:4:8"]]
- 009a7a30 ["CALL", null, ["ram:418c38:8"]]
- 009a7a30 bytes 82c4e997
+ 009dd780 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009dd780 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009dd780 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 009dd780 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009dd780 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9252bd9b64c89fc68d35dc1a3d02506"></a>

### [`009a8714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8714.md) → [`009de474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de474.md) FUN_009de474

採用 · 移動量 `+0x35d60` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`007ab264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab264.md) · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a26b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26b68.md) [`00a26d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26d00.md)
- 新版 呼出元 2件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a849f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a849f8.md) [`00a84b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84b90.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de494",
      "value": [
        "leaf",
        "ram:a849f8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009a8734",
      "value": [
        "leaf",
        "ram:a26b68:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a873c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de4a0",
      "value": [
        "leaf",
        "ram:a84b90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009a8740",
      "value": [
        "leaf",
        "ram:a26d00:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009de494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26b68"
      ]
    ],
    [
      "unmatched:009a873c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "009de4a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26d00"
      ]
    ]
  ],
  "added": [
    [
      "009de494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a849f8"
      ]
    ],
    [
      "009de49c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "009de4a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84b90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a8734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8714.md#insn-009a8734) · [`009a873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8714.md#insn-009a873c) · [`009a8740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8714.md#insn-009a8740)
- 新版 [`009de494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de474.md#insn-009de494) · [`009de4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009de/009de474.md#insn-009de4a0)

~~~diff
- 009a8734 ["INT_ADD", "register:40f0:8", ["const:9a8734:8", "const:4:8"]]
- 009a8734 ["CALL", null, ["ram:a26b68:8"]]
+ 009de494 ["INT_ADD", "register:40f0:8", ["const:9de494:8", "const:4:8"]]
+ 009de494 ["CALL", null, ["ram:a849f8:8"]]
- 009a8734 bytes 0df90194
+ 009de494 bytes 59990294
- 009a873c ["INT_ADD", "register:40f0:8", ["const:9a873c:8", "const:4:8"]]
- 009a873c ["CALL", null, ["callee:008514b8:8"]]
- 009a873c bytes 91dbf997
- 009a8740 ["INT_ADD", "register:40f0:8", ["const:9a8740:8", "const:4:8"]]
- 009a8740 ["CALL", null, ["ram:a26d00:8"]]
+ 009de4a0 ["INT_ADD", "register:40f0:8", ["const:9de4a0:8", "const:4:8"]]
+ 009de4a0 ["CALL", null, ["ram:a84b90:8"]]
- 009a8740 bytes 70f90194
+ 009de4a0 bytes bc990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1915ddd343c37314b224f3490a8daf5c"></a>

### [`009a9794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9794.md) → [`00a066b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a066b4.md) FUN_00a066b4

採用 · 移動量 `+0x5cf20` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a28e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28e14.md) · 呼出先 7件 [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) [`005748a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md) [`00574b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574b74.md) [`00574b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574b80.md) [`00574b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574b8c.md)
- 新版 呼出元 1件 [`00a86ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86ca4.md) · 呼出先 7件 [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00597a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a0c.md) [`00597a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a18.md) [`00597a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a24.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a97d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a066f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a9844"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a97d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a9848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a067a8"
      ]
    ]
  ],
  "added": [
    [
      "00a066f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00a06768",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a067a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a97d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9794.md#insn-009a97d0) · [`009a9824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9794.md#insn-009a9824) · [`009a9844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9794.md#insn-009a9844)
- 新版 [`00a06744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a066b4.md#insn-00a06744)

~~~diff
- 009a97d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a97d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 009a97d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009a97d0 bytes a8831ef8
- 009a9824 ["INT_ADD", "register:40f0:8", ["const:9a9824:8", "const:4:8"]]
- 009a9824 ["CALL", null, ["callee:00597738:8"]]
+ 00a06744 ["INT_ADD", "register:40f0:8", ["const:a06744:8", "const:4:8"]]
+ 00a06744 ["CALL", null, ["callee:00597738:8"]]
- 009a9824 bytes 1f2cef97
+ 00a06744 bytes fd43ee97
- 009a9844 ["COPY", "register:100:1", ["const:0:1"]]
- 009a9844 ["COPY", "register:101:1", ["const:0:1"]]
- 009a9844 ["COPY", "register:102:1", ["const:1:1"]]
- 009a9844 ["COPY", "register:103:1", ["const:1:1"]]
- 009a9844 bytes 0020611e
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4d8f2dbab0cbf04bde796d59d82dc3"></a>

### [`009a98b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a98b4.md) → [`00a067d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a067d4.md) FUN_00a067d4

採用 · 移動量 `+0x5cf20` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a98b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a98b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a98b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a98b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a98b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a067d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a067d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a98b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a98b4.md#insn-009a98b4) · [`009a98b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a98b4.md#insn-009a98b8)
- 新版 [`00a067d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a067d4.md#insn-00a067d4)

~~~diff
- 009a98b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a98b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a98b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a98b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a98b4 bytes fd7bbea9
- 009a98b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009a98b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009a98b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009a98b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a98b8 bytes f44f01a9
+ 00a067d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a067d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a067d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a067d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a067d4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b2f8e863311654330337839a54a4d6"></a>

### [`009a9928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9928.md) → [`00a06848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06848.md) FUN_00a06848

採用 · 移動量 `+0x5cf20` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a8d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8d24.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a05c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a9928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a9928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a06848"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a9928",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a9934",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009a9938",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00a06848",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a06854",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a06858",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a9928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9928.md#insn-009a9928) · [`009a9938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9928.md#insn-009a9938)
- 新版 [`00a06848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06848.md#insn-00a06848)

~~~diff
- 009a9928 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a9928 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a9928 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009a9928 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a9928 bytes fd7bbfa9
- 009a9938 ["INT_ADD", "register:40f0:8", ["const:9a9938:8", "const:4:8"]]
- 009a9938 ["CALL", null, ["ram:418c38:8"]]
- 009a9938 bytes c0bce997
+ 00a06848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a06848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a06848 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a06848 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a06848 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee0cdbb28e6d09a5aecae8f21b5d7e7"></a>

### [`009a993c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a993c.md) → [`00a0685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a0685c.md) FUN_00a0685c

採用 · 移動量 `+0x5cf20` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a8d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a8/009a8d24.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a05c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a993c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a993c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a0685c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a993c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a9948",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009a994c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00a0685c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a06868",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a0686c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a993c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a993c.md#insn-009a993c) · [`009a994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a993c.md#insn-009a994c)
- 新版 [`00a0685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a0685c.md#insn-00a0685c)

~~~diff
- 009a993c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a993c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a993c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009a993c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a993c bytes fd7bbfa9
- 009a994c ["INT_ADD", "register:40f0:8", ["const:9a994c:8", "const:4:8"]]
- 009a994c ["CALL", null, ["ram:418c38:8"]]
- 009a994c bytes bbbce997
+ 00a0685c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a0685c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a0685c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a0685c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a0685c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb233c01b81c7a4705ab8908fc9de7bb"></a>

### [`009d2194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d2/009d2194.md) → [`00a2f090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f090.md) FUN_00a2f090

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) [`00a085a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a085a8.md) [`00a08b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08b90.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d2194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009d2194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a2f090"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d2194",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009d21a0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009d21a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a2f090",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a2f09c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a2f0a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d2194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d2/009d2194.md#insn-009d2194) · [`009d21a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d2/009d2194.md#insn-009d21a4)
- 新版 [`00a2f090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f090.md#insn-00a2f090)

~~~diff
- 009d2194 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009d2194 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009d2194 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009d2194 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009d2194 bytes fd7bbfa9
- 009d21a4 ["INT_ADD", "register:40f0:8", ["const:9d21a4:8", "const:4:8"]]
- 009d21a4 ["CALL", null, ["ram:41fdf0:8"]]
- 009d21a4 bytes 1337e997
+ 00a2f090 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a2f090 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a2f090 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a2f090 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a2f090 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59c75232dcd85b0d05c46d0d92a9f65a"></a>

### [`009d52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md) → [`00a321a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a321a8.md) FUN_00a321a8

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00644b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644b38.md) · 呼出先 2件 [`006ef68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ef/006ef68c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0066ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ae10.md) · 呼出先 2件 [`007196f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 72.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009d52e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a321e4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009d52e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a321d4"
      ]
    ]
  ],
  "added": [
    [
      "00a321e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a321d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d52e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md#insn-009d52e8) · [`009d52cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d5/009d52ac.md#insn-009d52cc)
- 新版 [`00a321e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a321a8.md#insn-00a321e4) · [`00a321c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a321a8.md#insn-00a321c8)

~~~diff
- 009d52e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009d52e8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 009d52e8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 009d52e8 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 009d52e8 bytes 8cffff54
+ 00a321e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a321e4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00a321e4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00a321e4 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
+ 00a321e4 bytes 8cffff54
- 009d52cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009d52cc ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00a321c8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a321c8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 009d52cc bytes 880400b4
+ 00a321c8 bytes 880400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

