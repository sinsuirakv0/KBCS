# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (2)

[一覧の目次](README.md)

<a id="compare-84f05b8c569984b4c256903d3a60482b"></a>

### [`005784a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005784a0.md) → [`0059ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md) FUN_0059ad78

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00576890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576890.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005784a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005784a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005784a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005784a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005784a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005784c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059adc8"
      ]
    ]
  ],
  "added": [
    [
      "0059ad78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0059ad7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0059ad9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059adc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005784a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005784a0.md#insn-005784a0) · [`005784a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005784a0.md#insn-005784a4) · [`005784c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005784a0.md#insn-005784c4)

~~~diff
- 005784a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005784a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005784a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005784a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005784a0 bytes fd7bbea9
- 005784a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005784a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005784a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005784a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005784a4 bytes f44f01a9
- 005784c4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 005784c4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005784c4 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-721e5057a02f7da3f3b52e961306910b"></a>

### [`005788ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005788ec.md) → [`0059b1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b1c4.md) FUN_0059b1c4

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 25.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059b1dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00578908"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00578904",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00578908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059b1f4"
      ]
    ],
    [
      "unmatched:00578934",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0059b1dc",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ],
    [
      "0059b1e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059b1f4"
      ]
    ],
    [
      "0059b20c",
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

- 旧版 [`00578904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005788ec.md#insn-00578904) · [`00578908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005788ec.md#insn-00578908) · [`00578934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005788ec.md#insn-00578934)

~~~diff
- 00578904 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00578904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00578904 bytes 080000f9
- 00578908 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00578908 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00578908 bytes b30000b4
- 00578934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00578934 ["INT_ADD", "register:40f0:8", ["const:578934:8", "const:4:8"]]
- 00578934 ["CALLIND", null, ["register:0:8"]]
- 00578934 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a78f5a1a92a33feadade6b11f883f52"></a>

### [`00578948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578948.md) → [`0059b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md) FUN_0059b220

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059b23c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00578988"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00578964",
      "DATA",
      [
        "storage",
        "00bf09c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00578988",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0059b23c",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ],
    [
      "0059b260",
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

- 旧版 [`00578964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578948.md#insn-00578964) · [`00578988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578948.md#insn-00578988)
- 新版 [`0059b23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b220.md#insn-0059b23c)

~~~diff
- 00578964 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00578964 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00578964 bytes 080000f9
- 00578988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00578988 ["INT_ADD", "register:40f0:8", ["const:578988:8", "const:4:8"]]
- 00578988 ["CALLIND", null, ["register:0:8"]]
- 00578988 bytes 00013fd6
+ 0059b23c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0059b23c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0059b23c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7aed3b52e3e8f9254ef0df84bebdad2"></a>

### [`00578a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a78.md) → [`0059b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md) FUN_0059b350

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578a7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00578a78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00578a7c",
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
      "0059b350",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0059b354",
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

- 旧版 [`00578a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a78.md#insn-00578a78) · [`00578a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578a78.md#insn-00578a7c)
- 新版 [`0059b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b350.md#insn-0059b350)

~~~diff
- 00578a78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00578a78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00578a78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00578a78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00578a78 bytes fd7bbea9
- 00578a7c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00578a7c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00578a7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00578a7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00578a7c bytes f44f01a9
+ 0059b350 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0059b350 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0059b350 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0059b350 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0059b350 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07249b519f6fdf49ff42e022b295f783"></a>

### [`00578ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ac8.md) → [`0059b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b3a0.md) FUN_0059b3a0

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00579074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579074.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0059b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.15% / 新版 71.15%

CFGの説明率　旧版 14.29% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578ad0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00578acc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00578ad0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00578ad4",
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
      "0059b3a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0059b3a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0059b3ac",
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

- 旧版 [`00578acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ac8.md#insn-00578acc) · [`00578ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ac8.md#insn-00578ad0) · [`00578ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ac8.md#insn-00578ad4)

~~~diff
- 00578acc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00578acc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00578acc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00578acc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00578acc bytes fd7b01a9
- 00578ad0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00578ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00578ad0 bytes f51300f9
- 00578ad4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00578ad4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00578ad4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00578ad4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00578ad4 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9498023260395ec6d97b4f589c92ca"></a>

### [`00578fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md) → [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) FUN_0059b89c

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00579ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579ab8.md) [`0057a7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a7f0.md) [`0057b864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b864.md) [`0057be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057be30.md) [`0057caac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057caac.md) · 呼出先 0件 
- 新版 呼出元 18件 [`0059c508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c508.md) [`0059d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d124.md) [`0059e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e110.md) [`0059e6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e6dc.md) [`0059f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f2d0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578fcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00578fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059b8a4"
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
      "unmatched:00578fd0",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059b8a8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md#insn-00578fcc) · [`00578fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578fc4.md#insn-00578fd0)
- 新版 [`0059b8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md#insn-0059b8a4)

~~~diff
- 00578fcc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00578fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00578fcc bytes 010800b9
- 00578fd0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00578fd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00578fd0 bytes 080000f9
+ 0059b8a4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
+ 0059b8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
+ 0059b8a4 bytes 010800b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f40bb6eae421bf0e63d9d5a7acf3759b"></a>

### [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md) → [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) FUN_0059b8c8

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00579e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md) [`0057a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md) [`0057c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057c274.md) [`0057cc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057c/0057cc9c.md) [`0057de8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057de8c.md) · 呼出先 1件 [`00579074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579074.md)
- 新版 呼出元 18件 [`0059c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md) [`0059d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md) [`0059eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md) [`0059f4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md) [`005a0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md) · 呼出先 1件 [`0059b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b94c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00579014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059b8ec"
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
      "unmatched:00579014",
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
      "0059b8ec",
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

- 旧版 [`00579014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md#insn-00579014) · [`00579008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md#insn-00579008)
- 新版 [`0059b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md#insn-0059b8ec) · [`0059b8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md#insn-0059b8e0)

~~~diff
- 00579014 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00579014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00579014 bytes 080000f9
+ 0059b8ec ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0059b8ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0059b8ec bytes 080000f9
- 00579008 ["COPY", "register:4040:8", ["const:bf0000:8"]]
+ 0059b8e0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00579008 bytes a83300f0
+ 0059b8e0 bytes 883600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb9b884ef336bfa0ea3765a8d2cd08f"></a>

### [`00579e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md) → [`0059c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md) FUN_0059c85c

採用 · 移動量 `+0x22a50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005907e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/005907e4.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`005b4e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4e14.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

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
      "site": "00579e38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059c888"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00579e7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00579e38",
      "DATA",
      [
        "storage",
        "00bf0af8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059c888",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md#insn-00579e38) · [`00579e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00579/00579e0c.md#insn-00579e7c)
- 新版 [`0059c888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059c/0059c85c.md#insn-0059c888)

~~~diff
- 00579e38 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00579e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00579e38 bytes c80200f9
- 00579e7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00579e7c ["RETURN", null, ["register:0:8"]]
- 00579e7c bytes c0035fd6
+ 0059c888 ["COPY", "tmp:0:8", ["register:40b0:8"]]
+ 0059c888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0059c888 bytes c80200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4b1965b0750f66ba3f852fc2facd7b"></a>

### [`0057a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md) → [`0059d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md) FUN_0059d314

採用 · 移動量 `+0x22934` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058ef88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ef88.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057aa00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059d334"
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
      "unmatched:0057aa00",
      "DATA",
      [
        "storage",
        "00bf0c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059d334",
      "DATA",
      [
        "storage",
        "00c6d840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md#insn-0057aa00) · [`0057a9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057a/0057a9e0.md#insn-0057a9f4)
- 新版 [`0059d334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md#insn-0059d334) · [`0059d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md#insn-0059d328)

~~~diff
- 0057aa00 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0057aa00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057aa00 bytes 880200f9
+ 0059d334 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 0059d334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0059d334 bytes 880200f9
- 0057a9f4 ["INT_ADD", "register:40f0:8", ["const:57a9f4:8", "const:4:8"]]
- 0057a9f4 ["CALL", null, ["callee:0059b8c8:8"]]
+ 0059d328 ["INT_ADD", "register:40f0:8", ["const:59d328:8", "const:4:8"]]
+ 0059d328 ["CALL", null, ["callee:0059b8c8:8"]]
- 0057a9f4 bytes 7ff9ff97
+ 0059d328 bytes 68f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb591b941b444f16d39efaff79e4a9a8"></a>

### [`0057b9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b9bc.md) → [`0059e268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md) FUN_0059e268

採用 · 移動量 `+0x228ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 43.75% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ba28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0059e2d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0057b9e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057b9e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059e2c0"
      ]
    ],
    [
      "unmatched:0057ba28",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059e290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059e2c0"
      ]
    ],
    [
      "0059e2d4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b9bc.md#insn-0057b9e4) · [`0057ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b9bc.md#insn-0057ba28)
- 新版 [`0059e290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059e268.md#insn-0059e290)

~~~diff
- 0057b9e4 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 0057b9e4 bytes 80010054
- 0057ba28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 0057ba28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057ba28 bytes 690e00f9
+ 0059e290 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 0059e290 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3de922519f06d998b6e2df523a67fd"></a>

### [`0057d670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d670.md) → [`0059fe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059fe0c.md) FUN_0059fe0c

採用 · 移動量 `+0x2279c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d68c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059fe18",
      "READ",
      [
        "storage",
        "002a1778",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0057d684",
      "READ",
      [
        "storage",
        "002a177f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059fe18",
      "READ",
      [
        "storage",
        "002b1dc4",
        null,
        "string"
      ]
    ],
    [
      "0059fe20",
      "READ",
      [
        "storage",
        "002b1dcb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d670.md#insn-0057d688) · [`0057d68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d670.md#insn-0057d68c) · [`0057d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d670.md#insn-0057d690)

~~~diff
- 0057d688 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0057d688 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0057d688 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:10:8"]]
- 0057d688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0057d688 bytes 1f410039
- 0057d68c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0057d68c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 0057d68c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0057d68c bytes 0b1100f8
- 0057d690 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 0057d690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057d690 bytes 090500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e82f8f5ed71731961adc83f935f4d8a"></a>

### [`0057d710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d710.md) → [`0059feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059feac.md) FUN_0059feac

採用 · 移動量 `+0x2279c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 12.50% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057d714"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057d710",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057d714",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057d724",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059feac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0059feb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0059fec0",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d710.md#insn-0057d710) · [`0057d714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d710.md#insn-0057d714) · [`0057d730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057d/0057d710.md#insn-0057d730)

~~~diff
- 0057d710 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0057d710 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0057d710 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0057d710 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0057d710 bytes fd7bbea9
- 0057d714 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0057d714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0057d714 bytes f30b00f9
- 0057d730 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0057d730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057d730 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bec5b8bc8f363e4385582786b1e13d"></a>

### [`0057ebfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ebfc.md) → [`005a1310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1310.md) FUN_005a1310

採用 · 移動量 `+0x22714` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ebfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ebfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ec00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0057ebfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057ec00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0057ec04",
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
      "005a1310",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005a1314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a1318",
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

- 旧版 [`0057ebfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ebfc.md#insn-0057ebfc) · [`0057ec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ebfc.md#insn-0057ec00) · [`0057ec04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ebfc.md#insn-0057ec04)

~~~diff
- 0057ebfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0057ebfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0057ebfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0057ebfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0057ebfc bytes fd7bbda9
- 0057ec00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0057ec00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0057ec00 bytes f50b00f9
- 0057ec04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0057ec04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0057ec04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0057ec04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0057ec04 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b728e34c41c490ec0237b5ef8f3de8fa"></a>

### [`0057ec78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ec78.md) → [`005a138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a138c.md) FUN_005a138c

採用 · 移動量 `+0x22714` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00772358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772358.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`0079c82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079c82c.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057ec9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057eca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a13b0"
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
      "unmatched:0057eca4",
      "DATA",
      [
        "storage",
        "00bf1550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a13b8",
      "DATA",
      [
        "storage",
        "00c6e110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ec9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ec78.md#insn-0057ec9c) · [`0057eca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057ec78.md#insn-0057eca4)
- 新版 [`005a13b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a138c.md#insn-005a13b0)

~~~diff
- 0057ec9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 0057ec9c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0057ec9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0057ec9c bytes 9f1e00f9
- 0057eca4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0057eca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057eca4 bytes 890200f9
+ 005a13b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
+ 005a13b0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 005a13b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 005a13b0 bytes 9f1e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8efb2daa403b324b0d32c2a5c78dfc54"></a>

### [`0057f3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f3a0.md) → [`005a1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ae0.md) FUN_005a1ae0

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 45.45% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057f3b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0057f3b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a1af0"
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
      "unmatched:0057f3b0",
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
      "005a1af0",
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

- 旧版 [`0057f3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f3a0.md#insn-0057f3b0) · [`0057f3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f3a0.md#insn-0057f3b4)
- 新版 [`005a1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1ae0.md#insn-005a1af0)

~~~diff
- 0057f3b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0057f3b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0057f3b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0057f3b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0057f3b0 bytes f44f01a9
+ 005a1af0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 005a1af0 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 005a1af0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 005a1af0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005a1af0 bytes f44f01a9
- 0057f3b4 ["COPY", "register:40e8:8", ["register:8:8"]]
- 0057f3b4 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1538896cd5cf8234c7c3ff37545ed4b"></a>

### [`00580004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580004.md) → [`005a2744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a2744.md) FUN_005a2744

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00580010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00580018"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00580018"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00580010",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00580014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a2780"
      ]
    ],
    [
      "unmatched:00580018",
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
      "005a2750",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ],
    [
      "005a2754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a2780"
      ]
    ],
    [
      "005a2758",
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

- 旧版 [`00580010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580004.md#insn-00580010) · [`00580014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580004.md#insn-00580014) · [`00580018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580004.md#insn-00580018)

~~~diff
- 00580010 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00580010 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00580010 bytes 090000f9
- 00580014 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00580014 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00580014 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00580014 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00580014 bytes 68010036
- 00580018 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00580018 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00580018 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00580018 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00580018 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d87ee2073f029d2486bcfe5ed1f139e"></a>

### [`00580084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580084.md) → [`005a27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27c4.md) FUN_005a27c4

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00580090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a27d0"
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
      "unmatched:00580090",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a27d0",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580084.md#insn-00580090) · [`00580084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580084.md#insn-00580084)
- 新版 [`005a27d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a2/005a27c4.md#insn-005a27d0)

~~~diff
- 00580090 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00580090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00580090 bytes 090c00f9
+ 005a27d0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
+ 005a27d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005a27d0 bytes 090c00f9
- 00580084 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00580084 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00580084 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00580084 bytes 08a04039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50095880901f8f7cfc23c2bc1eecac01"></a>

### [`00581760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581760.md) → [`005a3ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md) FUN_005a3ea0

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058176c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a3eac"
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
      "unmatched:0058176c",
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
      "005a3eac",
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

- 旧版 [`0058176c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581760.md#insn-0058176c) · [`00581770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581760.md#insn-00581770)
- 新版 [`005a3eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md#insn-005a3eac)

~~~diff
- 0058176c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0058176c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0058176c bytes f30b00f9
+ 005a3eac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 005a3eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 005a3eac bytes f30b00f9
- 00581770 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00581770 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1022eb6c10f84c7e64ed70c77eb06d6e"></a>

### [`00581818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581818.md) → [`005a3f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3f58.md) FUN_005a3f58

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 22.22% / 新版 22.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058181c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00581818",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058181c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058183c",
      "DATA",
      [
        "storage",
        "00bf1948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a3f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a3f5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a3f7c",
      "DATA",
      [
        "storage",
        "00c6e508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581818.md#insn-00581818) · [`0058181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581818.md#insn-0058181c) · [`00581838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581818.md#insn-00581838)

~~~diff
- 00581818 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00581818 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00581818 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00581818 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00581818 bytes fd7bbea9
- 0058181c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0058181c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0058181c bytes f30b00f9
- 00581838 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00581838 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00581838 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00581838 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00581838 bytes 1ffc00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68339576e7bf1165b4becc54c5258de"></a>

### [`00581860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581860.md) → [`005a3fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3fa0.md) FUN_005a3fa0

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00581874",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "005a3fc0",
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
      "005a3fb4",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "005a3fc0",
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

- 旧版 [`0058186c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581860.md#insn-0058186c) · [`00581874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581860.md#insn-00581874) · [`0058188c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581860.md#insn-0058188c)
- 新版 [`005a3fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3fa0.md#insn-005a3fac) · [`005a3fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3fa0.md#insn-005a3fcc)

~~~diff
- 0058186c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005a3fac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0058186c bytes c83400d0
+ 005a3fac bytes a83700f0
- 00581874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 00581874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00581874 bytes 089942f9
- 0058188c ["INT_ADD", "register:40f0:8", ["const:58188c:8", "const:4:8"]]
- 0058188c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005a3fcc ["INT_ADD", "register:40f0:8", ["const:5a3fcc:8", "const:4:8"]]
+ 005a3fcc ["CALL", null, ["callee:00c57ab0:8"]]
- 0058188c bytes f5651994
+ 005a3fcc bytes b9ce1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa203c90f0cc228f8a9ce721456f63c9"></a>

### [`0058190c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md) → [`005a404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md) FUN_005a404c

採用 · 移動量 `+0x22740` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 59.09% / 新版 59.09%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058190c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058190c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581910"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058190c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581910",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a4078"
      ]
    ]
  ],
  "added": [
    [
      "005a404c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a4050",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a4064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a4078"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058190c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md#insn-0058190c) · [`00581910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md#insn-00581910) · [`00581924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md#insn-00581924)

~~~diff
- 0058190c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058190c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058190c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0058190c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0058190c bytes fd7bbea9
- 00581910 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00581910 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00581910 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00581910 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00581910 bytes f44f01a9
- 00581924 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00581924 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00581924 bytes a10000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7cc68a363bc7b2a05b336b69be043e2"></a>

### [`00581aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581aec.md) → [`005a422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md) FUN_005a422c

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00581964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581964.md) [`00581e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581e14.md) [`007726fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007726fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`005a40a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a40a4.md) [`005a4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4554.md) [`0079cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cbd0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00581aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a422c"
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
      "unmatched:00581aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581af8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00581afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005a422c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a4238",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005a423c",
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

- 旧版 [`00581aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581aec.md#insn-00581aec) · [`00581afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581aec.md#insn-00581afc)
- 新版 [`005a422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a422c.md#insn-005a422c)

~~~diff
- 00581aec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00581aec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00581aec ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00581aec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00581aec bytes fd7bbfa9
- 00581afc ["INT_ADD", "register:40f0:8", ["const:581afc:8", "const:4:8"]]
- 00581afc ["CALL", null, ["ram:418c38:8"]]
- 00581afc bytes 4f5cfa97
+ 005a422c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005a422c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005a422c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005a422c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005a422c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6593b725286c922f48da3f663ea5aed8"></a>

### [`00581cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md) → [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md) FUN_005a4418

採用 · 移動量 `+0x22740` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 19件 [`00580ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00580/00580ba0.md) [`00581b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581b20.md) [`00772a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/00772a60.md) [`007730b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00773/007730b8.md) [`00775b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00775/00775b20.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 19件 [`005a32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a32e0.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md) [`0079cf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cf34.md) [`0079d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d58c.md) [`0079fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fff4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00581cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a4418"
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
      "unmatched:00581cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581ce4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00581ce8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005a4418",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a4424",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005a4428",
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

- 旧版 [`00581cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md#insn-00581cd8) · [`00581ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cd8.md#insn-00581ce8)
- 新版 [`005a4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4418.md#insn-005a4418)

~~~diff
- 00581cd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00581cd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00581cd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00581cd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00581cd8 bytes fd7bbfa9
- 00581ce8 ["INT_ADD", "register:40f0:8", ["const:581ce8:8", "const:4:8"]]
- 00581ce8 ["CALL", null, ["ram:418c38:8"]]
- 00581ce8 bytes d45bfa97
+ 005a4418 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005a4418 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005a4418 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005a4418 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005a4418 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ff7fe12f39650a7cdcd92592982c967"></a>

### [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md) → [`005a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a44c8.md) FUN_005a44c8

採用 · 移動量 `+0x22740` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00581760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581760.md) [`005818b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/005818b0.md) [`0058190c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/0058190c.md) [`00581aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581aa8.md) [`005822bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/005822bc.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 8件 [`005a3ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ea0.md) [`005a3ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a3/005a3ff0.md) [`005a404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a404c.md) [`005a41e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a41e8.md) [`005a49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a49fc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 25.00% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00581d8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00581d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00581dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a44ec"
      ]
    ]
  ],
  "added": [
    [
      "005a44c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005a44cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a4508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005a44ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md#insn-00581d88) · [`00581d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md#insn-00581d8c) · [`00581dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581d88.md#insn-00581dc8)

~~~diff
- 00581d88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00581d88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00581d88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00581d88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00581d88 bytes fd7bbda9
- 00581d8c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00581d8c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00581d8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00581d8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00581d8c bytes f65701a9
- 00581dc8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00581dc8 bytes 20ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b1557544c9dbaf5378b655b210cb460"></a>

### [`00582d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582d1c.md) → [`005a74f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md) FUN_005a74f4

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0096f440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096f440.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`009a4f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a4/009a4f24.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a7514"
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
      "unmatched:00582d3c",
      "DATA",
      [
        "storage",
        "00bf19b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7514",
      "DATA",
      [
        "storage",
        "00c6e9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582d1c.md#insn-00582d3c) · [`00582d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582d1c.md#insn-00582d30)
- 新版 [`005a7514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md#insn-005a7514) · [`005a7508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a74f4.md#insn-005a7508)

~~~diff
- 00582d3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00582d3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00582d3c bytes 880200f9
+ 005a7514 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 005a7514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005a7514 bytes 880200f9
- 00582d30 ["INT_ADD", "register:40f0:8", ["const:582d30:8", "const:4:8"]]
- 00582d30 ["CALL", null, ["callee:0059b8c8:8"]]
+ 005a7508 ["INT_ADD", "register:40f0:8", ["const:5a7508:8", "const:4:8"]]
+ 005a7508 ["CALL", null, ["callee:0059b8c8:8"]]
- 00582d30 bytes b0d8ff97
+ 005a7508 bytes f0d0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09f11061b7ab1397af274202ae1f1ad"></a>

### [`00582e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e84.md) → [`005a765c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a765c.md) FUN_005a765c

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582e88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00582e84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00582e88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00582e98",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a765c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a7660",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a7670",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e84.md#insn-00582e84) · [`00582e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e84.md#insn-00582e88) · [`00582ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582e84.md#insn-00582ea4)

~~~diff
- 00582e84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00582e84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00582e84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00582e84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00582e84 bytes fd7bbea9
- 00582e88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00582e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00582e88 bytes f30b00f9
- 00582ea4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00582ea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00582ea4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f39d7d47c7d428d8265d4984bbedf6"></a>

### [`00582f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582f68.md) → [`005a7740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7740.md) FUN_005a7740

採用 · 移動量 `+0x247d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 35.29% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00582f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00582f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00582f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00582f70",
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
      "005a7740",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005a7744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005a7748",
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

- 旧版 [`00582f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582f68.md#insn-00582f68) · [`00582f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582f68.md#insn-00582f6c) · [`00582f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582f68.md#insn-00582f70)

~~~diff
- 00582f68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00582f68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00582f68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00582f68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00582f68 bytes fd7bbda9
- 00582f6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00582f6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00582f6c bytes f50b00f9
- 00582f70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00582f70 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00582f70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00582f70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00582f70 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46a57921f3d6920b3b174cb166f697a"></a>

### [`005831d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005831d8.md) → [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md) FUN_005a79b0

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00582ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/00582ff4.md) [`00583240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`005a77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a77cc.md) [`005a7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "005831d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005831d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a79b0"
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
      "unmatched:005831d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005831e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005831e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005a79b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a79bc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005a79c0",
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

- 旧版 [`005831d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005831d8.md#insn-005831d8) · [`005831e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005831d8.md#insn-005831e8)
- 新版 [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md#insn-005a79b0)

~~~diff
- 005831d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005831d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005831d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005831d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005831d8 bytes fd7bbfa9
- 005831e8 ["INT_ADD", "register:40f0:8", ["const:5831e8:8", "const:4:8"]]
- 005831e8 ["CALL", null, ["ram:418c38:8"]]
- 005831e8 bytes 9456fa97
+ 005a79b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005a79b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005a79b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005a79b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005a79b0 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fbdc94d3e77e53ea2e7de990c8f9933"></a>

### [`00583240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md) → [`005a7a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7a18.md) FUN_005a7a18

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005826f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00582/005826f4.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005831d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005831d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005a6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a6/005a6ecc.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a79b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a79b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 43.24% / 新版 39.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00583244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00583244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00583248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00583244",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00583248",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058324c",
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
      "005a7a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005a7a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005a7a24",
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

- 旧版 [`00583244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md#insn-00583244) · [`00583248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md#insn-00583248) · [`0058324c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583240.md#insn-0058324c)

~~~diff
- 00583244 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00583244 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00583244 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00583244 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00583244 bytes fd7b03a9
- 00583248 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00583248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00583248 bytes f92300f9
- 0058324c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0058324c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0058324c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0058324c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058324c bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dab9bafde9406cefe5d883bc1ad4634"></a>

### [`005835bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005835bc.md) → [`005a7d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md) FUN_005a7d94

採用 · 移動量 `+0x247d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

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
      "site": "00583624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a7dfc"
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
      "unmatched:00583624",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7dfc",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005835bc.md#insn-00583624) · [`00583604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/005835bc.md#insn-00583604)
- 新版 [`005a7dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md#insn-005a7dfc) · [`005a7ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md#insn-005a7ddc)

~~~diff
- 00583624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00583624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00583624 bytes 690e00f9
+ 005a7dfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
+ 005a7dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005a7dfc bytes 690e00f9
- 00583604 ["INT_ADD", "register:40f0:8", ["const:583604:8", "const:4:8"]]
- 00583604 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005a7ddc ["INT_ADD", "register:40f0:8", ["const:5a7ddc:8", "const:4:8"]]
+ 005a7ddc ["CALL", null, ["callee:00c57ab0:8"]]
- 00583604 bytes 975e1994
+ 005a7ddc bytes 35bf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d5212f2c8f0d4dabeb522e68d4b1021"></a>

### [`00583d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md) → [`005a84f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md) FUN_005a84f8

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096fb34.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`009a5618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a5/009a5618.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00583d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a8520"
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
      "unmatched:00583d48",
      "DATA",
      [
        "storage",
        "00bf1b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a8520",
      "DATA",
      [
        "storage",
        "00c6eb58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md#insn-00583d48) · [`00583d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583d20.md#insn-00583d3c)
- 新版 [`005a8520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md#insn-005a8520) · [`005a8514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md#insn-005a8514)

~~~diff
- 00583d48 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00583d48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00583d48 bytes a80200f9
+ 005a8520 ["COPY", "tmp:0:8", ["register:40a8:8"]]
+ 005a8520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005a8520 bytes a80200f9
- 00583d3c ["INT_ADD", "register:40f0:8", ["const:583d3c:8", "const:4:8"]]
- 00583d3c ["CALL", null, ["callee:0059b8c8:8"]]
+ 005a8514 ["INT_ADD", "register:40f0:8", ["const:5a8514:8", "const:4:8"]]
+ 005a8514 ["CALL", null, ["callee:0059b8c8:8"]]
- 00583d3c bytes add4ff97
+ 005a8514 bytes edccff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aaeb6d756aa903afae8fc625d0042c2"></a>

### [`00584fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md) → [`005a9720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md) FUN_005a9720

採用 · 移動量 `+0x24740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00585008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058500c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a9748"
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
      "unmatched:0058500c",
      "DATA",
      [
        "storage",
        "00bf1ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a974c",
      "DATA",
      [
        "storage",
        "00c6ecd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00585008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md#insn-00585008) · [`0058500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md#insn-0058500c)
- 新版 [`005a9748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md#insn-005a9748)

~~~diff
- 00585008 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:38:8"]]
- 00585008 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00585008 bytes b43a00b9
- 0058500c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 0058500c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058500c bytes a80200f9
+ 005a9748 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:38:8"]]
+ 005a9748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 005a9748 bytes b43a00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4daa657a8d309539b584949cf22f144d"></a>

### [`0058574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058574c.md) → [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md) FUN_005a9ea4

採用 · 移動量 `+0x24758` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0058558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058558c.md) [`00980108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980108.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0058574c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058574c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005a9ea4"
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
      "unmatched:0058574c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00585758",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0058575c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005a9ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005a9eb0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005a9eb4",
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

- 旧版 [`0058574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058574c.md#insn-0058574c) · [`0058575c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058574c.md#insn-0058575c)
- 新版 [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md#insn-005a9ea4)

~~~diff
- 0058574c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058574c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058574c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0058574c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0058574c bytes fd7bbfa9
- 0058575c ["INT_ADD", "register:40f0:8", ["const:58575c:8", "const:4:8"]]
- 0058575c ["CALL", null, ["ram:418c38:8"]]
- 0058575c bytes 374dfa97
+ 005a9ea4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005a9ea4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005a9ea4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005a9ea4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005a9ea4 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f57bd100378c664221a2089672f911d"></a>

### [`005858e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005858e4.md) → [`005aa03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa03c.md) FUN_005aa03c

採用 · 移動量 `+0x24758` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005857bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005857bc.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 11.11% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058590c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00585968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005aa064"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0058590c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005858e4.md#insn-0058590c) · [`00585968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005858e4.md#insn-00585968) · [`00585988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005858e4.md#insn-00585988)

~~~diff
- 0058590c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0058590c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058590c bytes 6002803d
- 00585968 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00585968 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:48:8"]]
- 00585968 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00585968 bytes 698204f8
- 00585988 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00585988 ["RETURN", null, ["register:0:8"]]
- 00585988 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df490889e2d79307e933862575b3b814"></a>

### [`005859d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md) → [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) FUN_005aa130

採用 · 移動量 `+0x24758` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`005857bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005857bc.md) [`00585ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/00585ea0.md) [`00587008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587008.md) [`0071d8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d8c4.md) [`0071e020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e020.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 12件 [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`005aa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md) [`005ab760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md) [`00747a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747a70.md) [`007481cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007481cc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "005859d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005859d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005aa130"
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
      "unmatched:005859d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005859e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005859e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005aa130",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005aa13c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005aa140",
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

- 旧版 [`005859d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md#insn-005859d8) · [`005859e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md#insn-005859e8)
- 新版 [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md#insn-005aa130)

~~~diff
- 005859d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005859d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005859d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005859d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005859d8 bytes fd7bbfa9
- 005859e8 ["INT_ADD", "register:40f0:8", ["const:5859e8:8", "const:4:8"]]
- 005859e8 ["CALL", null, ["ram:418c38:8"]]
- 005859e8 bytes 944cfa97
+ 005aa130 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005aa130 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005aa130 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005aa130 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005aa130 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0894059623d15fda1c865c9980cf7479"></a>

### [`005866f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md) → [`005aae48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md) FUN_005aae48

採用 · 移動量 `+0x24758` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00586718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058671c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00586728"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058671c",
      "DATA",
      [
        "storage",
        "00bf1e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aae74",
      "DATA",
      [
        "storage",
        "00c6ee48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md#insn-00586718) · [`0058671c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md#insn-0058671c) · [`00586728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md#insn-00586728)

~~~diff
- 00586718 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:38:8"]]
- 00586718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00586718 bytes b43a00b9
- 0058671c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 0058671c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058671c bytes a80200f9
- 00586728 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:50:8"]]
- 00586728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00586728 bytes a82a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83f59e89356f0adf75c947f1a669d09d"></a>

### [`00586994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586994.md) → [`005ab0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0ec.md) FUN_005ab0ec

採用 · 移動量 `+0x24758` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.89% / 新版 38.89%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005869b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005869b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005869b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005869b8",
      "DATA",
      [
        "storage",
        "00bf1f28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005869c8",
      "DATA",
      [
        "storage",
        "00bf1e78",
        null,
        null
      ]
    ],
    [
      "unmatched:005869d0",
      "READ",
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
      "005ab110",
      "DATA",
      [
        "storage",
        "00c6ef50",
        null,
        "undefined *"
      ]
    ],
    [
      "005ab120",
      "DATA",
      [
        "storage",
        "00c6eea0",
        null,
        null
      ]
    ],
    [
      "005ab128",
      "READ",
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

- 旧版 [`005869b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586994.md#insn-005869b4) · [`005869b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586994.md#insn-005869b8) · [`005869c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586994.md#insn-005869c4)

~~~diff
- 005869b4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005869b4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005869b4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005869b4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005869b4 bytes 1ffc00a9
- 005869b8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005869b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005869b8 bytes 080000f9
- 005869c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 005869c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005869c4 bytes 600600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c70e517035fdcda99f94316fedc1de"></a>

### [`005869dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005869dc.md) → [`005ab134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md) FUN_005ab134

採用 · 移動量 `+0x24758` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 44.44% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00586a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005ab164"
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
      "unmatched:00586a0c",
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
      "005ab164",
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

- 旧版 [`00586a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005869dc.md#insn-00586a0c) · [`005869f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005869dc.md#insn-005869f8)
- 新版 [`005ab164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md#insn-005ab164) · [`005ab150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md#insn-005ab150)

~~~diff
- 00586a0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00586a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00586a0c bytes 680200f9
+ 005ab164 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005ab164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005ab164 bytes 680200f9
- 005869f8 ["INT_ADD", "register:40f0:8", ["const:5869f8:8", "const:4:8"]]
- 005869f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005ab150 ["INT_ADD", "register:40f0:8", ["const:5ab150:8", "const:4:8"]]
+ 005ab150 ["CALL", null, ["callee:00c57ab0:8"]]
- 005869f8 bytes 9a511994
+ 005ab150 bytes 58b21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e9ede2e91bcc2a1405bfce1570fab0"></a>

### [`00586aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586aa0.md) → [`005ab1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md) FUN_005ab1f8

採用 · 移動量 `+0x24758` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 58.33% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00586aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005ab244"
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
      "unmatched:00586aec",
      "DATA",
      [
        "storage",
        "00bf0a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab244",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586aa0.md#insn-00586aec) · [`00586abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586aa0.md#insn-00586abc)
- 新版 [`005ab244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md#insn-005ab244) · [`005ab214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md#insn-005ab214)

~~~diff
- 00586aec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00586aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00586aec bytes 690200f9
+ 005ab244 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005ab244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005ab244 bytes 690200f9
- 00586abc ["INT_ADD", "register:40f0:8", ["const:586abc:8", "const:4:8"]]
- 00586abc ["CALL", null, ["callee:00c57ab0:8"]]
+ 005ab214 ["INT_ADD", "register:40f0:8", ["const:5ab214:8", "const:4:8"]]
+ 005ab214 ["CALL", null, ["callee:00c57ab0:8"]]
- 00586abc bytes 69511994
+ 005ab214 bytes 27b21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02a718f08015b6f78b044fe926ad087f"></a>

### [`00587858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587858.md) → [`005abfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md) FUN_005abfb0

採用 · 移動量 `+0x24758` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4e8.md) · 呼出先 1件 [`00578ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578ff0.md)
- 新版 呼出元 1件 [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00587858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00587858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058785c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00587858",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058785c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00587860",
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
      "005abfb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005abfb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005abfb8",
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

- 旧版 [`00587858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587858.md#insn-00587858) · [`0058785c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587858.md#insn-0058785c) · [`00587860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587858.md#insn-00587860)

~~~diff
- 00587858 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00587858 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00587858 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00587858 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00587858 bytes fd7bbda9
- 0058785c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0058785c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0058785c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0058785c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058785c bytes f65701a9
- 00587860 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00587860 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00587860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00587860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00587860 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d60e4968f8d3a80339e4df391fb308b3"></a>

### [`00588c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588c84.md) → [`005ad248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md) FUN_005ad248

採用 · 移動量 `+0x245c4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 57.14% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00588cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005ad298"
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
      "unmatched:00588cd4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005ad298",
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

- 旧版 [`00588cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588c84.md#insn-00588cd4) · [`00588c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588c84.md#insn-00588c98)
- 新版 [`005ad298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md#insn-005ad298) · [`005ad25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad248.md#insn-005ad25c)

~~~diff
- 00588cd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588cd4 ["INT_ADD", "register:40f0:8", ["const:588cd4:8", "const:4:8"]]
- 00588cd4 ["CALLIND", null, ["register:0:8"]]
- 00588cd4 bytes 00013fd6
+ 005ad298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad298 ["INT_ADD", "register:40f0:8", ["const:5ad298:8", "const:4:8"]]
+ 005ad298 ["CALLIND", null, ["register:0:8"]]
+ 005ad298 bytes 00013fd6
- 00588c98 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00588c98 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00588c98 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00588c98 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 005ad25c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 005ad25c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 005ad25c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 005ad25c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00588c98 bytes 68000036
+ 005ad25c bytes 68000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013fab32d5d14292f1d28d6f277f4b1f"></a>

### [`00588ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588ce8.md) → [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) FUN_005ad2ac

採用 · 移動量 `+0x245c4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058ff20.md) · 呼出先 2件 [`0058b17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b17c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 2件 [`005af740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 50.00% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00588d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005ad308"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00588d9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00588d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00588d9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ad374"
      ]
    ]
  ],
  "added": [
    [
      "005ad308",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005ad360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ad374"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588ce8.md#insn-00588d44) · [`00588d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588ce8.md#insn-00588d9c)
- 新版 [`005ad308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md#insn-005ad308)

~~~diff
- 00588d44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00588d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00588d44 bytes e81300f9
- 00588d9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00588d9c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00588d9c bytes a1000054
+ 005ad308 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
+ 005ad308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005ad308 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-365f19b80c7958f50a5e13651e868ff0"></a>

### [`00588f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md) → [`005ad4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md) FUN_005ad4d0

採用 · 移動量 `+0x245c4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0057753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 37.84% / 新版 37.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00588f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00588f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00588f10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00588f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00588f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00588f30",
      "DATA",
      [
        "storage",
        "00bf20f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad4d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005ad4d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005ad4f4",
      "DATA",
      [
        "storage",
        "00c6f118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md#insn-00588f0c) · [`00588f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md#insn-00588f10) · [`00588f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588f0c.md#insn-00588f30)

~~~diff
- 00588f0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00588f0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00588f0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00588f0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00588f0c bytes fd7bbea9
- 00588f10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00588f10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00588f10 bytes f30b00f9
- 00588f30 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00588f30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00588f30 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5577f28c7338399f1f17387a1987b16"></a>

### [`00588fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588fa0.md) → [`005ad564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md) FUN_005ad564

採用 · 移動量 `+0x245c4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00588fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005ad580"
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
      "unmatched:00588fbc",
      "DATA",
      [
        "storage",
        "00bf2138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad580",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588fa0.md#insn-00588fbc) · [`00588fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588fa0.md#insn-00588fb4)
- 新版 [`005ad580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md#insn-005ad580) · [`005ad578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md#insn-005ad578)

~~~diff
- 00588fbc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00588fbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00588fbc bytes 090000f9
+ 005ad580 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 005ad580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005ad580 bytes 090000f9
- 00588fb4 ["COPY", "register:4048:8", ["const:bf2000:8"]]
+ 005ad578 ["COPY", "register:4048:8", ["const:c6f000:8"]]
- 00588fb4 bytes 493300d0
+ 005ad578 bytes 093600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02715de1972660d11bf2cabe88a25849"></a>

### [`0058b17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b17c.md) → [`005af740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af740.md) FUN_005af740

採用 · 移動量 `+0x245c4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00588ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00588/00588ce8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.28% / 新版 75.28%

CFGの説明率　旧版 31.25% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058b19c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005af760"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0058b1a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058b19c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058b1a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005af87c"
      ]
    ],
    [
      "unmatched:0058b1b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005af794"
      ]
    ]
  ],
  "added": [
    [
      "005af760",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005af764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005af87c"
      ]
    ],
    [
      "005af77c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005af794"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b17c.md#insn-0058b19c) · [`0058b1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b17c.md#insn-0058b1a0) · [`0058b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b17c.md#insn-0058b1b8)

~~~diff
- 0058b19c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0058b19c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0058b19c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0058b19c bytes a8831ff8
- 0058b1a0 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0058b1a0 bytes c0080054
- 0058b1b8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0058b1b8 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc671a261315b8b2701e63948edfbdb2"></a>

### [`0058c56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c56c.md) → [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) FUN_005b0b9c

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0058dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058dabc.md) [`0058ead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ead0.md) [`005922a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005922a8.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0058c5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c5d8.md)
- 新版 呼出元 3件 [`005b20ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md) [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) [`005b68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d8.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005b0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058c56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058c56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058c570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058c56c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058c570",
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
      "005b0b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b0ba0",
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

- 旧版 [`0058c56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c56c.md#insn-0058c56c) · [`0058c570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c56c.md#insn-0058c570)
- 新版 [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md#insn-005b0b9c)

~~~diff
- 0058c56c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058c56c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058c56c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0058c56c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0058c56c bytes fd7bbea9
- 0058c570 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0058c570 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0058c570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0058c570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058c570 bytes f44f01a9
+ 005b0b9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005b0b9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005b0b9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005b0b9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005b0b9c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72f7c2da9801d5a08777b89befe10e23"></a>

### [`0058cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md) → [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) FUN_005b1368

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008167b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/008167b4.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 4件 [`00590bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md) [`00590c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md) [`00847a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847a50.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008485ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008485ac.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 4件 [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) [`00879d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 58.33% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058cd38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058cd38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058cd3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058cd38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058cd3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058cd64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b13a4"
      ]
    ]
  ],
  "added": [
    [
      "005b1368",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b136c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b1394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b13a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md#insn-0058cd38) · [`0058cd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md#insn-0058cd3c) · [`0058cd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md#insn-0058cd64)

~~~diff
- 0058cd38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058cd38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058cd38 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0058cd38 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0058cd38 bytes fd7bbea9
- 0058cd3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0058cd3c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0058cd3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0058cd3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058cd3c bytes f44f01a9
- 0058cd64 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0058cd64 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d78d2add204d4120fd8631fba8643793"></a>

### [`0058de44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058de44.md) → [`005b2474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2474.md) FUN_005b2474

採用 · 移動量 `+0x24630` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0058de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058de3c.md) [`0058f85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f85c.md) · 呼出先 6件 [`00591534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591534.md) [`00591538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591538.md) [`005915d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005915d4.md) [`005915d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005915d8.md) [`008480ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/008480ec.md)
- 新版 呼出元 2件 [`005b246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b246c.md) [`005b3e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e8c.md) · 呼出先 6件 [`005b5b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b64.md) [`005b5b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b68.md) [`005b5c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c04.md) [`005b5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c08.md) [`0087a5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a5a4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 51.79% / 新版 51.79%

CFGの説明率　旧版 5.00% / 新版 4.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058de48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058de48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058de4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058de48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058de4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058de68",
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
      "005b2478",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b247c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b2498",
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

- 旧版 [`0058de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058de44.md#insn-0058de48) · [`0058de4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058de44.md#insn-0058de4c) · [`0058de68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058de44.md#insn-0058de68)

~~~diff
- 0058de48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058de48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058de48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0058de48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058de48 bytes fd7b07a9
- 0058de4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0058de4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0058de4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0058de4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058de4c bytes f44f08a9
- 0058de68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0058de68 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0058de68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0058de68 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d0b41334174202ccc0767c11c4ec60d"></a>

### [`0058e498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e498.md) → [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) FUN_005b2ac8

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 9件 [`0058cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cea4.md) [`0058cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cfe0.md) [`0058e620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e620.md) [`0058e878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e878.md) [`00591830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591830.md)
- 新版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 9件 [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) [`005b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md) [`005b2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md) [`005b5e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 5.56% / 新版 7.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058e49c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058e49c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058e4a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058e49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058e4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058e4a4",
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
      "005b2acc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005b2ad0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005b2ad4",
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

- 旧版 [`0058e49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e498.md#insn-0058e49c) · [`0058e4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e498.md#insn-0058e4a0) · [`0058e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e498.md#insn-0058e4a4)

~~~diff
- 0058e49c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0058e49c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0058e49c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0058e49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058e49c bytes fd7b04a9
- 0058e4a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0058e4a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0058e4a0 bytes f72b00f9
- 0058e4a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0058e4a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0058e4a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0058e4a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058e4a4 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01eaf6952fa3cd8379250960d27f8195"></a>

### [`0058ecd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md) → [`005b3308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md) FUN_005b3308

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0058ead0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ead0.md) [`0058ecd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd4.md) [`0059198c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059198c.md) · 呼出先 6件 [`00591aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591aec.md) [`00591af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591af0.md) [`00591b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b7c.md) [`00591b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b80.md) [`0084859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/0084859c.md)
- 新版 呼出元 3件 [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) [`005b3304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3304.md) [`005b5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md) · 呼出先 6件 [`005b611c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b611c.md) [`005b6120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6120.md) [`005b61ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b61ac.md) [`005b61b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b61b0.md) [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 17.65% / 新版 15.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058ecf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058ed04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058ed04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0058ecf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:0058ed04",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0058ed04",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b3328",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "005b3334",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3334",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ecf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md#insn-0058ecf8) · [`0058ed04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md#insn-0058ed04) · [`0058ed0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md#insn-0058ed0c)

~~~diff
- 0058ecf8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0058ecf8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0058ecf8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0058ecf8 bytes a8831ff8
- 0058ed04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0058ed04 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 0058ed04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0058ed04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0058ed04 bytes e80303a9
- 0058ed0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 0058ed0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058ed0c bytes e82300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d7cb02be32f1afcff23cff6c1b26971"></a>

### [`00590780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590780.md) → [`005b4db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md) FUN_005b4db0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 37.50% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005907a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b4dd8"
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
      "unmatched:005907a8",
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
      "005b4dd8",
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

- 旧版 [`005907a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590780.md#insn-005907a8) · [`00590794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590780.md#insn-00590794)
- 新版 [`005b4dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md#insn-005b4dd8) · [`005b4dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4db0.md#insn-005b4dc4)

~~~diff
- 005907a8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 005907a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005907a8 bytes 680200f9
+ 005b4dd8 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005b4dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b4dd8 bytes 680200f9
- 00590794 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00590794 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005b4dc4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005b4dc4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00590794 bytes 330200b4
+ 005b4dc4 bytes 330200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65fc005e258f67dd764a9f646a71e96f"></a>

### [`00590c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c94.md) → [`005b52c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b52c4.md) FUN_005b52c4

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00590cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b52e8"
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
      "unmatched:00590cb8",
      "DATA",
      [
        "storage",
        "00bf2288",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00590cbc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00590cc0",
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
      "005b52e8",
      "DATA",
      [
        "storage",
        "00c6f2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b52ec",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b52f0",
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

- 旧版 [`00590cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c94.md#insn-00590cb8) · [`00590cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c94.md#insn-00590cc4)
- 新版 [`005b52e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b52c4.md#insn-005b52e8)

~~~diff
- 00590cb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00590cb8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00590cb8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00590cb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00590cb8 bytes 082400a9
- 00590cc4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00590cc4 ["RETURN", null, ["register:0:8"]]
- 00590cc4 bytes c0035fd6
+ 005b52e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b52e8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b52e8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b52e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b52e8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8c56864c36ceeec80a360c29a676d10"></a>

### [`00590d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d18.md) → [`005b5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5348.md) FUN_005b5348

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b536c"
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
      "unmatched:00590d3c",
      "DATA",
      [
        "storage",
        "00bf2318",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00590d40",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00590d44",
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
      "005b536c",
      "DATA",
      [
        "storage",
        "00c6f340",
        null,
        "undefined *"
      ]
    ],
    [
      "005b5370",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b5374",
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

- 旧版 [`00590d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d18.md#insn-00590d3c) · [`00590d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590d18.md#insn-00590d48)
- 新版 [`005b536c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5348.md#insn-005b536c)

~~~diff
- 00590d3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00590d3c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00590d3c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00590d3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00590d3c bytes 082400a9
- 00590d48 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00590d48 ["RETURN", null, ["register:0:8"]]
- 00590d48 bytes c0035fd6
+ 005b536c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b536c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b536c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b536c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b536c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946bab7b1436d53ccdd87ac3b038ba6c"></a>

### [`00590dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590dc4.md) → [`005b53f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b53f4.md) FUN_005b53f4

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5400"
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
      "unmatched:00590dd0",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5400",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590dc4.md#insn-00590dd0) · [`00590dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590dc4.md#insn-00590dc8)
- 新版 [`005b5400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b53f4.md#insn-005b5400)

~~~diff
- 00590dd0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00590dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00590dd0 bytes 090000f9
+ 005b5400 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 005b5400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005b5400 bytes 090000f9
- 00590dc8 ["COPY", "register:4048:8", ["const:bf2000:8"]]
- 00590dc8 bytes 093300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc2a19df5c87acd93e3e2edf2bbeb9bf"></a>

### [`00590ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ea0.md) → [`005b54d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b54d0.md) FUN_005b54d0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00590eac",
      "DATA",
      [
        "storage",
        "00bf23a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b54dc",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ea0.md#insn-00590eac) · [`00590ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ea0.md#insn-00590ec4) · [`00590ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590ea0.md#insn-00590ec8)

~~~diff
- 00590eac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00590eac ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00590eac ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00590eac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00590eac bytes 292000a9
- 00590ec4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00590ec4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:20:8"]]
- 00590ec4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00590ec4 bytes 290002f8
- 00590ec8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00590ec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00590ec8 bytes 2000813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f82bfcedb5bc047ccd6002aae6bec539"></a>

### [`00590f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f64.md) → [`005b5594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5594.md) FUN_005b5594

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00590f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b55b8"
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
      "unmatched:00590f88",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00590f8c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00590f90",
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
      "005b55b8",
      "DATA",
      [
        "storage",
        "00c6f460",
        null,
        "undefined *"
      ]
    ],
    [
      "005b55bc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b55c0",
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

- 旧版 [`00590f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f64.md#insn-00590f88) · [`00590f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f64.md#insn-00590f94)
- 新版 [`005b55b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5594.md#insn-005b55b8)

~~~diff
- 00590f88 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00590f88 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00590f88 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00590f88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00590f88 bytes 082400a9
- 00590f94 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00590f94 ["RETURN", null, ["register:0:8"]]
- 00590f94 bytes c0035fd6
+ 005b55b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b55b8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b55b8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b55b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b55b8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-059c01ba35536ff5407c1596380475c9"></a>

### [`00590f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f98.md) → [`005b55c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55c8.md) FUN_005b55c8

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00590fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b55d4"
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
      "unmatched:00590fa4",
      "DATA",
      [
        "storage",
        "00bf2438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b55d4",
      "DATA",
      [
        "storage",
        "00c6f460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f98.md#insn-00590fa4) · [`00590fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590f98.md#insn-00590fa8)
- 新版 [`005b55d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55c8.md#insn-005b55d4)

~~~diff
- 00590fa4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00590fa4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00590fa4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00590fa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00590fa4 bytes 292000a9
- 00590fa8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00590fa8 ["RETURN", null, ["register:0:8"]]
- 00590fa8 bytes c0035fd6
+ 005b55d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005b55d4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 005b55d4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 005b55d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b55d4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abde39ee31708390eb4819d45761b2e6"></a>

### [`005910a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910a0.md) → [`005b56d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56d0.md) FUN_005b56d0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "005910c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005910c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b56f4"
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
      "unmatched:005910c4",
      "DATA",
      [
        "storage",
        "00bf2538",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005910c8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005910cc",
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
      "005b56f4",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ],
    [
      "005b56f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b56fc",
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

- 旧版 [`005910c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910a0.md#insn-005910c4) · [`005910d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005910a0.md#insn-005910d0)
- 新版 [`005b56f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b56d0.md#insn-005b56f4)

~~~diff
- 005910c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005910c4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005910c4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005910c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005910c4 bytes 082400a9
- 005910d0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005910d0 ["RETURN", null, ["register:0:8"]]
- 005910d0 bytes c0035fd6
+ 005b56f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b56f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b56f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b56f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b56f4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515d1c0c6983a3f0ff7801641faf515a"></a>

### [`00591154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591154.md) → [`005b5784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5784.md) FUN_005b5784

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b57a8"
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
      "unmatched:00591178",
      "DATA",
      [
        "storage",
        "00bf25b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0059117c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591180",
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
      "005b57a8",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b57ac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b57b0",
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

- 旧版 [`00591178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591154.md#insn-00591178) · [`00591184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591154.md#insn-00591184)
- 新版 [`005b57a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5784.md#insn-005b57a8)

~~~diff
- 00591178 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591178 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591178 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591178 bytes 082400a9
- 00591184 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591184 ["RETURN", null, ["register:0:8"]]
- 00591184 bytes c0035fd6
+ 005b57a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b57a8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b57a8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b57a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b57a8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d86c0026b061948747225282c8880efc"></a>

### [`00591454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591454.md) → [`005b5a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a84.md) FUN_005b5a84

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00591460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5a90"
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
      "unmatched:00591460",
      "DATA",
      [
        "storage",
        "00bf2688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5a90",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591454.md#insn-00591460) · [`00591464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591454.md#insn-00591464)
- 新版 [`005b5a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a84.md#insn-005b5a90)

~~~diff
- 00591460 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00591460 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00591460 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00591460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591460 bytes 292000a9
- 00591464 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591464 ["RETURN", null, ["register:0:8"]]
- 00591464 bytes c0035fd6
+ 005b5a90 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005b5a90 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 005b5a90 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 005b5a90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b5a90 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-685e556ea932ebaa5e52a62ce3e93abf"></a>

### [`00591620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591620.md) → [`005b5c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c50.md) FUN_005b5c50

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00591644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5c74"
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
      "unmatched:00591644",
      "DATA",
      [
        "storage",
        "00bf2818",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00591648",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059164c",
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
      "005b5c74",
      "DATA",
      [
        "storage",
        "00c6f840",
        null,
        "undefined *"
      ]
    ],
    [
      "005b5c78",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b5c7c",
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

- 旧版 [`00591644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591620.md#insn-00591644) · [`00591650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591620.md#insn-00591650)
- 新版 [`005b5c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c50.md#insn-005b5c74)

~~~diff
- 00591644 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591644 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591644 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591644 bytes 082400a9
- 00591650 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591650 ["RETURN", null, ["register:0:8"]]
- 00591650 bytes c0035fd6
+ 005b5c74 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b5c74 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b5c74 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b5c74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b5c74 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0a0ad741211ad66175e3674eed354d"></a>

### [`00591670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591670.md) → [`005b5ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5ca0.md) FUN_005b5ca0

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 9.52% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005916a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005916f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00591710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b5cc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005916e4"
      ]
    ],
    [
      "005b5ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005916e4"
      ]
    ],
    [
      "005b5cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005916e4"
      ]
    ]
  ],
  "added": [
    [
      "005b5cc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b5d14"
      ]
    ],
    [
      "005b5ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b5d14"
      ]
    ],
    [
      "005b5cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b5d14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005916a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591670.md#insn-005916a8) · [`005916e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591670.md#insn-005916e0) · [`005916f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591670.md#insn-005916f0)

~~~diff
- 005916a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005916a8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005916a8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005916a8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 005916a8 bytes 08b18a9a
- 005916e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005916e0 ["INT_ADD", "register:40f0:8", ["const:5916e0:8", "const:4:8"]]
- 005916e0 ["CALLIND", null, ["register:0:8"]]
- 005916e0 bytes 00013fd6
- 005916f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005916f0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 005916f0 bytes 41010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e0387e087f9038c0316ab2b5ac2654"></a>

### [`00591748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591748.md) → [`005b5d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d78.md) FUN_005b5d78

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0059176c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059176c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5d9c"
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
      "unmatched:0059176c",
      "DATA",
      [
        "storage",
        "00bf2898",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00591770",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591774",
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
      "005b5d9c",
      "DATA",
      [
        "storage",
        "00c6f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b5da0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b5da4",
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

- 旧版 [`0059176c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591748.md#insn-0059176c) · [`00591778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591748.md#insn-00591778)
- 新版 [`005b5d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5d78.md#insn-005b5d9c)

~~~diff
- 0059176c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0059176c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0059176c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0059176c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0059176c bytes 082400a9
- 00591778 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591778 ["RETURN", null, ["register:0:8"]]
- 00591778 bytes c0035fd6
+ 005b5d9c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b5d9c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b5d9c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b5d9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b5d9c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50c69a911150382786d66140d8e3161e"></a>

### [`005917e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917e0.md) → [`005b5e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e10.md) FUN_005b5e10

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005917e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005917e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005917e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005917e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005917e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591804",
      "DATA",
      [
        "storage",
        "00bf2918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b5e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b5e34",
      "DATA",
      [
        "storage",
        "00c6f940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005917e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917e0.md#insn-005917e0) · [`005917e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917e0.md#insn-005917e4) · [`00591804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/005917e0.md#insn-00591804)

~~~diff
- 005917e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005917e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005917e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005917e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005917e0 bytes fd7bbea9
- 005917e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005917e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005917e4 bytes f30b00f9
- 00591804 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00591804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591804 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87dfc5906aedc9d6f86ea3ba9289298f"></a>

### [`00591818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591818.md) → [`005b5e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e48.md) FUN_005b5e48

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00591820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5e50"
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
      "unmatched:00591820",
      "DATA",
      [
        "storage",
        "00bf2918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e50",
      "DATA",
      [
        "storage",
        "00c6f940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591818.md#insn-00591820) · [`00591828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591818.md#insn-00591828) · [`0059182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591818.md#insn-0059182c)

~~~diff
- 00591820 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00591820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591820 bytes 280000f9
- 00591828 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00591828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00591828 bytes 2080803c
- 0059182c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0059182c ["RETURN", null, ["register:0:8"]]
- 0059182c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-547ddeefffc60e62ac9e951ba4abc6cd"></a>

### [`00591934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591934.md) → [`005b5f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f64.md) FUN_005b5f64

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059195c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5f88"
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
      "unmatched:00591958",
      "DATA",
      [
        "storage",
        "00bf29a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00591960",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591964",
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
      "005b5f88",
      "DATA",
      [
        "storage",
        "00c6f9d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b5f90",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b5f94",
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

- 旧版 [`00591958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591934.md#insn-00591958) · [`0059195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591934.md#insn-0059195c) · [`00591968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591934.md#insn-00591968)

~~~diff
- 00591958 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00591958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591958 bytes 080000f9
- 0059195c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 0059195c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0059195c bytes 0080803c
- 00591968 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591968 ["RETURN", null, ["register:0:8"]]
- 00591968 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0513439a5d726cdd34a5f0ed4a8da478"></a>

### [`0059196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059196c.md) → [`005b5f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5f9c.md) FUN_005b5f9c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059197c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b5fa4"
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
      "unmatched:00591974",
      "DATA",
      [
        "storage",
        "00bf29a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5fa4",
      "DATA",
      [
        "storage",
        "00c6f9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059196c.md#insn-00591974) · [`0059197c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059196c.md#insn-0059197c) · [`00591980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059196c.md#insn-00591980)

~~~diff
- 00591974 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00591974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591974 bytes 280000f9
- 0059197c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 0059197c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0059197c bytes 2080803c
- 00591980 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591980 ["RETURN", null, ["register:0:8"]]
- 00591980 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6fd34cc3dd5f0fbe11531f480077552"></a>

### [`0059198c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059198c.md) → [`005b5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md) FUN_005b5fbc

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0058ecd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058ecd8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b3308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 36.36% / 新版 34.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005919e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00591a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00591a44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005919e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00591a38"
      ]
    ],
    [
      "unmatched:00591a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00591a38"
      ]
    ],
    [
      "005b6048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00591a38"
      ]
    ]
  ],
  "added": [
    [
      "005b6018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b6068"
      ]
    ],
    [
      "005b603c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b6068"
      ]
    ],
    [
      "005b6048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b6068"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005919e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059198c.md#insn-005919e8) · [`00591a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059198c.md#insn-00591a0c) · [`00591a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/0059198c.md#insn-00591a34)

~~~diff
- 005919e8 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 005919e8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 005919e8 bytes 8a0200b4
- 00591a0c ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00591a0c bytes 60010054
- 00591a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00591a34 ["INT_ADD", "register:40f0:8", ["const:591a34:8", "const:4:8"]]
- 00591a34 ["CALLIND", null, ["register:0:8"]]
- 00591a34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be85a4680107a53e7d2308b0fa52e41e"></a>

### [`00591a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a9c.md) → [`005b60cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60cc.md) FUN_005b60cc

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b60f0"
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
      "unmatched:00591ac0",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b60f0",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a9c.md#insn-00591ac0) · [`00591aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591a9c.md#insn-00591aa4)
- 新版 [`005b60f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b60cc.md#insn-005b60f0)

~~~diff
- 00591ac0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00591ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591ac0 bytes 080000f9
+ 005b60f0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 005b60f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b60f0 bytes 080000f9
- 00591aa4 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00591aa4 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7be88265ff29390836b4458fd9dfdd35"></a>

### [`00591ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ad4.md) → [`005b6104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6104.md) FUN_005b6104

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00591adc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b610c"
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
      "unmatched:00591adc",
      "DATA",
      [
        "storage",
        "00bf2a38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b610c",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ad4.md#insn-00591adc) · [`00591ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ad4.md#insn-00591ae4) · [`00591ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ad4.md#insn-00591ae8)

~~~diff
- 00591adc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00591adc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591adc bytes 280000f9
- 00591ae4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00591ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00591ae4 bytes 2080803c
- 00591ae8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591ae8 ["RETURN", null, ["register:0:8"]]
- 00591ae8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02661487e56724983266a8e42657a48"></a>

### [`00591b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b34.md) → [`005b6164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6164.md) FUN_005b6164

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00591b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591b38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00591b34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591b58",
      "DATA",
      [
        "storage",
        "00bf2ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6164",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b6168",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6188",
      "DATA",
      [
        "storage",
        "00c6fae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b34.md#insn-00591b34) · [`00591b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b34.md#insn-00591b38) · [`00591b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591b34.md#insn-00591b58)

~~~diff
- 00591b34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00591b34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00591b34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00591b34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00591b34 bytes fd7bbea9
- 00591b38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00591b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00591b38 bytes f30b00f9
- 00591b58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591b58 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591b58 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591b58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591b58 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31748d4a535a1a2ac17e1a760e9a9faa"></a>

### [`00591be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591be8.md) → [`005b6218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6218.md) FUN_005b6218

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b623c"
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
      "unmatched:00591c0c",
      "DATA",
      [
        "storage",
        "00bf2b38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00591c10",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591c14",
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
      "005b623c",
      "DATA",
      [
        "storage",
        "00c6fb60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b6240",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6244",
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

- 旧版 [`00591c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591be8.md#insn-00591c0c) · [`00591c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591be8.md#insn-00591c18)
- 新版 [`005b623c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6218.md#insn-005b623c)

~~~diff
- 00591c0c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591c0c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591c0c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591c0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591c0c bytes 082400a9
- 00591c18 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591c18 ["RETURN", null, ["register:0:8"]]
- 00591c18 bytes c0035fd6
+ 005b623c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b623c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b623c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b623c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b623c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a8703ecaf7597adb7d0fd2f9ef4dee6"></a>

### [`00591c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591c38.md) → [`005b6268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6268.md) FUN_005b6268

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.77% / 新版 69.77%

CFGの説明率　旧版 44.44% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00591c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591c50",
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
      "005b626c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b6270",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6280",
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

- 旧版 [`00591c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591c38.md#insn-00591c3c) · [`00591c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591c38.md#insn-00591c40) · [`00591c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591c38.md#insn-00591c50)

~~~diff
- 00591c3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00591c3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00591c3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00591c3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591c3c bytes fd7b01a9
- 00591c40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00591c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00591c40 bytes f31300f9
- 00591c50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00591c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00591c50 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093e74d3dd4530331eee9ba7dbd1e820"></a>

### [`00591d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d10.md) → [`005b6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6340.md) FUN_005b6340

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00591d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591d14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00591d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591d34",
      "DATA",
      [
        "storage",
        "00bf2bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6340",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b6344",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6364",
      "DATA",
      [
        "storage",
        "00c6fbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d10.md#insn-00591d10) · [`00591d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d10.md#insn-00591d14) · [`00591d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591d10.md#insn-00591d34)

~~~diff
- 00591d10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00591d10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00591d10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00591d10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00591d10 bytes fd7bbea9
- 00591d14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00591d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00591d14 bytes f30b00f9
- 00591d34 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591d34 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591d34 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591d34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591d34 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2565a7edc0e953bfd1f3555d258cf8e"></a>

### [`00591da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591da8.md) → [`005b63d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md) FUN_005b63d8

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00591dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b63fc"
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
      "unmatched:00591dcc",
      "DATA",
      [
        "storage",
        "00bf2c38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00591dd0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00591dd4",
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
      "005b63fc",
      "DATA",
      [
        "storage",
        "00c6fc60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b6400",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b6404",
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

- 旧版 [`00591dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591da8.md#insn-00591dcc) · [`00591dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591da8.md#insn-00591dd8)
- 新版 [`005b63fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b63d8.md#insn-005b63fc)

~~~diff
- 00591dcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00591dcc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00591dcc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00591dcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591dcc bytes 082400a9
- 00591dd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591dd8 ["RETURN", null, ["register:0:8"]]
- 00591dd8 bytes c0035fd6
+ 005b63fc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b63fc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005b63fc ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005b63fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b63fc bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15a033356f8cdd0d2d872476d1a1a87e"></a>

### [`00591ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ddc.md) → [`005b640c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b640c.md) FUN_005b640c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00591de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00591de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b6418"
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
      "unmatched:00591de8",
      "DATA",
      [
        "storage",
        "00bf2c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6418",
      "DATA",
      [
        "storage",
        "00c6fc60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ddc.md#insn-00591de8) · [`00591dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591ddc.md#insn-00591dec)
- 新版 [`005b6418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b640c.md#insn-005b6418)

~~~diff
- 00591de8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00591de8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00591de8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00591de8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00591de8 bytes 292000a9
- 00591dec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00591dec ["RETURN", null, ["register:0:8"]]
- 00591dec bytes c0035fd6
+ 005b6418 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005b6418 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 005b6418 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 005b6418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b6418 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3671d37bed00e502b71fc4035c3341ae"></a>

### [`0059201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059201c.md) → [`005b664c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md) FUN_005b664c

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00591df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591df8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b6428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6428.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00592030"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b6660"
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
      "unmatched:00592030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b66b8"
      ]
    ]
  ],
  "added": [
    [
      "005b6660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b66b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059201c.md#insn-00592030) · [`00592044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059201c.md#insn-00592044)
- 新版 [`005b6660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md#insn-005b6660) · [`005b6674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b664c.md#insn-005b6674)

~~~diff
- 00592030 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00592030 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00592030 bytes d40200b4
+ 005b6660 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 005b6660 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 005b6660 bytes d40200b4
- 00592044 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 005b6674 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00592044 bytes 80010054
+ 005b6674 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cbb799790304a382e0c20db502d511d"></a>

### [`005920a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005920a0.md) → [`005b66d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b66d0.md) FUN_005b66d0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

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
      "site": "005920a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005920a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005920a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005920a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005920a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005920c4",
      "DATA",
      [
        "storage",
        "00bf2d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b66d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b66d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b66f4",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005920a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005920a0.md#insn-005920a0) · [`005920a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005920a0.md#insn-005920a4) · [`005920c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005920a0.md#insn-005920c4)

~~~diff
- 005920a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005920a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005920a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005920a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005920a0 bytes fd7bbea9
- 005920a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005920a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005920a4 bytes f30b00f9
- 005920c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005920c4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005920c4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005920c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005920c4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d5611a073b29760c6803c37c8b05de6"></a>

### [`005926ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005926ec.md) → [`005b6d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d1c.md) FUN_005b6d1c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005926ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005926ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005926f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005926ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005926f0",
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
      "005b6d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b6d20",
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

- 旧版 [`005926ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005926ec.md#insn-005926ec) · [`005926f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/005926ec.md#insn-005926f0)
- 新版 [`005b6d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6d1c.md#insn-005b6d1c)

~~~diff
- 005926ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005926ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005926ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005926ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005926ec bytes fd7bbea9
- 005926f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005926f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005926f0 bytes f30b00f9
+ 005b6d1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005b6d1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005b6d1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005b6d1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005b6d1c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-840ce9269a65e5b4ac16725d9a20e3c3"></a>

### [`0059298c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059298c.md) → [`005b6fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fbc.md) FUN_005b6fbc

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00592998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00592998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b6fc8"
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
      "unmatched:00592998",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6fc8",
      "DATA",
      [
        "storage",
        "00c700c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059298c.md#insn-00592998) · [`0059299c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/0059298c.md#insn-0059299c)
- 新版 [`005b6fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fbc.md#insn-005b6fc8)

~~~diff
- 00592998 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00592998 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00592998 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00592998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00592998 bytes 292000a9
- 0059299c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0059299c ["RETURN", null, ["register:0:8"]]
- 0059299c bytes c0035fd6
+ 005b6fc8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005b6fc8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 005b6fc8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 005b6fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005b6fc8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c95c6a3b77e646a148d3e687ace6ae75"></a>

### [`00592d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592d20.md) → [`005b7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7350.md) FUN_005b7350

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00592d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b7374"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00592d48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00592d44",
      "DATA",
      [
        "storage",
        "00bf31e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00592d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7388"
      ]
    ]
  ],
  "added": [
    [
      "005b7374",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ],
    [
      "005b7378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7388"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592d20.md#insn-00592d44) · [`00592d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592d20.md#insn-00592d48)
- 新版 [`005b7374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7350.md#insn-005b7374)

~~~diff
- 00592d44 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00592d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00592d44 bytes 680200f9
- 00592d48 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00592d48 bytes 80000054
+ 005b7374 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005b7374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b7374 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e686901073a681d390162c54357cc61"></a>

### [`00592f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592f00.md) → [`005b7530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7530.md) FUN_005b7530

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0057b15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057b/0057b15c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0059da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059da08.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 51.61% / 新版 51.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00592fe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0059300c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b7618"
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
      "005b7580",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00593000"
      ]
    ],
    [
      "unmatched:00592fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7678"
      ]
    ],
    [
      "unmatched:00593004",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b7580",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7630"
      ]
    ],
    [
      "005b7618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7678"
      ]
    ],
    [
      "005b7634",
      "READ",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592f00.md#insn-00592fe8) · [`00592ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592f00.md#insn-00592ffc) · [`0059300c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592f00.md#insn-0059300c)

~~~diff
- 00592fe8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00592fe8 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00592fe8 bytes 01030054
- 00592ffc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00592ffc ["RETURN", null, ["register:0:8"]]
- 00592ffc bytes c0035fd6
- 0059300c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0059300c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 0059300c bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f31c4c6650854005f3b28243fdea516"></a>

### [`005932f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005932f8.md) → [`005b7928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7928.md) FUN_005b7928

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005932f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005932f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005932fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005932f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005932fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059331c",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b792c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b794c",
      "DATA",
      [
        "storage",
        "00c702a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005932f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005932f8.md#insn-005932f8) · [`005932fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005932f8.md#insn-005932fc) · [`0059331c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/005932f8.md#insn-0059331c)

~~~diff
- 005932f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005932f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005932f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005932f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005932f8 bytes fd7bbea9
- 005932fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005932fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005932fc bytes f30b00f9
- 0059331c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0059331c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0059331c bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8756314d87f76b5f6f73378956a5f38"></a>

### [`00593488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593488.md) → [`005b7ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ab8.md) FUN_005b7ab8

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058d7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058d/0058d7b4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005934a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b7ad4"
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
      "unmatched:005934a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7ae4"
      ]
    ]
  ],
  "added": [
    [
      "005b7ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7ae4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005934a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593488.md#insn-005934a4) · [`0059349c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593488.md#insn-0059349c)
- 新版 [`005b7ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7ab8.md#insn-005b7ad4)

~~~diff
- 005934a4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 005934a4 bytes 80000054
+ 005b7ad4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 005b7ad4 bytes 80000054
- 0059349c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0059349c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0059349c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0059349c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0059349c bytes 69420091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c24348af77655ea8955aedf0c9dc0a62"></a>

### [`00593800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593800.md) → [`005b7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e30.md) FUN_005b7e30

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00593818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b7e48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0059381c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00593818",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0059381c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e5c"
      ]
    ]
  ],
  "added": [
    [
      "005b7e48",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ],
    [
      "005b7e4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b7e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593800.md#insn-00593818) · [`0059381c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593800.md#insn-0059381c)
- 新版 [`005b7e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e30.md#insn-005b7e48)

~~~diff
- 00593818 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00593818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00593818 bytes 0a0100f9
- 0059381c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0059381c bytes 80000054
+ 005b7e48 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b7e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 005b7e48 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5c6731f36f4ae63bb1be7ce01f49360"></a>

### [`00593844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593844.md) → [`005b7e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e74.md) FUN_005b7e74

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00593868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b7e98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0059388c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00593868",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0059388c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005b7e98",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ],
    [
      "005b7ebc",
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

- 旧版 [`00593868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593844.md#insn-00593868) · [`0059388c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593844.md#insn-0059388c)
- 新版 [`005b7e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7e74.md#insn-005b7e98)

~~~diff
- 00593868 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00593868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00593868 bytes 680200f9
- 0059388c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059388c ["INT_ADD", "register:40f0:8", ["const:59388c:8", "const:4:8"]]
- 0059388c ["CALLIND", null, ["register:0:8"]]
- 0059388c bytes 00013fd6
+ 005b7e98 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005b7e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b7e98 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7306d0b9037f424d24735acbeae149"></a>

### [`00593928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593928.md) → [`005b7f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7f58.md) FUN_005b7f58

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 58.62% / 新版 58.62%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00593928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00593928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059392c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00593928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059392c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00593944",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b7f5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b7f74",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593928.md#insn-00593928) · [`0059392c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593928.md#insn-0059392c) · [`00593944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593928.md#insn-00593944)

~~~diff
- 00593928 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00593928 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00593928 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00593928 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00593928 bytes fd7bbea9
- 0059392c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0059392c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0059392c bytes f30b00f9
- 00593944 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00593944 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00593944 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00593944 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00593944 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-477376942fc73771e26d48cf1d8a08b3"></a>

### [`00593fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593fc8.md) → [`005b85f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b85f8.md) FUN_005b85f8

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 41.18% / 新版 41.18%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00593fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8610"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00593fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00593fe0",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00593fe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8624"
      ]
    ]
  ],
  "added": [
    [
      "005b8610",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8624"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593fc8.md#insn-00593fe0) · [`00593fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593fc8.md#insn-00593fe4)
- 新版 [`005b8610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b85f8.md#insn-005b8610)

~~~diff
- 00593fe0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00593fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00593fe0 bytes 0a0100f9
- 00593fe4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00593fe4 bytes 80000054
+ 005b8610 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b8610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 005b8610 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c92169299ae52341a9500c08fcafb0"></a>

### [`0059400c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059400c.md) → [`005b863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b863c.md) FUN_005b863c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 25.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8660"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00594034"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594030",
      "DATA",
      [
        "storage",
        "00bf33f8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00594034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8674"
      ]
    ]
  ],
  "added": [
    [
      "005b8660",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8674"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059400c.md#insn-00594030) · [`00594034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059400c.md#insn-00594034)
- 新版 [`005b8660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b863c.md#insn-005b8660)

~~~diff
- 00594030 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00594030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00594030 bytes 680200f9
- 00594034 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00594034 bytes 80000054
+ 005b8660 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005b8660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b8660 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dcc2c3c8416fe376f4adc98641da03d"></a>

### [`005945bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005945bc.md) → [`005b8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bec.md) FUN_005b8bec

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "005945d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8c04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005945d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005945d4",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005945d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8c18"
      ]
    ]
  ],
  "added": [
    [
      "005b8c04",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8c18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005945d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005945bc.md#insn-005945d4) · [`005945d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005945bc.md#insn-005945d8)
- 新版 [`005b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8bec.md#insn-005b8c04)

~~~diff
- 005945d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005945d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 005945d4 bytes 0a0100f9
- 005945d8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 005945d8 bytes 80000054
+ 005b8c04 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005b8c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 005b8c04 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0325fab3ea86eed622800614ad91842"></a>

### [`00594600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594600.md) → [`005b8c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c30.md) FUN_005b8c30

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 27.27% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b8c54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00594628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594624",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00594628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8c68"
      ]
    ]
  ],
  "added": [
    [
      "005b8c54",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b8c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8c68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594600.md#insn-00594624) · [`00594628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594600.md#insn-00594628)
- 新版 [`005b8c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8c30.md#insn-005b8c54)

~~~diff
- 00594624 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00594624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00594624 bytes 680200f9
- 00594628 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00594628 bytes 80000054
+ 005b8c54 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 005b8c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005b8c54 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b85e5d4f362ba67a0dfe85eb9a0529b1"></a>

### [`00594790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594790.md) → [`005b8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8dc0.md) FUN_005b8dc0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058ff20.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005947ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005b8ddc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005947cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005947ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8dec"
      ]
    ],
    [
      "unmatched:005947cc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005b8ddc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8dec"
      ]
    ],
    [
      "005b8dfc",
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

- 旧版 [`005947ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594790.md#insn-005947ac) · [`005947cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594790.md#insn-005947cc)
- 新版 [`005b8ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8dc0.md#insn-005b8ddc)

~~~diff
- 005947ac ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 005947ac bytes 80000054
- 005947cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005947cc ["INT_ADD", "register:40f0:8", ["const:5947cc:8", "const:4:8"]]
- 005947cc ["CALLIND", null, ["register:0:8"]]
- 005947cc bytes 00013fd6
+ 005b8ddc ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 005b8ddc bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b160e88363c00191970bf42a462413f9"></a>

### [`005947e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005947e0.md) → [`005b8e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8e10.md) FUN_005b8e10

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 63.16% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594800",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594808",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059482c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8ec0"
      ]
    ]
  ],
  "added": [
    [
      "005b8e30",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005b8e38",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005b8e5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b8ec0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005947e0.md#insn-00594800) · [`00594808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005947e0.md#insn-00594808) · [`0059482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005947e0.md#insn-0059482c)

~~~diff
- 00594800 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00594800 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00594800 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00594800 bytes a8831ff8
- 00594808 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00594808 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00594808 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00594808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00594808 bytes f64f00a9
- 0059482c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0059482c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 0059482c bytes 200300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9bbcf7e26d715d409923ae489422d5f"></a>

### [`00594be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594be4.md) → [`005b9214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9214.md) FUN_005b9214

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594be8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594be4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594be8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594c00",
      "DATA",
      [
        "storage",
        "00bf3548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9214",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b9218",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b9230",
      "DATA",
      [
        "storage",
        "00c70570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594be4.md#insn-00594be4) · [`00594be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594be4.md#insn-00594be8) · [`00594c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594be4.md#insn-00594c00)

~~~diff
- 00594be4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00594be4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00594be4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00594be4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00594be4 bytes fd7bbea9
- 00594be8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00594be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00594be8 bytes f30b00f9
- 00594c00 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00594c00 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00594c00 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00594c00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00594c00 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-298ebfd33b430e9a5000443c1f80aa3e"></a>

### [`00594c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594c90.md) → [`005b92c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b92c0.md) FUN_005b92c0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00590428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590428.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594c94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b92ec"
      ]
    ]
  ],
  "added": [
    [
      "005b92c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005b92c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005b92dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b92ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594c90.md#insn-00594c90) · [`00594c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594c90.md#insn-00594c94) · [`00594cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594c90.md#insn-00594cac)

~~~diff
- 00594c90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00594c90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00594c90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00594c90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00594c90 bytes fd7bbea9
- 00594c94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00594c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00594c94 bytes f30b00f9
- 00594cac ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00594cac bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a21881d06e3e40b8422aed8643e5b86"></a>

### [`00594d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594d28.md) → [`005b9358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9358.md) FUN_005b9358

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058e620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058e/0058e620.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 31.25% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00594d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b9378"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00594d4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00594d48",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00594d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b9494"
      ]
    ],
    [
      "unmatched:00594d64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b93ac"
      ]
    ]
  ],
  "added": [
    [
      "005b9378",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005b937c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b9494"
      ]
    ],
    [
      "005b9394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005b93ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594d28.md#insn-00594d48) · [`00594d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594d28.md#insn-00594d4c) · [`00594d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594d28.md#insn-00594d64)

~~~diff
- 00594d48 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00594d48 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00594d48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00594d48 bytes a8831ff8
- 00594d4c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00594d4c bytes c0080054
- 00594d64 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00594d64 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d82acb89b897b723ed7261b0b41ecb"></a>

### [`00595428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595428.md) → [`005b9a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md) FUN_005b9a58

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) · 呼出先 2件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md)
- 新版 呼出元 1件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) · 呼出先 2件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059545c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005b9a8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00595444"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00595444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "005b9a74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595428.md#insn-00595444) · [`0059545c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595428.md#insn-0059545c)
- 新版 [`005b9a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9a58.md#insn-005b9a74)

~~~diff
- 00595444 ["INT_ADD", "register:40f0:8", ["const:595444:8", "const:4:8"]]
- 00595444 ["CALL", null, ["ram:469e20:8"]]
- 00595444 bytes 7752fb97
- 0059545c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 0059545c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 0059545c bytes 600600fd
+ 005b9a74 ["INT_ADD", "register:40f0:8", ["const:5b9a74:8", "const:4:8"]]
+ 005b9a74 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b9a74 bytes 914cfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d92f17acce6d0f4c67ae0c5603b0835"></a>

### [`00596660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596660.md) → [`005bac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bac90.md) FUN_005bac90

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ad6364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6364.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b35d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00596664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00596664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00596668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00596664",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00596668",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059667c",
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
      "005bac94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005bac98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005bacac",
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

- 旧版 [`00596664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596660.md#insn-00596664) · [`00596668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596660.md#insn-00596668) · [`0059667c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596660.md#insn-0059667c)

~~~diff
- 00596664 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00596664 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00596664 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00596664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00596664 bytes fd7b02a9
- 00596668 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00596668 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00596668 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00596668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00596668 bytes f44f03a9
- 0059667c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0059667c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0059667c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0059667c bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a4037a3604dd0f9bdfe7d01f17673d"></a>

### [`0059675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/0059675c.md) → [`005bad8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md) FUN_005bad8c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005962e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005962e8.md) · 呼出先 2件 [`00bdb6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6e0.md) [`00bdb6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6f0.md)
- 新版 呼出元 1件 [`005ba918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba918.md) · 呼出先 2件 [`00c58130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58140.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059675c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059675c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00596760"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0059675c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00596760",
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
      "005bad8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005bad90",
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

- 旧版 [`0059675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/0059675c.md#insn-0059675c) · [`00596760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/0059675c.md#insn-00596760)
- 新版 [`005bad8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md#insn-005bad8c)

~~~diff
- 0059675c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0059675c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0059675c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0059675c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0059675c bytes fd7bbea9
- 00596760 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00596760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00596760 bytes f30b00f9
+ 005bad8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005bad8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005bad8c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005bad8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005bad8c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac740943ac8a42c46bf0ac0e72b0b26"></a>

### [`00596784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596784.md) → [`005badb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md) FUN_005badb4

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005967a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005badd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005967a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005967a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:005967a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00596128"
      ]
    ]
  ],
  "added": [
    [
      "005badd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "005badd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ba758"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005967a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596784.md#insn-005967a0) · [`005967a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596784.md#insn-005967a8)
- 新版 [`005badd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005badb4.md#insn-005badd0)

~~~diff
- 005967a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 005967a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005967a0 bytes e80700f9
- 005967a8 ["INT_ADD", "register:40f0:8", ["const:5967a8:8", "const:4:8"]]
- 005967a8 ["CALL", null, ["ram:596128:8"]]
- 005967a8 bytes 60feff97
+ 005badd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 005badd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005badd0 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

