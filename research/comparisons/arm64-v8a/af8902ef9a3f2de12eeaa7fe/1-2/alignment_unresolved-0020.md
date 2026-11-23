# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (20)

[一覧の目次](README.md)

<a id="compare-3c56a90a6b2183f0f2671ac6855bebc3"></a>

### [`00bbb5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb5ac.md) → [`00c37ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md) __dynamic_cast

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 29.73% / 新版 28.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb5dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb6d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb6dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb5dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38130"
      ]
    ],
    [
      "unmatched:00bbb650",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38130"
      ]
    ],
    [
      "00c38098",
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

- 旧版 [`00bbb5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb5ac.md#insn-00bbb5dc) · [`00bbb650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb5ac.md#insn-00bbb650) · [`00bbb6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb5ac.md#insn-00bbb6d8)

~~~diff
- 00bbb5dc ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00bbb5dc bytes 60080054
- 00bbb650 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bbb650 ["INT_ADD", "register:40f0:8", ["const:bbb650:8", "const:4:8"]]
- 00bbb650 ["CALLIND", null, ["register:0:8"]]
- 00bbb650 bytes 20013fd6
- 00bbb6d8 ["COPY", "tmp:0:1", ["register:101:1"]]
- 00bbb6d8 ["COPY", "tmp:1:1", ["const:0:1"]]
- 00bbb6d8 ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 00bbb6d8 ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 00bbb6d8 bytes 2009417a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9103c6659291f0bf175aaaa574bcd931"></a>

### [`00bbb7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb7b8.md) → [`00c38200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38200.md) FUN_00c38200

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3826c"
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
      "unmatched:00bbb7cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3821c"
      ]
    ],
    [
      "unmatched:00bbb7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38240"
      ]
    ],
    [
      "unmatched:00bbb7f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38274"
      ]
    ]
  ],
  "added": [
    [
      "00c38214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3821c"
      ]
    ],
    [
      "00c38230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38240"
      ]
    ],
    [
      "00c3823c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38274"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb7b8.md#insn-00bbb7cc) · [`00bbb7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb7b8.md#insn-00bbb7e8) · [`00bbb7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb7b8.md#insn-00bbb7f4)

~~~diff
- 00bbb7cc ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bbb7cc bytes 40000054
- 00bbb7e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbb7e8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bbb7e8 bytes 81000054
- 00bbb7f4 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bbb7f4 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9def52a144f87107f0cbcfc67e0fae70"></a>

### [`00bbb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb840.md) → [`00c38288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38288.md) FUN_00c38288

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 12.50% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c38300"
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
      "unmatched:00bbb854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c382b0"
      ]
    ],
    [
      "unmatched:00bbb87c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c382d4"
      ]
    ],
    [
      "unmatched:00bbb888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38308"
      ]
    ]
  ],
  "added": [
    [
      "00c3829c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c382b0"
      ]
    ],
    [
      "00c382c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c382d4"
      ]
    ],
    [
      "00c382d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38308"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb840.md#insn-00bbb854) · [`00bbb87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb840.md#insn-00bbb87c) · [`00bbb888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb840.md#insn-00bbb888)

~~~diff
- 00bbb854 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bbb854 bytes a0000054
- 00bbb87c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbb87c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bbb87c bytes 81000054
- 00bbb888 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bbb888 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2653163f32dbdf66c928d85fffd54e30"></a>

### [`00bbd1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd1d8.md) → [`00c39c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39c20.md) FUN_00c39c20

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 6.25% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd1f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd234"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd1f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39c50"
      ]
    ],
    [
      "unmatched:00bbd234",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbd23c"
      ]
    ],
    [
      "unmatched:00bbd238",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ],
  "added": [
    [
      "00c39c3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39c50"
      ]
    ],
    [
      "00c39c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39c84"
      ]
    ],
    [
      "00c39c80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd1d8.md#insn-00bbd1f4) · [`00bbd234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd1d8.md#insn-00bbd234) · [`00bbd238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd1d8.md#insn-00bbd238)

~~~diff
- 00bbd1f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bbd1f4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bbd1f4 bytes a00000b5
- 00bbd234 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00bbd234 bytes 40000054
- 00bbd238 ["INT_ADD", "register:40f0:8", ["const:bbd238:8", "const:4:8"]]
- 00bbd238 ["CALL", null, ["callee:00c58260:8"]]
- 00bbd238 bytes 76790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6755e2b8bbfe84bf8dfe30b2fc0039c3"></a>

### [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) → [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) FUN_00c3a7f0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.89% / 新版 68.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbde04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbde18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3a84c"
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
      "unmatched:00bbddd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a840"
      ]
    ],
    [
      "unmatched:00bbde08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57be0"
      ]
    ],
    [
      "unmatched:00bbde18",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3a81c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a840"
      ]
    ],
    [
      "00c3a850",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57be0"
      ]
    ],
    [
      "00c3a860",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbddd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md#insn-00bbddd4) · [`00bbde04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md#insn-00bbde04) · [`00bbde08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md#insn-00bbde08)

~~~diff
- 00bbddd4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbddd4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbddd4 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bbddd4 bytes 28010054
- 00bbde04 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bbde04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bbde04 bytes c90600f9
- 00bbde08 ["INT_ADD", "register:40f0:8", ["const:bbde08:8", "const:4:8"]]
- 00bbde08 ["CALL", null, ["callee:00c57be0:8"]]
- 00bbde08 bytes e2740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ec97145b643cbc344884cc64682b2f5"></a>

### [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) → [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) FUN_00c3c9b8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 10件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.92% / 新版 60.92%

CFGの説明率　旧版 38.10% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbff74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbff74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbff78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbff74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbff78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbff7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3c9bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c3c9c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c3c9c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbff74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md#insn-00bbff74) · [`00bbff78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md#insn-00bbff78) · [`00bbff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md#insn-00bbff7c)

~~~diff
- 00bbff74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbff74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbff74 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bbff74 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbff74 bytes fd7bbaa9
- 00bbff78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbff78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00bbff78 bytes fb0b00f9
- 00bbff7c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bbff7c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bbff7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbff7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbff7c bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3724dee03513a201cc6c3c6d8fd5df9c"></a>

### [`00bc0ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ac8.md) → [`00c3d510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d510.md) FUN_00c3d510

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0b50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0b2c",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc0b50",
      "DATA",
      [
        "storage",
        "002af7b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d574",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d598",
      "DATA",
      [
        "storage",
        "002c0dd4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ac8.md#insn-00bc0b24) · [`00bc0b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ac8.md#insn-00bc0b2c) · [`00bc0b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ac8.md#insn-00bc0b50)

~~~diff
- 00bc0b24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc0b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc0b24 bytes a90600f9
- 00bc0b2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0b2c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc0b2c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc0b2c bytes 080c01f8
- 00bc0b50 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0b50 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00bc0b50 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 00bc0b50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc0b50 bytes 083001a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac914404360d7ede9a8466efe32029e"></a>

### [`00bc0ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ec0.md) → [`00c3d908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md) FUN_00c3d908

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 81.82% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c3d9bc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ec0.md#insn-00bc0f74) · [`00bc0f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0ec0.md#insn-00bc0f10)
- 新版 [`00c3d9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md#insn-00c3d9bc) · [`00c3d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d908.md#insn-00c3d958)

~~~diff
- 00bc0f74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc0f74 ["RETURN", null, ["register:0:8"]]
- 00bc0f74 bytes c0035fd6
+ 00c3d9bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c3d9bc ["RETURN", null, ["register:0:8"]]
+ 00c3d9bc bytes c0035fd6
- 00bc0f10 ["INT_ADD", "register:40f0:8", ["const:bc0f10:8", "const:4:8"]]
- 00bc0f10 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
+ 00c3d958 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc0f10 bytes d0700094
+ 00c3d958 bytes d2700094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528d55d3df03daea011bc95c9ae52330"></a>

### [`00bc0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0fc0.md) → [`00c3da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md) FUN_00c3da08

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.55% / 新版 92.55%

CFGの説明率　旧版 68.75% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3da7c"
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
      "unmatched:00bc1028",
      "READ",
      [
        "storage",
        "002aa3a0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc102c",
      "READ",
      [
        "storage",
        "002aa3b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3da70",
      "READ",
      [
        "storage",
        "002bb11c",
        null,
        "string"
      ]
    ],
    [
      "00c3da74",
      "READ",
      [
        "storage",
        "002bb12c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0fc0.md#insn-00bc1034) · [`00bc1038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0fc0.md#insn-00bc1038)
- 新版 [`00c3da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md#insn-00c3da7c)

~~~diff
- 00bc1034 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc1034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bc1034 bytes 0001803d
- 00bc1038 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00bc1038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc1038 bytes 090900f9
+ 00c3da7c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c3da7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00c3da7c bytes 0001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac481b0baa565503f9451b88e273883f"></a>

### [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) → [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) FUN_00c3eee8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) · 呼出先 13件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc0cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md) [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md)
- 新版 呼出元 2件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) · 呼出先 13件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 70.20% / 新版 67.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc262c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3efe0"
      ]
    ],
    [
      "unmatched:00bc259c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f0cc"
      ]
    ],
    [
      "unmatched:00bc25bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f244"
      ]
    ]
  ],
  "added": [
    [
      "00c3efcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3efe0"
      ]
    ],
    [
      "00c3efe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f0cc"
      ]
    ],
    [
      "00c3f004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f244"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md#insn-00bc2584) · [`00bc259c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md#insn-00bc259c) · [`00bc25bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md#insn-00bc25bc)

~~~diff
- 00bc2584 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bc2584 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00bc2584 bytes a3000054
- 00bc259c ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
- 00bc259c bytes 40070054
- 00bc25bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00bc25bc ["CBRANCH", null, ["local:b56:8", "tmp:0:1"]]
- 00bc25bc bytes 0a1200b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44eadfc84d8c0124a4254bef64fee338"></a>

### [`00bc2d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d8c.md) → [`00c3f7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md) FUN_00c3f7d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c3f80c"
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
      "unmatched:00bc2dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f830"
      ]
    ]
  ],
  "added": [
    [
      "00c3f80c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3f830"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d8c.md#insn-00bc2dc4) · [`00bc2da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d8c.md#insn-00bc2da8)
- 新版 [`00c3f80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md#insn-00c3f80c) · [`00c3f7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md#insn-00c3f7f0)

~~~diff
- 00bc2dc4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc2dc4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc2dc4 bytes 21010054
+ 00c3f80c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c3f80c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00c3f80c bytes 21010054
- 00bc2da8 ["BRANCH", null, ["local:b6:8"]]
+ 00c3f7f0 ["BRANCH", null, ["local:b7:8"]]
- 00bc2da8 bytes 13000014
+ 00c3f7f0 bytes 13000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a094979cb4e3c5c2a58d39254c62522c"></a>

### [`00bc2eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2eb4.md) → [`00c3f8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8fc.md) FUN_00c3f8fc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

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
      "site": "00bc2ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c3f92c"
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
      "unmatched:00bc2ee4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3f92c",
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

- 旧版 [`00bc2ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2eb4.md#insn-00bc2ee4) · [`00bc2ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2eb4.md#insn-00bc2ec8)
- 新版 [`00c3f92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8fc.md#insn-00c3f92c) · [`00c3f910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8fc.md#insn-00c3f910)

~~~diff
- 00bc2ee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2ee4 ["INT_ADD", "register:40f0:8", ["const:bc2ee4:8", "const:4:8"]]
- 00bc2ee4 ["CALLIND", null, ["register:0:8"]]
- 00bc2ee4 bytes 00013fd6
+ 00c3f92c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3f92c ["INT_ADD", "register:40f0:8", ["const:c3f92c:8", "const:4:8"]]
+ 00c3f92c ["CALLIND", null, ["register:0:8"]]
+ 00c3f92c bytes 00013fd6
- 00bc2ec8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bc2ec8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bc2ec8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bc2ec8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c3f910 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00c3f910 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c3f910 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c3f910 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00bc2ec8 bytes 28010037
+ 00c3f910 bytes 28010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ffb4ad8b4ebde5d0b7845a57af8a16"></a>

### [`00bc4750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4750.md) → [`00c41198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41198.md) FUN_00c41198

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc47bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc47c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c41204"
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
      "unmatched:00bc4788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c411f4"
      ]
    ],
    [
      "unmatched:00bc47c4",
      "DATA",
      [
        "storage",
        "00c181b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c411d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c411f4"
      ]
    ],
    [
      "00c4120c",
      "DATA",
      [
        "storage",
        "00c97b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4750.md#insn-00bc4788) · [`00bc47bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4750.md#insn-00bc47bc) · [`00bc47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4750.md#insn-00bc47c4)

~~~diff
- 00bc4788 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc4788 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc4788 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bc4788 bytes 28010054
- 00bc47bc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:8:8"]]
- 00bc47bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc47bc bytes 090700f9
- 00bc47c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc47c4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc47c4 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc47c4 bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1189e1e149f9de3671f85012f22989a5"></a>

### [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) → [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) FUN_00c42064

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) · 呼出先 5件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) · 呼出先 5件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.75% / 新版 46.75%

CFGの説明率　旧版 20.75% / 新版 18.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc56c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc56c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc566c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42150"
      ]
    ],
    [
      "unmatched:00bc568c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c42064"
      ]
    ],
    [
      "unmatched:00bc5690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c422b0"
      ]
    ]
  ],
  "added": [
    [
      "00c420b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42150"
      ]
    ],
    [
      "00c420f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42114"
      ]
    ],
    [
      "00c420fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md#insn-00bc5678) · [`00bc56c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md#insn-00bc56c0) · [`00bc56c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md#insn-00bc56c8)

~~~diff
- 00bc5678 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bc5678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc5678 bytes 080000f9
- 00bc56c0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bc56c0 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00bc56c0 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00bc56c0 ["COPY", "tmp:3:8", ["register:4000:8"]]
- 00bc56c0 bytes 167c00a9
- 00bc56c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:1330:8"]]
- 00bc56c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc56c8 bytes a09a09f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca82b5987ad1801213d0ae504cf608ba"></a>

### [`00bc5884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5884.md) → [`00c422cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c422cc.md) FUN_00c422cc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 58.54% / 新版 58.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc58e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc58e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc58f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc58ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42318"
      ]
    ],
    [
      "unmatched:00bc58e8",
      "DATA",
      [
        "storage",
        "00c18c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c422f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42318"
      ]
    ],
    [
      "00c42330",
      "DATA",
      [
        "storage",
        "00c985e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc58ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5884.md#insn-00bc58ac) · [`00bc58e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5884.md#insn-00bc58e0) · [`00bc58e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5884.md#insn-00bc58e8)

~~~diff
- 00bc58ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc58ac ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc58ac ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bc58ac bytes 28010054
- 00bc58e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc58e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc58e0 bytes a90600f9
- 00bc58e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc58e8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc58e8 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc58e8 bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-913a551470b8a1cd0998e294d77a5d0c"></a>

### [`00bc5928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5928.md) → [`00c42370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42370.md) FUN_00c42370

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 52.78% / 新版 57.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5a58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc5944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bbde5c"
      ]
    ],
    [
      "unmatched:00bc5988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c424b8"
      ]
    ],
    [
      "unmatched:00bc5a44",
      "DATA",
      [
        "storage",
        "00c18ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4238c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c3a8a4"
      ]
    ],
    [
      "00c423d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c424b8"
      ]
    ],
    [
      "00c4248c",
      "DATA",
      [
        "storage",
        "00c98650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5928.md#insn-00bc5944) · [`00bc5988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5928.md#insn-00bc5988) · [`00bc5a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5928.md#insn-00bc5a44)

~~~diff
- 00bc5944 ["INT_ADD", "register:40f0:8", ["const:bc5944:8", "const:4:8"]]
- 00bc5944 ["CALL", null, ["ram:bbde5c:8"]]
- 00bc5944 bytes 46e1ff97
- 00bc5988 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00bc5988 bytes 40070054
- 00bc5a44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc5a44 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:10:8"]]
- 00bc5a44 ["STORE", null, ["const:1b1:8", "register:4048:8", "tmp:0:8"]]
- 00bc5a44 bytes 280d01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed221c5be7bc3ce2e69e130532b961c0"></a>

### [`00bc6374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6374.md) → [`00c42dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42dbc.md) FUN_00c42dbc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 20.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc63d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c42e18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc639c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc639c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42e08"
      ]
    ],
    [
      "00c42e20",
      "DATA",
      [
        "storage",
        "00c18ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42e08"
      ]
    ],
    [
      "00c42e20",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc639c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6374.md#insn-00bc639c) · [`00bc63d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6374.md#insn-00bc63d0) · [`00bc640c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6374.md#insn-00bc640c)

~~~diff
- 00bc639c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc639c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc639c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bc639c bytes 28010054
- 00bc63d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc63d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc63d0 bytes a90600f9
- 00bc640c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc640c ["RETURN", null, ["register:0:8"]]
- 00bc640c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75f5ad54655b47289c3fac31b0ddfce6"></a>

### [`00bc6414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6414.md) → [`00c42e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42e5c.md) FUN_00c42e5c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 14.29% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6484"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc643c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ea8"
      ]
    ],
    [
      "unmatched:00bc6478",
      "DATA",
      [
        "storage",
        "00c18f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ea8"
      ]
    ],
    [
      "00c42ec0",
      "DATA",
      [
        "storage",
        "00c988f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc643c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6414.md#insn-00bc643c) · [`00bc6470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6414.md#insn-00bc6470) · [`00bc6478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6414.md#insn-00bc6478)

~~~diff
- 00bc643c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc643c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc643c ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00bc643c bytes 28010054
- 00bc6470 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc6470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc6470 bytes a90600f9
- 00bc6478 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc6478 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc6478 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc6478 bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c4689190ccb83a9b78632457f12681"></a>

### [`00bc64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc64b4.md) → [`00c42efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42efc.md) FUN_00c42efc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 51.11% / 新版 51.11%

CFGの説明率　旧版 40.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc651c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc652c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc64dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42f48"
      ]
    ],
    [
      "unmatched:00bc651c",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc6534",
      "DATA",
      [
        "storage",
        "0029d276",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c42f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42f48"
      ]
    ],
    [
      "00c42f64",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42f7c",
      "DATA",
      [
        "storage",
        "002ad500",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc64dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc64b4.md#insn-00bc64dc) · [`00bc6510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc64b4.md#insn-00bc6510) · [`00bc651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc64b4.md#insn-00bc651c)

~~~diff
- 00bc64dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc64dc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc64dc ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00bc64dc bytes 28010054
- 00bc6510 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc6510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc6510 bytes a90600f9
- 00bc651c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc651c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc651c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc651c bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8deda7c72643097ff2163df7ab901f70"></a>

### [`00bc6604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md) → [`00c4304c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c4304c.md) FUN_00c4304c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 55.81% / 新版 55.81%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc660c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6608",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc660c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc6610",
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
      "00c43050",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c43054",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c43058",
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

- 旧版 [`00bc6608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc6608) · [`00bc660c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc660c) · [`00bc6610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6604.md#insn-00bc6610)

~~~diff
- 00bc6608 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc6608 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc6608 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc6608 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc6608 bytes fd7bbda9
- 00bc660c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc660c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc660c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc660c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc660c bytes f65701a9
- 00bc6610 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc6610 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc6610 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc6610 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc6610 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864d01783746255597edbf68a69ca269"></a>

### [`00bc6f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6f3c.md) → [`00c43984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43984.md) FUN_00c43984

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.87% / 新版 66.87%

CFGの説明率　旧版 36.27% / 新版 40.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc700c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43a6c"
      ]
    ],
    [
      "unmatched:00bc7010",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bc7018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc7430"
      ]
    ]
  ],
  "added": [
    [
      "00c43a40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43a6c"
      ]
    ],
    [
      "00c43a58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c43a60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43e78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6f3c.md#insn-00bc6ff0) · [`00bc700c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6f3c.md#insn-00bc700c) · [`00bc7014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6f3c.md#insn-00bc7014)

~~~diff
- 00bc6ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00bc6ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 00bc6ff0 bytes 6b2200b9
- 00bc700c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc700c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc700c bytes 610a00f9
- 00bc7014 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc7014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc7014 bytes 600200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc4c8e6b9f515f2733b20062d920fee"></a>

### [`00bc7450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md) → [`00c43e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43e98.md) FUN_00c43e98

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc74b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc74c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc74cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc74c0",
      "DATA",
      [
        "storage",
        "00c17e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43f08",
      "DATA",
      [
        "storage",
        "00c977e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc74b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc74b8) · [`00bc74c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc74c0) · [`00bc74cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7450.md#insn-00bc74cc)

~~~diff
- 00bc74b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00bc74b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc74b8 bytes e90600f9
- 00bc74c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc74c0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc74c0 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc74c0 bytes 080c01f8
- 00bc74cc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc74cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc74cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc74cc bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44346d8d708c6bfbec99a97f8f1e6992"></a>

### [`00bc7510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7510.md) → [`00c43f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43f58.md) FUN_00c43f58

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.33% / 新版 78.33%

CFGの説明率　旧版 25.00% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc76ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc760c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44080"
      ]
    ],
    [
      "unmatched:00bc7624",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bc762c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44130"
      ]
    ]
  ],
  "added": [
    [
      "00c44054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44080"
      ]
    ],
    [
      "00c4406c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c44074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7510.md#insn-00bc760c) · [`00bc761c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7510.md#insn-00bc761c) · [`00bc7620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7510.md#insn-00bc7620)

~~~diff
- 00bc760c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bc760c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bc760c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00bc760c bytes 69010054
- 00bc761c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc761c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc761c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bc761c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bc761c bytes 2181889a
- 00bc7620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc7620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc7620 bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ece150c38aa0b0e9d823fc4d8ec929"></a>

### [`00bc76f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc76f8.md) → [`00c44140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44140.md) FUN_00c44140

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.67% / 新版 71.67%

CFGの説明率　旧版 32.35% / 新版 37.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc77a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc77b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7834"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc7754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c441b4"
      ]
    ],
    [
      "unmatched:00bc77ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bc77b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44318"
      ]
    ]
  ],
  "added": [
    [
      "00c4419c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c441b4"
      ]
    ],
    [
      "00c441f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c441fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44318"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc76f8.md#insn-00bc7744) · [`00bc7754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc76f8.md#insn-00bc7754) · [`00bc77a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc76f8.md#insn-00bc77a4)

~~~diff
- 00bc7744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7744 ["INT_ADD", "register:40f0:8", ["const:bc7744:8", "const:4:8"]]
- 00bc7744 ["CALLIND", null, ["register:0:8"]]
- 00bc7744 bytes 00013fd6
- 00bc7754 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bc7754 bytes c0000054
- 00bc77a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc77a4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc77a4 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bc77a4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bc77a4 bytes 2181889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3567948ed0495b96ca8d660531c13cb9"></a>

### [`00bc78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc78e0.md) → [`00c44328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44328.md) FUN_00c44328

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.82% / 新版 66.82%

CFGの説明率　旧版 30.91% / 新版 35.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7984"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc798c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c44380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc7a34"
      ]
    ],
    [
      "00c44398",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc7a34"
      ]
    ],
    [
      "unmatched:00bc7970",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c443e4"
      ]
    ]
  ],
  "added": [
    [
      "00c44380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4447c"
      ]
    ],
    [
      "00c44398",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4447c"
      ]
    ],
    [
      "00c443b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c443e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc78e0.md#insn-00bc7968) · [`00bc7970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc78e0.md#insn-00bc7970) · [`00bc7980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc78e0.md#insn-00bc7980)

~~~diff
- 00bc7968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00bc7968 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 00bc7968 bytes 6b2200b9
- 00bc7970 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bc7970 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bc7970 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00bc7970 bytes 69010054
- 00bc7980 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc7980 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc7980 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bc7980 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bc7980 bytes 2181889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc300327b61e4c95554c69c1706ccd26"></a>

### [`00bc86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md) → [`00c45124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md) FUN_00c45124

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 41.10% / 新版 41.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc86e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc86e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc86e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc86e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc86e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc86e8",
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
      "00c45128",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4512c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c45130",
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

- 旧版 [`00bc86e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md#insn-00bc86e0) · [`00bc86e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md#insn-00bc86e4) · [`00bc86e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md#insn-00bc86e8)

~~~diff
- 00bc86e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc86e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc86e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc86e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc86e0 bytes fd7bbda9
- 00bc86e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc86e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc86e4 bytes f50b00f9
- 00bc86e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc86e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc86e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc86e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc86e8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60960b1119c0e503547d458bfdee87e8"></a>

### [`00bc89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc89e8.md) → [`00c45430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45430.md) FUN_00c45430

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 34.68% / 新版 34.68%

CFGの説明率　旧版 1.58% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 22件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc89ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc89ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc89f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc89ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc89f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc89f4",
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
      "00c45434",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c45438",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4543c",
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

- 旧版 [`00bc89ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc89e8.md#insn-00bc89ec) · [`00bc89f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc89e8.md#insn-00bc89f0) · [`00bc89f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc89e8.md#insn-00bc89f4)

~~~diff
- 00bc89ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc89ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc89ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc89ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc89ec bytes fd7bbda9
- 00bc89f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc89f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc89f0 bytes f50b00f9
- 00bc89f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc89f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc89f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc89f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc89f4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e92907581af0d97b9f6552b7c220ff9"></a>

### [`00bc8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8e94.md) → [`00c458dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c458dc.md) FUN_00c458dc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.17% / 新版 73.17%

CFGの説明率　旧版 33.33% / 新版 40.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8ff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc8fa4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c459f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc91b0"
      ]
    ],
    [
      "unmatched:00bc8fdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c45a50"
      ]
    ]
  ],
  "added": [
    [
      "00c459ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c459f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c45bf8"
      ]
    ],
    [
      "00c45a24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c45a50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8e94.md#insn-00bc8f9c) · [`00bc8fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8e94.md#insn-00bc8fa0) · [`00bc8fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8e94.md#insn-00bc8fd8)

~~~diff
- 00bc8f9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc8f9c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc8f9c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bc8f9c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bc8f9c bytes 2181889a
- 00bc8fa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc8fa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc8fa0 bytes 610a00f9
- 00bc8fd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bc8fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc8fd8 bytes 680600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31d7c9ee0cd481727a23fcfa267f14c7"></a>

### [`00bca270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca270.md) → [`00c46cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md) FUN_00c46cb8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c46d30",
      "PARAM",
      [
        "storage",
        "0029e335",
        null,
        null
      ]
    ],
    [
      "00c46d30",
      "PARAM",
      [
        "storage",
        "0028f920",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c46d30",
      "PARAM",
      [
        "storage",
        "002ae6ba",
        null,
        null
      ]
    ],
    [
      "00c46d30",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca270.md#insn-00bca2c0) · [`00bca2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca270.md#insn-00bca2d0) · [`00bca2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca270.md#insn-00bca2d4)
- 新版 [`00c46d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d08) · [`00c46d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d18) · [`00c46d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d1c)

~~~diff
- 00bca2c0 ["INT_ADD", "register:40f0:8", ["const:bca2c0:8", "const:4:8"]]
- 00bca2c0 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c46d08 ["INT_ADD", "register:40f0:8", ["const:c46d08:8", "const:4:8"]]
+ 00c46d08 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bca2c0 bytes e44b0094
+ 00c46d08 bytes e64b0094
- 00bca2d0 ["COPY", "register:4048:8", ["const:29e000:8"]]
+ 00c46d18 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 00bca2d0 bytes a9b6ff90
+ 00c46d18 bytes 49b3ff90
- 00bca2d4 ["COPY", "tmp:0:8", ["const:335:8"]]
- 00bca2d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bca2d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bca2d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c46d1c ["COPY", "tmp:0:8", ["const:6ba:8"]]
+ 00c46d1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46d1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46d1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bca2d4 bytes 29d50c91
+ 00c46d1c bytes 29e91a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ff2dd7f4dab9bece8cf2b4e84898c2"></a>

### [`00bcb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md) → [`00c47d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47d78.md) FUN_00c47d78

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb3ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c47dec"
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
      "unmatched:00bcb3ac",
      "DATA",
      [
        "storage",
        "00c188b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47df4",
      "DATA",
      [
        "storage",
        "00c98260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb3a4) · [`00bcb3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb3ac) · [`00bcb408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md#insn-00bcb408)

~~~diff
- 00bcb3a4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:8:8"]]
- 00bcb3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bcb3a4 bytes 290700f9
- 00bcb3ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcb3ac ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bcb3ac ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bcb3ac bytes 080c01f8
- 00bcb408 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcb408 ["RETURN", null, ["register:0:8"]]
- 00bcb408 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d01b5b427792616b4ad1592fcd6f70"></a>

### [`00bcb9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb9a8.md) → [`00c483f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md) FUN_00c483f0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcba3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c48484"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb9a8.md#insn-00bcba3c) · [`00bcb9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb9a8.md#insn-00bcb9cc)
- 新版 [`00c48484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md#insn-00c48484) · [`00c48414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c483f0.md#insn-00c48414)

~~~diff
- 00bcba3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bcba3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcba3c bytes 680600f9
+ 00c48484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
+ 00c48484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c48484 bytes 680600f9
- 00bcb9cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb9cc ["INT_ADD", "register:40f0:8", ["const:bcb9cc:8", "const:4:8"]]
- 00bcb9cc ["CALLIND", null, ["register:0:8"]]
+ 00c48414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48414 ["INT_ADD", "register:40f0:8", ["const:c48414:8", "const:4:8"]]
+ 00c48414 ["CALLIND", null, ["register:0:8"]]
- 00bcb9cc bytes 00013fd6
+ 00c48414 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac832baf606cdcdf6f15a5b0f2d21af4"></a>

### [`00bcbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md) → [`00c48648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md) FUN_00c48648

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.87% / 新版 60.87%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbc48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbc50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbc70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4867c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcbc5c"
      ]
    ],
    [
      "unmatched:00bcbc4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcbc54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48754"
      ]
    ]
  ],
  "added": [
    [
      "00c4867c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c486a4"
      ]
    ],
    [
      "00c48694",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4869c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48754"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbc44) · [`00bcbc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbc48) · [`00bcbc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md#insn-00bcbc4c)

~~~diff
- 00bcbc44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcbc44 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcbc44 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bcbc44 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcbc44 bytes 2181889a
- 00bcbc48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcbc48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcbc48 bytes 610a00f9
- 00bcbc4c ["INT_ADD", "register:40f0:8", ["const:bcbc4c:8", "const:4:8"]]
- 00bcbc4c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcbc4c bytes 81450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba5b230bc2dd1778382aada96f39889"></a>

### [`00bcc3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md) → [`00c48df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md) FUN_00c48df8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 17.65% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc3b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc3b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc3b8",
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
      "00c48dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c48e00",
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

- 旧版 [`00bcc3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md#insn-00bcc3b4) · [`00bcc3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md#insn-00bcc3b8) · [`00bcc480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md#insn-00bcc480)

~~~diff
- 00bcc3b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc3b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc3b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc3b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc3b4 bytes fd7bbea9
- 00bcc3b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc3b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc3b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc3b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc3b8 bytes f44f01a9
- 00bcc480 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bcc480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:4:8"]]
- 00bcc480 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcc480 bytes 09110039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dfe9b8b6dfa3694591903b5ac5e928d"></a>

### [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) → [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) FUN_00c49a4c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bcc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md) [`00bce544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md) · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 2件 [`00c492c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md) [`00c4af8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md) · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 89.29% / 新版 92.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd00c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd008",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd010",
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
      "00c49a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c49a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c49a58",
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

- 旧版 [`00bcd008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md#insn-00bcd008) · [`00bcd00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md#insn-00bcd00c) · [`00bcd010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md#insn-00bcd010)

~~~diff
- 00bcd008 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcd008 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcd008 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bcd008 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcd008 bytes fd7bbba9
- 00bcd00c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bcd00c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bcd00c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcd00c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd00c bytes fa6701a9
- 00bcd010 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bcd010 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bcd010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcd010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd010 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e157be95fd91d6bae4351b887476a9ec"></a>

### [`00bcd410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd410.md) → [`00c49e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md) FUN_00c49e58

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 81.25% / 新版 83.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4a04c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd410.md#insn-00bcd604) · [`00bcd458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd410.md#insn-00bcd458)
- 新版 [`00c4a04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md#insn-00c4a04c) · [`00c49ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49e58.md#insn-00c49ea0)

~~~diff
- 00bcd604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bcd604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcd604 bytes 680600f9
+ 00c4a04c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
+ 00c4a04c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c4a04c bytes 680600f9
- 00bcd458 ["INT_ADD", "register:40f0:8", ["const:bcd458:8", "const:4:8"]]
- 00bcd458 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c49ea0 ["INT_ADD", "register:40f0:8", ["const:c49ea0:8", "const:4:8"]]
+ 00c49ea0 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcd458 bytes 7e3f0094
+ 00c49ea0 bytes 803f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe791aa240dda8b113e8e44de2deb785"></a>

### [`00bcd67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd67c.md) → [`00c4a0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a0c4.md) FUN_00c4a0c4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.46% / 新版 72.46%

CFGの説明率　旧版 11.11% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd750"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd6e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a15c"
      ]
    ],
    [
      "unmatched:00bcd700",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcd708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a1d0"
      ]
    ]
  ],
  "added": [
    [
      "00c4a130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a15c"
      ]
    ],
    [
      "00c4a148",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4a150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a1d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd67c.md#insn-00bcd6e8) · [`00bcd6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd67c.md#insn-00bcd6f8) · [`00bcd6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd67c.md#insn-00bcd6fc)

~~~diff
- 00bcd6e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcd6e8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcd6e8 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00bcd6e8 bytes 69010054
- 00bcd6f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcd6f8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcd6f8 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bcd6f8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcd6f8 bytes 2181889a
- 00bcd6fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcd6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcd6fc bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d15690991721baa3bafd0e7e70cbed"></a>

### [`00bcd798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd798.md) → [`00c4a1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a1e0.md) FUN_00c4a1e0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 51.61% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd87c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd8c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd878",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcd880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a3dc"
      ]
    ],
    [
      "unmatched:00bcd8cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c4a2c0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4a2c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4a3dc"
      ]
    ],
    [
      "00c4a314",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd798.md#insn-00bcd870) · [`00bcd874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd798.md#insn-00bcd874) · [`00bcd878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd798.md#insn-00bcd878)

~~~diff
- 00bcd870 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcd870 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcd870 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bcd870 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcd870 bytes 2181889a
- 00bcd874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcd874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcd874 bytes 610a00f9
- 00bcd878 ["INT_ADD", "register:40f0:8", ["const:bcd878:8", "const:4:8"]]
- 00bcd878 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcd878 bytes 763e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e92b88742f43f8479cf24b77e68a728a"></a>

### [`00bcdedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdedc.md) → [`00c4a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md) FUN_00c4a924

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 81.13% / 新版 84.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdf48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4a990"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce140"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ab58"
      ]
    ]
  ],
  "added": [
    [
      "00c4ab88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ab58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdedc.md#insn-00bcdf48) · [`00bce140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdedc.md#insn-00bce140)
- 新版 [`00c4a990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md#insn-00c4a990)

~~~diff
- 00bcdf48 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bcdf48 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bcdf48 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bcdf48 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00bcdf48 bytes 0a6929f8
- 00bce140 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 00bce140 bytes 80feff54
+ 00c4a990 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00c4a990 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00c4a990 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00c4a990 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00c4a990 bytes 0a6929f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d0965f77a8f39c388f4211506eb09e"></a>

### [`00bce6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce6d8.md) → [`00c4b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md) FUN_00c4b120

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 75.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce788"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c4b1d0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bce788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce6d8.md#insn-00bce788) · [`00bce71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce6d8.md#insn-00bce71c)
- 新版 [`00c4b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md#insn-00c4b1d0) · [`00c4b164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b120.md#insn-00c4b164)

~~~diff
- 00bce788 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bce788 ["RETURN", null, ["register:0:8"]]
- 00bce788 bytes c0035fd6
+ 00c4b1d0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c4b1d0 ["RETURN", null, ["register:0:8"]]
+ 00c4b1d0 bytes c0035fd6
- 00bce71c ["INT_ADD", "register:40f0:8", ["const:bce71c:8", "const:4:8"]]
- 00bce71c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4b164 ["INT_ADD", "register:40f0:8", ["const:c4b164:8", "const:4:8"]]
+ 00c4b164 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bce71c bytes cd3a0094
+ 00c4b164 bytes cf3a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3ba7106efa58b0f1433a948ead2cd27"></a>

### [`00bcf1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf1ec.md) → [`00c4bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md) FUN_00c4bc34

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 20.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf260"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4bca8"
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
      "unmatched:00bcf250",
      "READ",
      [
        "storage",
        "002ab3aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4bc98",
      "READ",
      [
        "storage",
        "002bc2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf1ec.md#insn-00bcf260) · [`00bcf264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf1ec.md#insn-00bcf264)
- 新版 [`00c4bca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md#insn-00c4bca8)

~~~diff
- 00bcf260 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcf260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bcf260 bytes 0a0100f9
- 00bcf264 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bcf264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:7:8"]]
- 00bcf264 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00bcf264 bytes 097100b8
+ 00c4bca8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c4bca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00c4bca8 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ccc9ed071961c2f717d7754929fcfde"></a>

### [`00bcf2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf2d4.md) → [`00c4bd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bd1c.md) FUN_00c4bd1c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.00% / 新版 82.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf310"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf364"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4bd58"
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
      "unmatched:00bcf364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4bdc0"
      ]
    ],
    [
      "unmatched:00bcf354",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4bdac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4bdc0"
      ]
    ],
    [
      "00c4bd9c",
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

- 旧版 [`00bcf310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf2d4.md#insn-00bcf310) · [`00bcf354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf2d4.md#insn-00bcf354) · [`00bcf364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf2d4.md#insn-00bcf364)

~~~diff
- 00bcf310 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcf310 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcf310 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00bcf310 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcf310 bytes 4181899a
- 00bcf354 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf354 ["INT_ADD", "register:40f0:8", ["const:bcf354:8", "const:4:8"]]
- 00bcf354 ["CALLIND", null, ["register:0:8"]]
- 00bcf354 bytes 00013fd6
- 00bcf364 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcf364 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bcf364 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754ca1bd867e2d664afb1a2aaf6b7256"></a>

### [`00bcf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md) → [`00c4be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4be00.md) FUN_00c4be00

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) · 呼出先 3件 [`00bcf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9d0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) · 呼出先 3件 [`00c4c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c418.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 36.00% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcf3cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf408",
      "DATA",
      [
        "storage",
        "00c193a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4be14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c4be50",
      "DATA",
      [
        "storage",
        "00c98d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md#insn-00bcf3cc) · [`00bcf408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md#insn-00bcf408) · [`00bcf410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md#insn-00bcf410)

~~~diff
- 00bcf3cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcf3cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcf3cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcf3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcf3cc bytes f44f04a9
- 00bcf408 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00bcf408 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bcf408 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bcf408 bytes 170c01f8
- 00bcf410 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00bcf410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00bcf410 bytes 160c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f11e32068fb23c3cf4f21e42c3a9b301"></a>

### [`00bcff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcff7c.md) → [`00c4c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md) FUN_00c4c9c4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.43% / 新版 61.43%

CFGの説明率　旧版 21.05% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd003c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0014",
      "READ",
      [
        "storage",
        "0029577f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cab4"
      ]
    ],
    [
      "unmatched:00bd0058",
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
      "00c4ca5c",
      "READ",
      [
        "storage",
        "002a51b8",
        null,
        "string"
      ]
    ],
    [
      "00c4ca9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cab4"
      ]
    ],
    [
      "00c4caa0",
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

- 旧版 [`00bcffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcff7c.md#insn-00bcffa8) · [`00bd0020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcff7c.md#insn-00bd0020) · [`00bd0024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcff7c.md#insn-00bd0024)

~~~diff
- 00bcffa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcffa8 ["INT_ADD", "register:40f0:8", ["const:bcffa8:8", "const:4:8"]]
- 00bcffa8 ["CALLIND", null, ["register:0:8"]]
- 00bcffa8 bytes 00013fd6
- 00bd0020 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd0020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bd0020 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd0020 bytes 0a210039
- 00bd0024 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd0024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd0024 bytes 090100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ef89cd15d4a899a280995ee2e042a5f"></a>

### [`00bd00b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd00b0.md) → [`00c4caf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md) FUN_00c4caf8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd015c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4cba4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0164",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4cbac",
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

- 旧版 [`00bd015c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd00b0.md#insn-00bd015c) · [`00bd0164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd00b0.md#insn-00bd0164)
- 新版 [`00c4cba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4caf8.md#insn-00c4cba4)

~~~diff
- 00bd015c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bd015c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd015c bytes 680600f9
- 00bd0164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0164 ["INT_ADD", "register:40f0:8", ["const:bd0164:8", "const:4:8"]]
- 00bd0164 ["CALLIND", null, ["register:0:8"]]
- 00bd0164 bytes 00013fd6
+ 00c4cba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
+ 00c4cba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c4cba4 bytes 680600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b451ab69a33c73990473d61c480ecc1"></a>

### [`00bd01d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd01d0.md) → [`00c4cc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cc18.md) FUN_00c4cc18

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd01f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0214"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0230"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd01f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cca8"
      ]
    ],
    [
      "unmatched:00bd0214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cca8"
      ]
    ],
    [
      "unmatched:00bd0230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cc60"
      ]
    ]
  ],
  "added": [
    [
      "00c4cc38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cca8"
      ]
    ],
    [
      "00c4cc5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cca8"
      ]
    ],
    [
      "00c4cc78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cc60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd01d0.md#insn-00bd01f0) · [`00bd0214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd01d0.md#insn-00bd0214) · [`00bd0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd01d0.md#insn-00bd0230)

~~~diff
- 00bd01f0 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00bd01f0 bytes 80030054
- 00bd0214 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00bd0214 bytes 60020054
- 00bd0230 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd0230 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bd0230 bytes 41ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6bd4e1a07aedad731742758044223da"></a>

### [`00bd032c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md) → [`00c4cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md) FUN_00c4cd74

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd038c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4cdd4"
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
      "unmatched:00bd0394",
      "DATA",
      [
        "storage",
        "00c19648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4cddc",
      "DATA",
      [
        "storage",
        "00c98ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd038c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md#insn-00bd038c) · [`00bd0394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd032c.md#insn-00bd0394)
- 新版 [`00c4cdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md#insn-00c4cdd4)

~~~diff
- 00bd038c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bd038c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd038c bytes c90600f9
- 00bd0394 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd0394 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd0394 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd0394 bytes 080c01f8
+ 00c4cdd4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
+ 00c4cdd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c4cdd4 bytes c90600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a626ded9c7d247ecfc9a82ec62a96746"></a>

### [`00bd03d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd03d4.md) → [`00c4ce1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ce1c.md) FUN_00c4ce1c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd044c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4ce94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cef8"
      ]
    ],
    [
      "unmatched:00bd049c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0424",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4cee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cef8"
      ]
    ],
    [
      "00c4cee4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c4ce6c",
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

- 旧版 [`00bd0424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd03d4.md#insn-00bd0424) · [`00bd0448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd03d4.md#insn-00bd0448) · [`00bd044c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd03d4.md#insn-00bd044c)

~~~diff
- 00bd0424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0424 ["INT_ADD", "register:40f0:8", ["const:bd0424:8", "const:4:8"]]
- 00bd0424 ["CALLIND", null, ["register:0:8"]]
- 00bd0424 bytes 00013fd6
- 00bd0448 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd0448 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd0448 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd0448 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd0448 bytes 2181889a
- 00bd044c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd044c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd044c bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aea40134e0c1e6b24b2485200df35e90"></a>

### [`00bd04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd04e0.md) → [`00c4cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md) FUN_00c4cf28

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd04fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4cf44"
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
      "unmatched:00bd04fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cf80"
      ]
    ]
  ],
  "added": [
    [
      "00c4cf44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4cf80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd04fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd04e0.md#insn-00bd04fc) · [`00bd04ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd04e0.md#insn-00bd04ec)
- 新版 [`00c4cf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md#insn-00c4cf44) · [`00c4cf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf28.md#insn-00c4cf34)

~~~diff
- 00bd04fc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd04fc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd04fc ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00bd04fc bytes e9010054
+ 00c4cf44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4cf44 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4cf44 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00c4cf44 bytes e9010054
- 00bd04ec ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00c4cf34 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd04ec bytes c0010054
+ 00c4cf34 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5652be082973b885ba8677cb2410de6"></a>

### [`00bd054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd054c.md) → [`00c4cf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf94.md) FUN_00c4cf94

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd054c.md#insn-00bd0558) · [`00bd0568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd054c.md#insn-00bd0568) · [`00bd0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd054c.md#insn-00bd0580)
- 新版 [`00c4cfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf94.md#insn-00c4cfa0) · [`00c4cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf94.md#insn-00c4cfb0) · [`00c4cfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cf94.md#insn-00c4cfc8)

~~~diff
- 00bd0558 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00c4cfa0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd0558 bytes c0010054
+ 00c4cfa0 bytes c0010054
- 00bd0568 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd0568 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd0568 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 00c4cfb0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4cfb0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4cfb0 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bd0568 bytes e9010054
+ 00c4cfb0 bytes e9010054
- 00bd0580 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd0580 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00c4cfc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c4cfc8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd0580 bytes 61010054
+ 00c4cfc8 bytes 61010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ef1423cadec8b74da4b74047a6b734"></a>

### [`00bd05b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd05b8.md) → [`00c4d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d000.md) FUN_00c4d000

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 18.18% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd05d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4d01c"
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
      "unmatched:00bd05d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d058"
      ]
    ]
  ],
  "added": [
    [
      "00c4d01c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd05d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd05b8.md#insn-00bd05d4) · [`00bd05c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd05b8.md#insn-00bd05c4)
- 新版 [`00c4d01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d000.md#insn-00c4d01c) · [`00c4d00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d000.md#insn-00c4d00c)

~~~diff
- 00bd05d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd05d4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd05d4 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00bd05d4 bytes e9010054
+ 00c4d01c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4d01c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4d01c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00c4d01c bytes e9010054
- 00bd05c4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00c4d00c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd05c4 bytes c0010054
+ 00c4d00c bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e973b4b2caef7025518bac26a60cfd45"></a>

### [`00bd0624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0624.md) → [`00c4d06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d06c.md) FUN_00c4d06c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 5.26% / 新版 5.26%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4d0a8"
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
      "unmatched:00bd0630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0658"
      ]
    ],
    [
      "unmatched:00bd0640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d0b4"
      ]
    ],
    [
      "unmatched:00bd0668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0644"
      ]
    ]
  ],
  "added": [
    [
      "00c4d078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d0a0"
      ]
    ],
    [
      "00c4d088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d0b4"
      ]
    ],
    [
      "00c4d0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d08c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0624.md#insn-00bd0630) · [`00bd0640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0624.md#insn-00bd0640) · [`00bd0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0624.md#insn-00bd0660)

~~~diff
- 00bd0630 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00bd0630 bytes 40010054
- 00bd0640 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd0640 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd0640 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00bd0640 bytes 69010054
- 00bd0660 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd0660 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd0660 ["COPY", "tmp:2:4", ["register:4048:4"]]
- 00bd0660 ["INT_ADD", "tmp:3:8", ["register:4008:8", "const:18:8"]]
- 00bd0660 bytes 3f240329
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9803119a09fafa1cc12501070fa798cd"></a>

### [`00bd0670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0670.md) → [`00c4d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d0b8.md) FUN_00c4d0b8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0670.md#insn-00bd067c) · [`00bd068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0670.md#insn-00bd068c) · [`00bd0698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0670.md#insn-00bd0698)
- 新版 [`00c4d0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d0b8.md#insn-00c4d0c4) · [`00c4d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d0b8.md#insn-00c4d0d4)

~~~diff
- 00bd067c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00c4d0c4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bd067c bytes 40010054
+ 00c4d0c4 bytes 40010054
- 00bd068c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd068c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd068c ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00c4d0d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4d0d4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4d0d4 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bd068c bytes 69010054
+ 00c4d0d4 bytes 69010054
- 00bd0698 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bd0698 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd0698 bytes 080040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a4a362409f059cd0a97b507fe725c4"></a>

### [`00bd06bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd06bc.md) → [`00c4d104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d104.md) FUN_00c4d104

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 37.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0700"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4d148"
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
      "unmatched:00bd0700",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d124"
      ]
    ]
  ],
  "added": [
    [
      "00c4d148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d124"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd06bc.md#insn-00bd0700) · [`00bd06d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd06bc.md#insn-00bd06d8)
- 新版 [`00c4d148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d104.md#insn-00c4d148) · [`00c4d120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d104.md#insn-00c4d120)

~~~diff
- 00bd0700 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd0700 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd0700 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
- 00bd0700 bytes e8feff54
+ 00c4d148 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c4d148 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c4d148 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 00c4d148 bytes e8feff54
- 00bd06d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd06d8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd06d8 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00c4d120 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4d120 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4d120 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bd06d8 bytes 69010054
+ 00c4d120 bytes 69010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51e65398fd04d047e423975a2d166f1d"></a>

### [`00bd0710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0710.md) → [`00c4d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d158.md) FUN_00c4d158

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd07b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4d1a0"
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
      "unmatched:00bd075c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd07b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c4d1a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4d1fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0710.md#insn-00bd0754) · [`00bd0758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0710.md#insn-00bd0758) · [`00bd075c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0710.md#insn-00bd075c)

~~~diff
- 00bd0754 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd0754 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd0754 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd0754 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd0754 bytes 2181889a
- 00bd0758 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd0758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd0758 bytes 610a00f9
- 00bd075c ["INT_ADD", "register:40f0:8", ["const:bd075c:8", "const:4:8"]]
- 00bd075c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd075c bytes bd320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b0471ce67558a58337d7066f647b51"></a>

### [`00bd0808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0808.md) → [`00c4d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md) FUN_00c4d250

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0808.md#insn-00bd0834) · [`00bd0858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0808.md#insn-00bd0858) · [`00bd0870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0808.md#insn-00bd0870)
- 新版 [`00c4d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d27c) · [`00c4d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d2a0) · [`00c4d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d250.md#insn-00c4d2b8)

~~~diff
- 00bd0834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0834 ["INT_ADD", "register:40f0:8", ["const:bd0834:8", "const:4:8"]]
- 00bd0834 ["CALLIND", null, ["register:0:8"]]
+ 00c4d27c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d27c ["INT_ADD", "register:40f0:8", ["const:c4d27c:8", "const:4:8"]]
+ 00c4d27c ["CALLIND", null, ["register:0:8"]]
- 00bd0834 bytes 00013fd6
+ 00c4d27c bytes 00013fd6
- 00bd0858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0858 ["INT_ADD", "register:40f0:8", ["const:bd0858:8", "const:4:8"]]
- 00bd0858 ["CALLIND", null, ["register:0:8"]]
+ 00c4d2a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d2a0 ["INT_ADD", "register:40f0:8", ["const:c4d2a0:8", "const:4:8"]]
+ 00c4d2a0 ["CALLIND", null, ["register:0:8"]]
- 00bd0858 bytes 00013fd6
+ 00c4d2a0 bytes 00013fd6
- 00bd0870 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0870 ["INT_ADD", "register:40f0:8", ["const:bd0870:8", "const:4:8"]]
- 00bd0870 ["CALLIND", null, ["register:0:8"]]
+ 00c4d2b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d2b8 ["INT_ADD", "register:40f0:8", ["const:c4d2b8:8", "const:4:8"]]
+ 00c4d2b8 ["CALLIND", null, ["register:0:8"]]
- 00bd0870 bytes 00013fd6
+ 00c4d2b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07610e540099060198bf07b68539aadf"></a>

### [`00bd22b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md) → [`00c4ecfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ecfc.md) FUN_00c4ecfc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.24% / 新版 70.24%

CFGの説明率　旧版 32.00% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd23c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd23c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd23d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4ed4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2338"
      ]
    ],
    [
      "unmatched:00bd2334",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ed9c"
      ]
    ],
    [
      "unmatched:00bd2344",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ed9c"
      ]
    ]
  ],
  "added": [
    [
      "00c4ed4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ed80"
      ]
    ],
    [
      "00c4ed7c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ed9c"
      ]
    ],
    [
      "00c4ed8c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ed9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd23c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd23c0) · [`00bd23c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd23c8) · [`00bd23d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md#insn-00bd23d4)

~~~diff
- 00bd23c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bd23c0 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:10:8"]]
- 00bd23c0 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:0:8"]]
- 00bd23c0 bytes 090d01f8
- 00bd23c8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd23c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bd23c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd23c8 bytes 0a210039
- 00bd23d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 00bd23d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd23d4 bytes 001100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-426eb77f81a97829d04d51e1195da7ed"></a>

### [`00bd2aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md) → [`00c4f4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md) FUN_00c4f4f4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4f53c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2af0"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md#insn-00bd2af0) · [`00bd2af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2aac.md#insn-00bd2af4)
- 新版 [`00c4f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md#insn-00c4f538)

~~~diff
- 00bd2af0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd2af0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd2af0 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd2af0 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd2af0 bytes 2181889a
- 00bd2af4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd2af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd2af4 bytes 610a00f9
+ 00c4f538 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c4f538 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c4f538 ["COPY", "tmp:2:8", ["register:4048:8"]]
+ 00c4f538 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 00c4f538 bytes 2181889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8407b979b782ab790248f6c4c815c50"></a>

### [`00bd3040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md) → [`00c4fa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md) FUN_00c4fa88

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd31a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c4fbec"
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
      "00c4fb0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd31a4"
      ]
    ],
    [
      "unmatched:00bd31a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad40"
      ]
    ]
  ],
  "added": [
    [
      "00c4fb0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4fbec"
      ]
    ],
    [
      "00c4fbec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd31a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md#insn-00bd31a4) · [`00bd306c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md#insn-00bd306c)
- 新版 [`00c4fbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md#insn-00c4fbec) · [`00c4fab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fa88.md#insn-00c4fab4)

~~~diff
- 00bd31a4 ["INT_ADD", "register:40f0:8", ["const:bd31a4:8", "const:4:8"]]
- 00bd31a4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bd31a4 bytes 472c0094
+ 00c4fbec ["INT_ADD", "register:40f0:8", ["const:c4fbec:8", "const:4:8"]]
+ 00c4fbec ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c4fbec bytes 552c0094
- 00bd306c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd306c ["INT_ADD", "register:40f0:8", ["const:bd306c:8", "const:4:8"]]
- 00bd306c ["CALLIND", null, ["register:0:8"]]
+ 00c4fab4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4fab4 ["INT_ADD", "register:40f0:8", ["const:c4fab4:8", "const:4:8"]]
+ 00c4fab4 ["CALLIND", null, ["register:0:8"]]
- 00bd306c bytes 00013fd6
+ 00c4fab4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e18649eafb374b607318f06a1c0425b9"></a>

### [`00bd362c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md) → [`00c50074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50074.md) FUN_00c50074

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.83% / 新版 72.83%

CFGの説明率　旧版 26.53% / 新版 30.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3634"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3630",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3634",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c500c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd3908"
      ]
    ]
  ],
  "added": [
    [
      "00c50078",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c5007c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c500c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c50350"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd3630) · [`00bd3634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd3634) · [`00bd369c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd362c.md#insn-00bd369c)

~~~diff
- 00bd3630 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd3630 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd3630 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd3630 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd3630 bytes fd7bbea9
- 00bd3634 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd3634 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd3634 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd3634 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3634 bytes f44f01a9
- 00bd369c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd369c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bd369c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd369c bytes 0a210039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c2ff7329541ea580813f3adf3ee8a9"></a>

### [`00bd40ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md) → [`00c50b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50b34.md) FUN_00c50b34

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.96% / 新版 91.96%

CFGの説明率　旧版 80.00% / 新版 84.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c50bdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4190"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4198",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd4110",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c50be0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c50b58",
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

- 旧版 [`00bd4110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4110) · [`00bd4190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4190) · [`00bd4194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd40ec.md#insn-00bd4194)

~~~diff
- 00bd4110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4110 ["INT_ADD", "register:40f0:8", ["const:bd4110:8", "const:4:8"]]
- 00bd4110 ["CALLIND", null, ["register:0:8"]]
- 00bd4110 bytes 00013fd6
- 00bd4190 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd4190 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd4190 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd4190 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd4190 bytes 2181889a
- 00bd4194 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd4194 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd4194 bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113943c1b56e855f60f10402f44ffb00"></a>

### [`00bd4840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md) → [`00c51288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md) FUN_00c51288

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 75.86% / 新版 81.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4934"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c5137c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md#insn-00bd4934) · [`00bd485c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4840.md#insn-00bd485c)
- 新版 [`00c5137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51288.md#insn-00c5137c)

~~~diff
- 00bd4934 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd4934 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd4934 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd4934 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd4934 bytes 2181889a
+ 00c5137c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c5137c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c5137c ["COPY", "tmp:2:8", ["register:4048:8"]]
+ 00c5137c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 00c5137c bytes 2181889a
- 00bd485c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00bd485c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd485c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd485c bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af539cf404f1bdbe94159fb0a801017"></a>

### [`00bd50f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md) → [`00c51b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b3c.md) __cxa_free_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0d0.md) · 呼出先 1件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md)
- 新版 呼出元 1件 [`00c57b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b20.md) · 呼出先 1件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd50f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd50f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c51b40"
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
      "unmatched:00bd50f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bd59a8"
      ]
    ],
    [
      "unmatched:00bd5108",
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
      "00c51b40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c51b4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ],
    [
      "00c51b50",
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

- 旧版 [`00bd50f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md#insn-00bd50f8) · [`00bd5104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md#insn-00bd5104) · [`00bd5110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd50f4.md#insn-00bd5110)

~~~diff
- 00bd50f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd50f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd50f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bd50f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd50f8 bytes fd7bbfa9
- 00bd5104 ["INT_ADD", "register:40f0:8", ["const:bd5104:8", "const:4:8"]]
- 00bd5104 ["CALL", null, ["ram:bd59a8:8"]]
- 00bd5104 bytes 29020094
- 00bd5110 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5110 ["RETURN", null, ["register:0:8"]]
- 00bd5110 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2eb96de41c10ff3c2683f3a03eb93f4"></a>

### [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) → [`00c51bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md) FUN_00c51bd0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd5118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5118.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c51b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b60.md) · 呼出先 4件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c51c14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd51d0"
      ]
    ],
    [
      "unmatched:00bd51cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bd59a8"
      ]
    ],
    [
      "unmatched:00bd51d0",
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
      "00c51bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51c18"
      ]
    ],
    [
      "00c51c14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ],
    [
      "00c51c18",
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

- 旧版 [`00bd51cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md#insn-00bd51cc) · [`00bd51dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md#insn-00bd51dc)
- 新版 [`00c51c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md#insn-00c51c14)

~~~diff
- 00bd51cc ["INT_ADD", "register:40f0:8", ["const:bd51cc:8", "const:4:8"]]
- 00bd51cc ["CALL", null, ["ram:bd59a8:8"]]
- 00bd51cc bytes f7010094
- 00bd51dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd51dc ["RETURN", null, ["register:0:8"]]
- 00bd51dc bytes c0035fd6
+ 00c51c14 ["INT_ADD", "register:40f0:8", ["const:c51c14:8", "const:4:8"]]
+ 00c51c14 ["CALL", null, ["ram:c523f0:8"]]
+ 00c51c14 bytes f7010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef353018ecd1830f0610818b9d6bb9e"></a>

### [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) → [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) FUN_00c51cd8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) · 呼出先 2件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md)
- 新版 呼出元 1件 [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) · 呼出先 2件 [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c57c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c10.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5294",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5298",
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
      "00c51cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c51ce0",
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

- 旧版 [`00bd5294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md#insn-00bd5294) · [`00bd5298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md#insn-00bd5298)
- 新版 [`00c51cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md#insn-00c51cdc)

~~~diff
- 00bd5294 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5294 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5294 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5294 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5294 bytes fd7bbea9
- 00bd5298 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd5298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bd5298 bytes f30b00f9
+ 00c51cdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c51cdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c51cdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c51cdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c51cdc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a7f26e2ebca230e0eef91a8a31e2793"></a>

### [`00bd5408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5408.md) → [`00c51e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51e50.md) __cxa_current_exception_type

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 27.27% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd540c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd540c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c51e54"
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
      "unmatched:00bd540c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd543c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51e90"
      ]
    ]
  ],
  "added": [
    [
      "00c51e54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c51e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd540c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5408.md#insn-00bd540c) · [`00bd543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5408.md#insn-00bd543c)
- 新版 [`00c51e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51e50.md#insn-00c51e54)

~~~diff
- 00bd540c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd540c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd540c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bd540c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd540c bytes fd7bbfa9
- 00bd543c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd543c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bd543c bytes 61000054
+ 00c51e54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c51e54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c51e54 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c51e54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c51e54 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e75efd2c6def327d36b8f7ef0a64e2b"></a>

### [`00bd553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md) → [`00c51f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51f84.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f20.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c5db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db20.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md#insn-00bd5540) · [`00bd554c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md#insn-00bd554c) · [`00bd5558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd553c.md#insn-00bd5558)
- 新版 [`00c51f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51f84.md#insn-00c51f88) · [`00c51fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51f84.md#insn-00c51fa0)

~~~diff
- 00bd5540 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bd5540 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c51f88 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c51f88 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5540 bytes 200100b4
+ 00c51f88 bytes 200100b4
- 00bd554c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00bd554c bytes fd030091
- 00bd5558 ["INT_ADD", "register:40f0:8", ["const:bd5558:8", "const:4:8"]]
- 00bd5558 ["CALL", null, ["callee:00c538e0:8"]]
+ 00c51fa0 ["INT_ADD", "register:40f0:8", ["const:c51fa0:8", "const:4:8"]]
+ 00c51fa0 ["CALL", null, ["callee:00c538e0:8"]]
- 00bd5558 bytes 4e060094
+ 00c51fa0 bytes 50060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ead6bde88244d41f86c57faff6139fc"></a>

### [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) → [`00c52cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md) FUN_00c52cd8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) · 呼出先 1件 [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 3件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) [`00c52e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52e80.md) · 呼出先 1件 [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 80.82% / 新版 85.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd62b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6324"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c52cfc"
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
      "unmatched:00bd62b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52d2c"
      ]
    ],
    [
      "unmatched:00bd6324",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52dfc"
      ]
    ],
    [
      "00c52dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6360"
      ]
    ]
  ],
  "added": [
    [
      "00c52cfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52d2c"
      ]
    ],
    [
      "00c52d6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52dfc"
      ]
    ],
    [
      "00c52dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52da8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd62b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md#insn-00bd62b4) · [`00bd6324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md#insn-00bd6324)
- 新版 [`00c52cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md#insn-00c52cfc)

~~~diff
- 00bd62b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd62b4 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00bd62b4 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00bd62b4 bytes 8d010054
- 00bd6324 ["CBRANCH", null, ["local:b30:8", "register:101:1"]]
- 00bd6324 bytes 80040054
+ 00c52cfc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00c52cfc ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00c52cfc ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
+ 00c52cfc bytes 8d010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6778cf96e2f21039a5376a2be70196b6"></a>

### [`00bd65f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd65f8.md) → [`00c53040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53040.md) FUN_00c53040

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c530d0"
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
      "00c5307c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6678"
      ]
    ],
    [
      "unmatched:00bd6688",
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
      "00c5307c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c530c0"
      ]
    ],
    [
      "00c530d0",
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

- 旧版 [`00bd666c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd65f8.md#insn-00bd666c) · [`00bd6670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd65f8.md#insn-00bd6670) · [`00bd6674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd65f8.md#insn-00bd6674)

~~~diff
- 00bd666c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bd666c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00bd666c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd666c ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00bd666c bytes e9038c9a
- 00bd6670 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd6670 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd6670 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd6670 ["COPY", "tmp:1:4", ["register:4058:4"]]
- 00bd6670 bytes eb038b1a
- 00bd6674 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bd6674 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00bd6674 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd6674 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bd6674 bytes ea038a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02cf0029fc991c59ef22622862139fc6"></a>

### [`00bd68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md) → [`00c53340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53340.md) FUN_00c53340

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd68bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md) · 呼出先 2件 [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c53304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md) · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 81.82% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6924",
      "READ",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00c5336c",
      "READ",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd690c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md#insn-00bd690c) · [`00bd6914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md#insn-00bd6914) · [`00bd6924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md#insn-00bd6924)
- 新版 [`00c53354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53340.md#insn-00c53354) · [`00c5335c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53340.md#insn-00c5335c)

~~~diff
- 00bd690c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd690c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c53354 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00c53354 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd690c bytes 480100b4
+ 00c53354 bytes 480100b4
- 00bd6914 ["COPY", "register:4048:8", ["const:10a3000:8"]]
+ 00c5335c ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00bd6914 bytes 692600b0
+ 00c5335c bytes a92600b0
- 00bd6924 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:994:8"]]
- 00bd6924 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00bd6924 ["INT_ZEXT", "register:4000:8", ["tmp:1:4"]]
- 00bd6924 bytes 209549b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-658a04addb45e8febc4a3c0d2f5bcbda"></a>

### [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) → [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) FUN_00c53d80

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) · 呼出先 2件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 3件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) · 呼出先 2件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd735c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd735c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd735c",
      "DATA",
      [
        "storage",
        "00c1a218",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bd735c",
      "DATA",
      [
        "storage",
        "010a39e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c53dac",
      "DATA",
      [
        "storage",
        "00c99bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c53dac",
      "DATA",
      [
        "storage",
        "011288f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md#insn-00bd735c) · [`00bd7378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md#insn-00bd7378) · [`00bd737c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md#insn-00bd737c)

~~~diff
- 00bd735c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd735c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bd735c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bd735c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd735c bytes 082481a8
- 00bd7378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:140:8"]]
- 00bd7378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00bd7378 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00bd7378 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00bd7378 bytes 61020aad
- 00bd737c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
- 00bd737c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5060:16"]]
- 00bd737c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00bd737c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00bd737c bytes 630a09ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45b5f6214427aab30a25ecc0a1c0b7df"></a>

### [`00bd92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md) → [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) FUN_00c55cf0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) · 呼出先 5件 [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) · 呼出先 5件 [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.06% / 新版 81.06%

CFGの説明率　旧版 53.66% / 新版 62.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd92c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9374"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c55d14"
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
      "unmatched:00bd92c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55d98"
      ]
    ],
    [
      "00c55d24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9448"
      ]
    ],
    [
      "00c55d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9448"
      ]
    ]
  ],
  "added": [
    [
      "00c55d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55d98"
      ]
    ],
    [
      "00c55d24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55e98"
      ]
    ],
    [
      "00c55d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55e98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd92c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md#insn-00bd92c4) · [`00bd92ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md#insn-00bd92ec) · [`00bd9374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md#insn-00bd9374)

~~~diff
- 00bd92c4 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bd92c4 bytes 20040054
- 00bd92ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd92ec ["RETURN", null, ["register:0:8"]]
- 00bd92ec bytes c0035fd6
- 00bd9374 ["CBRANCH", null, ["local:b30:8", "register:101:1"]]
- 00bd9374 bytes 20050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b389a0617c3c498b13a796554c486f"></a>

### [`00bda69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md) → [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) FUN_00c570ec

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) · 呼出先 1件 [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md)
- 新版 呼出元 1件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) · 呼出先 1件 [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c57214"
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
      "unmatched:00bda7c8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c57130"
      ]
    ]
  ],
  "added": [
    [
      "00c57218",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c57130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md#insn-00bda7c4) · [`00bda7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md#insn-00bda7ac)
- 新版 [`00c57214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md#insn-00c57214) · [`00c571fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md#insn-00c571fc)

~~~diff
- 00bda7c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bda7c4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bda7c4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:10:8"]]
- 00bda7c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bda7c4 bytes 282901a9
+ 00c57214 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c57214 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00c57214 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:10:8"]]
+ 00c57214 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c57214 bytes 282901a9
- 00bda7ac ["INT_ADD", "register:40f0:8", ["const:bda7ac:8", "const:4:8"]]
- 00bda7ac ["CALL", null, ["callee:00c5721c:8"]]
+ 00c571fc ["INT_ADD", "register:40f0:8", ["const:c571fc:8", "const:4:8"]]
+ 00c571fc ["CALL", null, ["callee:00c5721c:8"]]
- 00bda7ac bytes 08000094
+ 00c571fc bytes 08000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d49dbbea2512dbb136aeaa218db3371"></a>

### [`00bdaea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaea4.md) → [`00c578ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md) _Znwm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaf0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c5793c"
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
      "unmatched:00bdaef4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "unmatched:00bdaf04",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf04",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c5793c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "00c5794c",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5794c",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaea4.md#insn-00bdaef4) · [`00bdaf0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaea4.md#insn-00bdaf0c)
- 新版 [`00c5793c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md#insn-00c5793c)

~~~diff
- 00bdaef4 ["INT_ADD", "register:40f0:8", ["const:bdaef4:8", "const:4:8"]]
- 00bdaef4 ["CALL", null, ["ram:bdbbf0:8"]]
- 00bdaef4 bytes 3f030094
- 00bdaf0c ["INT_ADD", "register:40f0:8", ["const:bdaf0c:8", "const:4:8"]]
- 00bdaf0c ["CALL", null, ["callee:00c57b10:8"]]
- 00bdaf0c bytes 6d000094
+ 00c5793c ["INT_ADD", "register:40f0:8", ["const:c5793c:8", "const:4:8"]]
+ 00c5793c ["CALL", null, ["ram:c58640:8"]]
+ 00c5793c bytes 41030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803d027e4a1283167b1dee865673c898"></a>

### [`00bdaf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md) → [`00c57960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57960.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f00.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md) [`00be1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e20.md)
- 新版 呼出元 1件 [`00c5eac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eac0.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md) [`00c5e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 22.22% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaf3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c57984"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaf8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "unmatched:00bdaf9c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf9c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c579d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "00c579e4",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c579e4",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md#insn-00bdaf3c) · [`00bdaf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md#insn-00bdaf8c) · [`00bdafa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaf18.md#insn-00bdafa4)

~~~diff
- 00bdaf3c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdaf3c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bdaf3c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00bdaf3c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bdaf3c bytes 3480889a
- 00bdaf8c ["INT_ADD", "register:40f0:8", ["const:bdaf8c:8", "const:4:8"]]
- 00bdaf8c ["CALL", null, ["ram:bdbbf0:8"]]
- 00bdaf8c bytes 19030094
- 00bdafa4 ["INT_ADD", "register:40f0:8", ["const:bdafa4:8", "const:4:8"]]
- 00bdafa4 ["CALL", null, ["callee:00c57b10:8"]]
- 00bdafa4 bytes 47000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-966f50730b166b01d633368bfccc2cfe"></a>

### [`00bdaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaff0.md) → [`00c57a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a40.md) &lt;EXTERNAL&gt;::__register_atfork

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00418320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418320.md) · 呼出先 1件 [`010a5010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5010.md)
- 新版 呼出元 1件 [`0043ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae20.md) · 呼出先 1件 [`0112a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a010.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaff4",
      "READ",
      [
        "storage",
        "00c1c0b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a010"
      ]
    ]
  ],
  "added": [
    [
      "00c57a44",
      "READ",
      [
        "storage",
        "00c9bae0",
        null,
        "pointer"
      ]
    ],
    [
      "00c57a4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaff0.md#insn-00bdaff0) · [`00bdaff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaff0.md#insn-00bdaff4) · [`00bdaff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaff0.md#insn-00bdaff8)

~~~diff
- 00bdaff0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdaff0 bytes 100200d0
- 00bdaff4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b0:8"]]
- 00bdaff4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaff4 bytes 115a40f9
- 00bdaff8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00bdaff8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 bytes 10c20291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f668efcb62358d7b032cf550e748da4b"></a>

### [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) → [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) __cxa_guard_release

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 356件 [`00418338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) [`004184bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) [`004185a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) [`00419640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md) [`004196bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md) · 呼出先 1件 [`00bba844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md)
- 新版 呼出元 347件 [`0043ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae38.md) [`0043afbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) [`0043b0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) [`0043c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c140.md) [`0043c1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c1bc.md) · 呼出先 1件 [`00c3728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb024",
      "READ",
      [
        "storage",
        "00c1c0c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb02c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00c3728c"
      ]
    ]
  ],
  "added": [
    [
      "00c57a74",
      "READ",
      [
        "storage",
        "00c9baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57a7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00c3728c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md#insn-00bdb020) · [`00bdb024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md#insn-00bdb024) · [`00bdb028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md#insn-00bdb028)

~~~diff
- 00bdb020 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb020 bytes 100200b0
- 00bdb024 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c8:8"]]
- 00bdb024 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb024 bytes 116640f9
- 00bdb028 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00bdb028 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb028 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb028 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb028 bytes 10220391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97a96daca77502ba9249233837f510ed"></a>

### [`00bdb0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md) → [`00c57b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b30.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00418c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c88.md) [`0041fe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fe40.md) [`00ae0510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0510.md) [`00b7b3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3b0.md) · 呼出先 1件 [`00b737b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md)
- 新版 呼出元 4件 [`0043b788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b788.md) [`00442940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442940.md) [`00b3fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fee8.md) [`00bf7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7df8.md) · 呼出先 1件 [`00bf03bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb0e4",
      "READ",
      [
        "storage",
        "00c1c128",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb0ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf03bc"
      ]
    ]
  ],
  "added": [
    [
      "00c57b34",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c57b3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf03bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md#insn-00bdb0e0) · [`00bdb0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md#insn-00bdb0e4) · [`00bdb0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md#insn-00bdb0e8)

~~~diff
- 00bdb0e0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb0e0 bytes 100200b0
- 00bdb0e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:128:8"]]
- 00bdb0e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb0e4 bytes 119640f9
- 00bdb0e8 ["COPY", "tmp:0:8", ["const:128:8"]]
- 00bdb0e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb0e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb0e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb0e8 bytes 10a20491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-945cc92ada6ce9dfd6dcbc33720bb85f"></a>

### [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) → [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) _ZNSt6__ndk15mutex6unlockEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 92件 [`00423bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) [`00423f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f08.md) [`00428128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) · 呼出先 1件 [`00b7d314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d314.md)
- 新版 呼出元 92件 [`004466bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) [`00446a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446a08.md) [`0044ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac28.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) · 呼出先 1件 [`00bf9d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d5c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb2a4",
      "READ",
      [
        "storage",
        "00c1c208",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb2ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9d5c"
      ]
    ]
  ],
  "added": [
    [
      "00c57cf4",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ],
    [
      "00c57cfc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf9d5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md#insn-00bdb2a0) · [`00bdb2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md#insn-00bdb2a4) · [`00bdb2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md#insn-00bdb2a8)

~~~diff
- 00bdb2a0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb2a0 bytes 100200b0
- 00bdb2a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:208:8"]]
- 00bdb2a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb2a4 bytes 110641f9
- 00bdb2a8 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bdb2a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb2a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb2a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb2a8 bytes 10220891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddcca0d1ae3a49eb43d7ae9a6955dbb0"></a>

### [`00bdb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md) → [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`00428128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md) [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) [`00450398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md) [`0045c7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md) [`00474da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md) · 呼出先 1件 [`00b7d874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d874.md)
- 新版 呼出元 14件 [`0044ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac28.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00473230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md) [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) · 呼出先 1件 [`00bfa2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2bc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb334",
      "READ",
      [
        "storage",
        "00c1c250",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb33c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bfa2bc"
      ]
    ]
  ],
  "added": [
    [
      "00c57d84",
      "READ",
      [
        "storage",
        "00c9bc80",
        null,
        "pointer"
      ]
    ],
    [
      "00c57d8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bfa2bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md#insn-00bdb330) · [`00bdb334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md#insn-00bdb334) · [`00bdb338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md#insn-00bdb338)

~~~diff
- 00bdb330 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb330 bytes 100200b0
- 00bdb334 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:250:8"]]
- 00bdb334 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb334 bytes 112a41f9
- 00bdb338 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00bdb338 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb338 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb338 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb338 bytes 10420991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1910b39e5e8b9be038d36c216fd0f5d"></a>

### [`00bdb3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3c0.md) → [`00c57e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e10.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEd

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00b2b454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b454.md) · 呼出先 1件 [`00b385cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b385cc.md)
- 新版 呼出元 2件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00b91504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91504.md) · 呼出先 1件 [`00ba1868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1868.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb3c4",
      "READ",
      [
        "storage",
        "00c1c298",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb3cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba1868"
      ]
    ]
  ],
  "added": [
    [
      "00c57e14",
      "READ",
      [
        "storage",
        "00c9bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57e1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba1868"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3c0.md#insn-00bdb3c0) · [`00bdb3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3c0.md#insn-00bdb3c4) · [`00bdb3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3c0.md#insn-00bdb3c8)

~~~diff
- 00bdb3c0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb3c0 bytes 100200b0
- 00bdb3c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:298:8"]]
- 00bdb3c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb3c4 bytes 114e41f9
- 00bdb3c8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00bdb3c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb3c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb3c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb3c8 bytes 10620a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b1769d042a8959e64312e73778c3ca"></a>

### [`00bdb650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md) → [`00c580a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580a0.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md) · 呼出先 1件 [`00b7cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md)
- 新版 呼出元 3件 [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) [`0053906c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md) [`00587af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md) · 呼出先 1件 [`00bf95e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb654",
      "READ",
      [
        "storage",
        "00c1c3e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb65c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf95e8"
      ]
    ]
  ],
  "added": [
    [
      "00c580a4",
      "READ",
      [
        "storage",
        "00c9be10",
        null,
        "pointer"
      ]
    ],
    [
      "00c580ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf95e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md#insn-00bdb650) · [`00bdb654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md#insn-00bdb654) · [`00bdb658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md#insn-00bdb658)

~~~diff
- 00bdb650 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb650 bytes 100200b0
- 00bdb654 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3e0:8"]]
- 00bdb654 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb654 bytes 11f241f9
- 00bdb658 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 00bdb658 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb658 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb658 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb658 bytes 10820f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f405e027302da8811b6b3eb3eb2446b3"></a>

### [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md) → [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md) _ZNSt13exception_ptrC1ERKS_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md) [`00b72b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b88.md) [`00b7cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md) · 呼出先 1件 [`00b72a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a68.md)
- 新版 呼出元 7件 [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) [`0053906c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053906c.md) [`00587af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md) [`00bef790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef790.md) [`00bf9500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md) · 呼出先 1件 [`00bef670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef670.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb664",
      "READ",
      [
        "storage",
        "00c1c3e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb66c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bef670"
      ]
    ]
  ],
  "added": [
    [
      "00c580b4",
      "READ",
      [
        "storage",
        "00c9be18",
        null,
        "pointer"
      ]
    ],
    [
      "00c580bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bef670"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md#insn-00bdb660) · [`00bdb664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md#insn-00bdb664) · [`00bdb668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md#insn-00bdb668)

~~~diff
- 00bdb660 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb660 bytes 100200b0
- 00bdb664 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:3e8:8"]]
- 00bdb664 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb664 bytes 11f641f9
- 00bdb668 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00bdb668 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb668 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb668 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb668 bytes 10a20f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5617e50897bfbffaeab456e3b4d4fb7a"></a>

### [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) → [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) _ZN5Botan11BER_Decoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 33件 [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004c56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md) [`004c5ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md) · 呼出先 1件 [`00482990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482990.md)
- 新版 呼出元 33件 [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`004e8548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md) [`004e8960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md) · 呼出先 1件 [`004a5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5828.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8b4",
      "READ",
      [
        "storage",
        "00c1c510",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a5828"
      ]
    ]
  ],
  "added": [
    [
      "00c58304",
      "READ",
      [
        "storage",
        "00c9bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00c5830c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a5828"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md#insn-00bdb8b0) · [`00bdb8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md#insn-00bdb8b4) · [`00bdb8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md#insn-00bdb8b8)

~~~diff
- 00bdb8b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8b0 bytes 100200b0
- 00bdb8b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:510:8"]]
- 00bdb8b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8b4 bytes 118a42f9
- 00bdb8b8 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00bdb8b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 bytes 10421491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a014126219cf395a3dc3918afd00ab83"></a>

### [`00bdb910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md) → [`00c58360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58360.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00489628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md) · 呼出先 1件 [`0048322c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md)
- 新版 呼出元 1件 [`004ac4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md) · 呼出先 1件 [`004a60c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb914",
      "READ",
      [
        "storage",
        "00c1c540",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb91c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a60c4"
      ]
    ]
  ],
  "added": [
    [
      "00c58364",
      "READ",
      [
        "storage",
        "00c9bf70",
        null,
        "pointer"
      ]
    ],
    [
      "00c5836c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a60c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md#insn-00bdb910) · [`00bdb914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md#insn-00bdb914) · [`00bdb918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md#insn-00bdb918)

~~~diff
- 00bdb910 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb910 bytes 100200b0
- 00bdb914 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:540:8"]]
- 00bdb914 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb914 bytes 11a242f9
- 00bdb918 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00bdb918 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb918 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb918 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb918 bytes 10021591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27ff0c5b1e4aed6462022eb54125492"></a>

### [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md) → [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00483728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483728.md) [`004839c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md) [`00484b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484b8c.md) [`00489628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md) [`0048a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md) · 呼出先 1件 [`00b79858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md)
- 新版 呼出元 15件 [`004a65c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a65c0.md) [`004a685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md) [`004a7a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7a24.md) [`004ac4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md) [`004acf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md) · 呼出先 1件 [`00bf62a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb944",
      "READ",
      [
        "storage",
        "00c1c558",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb94c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf62a0"
      ]
    ]
  ],
  "added": [
    [
      "00c58394",
      "READ",
      [
        "storage",
        "00c9bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00c5839c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bf62a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md#insn-00bdb940) · [`00bdb944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md#insn-00bdb944) · [`00bdb948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md#insn-00bdb948)

~~~diff
- 00bdb940 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb940 bytes 100200b0
- 00bdb944 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:558:8"]]
- 00bdb944 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb944 bytes 11ae42f9
- 00bdb948 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00bdb948 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb948 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb948 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb948 bytes 10621591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42296f069649ee44019b811abf6c3ff5"></a>

### [`00bdb950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md) → [`00c583a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583a0.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00490d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490d78.md) [`004c73c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md) [`004cf634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md) [`004ee7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md) · 呼出先 1件 [`0048fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md)
- 新版 呼出元 7件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004b3c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3c10.md) [`004ea25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md) [`004f24cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md) [`00511670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md) · 呼出先 1件 [`004b28a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb954",
      "READ",
      [
        "storage",
        "00c1c560",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb95c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b28a4"
      ]
    ]
  ],
  "added": [
    [
      "00c583a4",
      "READ",
      [
        "storage",
        "00c9bf90",
        null,
        "pointer"
      ]
    ],
    [
      "00c583ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b28a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md#insn-00bdb950) · [`00bdb954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md#insn-00bdb954) · [`00bdb958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md#insn-00bdb958)

~~~diff
- 00bdb950 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb950 bytes 100200b0
- 00bdb954 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:560:8"]]
- 00bdb954 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb954 bytes 11b242f9
- 00bdb958 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00bdb958 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb958 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb958 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb958 bytes 10821591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58d5357a9739af669c3801dcdd4a4bcb"></a>

### [`00bdb980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md) → [`00c583d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583d0.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00484570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md) · 呼出先 1件 [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md)
- 新版 呼出元 1件 [`004a7408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md) · 呼出先 1件 [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb984",
      "READ",
      [
        "storage",
        "00c1c578",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb98c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a75ec"
      ]
    ]
  ],
  "added": [
    [
      "00c583d4",
      "READ",
      [
        "storage",
        "00c9bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00c583dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a75ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md#insn-00bdb980) · [`00bdb984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md#insn-00bdb984) · [`00bdb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md#insn-00bdb988)

~~~diff
- 00bdb980 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb980 bytes 100200b0
- 00bdb984 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:578:8"]]
- 00bdb984 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb984 bytes 11be42f9
- 00bdb988 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00bdb988 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb988 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb988 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb988 bytes 10e21591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-349307902f625bbe6604080de107e25b"></a>

### [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md) → [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) [`0048ae8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md) [`00491ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491ef0.md) [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) [`004c5e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5e50.md) · 呼出先 1件 [`0048bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md)
- 新版 呼出元 9件 [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) [`004add24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md) [`004b4d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4d88.md) [`004e6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md) [`004e8ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8ce8.md) · 呼出先 1件 [`004aee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb9a4",
      "READ",
      [
        "storage",
        "00c1c588",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb9ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aee1c"
      ]
    ]
  ],
  "added": [
    [
      "00c583f4",
      "READ",
      [
        "storage",
        "00c9bfb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c583fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aee1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md#insn-00bdb9a0) · [`00bdb9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md#insn-00bdb9a4) · [`00bdb9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md#insn-00bdb9a8)

~~~diff
- 00bdb9a0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb9a0 bytes 100200b0
- 00bdb9a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:588:8"]]
- 00bdb9a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb9a4 bytes 11c642f9
- 00bdb9a8 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00bdb9a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb9a8 bytes 10221691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaaf0cca844d278926c631b4c93794e5"></a>

### [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md) → [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md) _ZNK5Botan3OID9as_stringEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) [`004873a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) [`004c585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md) · 呼出先 1件 [`00484b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484b8c.md)
- 新版 呼出元 12件 [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) [`004aa23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md) [`004e86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md) · 呼出先 1件 [`004a7a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7a24.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb9b4",
      "READ",
      [
        "storage",
        "00c1c590",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb9bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a7a24"
      ]
    ]
  ],
  "added": [
    [
      "00c58404",
      "READ",
      [
        "storage",
        "00c9bfc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5840c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a7a24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md#insn-00bdb9b0) · [`00bdb9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md#insn-00bdb9b4) · [`00bdb9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md#insn-00bdb9b8)

~~~diff
- 00bdb9b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb9b0 bytes 100200b0
- 00bdb9b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:590:8"]]
- 00bdb9b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb9b4 bytes 11ca42f9
- 00bdb9b8 ["COPY", "tmp:0:8", ["const:590:8"]]
- 00bdb9b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb9b8 bytes 10421691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc665323b709c747fa834268ff60f6e0"></a>

### [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) → [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 23件 [`00484f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md) [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) [`0048a574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a574.md) [`0048a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5bc.md) [`0048b6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md) · 呼出先 1件 [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md)
- 新版 呼出元 23件 [`004a7de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md) [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) [`004ad40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad40c.md) [`004ad454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad454.md) [`004ae544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md) · 呼出先 1件 [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb9d4",
      "READ",
      [
        "storage",
        "00c1c5a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb9dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ad470"
      ]
    ]
  ],
  "added": [
    [
      "00c58424",
      "READ",
      [
        "storage",
        "00c9bfd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5842c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ad470"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md#insn-00bdb9d0) · [`00bdb9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md#insn-00bdb9d4) · [`00bdb9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md#insn-00bdb9d8)

~~~diff
- 00bdb9d0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb9d0 bytes 100200b0
- 00bdb9d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:5a0:8"]]
- 00bdb9d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb9d4 bytes 11d242f9
- 00bdb9d8 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00bdb9d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb9d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb9d8 bytes 10821691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5744a9458de208b76a0aa20c26f0b1"></a>

### [`00bdba10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba10.md) → [`00c58460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58460.md) _ZNK5Botan14ASN1_Formatter15print_to_streamERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEEPKhm

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00485cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md) · 呼出先 1件 [`00485e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485e70.md)
- 新版 呼出元 1件 [`004a8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md) · 呼出先 1件 [`004a8d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdba14",
      "READ",
      [
        "storage",
        "00c1c5c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdba1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a8d08"
      ]
    ]
  ],
  "added": [
    [
      "00c58464",
      "READ",
      [
        "storage",
        "00c9bff0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5846c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a8d08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdba10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba10.md#insn-00bdba10) · [`00bdba14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba10.md#insn-00bdba14) · [`00bdba18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba10.md#insn-00bdba18)

~~~diff
- 00bdba10 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdba10 bytes 100200b0
- 00bdba14 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:5c0:8"]]
- 00bdba14 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdba14 bytes 11e242f9
- 00bdba18 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00bdba18 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdba18 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdba18 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdba18 bytes 10021791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99d4bf7d2ffc002c7c572a5fec77bec2"></a>

### [`00bdbc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md) → [`00c58670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58670.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`0048dc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc08.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004c13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md) [`004c5ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md) [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) · 呼出先 1件 [`0048dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md)
- 新版 呼出元 10件 [`004b0aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aa0.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`004e4288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md) [`004e8960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) · 呼出先 1件 [`004b0aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbc24",
      "READ",
      [
        "storage",
        "00c1c6c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbc2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b0aac"
      ]
    ]
  ],
  "added": [
    [
      "00c58674",
      "READ",
      [
        "storage",
        "00c9c0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5867c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b0aac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md#insn-00bdbc20) · [`00bdbc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md#insn-00bdbc24) · [`00bdbc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md#insn-00bdbc28)

~~~diff
- 00bdbc20 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbc20 bytes 100200b0
- 00bdbc24 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:6c8:8"]]
- 00bdbc24 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbc24 bytes 116643f9
- 00bdbc28 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00bdbc28 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbc28 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbc28 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbc28 bytes 10221b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145f869e6e849180532b143757db6748"></a>

### [`00bdbd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd70.md) → [`00c587c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587c0.md) _ZN5Botan13base64_encodeEPcPKhmRmb

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00492b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md) · 呼出先 1件 [`004929ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004929ac.md)
- 新版 呼出元 1件 [`004b5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md) · 呼出先 1件 [`004b5844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5844.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbd74",
      "READ",
      [
        "storage",
        "00c1c770",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbd7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b5844"
      ]
    ]
  ],
  "added": [
    [
      "00c587c4",
      "READ",
      [
        "storage",
        "00c9c1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00c587cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b5844"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd70.md#insn-00bdbd70) · [`00bdbd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd70.md#insn-00bdbd74) · [`00bdbd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd70.md#insn-00bdbd78)

~~~diff
- 00bdbd70 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbd70 bytes 100200b0
- 00bdbd74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:770:8"]]
- 00bdbd74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbd74 bytes 11ba43f9
- 00bdbd78 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00bdbd78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbd78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbd78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbd78 bytes 10c21d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14a2fb2d3116afddfff3a3bff6c1891b"></a>

### [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) → [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) _ZN5BotanmlERKNS_6BigIntES2_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 13件 [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) [`004b5004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md) [`004b8d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md) [`004bc070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md) [`004bc440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md) · 呼出先 1件 [`0049731c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md)
- 新版 呼出元 13件 [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) [`004d7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md) [`004dbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md) [`004def08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md) [`004df2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md) · 呼出先 1件 [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbe04",
      "READ",
      [
        "storage",
        "00c1c7b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbe0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ba1b4"
      ]
    ]
  ],
  "added": [
    [
      "00c58854",
      "READ",
      [
        "storage",
        "00c9c1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5885c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ba1b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md#insn-00bdbe00) · [`00bdbe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md#insn-00bdbe04) · [`00bdbe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md#insn-00bdbe08)

~~~diff
- 00bdbe00 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbe00 bytes 100200b0
- 00bdbe04 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:7b8:8"]]
- 00bdbe04 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbe04 bytes 11de43f9
- 00bdbe08 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00bdbe08 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe08 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe08 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbe08 bytes 10e21e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6919757eb98045b241ed2d0e0069040"></a>

### [`00bdc160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md) → [`00c58bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`004a3d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md) [`004ae010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) · 呼出先 1件 [`004d9ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md)
- 新版 呼出元 12件 [`004c6c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md) [`004d0ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md) · 呼出先 1件 [`004fcd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc164",
      "READ",
      [
        "storage",
        "00c1c968",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc16c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fcd68"
      ]
    ]
  ],
  "added": [
    [
      "00c58bb4",
      "READ",
      [
        "storage",
        "00c9c398",
        null,
        "pointer"
      ]
    ],
    [
      "00c58bbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fcd68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md#insn-00bdc160) · [`00bdc164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md#insn-00bdc164) · [`00bdc168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md#insn-00bdc168)

~~~diff
- 00bdc160 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc160 bytes 10020090
- 00bdc164 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:968:8"]]
- 00bdc164 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc164 bytes 11b644f9
- 00bdc168 ["COPY", "tmp:0:8", ["const:968:8"]]
- 00bdc168 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc168 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc168 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc168 bytes 10a22591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c25b1276376f46dae0222c654efde5"></a>

### [`00bdc340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md) → [`00c58d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d90.md) _ZNK5Botan4HMAC4nameEv

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004aa3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa3fc.md) · 呼出先 1件 [`004aa2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md)
- 新版 呼出元 1件 [`004cd294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd294.md) · 呼出先 1件 [`004cd184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc344",
      "READ",
      [
        "storage",
        "00c1ca58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc34c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004cd184"
      ]
    ]
  ],
  "added": [
    [
      "00c58d94",
      "READ",
      [
        "storage",
        "00c9c488",
        null,
        "pointer"
      ]
    ],
    [
      "00c58d9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004cd184"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md#insn-00bdc340) · [`00bdc344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md#insn-00bdc344) · [`00bdc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md#insn-00bdc348)

~~~diff
- 00bdc340 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc340 bytes 10020090
- 00bdc344 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a58:8"]]
- 00bdc344 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc344 bytes 112e45f9
- 00bdc348 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00bdc348 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc348 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc348 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc348 bytes 10622991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38395ff50ca3dcb6dbe1b0871a66757e"></a>

### [`00bdc540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md) → [`00c58f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f90.md) _ZN5Botan3lcmERKNS_6BigIntES2_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004c5f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md) [`004cfcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md) [`004d04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md) [`004d0c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md) [`004d1904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md) · 呼出先 1件 [`004b8d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md)
- 新版 呼出元 5件 [`004e8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md) [`004f2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md) [`004f3358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md) [`004f3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md) [`004f479c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md) · 呼出先 1件 [`004dbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc544",
      "READ",
      [
        "storage",
        "00c1cb58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc54c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbbdc"
      ]
    ]
  ],
  "added": [
    [
      "00c58f94",
      "READ",
      [
        "storage",
        "00c9c588",
        null,
        "pointer"
      ]
    ],
    [
      "00c58f9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbbdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md#insn-00bdc540) · [`00bdc544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md#insn-00bdc544) · [`00bdc548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md#insn-00bdc548)

~~~diff
- 00bdc540 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc540 bytes 10020090
- 00bdc544 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b58:8"]]
- 00bdc544 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc544 bytes 11ae45f9
- 00bdc548 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00bdc548 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 bytes 10622d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-385af3fed5a1b923051f6eaf954cf135"></a>

### [`00bdc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md) → [`00c58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fa0.md) _ZN5Botan25almost_montgomery_inverseERNS_6BigIntERKS0_S3_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004b97b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b97b0.md) · 呼出先 1件 [`004b8e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md)
- 新版 呼出元 1件 [`004dc648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc648.md) · 呼出先 1件 [`004dbcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc554",
      "READ",
      [
        "storage",
        "00c1cb60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbcf0"
      ]
    ]
  ],
  "added": [
    [
      "00c58fa4",
      "READ",
      [
        "storage",
        "00c9c590",
        null,
        "pointer"
      ]
    ],
    [
      "00c58fac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbcf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md#insn-00bdc550) · [`00bdc554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md#insn-00bdc554) · [`00bdc558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md#insn-00bdc558)

~~~diff
- 00bdc550 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc550 bytes 10020090
- 00bdc554 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b60:8"]]
- 00bdc554 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc554 bytes 11b245f9
- 00bdc558 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00bdc558 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 bytes 10822d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7326322f8f9b923f725eb5fc144b94b3"></a>

### [`00bdc610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc610.md) → [`00c59060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59060.md) _ZN5Botan11BER_Decoder15decode_optionalImEERS0_RT_NS_8ASN1_TagES5_RKS3_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004e637c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md) [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) [`004f52c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f5/004f52c8.md) · 呼出先 1件 [`004c13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md)
- 新版 呼出元 7件 [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`00509214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md) [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) [`00518160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518160.md) · 呼出先 1件 [`004e4288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc614",
      "READ",
      [
        "storage",
        "00c1cbc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc61c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e4288"
      ]
    ]
  ],
  "added": [
    [
      "00c59064",
      "READ",
      [
        "storage",
        "00c9c5f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c5906c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e4288"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc610.md#insn-00bdc610) · [`00bdc614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc610.md#insn-00bdc614) · [`00bdc618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc610.md#insn-00bdc618)

~~~diff
- 00bdc610 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc610 bytes 10020090
- 00bdc614 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc0:8"]]
- 00bdc614 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc614 bytes 11e245f9
- 00bdc618 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00bdc618 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc618 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc618 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc618 bytes 10022f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d73223a0e810e8a7301eeee2c15af2"></a>

### [`00bdc620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc620.md) → [`00c59070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59070.md) _ZN5Botan11BER_Decoder15decode_optionalINS_19AlgorithmIdentifierEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) [`004fcb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fcb38.md) · 呼出先 1件 [`004c15a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md)
- 新版 呼出元 2件 [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) [`0051f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md) · 呼出先 1件 [`004e443c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc624",
      "READ",
      [
        "storage",
        "00c1cbc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc62c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e443c"
      ]
    ]
  ],
  "added": [
    [
      "00c59074",
      "READ",
      [
        "storage",
        "00c9c5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c5907c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e443c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc620.md#insn-00bdc620) · [`00bdc624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc620.md#insn-00bdc624) · [`00bdc628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc620.md#insn-00bdc628)

~~~diff
- 00bdc620 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc620 bytes 10020090
- 00bdc624 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc8:8"]]
- 00bdc624 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc624 bytes 11e645f9
- 00bdc628 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00bdc628 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc628 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc628 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc628 bytes 10222f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

