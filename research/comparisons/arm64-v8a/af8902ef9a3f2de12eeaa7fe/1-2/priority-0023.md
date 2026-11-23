# v15.7.4 → v16.0.0 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-4c32c2b26c05c9cee47f7076119f1e58"></a>

### [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) → [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) FUN_005cde4c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) [`005a94a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md) [`005b0b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md) · 呼出先 3件 [`005b04a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04a4.md) [`005b0b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) [`005ce174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce174.md) [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) · 呼出先 3件 [`005d5170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5170.md) [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 6.45% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 10件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a928c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a92b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a92b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cde80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005a92f0"
      ]
    ],
    [
      "005cdea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005a92f0"
      ]
    ],
    [
      "unmatched:005a91f0",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cde80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cdfbc"
      ]
    ],
    [
      "005cdea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cdfbc"
      ]
    ],
    [
      "005cdebc",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a91c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md#insn-005a91c8) · [`005a9254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md#insn-005a9254) · [`005a925c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md#insn-005a925c)
- 新版 [`005cdf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md#insn-005cdf10) · [`005cdf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md#insn-005cdf28)

~~~diff
- 005a91c8 ["INT_ADD", "register:40f0:8", ["const:5a91c8:8", "const:4:8"]]
- 005a91c8 ["CALL", null, ["callee:005d582c:8"]]
+ 005cdf10 ["INT_ADD", "register:40f0:8", ["const:5cdf10:8", "const:4:8"]]
+ 005cdf10 ["CALL", null, ["callee:005d582c:8"]]
- 005a91c8 bytes 661e0094
+ 005cdf10 bytes 471e0094
- 005a9254 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 005a9254 bytes e0040054
- 005a925c ["INT_ADD", "register:40f0:8", ["const:5a925c:8", "const:4:8"]]
- 005a925c ["CALL", null, ["callee:00c57a90:8"]]
+ 005cdf28 ["INT_ADD", "register:40f0:8", ["const:5cdf28:8", "const:4:8"]]
+ 005cdf28 ["CALL", null, ["callee:00c57a90:8"]]
- 005a925c bytes 79c71894
+ 005cdf28 bytes da261a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e5776472e64b66d615e4df6dc09737f"></a>

### [`005a92f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a92f4.md) → [`005cdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdfc0.md) FUN_005cdfc0

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) · 呼出先 3件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) · 呼出先 3件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 13.33% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a93c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a93c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005a933c",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005ce038",
      "DATA",
      [
        "storage",
        "00bf3718",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005a93a0",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce008",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ],
    [
      "005ce038",
      "DATA",
      [
        "storage",
        "00c70740",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce06c",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a932c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a92f4.md#insn-005a932c) · [`005a9370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a92f4.md#insn-005a9370) · [`005a93c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a92f4.md#insn-005a93c4)
- 新版 [`005cdff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdfc0.md#insn-005cdff8)

~~~diff
- 005a932c ["INT_ADD", "register:40f0:8", ["const:5a932c:8", "const:4:8"]]
- 005a932c ["CALL", null, ["callee:00c57bd0:8"]]
+ 005cdff8 ["INT_ADD", "register:40f0:8", ["const:5cdff8:8", "const:4:8"]]
+ 005cdff8 ["CALL", null, ["callee:00c57bd0:8"]]
- 005a932c bytes 95c71894
+ 005cdff8 bytes f6261a94
- 005a9370 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005a9370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005a9370 bytes 080400f9
- 005a93c4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005a93c4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005a93c4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005a93c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005a93c4 bytes 1a2000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66ef3e9f2b9bb8a4c9f7e4a97fdefcf"></a>

### [`005a94a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md) → [`005ce174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce174.md) FUN_005ce174

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) · 呼出先 3件 [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) · 呼出先 3件 [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a95a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a95a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005a94f0",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005ce1ec",
      "DATA",
      [
        "storage",
        "00bf3718",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005a9554",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce1bc",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ],
    [
      "005ce1ec",
      "DATA",
      [
        "storage",
        "00c70740",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce220",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md#insn-005a9514) · [`005a9524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md#insn-005a9524) · [`005a953c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md#insn-005a953c)
- 新版 [`005ce1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce174.md#insn-005ce1e0)

~~~diff
- 005a9514 ["INT_ADD", "register:40f0:8", ["const:5a9514:8", "const:4:8"]]
- 005a9514 ["CALL", null, ["callee:00c57a90:8"]]
+ 005ce1e0 ["INT_ADD", "register:40f0:8", ["const:5ce1e0:8", "const:4:8"]]
+ 005ce1e0 ["CALL", null, ["callee:00c57a90:8"]]
- 005a9514 bytes cbc61894
+ 005ce1e0 bytes 2c261a94
- 005a9524 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005a9524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005a9524 bytes 080400f9
- 005a953c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005a953c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005a953c ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 005a953c ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 005a953c bytes b606959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f155577e74cdb6b888a38f516c55a9a"></a>

### [`005a96ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a96ac.md) → [`005ce378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce378.md) FUN_005ce378

採用 · 移動量 `+0x24ccc` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-a31cedada0a91b2b2edb13d0eefbedf2"></a>

### [`005a971c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a971c.md) → [`005ce3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce3e8.md) FUN_005ce3e8

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ce3f4",
      "incomplete_value": true,
      "site": "005ce3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9728",
      "incomplete_value": true,
      "site": "005a972c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9730"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005ce3fc"
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
      "005ce3ec",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce3f8",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005a9730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce42c"
      ]
    ]
  ],
  "added": [
    [
      "005ce3ec",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005ce3f8",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce3fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce42c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a971c.md#insn-005a9730) · [`005a971c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a971c.md#insn-005a971c)
- 新版 [`005ce3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce3e8.md#insn-005ce3fc) · [`005ce3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce3e8.md#insn-005ce3e8)

~~~diff
- 005a9730 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005a9730 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005a9730 bytes 880100b4
+ 005ce3fc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005ce3fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 005ce3fc bytes 880100b4
- 005a971c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005ce3e8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005a971c bytes 893300d0
+ 005ce3e8 bytes 69360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267759161b6a55ca17344ab196c4c3b1"></a>

### [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) → [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) FUN_005ce48c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) · 呼出先 3件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md)
- 新版 呼出元 1件 [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) · 呼出先 3件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9808"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005ce4d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005a9834",
      "incomplete_value": true,
      "site": "005a983c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005a9808",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce514"
      ]
    ]
  ],
  "added": [
    [
      "005ce4d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce514"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md#insn-005a9808) · [`005a983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md#insn-005a983c)
- 新版 [`005ce508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md#insn-005ce508) · [`005ce4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md#insn-005ce4d4)

~~~diff
- 005a9808 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 005a9808 bytes 00020054
- 005a983c ["INT_ADD", "register:40f0:8", ["const:5a983c:8", "const:4:8"]]
- 005a983c ["CALL", null, ["callee:005ce924:8"]]
+ 005ce508 ["INT_ADD", "register:40f0:8", ["const:5ce508:8", "const:4:8"]]
+ 005ce508 ["CALL", null, ["callee:005ce924:8"]]
- 005a983c bytes 07010094
+ 005ce508 bytes 07010094
+ 005ce4d4 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 005ce4d4 bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c85772d870cbab9ee948ebda069c081"></a>

### [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) → [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) FUN_005ce52c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`005a8e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8e3c.md) · 呼出先 3件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md)
- 新版 呼出元 1件 [`005cdb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdb08.md) · 呼出先 3件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005a9880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md#insn-005a9880) · [`005a98b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md#insn-005a98b4)
- 新版 [`005ce54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md#insn-005ce54c) · [`005ce580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md#insn-005ce580)

~~~diff
- 005a9880 ["INT_ADD", "register:40f0:8", ["const:5a9880:8", "const:4:8"]]
- 005a9880 ["CALL", null, ["callee:005ce5c0:8"]]
+ 005ce54c ["INT_ADD", "register:40f0:8", ["const:5ce54c:8", "const:4:8"]]
+ 005ce54c ["CALL", null, ["callee:005ce5c0:8"]]
- 005a9880 bytes 1d000094
+ 005ce54c bytes 1d000094
- 005a98b4 ["INT_ADD", "register:40f0:8", ["const:5a98b4:8", "const:4:8"]]
- 005a98b4 ["CALL", null, ["callee:005ce924:8"]]
+ 005ce580 ["INT_ADD", "register:40f0:8", ["const:5ce580:8", "const:4:8"]]
+ 005ce580 ["CALL", null, ["callee:005ce924:8"]]
- 005a98b4 bytes e9000094
+ 005ce580 bytes e9000094
~~~


<a id="compare-51cfa1b198200818822310147178ebb9"></a>

### [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) → [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) FUN_005ce5c0

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) · 呼出先 8件 [`005a8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a0c.md) [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) [`005aa270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa270.md) [`005aa2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md) [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md)
- 新版 呼出元 2件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) · 呼出先 8件 [`005cd6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md) [`005cd778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd778.md) [`005cef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cef3c.md) [`005cefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md) [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.44% / 新版 62.44%

CFGの説明率　旧版 14.06% / 新版 14.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a98f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a98f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a98fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005a98f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005a98fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005a9900",
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
      "005ce5c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005ce5c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005ce5cc",
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

- 旧版 [`005a98f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a98f8) · [`005a98fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a98fc) · [`005a9900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a9900)

~~~diff
- 005a98f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005a98f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005a98f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005a98f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005a98f8 bytes fd7b05a9
- 005a98fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 005a98fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005a98fc bytes f73300f9
- 005a9900 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005a9900 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005a9900 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005a9900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005a9900 bytes f65707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d81b217f5f58e86a2314ebb8ca5ff8ad"></a>

### [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) → [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) FUN_005ce924

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) · 呼出先 10件 [`005a8e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8e3c.md) [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005aba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005aba98.md) [`005abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md)
- 新版 呼出元 2件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) · 呼出先 10件 [`005cdb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdb08.md) [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0764.md) [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.23% / 新版 90.23%

CFGの説明率　旧版 46.77% / 新版 46.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ce97c",
      "incomplete_value": true,
      "site": "005ce98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9cb0",
      "incomplete_value": true,
      "site": "005a9cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a9da8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ce974",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005ce98c",
      "DATA",
      [
        "storage",
        "00bf38e0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005a9ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce9c8"
      ]
    ]
  ],
  "added": [
    [
      "005ce974",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005ce98c",
      "DATA",
      [
        "storage",
        "00c70908",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce9ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce9c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9ccc) · [`005a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9ce0) · [`005a9d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9d00)

~~~diff
- 005a9ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 005a9ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005a9ccc bytes 681e00f9
- 005a9ce0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005a9ce0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 005a9ce0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 005a9ce0 ["CBRANCH", null, ["local:b11:8", "tmp:2:1"]]
- 005a9ce0 bytes ec000054
- 005a9d00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005a9d00 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 005a9d00 bytes e10f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08410404d8ac003016bc9c9786dd5223"></a>

### [`005aa2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md) → [`005cefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md) FUN_005cefa8

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) · 呼出先 3件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 1件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa360"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005aa314",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005aa324",
      "DATA",
      [
        "storage",
        "00bf3898",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005cefe0",
      "READ",
      [
        "storage",
        "00c9aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005ceff0",
      "DATA",
      [
        "storage",
        "00c708c0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md#insn-005aa324) · [`005aa328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md#insn-005aa328) · [`005aa350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md#insn-005aa350)
- 新版 [`005ceff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md#insn-005ceff4) · [`005cf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cefa8.md#insn-005cf01c)

~~~diff
- 005aa324 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005aa324 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005aa324 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005aa324 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005aa324 bytes 092081a8
- 005aa328 ["INT_ADD", "register:40f0:8", ["const:5aa328:8", "const:4:8"]]
- 005aa328 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 005ceff4 ["INT_ADD", "register:40f0:8", ["const:5ceff4:8", "const:4:8"]]
+ 005ceff4 ["CALL", null, ["callee:00c5a3d0:8"]]
- 005aa328 bytes 96cd1894
+ 005ceff4 bytes f72c1a94
- 005aa350 ["INT_ADD", "register:40f0:8", ["const:5aa350:8", "const:4:8"]]
- 005aa350 ["CALL", null, ["callee:00c538b0:8"]]
+ 005cf01c ["INT_ADD", "register:40f0:8", ["const:5cf01c:8", "const:4:8"]]
+ 005cf01c ["CALL", null, ["callee:00c538b0:8"]]
- 005aa350 bytes c4b21894
+ 005cf01c bytes 25121a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c87009aefe336809c676fcdd21780878"></a>

### [`005aa3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa3dc.md) → [`005cf0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf0a8.md) FUN_005cf0a8

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cf0b4",
      "incomplete_value": true,
      "site": "005cf0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa3e8",
      "incomplete_value": true,
      "site": "005aa3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa410"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005cf0dc"
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
      "005cf0ac",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cf0b8",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005aa410",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005cf0ac",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf0b8",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf0dc",
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

- 旧版 [`005aa410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa3dc.md#insn-005aa410) · [`005aa3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa3dc.md#insn-005aa3dc)
- 新版 [`005cf0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf0a8.md#insn-005cf0dc) · [`005cf0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf0a8.md#insn-005cf0a8)

~~~diff
- 005aa410 ["COPY", "register:0:8", ["register:4048:8"]]
- 005aa410 ["INT_ADD", "register:40f0:8", ["const:5aa410:8", "const:4:8"]]
- 005aa410 ["CALLIND", null, ["register:0:8"]]
- 005aa410 bytes 20013fd6
+ 005cf0dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005cf0dc ["INT_ADD", "register:40f0:8", ["const:5cf0dc:8", "const:4:8"]]
+ 005cf0dc ["CALLIND", null, ["register:0:8"]]
+ 005cf0dc bytes 20013fd6
- 005aa3dc ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005cf0a8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005aa3dc bytes 893300b0
+ 005cf0a8 bytes 493600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b7c30c092d6abfb735360033da3be6"></a>

### [`005aa484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa484.md) → [`005cf150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf150.md) FUN_005cf150

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cf15c",
      "incomplete_value": true,
      "site": "005cf160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa490",
      "incomplete_value": true,
      "site": "005aa494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cf154",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005cf160",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005cf154",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf160",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa484.md#insn-005aa484) · [`005aa488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa484.md#insn-005aa488) · [`005aa498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa484.md#insn-005aa498)
- 新版 [`005cf150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf150.md#insn-005cf150) · [`005cf154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf150.md#insn-005cf154) · [`005cf164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf150.md#insn-005cf164)

~~~diff
- 005aa484 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005cf150 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005aa484 bytes 893300b0
+ 005cf150 bytes 493600f0
- 005aa488 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b0:8"]]
- 005aa488 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fa8:8"]]
+ 005cf154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa488 bytes 29d942f9
+ 005cf154 bytes 29d547f9
- 005aa498 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005aa498 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005cf164 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005cf164 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005aa498 bytes 880100b4
+ 005cf164 bytes 880100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd9ef98b654cde842c4728ae5053aac"></a>

### [`005aa4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa4cc.md) → [`005cf198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf198.md) FUN_005cf198

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aa504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa4cc.md#insn-005aa504)
- 新版 [`005cf1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf198.md#insn-005cf1d0)

~~~diff
- 005aa504 ["BRANCH", null, ["local:b8:8"]]
+ 005cf1d0 ["BRANCH", null, ["local:b7:8"]]
- 005aa504 bytes 03000014
+ 005cf1d0 bytes 03000014
~~~


<a id="compare-0f18d760ab583c1aed7a26e4de175d94"></a>

### [`005aa770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md) → [`005cf43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md) FUN_005cf43c

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 44.44% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cf4a0",
      "incomplete_value": true,
      "site": "005cf4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa7d4",
      "incomplete_value": true,
      "site": "005aa7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005cf45c"
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
      "unmatched:005aa784",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005aa790",
      "DATA",
      [
        "storage",
        "00bf3898",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf490",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "005cf450",
      "READ",
      [
        "storage",
        "00c9aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf45c",
      "DATA",
      [
        "storage",
        "00c708c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf490",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md#insn-005aa790) · [`005aa7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md#insn-005aa7a0) · [`005aa7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md#insn-005aa7c4)
- 新版 [`005cf46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md#insn-005cf46c) · [`005cf490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf43c.md#insn-005cf490)

~~~diff
- 005aa790 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005aa790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005aa790 bytes 080000f9
- 005aa7a0 ["INT_ADD", "register:40f0:8", ["const:5aa7a0:8", "const:4:8"]]
- 005aa7a0 ["CALL", null, ["callee:00c538e0:8"]]
+ 005cf46c ["INT_ADD", "register:40f0:8", ["const:5cf46c:8", "const:4:8"]]
+ 005cf46c ["CALL", null, ["callee:00c538e0:8"]]
- 005aa7a0 bytes bcb11894
+ 005cf46c bytes 1d111a94
- 005aa7c4 ["INT_ADD", "register:40f0:8", ["const:5aa7c4:8", "const:4:8"]]
- 005aa7c4 ["CALL", null, ["ram:bdb440:8"]]
+ 005cf490 ["INT_ADD", "register:40f0:8", ["const:5cf490:8", "const:4:8"]]
+ 005cf490 ["CALL", null, ["ram:c57e90:8"]]
- 005aa7c4 bytes 1fc31894
+ 005cf490 bytes 80221a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d549dace714195a1eddb6e5d8fe9ddbb"></a>

### [`005aa7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md) → [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) FUN_005cf4c8

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 40.91% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa82c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa82c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005aa820",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aa82c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aa834",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005cf4ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005cf4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "005cf500",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md#insn-005aa820) · [`005aa82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md#insn-005aa82c) · [`005aa834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md#insn-005aa834)

~~~diff
- 005aa820 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005aa820 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005aa820 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005aa820 bytes a8831ff8
- 005aa82c ["COPY", "tmp:0:8", ["const:0:8"]]
- 005aa82c ["COPY", "tmp:1:8", ["const:0:8"]]
- 005aa82c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005aa82c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005aa82c bytes ffff03a9
- 005aa834 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005aa834 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005aa834 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:48:8"]]
- 005aa834 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005aa834 bytes ff230139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c62521e716439107d16b054ef2e5199c"></a>

### [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) → [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) FUN_005cf680

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005aa7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md) [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md) · 呼出先 10件 [`005ab048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md) [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md) [`005ab258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab258.md) [`005ab2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md)
- 新版 呼出元 2件 [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 10件 [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md) [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.03% / 新版 83.03%

CFGの説明率　旧版 34.17% / 新版 36.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 4件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa9e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005aa9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aa9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aa9e8",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005cf6a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "005cf6b0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "005cf6b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md#insn-005aa9dc) · [`005aa9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md#insn-005aa9e4) · [`005aa9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md#insn-005aa9e8)

~~~diff
- 005aa9dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005aa9dc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005aa9dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005aa9dc bytes a8831ff8
- 005aa9e4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005aa9e4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005aa9e4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005aa9e4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005aa9e4 bytes ffff00a9
- 005aa9e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 005aa9e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005aa9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005aa9e8 bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa1828ab4e725c77ae5aaf8ebc35caa"></a>

### [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) → [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) FUN_005cfcbc

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md) [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md) [`005b3380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005d0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md) [`005d804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005cfccc",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ab000",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cfcc8",
      "incomplete_value": false,
      "site": "005cfccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaffc",
      "incomplete_value": false,
      "site": "005ab000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cfcc8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005cfccc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005cfcc8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005cfccc",
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

- 旧版 [`005ab000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md#insn-005ab000) · [`005aaff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md#insn-005aaff8) · [`005aaffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md#insn-005aaffc)
- 新版 [`005cfccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md#insn-005cfccc) · [`005cfcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md#insn-005cfcc4) · [`005cfcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md#insn-005cfcc8)

~~~diff
- 005ab000 ["INT_ADD", "register:40f0:8", ["const:5ab000:8", "const:4:8"]]
- 005ab000 ["CALL", null, ["ram:418c38:8"]]
+ 005cfccc ["INT_ADD", "register:40f0:8", ["const:5cfccc:8", "const:4:8"]]
+ 005cfccc ["CALL", null, ["ram:43b738:8"]]
- 005ab000 bytes 0eb7f997
+ 005cfccc bytes 9baef997
- 005aaff8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005cfcc4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005aaff8 bytes e0e7ffb0
+ 005cfcc4 bytes 40e7ff90
- 005aaffc ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005aaffc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005cfcc8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005cfcc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005cfcc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005cfcc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005aaffc bytes 00740e91
+ 005cfcc8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43e8d4c5672efe0e44d7b345fb591be"></a>

### [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) → [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) FUN_005cfd60

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 6件 [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) [`005ab930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 21.43% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab098"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab094",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab098",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab09c",
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
      "005cfd60",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005cfd64",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005cfd68",
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

- 旧版 [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md#insn-005ab094) · [`005ab098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md#insn-005ab098) · [`005ab09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md#insn-005ab09c)

~~~diff
- 005ab094 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ab094 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ab094 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005ab094 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ab094 bytes fd7bbba9
- 005ab098 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005ab098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005ab098 bytes f90b00f9
- 005ab09c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005ab09c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005ab09c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ab09c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ab09c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c4f8b328df755e92faa0534f69ee55"></a>

### [`005ab2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md) → [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) FUN_005cffac

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005ab4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab4c4.md) [`005ab664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d0190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md) [`005d0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.93% / 新版 83.93%

CFGの説明率　旧版 61.11% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab3d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab340",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab3e4",
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
      "005d000c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005d00b0",
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

- 旧版 [`005ab340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md#insn-005ab340) · [`005ab360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md#insn-005ab360) · [`005ab368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md#insn-005ab368)

~~~diff
- 005ab340 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 005ab340 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 005ab340 bytes ec1300f9
- 005ab360 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005ab360 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005ab360 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 005ab360 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 005ab360 bytes 6981899a
- 005ab368 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005ab368 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005ab368 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005ab368 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005ab368 bytes 3631889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e14a326aa3f8f3fefc06739276150bb1"></a>

### [`005ab5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab5e8.md) → [`005d02b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md) FUN_005d02b4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 61.54% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab62c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d02f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005ab62c"
      ],
      [
        "FALL_THROUGH",
        "005d02f8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005d02f8",
      "incomplete_value": true,
      "site": "005d02fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab62c",
      "incomplete_value": true,
      "site": "005ab630",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab62c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d02d0"
      ]
    ]
  ],
  "added": [
    [
      "005d02f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d02d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab5e8.md#insn-005ab62c) · [`005ab60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab5e8.md#insn-005ab60c)
- 新版 [`005d02f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md#insn-005d02f8) · [`005d02d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d02b4.md#insn-005d02d8)

~~~diff
- 005ab62c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005ab62c ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 005ab62c bytes c0feffb4
+ 005d02f8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 005d02f8 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
+ 005d02f8 bytes c0feffb4
- 005ab60c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 005d02d8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005ab60c bytes 80010054
+ 005d02d8 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82b89019967dc56f7a691d2fcdd0f0df"></a>

### [`005ab678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md) → [`005d0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0344.md) FUN_005d0344

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 57.14% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab67c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab678",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab67c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab680",
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
      "005d0344",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005d0348",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d034c",
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

- 旧版 [`005ab678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md#insn-005ab678) · [`005ab67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md#insn-005ab67c) · [`005ab680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md#insn-005ab680)

~~~diff
- 005ab678 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ab678 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ab678 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005ab678 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ab678 bytes fd7bbca9
- 005ab67c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005ab67c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005ab67c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ab67c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ab67c bytes f85f01a9
- 005ab680 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ab680 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ab680 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ab680 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ab680 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a9f59ee9aa0c22ec5a6cc82f91afa21"></a>

### [`005ab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md) → [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) FUN_005d04d0

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005ab930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 3件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 15.38% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab804",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab808",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab80c",
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
      "005d04d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005d04d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005d04d8",
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

- 旧版 [`005ab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md#insn-005ab804) · [`005ab808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md#insn-005ab808) · [`005ab80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md#insn-005ab80c)

~~~diff
- 005ab804 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ab804 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ab804 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005ab804 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ab804 bytes fd7bbba9
- 005ab808 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005ab808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005ab808 bytes f90b00f9
- 005ab80c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005ab80c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005ab80c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ab80c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ab80c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f46fb3dab6c2e8243fed179c945bae"></a>

### [`005ab930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md) → [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) FUN_005d05fc

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md) [`005b356c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) [`005d8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d060c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ab940",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0608",
      "incomplete_value": false,
      "site": "005d060c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab93c",
      "incomplete_value": false,
      "site": "005ab940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0608",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005d060c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d0608",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d060c",
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

- 旧版 [`005ab940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md#insn-005ab940) · [`005ab938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md#insn-005ab938) · [`005ab93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md#insn-005ab93c)
- 新版 [`005d060c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md#insn-005d060c) · [`005d0604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md#insn-005d0604) · [`005d0608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md#insn-005d0608)

~~~diff
- 005ab940 ["INT_ADD", "register:40f0:8", ["const:5ab940:8", "const:4:8"]]
- 005ab940 ["CALL", null, ["ram:418c38:8"]]
+ 005d060c ["INT_ADD", "register:40f0:8", ["const:5d060c:8", "const:4:8"]]
+ 005d060c ["CALL", null, ["ram:43b738:8"]]
- 005ab940 bytes beb4f997
+ 005d060c bytes 4bacf997
- 005ab938 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005d0604 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005ab938 bytes e0e7ff90
+ 005d0604 bytes 20e7fff0
- 005ab93c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005ab93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d0608 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005d0608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005ab93c bytes 00740e91
+ 005d0608 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ecf31b8ad29b29167e17d26540faa6"></a>

### [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) → [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) FUN_005d0610

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005b093c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b093c.md) [`005b0d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0d5c.md) · 呼出先 7件 [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005acbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md) [`005adeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 3件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d5608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5608.md) [`005d5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5a28.md) · 呼出先 7件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.41% / 新版 89.41%

CFGの説明率　旧版 46.88% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab944",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab948",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab94c",
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
      "005d0610",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005d0614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d0618",
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

- 旧版 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md#insn-005ab944) · [`005ab948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md#insn-005ab948) · [`005ab94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md#insn-005ab94c)

~~~diff
- 005ab944 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ab944 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ab944 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005ab944 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ab944 bytes fd7bbca9
- 005ab948 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005ab948 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005ab948 bytes f70b00f9
- 005ab94c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ab94c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ab94c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ab94c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ab94c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8971efe47f0e2eb1a8f004fb32b8a454"></a>

### [`005abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md) → [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md) FUN_005d07b0

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) · 呼出先 1件 [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md)
- 新版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 1件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005abaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md#insn-005abaf8) · [`005abb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md#insn-005abb08) · [`005abb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md#insn-005abb24)
- 新版 [`005d07c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md#insn-005d07c4) · [`005d07d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md#insn-005d07d4) · [`005d07f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md#insn-005d07f0)

~~~diff
- 005abaf8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 005d07c4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 005abaf8 bytes 20020054
+ 005d07c4 bytes 20020054
- 005abb08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005abb08 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005abb08 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 005d07d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005d07d4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 005d07d4 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 005abb08 bytes 08010054
+ 005d07d4 bytes 08010054
- 005abb24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005abb24 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005d07f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005d07f0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005abb24 bytes c1000054
+ 005d07f0 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad5f17803685f9674f2fd58d744d910"></a>

### [`005abbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md) → [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) FUN_005d08ac

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) · 呼出先 3件 [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md)
- 新版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 3件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d0970",
      "value": [
        "leaf",
        "ram:5d0fb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005abca4",
      "value": [
        "leaf",
        "ram:5ac2ec:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ac2ec"
      ]
    ]
  ],
  "added": [
    [
      "005d0970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d0fb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md#insn-005abca4) · [`005abc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md#insn-005abc04) · [`005abc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md#insn-005abc90)
- 新版 [`005d0970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d0970) · [`005d08d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d08d0) · [`005d095c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md#insn-005d095c)

~~~diff
- 005abca4 ["INT_ADD", "register:40f0:8", ["const:5abca4:8", "const:4:8"]]
- 005abca4 ["CALL", null, ["ram:5ac2ec:8"]]
+ 005d0970 ["INT_ADD", "register:40f0:8", ["const:5d0970:8", "const:4:8"]]
+ 005d0970 ["CALL", null, ["ram:5d0fb8:8"]]
- 005abca4 bytes 92010094
+ 005d0970 bytes 92010094
- 005abc04 ["INT_ADD", "register:40f0:8", ["const:5abc04:8", "const:4:8"]]
- 005abc04 ["CALL", null, ["callee:005d0e78:8"]]
+ 005d08d0 ["INT_ADD", "register:40f0:8", ["const:5d08d0:8", "const:4:8"]]
+ 005d08d0 ["CALL", null, ["callee:005d0e78:8"]]
- 005abc04 bytes 6a010094
+ 005d08d0 bytes 6a010094
- 005abc90 ["INT_ADD", "register:40f0:8", ["const:5abc90:8", "const:4:8"]]
- 005abc90 ["CALL", null, ["callee:005d1004:8"]]
+ 005d095c ["INT_ADD", "register:40f0:8", ["const:5d095c:8", "const:4:8"]]
+ 005d095c ["CALL", null, ["callee:005d1004:8"]]
- 005abc90 bytes aa010094
+ 005d095c bytes aa010094
~~~


<a id="compare-834d5e39a201a424ddfdd0be31807f13"></a>

### [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) → [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) FUN_005d0e78

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md) [`005abbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md) [`005abeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) [`005ae894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md) [`005b093c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b093c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 7件 [`005d07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d07b0.md) [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) [`005d5608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5608.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.94% / 新版 60.94%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac1e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac1f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac1f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0e94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005ac1fc"
      ]
    ],
    [
      "unmatched:005ac1e0",
      "READ",
      [
        "storage",
        "00c1b608",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005ac1f0",
      "DATA",
      [
        "storage",
        "00bf39b8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d0e94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0ec8"
      ]
    ],
    [
      "005d0eac",
      "READ",
      [
        "storage",
        "00c9b000",
        null,
        "pointer"
      ]
    ],
    [
      "005d0ebc",
      "DATA",
      [
        "storage",
        "00c709e0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac1e4) · [`005ac1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac1f0) · [`005ac1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac1f4)

~~~diff
- 005ac1e4 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 005ac1e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:10:8"]]
- 005ac1e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 005ac1e4 bytes 14400039
- 005ac1f0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005ac1f0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 005ac1f0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005ac1f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ac1f0 bytes 092800a9
- 005ac1f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 005ac1f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005ac1f4 bytes 000500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a37effe9ac479f6dc558fb718a94126"></a>

### [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md) → [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md) FUN_005d1004

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005abbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) [`005b0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 3件 [`005d08ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d08ac.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 62.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d1048",
      "incomplete_value": true,
      "site": "005d1048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac37c",
      "incomplete_value": true,
      "site": "005ac37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac3c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d1038",
      "READ",
      [
        "storage",
        "00c1b620",
        null,
        "pointer"
      ]
    ],
    [
      "005d1048",
      "DATA",
      [
        "storage",
        "00bf3a90",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1068",
      "READ",
      [
        "storage",
        "00c1b628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1038",
      "READ",
      [
        "storage",
        "00c9b018",
        null,
        "pointer"
      ]
    ],
    [
      "005d1048",
      "DATA",
      [
        "storage",
        "00c70ab8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1068",
      "READ",
      [
        "storage",
        "00c9b020",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md#insn-005ac3c8) · [`005ac3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md#insn-005ac3cc)
- 新版 [`005d1098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md#insn-005d1098) · [`005d1094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md#insn-005d1094)

~~~diff
- 005ac3c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005ac3c8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005ac3c8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005ac3c8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005ac3c8 bytes 092081a8
- 005ac3cc ["INT_ADD", "register:40f0:8", ["const:5ac3cc:8", "const:4:8"]]
- 005ac3cc ["CALL", null, ["callee:00c5a3d0:8"]]
+ 005d1098 ["INT_ADD", "register:40f0:8", ["const:5d1098:8", "const:4:8"]]
+ 005d1098 ["CALL", null, ["callee:00c5a3d0:8"]]
- 005ac3cc bytes 6dc51894
+ 005d1098 bytes ce241a94
+ 005d1094 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005d1094 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 005d1094 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005d1094 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 005d1094 bytes 092081a8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c4dc1a9ee35e487e78d36535337ac49"></a>

### [`005ac5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac5e0.md) → [`005d12ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d12ac.md) FUN_005d12ac

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac5f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d12c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005ac5f8"
      ],
      [
        "FALL_THROUGH",
        "005d12c4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005d12c4",
      "incomplete_value": true,
      "site": "005d12d4",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac5f8",
      "incomplete_value": true,
      "site": "005ac608",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ac5f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12e4"
      ]
    ]
  ],
  "added": [
    [
      "005d12c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac5e0.md#insn-005ac5f8) · [`005ac5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac5e0.md#insn-005ac5e8)
- 新版 [`005d12c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d12ac.md#insn-005d12c4) · [`005d12b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d12ac.md#insn-005d12b4)

~~~diff
- 005ac5f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005ac5f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005ac5f8 bytes 01010054
+ 005d12c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005d12c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005d12c4 bytes 01010054
- 005ac5e8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 005d12b4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 005ac5e8 bytes 80010054
+ 005d12b4 bytes 80010054
~~~


<a id="compare-f8421502935afa42332333569fdd53d9"></a>

### [`005ac990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac990.md) → [`005d165c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d165c.md) FUN_005d165c

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d1668",
      "incomplete_value": true,
      "site": "005d166c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac99c",
      "incomplete_value": true,
      "site": "005ac9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac9c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005d1690"
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
      "005d1660",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d166c",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005ac9c4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005d1660",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005d166c",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1690",
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

- 旧版 [`005ac9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac990.md#insn-005ac9c4) · [`005ac990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac990.md#insn-005ac990)
- 新版 [`005d1690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d165c.md#insn-005d1690) · [`005d165c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d165c.md#insn-005d165c)

~~~diff
- 005ac9c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ac9c4 ["INT_ADD", "register:40f0:8", ["const:5ac9c4:8", "const:4:8"]]
- 005ac9c4 ["CALLIND", null, ["register:0:8"]]
- 005ac9c4 bytes 20013fd6
+ 005d1690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d1690 ["INT_ADD", "register:40f0:8", ["const:5d1690:8", "const:4:8"]]
+ 005d1690 ["CALLIND", null, ["register:0:8"]]
+ 005d1690 bytes 20013fd6
- 005ac990 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005d165c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005ac990 bytes 693300f0
+ 005d165c bytes 493600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48898e366cb00a3171acb12a13e87ad4"></a>

### [`005ac9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac9d8.md) → [`005d16a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d16a4.md) FUN_005d16a4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 11.76% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac9dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ac9d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ac9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ac9e0",
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
      "005d16a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d16a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d16ac",
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

- 旧版 [`005ac9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac9d8.md#insn-005ac9d8) · [`005ac9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac9d8.md#insn-005ac9dc) · [`005ac9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac9d8.md#insn-005ac9e0)

~~~diff
- 005ac9d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ac9d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ac9d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005ac9d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ac9d8 bytes fd7bbda9
- 005ac9dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ac9dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ac9dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ac9dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ac9dc bytes f65701a9
- 005ac9e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005ac9e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005ac9e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ac9e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ac9e0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636450ebdcdf0c02762502f60e693062"></a>

### [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) → [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) FUN_005d1764

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md) [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md) · 呼出先 4件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 4件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005acad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005acae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d179c"
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
      "unmatched:005acad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d17c0"
      ]
    ],
    [
      "unmatched:005acae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d180c"
      ]
    ]
  ],
  "added": [
    [
      "005d179c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d17c0"
      ]
    ],
    [
      "005d17b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d180c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md#insn-005acad0) · [`005acae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md#insn-005acae8)
- 新版 [`005d179c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md#insn-005d179c)

~~~diff
- 005acad0 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 005acad0 bytes 22010054
- 005acae8 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 005acae8 bytes c2020054
+ 005d179c ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
+ 005d179c bytes 22010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5981dd4b6f272507fd6479b919b4a4b5"></a>

### [`005acbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md) → [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) FUN_005d18c0

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00bdd9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9a0.md)
- 新版 呼出元 2件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.33% / 新版 61.33%

CFGの説明率　旧版 7.14% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acc08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acc08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acc34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005acc08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005acc20",
      "READ",
      [
        "storage",
        "00c1b638",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005acc34",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005d18d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d18ec",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "005d1900",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md#insn-005acc08) · [`005acc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md#insn-005acc34) · [`005acc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md#insn-005acc3c)

~~~diff
- 005acc08 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005acc08 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005acc08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005acc08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005acc08 bytes f44f07a9
- 005acc34 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005acc34 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005acc34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005acc34 bytes a8831ff8
- 005acc3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005acc3c ["COPY", "tmp:1:8", ["register:4010:8"]]
- 005acc3c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005acc3c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005acc3c bytes 080881a8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e03a64bded453f10a09aba1688515439"></a>

### [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) → [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) FUN_005d2bc4

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) · 呼出先 14件 [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005adeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md) [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md)
- 新版 呼出元 1件 [`005d0610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0610.md) · 呼出先 14件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 66.67% / 新版 69.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae37c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ae0e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2ddc"
      ]
    ],
    [
      "unmatched:005ae2e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2f88"
      ]
    ],
    [
      "unmatched:005ae310",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005adeac"
      ]
    ]
  ],
  "added": [
    [
      "005d2db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2ddc"
      ]
    ],
    [
      "005d2fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2f88"
      ]
    ],
    [
      "005d2fdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d2b78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md#insn-005ae0e8) · [`005ae2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md#insn-005ae2e8) · [`005ae310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md#insn-005ae310)

~~~diff
- 005ae0e8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 005ae0e8 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 005ae0e8 bytes 490100b4
- 005ae2e8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 005ae2e8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 005ae2e8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 005ae2e8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 005ae2e8 bytes a8fe0736
- 005ae310 ["INT_ADD", "register:40f0:8", ["const:5ae310:8", "const:4:8"]]
- 005ae310 ["CALL", null, ["ram:5adeac:8"]]
- 005ae310 bytes e7feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-102b791084c40b09a603d6360e60f404"></a>

### [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) → [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) FUN_005d3094

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005adeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) [`005aef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md)
- 新版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 83.33% / 新版 86.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d3208",
      "incomplete_value": true,
      "site": "005d3214",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4048:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d320c",
      "incomplete_value": true,
      "site": "005d3214",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4040:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae5d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ae5d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005adeac"
      ]
    ],
    [
      "unmatched:005ae5e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005af158"
      ]
    ],
    [
      "unmatched:005ae5f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005af158"
      ]
    ]
  ],
  "added": [
    [
      "005d329c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d2b78"
      ]
    ],
    [
      "005d32b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d3e24"
      ]
    ],
    [
      "005d32c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d3e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md#insn-005ae548) · [`005ae5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md#insn-005ae5d0) · [`005ae5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md#insn-005ae5e4)
- 新版 [`005d3214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md#insn-005d3214)

~~~diff
- 005ae548 ["INT_ADD", "register:40f0:8", ["const:5ae548:8", "const:4:8"]]
- 005ae548 ["CALL", null, ["callee:005d3c18:8"]]
+ 005d3214 ["INT_ADD", "register:40f0:8", ["const:5d3214:8", "const:4:8"]]
+ 005d3214 ["CALL", null, ["callee:005d3c18:8"]]
- 005ae548 bytes 81020094
+ 005d3214 bytes 81020094
- 005ae5d0 ["INT_ADD", "register:40f0:8", ["const:5ae5d0:8", "const:4:8"]]
- 005ae5d0 ["CALL", null, ["ram:5adeac:8"]]
- 005ae5d0 bytes 37feff97
- 005ae5e4 ["INT_ADD", "register:40f0:8", ["const:5ae5e4:8", "const:4:8"]]
- 005ae5e4 ["CALL", null, ["ram:5af158:8"]]
- 005ae5e4 bytes dd020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e815c85f94f6ec6d9bdaee0c19888d6"></a>

### [`005ae654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md) → [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) FUN_005d3320

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 5件 [`005adeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) [`005af158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af158.md) [`005af1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 5件 [`005d2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2b78.md) [`005d3e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e24.md) [`005d3e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d3420",
      "value": [
        "leaf",
        "ram:5d2b78:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ae754",
      "value": [
        "leaf",
        "ram:5adeac:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d3434",
      "value": [
        "leaf",
        "ram:5d3e24:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005ae768",
      "value": [
        "leaf",
        "ram:5af158:8"
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
      "005d3420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005adeac"
      ]
    ],
    [
      "005d3434",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005af158"
      ]
    ]
  ],
  "added": [
    [
      "005d3420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d2b78"
      ]
    ],
    [
      "005d3434",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d3e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md#insn-005ae754) · [`005ae768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md#insn-005ae768) · [`005ae6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md#insn-005ae6d4)
- 新版 [`005d3420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d3420) · [`005d3434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d3434) · [`005d33a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md#insn-005d33a0)

~~~diff
- 005ae754 ["INT_ADD", "register:40f0:8", ["const:5ae754:8", "const:4:8"]]
- 005ae754 ["CALL", null, ["ram:5adeac:8"]]
+ 005d3420 ["INT_ADD", "register:40f0:8", ["const:5d3420:8", "const:4:8"]]
+ 005d3420 ["CALL", null, ["ram:5d2b78:8"]]
- 005ae754 bytes d6fdff97
+ 005d3420 bytes d6fdff97
- 005ae768 ["INT_ADD", "register:40f0:8", ["const:5ae768:8", "const:4:8"]]
- 005ae768 ["CALL", null, ["ram:5af158:8"]]
+ 005d3434 ["INT_ADD", "register:40f0:8", ["const:5d3434:8", "const:4:8"]]
+ 005d3434 ["CALL", null, ["ram:5d3e24:8"]]
- 005ae768 bytes 7c020094
+ 005d3434 bytes 7c020094
- 005ae6d4 ["INT_ADD", "register:40f0:8", ["const:5ae6d4:8", "const:4:8"]]
- 005ae6d4 ["CALL", null, ["callee:005d3e70:8"]]
+ 005d33a0 ["INT_ADD", "register:40f0:8", ["const:5d33a0:8", "const:4:8"]]
+ 005d33a0 ["CALL", null, ["callee:005d3e70:8"]]
- 005ae6d4 bytes b4020094
+ 005d33a0 bytes b4020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12dd913f3d146856ae71db41c726d394"></a>

### [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md) → [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) FUN_005d343c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 5件 [`005abb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md) [`005abeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005af810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md) [`00bdd990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 5件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 72.22% / 新版 78.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d34bc",
      "incomplete_value": true,
      "site": "005d34cc",
      "value": [
        "live",
        "register:4020:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d34c0",
      "incomplete_value": false,
      "site": "005d34cc",
      "value": [
        "leaf",
        "const:5f:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d344c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005ae890"
      ]
    ],
    [
      "unmatched:005ae890",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005abb94"
      ]
    ]
  ],
  "added": [
    [
      "005d344c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d355c"
      ]
    ],
    [
      "005d355c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d0860"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md#insn-005ae800) · [`005ae890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md#insn-005ae890)
- 新版 [`005d34cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md#insn-005d34cc) · [`005d355c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md#insn-005d355c)

~~~diff
- 005ae800 ["INT_ADD", "register:40f0:8", ["const:5ae800:8", "const:4:8"]]
- 005ae800 ["CALL", null, ["callee:005d44dc:8"]]
+ 005d34cc ["INT_ADD", "register:40f0:8", ["const:5d34cc:8", "const:4:8"]]
+ 005d34cc ["CALL", null, ["callee:005d44dc:8"]]
- 005ae800 bytes 04040094
+ 005d34cc bytes 04040094
- 005ae890 ["INT_ADD", "register:40f0:8", ["const:5ae890:8", "const:4:8"]]
- 005ae890 ["CALL", null, ["ram:5abb94:8"]]
- 005ae890 bytes c1f4ff97
+ 005d355c ["INT_ADD", "register:40f0:8", ["const:5d355c:8", "const:4:8"]]
+ 005d355c ["CALL", null, ["ram:5d0860:8"]]
+ 005d355c bytes c1f4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a76a1dac11dff1dcdb8c41cbbf9696"></a>

### [`005ae894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md) → [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) FUN_005d3560

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) [`005b0e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0e84.md) · 呼出先 3件 [`005abb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md) [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) [`00bdd990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd990.md)
- 新版 呼出元 2件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) · 呼出先 3件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 80.23% / 新版 84.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ae9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d36a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d371c",
      "incomplete_value": true,
      "site": "005d3720",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d3570",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005aea78"
      ]
    ],
    [
      "005d3670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005aea78"
      ]
    ],
    [
      "unmatched:005ae9dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d3728"
      ]
    ]
  ],
  "added": [
    [
      "005d3570",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d3744"
      ]
    ],
    [
      "005d3670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d3744"
      ]
    ],
    [
      "005d36a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d3728"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md#insn-005ae9dc) · [`005aea54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md#insn-005aea54) · [`005aea78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md#insn-005aea78)
- 新版 [`005d3720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md#insn-005d3720)

~~~diff
- 005ae9dc ["CBRANCH", null, ["local:b53:8", "register:101:1"]]
- 005ae9dc bytes 00040054
- 005aea54 ["INT_ADD", "register:40f0:8", ["const:5aea54:8", "const:4:8"]]
- 005aea54 ["CALL", null, ["callee:00c5a3e0:8"]]
+ 005d3720 ["INT_ADD", "register:40f0:8", ["const:5d3720:8", "const:4:8"]]
+ 005d3720 ["CALL", null, ["callee:00c5a3e0:8"]]
- 005aea54 bytes cfbb1894
+ 005d3720 bytes 301b1a94
- 005aea78 ["INT_ADD", "register:40f0:8", ["const:5aea78:8", "const:4:8"]]
- 005aea78 ["CALL", null, ["ram:5abb94:8"]]
- 005aea78 bytes 47f4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-023280b01c10483aca5ea4262acdb568"></a>

### [`005aea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md) → [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) FUN_005d3748

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 7件 [`004c9380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9380.md) [`005af96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af96c.md) [`005afb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb30.md) [`005afb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 7件 [`004ec218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec218.md) [`005d4638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md) [`005d47fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d47fc.md) [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.17% / 新版 70.17%

CFGの説明率　旧版 28.57% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 32件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aea80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aea80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aea84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005aea80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aea84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aea88",
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
      "005d374c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005d3750",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d3754",
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

- 旧版 [`005aea80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md#insn-005aea80) · [`005aea84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md#insn-005aea84) · [`005aea88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md#insn-005aea88)

~~~diff
- 005aea80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005aea80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005aea80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005aea80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005aea80 bytes fd7b07a9
- 005aea84 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005aea84 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005aea84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 005aea84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005aea84 bytes f85f08a9
- 005aea88 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005aea88 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005aea88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 005aea88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005aea88 bytes f65709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e604e37c600853fe38f29e766bb5a6"></a>

### [`005aef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md) → [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md) FUN_005d3c18

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005afd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 93.33% / 新版 95.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005aef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md#insn-005aef70) · [`005aef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md#insn-005aef80) · [`005aef9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md#insn-005aef9c)
- 新版 [`005d3c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3c3c) · [`005d3c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3c4c) · [`005d3c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md#insn-005d3c68)

~~~diff
- 005aef70 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 005aef70 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005d3c3c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 005d3c3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005aef70 bytes 68020034
+ 005d3c3c bytes 68020034
- 005aef80 ["COPY", "register:0:8", ["register:4040:8"]]
- 005aef80 ["INT_ADD", "register:40f0:8", ["const:5aef80:8", "const:4:8"]]
- 005aef80 ["CALLIND", null, ["register:0:8"]]
+ 005d3c4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d3c4c ["INT_ADD", "register:40f0:8", ["const:5d3c4c:8", "const:4:8"]]
+ 005d3c4c ["CALLIND", null, ["register:0:8"]]
- 005aef80 bytes 00013fd6
+ 005d3c4c bytes 00013fd6
- 005aef9c ["COPY", "register:0:8", ["register:4048:8"]]
- 005aef9c ["INT_ADD", "register:40f0:8", ["const:5aef9c:8", "const:4:8"]]
- 005aef9c ["CALLIND", null, ["register:0:8"]]
+ 005d3c68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d3c68 ["INT_ADD", "register:40f0:8", ["const:5d3c68:8", "const:4:8"]]
+ 005d3c68 ["CALLIND", null, ["register:0:8"]]
- 005aef9c bytes 20013fd6
+ 005d3c68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-056325d99d46642563eb9f8ce80dc0ed"></a>

### [`005afd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md) → [`005d49e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md) FUN_005d49e8

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005afb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d49f8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005afd2c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d49f4",
      "incomplete_value": false,
      "site": "005d49f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afd28",
      "incomplete_value": false,
      "site": "005afd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d49f4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005d49f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d49f4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d49f8",
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

- 旧版 [`005afd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md#insn-005afd2c) · [`005afd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md#insn-005afd24) · [`005afd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md#insn-005afd28)
- 新版 [`005d49f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md#insn-005d49f8) · [`005d49f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md#insn-005d49f0) · [`005d49f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md#insn-005d49f4)

~~~diff
- 005afd2c ["INT_ADD", "register:40f0:8", ["const:5afd2c:8", "const:4:8"]]
- 005afd2c ["CALL", null, ["ram:418c38:8"]]
+ 005d49f8 ["INT_ADD", "register:40f0:8", ["const:5d49f8:8", "const:4:8"]]
+ 005d49f8 ["CALL", null, ["ram:43b738:8"]]
- 005afd2c bytes c3a3f997
+ 005d49f8 bytes 509bf997
- 005afd24 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005d49f0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005afd24 bytes c0e7ff90
+ 005d49f0 bytes 00e7fff0
- 005afd28 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005afd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d49f4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005d49f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d49f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d49f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd28 bytes 00740e91
+ 005d49f4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636123417f1059be92d0bacf93a44bc6"></a>

### [`005afd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md) → [`005d49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md) FUN_005d49fc

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005aef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005d3c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3c18.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d4a0c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005afd40",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4a08",
      "incomplete_value": false,
      "site": "005d4a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afd3c",
      "incomplete_value": false,
      "site": "005afd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4a08",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005d4a0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d4a08",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d4a0c",
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

- 旧版 [`005afd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md#insn-005afd40) · [`005afd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md#insn-005afd38) · [`005afd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md#insn-005afd3c)
- 新版 [`005d4a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md#insn-005d4a0c) · [`005d4a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md#insn-005d4a04) · [`005d4a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49fc.md#insn-005d4a08)

~~~diff
- 005afd40 ["INT_ADD", "register:40f0:8", ["const:5afd40:8", "const:4:8"]]
- 005afd40 ["CALL", null, ["ram:418c38:8"]]
+ 005d4a0c ["INT_ADD", "register:40f0:8", ["const:5d4a0c:8", "const:4:8"]]
+ 005d4a0c ["CALL", null, ["ram:43b738:8"]]
- 005afd40 bytes bea3f997
+ 005d4a0c bytes 4b9bf997
- 005afd38 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005d4a04 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005afd38 bytes c0e7ff90
+ 005d4a04 bytes 00e7fff0
- 005afd3c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005afd3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d4a08 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005d4a08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4a08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd3c bytes 00740e91
+ 005d4a08 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e23f068d40065b778fbf50858af1de"></a>

### [`005afe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md) → [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) FUN_005d4b08

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.16% / 新版 90.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4b60",
      "incomplete_value": true,
      "site": "005d4b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afe94",
      "incomplete_value": true,
      "site": "005afe94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4b94",
      "incomplete_value": true,
      "site": "005d4b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afec8",
      "incomplete_value": true,
      "site": "005afec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4bc4",
      "incomplete_value": true,
      "site": "005d4bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afef8",
      "incomplete_value": true,
      "site": "005aff00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4b54",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005d4b60",
      "DATA",
      [
        "storage",
        "00bf3718",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4b7c",
      "READ",
      [
        "storage",
        "00c1b640",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4b54",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ],
    [
      "005d4b60",
      "DATA",
      [
        "storage",
        "00c70740",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4b7c",
      "READ",
      [
        "storage",
        "00c9b038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afe78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afe78) · [`005afe80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afe80) · [`005afe88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afe88)
- 新版 [`005d4b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b44) · [`005d4b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b4c) · [`005d4b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md#insn-005d4b54)

~~~diff
- 005afe78 ["INT_ADD", "register:40f0:8", ["const:5afe78:8", "const:4:8"]]
- 005afe78 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d4b44 ["INT_ADD", "register:40f0:8", ["const:5d4b44:8", "const:4:8"]]
+ 005d4b44 ["CALL", null, ["callee:00c57a90:8"]]
- 005afe78 bytes 72ac1894
+ 005d4b44 bytes d30b1a94
- 005afe80 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005d4b4c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005afe80 bytes 69330090
+ 005d4b4c bytes 293600d0
- 005afe88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:590:8"]]
- 005afe88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4b54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f88:8"]]
+ 005d4b54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005afe88 bytes 29c942f9
+ 005d4b54 bytes 29c547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9235b3174c719e3cb30af3741a23315"></a>

### [`005b0014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md) → [`005d4ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md) FUN_005d4ce0

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4cfc",
      "incomplete_value": true,
      "site": "005d4d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0030",
      "incomplete_value": true,
      "site": "005b0034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4d20",
      "incomplete_value": true,
      "site": "005d4d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0054",
      "incomplete_value": true,
      "site": "005b0058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4cf4",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d00",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4d18",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4cf4",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d4d00",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4d18",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md#insn-005b0020) · [`005b0028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md#insn-005b0028) · [`005b0044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md#insn-005b0044)
- 新版 [`005d4cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4cec) · [`005d4cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4cf4) · [`005d4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4ce0.md#insn-005d4d10)

~~~diff
- 005b0020 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005d4cec ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005b0020 bytes 483300f0
+ 005d4cec bytes 283600f0
- 005b0028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
- 005b0028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
+ 005d4cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0028 bytes 082943f9
+ 005d4cf4 bytes 082540f9
- 005b0044 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b0044 ["INT_ADD", "register:40f0:8", ["const:5b0044:8", "const:4:8"]]
- 005b0044 ["CALLIND", null, ["register:0:8"]]
+ 005d4d10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d4d10 ["INT_ADD", "register:40f0:8", ["const:5d4d10:8", "const:4:8"]]
+ 005d4d10 ["CALLIND", null, ["register:0:8"]]
- 005b0044 bytes 00013fd6
+ 005d4d10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4664352248822fe423ab1cc8a9037db"></a>

### [`005b0304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md) → [`005d4fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md) FUN_005d4fd0

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d4fec",
      "incomplete_value": true,
      "site": "005d4ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0320",
      "incomplete_value": true,
      "site": "005b0324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d5010",
      "incomplete_value": true,
      "site": "005d5014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0344",
      "incomplete_value": true,
      "site": "005b0348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4fe4",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005d4ff0",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5008",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4fe4",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d4ff0",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5008",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md#insn-005b0310) · [`005b0318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md#insn-005b0318) · [`005b0334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md#insn-005b0334)
- 新版 [`005d4fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d4fdc) · [`005d4fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d4fe4) · [`005d5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4fd0.md#insn-005d5000)

~~~diff
- 005b0310 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005d4fdc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005b0310 bytes 483300f0
+ 005d4fdc bytes 283600f0
- 005b0318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
- 005b0318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4fe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
+ 005d4fe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0318 bytes 082943f9
+ 005d4fe4 bytes 082540f9
- 005b0334 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b0334 ["INT_ADD", "register:40f0:8", ["const:5b0334:8", "const:4:8"]]
- 005b0334 ["CALLIND", null, ["register:0:8"]]
+ 005d5000 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d5000 ["INT_ADD", "register:40f0:8", ["const:5d5000:8", "const:4:8"]]
+ 005d5000 ["CALLIND", null, ["register:0:8"]]
- 005b0334 bytes 00013fd6
+ 005d5000 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c6e5114a5f64f2d17ac1cab17dd635"></a>

### [`005b0384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md) → [`005d5050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md) FUN_005d5050

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d506c",
      "incomplete_value": true,
      "site": "005d5070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b03a0",
      "incomplete_value": true,
      "site": "005b03a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d5090",
      "incomplete_value": true,
      "site": "005d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b03c4",
      "incomplete_value": true,
      "site": "005b03c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d5064",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005d5070",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5088",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5064",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d5070",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5088",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md#insn-005b0390) · [`005b0398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md#insn-005b0398) · [`005b03b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md#insn-005b03b4)
- 新版 [`005d505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d505c) · [`005d5064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d5064) · [`005d5080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5050.md#insn-005d5080)

~~~diff
- 005b0390 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005d505c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005b0390 bytes 483300f0
+ 005d505c bytes 283600d0
- 005b0398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
- 005b0398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5064 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
+ 005d5064 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0398 bytes 082943f9
+ 005d5064 bytes 082540f9
- 005b03b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b03b4 ["INT_ADD", "register:40f0:8", ["const:5b03b4:8", "const:4:8"]]
- 005b03b4 ["CALLIND", null, ["register:0:8"]]
+ 005d5080 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d5080 ["INT_ADD", "register:40f0:8", ["const:5d5080:8", "const:4:8"]]
+ 005d5080 ["CALLIND", null, ["register:0:8"]]
- 005b03b4 bytes 00013fd6
+ 005d5080 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef648396fe913a0ba304012018e30053"></a>

### [`005b03f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md) → [`005d50bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md) FUN_005d50bc

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d50d8",
      "incomplete_value": true,
      "site": "005d50dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b040c",
      "incomplete_value": true,
      "site": "005b0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d50fc",
      "incomplete_value": true,
      "site": "005d5100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0430",
      "incomplete_value": true,
      "site": "005b0434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d50d0",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005d50dc",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d50f4",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d50d0",
      "READ",
      [
        "storage",
        "00c9b048",
        null,
        "pointer"
      ]
    ],
    [
      "005d50dc",
      "DATA",
      [
        "storage",
        "00c70c38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d50f4",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b03fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md#insn-005b03fc) · [`005b0404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md#insn-005b0404) · [`005b0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md#insn-005b0420)
- 新版 [`005d50c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50c8) · [`005d50d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50d0) · [`005d50ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d50bc.md#insn-005d50ec)

~~~diff
- 005b03fc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005d50c8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005b03fc bytes 483300f0
+ 005d50c8 bytes 283600d0
- 005b0404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
- 005b0404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d50d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:48:8"]]
+ 005d50d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0404 bytes 082943f9
+ 005d50d0 bytes 082540f9
- 005b0420 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b0420 ["INT_ADD", "register:40f0:8", ["const:5b0420:8", "const:4:8"]]
- 005b0420 ["CALLIND", null, ["register:0:8"]]
+ 005d50ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d50ec ["INT_ADD", "register:40f0:8", ["const:5d50ec:8", "const:4:8"]]
+ 005d50ec ["CALLIND", null, ["register:0:8"]]
- 005b0420 bytes 00013fd6
+ 005d50ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83ca83ecee92b1f1e9f9133511bbfc20"></a>

### [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) → [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) FUN_005d51bc

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) · 呼出先 7件 [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md)
- 新版 呼出元 2件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) · 呼出先 7件 [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.89% / 新版 93.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d524c",
      "incomplete_value": true,
      "site": "005d5264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0580",
      "incomplete_value": true,
      "site": "005b0598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d53a0",
      "incomplete_value": true,
      "site": "005d53b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b06d4",
      "incomplete_value": true,
      "site": "005b06e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d53c0",
      "value": [
        "leaf",
        "ram:5cf05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b06f4",
      "value": [
        "leaf",
        "ram:5aa390:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d523c",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "005d5264",
      "DATA",
      [
        "storage",
        "00bf3b20",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5390",
      "READ",
      [
        "storage",
        "00c1b5f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d523c",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "005d5264",
      "DATA",
      [
        "storage",
        "00c70b48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5390",
      "READ",
      [
        "storage",
        "00c9aff0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b06f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md#insn-005b06f4) · [`005b06f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md#insn-005b06f8) · [`005b0510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md#insn-005b0510)
- 新版 [`005d53c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d53c0) · [`005d53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d53c4) · [`005d51dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md#insn-005d51dc)

~~~diff
- 005b06f4 ["INT_ADD", "register:40f0:8", ["const:5b06f4:8", "const:4:8"]]
- 005b06f4 ["CALL", null, ["ram:5aa390:8"]]
+ 005d53c0 ["INT_ADD", "register:40f0:8", ["const:5d53c0:8", "const:4:8"]]
+ 005d53c0 ["CALL", null, ["ram:5cf05c:8"]]
- 005b06f4 bytes 27e7ff97
+ 005d53c0 bytes 27e7ff97
- 005b06f8 ["INT_ADD", "register:40f0:8", ["const:5b06f8:8", "const:4:8"]]
- 005b06f8 ["CALL", null, ["ram:5ac2ec:8"]]
+ 005d53c4 ["INT_ADD", "register:40f0:8", ["const:5d53c4:8", "const:4:8"]]
+ 005d53c4 ["CALL", null, ["ram:5d0fb8:8"]]
- 005b06f8 bytes fdeeff97
+ 005d53c4 bytes fdeeff97
- 005b0510 ["INT_ADD", "register:40f0:8", ["const:5b0510:8", "const:4:8"]]
- 005b0510 ["CALL", null, ["callee:005d5608:8"]]
+ 005d51dc ["INT_ADD", "register:40f0:8", ["const:5d51dc:8", "const:4:8"]]
+ 005d51dc ["CALL", null, ["callee:005d5608:8"]]
- 005b0510 bytes 0b010094
+ 005d51dc bytes 0b010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7647e4965c0b5519f8eaed806195bc3a"></a>

### [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md) → [`005d53c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md) FUN_005d53c8

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) · 呼出先 3件 [`005afe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md) [`005aff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005aff7c.md) [`005affc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005affc8.md)
- 新版 呼出元 2件 [`005cdcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cdcc0.md) [`005d51bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d51bc.md) · 呼出先 3件 [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) [`005d4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md) [`005d4c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d55e4",
      "value": [
        "leaf",
        "ram:5d4c94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b0918",
      "value": [
        "leaf",
        "ram:5affc8:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d5604",
      "value": [
        "leaf",
        "ram:5d4c48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b0938",
      "value": [
        "leaf",
        "ram:5aff7c:8"
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
      "005d55e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005affc8"
      ]
    ],
    [
      "005d5604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005aff7c"
      ]
    ]
  ],
  "added": [
    [
      "005d55e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d4c94"
      ]
    ],
    [
      "005d5604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d4c48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md#insn-005b0918) · [`005b0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md#insn-005b0938) · [`005b0734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md#insn-005b0734)
- 新版 [`005d55e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d55e4) · [`005d5604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d5604) · [`005d5400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d53c8.md#insn-005d5400)

~~~diff
- 005b0918 ["INT_ADD", "register:40f0:8", ["const:5b0918:8", "const:4:8"]]
- 005b0918 ["CALL", null, ["ram:5affc8:8"]]
+ 005d55e4 ["INT_ADD", "register:40f0:8", ["const:5d55e4:8", "const:4:8"]]
+ 005d55e4 ["CALL", null, ["ram:5d4c94:8"]]
- 005b0918 bytes acfdff97
+ 005d55e4 bytes acfdff97
- 005b0938 ["INT_ADD", "register:40f0:8", ["const:5b0938:8", "const:4:8"]]
- 005b0938 ["CALL", null, ["ram:5aff7c:8"]]
+ 005d5604 ["INT_ADD", "register:40f0:8", ["const:5d5604:8", "const:4:8"]]
+ 005d5604 ["CALL", null, ["ram:5d4c48:8"]]
- 005b0938 bytes 91fdff97
+ 005d5604 bytes 91fdff97
- 005b0734 ["INT_ADD", "register:40f0:8", ["const:5b0734:8", "const:4:8"]]
- 005b0734 ["CALL", null, ["callee:005d4b08:8"]]
+ 005d5400 ["INT_ADD", "register:40f0:8", ["const:5d5400:8", "const:4:8"]]
+ 005d5400 ["CALL", null, ["callee:005d4b08:8"]]
- 005b0734 bytes c2fdff97
+ 005d5400 bytes c2fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17cd7182adcd7d738a210067bdc52c3e"></a>

### [`005b0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0a4c.md) → [`005d5718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md) FUN_005d5718

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d5728",
      "incomplete_value": true,
      "site": "005d572c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0a5c",
      "incomplete_value": true,
      "site": "005b0a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d5720",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d572c",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d5720",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005d572c",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0a4c.md#insn-005b0a4c) · [`005b0a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0a4c.md#insn-005b0a54)
- 新版 [`005d5718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md#insn-005d5718) · [`005d5720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5718.md#insn-005d5720)

~~~diff
- 005b0a4c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 005d5718 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005b0a4c bytes 493300f0
+ 005d5718 bytes 293600b0
- 005b0a54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b0:8"]]
- 005b0a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fa8:8"]]
+ 005d5720 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0a54 bytes 29d942f9
+ 005d5720 bytes 29d547f9
~~~


<a id="compare-66d78ce35b3aef4a192597218266aa57"></a>

### [`005b0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md) → [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md) FUN_005d57cc

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b0e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0e84.md) · 呼出先 2件 [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md)
- 新版 呼出元 1件 [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) · 呼出先 2件 [`005d0fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0fb8.md) [`005d1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1004.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d5828",
      "value": [
        "leaf",
        "ram:5d0fb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b0b5c",
      "value": [
        "leaf",
        "ram:5ac2ec:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d5828",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ac2ec"
      ]
    ]
  ],
  "added": [
    [
      "005d5828",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d0fb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md#insn-005b0b5c) · [`005b0b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md#insn-005b0b40)
- 新版 [`005d5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md#insn-005d5828) · [`005d580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md#insn-005d580c)

~~~diff
- 005b0b5c ["INT_ADD", "register:40f0:8", ["const:5b0b5c:8", "const:4:8"]]
- 005b0b5c ["CALL", null, ["ram:5ac2ec:8"]]
+ 005d5828 ["INT_ADD", "register:40f0:8", ["const:5d5828:8", "const:4:8"]]
+ 005d5828 ["CALL", null, ["ram:5d0fb8:8"]]
- 005b0b5c bytes e4edff97
+ 005d5828 bytes e4edff97
- 005b0b40 ["INT_ADD", "register:40f0:8", ["const:5b0b40:8", "const:4:8"]]
- 005b0b40 ["CALL", null, ["callee:005d1004:8"]]
+ 005d580c ["INT_ADD", "register:40f0:8", ["const:5d580c:8", "const:4:8"]]
+ 005d580c ["CALL", null, ["callee:005d1004:8"]]
- 005b0b40 bytes feedff97
+ 005d580c bytes feedff97
~~~


<a id="compare-60b84c57fd658bbd068aff6b7e228819"></a>

### [`005b0b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md) → [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) FUN_005d582c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) · 呼出先 5件 [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) [`005b0d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0d5c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) · 呼出先 5件 [`005cde4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cde4c.md) [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) [`005cf05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf05c.md) [`005d5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5a28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.64% / 新版 97.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d58cc",
      "incomplete_value": true,
      "site": "005d58e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0c00",
      "incomplete_value": true,
      "site": "005b0c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d59a4",
      "incomplete_value": true,
      "site": "005d59b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0cd8",
      "incomplete_value": true,
      "site": "005b0ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d5a24",
      "value": [
        "leaf",
        "ram:5cf05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b0d58",
      "value": [
        "leaf",
        "ram:5aa390:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d58a0",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005d58c0",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "005d58e4",
      "DATA",
      [
        "storage",
        "00bf3b20",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d58a0",
      "READ",
      [
        "storage",
        "00c9afc0",
        null,
        "pointer"
      ]
    ],
    [
      "005d58c0",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "005d58e4",
      "DATA",
      [
        "storage",
        "00c70b48",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md#insn-005b0d58) · [`005b0b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md#insn-005b0b8c) · [`005b0bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md#insn-005b0bc4)
- 新版 [`005d5a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md#insn-005d5a24) · [`005d5858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md#insn-005d5858) · [`005d5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md#insn-005d5890)

~~~diff
- 005b0d58 ["INT_ADD", "register:40f0:8", ["const:5b0d58:8", "const:4:8"]]
- 005b0d58 ["CALL", null, ["ram:5aa390:8"]]
+ 005d5a24 ["INT_ADD", "register:40f0:8", ["const:5d5a24:8", "const:4:8"]]
+ 005d5a24 ["CALL", null, ["ram:5cf05c:8"]]
- 005b0d58 bytes 8ee5ff97
+ 005d5a24 bytes 8ee5ff97
- 005b0b8c ["INT_ADD", "register:40f0:8", ["const:5b0b8c:8", "const:4:8"]]
- 005b0b8c ["CALL", null, ["callee:005d5a28:8"]]
+ 005d5858 ["INT_ADD", "register:40f0:8", ["const:5d5858:8", "const:4:8"]]
+ 005d5858 ["CALL", null, ["callee:005d5a28:8"]]
- 005b0b8c bytes 74000094
+ 005d5858 bytes 74000094
- 005b0bc4 ["INT_ADD", "register:40f0:8", ["const:5b0bc4:8", "const:4:8"]]
- 005b0bc4 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d5890 ["INT_ADD", "register:40f0:8", ["const:5d5890:8", "const:4:8"]]
+ 005d5890 ["CALL", null, ["callee:00c57a90:8"]]
- 005b0bc4 bytes 1fa91894
+ 005d5890 bytes 80081a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7320d239b99f8eb831e7b29423b1c659"></a>

### [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) → [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) FUN_005d60d0

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md) · 呼出先 10件 [`005ab048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md) [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md) [`005ab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md) [`005b2434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2434.md)
- 新版 呼出元 1件 [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 10件 [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005d04d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d04d0.md) [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d62c0",
      "incomplete_value": true,
      "site": "005d62d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b15f4",
      "incomplete_value": true,
      "site": "005b1604",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d6944",
      "value": [
        "leaf",
        "ram:5cfd14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1c78",
      "value": [
        "leaf",
        "ram:5ab048:8"
      ]
    },
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d695c",
      "value": [
        "leaf",
        "ram:5cfed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1c90",
      "value": [
        "leaf",
        "ram:5ab20c:8"
      ]
    },
    "ordinal": 23,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d62c0",
      "READ",
      [
        "storage",
        "002b0db0",
        null,
        null
      ]
    ],
    [
      "005d6944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ab048"
      ]
    ],
    [
      "005d695c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ab20c"
      ]
    ]
  ],
  "added": [
    [
      "005d62c0",
      "READ",
      [
        "storage",
        "002c23b0",
        null,
        null
      ]
    ],
    [
      "005d6944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005cfd14"
      ]
    ],
    [
      "005d695c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005cfed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md#insn-005b1c78) · [`005b1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md#insn-005b1c90) · [`005b147c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md#insn-005b147c)
- 新版 [`005d6944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d6944) · [`005d695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d695c) · [`005d6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md#insn-005d6148)

~~~diff
- 005b1c78 ["INT_ADD", "register:40f0:8", ["const:5b1c78:8", "const:4:8"]]
- 005b1c78 ["CALL", null, ["ram:5ab048:8"]]
+ 005d6944 ["INT_ADD", "register:40f0:8", ["const:5d6944:8", "const:4:8"]]
+ 005d6944 ["CALL", null, ["ram:5cfd14:8"]]
- 005b1c78 bytes f4e4ff97
+ 005d6944 bytes f4e4ff97
- 005b1c90 ["INT_ADD", "register:40f0:8", ["const:5b1c90:8", "const:4:8"]]
- 005b1c90 ["CALL", null, ["ram:5ab20c:8"]]
+ 005d695c ["INT_ADD", "register:40f0:8", ["const:5d695c:8", "const:4:8"]]
+ 005d695c ["CALL", null, ["ram:5cfed8:8"]]
- 005b1c90 bytes 5fe5ff97
+ 005d695c bytes 5fe5ff97
- 005b147c ["INT_ADD", "register:40f0:8", ["const:5b147c:8", "const:4:8"]]
- 005b147c ["CALL", null, ["callee:005d717c:8"]]
+ 005d6148 ["INT_ADD", "register:40f0:8", ["const:5d6148:8", "const:4:8"]]
+ 005d6148 ["CALL", null, ["callee:005d717c:8"]]
- 005b147c bytes 0d040094
+ 005d6148 bytes 0d040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b001e7d532af7976bc328a93b29f230e"></a>

### [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) → [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) FUN_005d69b0

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md) · 呼出先 13件 [`005ab004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab004.md) [`005ab048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md) [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md) [`005ab258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab258.md)
- 新版 呼出元 1件 [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 13件 [`005cfcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md) [`005cfd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd14.md) [`005cfd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfd60.md) [`005cfed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfed8.md) [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.47% / 新版 99.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d6f3c",
      "value": [
        "leaf",
        "ram:5cfd14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b2270",
      "value": [
        "leaf",
        "ram:5ab048:8"
      ]
    },
    "ordinal": 25,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d6f54",
      "value": [
        "leaf",
        "ram:5cfed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b2288",
      "value": [
        "leaf",
        "ram:5ab20c:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d6f3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ab048"
      ]
    ],
    [
      "005d6f54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ab20c"
      ]
    ]
  ],
  "added": [
    [
      "005d6f3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005cfd14"
      ]
    ],
    [
      "005d6f54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005cfed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md#insn-005b2270) · [`005b2288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md#insn-005b2288) · [`005b1d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md#insn-005b1d84)
- 新版 [`005d6f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6f3c) · [`005d6f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6f54) · [`005d6a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md#insn-005d6a50)

~~~diff
- 005b2270 ["INT_ADD", "register:40f0:8", ["const:5b2270:8", "const:4:8"]]
- 005b2270 ["CALL", null, ["ram:5ab048:8"]]
+ 005d6f3c ["INT_ADD", "register:40f0:8", ["const:5d6f3c:8", "const:4:8"]]
+ 005d6f3c ["CALL", null, ["ram:5cfd14:8"]]
- 005b2270 bytes 76e3ff97
+ 005d6f3c bytes 76e3ff97
- 005b2288 ["INT_ADD", "register:40f0:8", ["const:5b2288:8", "const:4:8"]]
- 005b2288 ["CALL", null, ["ram:5ab20c:8"]]
+ 005d6f54 ["INT_ADD", "register:40f0:8", ["const:5d6f54:8", "const:4:8"]]
+ 005d6f54 ["CALL", null, ["ram:5cfed8:8"]]
- 005b2288 bytes e1e3ff97
+ 005d6f54 bytes e1e3ff97
- 005b1d84 ["INT_ADD", "register:40f0:8", ["const:5b1d84:8", "const:4:8"]]
- 005b1d84 ["CALL", null, ["callee:005cffac:8"]]
+ 005d6a50 ["INT_ADD", "register:40f0:8", ["const:5d6a50:8", "const:4:8"]]
+ 005d6a50 ["CALL", null, ["callee:005cffac:8"]]
- 005b1d84 bytes 57e5ff97
+ 005d6a50 bytes 57e5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9050da293e7e36ecd6b7a302e514fea3"></a>

### [`005b3380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md) → [`005d804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d804c.md) FUN_005d804c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 4件 [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.30% / 新版 81.30%

CFGの説明率　旧版 59.38% / 新版 47.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d81d0"
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
      "unmatched:005b33c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d815c"
      ]
    ],
    [
      "unmatched:005b350c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d81b8"
      ]
    ]
  ],
  "added": [
    [
      "005d808c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d815c"
      ]
    ],
    [
      "005d81d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d81b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b33c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md#insn-005b33c0) · [`005b3414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md#insn-005b3414) · [`005b341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md#insn-005b341c)

~~~diff
- 005b33c0 ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 005b33c0 bytes 82060054
- 005b3414 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005b3414 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005b3414 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 005b3414 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 005b3414 bytes 4a81839a
- 005b341c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005b341c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 005b341c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005b341c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b341c bytes 4831899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd10e94855ce57f74c312175648c0d4"></a>

### [`005b356c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md) → [`005d8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8238.md) FUN_005d8238

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 4件 [`005ab930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 4件 [`005d05fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d05fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 48.33% / 新版 39.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b381c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b35a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d830c"
      ]
    ],
    [
      "unmatched:005b3678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8338"
      ]
    ],
    [
      "unmatched:005b36c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8464"
      ]
    ]
  ],
  "added": [
    [
      "005d826c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d830c"
      ]
    ],
    [
      "005d8344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8338"
      ]
    ],
    [
      "005d838c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8464"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b35a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md#insn-005b35a0) · [`005b3674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md#insn-005b3674) · [`005b3678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md#insn-005b3678)

~~~diff
- 005b35a0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005b35a0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 005b35a0 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 005b35a0 bytes 09050054
- 005b3674 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 005b3674 ["COPY", "tmp:1:8", ["register:4068:8"]]
- 005b3674 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b3674 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005b3674 bytes 0c3481a8
- 005b3678 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005b3678 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 005b3678 bytes a1ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9e7f13a7e83a37f4ae5cedaedd0d99"></a>

### [`005b39cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md) → [`005d8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md) FUN_005d8698

採用 · 移動量 `+0x24ccc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `reordered`

- 旧版 呼出元 1件 [`005b3850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005d86a8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b39dc",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d86a4",
      "incomplete_value": false,
      "site": "005d86a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b39d8",
      "incomplete_value": false,
      "site": "005b39dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d86a4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005d86a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d86a4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d86a8",
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

- 旧版 [`005b39dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md#insn-005b39dc) · [`005b39d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md#insn-005b39d4) · [`005b39d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md#insn-005b39d8)
- 新版 [`005d86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md#insn-005d86a8) · [`005d86a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md#insn-005d86a0) · [`005d86a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md#insn-005d86a4)

~~~diff
- 005b39dc ["INT_ADD", "register:40f0:8", ["const:5b39dc:8", "const:4:8"]]
- 005b39dc ["CALL", null, ["ram:418c38:8"]]
+ 005d86a8 ["INT_ADD", "register:40f0:8", ["const:5d86a8:8", "const:4:8"]]
+ 005d86a8 ["CALL", null, ["ram:43b738:8"]]
- 005b39dc bytes 9794f997
+ 005d86a8 bytes 248cf997
- 005b39d4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005d86a0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005b39d4 bytes a0e7ff90
+ 005d86a0 bytes e0e6fff0
- 005b39d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005b39d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d86a4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005d86a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d86a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d86a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 bytes 00740e91
+ 005d86a4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f564007778e49589153fa1a73cf408e8"></a>

### [`005b3cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3cf4.md) → [`005d89c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d89c0.md) FUN_005d89c0

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3cf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b3cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b3cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b3d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8a20"
      ]
    ]
  ],
  "added": [
    [
      "005d89c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d89c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d89d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8a20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3cf4.md#insn-005b3cf4) · [`005b3cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3cf4.md#insn-005b3cf8) · [`005b3d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3cf4.md#insn-005b3d04)

~~~diff
- 005b3cf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b3cf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b3cf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005b3cf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b3cf4 bytes fd7bbea9
- 005b3cf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b3cf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b3cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005b3cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b3cf8 bytes f44f01a9
- 005b3d04 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b3d04 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005b3d04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005b3d04 bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d277b1dea996d0ab79b71714b4463fc"></a>

### [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) → [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) FUN_005d8b88

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 75件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a1ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md) [`005a1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1b30.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005a7844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md) · 呼出先 2件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 79件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) [`005c6160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6160.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005cc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md) · 呼出先 2件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 36.36% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3ec0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b3ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b3ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b3ec4",
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
      "005d8b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005d8b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d8b90",
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

- 旧版 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md#insn-005b3ebc) · [`005b3ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md#insn-005b3ec0) · [`005b3ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md#insn-005b3ec4)

~~~diff
- 005b3ebc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b3ebc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b3ebc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005b3ebc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b3ebc bytes fd7bbca9
- 005b3ec0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005b3ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005b3ec0 bytes f70b00f9
- 005b3ec4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b3ec4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b3ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005b3ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b3ec4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d50728cfb2575e4e3f1ed01e47fc244f"></a>

### [`005b3f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3f58.md) → [`005d8c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md) FUN_005d8c24

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`005b4028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md) [`00815030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815030.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`005d8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md) [`00846cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00846/00846cd0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 89.47% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005b3fa0",
      "incomplete_value": true,
      "site": "005b3fa4",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005b3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3f58.md#insn-005b3fa4) · [`005b3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3f58.md#insn-005b3f74) · [`005b3f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3f58.md#insn-005b3f7c)
- 新版 [`005d8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c70) · [`005d8c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c40) · [`005d8c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md#insn-005d8c48)

~~~diff
- 005b3fa4 ["INT_ADD", "register:40f0:8", ["const:5b3fa4:8", "const:4:8"]]
- 005b3fa4 ["CALL", null, ["callee:00c57a80:8"]]
+ 005d8c70 ["INT_ADD", "register:40f0:8", ["const:5d8c70:8", "const:4:8"]]
+ 005d8c70 ["CALL", null, ["callee:00c57a80:8"]]
- 005b3fa4 bytes 239c1894
+ 005d8c70 bytes 84fb1994
- 005b3f74 ["INT_ADD", "register:40f0:8", ["const:5b3f74:8", "const:4:8"]]
- 005b3f74 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d8c40 ["INT_ADD", "register:40f0:8", ["const:5d8c40:8", "const:4:8"]]
+ 005d8c40 ["CALL", null, ["callee:00c57ab0:8"]]
- 005b3f74 bytes 3b9c1894
+ 005d8c40 bytes 9cfb1994
- 005b3f7c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 005b3f7c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 005d8c48 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 005d8c48 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005b3f7c bytes 740100b4
+ 005d8c48 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d8b5bb9efbc502c5c8d53edb231cfe"></a>

### [`005b4d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d68.md) → [`005d9a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md) FUN_005d9a34

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b4278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005b4ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4ff8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005d9cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9cc4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.85% / 新版 68.85%

CFGの説明率　旧版 15.38% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4d8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b4d78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b4d8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b4df0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9a90"
      ]
    ]
  ],
  "added": [
    [
      "005d9a44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d9a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005d9abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9a90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d68.md#insn-005b4d78) · [`005b4d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d68.md#insn-005b4d8c) · [`005b4d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d68.md#insn-005b4d90)

~~~diff
- 005b4d78 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b4d78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b4d78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005b4d78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b4d78 bytes f44f05a9
- 005b4d8c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b4d8c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b4d8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b4d8c bytes a8831ff8
- 005b4d90 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005b4d90 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 005b4d90 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:8:8"]]
- 005b4d90 ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 005b4d90 bytes bf8e00f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0d85e5c2648c03fca5999ae4dd8857"></a>

### [`005b4f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md) → [`005d9c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md) FUN_005d9c18

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005d9c2c",
      "incomplete_value": false,
      "site": "005d9c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4f60",
      "incomplete_value": false,
      "site": "005b4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d9c30",
      "DATA",
      [
        "storage",
        "00bf3e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005d9c30",
      "DATA",
      [
        "storage",
        "00c70e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md#insn-005b4f58) · [`005b4f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md#insn-005b4f5c) · [`005b4f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md#insn-005b4f60)
- 新版 [`005d9c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c24) · [`005d9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c28) · [`005d9c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c18.md#insn-005d9c2c)

~~~diff
- 005b4f58 ["INT_ADD", "register:40f0:8", ["const:5b4f58:8", "const:4:8"]]
- 005b4f58 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d9c24 ["INT_ADD", "register:40f0:8", ["const:5d9c24:8", "const:4:8"]]
+ 005d9c24 ["CALL", null, ["callee:00c57a90:8"]]
- 005b4f58 bytes 3a981894
+ 005d9c24 bytes 9bf71994
- 005b4f5c ["COPY", "register:4040:8", ["const:bf3000:8"]]
+ 005d9c28 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b4f5c bytes e83100f0
+ 005d9c28 bytes a83400f0
- 005b4f60 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 005b4f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005d9c2c ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 005d9c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005d9c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 bytes 08013991
+ 005d9c2c bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b1948b10be5a67a459dd405aab53756"></a>

### [`005b4ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4ff8.md) → [`005d9cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9cc4.md) FUN_005d9cc4

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b4d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4d68.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005d9a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9a34.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 68.25% / 新版 72.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5090"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b50bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d9d5c"
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
      "unmatched:005b5090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9d70"
      ]
    ],
    [
      "unmatched:005b50bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9db0"
      ]
    ]
  ],
  "added": [
    [
      "005d9d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9d70"
      ]
    ],
    [
      "005d9d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9db0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4ff8.md#insn-005b5090) · [`005b50bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4ff8.md#insn-005b50bc)
- 新版 [`005d9d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9cc4.md#insn-005d9d5c)

~~~diff
- 005b5090 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005b5090 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 005b5090 bytes aa000054
- 005b50bc ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 005b50bc ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 005b50bc bytes 4b0100b4
+ 005d9d5c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005d9d5c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 005d9d5c bytes aa000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e22bce754766e147a8120687333b5a"></a>

### [`005b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md) → [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) FUN_005d9f0c

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.49% / 新版 68.49%

CFGの説明率　旧版 29.29% / 新版 26.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5324"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b5264",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "005d9f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b52a8"
      ]
    ],
    [
      "unmatched:005b5290",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005a3eb8"
      ]
    ]
  ],
  "added": [
    [
      "005d9f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "005d9f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d9f74"
      ]
    ],
    [
      "005d9f5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005c8780"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md#insn-005b5264) · [`005b5320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md#insn-005b5320) · [`005b5324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md#insn-005b5324)

~~~diff
- 005b5264 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b5264 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b5264 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b5264 bytes a8831ff8
- 005b5320 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 005b5320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005b5320 bytes e03b00f9
- 005b5324 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b5324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b5324 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca05c375fdd531c16d6454889c0ee170"></a>

### [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) → [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) FUN_005da544

採用 · 移動量 `+0x24ccc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 26件 [`005b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md) [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) [`00684ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00684/00684ffc.md) [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) [`0071f7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f7e8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005b59a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 26件 [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 15.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b587c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b587c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b587c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b5880",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b5884",
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
      "005da548",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005da54c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005da550",
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

- 旧版 [`005b587c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md#insn-005b587c) · [`005b5880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md#insn-005b5880) · [`005b5884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md#insn-005b5884)

~~~diff
- 005b587c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b587c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b587c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005b587c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b587c bytes fd7b04a9
- 005b5880 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b5880 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b5880 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005b5880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b5880 bytes f65705a9
- 005b5884 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b5884 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b5884 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005b5884 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b5884 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-febd144ff96260651a83ea997db8847f"></a>

### [`005b59a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md) → [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) FUN_005da66c

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) [`005b59a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md) [`0060320c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md) [`00641308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) [`005da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da66c.md) [`00628d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md) [`006675e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.90% / 新版 80.90%

CFGの説明率　旧版 27.55% / 新版 33.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 3件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b59b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b59b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b59b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b59b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b59b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b59c0",
      "WRITE",
      [
        "storage",
        "Stack[-0xfc]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005da680",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005da684",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005da68c",
      "WRITE",
      [
        "storage",
        "Stack[-0xfc]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b59b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b59b4) · [`005b59b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b59b8) · [`005b59c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b59c0)

~~~diff
- 005b59b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b59b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b59b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 005b59b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b59b4 bytes f65710a9
- 005b59b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b59b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b59b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 005b59b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b59b8 bytes f44f11a9
- 005b59c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:24:8"]]
- 005b59c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:4"]]
- 005b59c0 bytes e32700b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a963c221b85800c184f5a0f5e09ce3"></a>

### [`005b62a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b62a8.md) → [`005daf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf74.md) FUN_005daf74

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005daf78",
      "incomplete_value": false,
      "site": "005daf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b62ac",
      "incomplete_value": false,
      "site": "005b62b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005daf7c",
      "DATA",
      [
        "storage",
        "00bf3f40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005daf7c",
      "DATA",
      [
        "storage",
        "00c70f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b62a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b62a8.md#insn-005b62a8) · [`005b62ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b62a8.md#insn-005b62ac)
- 新版 [`005daf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf74.md#insn-005daf74) · [`005daf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf74.md#insn-005daf78)

~~~diff
- 005b62a8 ["COPY", "register:4040:8", ["const:bf3000:8"]]
+ 005daf74 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b62a8 bytes e83100b0
+ 005daf74 bytes a83400d0
- 005b62ac ["COPY", "tmp:0:8", ["const:f40:8"]]
- 005b62ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b62ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b62ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005daf78 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 005daf78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005daf78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005daf78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b62ac bytes 08013d91
+ 005daf78 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6dedccbd9a13bf142879630fb1f8c4"></a>

### [`005b6778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md) → [`005db448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db448.md) FUN_005db448

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 29.79% / 新版 25.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b677c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b677c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b677c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6780",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6784",
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
      "005db44c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005db450",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005db454",
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

- 旧版 [`005b677c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md#insn-005b677c) · [`005b6780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md#insn-005b6780) · [`005b6784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md#insn-005b6784)

~~~diff
- 005b677c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b677c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b677c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 005b677c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b677c bytes fd7b0ea9
- 005b6780 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b6780 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b6780 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 005b6780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b6780 bytes f6570fa9
- 005b6784 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b6784 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b6784 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 005b6784 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b6784 bytes f44f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55744f9c3fbcdb525755b835f9e3c97e"></a>

### [`005b6ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ac8.md) → [`005db798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db798.md) FUN_005db798

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005db7a4",
      "incomplete_value": false,
      "site": "005db7a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6ad4",
      "incomplete_value": false,
      "site": "005b6ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005db7a4",
      "DATA",
      [
        "storage",
        "00bf41d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005db7a4",
      "DATA",
      [
        "storage",
        "00c711f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ac8.md#insn-005b6acc) · [`005b6ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ac8.md#insn-005b6ad0)
- 新版 [`005db79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db798.md#insn-005db79c) · [`005db7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db798.md#insn-005db7a0)

~~~diff
- 005b6acc ["COPY", "register:4048:8", ["const:bf4000:8"]]
+ 005db79c ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b6acc bytes e93100d0
+ 005db79c bytes a93400d0
- 005b6ad0 ["COPY", "tmp:0:8", ["const:1d0:8"]]
- 005b6ad0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005db7a0 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 005db7a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005db7a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005db7a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 bytes 29410791
+ 005db7a0 bytes 29e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7edaa5c40916b088100110759084b9f4"></a>

### [`005b6ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ae4.md) → [`005db7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db7b4.md) FUN_005db7b4

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6b08"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005db7dc",
      "incomplete_value": false,
      "site": "005db7e4",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005db7d8"
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
      "unmatched:005b6b08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "005db7d8",
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

- 旧版 [`005b6b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ae4.md#insn-005b6b08) · [`005b6b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ae4.md#insn-005b6b14)
- 新版 [`005db7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db7b4.md#insn-005db7e4) · [`005db7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db7b4.md#insn-005db7d8)

~~~diff
- 005b6b08 ["INT_ADD", "register:40f0:8", ["const:5b6b08:8", "const:4:8"]]
- 005b6b08 ["CALL", null, ["ram:457e1c:8"]]
- 005b6b08 bytes c584fa97
- 005b6b14 ["INT_ADD", "register:40f0:8", ["const:5b6b14:8", "const:4:8"]]
- 005b6b14 ["CALL", null, ["callee:0047cd94:8"]]
+ 005db7e4 ["INT_ADD", "register:40f0:8", ["const:5db7e4:8", "const:4:8"]]
+ 005db7e4 ["CALL", null, ["callee:0047cd94:8"]]
- 005b6b14 bytes fa8cfa97
+ 005db7e4 bytes 6c85fa97
+ 005db7d8 ["INT_ADD", "register:40f0:8", ["const:5db7d8:8", "const:4:8"]]
+ 005db7d8 ["CALL", null, ["ram:47acb4:8"]]
+ 005db7d8 bytes 377dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03073609a3a8d528afedc4bfadfde973"></a>

### [`005b6b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md) → [`005db828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db828.md) FUN_005db828

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_value

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005db848",
      "incomplete_value": false,
      "site": "005db84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6b78",
      "incomplete_value": false,
      "site": "005b6b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005db840",
      "incomplete_value": true,
      "site": "005db850",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b6b80",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005b6b68",
      "incomplete_value": false,
      "site": "005b6b6c",
      "value": [
        "leaf",
        "const:18:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005db84c",
      "DATA",
      [
        "storage",
        "00bf4260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005db84c",
      "DATA",
      [
        "storage",
        "00c71288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md#insn-005b6b6c) · [`005b6b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md#insn-005b6b74) · [`005b6b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md#insn-005b6b78)
- 新版 [`005db83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db828.md#insn-005db83c) · [`005db844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db828.md#insn-005db844) · [`005db848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db828.md#insn-005db848)

~~~diff
- 005b6b6c ["INT_ADD", "register:40f0:8", ["const:5b6b6c:8", "const:4:8"]]
- 005b6b6c ["CALL", null, ["callee:00c57a90:8"]]
+ 005db83c ["INT_ADD", "register:40f0:8", ["const:5db83c:8", "const:4:8"]]
+ 005db83c ["CALL", null, ["callee:00c57a90:8"]]
- 005b6b6c bytes 35911894
+ 005db83c bytes 95f01994
- 005b6b74 ["COPY", "register:4040:8", ["const:bf4000:8"]]
+ 005db844 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b6b74 bytes e83100d0
+ 005db844 bytes a83400d0
- 005b6b78 ["COPY", "tmp:0:8", ["const:260:8"]]
- 005b6b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005db848 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 005db848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005db848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005db848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 bytes 08810991
+ 005db848 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9743f6cb850c2c1ade4cdd8cbb2c8e"></a>

### [`005b6bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md) → [`005db880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db880.md) FUN_005db880

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b7004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005dbcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.36% / 新版 66.36%

CFGの説明率　旧版 22.54% / 新版 21.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6cc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6cc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b6bd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005db8b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b6c08"
      ]
    ],
    [
      "unmatched:005b6bec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "005db8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005db8b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005db8d8"
      ]
    ],
    [
      "005db8bc",
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

- 旧版 [`005b6bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md#insn-005b6bd0) · [`005b6cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md#insn-005b6cc4) · [`005b6cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md#insn-005b6cc8)

~~~diff
- 005b6bd0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b6bd0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b6bd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b6bd0 bytes a8831ff8
- 005b6cc4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 005b6cc4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 005b6cc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 005b6cc4 bytes e8830039
- 005b6cc8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005b6cc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005b6cc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2e:8"]]
- 005b6cc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005b6cc8 bytes ffbb0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912f5e57af31a97fa2ebce0d0d4a900d"></a>

### [`005b7004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md) → [`005dbcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md) FUN_005dbcd4

採用 · 移動量 `+0x24cd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005b6bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6bb0.md) [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00426e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 8件 [`005db880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db880.md) [`007728a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 10.53% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005dbd04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b70d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7034",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b70d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dbe08"
      ]
    ]
  ],
  "added": [
    [
      "005dbd04",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005dbda8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dbe08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md#insn-005b7034) · [`005b7074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md#insn-005b7074) · [`005b70a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md#insn-005b70a8)
- 新版 [`005dbd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md#insn-005dbd44) · [`005dbd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md#insn-005dbd78)

~~~diff
- 005b7034 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005b7034 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b7034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b7034 bytes a9831ff8
- 005b7074 ["INT_ADD", "register:40f0:8", ["const:5b7074:8", "const:4:8"]]
- 005b7074 ["CALL", null, ["callee:0043bae0:8"]]
+ 005dbd44 ["INT_ADD", "register:40f0:8", ["const:5dbd44:8", "const:4:8"]]
+ 005dbd44 ["CALL", null, ["callee:0043bae0:8"]]
- 005b7074 bytes db87f997
+ 005dbd44 bytes 677ff997
- 005b70a8 ["INT_ADD", "register:40f0:8", ["const:5b70a8:8", "const:4:8"]]
- 005b70a8 ["CALL", null, ["callee:0044998c:8"]]
+ 005dbd78 ["INT_ADD", "register:40f0:8", ["const:5dbd78:8", "const:4:8"]]
+ 005dbd78 ["CALL", null, ["callee:0044998c:8"]]
- 005b70a8 bytes 79bff997
+ 005dbd78 bytes 05b7f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1bcb37194685ee1e0d0649b3cf366a"></a>

### [`005b7140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7140.md) → [`005dbe10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe10.md) FUN_005dbe10

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dbe34",
      "incomplete_value": false,
      "site": "005dbe34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7164",
      "incomplete_value": false,
      "site": "005b7164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dbe34",
      "DATA",
      [
        "storage",
        "00bf42d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dbe34",
      "DATA",
      [
        "storage",
        "00c712f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7140.md#insn-005b7154) · [`005b715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7140.md#insn-005b715c) · [`005b7160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7140.md#insn-005b7160)
- 新版 [`005dbe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe10.md#insn-005dbe24) · [`005dbe2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe10.md#insn-005dbe2c) · [`005dbe30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe10.md#insn-005dbe30)

~~~diff
- 005b7154 ["INT_ADD", "register:40f0:8", ["const:5b7154:8", "const:4:8"]]
- 005b7154 ["CALL", null, ["callee:00c57a90:8"]]
+ 005dbe24 ["INT_ADD", "register:40f0:8", ["const:5dbe24:8", "const:4:8"]]
+ 005dbe24 ["CALL", null, ["callee:00c57a90:8"]]
- 005b7154 bytes bb8f1894
+ 005dbe24 bytes 1bef1994
- 005b715c ["COPY", "register:4040:8", ["const:bf4000:8"]]
+ 005dbe2c ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b715c bytes e83100b0
+ 005dbe2c bytes a83400d0
- 005b7160 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 005b7160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005dbe30 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005dbe30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005dbe30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005dbe30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7160 bytes 08410b91
+ 005dbe30 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b735e35fab14539603d3e04000d3bc"></a>

### [`005b7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7174.md) → [`005dbe44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe44.md) FUN_005dbe44

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dbe50",
      "incomplete_value": false,
      "site": "005dbe50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7180",
      "incomplete_value": false,
      "site": "005b7180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dbe50",
      "DATA",
      [
        "storage",
        "00bf42d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dbe50",
      "DATA",
      [
        "storage",
        "00c712f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7174.md#insn-005b7178) · [`005b717c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7174.md#insn-005b717c)
- 新版 [`005dbe48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe44.md#insn-005dbe48) · [`005dbe4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe44.md#insn-005dbe4c)

~~~diff
- 005b7178 ["COPY", "register:4048:8", ["const:bf4000:8"]]
+ 005dbe48 ["COPY", "register:4048:8", ["const:c71000:8"]]
- 005b7178 bytes e93100b0
+ 005dbe48 bytes a93400d0
- 005b717c ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 005b717c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b717c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b717c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005dbe4c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005dbe4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005dbe4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005dbe4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b717c bytes 29410b91
+ 005dbe4c bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c894755b8071726a56f9028a744400a7"></a>

### [`005b7190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7190.md) → [`005dbe60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe60.md) FUN_005dbe60

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005dbe84",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b71b4",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dbe84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "005dbe84",
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

- 旧版 [`005b71b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7190.md#insn-005b71b4) · [`005b71c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7190.md#insn-005b71c0)
- 新版 [`005dbe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe60.md#insn-005dbe84) · [`005dbe90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbe60.md#insn-005dbe90)

~~~diff
- 005b71b4 ["INT_ADD", "register:40f0:8", ["const:5b71b4:8", "const:4:8"]]
- 005b71b4 ["CALL", null, ["ram:457e1c:8"]]
+ 005dbe84 ["INT_ADD", "register:40f0:8", ["const:5dbe84:8", "const:4:8"]]
+ 005dbe84 ["CALL", null, ["ram:47acb4:8"]]
- 005b71b4 bytes 1a83fa97
+ 005dbe84 bytes 8c7bfa97
- 005b71c0 ["INT_ADD", "register:40f0:8", ["const:5b71c0:8", "const:4:8"]]
- 005b71c0 ["CALL", null, ["callee:0047cd94:8"]]
+ 005dbe90 ["INT_ADD", "register:40f0:8", ["const:5dbe90:8", "const:4:8"]]
+ 005dbe90 ["CALL", null, ["callee:0047cd94:8"]]
- 005b71c0 bytes 4f8bfa97
+ 005dbe90 bytes c183fa97
~~~


<a id="compare-2e0858d5209169c63e4040268cfbb189"></a>

### [`005b7244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7244.md) → [`005dbf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf14.md) FUN_005dbf14

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005dbf18",
      "incomplete_value": false,
      "site": "005dbf1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7248",
      "incomplete_value": false,
      "site": "005b724c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005dbf2c",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "old": {
      "definition_site": "005b7254",
      "incomplete_value": true,
      "site": "005b725c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dbf1c",
      "DATA",
      [
        "storage",
        "00bf4350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dbf1c",
      "DATA",
      [
        "storage",
        "00c71378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7244.md#insn-005b7244) · [`005b7248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7244.md#insn-005b7248) · [`005b7254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7244.md#insn-005b7254)
- 新版 [`005dbf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf14.md#insn-005dbf14) · [`005dbf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf14.md#insn-005dbf18)

~~~diff
- 005b7244 ["COPY", "register:4040:8", ["const:bf4000:8"]]
+ 005dbf14 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 005b7244 bytes e83100b0
+ 005dbf14 bytes a83400d0
- 005b7248 ["COPY", "tmp:0:8", ["const:350:8"]]
- 005b7248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005dbf18 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 005dbf18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005dbf18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005dbf18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7248 bytes 08410d91
+ 005dbf18 bytes 08e10d91
- 005b7254 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005b7254 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 005b7254 ["COPY", "register:5010:8", ["const:0:8"]]
- 005b7254 ["COPY", "register:5018:8", ["const:0:8"]]
- 005b7254 bytes 0080c03c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a541238fd3425ee86578799846db2b23"></a>

### [`005b74d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74d0.md) → [`005dc1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc1a0.md) FUN_005dc1a0

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`005a78d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a78d0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005cc560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc560.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005dc1bc",
      "incomplete_value": true,
      "site": "005dc1c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b74ec",
      "incomplete_value": true,
      "site": "005b74f0",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005b757c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005dc258",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b7588",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7514",
      "DATA",
      [
        "storage",
        "0032ff54",
        null,
        "byte[43]"
      ]
    ],
    [
      "005dc248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b75b8"
      ]
    ],
    [
      "unmatched:005b757c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "005dc1e4",
      "DATA",
      [
        "storage",
        "00333f94",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "005dc248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dc288"
      ]
    ],
    [
      "005dc24c",
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

- 旧版 [`005b74f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74d0.md#insn-005b74f0) · [`005b757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74d0.md#insn-005b757c) · [`005b7588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b74d0.md#insn-005b7588)
- 新版 [`005dc1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc1a0.md#insn-005dc1c0) · [`005dc258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc1a0.md#insn-005dc258)

~~~diff
- 005b74f0 ["INT_ADD", "register:40f0:8", ["const:5b74f0:8", "const:4:8"]]
- 005b74f0 ["CALL", null, ["callee:008b6e60:8"]]
+ 005dc1c0 ["INT_ADD", "register:40f0:8", ["const:5dc1c0:8", "const:4:8"]]
+ 005dc1c0 ["CALL", null, ["callee:008b6e60:8"]]
- 005b74f0 bytes f4310b94
+ 005dc1c0 bytes 286b0b94
- 005b757c ["INT_ADD", "register:40f0:8", ["const:5b757c:8", "const:4:8"]]
- 005b757c ["CALL", null, ["ram:457e1c:8"]]
- 005b757c bytes 2882fa97
- 005b7588 ["INT_ADD", "register:40f0:8", ["const:5b7588:8", "const:4:8"]]
- 005b7588 ["CALL", null, ["ram:457e1c:8"]]
+ 005dc258 ["INT_ADD", "register:40f0:8", ["const:5dc258:8", "const:4:8"]]
+ 005dc258 ["CALL", null, ["ram:47acb4:8"]]
- 005b7588 bytes 2582fa97
+ 005dc258 bytes 977afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497d529b9ff4c603f6ae5e02f1d8963c"></a>

### [`005b77d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77d8.md) → [`005dc4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc4a8.md) _INIT_65

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.54% / 新版 65.54%

CFGの説明率　旧版 60.00% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b781c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7808",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7814",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005b781c",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005dc4d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005dc4e4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005dc4ec",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77d8.md#insn-005b7808) · [`005b781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77d8.md#insn-005b781c) · [`005b7820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b77d8.md#insn-005b7820)

~~~diff
- 005b7808 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005b7808 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b7808 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b7808 bytes a9831ff8
- 005b781c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005b781c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 005b781c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005b781c bytes ea130278
- 005b7820 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 005b7820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005b7820 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5d8e503ca36c721edb319d34f46791"></a>

### [`005b7b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md) → [`005dc848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc848.md) FUN_005dc848

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.33% / 新版 80.33%

CFGの説明率　旧版 17.95% / 新版 15.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005dc868",
      "incomplete_value": true,
      "site": "005dc870",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7b98",
      "incomplete_value": true,
      "site": "005b7ba0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7c34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dc868",
      "READ",
      [
        "storage",
        "002b1780",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dc8c4"
      ]
    ],
    [
      "unmatched:005b7c2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0044104c"
      ]
    ]
  ],
  "added": [
    [
      "005dc868",
      "READ",
      [
        "storage",
        "002c2df0",
        null,
        null
      ]
    ],
    [
      "005dc8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dc8c4"
      ]
    ],
    [
      "005dc8fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0044104c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md#insn-005b7bdc) · [`005b7bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md#insn-005b7bec) · [`005b7c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md#insn-005b7c2c)

~~~diff
- 005b7bdc ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 005b7bdc bytes c0000054
- 005b7bec ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7bec ["INT_ADD", "register:40f0:8", ["const:5b7bec:8", "const:4:8"]]
- 005b7bec ["CALLIND", null, ["register:0:8"]]
- 005b7bec bytes 00013fd6
- 005b7c2c ["INT_ADD", "register:40f0:8", ["const:5b7c2c:8", "const:4:8"]]
- 005b7c2c ["CALL", null, ["callee:0044104c:8"]]
- 005b7c2c bytes 489af997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a21124359ab36f04db4da92b0435053"></a>

### [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) → [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) FUN_005dca68

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005b7b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7b78.md) [`005b9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md) [`005b97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md) [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md) · 呼出先 1件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)
- 新版 呼出元 5件 [`005dc848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc848.md) [`005ddde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005ddde8.md) [`005de470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md) [`005de640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de640.md) [`005dee40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005dee40.md) · 呼出先 1件 [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.81% / 新版 90.81%

CFGの説明率　旧版 87.88% / 新版 90.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005dcb28"
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
      "unmatched:005b7e5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcbe8"
      ]
    ],
    [
      "005dcbec",
      "PARAM",
      [
        "storage",
        "002a362e",
        null,
        "string"
      ]
    ],
    [
      "005dcc08",
      "PARAM",
      [
        "storage",
        "0029d6a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005dcb2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcbe8"
      ]
    ],
    [
      "005dcbec",
      "PARAM",
      [
        "storage",
        "002b3d08",
        null,
        "string"
      ]
    ],
    [
      "005dcc08",
      "PARAM",
      [
        "storage",
        "002ad931",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md#insn-005b7e58) · [`005b7e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md#insn-005b7e5c) · [`005b7f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md#insn-005b7f24)
- 新版 [`005dcbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md#insn-005dcbf4)

~~~diff
- 005b7e58 ["COPY", "tmp:0:1", ["register:101:1"]]
- 005b7e58 ["COPY", "tmp:1:1", ["const:0:1"]]
- 005b7e58 ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 005b7e58 ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 005b7e58 bytes 000149fa
- 005b7e5c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005b7e5c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 005b7e5c bytes e1050054
- 005b7f24 ["INT_ADD", "register:40f0:8", ["const:5b7f24:8", "const:4:8"]]
- 005b7f24 ["CALL", null, ["callee:00441e54:8"]]
+ 005dcbf4 ["INT_ADD", "register:40f0:8", ["const:5dcbf4:8", "const:4:8"]]
+ 005dcbf4 ["CALL", null, ["callee:00441e54:8"]]
- 005b7f24 bytes 0c9df997
+ 005dcbf4 bytes 9894f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-727f454700d3093787f2908eab75bb3f"></a>

### [`005b807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md) → [`005dcd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md) FUN_005dcd4c

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005c43a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c43a4.md) [`005c7548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c7/005c7548.md) · 呼出先 3件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md)
- 新版 呼出元 2件 [`005e9094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e9094.md) [`005ec234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ec/005ec234.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) [`005dda60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.16% / 新版 84.16%

CFGの説明率　旧版 15.00% / 新版 16.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8118"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8300"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b843c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dcefc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcfb8"
      ]
    ],
    [
      "005dcfd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcf90"
      ]
    ],
    [
      "005dcf6c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b82e8"
      ]
    ]
  ],
  "added": [
    [
      "005dcefc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcf38"
      ]
    ],
    [
      "005dcf50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcf90"
      ]
    ],
    [
      "005dcf6c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005dcfb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md#insn-005b8118) · [`005b81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md#insn-005b81f4) · [`005b825c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md#insn-005b825c)
- 新版 [`005dcec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md#insn-005dcec4) · [`005dcf2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md#insn-005dcf2c)

~~~diff
- 005b8118 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b8118 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005b8118 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 005b8118 ["COPY", "register:4000:8", ["tmp:0:8"]]
- 005b8118 bytes 00018a9a
- 005b81f4 ["INT_ADD", "register:40f0:8", ["const:5b81f4:8", "const:4:8"]]
- 005b81f4 ["CALL", null, ["callee:005dda60:8"]]
+ 005dcec4 ["INT_ADD", "register:40f0:8", ["const:5dcec4:8", "const:4:8"]]
+ 005dcec4 ["CALL", null, ["callee:005dda60:8"]]
- 005b81f4 bytes e7020094
+ 005dcec4 bytes e7020094
- 005b825c ["INT_ADD", "register:40f0:8", ["const:5b825c:8", "const:4:8"]]
- 005b825c ["CALL", null, ["callee:005dd710:8"]]
+ 005dcf2c ["INT_ADD", "register:40f0:8", ["const:5dcf2c:8", "const:4:8"]]
+ 005dcf2c ["CALL", null, ["callee:005dd710:8"]]
- 005b825c bytes f9010094
+ 005dcf2c bytes f9010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-642db2e6f0e2ffe6d637731c1492997a"></a>

### [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) → [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) FUN_005dd710

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005b807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md) [`005c43a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c43a4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`005dcd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md) [`005e9094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e9094.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.76% / 新版 84.76%

CFGの説明率　旧版 27.63% / 新版 36.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `return_value_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8a54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b8a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b8ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dd7e0"
      ]
    ]
  ],
  "added": [
    [
      "005dd720",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005dd724",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dd7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005dd7e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md#insn-005b8a50) · [`005b8a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md#insn-005b8a54) · [`005b8ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md#insn-005b8ae8)

~~~diff
- 005b8a50 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b8a50 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b8a50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005b8a50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b8a50 bytes f65704a9
- 005b8a54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b8a54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b8a54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005b8a54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b8a54 bytes f44f05a9
- 005b8ae8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005b8ae8 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 005b8ae8 bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3b082aec35d0199f0996917f394856"></a>

### [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md) → [`005dda60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md) FUN_005dda60

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b807c.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abf0.md) [`0044ac08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac08.md)
- 新版 呼出元 1件 [`005dcd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dcd4c.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da88.md) [`0046daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daa0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.90% / 新版 79.90%

CFGの説明率　旧版 37.10% / 新版 35.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005ddb7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b8de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b8de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ddae8"
      ]
    ],
    [
      "unmatched:005b8e20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ddae0"
      ]
    ],
    [
      "unmatched:005b8ecc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005df78c"
      ]
    ]
  ],
  "added": [
    [
      "005ddab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ddae8"
      ]
    ],
    [
      "005ddaf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ddae0"
      ]
    ],
    [
      "005ddb9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005df78c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md#insn-005b8de4) · [`005b8df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md#insn-005b8df0) · [`005b8e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md#insn-005b8e20)
- 新版 [`005ddac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md#insn-005ddac0)

~~~diff
- 005b8de4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 005b8de4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 005b8de4 bytes a90100b5
- 005b8df0 ["INT_ADD", "register:40f0:8", ["const:5b8df0:8", "const:4:8"]]
- 005b8df0 ["CALL", null, ["callee:0046d770:8"]]
+ 005ddac0 ["INT_ADD", "register:40f0:8", ["const:5ddac0:8", "const:4:8"]]
+ 005ddac0 ["CALL", null, ["callee:0046d770:8"]]
- 005b8df0 bytes ba46fa97
+ 005ddac0 bytes 2c3ffa97
- 005b8e20 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005b8e20 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 005b8e20 bytes 8bffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d67ce80dd428838b1872720bcab402b5"></a>

### [`005b90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b90c0.md) → [`005ddd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005ddd90.md) FUN_005ddd90

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`005c6d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c6/005c6d44.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005eba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005eb/005eba30.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-fa4e679a2cd76b0d9a96c937062e33fa"></a>

### [`005b9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md) → [`005ddde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005ddde8.md) FUN_005ddde8

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`005b97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md)
- 新版 呼出元 1件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`005de470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.07% / 新版 71.07%

CFGの説明率　旧版 15.27% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 32件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b911c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b911c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b911c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b9120",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b9124",
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
      "005dddec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005dddf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005dddf4",
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

- 旧版 [`005b911c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md#insn-005b911c) · [`005b9120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md#insn-005b9120) · [`005b9124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md#insn-005b9124)

~~~diff
- 005b911c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b911c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b911c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005b911c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b911c bytes fd7b06a9
- 005b9120 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005b9120 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005b9120 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005b9120 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9120 bytes fc6f07a9
- 005b9124 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005b9124 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005b9124 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 005b9124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9124 bytes fa6708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d29e6d01d2174beb5e9d8064e40b8913"></a>

### [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) → [`005de640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de640.md) FUN_005de640

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md)
- 新版 呼出元 1件 [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`005dee40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005dee40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.64% / 新版 74.64%

CFGの説明率　旧版 43.67% / 新版 40.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 6件, `store_value` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b9988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b998c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b9988",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b998c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b99a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005de658",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005de65c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005de678",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md#insn-005b9988) · [`005b998c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md#insn-005b998c) · [`005b99a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md#insn-005b99a8)

~~~diff
- 005b9988 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005b9988 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005b9988 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 005b9988 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b9988 bytes f6570aa9
- 005b998c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b998c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b998c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 005b998c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b998c bytes f44f0ba9
- 005b99a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b99a8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 005b99a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b99a8 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c52ff3a398fd45c2b0598ea39d3e6bf"></a>

### [`005ba170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md) → [`005dee40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005dee40.md) FUN_005dee40

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005de640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de640.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.81% / 新版 74.81%

CFGの説明率　旧版 25.00% / 新版 32.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba178"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba174",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba178",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba17c",
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
      "005dee44",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005dee48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005dee4c",
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

- 旧版 [`005ba174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md#insn-005ba174) · [`005ba178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md#insn-005ba178) · [`005ba17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba170.md#insn-005ba17c)

~~~diff
- 005ba174 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ba174 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ba174 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005ba174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba174 bytes fd7b04a9
- 005ba178 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 005ba178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005ba178 bytes f72b00f9
- 005ba17c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ba17c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ba17c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005ba17c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba17c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3208839bc6b2efd686ce0a520f91e1fa"></a>

### [`005ba3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md) → [`005df094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df094.md) FUN_005df094

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md)
- 新版 呼出元 4件 [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md) [`005df58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.83% / 新版 52.83%

CFGの説明率　旧版 25.53% / 新版 22.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba67c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba3c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba40c",
      "DATA",
      [
        "storage",
        "002c6b86",
        "switchD_005ba414::switchdataD_002c6b86",
        "ushort"
      ]
    ],
    [
      "005df0f8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005df098",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005df0dc",
      "DATA",
      [
        "storage",
        "002d85b2",
        "switchD_005df0e4::switchdataD_002d85b2",
        "ushort"
      ]
    ],
    [
      "005df0f8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ba3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md#insn-005ba3c8) · [`005ba67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md#insn-005ba67c) · [`005ba688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md#insn-005ba688)

~~~diff
- 005ba3c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ba3c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ba3c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005ba3c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba3c8 bytes fd7b04a9
- 005ba67c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 005ba67c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:4"]]
- 005ba67c bytes 1b2000b9
- 005ba688 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005ba688 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005ba688 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005ba688 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005ba688 bytes 1f7c03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a738b5e88099caaf125c08bbb21d58"></a>

### [`005baabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md) → [`005df78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df78c.md) FUN_005df78c

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md)
- 新版 呼出元 1件 [`005dda60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md) [`005df58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.34% / 新版 47.34%

CFGの説明率　旧版 10.62% / 新版 12.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bad74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bad80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bad80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bab00",
      "DATA",
      [
        "storage",
        "002c6ba8",
        "switchD_005bab08::switchdataD_002c6ba8",
        "ushort"
      ]
    ],
    [
      "005df7d8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:005bab64"
      ]
    ],
    [
      "005df7d8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:005bac0c"
      ]
    ]
  ],
  "added": [
    [
      "005df7d0",
      "DATA",
      [
        "storage",
        "002d85d4",
        "switchD_005df7d8::switchdataD_002d85d4",
        "ushort"
      ]
    ],
    [
      "005df7d8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "005df954"
      ]
    ],
    [
      "005df7d8",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "005df8dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md#insn-005bad74) · [`005bad80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md#insn-005bad80) · [`005bad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md#insn-005bad88)

~~~diff
- 005bad74 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 005bad74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:4"]]
- 005bad74 bytes 1a2000b9
- 005bad80 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005bad80 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005bad80 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 005bad80 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 005bad80 bytes 1f7c03a9
- 005bad88 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 005bad88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005bad88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005bad88 bytes 1f1400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3761fcef42a1fe59bbfb7f78fa785f6"></a>

### [`005bafb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md) → [`005dfc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc88.md) FUN_005dfc88

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b8d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8d90.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`00a09c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09c28.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005dda60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dda60.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`00a678f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a678f8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005dfc98",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005bafc8",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005dfc94",
      "incomplete_value": false,
      "site": "005dfc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005bafc4",
      "incomplete_value": false,
      "site": "005bafc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:39d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005dfc94",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "005dfc98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "005dfc94",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005dfc98",
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

- 旧版 [`005bafc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md#insn-005bafc8) · [`005bafc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md#insn-005bafc0) · [`005bafc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafb8.md#insn-005bafc4)
- 新版 [`005dfc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc88.md#insn-005dfc98) · [`005dfc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc88.md#insn-005dfc90) · [`005dfc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc88.md#insn-005dfc94)

~~~diff
- 005bafc8 ["INT_ADD", "register:40f0:8", ["const:5bafc8:8", "const:4:8"]]
- 005bafc8 ["CALL", null, ["ram:41fdf0:8"]]
+ 005dfc98 ["INT_ADD", "register:40f0:8", ["const:5dfc98:8", "const:4:8"]]
+ 005dfc98 ["CALL", null, ["ram:4428f0:8"]]
- 005bafc8 bytes 8a93f997
+ 005dfc98 bytes 168bf997
- 005bafc0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005dfc90 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 005bafc0 bytes 60e7ffb0
+ 005dfc90 bytes c0e6ff90
- 005bafc4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 005bafc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005dfc94 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 005dfc94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005dfc94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005dfc94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005bafc4 bytes 00740e91
+ 005dfc94 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0503eff6343bbba1a1a09bae79c10214"></a>

### [`005bafcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafcc.md) → [`005dfc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc9c.md) _INIT_66

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.27% / 新版 76.27%

CFGの説明率　旧版 41.46% / 新版 40.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005baffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005baffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb008",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005bb010",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005dfccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005dfcd8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005dfce0",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005baffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafcc.md#insn-005baffc) · [`005bb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafcc.md#insn-005bb010) · [`005bb014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005bafcc.md#insn-005bb014)

~~~diff
- 005baffc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005baffc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005baffc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005baffc bytes a9831ff8
- 005bb010 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005bb010 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 005bb010 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005bb010 bytes ea130278
- 005bb014 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 005bb014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005bb014 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b917ebac1f17d45e241b6b2e808d6c5"></a>

### [`005bb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb364.md) → [`005e0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md) FUN_005e0034

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e0044",
      "incomplete_value": true,
      "site": "005e004c",
      "value": [
        "live",
        "register:4008:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e0054",
      "incomplete_value": true,
      "site": "005e0058",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e0060",
      "incomplete_value": true,
      "site": "005e0064",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005bb37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb364.md#insn-005bb37c) · [`005bb388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb364.md#insn-005bb388) · [`005bb394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb364.md#insn-005bb394)
- 新版 [`005e004c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e004c) · [`005e0058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e0058) · [`005e0064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0034.md#insn-005e0064)

~~~diff
- 005bb37c ["INT_ADD", "register:40f0:8", ["const:5bb37c:8", "const:4:8"]]
- 005bb37c ["CALL", null, ["callee:004803b0:8"]]
+ 005e004c ["INT_ADD", "register:40f0:8", ["const:5e004c:8", "const:4:8"]]
+ 005e004c ["CALL", null, ["callee:004803b0:8"]]
- 005bb37c bytes 6788fa97
+ 005e004c bytes d980fa97
- 005bb388 ["INT_ADD", "register:40f0:8", ["const:5bb388:8", "const:4:8"]]
- 005bb388 ["CALL", null, ["callee:004803b0:8"]]
+ 005e0058 ["INT_ADD", "register:40f0:8", ["const:5e0058:8", "const:4:8"]]
+ 005e0058 ["CALL", null, ["callee:004803b0:8"]]
- 005bb388 bytes 6488fa97
+ 005e0058 bytes d680fa97
- 005bb394 ["INT_ADD", "register:40f0:8", ["const:5bb394:8", "const:4:8"]]
- 005bb394 ["CALL", null, ["callee:004803b0:8"]]
+ 005e0064 ["INT_ADD", "register:40f0:8", ["const:5e0064:8", "const:4:8"]]
+ 005e0064 ["CALL", null, ["callee:004803b0:8"]]
- 005bb394 bytes 6188fa97
+ 005e0064 bytes d380fa97
~~~


<a id="compare-afb2dd71a1b8485da3e4871dfcbbae35"></a>

### [`005bb3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3f8.md) → [`005e00c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md) FUN_005e00c8

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bb418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3f8.md#insn-005bb418) · [`005bb424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3f8.md#insn-005bb424) · [`005bb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3f8.md#insn-005bb430)
- 新版 [`005e00e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e00e8) · [`005e00f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e00f4) · [`005e0100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e00c8.md#insn-005e0100)

~~~diff
- 005bb418 ["INT_ADD", "register:40f0:8", ["const:5bb418:8", "const:4:8"]]
- 005bb418 ["CALL", null, ["callee:00480de8:8"]]
+ 005e00e8 ["INT_ADD", "register:40f0:8", ["const:5e00e8:8", "const:4:8"]]
+ 005e00e8 ["CALL", null, ["callee:00480de8:8"]]
- 005bb418 bytes ce8afa97
+ 005e00e8 bytes 4083fa97
- 005bb424 ["INT_ADD", "register:40f0:8", ["const:5bb424:8", "const:4:8"]]
- 005bb424 ["CALL", null, ["callee:00480de8:8"]]
+ 005e00f4 ["INT_ADD", "register:40f0:8", ["const:5e00f4:8", "const:4:8"]]
+ 005e00f4 ["CALL", null, ["callee:00480de8:8"]]
- 005bb424 bytes cb8afa97
+ 005e00f4 bytes 3d83fa97
- 005bb430 ["INT_ADD", "register:40f0:8", ["const:5bb430:8", "const:4:8"]]
- 005bb430 ["CALL", null, ["callee:00480de8:8"]]
+ 005e0100 ["INT_ADD", "register:40f0:8", ["const:5e0100:8", "const:4:8"]]
+ 005e0100 ["CALL", null, ["callee:00480de8:8"]]
- 005bb430 bytes c88afa97
+ 005e0100 bytes 3a83fa97
~~~


<a id="compare-e90bf73fd6800d2d410b85e06d013017"></a>

### [`005bb498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb498.md) → [`005e0168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md) FUN_005e0168

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005bb4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb498.md#insn-005bb4b8) · [`005bb4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb498.md#insn-005bb4c4)
- 新版 [`005e0188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md#insn-005e0188) · [`005e0194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0168.md#insn-005e0194)

~~~diff
- 005bb4b8 ["INT_ADD", "register:40f0:8", ["const:5bb4b8:8", "const:4:8"]]
- 005bb4b8 ["CALL", null, ["callee:00480de8:8"]]
+ 005e0188 ["INT_ADD", "register:40f0:8", ["const:5e0188:8", "const:4:8"]]
+ 005e0188 ["CALL", null, ["callee:00480de8:8"]]
- 005bb4b8 bytes a68afa97
+ 005e0188 bytes 1883fa97
- 005bb4c4 ["INT_ADD", "register:40f0:8", ["const:5bb4c4:8", "const:4:8"]]
- 005bb4c4 ["CALL", null, ["callee:00480de8:8"]]
+ 005e0194 ["INT_ADD", "register:40f0:8", ["const:5e0194:8", "const:4:8"]]
+ 005e0194 ["CALL", null, ["callee:00480de8:8"]]
- 005bb4c4 bytes a38afa97
+ 005e0194 bytes 1583fa97
~~~


<a id="compare-9bc4bfa48843bed9225d000aeffd59a9"></a>

### [`005bb544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb544.md) → [`005e0214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md) FUN_005e0214

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e023c",
      "incomplete_value": true,
      "site": "005e0240",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e0238",
      "incomplete_value": true,
      "site": "005e0240",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005bb570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb544.md#insn-005bb570) · [`005bb564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb544.md#insn-005bb564) · [`005bb57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb544.md#insn-005bb57c)
- 新版 [`005e0240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e0240) · [`005e0234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e0234) · [`005e024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0214.md#insn-005e024c)

~~~diff
- 005bb570 ["INT_ADD", "register:40f0:8", ["const:5bb570:8", "const:4:8"]]
- 005bb570 ["CALL", null, ["callee:00480de8:8"]]
+ 005e0240 ["INT_ADD", "register:40f0:8", ["const:5e0240:8", "const:4:8"]]
+ 005e0240 ["CALL", null, ["callee:00480de8:8"]]
- 005bb570 bytes 788afa97
+ 005e0240 bytes ea82fa97
- 005bb564 ["INT_ADD", "register:40f0:8", ["const:5bb564:8", "const:4:8"]]
- 005bb564 ["CALL", null, ["callee:00480de8:8"]]
+ 005e0234 ["INT_ADD", "register:40f0:8", ["const:5e0234:8", "const:4:8"]]
+ 005e0234 ["CALL", null, ["callee:00480de8:8"]]
- 005bb564 bytes 7b8afa97
+ 005e0234 bytes ed82fa97
- 005bb57c ["INT_ADD", "register:40f0:8", ["const:5bb57c:8", "const:4:8"]]
- 005bb57c ["CALL", null, ["callee:00480de8:8"]]
+ 005e024c ["INT_ADD", "register:40f0:8", ["const:5e024c:8", "const:4:8"]]
+ 005e024c ["CALL", null, ["callee:00480de8:8"]]
- 005bb57c bytes 758afa97
+ 005e024c bytes e782fa97
~~~


<a id="compare-ffab1142c5f9b1335225433827a19561"></a>

### [`005bb610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb610.md) → [`005e02e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e02e0.md) FUN_005e02e0

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 4件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`005bbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bbc90.md)
- 新版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 4件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005e0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.38% / 新版 75.38%

CFGの説明率　旧版 9.09% / 新版 8.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb610"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb610"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb614"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb610",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb614",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb618",
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
      "005e02e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005e02e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e02e8",
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

- 旧版 [`005bb610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb610.md#insn-005bb610) · [`005bb614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb610.md#insn-005bb614) · [`005bb618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb610.md#insn-005bb618)

~~~diff
- 005bb610 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bb610 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bb610 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005bb610 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bb610 bytes fd7bbda9
- 005bb614 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005bb614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 005bb614 bytes f50b00f9
- 005bb618 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bb618 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bb618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005bb618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb618 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21a7385816274e17bcbc33ea9fcf34e"></a>

### [`005bb714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb714.md) → [`005e03e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e03e4.md) FUN_005e03e4

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.37% / 新版 79.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb714"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb714"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb718"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb714",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb718",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb71c",
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
      "005e03e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005e03e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005e03ec",
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

- 旧版 [`005bb714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb714.md#insn-005bb714) · [`005bb718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb714.md#insn-005bb718) · [`005bb71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb714.md#insn-005bb71c)

~~~diff
- 005bb714 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bb714 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bb714 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005bb714 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bb714 bytes fd7bbca9
- 005bb718 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005bb718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005bb718 bytes f70b00f9
- 005bb71c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005bb71c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005bb71c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005bb71c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb71c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3ed06dd2cec358aa987082923253881"></a>

### [`005bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb810.md) → [`005e04e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e04e0.md) _INIT_67

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.97% / 新版 77.97%

CFGの説明率　旧版 29.79% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb854"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb858"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb840",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb84c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005bb854",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005e0510",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005e051c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005e0524",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb810.md#insn-005bb840) · [`005bb854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb810.md#insn-005bb854) · [`005bb858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb810.md#insn-005bb858)

~~~diff
- 005bb840 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005bb840 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005bb840 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005bb840 bytes a9831ff8
- 005bb854 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005bb854 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 005bb854 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005bb854 bytes ea130278
- 005bb858 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 005bb858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005bb858 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0892ac9503b41db239525e58175ecaa"></a>

### [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) → [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) FUN_005e0eac

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 13件 [`005c2ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md) [`006453ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006453ac.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005bc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc280.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 14件 [`005e7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md) [`0066b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) · 呼出先 2件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bc1f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bc1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bc230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005bc280"
      ]
    ]
  ],
  "added": [
    [
      "005e0ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e0ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005e0f00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e0f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bc1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md#insn-005bc1ec) · [`005bc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md#insn-005bc1f0) · [`005bc218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md#insn-005bc218)

~~~diff
- 005bc1ec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005bc1ec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005bc1ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005bc1ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc1ec bytes f65704a9
- 005bc1f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bc1f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bc1f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005bc1f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bc1f0 bytes f44f05a9
- 005bc218 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 005bc218 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005bc218 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 005bc218 ["INT_ZEXT", "register:40c0:8", ["tmp:0:4"]]
- 005bc218 bytes 3801881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

